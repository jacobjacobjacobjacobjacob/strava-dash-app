# dashapp/components/plots/goal_plots.py
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from assets.utils import ALL_MONTHS, CURRENT_MONTH
from dashapp.components.plots.plot_styles import (
    apply_plot_styles,
    SPORT_TYPE_COLORS,
    LINE_CHART_PLOT_STYLE,
)
from modules.goals import get_goal_dataframes


def get_distance_goal_chart(df: pd.DataFrame, current_month: str):
    """Line Chart - Actual vs. Goal Distance by Month"""

    # Create the figure object
    fig = go.Figure()

    # Determine the index for the current month
    current_month_index = df[df["month"] == current_month].index[0] + 1

    # Add actual distance line
    fig.add_trace(
        go.Scatter(
            x=df["month"][
                :current_month_index
            ],  # Slice to include only up to current month
            y=df["distance"][:current_month_index],
            mode="lines",
            name="Actual",
            line=dict(color="green"),
            marker=dict(color="green", size=10),
        )
    )

    # Add goal distance line
    fig.add_trace(
        go.Scatter(
            x=df["month"],  # Use the full range for the goal line
            y=df["goal_distance"],
            mode="lines",
            name="Goal",
            line=dict(color="gray", dash="dash"),
        )
    )

    # Customize layout
    fig.update_layout(
        title="Distance",
        xaxis_title="Month",
        yaxis_title=dict(
            text="Distance (km)",
            font=dict(size=16),  # Increase the y-axis title font size
        ),
        legend_title="Legend",
        xaxis=dict(
            tickmode="array",
            tickvals=df["month"],
            ticktext=df["month"],
        ),
        yaxis=dict(tickmode="linear", tick0=0, dtick=300),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        width=570,
        height=300,
    )

    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig


def get_duration_goal_chart(df: pd.DataFrame, current_month: str):
    """Line Chart - Actual vs. Goal Distance by Month"""

    # Create the figure object
    fig = go.Figure()

    # Determine the index for the current month
    current_month_index = df[df["month"] == current_month].index[0] + 1

    # Add actual distance line
    fig.add_trace(
        go.Scatter(
            x=df["month"][
                :current_month_index
            ],  # Slice to include only up to current month
            y=df["duration"][:current_month_index],
            mode="lines",
            name="Actual",
            line=dict(color="green"),
            marker=dict(color="green", size=10),
        )
    )

    # Add goal distance line
    fig.add_trace(
        go.Scatter(
            x=df["month"],  # Use the full range for the goal line
            y=df["goal_duration"],
            mode="lines",
            name="Goal",
            line=dict(color="gray", dash="dash"),
        )
    )

    # Customize layout
    fig.update_layout(
        title="Duration",
        xaxis_title="Month",
        yaxis_title=dict(
            text="Duration (h)",
            font=dict(size=16),  # Increase the y-axis title font size
        ),
        legend_title="Legend",
        xaxis=dict(
            tickmode="array",
            tickvals=df["month"],
            ticktext=df["month"],
        ),
        yaxis=dict(tickmode="linear", tick0=0, dtick=300),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        width=570,
        height=300,
    )

    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig
