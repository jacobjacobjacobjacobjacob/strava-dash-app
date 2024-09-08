# dashapp/callbacks/bike_stats_callback.py
from dash import Input, Output, State, Dash, callback_context
import pandas as pd

from assets.utils import ALL_MONTHS, CURRENT_MONTH
from dashapp.components.plots.bike_stats_plots import *
from dashapp.components.ids import *


"""
Callbacks for the "Bike Stats"-layout.
"""


def register_bike_stats_callbacks(app: Dash, df: pd.DataFrame):

    @app.callback(
        [
            Output(YEAR_DROPDOWN, "value"),
            Output(BIKE_METRICS_CHECKLIST, "value"),
            Output(ENVIRONMENT_CHECKLIST, "value"),
            Output(BIKE_STATS_AVERAGE_SPEED_LINE_CHART, "figure"),
            Output(BIKE_STATS_AVERAGE_POWER_LINE_CHART, "figure"),
            Output(BIKE_STATS_AVERAGE_HR_LINE_CHART, "figure"),
            Output(BIKE_STATS_COMPARISON_CHART, "figure"),
        ],
        [Input(YEAR_DROPDOWN, "value"), Input(BIKE_METRICS_CHECKLIST, "value"), Input(ENVIRONMENT_CHECKLIST, "value")],
    )
    def update_bike_stats(selected_year, selected_metrics, selected_environment):

        # Enforce the limit of 2 options selected for the checklist
        if len(selected_metrics) > 2:
            selected_metrics = selected_metrics[:2]
        
        # Filter by environment (None = all)
        if selected_environment:
            df_filtered = df[df["environment"].isin(selected_environment)].copy()
        else:
            df_filtered = df.copy()


        # Generate line charts based on the selected year
        bike_stats_average_speed_line_chart = get_average_metric_line_chart(
            df=df_filtered,
            metric="average_speed",
            sport_type="Bike",
            selected_year=selected_year,
        )

        # Generate the comparison chart only if two metrics are selected
        if len(selected_metrics) == 2:
            bike_stats_comparison_chart = get_comparison_chart(
                df=df_filtered,
                metric_1=selected_metrics[0],
                metric_2=selected_metrics[1],
                sport_type="Bike",
                selected_year=selected_year,
            )
        else:
            # Return an empty figure if not enough metrics are selected
            bike_stats_comparison_chart = {}

        bike_stats_average_power_line_chart = get_average_metric_line_chart(
            df=df_filtered,
            metric="average_watts",
            sport_type="Bike",
            selected_year=selected_year,
        )

        bike_stats_average_hr_line_chart = get_average_metric_line_chart(
            df=df_filtered,
            metric="average_heartrate",
            sport_type="Bike",
            selected_year=selected_year,
        )
       
        return (
            selected_year,
            selected_metrics,
            selected_environment,
            bike_stats_average_speed_line_chart,
            bike_stats_average_power_line_chart,
            bike_stats_average_hr_line_chart,
            bike_stats_comparison_chart,
        )
