# dashapp/components/plots/overview_plots.py
import plotly.express as px
import pandas as pd

from assets.utils import ALL_MONTHS
from dashapp.components.plots.plot_styles import (
    apply_plot_styles,
    SPORT_TYPE_COLORS,
    BAR_CHART_PLOT_STYLE,
    PIE_CHART_PLOT_STYLE,
    SCATTER_CHART_PLOT_STYLE,
    POLAR_CHART_PLOT_STYLE,
)


def get_overview_duration_bar_chart(df: pd.DataFrame, selected_months: list):
    """Bar Chart - Total Duration by Month"""
    df = df.copy()

    # Sort and filter selected months
    selected_months = [month.capitalize() for month in selected_months]
    valid_months = [month for month in selected_months if month in ALL_MONTHS]
    selected_months_sorted = sorted(valid_months, key=lambda x: ALL_MONTHS.index(x))

    # Aggregate data
    df_aggregated = df.groupby(["month", "sport_type"], as_index=False).agg(
        {"duration": "sum"}
    )

    # Sort by month
    df_aggregated["month"] = pd.Categorical(
        df_aggregated["month"], categories=selected_months_sorted, ordered=True
    )
    df_aggregated = df_aggregated.sort_values("month")

    fig = px.bar(
        df_aggregated,
        x="month",
        y="duration",
        color="sport_type",
        labels={"duration": "", "month": ""},
        category_orders={
            "month": selected_months_sorted
        },  # Only use sorted selected months
        color_discrete_map=SPORT_TYPE_COLORS,
    )

    # Calculate totals for each month
    monthly_totals = (
        df_aggregated.groupby("month", observed=False)["duration"].sum().reset_index()
    )
    monthly_totals = monthly_totals[
        monthly_totals["duration"] > 0
    ]  # Exclude zero values
    monthly_totals["text"] = (
        monthly_totals["duration"].astype(int).astype(str)
    )  # Format as integers

    # Add annotations for each month
    for _, row in monthly_totals.iterrows():
        fig.add_annotation(
            x=row["month"],
            y=row["duration"],
            text=row["text"],
            showarrow=False,
            yshift=15,
            font=dict(size=12, color="black"),
            align="center",
        )

    # Size
    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        width=450,
        height=250,
    )

    # Apply centralized style configuration
    fig = apply_plot_styles(fig, BAR_CHART_PLOT_STYLE)

    return fig


def get_overview_distance_bar_chart(df: pd.DataFrame, selected_months: list):
    """Bar Chart - Total Distance by Month"""
    df = df.copy()

    # Sort and filter selected months
    selected_months = [month.capitalize() for month in selected_months]
    valid_months = [month for month in selected_months if month in ALL_MONTHS]
    selected_months_sorted = sorted(valid_months, key=lambda x: ALL_MONTHS.index(x))

    # Aggregate data
    df_aggregated = df.groupby(["month", "sport_type"], as_index=False).agg(
        {"distance": "sum"}
    )

    # Sort by month
    df_aggregated["month"] = pd.Categorical(
        df_aggregated["month"], categories=selected_months_sorted, ordered=True
    )
    df_aggregated = df_aggregated.sort_values("month")

    fig = px.bar(
        df_aggregated,
        x="month",
        y="distance",
        color="sport_type",
        labels={"distance": "", "month": ""},
        category_orders={
            "month": selected_months_sorted
        },  # Only use sorted selected months
        color_discrete_map=SPORT_TYPE_COLORS,
    )

    # Calculate totals for each month
    monthly_totals = (
        df_aggregated.groupby("month", observed=False)["distance"].sum().reset_index()
    )
    monthly_totals = monthly_totals[
        monthly_totals["distance"] > 0
    ]  # Exclude zero values
    monthly_totals["text"] = (
        monthly_totals["distance"].astype(int).astype(str)
    )  # Format as integers

    # Add annotations for each month
    for _, row in monthly_totals.iterrows():
        fig.add_annotation(
            x=row["month"],
            y=row["distance"],
            text=row["text"],
            showarrow=False,
            yshift=15,
            font=dict(size=12, color="black"),
            align="center",
        )

    # Size
    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        width=450,
        height=250,
    )

    # Apply centralized style configuration
    fig = apply_plot_styles(fig, BAR_CHART_PLOT_STYLE)

    return fig


def get_overview_activity_count_pie_chart(df: pd.DataFrame, selected_months: list):
    df = df.copy()

    # Aggregate data
    df_aggregated = df.groupby("sport_type").size().reset_index(name="count")

    # Ensure all sports types are present in the color map
    for sport_type in SPORT_TYPE_COLORS.keys():
        if sport_type not in df_aggregated["sport_type"].values:
            df_aggregated = pd.concat(
                [
                    df_aggregated,
                    pd.DataFrame([[sport_type, 0]], columns=["sport_type", "count"]),
                ]
            )

    # Create pie chart
    fig = px.pie(
        df_aggregated,
        names="sport_type",
        values="count",
        labels={"count": "Activity Count", "sport_type": "Sport Type"},
        color_discrete_map=SPORT_TYPE_COLORS,
    )

    # Manually set colors if needed
    fig.update_traces(
        textinfo="label+value",
        textposition="inside",
        hole=0.3,
        marker=dict(
            colors=[SPORT_TYPE_COLORS.get(s) for s in df_aggregated["sport_type"]]
        ),
    )
    # Size
    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0), width=300, height=220, showlegend=False
    )

    # Apply centralized style configuration
    fig = apply_plot_styles(fig, PIE_CHART_PLOT_STYLE)

    return fig


def get_overview_effort_scatter_chart(df: pd.DataFrame, selected_months: list):
    """Area Chart - Total Effort by Month"""
    df = df.copy()

    # Sort and filter selected months
    selected_months = [month.capitalize() for month in selected_months]
    valid_months = [month for month in selected_months if month in ALL_MONTHS]
    selected_months_sorted = sorted(valid_months, key=lambda x: ALL_MONTHS.index(x))

    # Aggregate data
    df_aggregated = df.groupby(["month", "sport_type"], as_index=False).agg(
        {"suffer_score": "sum"}
    )

    # Sort by month
    df_aggregated["month"] = pd.Categorical(
        df_aggregated["month"], categories=selected_months_sorted, ordered=True
    )
    df_aggregated = df_aggregated.sort_values("month")

    fig = px.scatter(
        df_aggregated,
        x="month",
        y="suffer_score",
        size="suffer_score",
        color="sport_type",
        labels={"suffer_score": "", "month": ""},
        category_orders={
            "month": selected_months_sorted
        },  # Only use sorted selected months
        color_discrete_map=SPORT_TYPE_COLORS,
    )

    fig.update_traces(marker=dict(opacity=1))  # Full opacity

    # Size
    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        width=300,
        height=220,
    )

    # Apply centralized style configuration
    fig = apply_plot_styles(fig, SCATTER_CHART_PLOT_STYLE)

    return fig


def get_overview_polar_chart_count_by_day(df: pd.DataFrame, selected_months: list):
    df = df.copy()

    # Convert 'date' to datetime and extract relevant parts
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.strftime("%b")  # Get full month name
    df["day_of_week"] = df["date"].dt.strftime("%a")  # Get abbreviated day name

    if selected_months:
        selected_months = [month.capitalize() for month in selected_months]
        df = df[df["month"].isin(selected_months)]

    df_grouped = df.groupby("day_of_week").size().reset_index(name="count")

    # Define weekdays to account for months where not all days are present
    all_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Ensure correct day ordering
    df_grouped["day_of_week"] = pd.Categorical(
        df_grouped["day_of_week"], categories=all_days, ordered=True
    )
    df_grouped = df_grouped.sort_values("day_of_week")

    # Reindex with all days and fill missing with zeros
    df_grouped = (
        df_grouped.set_index("day_of_week")
        .reindex(all_days, fill_value=0)
        .reset_index()
    )

    # Create polar radar plot
    fig = px.line_polar(
        df_grouped,
        r="count",
        theta="day_of_week",
        line_close=True,
        title="",
    )

    fig.update_traces(
        fill="toself",
        marker=dict(size=10),
        line=dict(color="#7eb0d5"),
        fillcolor="#7eb0d5",
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                showticklabels=False,
                ticks="",
                range=[0, df_grouped["count"].max()],
                showline=False,
            ),
            angularaxis=dict(
                rotation=90,
                visible=True,
            ),
        ),
        margin=dict(l=10, r=10, t=20, b=10),
        width=300,
        height=220,
        showlegend=False,
    )

    # Apply centralized style configuration
    fig = apply_plot_styles(fig, POLAR_CHART_PLOT_STYLE)

    return fig
