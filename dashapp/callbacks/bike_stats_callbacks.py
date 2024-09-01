# dashapp/callbacks/overview_callbacks.py
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
        ],
        [Input(YEAR_DROPDOWN, "value")],
    )
    def update_values(selected_year):
        # Filter data for 'Bike' sport type
        filtered_df = df[df["sport_type"] == "Bike"]

        # Apply year filter if selected_year is provided
        if selected_year:
            filtered_df = filtered_df[filtered_df["year"] == int(selected_year)]

        # Generate the line chart with the filtered data
        bike_stats_average_speed_line_chart = get_average_metric_line_chart(
            df=filtered_df,
            selected_year=selected_year,
            sport_type="Bike",
            metric="average_speed",
        )

        return (selected_year, bike_stats_average_speed_line_chart)
