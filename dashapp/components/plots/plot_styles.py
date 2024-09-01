# dashapp/assets/plot_styles.py

""" Centralized Plot Styles """


def apply_plot_styles(fig, style):
    fig.update_layout(**style)
    return fig


SPORT_TYPE_COLORS = {
    "Bike": "#7eb0d5",
    "Run": "#fd7f6f",
    "Walk": "#b2e061",
    "Hike": "#bd7ebe",
    "Row": "#ffb55a",
    "Swim": "#8bd3c7",
}

LINE_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 12},
    },
    "title": None,
}

BAR_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 12},
    },
    "title": None,
    "xaxis": {
        "showgrid": False,
        "zeroline": False,
    },
    "yaxis": {
        "showgrid": False,
        "zeroline": False,
        "showticklabels": False,
    },
}

PIE_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 12},
    },
    "title": None,
}

SCATTER_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 9.5},
    },
    "title": None,
    "xaxis": {
        "showgrid": False,
        "zeroline": False,
    },
    "yaxis": {
        "showgrid": False,
        "zeroline": False,
        "showticklabels": False,
    },
}

HISTOGRAM_CHART_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 9.5},
    },
    "title": None,
    "xaxis": {
        "showgrid": False,
        "zeroline": False,
    },
    "yaxis": {
        "showgrid": False,
        "zeroline": False,
        "showticklabels": False,
    },
}

POLAR_CHART_PLOT_STYLE = {
    "template": "seaborn",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "legend": {
        "title": None,
        "orientation": "h",
        "yanchor": "top",
        "y": -0.2,
        "xanchor": "center",
        "x": 0.5,
        "font": {"size": 9.5},
    },
    "title": None,
    "xaxis": {
        "showgrid": False,
        "zeroline": False,
    },
    "yaxis": {
        "showgrid": False,
        "zeroline": False,
        "showticklabels": False,
    },
}
