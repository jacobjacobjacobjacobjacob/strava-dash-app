# dashapp/layouts/overview.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from dashapp.components.navbar import navbar
from dashapp.components.ids import *

""" 
MAIN OVERVIEW LAYOUT 
"""


def get_overview_layout(**controls):
    return dbc.Container(
        [
            # Navbar
            navbar,
            dbc.Row(
                [
                    # Controls Column (spanning full height)
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    id="overview-controls-box",
                                    className="controls",
                                    children=[
                                        html.H4(
                                            "Monthly Overview",
                                            className="bg-primary text-white p-3 mb-1 text-center",
                                        ),
                                        html.H5(
                                            "Month",
                                            className="bg-primary text-white p-2 mb-2 text-center",
                                        ),
                                        controls["month_checklist"],
                                        html.H5(
                                            "Year",
                                            className="bg-primary text-white p-2 mb-2 text-center",
                                        ),
                                        controls["year_checklist"],
                                        html.H5(
                                            "Sport",
                                            className="bg-primary text-white p-2 mb-2 text-center",
                                        ),
                                        controls["sport_type_checklist"],
                                        controls["month_filtering_button_group"],
                                    ],
                                ),
                            ),
                            color="primary",
                            outline=True,
                        ),
                        width=2,
                        style={"height": "100vh"},  # Full height
                    ),
                    # Main Content Column
                    dbc.Col(
                        [
                            # Top boxes Row
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H2(
                                                            id=ACTIVITY_COUNT_MONTH,
                                                        ),
                                                        html.H4(
                                                            "Activities",
                                                        ),
                                                    ],
                                                    className="flex-center",
                                                ),
                                            ),
                                            color="primary",
                                        ),
                                        width=3,
                                        className="overview-small-card",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H2(
                                                            id=DURATION_MONTH,
                                                        ),
                                                        html.H4(
                                                            "Hours",
                                                        ),
                                                    ],
                                                    className="flex-center",
                                                ),
                                            ),
                                            color="primary",
                                        ),
                                        width=3,
                                        className="overview-small-card",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H2(
                                                            id=DISTANCE_MONTH,
                                                        ),
                                                        html.H4(
                                                            "Kilometers",
                                                        ),
                                                    ],
                                                    className="flex-center",
                                                ),
                                            ),
                                            color="primary",
                                        ),
                                        width=3,
                                        className="overview-small-card",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H2(
                                                            id=SUFFER_SCORE_MONTH,
                                                            className="no-margin",
                                                        ),
                                                        html.H4(
                                                            "Effort",
                                                            className="no-margin",
                                                        ),
                                                    ],
                                                    className="flex-center",
                                                ),
                                            ),
                                            color="primary",
                                        ),
                                        width=3,
                                        className="overview-small-card",
                                    ),
                                ],
                            ),
                            # Large boxes Row
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H5("Total Duration (h)"),
                                                        dcc.Graph(
                                                            id=OVERVIEW_DURATION_BAR_CHART,
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
                                                        html.H5("Total Distance (km)"),
                                                        dcc.Graph(
                                                            id=OVERVIEW_DISTANCE_BAR_CHART,
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
                            # Medium boxes Row
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H5("Effort"),
                                                        dcc.Graph(
                                                            id=OVERVIEW_EFFORT_SCATTER_CHART,
                                                            style={
                                                                "width": "450px",
                                                            },
                                                        ),
                                                    ],
                                                    className="text-center",
                                                )
                                            ),
                                            color="light",
                                        ),
                                        width=4,
                                        className="overview-medium-card",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H5("Activities"),
                                                        dcc.Graph(
                                                            id=OVERVIEW_ACTIVITY_COUNT_PIE_CHART,
                                                            style={
                                                                "width": "450px",
                                                            },
                                                        ),
                                                    ],
                                                    className="text-center",
                                                )
                                            ),
                                            color="light",
                                        ),
                                        width=4,
                                        className="overview-medium-card",
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                html.Div(
                                                    children=[
                                                        html.H5("Weekdays"),
                                                        dcc.Graph(
                                                            id=OVERVIEW_POLAR_CHART,
                                                            style={
                                                                "width": "450px",
                                                            },
                                                        ),
                                                    ],
                                                    className="text-center",
                                                )
                                            ),
                                            color="light",
                                        ),
                                        width=4,
                                        className="overview-medium-card",
                                    ),
                                ],
                            ),
                        ],
                        width=10,
                        style={"height": "auto"},
                    ),
                ],
            ),
        ],
        fluid=True,
    )
