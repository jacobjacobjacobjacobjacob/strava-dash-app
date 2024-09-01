# modules/goals.py
import pandas as pd
from assets.utils import ALL_MONTHS
from assets.config import (
    BIKE_DURATION_GOAL_2024,
    BIKE_DISTANCE_GOAL_2024,
    RUN_DURATION_GOAL_2024,
    RUN_DISTANCE_GOAL_2024,
)

"""
Script to generate DataFrames to plot progression towards different goals
"""


def get_yearly_goal_data(
    df: pd.DataFrame, sport_type: str, goal_type: str, goal_value: int, year: int
) -> pd.DataFrame:
    # Ensure date parsing
    df["date"] = pd.to_datetime(df["date"])
    goal_type = goal_type.lower()

    # Filter data by the specified year
    df_filtered = df[df["date"].dt.year == year].copy()

    # Create 'month_dt' column with the specified year
    df_filtered["month_dt"] = pd.to_datetime(
        df_filtered["month"] + f" {year}", format="%b %Y"
    )

    # Filter by sport_type and sort data
    filtered_df = df_filtered[df_filtered["sport_type"] == sport_type].copy()
    filtered_df = filtered_df.sort_values(by=["date"])

    # Calculate cumulative sum
    filtered_df[goal_type] = filtered_df[goal_type].cumsum()

    # Aggregate to get cumulative sum at the end of each month
    result_df = filtered_df.groupby("month_dt").agg({goal_type: "max"}).reset_index()

    # Convert 'month_dt' to month names
    result_df["month"] = result_df["month_dt"].dt.strftime("%b")

    # Ensure month ordering
    result_df["month"] = pd.Categorical(
        result_df["month"], categories=ALL_MONTHS, ordered=True
    )
    result_df = result_df.sort_values(by="month").reset_index(drop=True)

    # Drop intermediate columns
    result_df = result_df.drop(columns=["month_dt"])

    monthly_goal = goal_value / len(result_df)
    result_df[f"goal_{goal_type}"] = (result_df.index + 1) * monthly_goal

    # Merge
    all_months_df = pd.DataFrame({"month": ALL_MONTHS})
    full_df = all_months_df.merge(result_df, on="month", how="left").fillna(0)
    full_df[f"goal_{goal_type}"] = (
        full_df[f"goal_{goal_type}"].max() / len(full_df) * (full_df.index + 1)
    )

    return full_df


def get_goal_dataframes(df) -> pd.DataFrame:
    """
    Generate DataFrames for plotting goals

    :param df (pd.DataFrame): The DataFrame containing Strava data.

    :return: Dataframes for distance and duration goals for cycling and running.
    """
    df_bike_duration_goal_2024 = get_yearly_goal_data(
        df,
        sport_type="Bike",
        goal_type="Duration",
        goal_value=BIKE_DURATION_GOAL_2024,
        year=2024,
    )
    df_bike_distance_goal_2024 = get_yearly_goal_data(
        df,
        sport_type="Bike",
        goal_type="Distance",
        goal_value=BIKE_DISTANCE_GOAL_2024,
        year=2024,
    )
    df_run_duration_goal_2024 = get_yearly_goal_data(
        df,
        sport_type="Run",
        goal_type="Duration",
        goal_value=RUN_DURATION_GOAL_2024,
        year=2024,
    )
    df_run_distance_goal_2024 = get_yearly_goal_data(
        df,
        sport_type="Run",
        goal_type="Distance",
        goal_value=RUN_DISTANCE_GOAL_2024,
        year=2024,
    )

    return (
        df_bike_duration_goal_2024,
        df_bike_distance_goal_2024,
        df_run_duration_goal_2024,
        df_run_distance_goal_2024,
    )
