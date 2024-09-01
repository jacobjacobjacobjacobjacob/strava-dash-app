# dashapp/callbacks/overview_callbacks.py
from dash import Input, Output, State, Dash, callback_context
import pandas as pd

from assets.utils import ALL_MONTHS, CURRENT_MONTH
from dashapp.components.plots.overview_plots import *
from dashapp.components.ids import *

"""
Callbacks for the "Overview"-layout.
"""


def register_overview_callbacks(app: Dash, df: pd.DataFrame):
    @app.callback(
        [
            Output(ACTIVITY_COUNT_MONTH, "children"),
            Output(DISTANCE_MONTH, "children"),
            Output(DURATION_MONTH, "children"),
            Output(SUFFER_SCORE_MONTH, "children"),
            Output(OVERVIEW_DURATION_BAR_CHART, "figure"),
            Output(OVERVIEW_DISTANCE_BAR_CHART, "figure"),
            Output(OVERVIEW_ACTIVITY_COUNT_PIE_CHART, "figure"),
            Output(OVERVIEW_EFFORT_SCATTER_CHART, "figure"),
            Output(OVERVIEW_POLAR_CHART, "figure"),
            Output(MONTH_CHECKLIST, "value"),
            Output(SPORT_TYPE_CHECKLIST, "value"),
        ],
        [
            Input(MONTH_CHECKLIST, "value"),
            Input(YEAR_CHECKLIST, "value"),
            Input(SPORT_TYPE_CHECKLIST, "value"),
            Input(OVERVIEW_CLEAR_BUTTON, "n_clicks"),
            Input(OVERVIEW_CURRENT_MONTH_BUTTON, "n_clicks"),
            Input(OVERVIEW_SELECT_ALL_BUTTON, "n_clicks"),
        ],
        [
            State(MONTH_CHECKLIST, "value"),
            State(SPORT_TYPE_CHECKLIST, "value"),
            State(YEAR_CHECKLIST, "value"),
        ],
    )
    def update_values(
        month_values,
        year_values,
        sport_type_values,
        clear_button_clicks,
        select_all_button_clicks,
        current_month_button_clicks,
        current_month_values,
        current_sport_type_values,
        current_year_values,
    ):
        # Handle button clicks
        triggered_id = callback_context.triggered_id

        if triggered_id == OVERVIEW_CLEAR_BUTTON:
            new_sport_type_values = current_sport_type_values
            new_month_values = []

        elif triggered_id == OVERVIEW_CURRENT_MONTH_BUTTON:
            new_month_values = [CURRENT_MONTH]
            new_sport_type_values = current_sport_type_values

        elif triggered_id == OVERVIEW_SELECT_ALL_BUTTON:
            # Select all months and sport types
            new_month_values = ALL_MONTHS
            new_sport_type_values = list(df["sport_type"].unique())

        else:
            new_month_values = month_values
            new_sport_type_values = sport_type_values

        # Convert year values to integers
        selected_years = [int(year) for year in year_values]

        filtered_df = df[
            df["month"].isin(new_month_values)
            & df["year"].isin(selected_years)
            & df["sport_type"].isin(new_sport_type_values)
        ]

        activity_count = len(filtered_df)
        distance_sum = filtered_df["distance"].sum()
        duration_sum = filtered_df["duration"].sum()
        suffer_score_sum = filtered_df["suffer_score"].sum()

        # Formatting
        distance_sum = f"{distance_sum:.0f}"
        duration_sum = f"{duration_sum:.0f}"
        suffer_score_sum = f"{suffer_score_sum:.0f}"

        # Plots
        overview_duration_bar_chart = get_overview_duration_bar_chart(
            filtered_df, new_month_values
        )
        overview_distance_bar_chart = get_overview_distance_bar_chart(
            filtered_df, new_month_values
        )
        overview_activity_count_pie_chart = get_overview_activity_count_pie_chart(
            filtered_df, new_month_values
        )

        overview_effort_scatter_chart = get_overview_effort_scatter_chart(
            filtered_df, new_month_values
        )

        overview_polar_chart_duration_by_day = get_overview_polar_chart_count_by_day(
            filtered_df, new_month_values
        )

        return (
            activity_count,
            distance_sum,
            duration_sum,
            suffer_score_sum,
            overview_duration_bar_chart,
            overview_distance_bar_chart,
            overview_activity_count_pie_chart,
            overview_effort_scatter_chart,
            overview_polar_chart_duration_by_day,
            new_month_values,
            new_sport_type_values,
        )
