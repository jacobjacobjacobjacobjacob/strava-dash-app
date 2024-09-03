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
            Output(BIKE_STATS_AVERAGE_SPEED_LINE_CHART, "figure"),
            Output(BIKE_STATS_AVERAGE_POWER_LINE_CHART, "figure"),
            Output(BIKE_STATS_AVERAGE_HR_LINE_CHART, "figure"),
        ],
        [Input(YEAR_DROPDOWN, "value")],
    )
    def update_values(selected_year):
        # Generate the line charts with the filtered data directly
        bike_stats_average_speed_line_chart = get_average_metric_line_chart(
            df=df,
            metric="average_speed",
            sport_type="Bike",
            selected_year=selected_year,
        )

        bike_stats_average_power_line_chart = get_average_metric_line_chart(
            df=df,
            metric="average_watts",
            sport_type="Bike",
            selected_year=selected_year,
        )

        bike_stats_average_hr_line_chart = get_average_metric_line_chart(
            df=df,
            metric="average_heartrate",
            sport_type="Bike",
            selected_year=selected_year,
        )

        return (
            selected_year,
            bike_stats_average_speed_line_chart,
            bike_stats_average_power_line_chart,
            bike_stats_average_hr_line_chart,
        )
