# dashapp/components/plots/overview_plots.py
import plotly.express as px
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

    # Filter by year if selected_year is provided
    if selected_year:
        df = df[df["year"] == int(selected_year)]

    # Convert 'date' to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Ignore NaN values and filter
    df_filtered = df[df[metric] > 0].dropna(subset=[metric])

    # Resample by month and calculate mean
    monthly_average = (
        df_filtered[metric].resample("ME").mean().reset_index()
    )  # 'ME' for month end
    monthly_average.rename(columns={"date": "Month", metric: metric}, inplace=True)

    # Filter out months if average == 0
    monthly_average = monthly_average[monthly_average[metric] > 0]

    fig = px.line(
        monthly_average,
        x="Month",
        y=metric,
        labels={"Month": "", metric: ""},
        markers=True,
        color_discrete_sequence=[SPORT_TYPE_COLORS.get(sport_type.capitalize())],
    )

    # Tick values
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
        ),
    )

    # Apply plot styles
    fig = apply_plot_styles(fig, LINE_CHART_PLOT_STYLE)

    return fig
