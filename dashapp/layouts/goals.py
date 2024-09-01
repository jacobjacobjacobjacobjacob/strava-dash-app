# dashapp/layouts/goals.py
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from dashapp.components.navbar import navbar
from dashapp.components.ids import *
from dashapp.components.plots.goal_plots import (
    get_duration_goal_chart,
    get_distance_goal_chart,
)

from assets.utils import CURRENT_MONTH
from modules.goals import get_goal_dataframes

""" 
GOALS LAYOUT
"""


def get_goals_layout(df: pd.DataFrame) -> html.Div:
    # Get the dataframes
    (
        df_bike_duration_goal_2024,
        df_bike_distance_goal_2024,
        df_run_duration_goal_2024,
        df_run_distance_goal_2024,
    ) = get_goal_dataframes(df)

    bike_duration_chart = get_duration_goal_chart(
        df_bike_duration_goal_2024, CURRENT_MONTH
    )
    bike_distance_chart = get_distance_goal_chart(
        df_bike_distance_goal_2024, CURRENT_MONTH
    )
    run_duration_chart = get_duration_goal_chart(
        df_run_duration_goal_2024, CURRENT_MONTH
    )
    run_distance_chart = get_distance_goal_chart(
        df_run_distance_goal_2024, CURRENT_MONTH
    )

    return dbc.Container(
        [
            # Navbar
            navbar,
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H4("Bike Goals"),
                                                        dcc.Graph(
                                                            id="bike-distance-goal-chart",
                                                            figure=bike_distance_chart,
                                                        ),
                                                        html.Br(),
                                                        dcc.Graph(
                                                            id="bike-duration-goal-chart",
                                                            figure=bike_duration_chart,
                                                        ),
                                                    ],
                                                    className="text-center",
                                                )
                                            ),
                                            color="light",
                                        ),
                                        className="overview-large-card",
                                        width=6,
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H4("Run Goals"),
                                                        dcc.Graph(
                                                            id="run-distance-goal-chart",
                                                            figure=run_distance_chart,
                                                        ),
                                                        html.Br(),
                                                        dcc.Graph(
                                                            id="run-duration-goal-chart",
                                                            figure=run_duration_chart,
                                                        ),
                                                    ],
                                                    className="text-center",
                                                )
                                            ),
                                            color="light",
                                        ),
                                        className="overview-large-card",
                                        width=6,
                                    ),
                                ],
                            ),
                        ],
                        width=12,
                    ),
                ],
            ),
        ],
        fluid=True,
    )
