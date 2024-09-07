# dashapp/components/controls.py
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from assets.utils import ALL_MONTHS, CURRENT_YEAR, BIKE_METRICS, RUN_METRICS
from dashapp.components.ids import *


# BUTTONS


# BUTTON GROUPS
def get_month_filtering_button_group() -> html.Div:
    return html.Div(
        dbc.ButtonGroup(
            [
                dbc.Button(
                    "Current Month",
                    id=OVERVIEW_CURRENT_MONTH_BUTTON,
                    color="light",
                    outline=False,
                ),
                dbc.Button(
                    "Select All",
                    id=OVERVIEW_SELECT_ALL_BUTTON,
                    color="light",
                    outline=False,
                ),
                dbc.Button(
                    "Clear",
                    id=OVERVIEW_CLEAR_BUTTON,
                    color="light",
                    outline=False,
                ),
            ],
            vertical=True,
            className="button-group",
        ),
        className="button-group-container",
    )


# CHECKLISTS
def get_month_checklist(df: pd.DataFrame) -> html.Div:

    return html.Div(
        children=[
            dbc.Checklist(
                id=MONTH_CHECKLIST,
                options=ALL_MONTHS,
                value=ALL_MONTHS,
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "columnGap": "10px",
                    "rowGap": "1px",
                },
            ),
        ],
        style={"display": "flex", "flexDirection": "row"},
    )


def get_year_checklist(df: pd.DataFrame) -> html.Div:
    options = [
        {"label": str(year), "value": str(year)}
        for year in sorted(df["year"].dropna().unique())
    ]

    return html.Div(
        children=[
            dbc.Checklist(
                id=YEAR_CHECKLIST,
                options=options,
                value=[str(CURRENT_YEAR)],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "columnGap": "10px",
                    "rowGap": "1px",
                },
                inline=True,
            ),
        ],
        style={"display": "flex", "flexDirection": "row"},
    )


def get_sport_type_checklist(df: pd.DataFrame) -> html.Div:
    all_sport_types = sorted(df["sport_type"].dropna().unique())

    options = [
        {"label": sport_type, "value": sport_type} for sport_type in all_sport_types
    ]

    return html.Div(
        children=[
            dbc.Checklist(
                id=SPORT_TYPE_CHECKLIST,
                options=options,
                value=["Bike", "Run"],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "columnGap": "10px",
                    "rowGap": "1px",
                },
                inline=True,
            ),
        ],
        style={"display": "flex", "flexDirection": "row"},
    )


# DROPDOWNS
def get_year_dropdown(df: pd.DataFrame) -> html.Div:
    options = [
        {"label": str(year), "value": str(year)}
        for year in sorted(df["year"].dropna().unique())
    ]

    return html.Div(
        children=[
            dcc.Dropdown(
                id=YEAR_DROPDOWN,
                options=options,
                value=CURRENT_YEAR,
                multi=False,
                clearable=True,
            ),
        ]
    )


def get_bike_metrics_dropdown(df: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            dcc.Dropdown(
                id=BIKE_METRICS_DROPDOWN,
                options=BIKE_METRICS,
                value=None,
                multi=True,
                clearable=True,
            ),
        ]
    )
