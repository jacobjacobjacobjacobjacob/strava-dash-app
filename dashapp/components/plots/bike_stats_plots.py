# dashapp/components/plots/overview_plots.py
import plotly.express as px
import pandas as pd

from assets.utils import ALL_MONTHS, CURRENT_YEAR
from dashapp.components.plots.plot_styles import (
    apply_plot_styles,
    SPORT_TYPE_COLORS,
    PIE_CHART_PLOT_STYLE,
    SCATTER_CHART_PLOT_STYLE,
    POLAR_CHART_PLOT_STYLE,
    LINE_CHART_PLOT_STYLE,
)


def get_bike_stats_average_speed_line_chart(df: pd.DataFrame, selected_year=None):
    """Line Chart - Average Speed by Month, filtered by year"""
    df = df.copy()

    # Filter by year if selected_year is provided
    if selected_year:
        df = df[df["year"] == int(selected_year)]

    # Convert 'date' to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Ignore NaN values and filter
    df_filtered = df[df["average_speed"] > 0].dropna(subset=["average_speed"])

    # Resample by month and calculate mean
    monthly_average_speed = (
        df_filtered["average_speed"].resample("ME").mean().reset_index()
    )  # 'MS' for month start
    monthly_average_speed.rename(
        columns={"date": "Month", "average_speed": "Average Speed"}, inplace=True
    )

    # Filter out months if average == 0
    monthly_average_speed = monthly_average_speed[
        monthly_average_speed["Average Speed"] > 0
    ]

    # Create the figure using Plotly Express
    fig = px.line(
        monthly_average_speed,
        x="Month",
        y="Average Speed",
        labels={"Month": "", "Average Speed": ""},
        markers=True,
        color_discrete_sequence=[SPORT_TYPE_COLORS.get("Bike")],
    )

    # Tick values
    tickvals = monthly_average_speed["Month"]
    ticktext = [date.strftime("%m.%y") for date in tickvals]

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        width=385,
        height=220,
        xaxis=dict(
            ticktext=ticktext,
            tickvals=tickvals,
            tickformat="%b %y",
            tickangle=-45,
            tickmode="auto",
        ),
    )

    # Apply plot styles
    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig


def get_average_line_chart(
    df: pd.DataFrame,
    selected_year=None,
):
    """Line Chart - Average Speed by Month, filtered by year"""
    df = df.copy()

    # Filter by year if selected_year is provided
    if selected_year:
        df = df[df["year"] == int(selected_year)]

    # Convert 'date' to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Ignore NaN values and filter
    df_filtered = df[df["average_speed"] > 0].dropna(subset=["average_speed"])

    # Resample by month and calculate mean
    monthly_average_speed = (
        df_filtered["average_speed"].resample("ME").mean().reset_index()
    )  # 'MS' for month start
    monthly_average_speed.rename(
        columns={"date": "Month", "average_speed": "Average Speed"}, inplace=True
    )

    # Filter out months if average == 0
    monthly_average_speed = monthly_average_speed[
        monthly_average_speed["Average Speed"] > 0
    ]

    # Create the figure using Plotly Express
    fig = px.line(
        monthly_average_speed,
        x="Month",
        y="Average Speed",
        labels={"Month": "", "Average Speed": ""},
        markers=True,
        color_discrete_sequence=[SPORT_TYPE_COLORS.get("Bike")],
    )

    # Tick values
    tickvals = monthly_average_speed["Month"]
    ticktext = [date.strftime("%m.%y") for date in tickvals]

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        width=385,
        height=220,
        xaxis=dict(
            ticktext=ticktext,
            tickvals=tickvals,
            tickformat="%b %y",
            tickangle=-45,
            tickmode="auto",
        ),
    )

    # Apply plot styles
    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig
