# dashapp/components/plots/overview_plots.py
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd


from assets.utils import ALL_MONTHS, CURRENT_YEAR
from dashapp.components.plots.plot_styles import (
    apply_plot_styles,
    SPORT_TYPE_COLORS,
    LINE_CHART_PLOT_STYLE,
)


def get_average_metric_line_chart(
    df: pd.DataFrame, metric: str, sport_type: str, selected_year=None
):
    """Line Chart - Average data for selected metric and sport, filtered by year"""
    df = df.copy()

    # Convert 'date' to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True, drop=False)

    # Filter by year if selected_year is provided
    if selected_year:
        df = df[df["year"] == int(selected_year)]

    # Filter by sport_type
    df_filtered = df[df["sport_type"] == sport_type]

    # Ignore NaN values and filter for positive metric values
    df_filtered = df_filtered[df_filtered[metric] > 0].dropna(subset=[metric])

    # Resample by month and calculate mean
    monthly_average = df_filtered[metric].resample("ME").mean().reset_index()
    monthly_average.rename(columns={"date": "Month", metric: metric}, inplace=True)

    # Filter out months if average == 0
    monthly_average = monthly_average[monthly_average[metric] > 0]

    # Create the figure
    fig = px.line(
        monthly_average,
        x="Month",
        y=metric,
        labels={"Month": "", metric: ""},
        markers=True,
        color_discrete_sequence=[SPORT_TYPE_COLORS.get(sport_type.capitalize())],
    )

    # Format tick values
    tickvals = monthly_average["Month"]
    ticktext = [date.strftime("%b.%y") for date in tickvals]

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        width=385,
        height=220,
        xaxis=dict(
            tickvals=tickvals,
            ticktext=ticktext,
            tickangle=-45,
            tickmode="array",
            showgrid=False
        ),
        yaxis=dict(
            showgrid=False
        )
    )

    # Apply plot styles
    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig


def get_comparison_chart(
    df: pd.DataFrame, metric_1: str, metric_2: str, sport_type: str, selected_year=None
):
    # Convert 'date' to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True, drop=False)

    # Filter by year if selected_year is provided
    if selected_year:
        df = df[df["year"] == int(selected_year)].copy()

    # Filter by sport_type
    df_filtered = df[df["sport_type"] == sport_type].copy()

    # Filter and clean data for both metrics
    df_filtered_1 = df_filtered.loc[df_filtered[metric_1] > 0].dropna(subset=[metric_1])
    df_filtered_2 = df_filtered.loc[df_filtered[metric_2] > 0].dropna(subset=[metric_2])

    # Resample by month and calculate mean for both metrics
    monthly_average_1 = df_filtered_1[metric_1].resample("ME").mean().reset_index()
    monthly_average_2 = df_filtered_2[metric_2].resample("ME").mean().reset_index()

    # Rename the date columns
    monthly_average_1.rename(
        columns={"date": "Month", metric_1: metric_1}, inplace=True
    )
    monthly_average_2.rename(
        columns={"date": "Month", metric_2: metric_2}, inplace=True
    )

    # Filter out months where averages are 0
    monthly_average_1 = monthly_average_1[monthly_average_1[metric_1] > 0]
    monthly_average_2 = monthly_average_2[monthly_average_2[metric_2] > 0]

    # Create a figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add the first metric line
    fig.add_trace(
        go.Scatter(
            x=monthly_average_1["Month"],
            y=monthly_average_1[metric_1],
            name=metric_1,
            mode="lines+markers",
            line=dict(color=SPORT_TYPE_COLORS.get(sport_type.capitalize())),
        ),
        secondary_y=False,
    )

    # Add the second metric line
    fig.add_trace(
        go.Scatter(
            x=monthly_average_2["Month"],
            y=monthly_average_2[metric_2],
            name=metric_2,
            mode="lines+markers",
            line=dict(color="#fd7f6f"),
        ), 
        secondary_y=True,
    )

    # Format tick values
    tickvals = monthly_average_1["Month"]
    ticktext = [date.strftime("%b.%y") for date in tickvals]

    # Update layout with both y-axes
    fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    width=700,
    height=450,
    xaxis=dict(
        tickvals=tickvals,
        ticktext=ticktext,
        tickangle=-45,
        tickmode="array",
        showgrid=False  
    ),
    yaxis=dict(
        title=None,
        showgrid=False  
    ),
    yaxis2=dict(
        title=None,
        overlaying="y",
        side="right",
        showgrid=False  
    )
)


    # Apply plot styles
    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig
