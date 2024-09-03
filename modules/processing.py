# modules/processing.py
import pandas as pd
import logging


from assets.utils import (
    m_to_km,
    ms_to_kph,
    sec_to_h,
)
from assets.health_data import resting_hr, max_hr, weight_kg, stride_length
from assets.config import local_tz, ignored_tzs, setup_logging

setup_logging()
logger = logging.getLogger(__name__)


"""
This module processes Strava activity data to extract, clean, and analyze relevant information.

The main tasks performed by this module include:

1. **Reading Raw Data**: Importing raw activity data from a CSV file.
2. **Filtering Data**: Applying filters based on activity type and date range to focus on relevant entries.
3. **Metric Conversion**: Converting raw metrics (e.g., distance, speed, duration) into more user-friendly formats.
4. **Data Compilation**: Organizing and compiling the cleaned data into structured DataFrames for further analysis or reporting.

This module ensures that Strava data is processed efficiently, providing clean and actionable insights.
"""


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns for readability and clarity.

    :param df: The DataFrame containing Strava data.
    :type df: pd.DataFrame
    :return: DataFrame with renamed columns.
    :rtype: pd.DataFrame
    """
    rename_mapping = {
        "trainer": "environment",
        "start_date": "date",
        "moving_time": "duration",
        "total_elevation_gain": "elevation_gain",
    }
    df.rename(columns=rename_mapping, inplace=True)

    return df


def filter_by_timezone(df: pd.DataFrame, excluded_timezones: list) -> pd.DataFrame:
    """
    Filter out activities from specific time zones.

    :param df: The DataFrame containing activities.
    :param excluded_timezones: List of time zones to exclude.
    :return: DataFrame filtered by excluding rides in specified time zones.
    :rtype: pd.DataFrame
    """

    # Filter out rows with specified time zones and sport type 'ride'
    df_filtered = df[~df["timezone"].isin(excluded_timezones)]

    return df_filtered


def filter_by_period(
    df: pd.DataFrame,
    start_date: str = None,
    end_date: str = None,
    year: int = None,
    month: int = None,
) -> pd.DataFrame:
    """
    Filter DataFrame by time parameters.

    :param df: The DataFrame containing data with a 'date' column.
    :param start_date: Start date in 'YYYY-MM-DD' format (optional).
    :param end_date: End date in 'YYYY-MM-DD' format (optional).
    :param year: Year to filter by (optional).
    :param month: Month to filter by (optional).
    :return: DataFrame filtered by given period.
    :rtype: pd.DataFrame
    """
    df = df.sort_values(by="date", ascending=True)

    if start_date:
        try:
            start_date = pd.to_datetime(start_date)
            df = df[df["date"] >= start_date]
        except ValueError:
            raise ValueError(f"Invalid start_date format: {start_date}")

    if end_date:
        try:
            end_date = pd.to_datetime(end_date)
            df = df[df["date"] <= end_date]
        except ValueError:
            raise ValueError(f"Invalid end_date format: {end_date}")

    if year:
        df = df[df["date"].dt.year >= year]

    if month:
        df = df[df["date"].dt.month == month]

    return df


def convert_units(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert units (distance, speed etc.) and formats date to datetime.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with converted units.
    """

    if "distance" in df.columns:
        df["distance"] = df["distance"].apply(m_to_km)
    if "duration" in df.columns:
        df["duration"] = df["duration"].apply(sec_to_h)
    if "average_speed" in df.columns:
        df["average_speed"] = df["average_speed"].apply(ms_to_kph)
    if "max_speed" in df.columns:
        df["max_speed"] = df["max_speed"].apply(ms_to_kph)

    return df


def convert_datatypes(df: pd.DataFrame) -> pd.DataFrame:
    # Convert to datetime-format.
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df


def filter_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame to only keep the specified columns.

    :param cleaned_df: The DataFrame containing cleaned Strava data.
    :type cleaned_df: pd.DataFrame
    :return: Filtered DataFrame with desired columns.
    :rtype: pd.DataFrame
    """
    columns = [
        "id",
        "date",
        "year",
        "month",
        "day_of_week",
        "start_time",
        "end_time",
        "duration",
        "distance",
        "elevation_gain",
        "average_speed",
        "max_speed",
        "average_heartrate",
        "max_heartrate",
        "suffer_score",
        "suffer_score_bucket",
        "elevation_rate",
        "average_watts",
        "average_cadence",
        "pace",
        "spm",
        "vo2_max",
        "sport_type",
        "environment",
    ]

    df = df[columns].copy()
    return df


def add_year_month_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add "month" and "year" columns to the DataFrame.

    :param df: The DataFrame containing Strava data.e
    :return: DataFrame with "month" and "year" columns added.
    :rtype: pd.DataFrame
    """

    df["month"] = df["date"].dt.month_name().str.slice(stop=3).str.lower()
    df["year"] = df["date"].dt.year
    return df


def add_day_of_week(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add "day_of_week"-column to the DataFrame.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with "day_of_week"-column added.
    """

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    df["day_of_week"] = df["date"].dt.weekday.map(lambda x: weekdays[x])
    return df


def add_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Converts the "date"-column to the specified local timezone.
    - Add "start_time" and "end_time" columns based on duration.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with "start_time" and "end_time" columns added.
    """

    # Check if date column is timezone-aware
    if df["date"].dt.tz is None:
        # Localize to UTC
        df["date"] = df["date"].dt.tz_localize("UTC")

    # Convert to local timezone
    df["date"] = df["date"].dt.tz_convert(local_tz)

    # Calculate end_time based on duration
    df["end_time"] = df["date"] + pd.to_timedelta(df["duration"], unit="h")

    df["start_time"] = df["date"].dt.strftime("%H:%M")
    df["end_time"] = df["end_time"].dt.strftime("%H:%M")

    return df


def add_elevation_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add "elevation_rate"-column (elevation gained per kilometer).

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with "elevation_rate"-column added.
    """
    df["elevation_rate"] = df.apply(
        lambda row: (
            (row["elevation_gain"] / row["distance"]) if row["distance"] > 0 else 0
        ),
        axis=1,
    )
    return df


def sort_and_reset_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort DataFrame by 'date' column and reset index.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: Sorted and reindexed DataFrame.
    """

    df = df.sort_values(by="date")

    df.reset_index(drop=True, inplace=True)
    df.index += 1  # Shift index to start from 1

    return df


def update_environment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Update the 'environment' column to 'indoor' if its value is True,
    and 'outdoor' if its value is False.

    :param df: The DataFrame containing activity data with a boolean 'environment' column.
    :return: Updated DataFrame with 'environment' adjusted to 'indoor' or 'outdoor'.
    :rtype: pd.DataFrame
    """

    df["environment"] = df["environment"].apply(lambda x: "indoor" if x else "outdoor")

    return df


def replace_nan_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace NaN values with the mean for columns with missing heart rate data.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with NaN values replaced.
    """
    columns_to_fill = ["max_heartrate", "average_heartrate", "suffer_score"]

    for column in columns_to_fill:
        if column in df.columns:
            mean_value = df[column].mean()
            df[column] = df[column].fillna(mean_value)

    return df


def add_suffer_score_buckets(df: pd.DataFrame, num_bins: int = 3) -> pd.DataFrame:
    """
    Categorize the 'suffer_score' column into discrete buckets.

    This function creates a new column 'suffer_score_bucket' in the DataFrame,
    categorizing the 'suffer_score' into quantile-based buckets with labels
    such as "very low", "low", "medium", "high", and "very high".

    :param df: The DataFrame containing the 'suffer_score' column.
    :type df: pd.DataFrame
    :param num_bins: The number of quantile bins to create. Default is 5.
    :type num_bins: int
    :return: DataFrame with an additional 'suffer_score_bucket' column.
    :rtype: pd.DataFrame
    """
    labels = ["low", "medium", "high"]
    df["suffer_score_bucket"] = pd.qcut(
        df["suffer_score"], q=num_bins, labels=labels[:num_bins]
    )
    return df


def remove_short_rides(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rides under 10 km from the DataFrame.

    :param
        df (pd.DataFrame): The DataFrame containing Strava data.

    :returns
        pd.DataFrame: DataFrame with short rides removed.
    """
    if "sport_type" in df.columns and "environment" in df.columns:
        df = df.drop(
            df[
                (df["environment"] == "outdoor")
                & (df["sport_type"] == "bike")
                & (df["distance"] < 10)
            ].index
        )
    return df


def calculate_vo2_max(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the VO2 max for each activity in the DataFrame.
    :param
        df (pd.DataFrame): The DataFrame containing Strava data.
    :return:
        pd.DataFrame: DataFrame with Vo2-max estimates added.
    """

    # Convert dictionary to DataFrame
    resting_hr_df = pd.DataFrame(
        list(resting_hr.items()), columns=["year_month", "average_resting_hr"]
    )
    resting_hr_df["year_month"] = pd.to_datetime(
        resting_hr_df["year_month"] + "-01"
    ).dt.to_period("M")

    if df["date"].dt.tz is None:
        df["date"] = df["date"].dt.tz_localize("UTC")

    # Extract Year-Month to match the "resting_hr" data
    df["year_month"] = df["date"].dt.tz_convert(None).dt.to_period("M")

    # Merge resting HR data with the original DataFrame
    df = df.merge(resting_hr_df, on="year_month", how="left")

    # Calculate VO2 max using vectorized operations
    df["vo2_max"] = (df["average_watts"] * 10.8 / weight_kg) + (
        7 * (max_hr / df["average_resting_hr"])
    )

    # Round data and drop the helper columns
    df["vo2_max"] = df["vo2_max"].round(2)
    df.drop(columns=["average_resting_hr", "year_month"], inplace=True)

    return df


def calculate_running_cadence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add SPM (steps per minute) to runs.

    :param df (pd.DataFrame): The DataFrame containing Strava data.
    :return: pd.DataFrame: DataFrame with running cadence (SPM) added.
    """

    df["spm"] = None
    df.loc[df["sport_type"] == "Run", "spm"] = (
        df["distance"] * 1000 / stride_length
    ) / (df["duration"] * 60)

    return df


def calculate_pace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate pace (minutes per kilometer)

    :param df (pd.DataFrame): The DataFrame containing Strava data.

    :return: pd.DataFrame: DataFrame with pace.
    """
    df["pace"] = df.apply(
        lambda row: (
            (row["duration"] * 60 / row["distance"]) if row["distance"] > 0 else 0
        ),
        axis=1,
    )

    return df


def capitalize_all_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Capitalize all strings

    :param df (pd.DataFrame): The DataFrame containing Strava data.

    :return: pd.DataFrame: DataFrame with all strings capitalized.
    """
    df = df.map(lambda x: x.capitalize() if isinstance(x, str) else x)
    return df


def rename_sport_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df (pd.DataFrame): The DataFrame containing Strava data.
    :return: pd.DataFrame: DataFrame with renamed sport types.
    """
    # Use .loc to avoid SettingWithCopyWarning
    df.loc[:, "sport_type"] = df["sport_type"].replace({"Ride": "Bike", "Hike": "Walk"})

    # Remove unwanted sport types
    df = df[~df["sport_type"].isin(["Swims", "Rowing"])]
    return df


def convert_date_to_yyyymmdd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'date' column to format YYYY-MM-DD.

    :param
        df (pd.DataFrame): DataFrame with a 'date' column.

    :return
        pd.DataFrame: DataFrame with 'date' column converted to YYYY-MM-DD format.
    """

    df["date"] = df["date"].dt.date
    return df


def add_average_running_speed(df: pd.DataFrame) -> pd.DataFrame:
    """
    Manually add average speed to running activities, Strava only registers "pace", not kph.

    :param df: DataFrame with average speed for running activities.
    :return: DataFrame with running speed added.
    """

    # Calculate average speed (distance / duration) for running activities only
    df["average_speed"] = df.apply(
        lambda row: (
            row["distance"] / row["duration"]
            if row["sport_type"] == "Run" and row["duration"] > 0
            else row[
                "average_speed"
            ]  # Preserve existing speed for non-running activities
        ),
        axis=1,
    )

    return df


def clean_data(df):
    try:
        clean_df = (
            df.pipe(rename_columns)
            .pipe(filter_by_timezone, ignored_tzs)
            .pipe(rename_sport_types)
            .pipe(convert_units)
            .pipe(convert_datatypes)
            .pipe(filter_by_period, year=2023)
            .pipe(add_year_month_column)
            .pipe(add_day_of_week)
            .pipe(add_time_columns)
            .pipe(add_elevation_rate)
            .pipe(add_suffer_score_buckets)
            .pipe(calculate_vo2_max)
            .pipe(calculate_pace)
            .pipe(calculate_running_cadence)
            .pipe(add_average_running_speed)
            .pipe(update_environment)
            .pipe(replace_nan_values)
            .pipe(filter_columns)
            .pipe(convert_date_to_yyyymmdd)
            .pipe(capitalize_all_strings)
            .pipe(sort_and_reset_index)
        )

    except Exception as e:
        logger.error(f"Error during DataFrame cleaning: {e}")
        raise

    return clean_df
