#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Vaishnavi Chilakamarthi
# Created Date: Mon May 1 16:00:00 EST 2023
# =============================================================================
"""This is the Main module to create and run the 
Dask application on top of the Flask server."""
# =============================================================================
# Imports
# =============================================================================

from flask import Flask
from dash import dcc, Dash, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from take_home_project.models.models import Stock1_Price, Stock2_Price, Stock3_Price, Stock4_Price
from take_home_project.db_helper import Db_helper
from datetime import datetime, timedelta
import pandas as pd

"""Creating a Flask server."""

app = Flask(__name__)


"""Creating a Dask server on top of the Flask Server."""

dashapp = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
    server=app,
    url_base_pathname="/",
)

dashapp.logger.info(
    str(datetime.now()) + " LOG: " + "Creating dash application for the dashboard"
)

# Adding the main title - Stock prices
main_title = dcc.Markdown(
    children="Real-time Stock Prices",
    style={
        "font-size": "50px",
        "text-align": "center",
        "font-weight": "bold",
        "padding": "30px",
        "background-color": "d2deef",
    },
)

dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Creating components for the Stock1_Price graphs in the dashboard"
)

"""Creating Dashboard for values in Stock1_Price table."""

# Adding the title for the Stock1_Price vs Time graph
stock1_title = dcc.Markdown(
    children="Stock1_Price vs Time",
    style={
        "font-size": "30px",
        "font-weight": "bold",
        "text-align": "center",
        "margin-top": "10px",
    },
)

# Adding date selector for Stock1_Price graph
stock1_graph_date_selector = dcc.DatePickerSingle(
    id="stock1-date-picker",
    date=datetime(2023, 4, 19),
    display_format="YYYY-MM-DD",
    style={"marginRight": 10},
)

# Adding time range slider for Stock1_Price graph
stock1_graph_time_selector = dcc.RangeSlider(
    id="stock1-time-range-slider",
    min=0,
    max=24,
    step=1,
    marks={i: f"{i}:00" for i in range(0, 25)},
    value=[0, 24],
)

# Adding the Stock1_Price vs Time graph
stock1_graph = dcc.Graph(figure={}, style={"margin-top": "10px"})

# Adding a dropdown to select Stock1_Price graph type
stock1_dropdown = dcc.Dropdown(
    options=["Line Plot", "Scatter Plot"],
    value="Line Plot",
    clearable=False,
    style={"margin-top": "10px", "width": "50%"},
)

# Creating a button to download Stock1_Price vs Time data as a CSV
stock1_csv_download_button = html.Div(
    [
        dbc.Button(
            "Download as CSV",
            id="stock1-csv-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="success",
        ),
        html.Span(id="stock1-csv-output", style={"verticalAlign": "middle"}),
    ]
)
stock1_csv_download_component = dcc.Download(id="stock1-csv")

# Creating refresh button to reload data from Stock1_Price table
refresh_stock1_graph_button = html.Div(
    [
        dbc.Button(
            "Refresh Data",
            id="stock1-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="info",
        ),
        html.Span(id="stock1-output", style={"verticalAlign": "middle"}),
    ]
)

dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Creating components for the Stock2_Price graphs in the dashboard"
)

"""Creating Dashboard for values in Stock2_Price table."""

# Adding the title for the Stock2_Price vs Time graph
stock2_title = dcc.Markdown(
    children="Stock2_Price vs Time",
    style={
        "font-size": "30px",
        "margin-top": "60px",
        "font-weight": "bold",
        "text-align": "center",
    },
)

# Adding date selector for Stock2_Price graph
stock2_graph_date_selector = dcc.DatePickerSingle(
    id="stock2-date-picker",
    date=datetime(2023, 4, 19),
    display_format="YYYY-MM-DD",
    style={"marginRight": 10},
)

# Adding time range slider for Stock2_Price graph
stock2_graph_time_selector = dcc.RangeSlider(
    id="stock2-time-range-slider",
    min=0,
    max=24,
    step=1,
    marks={i: f"{i}:00" for i in range(0, 25)},
    value=[0, 24],
)

# Adding the Stock2_Price vs Time graph
stock2_graph = dcc.Graph(figure={}, style={"margin-top": "10px"})

# Adding a dropdown to select Stock2_Price graph type
stock2_dropdown = dcc.Dropdown(
    options=["Line Plot", "Scatter Plot"],
    value="Line Plot",
    clearable=False,
    style={"margin-top": "10px", "width": "50%"},
)

# Creating a button to download Stock2_Price vs Time data as a CSV
stock2_csv_download_button = html.Div(
    [
        dbc.Button(
            "Download as CSV",
            id="stock2-csv-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="success",
        ),
        html.Span(id="stock2-csv-output", style={"verticalAlign": "middle"}),
    ]
)
stock2_csv_download_component = dcc.Download(id="stock2-csv")

# Creating refresh button to reload data from Stock2_Price table
refresh_stock2_graph_button = html.Div(
    [
        dbc.Button(
            "Refresh Data",
            id="stock2-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="info",
        ),
        html.Span(id="stock2-output", style={"verticalAlign": "middle"}),
    ]
)

dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Creating components for the Stock3_Price graphs in the dashboard"
)

"""Creating Dashboard for values in Stock3_Price table."""

# Adding the title for the Stock3_Price vs Time graph
stock3_title = dcc.Markdown(
    children="Stock3_Price vs Time",
    style={
        "font-size": "30px",
        "margin-top": "60px",
        "font-weight": "bold",
        "text-align": "center",
    },
)

# Adding date selector for Stock3_Price graph
stock3_graph_date_selector = dcc.DatePickerSingle(
    id="stock3-date-picker",
    date=datetime(2023, 4, 19),
    display_format="YYYY-MM-DD",
    style={"marginRight": 10},
)

# Adding time range slider for Stock3_Price graph
stock3_graph_time_selector = dcc.RangeSlider(
    id="stock3-time-range-slider",
    min=0,
    max=24,
    step=1,
    marks={i: f"{i}:00" for i in range(0, 25)},
    value=[0, 24],
)

# Adding the Stock3_Price vs Time graph
stock3_graph = dcc.Graph(figure={}, style={"margin-top": "10px"})

# Adding a dropdown to select Stock3_Price graph type
stock3_dropdown = dcc.Dropdown(
    options=["Line Plot", "Scatter Plot"],
    value="Line Plot",
    clearable=False,
    style={"margin-top": "10px", "width": "50%"},
)

# Creating a button to download Stock3_Price vs Time data as a CSV
stock3_csv_download_button = html.Div(
    [
        dbc.Button(
            "Download as CSV",
            id="stock3-csv-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="success",
        ),
        html.Span(id="stock3-csv-output", style={"verticalAlign": "middle"}),
    ]
)
stock3_csv_download_component = dcc.Download(id="stock3-csv")

# Creating refresh button to reload data from Stock3_Price table
refresh_stock3_graph_button = html.Div(
    [
        dbc.Button(
            "Refresh Data",
            id="stock3-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="info",
        ),
        html.Span(id="stock3-output", style={"verticalAlign": "middle"}),
    ]
)

dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Creating components for the Stock4_Price graphs in the dashboard"
)


"""Creating Dashboard for values in Stock4_Price table."""

# Adding the title for the Stock4_Price vs Time graph
stock4_title = dcc.Markdown(
    children="Stock4_Price vs Time",
    style={
        "font-size": "30px",
        "margin-top": "60px",
        "font-weight": "bold",
        "text-align": "center",
    },
)

# Adding date selector for Stock4_Price graph
stock4_graph_date_selector = dcc.DatePickerSingle(
    id="stock4-date-picker",
    date=datetime(2023, 4, 19),
    display_format="YYYY-MM-DD",
    style={"marginRight": 10},
)

# Adding time range slider for Stock4_Price graph
stock4_graph_time_selector = dcc.RangeSlider(
    id="stock4-time-range-slider",
    min=0,
    max=24,
    step=1,
    marks={i: f"{i}:00" for i in range(0, 25)},
    value=[0, 24],
)

# Adding the Stock4_Price vs Time graph
stock4_graph = dcc.Graph(figure={}, style={"margin-top": "10px"})

# Adding a dropdown to select Stock4_Price graph type
stock4_dropdown = dcc.Dropdown(
    options=["Line Plot", "Scatter Plot"],
    value="Line Plot",
    clearable=False,
    style={"margin-top": "10px", "width": "50%"},
)

# Creating a button to download Stock4_Price vs Time data as a CSV
stock4_csv_download_button = html.Div(
    [
        dbc.Button(
            "Download as CSV",
            id="stock4-csv-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px"},
            color="success",
        ),
        html.Span(id="stock4-csv-output", style={"verticalAlign": "middle"}),
    ]
)
stock4_csv_download_component = dcc.Download(id="stock4-csv")

# Creating refresh button to reload data from Stock4_Price table
refresh_stock4_graph_button = html.Div(
    [
        dbc.Button(
            "Refresh Data",
            id="stock4-button",
            className="me-2",
            n_clicks=0,
            style={"margin-top": "10px", "margin-bottom": "30px"},
            color="info",
        ),
        html.Span(id="stock4-output", style={"verticalAlign": "middle"}),
    ]
)

dashapp.logger.info(
    str(datetime.now()) + " LOG: " + "Defining the layout for the dashboard"
)


"""Creating the layout for the Dash app."""

dashapp.layout = dbc.Container(
    [
        main_title,  # Main title for the dashboard
        stock1_title,  # Stock1_Price block
        stock1_graph_date_selector,
        stock1_graph_time_selector,
        stock1_graph,
        stock1_dropdown,
        stock1_csv_download_button,
        stock1_csv_download_component,
        refresh_stock1_graph_button,
        stock2_title,  # Stock2_Price block
        stock2_graph_date_selector,
        stock2_graph_time_selector,
        stock2_graph,
        stock2_dropdown,
        stock2_csv_download_button,
        stock2_csv_download_component,
        refresh_stock2_graph_button,
        stock3_title,  # Stock3_Price block
        stock3_graph_date_selector,
        stock3_graph_time_selector,
        stock3_graph,
        stock3_dropdown,
        stock3_csv_download_button,
        stock3_csv_download_component,
        refresh_stock3_graph_button,
        stock4_title,  # Stock4_Price block
        stock4_graph_date_selector,
        stock4_graph_time_selector,
        stock4_graph,
        stock4_dropdown,
        stock4_csv_download_button,
        stock4_csv_download_component,
        refresh_stock4_graph_button,
    ],
    style={"backgroundColor": "#d2deef"},
)


"""Callback function to refresh the Stock1_Price data when the button is clicked."""


@dashapp.callback(
    Output(stock1_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock1-button", "n_clicks"),
        Input(stock1_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def refresh_graph1(n_clicks: int, graph_type: str):
    global df_stock1
    # Reloading the data from the database and updating the global df_stock1 value
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Reloading data from Stock1_Price table"
    )
    df_stock1 = db_helper.fetch_data(Stock1_Price)
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock1, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_stock1, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to refresh the Stock2_Price data when the button is clicked."""


@dashapp.callback(
    Output(stock2_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock2-button", "n_clicks"), 
        Input(stock2_dropdown, component_property="value")
    ],
    prevent_initial_call=True,
)
def refresh_graph2(n_clicks: int, graph_type: str):
    global df_stock2
    # Reloading the data from the database and updating the global df_stock2 value
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Reloading data from Stock2_Price table"
    )
    df_stock2 = db_helper.fetch_data(Stock2_Price)
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock2, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_stock2, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to refresh the Stock3_Price data when the button is clicked."""


@dashapp.callback(
    Output(stock3_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock3-button", "n_clicks"),
        Input(stock3_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def refresh_graph3(n_clicks: int, graph_type: str):
    global df_stock3
    # Reloading the data from the database and updating the global df_stock3 value
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Reloading data from Stock3_Price table"
    )
    df_stock3 = db_helper.fetch_data(Stock3_Price)
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock3, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_stock3, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to refresh the Stock4_Price data when the button is clicked."""


@dashapp.callback(
    Output(stock4_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock4-button", "n_clicks"),
        Input(stock4_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def refresh_graph4(n_clicks: int, graph_type: str):
    global df_stock4
    # Reloading the data from the database and updating the global df_stock4 value
    dashapp.logger.info(
        str(datetime.now()) + " LOG: " + "Reloading data from Stock4_Price table"
    )
    df_stock4 = db_helper.fetch_data(Stock4_Price)
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock4, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_stock4, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle change in graph-type for Stock1_Price vs Time graph."""


@dashapp.callback(
    Output(stock1_graph, component_property="figure"),
    Input(stock1_dropdown, component_property="value"),
)
def update_graph1(user_input: str):
    if user_input == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock1, x="Time", y="Value")  # Scatter plot
    if user_input == "Line Plot":
        fig = px.line(data_frame=df_stock1, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle change in graph-type for Stock2_Price vs Time graph."""


@dashapp.callback(
    Output(stock2_graph, component_property="figure"),
    Input(stock2_dropdown, component_property="value"),
)
def update_graph2(user_input: str):
    if user_input == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock2, x="Time", y="Value")  # Scatter plot
    if user_input == "Line Plot":
        fig = px.line(data_frame=df_stock2, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle change in graph-type for Stock3_Price vs Time graph."""


@dashapp.callback(
    Output(stock3_graph, component_property="figure"),
    Input(stock3_dropdown, component_property="value"),
)
def update_graph3(user_input: str):
    if user_input == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock3, x="Time", y="Value")  # Scatter plot
    if user_input == "Line Plot":
        fig = px.line(data_frame=df_stock3, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle change in graph-type for Stock4_Price vs Time graph."""


@dashapp.callback(
    Output(stock4_graph, component_property="figure"),
    Input(stock4_dropdown, component_property="value"),
)
def update_graph4(user_input: str):
    if user_input == "Scatter Plot":
        fig = px.scatter(data_frame=df_stock4, x="Time", y="Value")  # Scatter plot
    if user_input == "Line Plot":
        fig = px.line(data_frame=df_stock4, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle Download as CSV button for the Stock1_Price vs Time graph."""


@dashapp.callback(
    Output("stock1-csv", "data"),
    Input("stock1-csv-button", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks: int):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Download request received for Stock1_Price vs Time data as a CSV"
    )

    # Sending Stock1_Price vs Time data as CSV
    return dcc.send_data_frame(df_stock1.to_csv, "Stock1_Price_CSV.csv")


"""Callback function to handle Download as CSV button for the Stock2_Price vs Time graph."""


@dashapp.callback(
    Output("stock2-csv", "data"),
    Input("stock2-csv-button", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks: int):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Download request received for Stock2_Price vs Time data as a CSV"
    )
    # Sending Stock2_Price vs Time data as CSV
    return dcc.send_data_frame(df_stock2.to_csv, "Stock2_Price_CSV.csv")


"""Callback function to handle Download as CSV button for the Stock3_Price vs Time graph."""


@dashapp.callback(
    Output("stock3-csv", "data"),
    Input("stock3-csv-button", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks: int):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Download request received for Stock3_Price vs Time data as a CSV"
    )
    # Sending Stock3_Price vs Time data as CSV
    return dcc.send_data_frame(df_stock3.to_csv, "Stock3_Price_CSV.csv")


"""Callback function to handle Download as CSV button for the Stock4_Price vs Time graph."""


@dashapp.callback(
    Output("stock4-csv", "data"),
    Input("stock4-csv-button", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks: int):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Download request received for Stock4_Price vs Time data as a CSV"
    )
    # Sending Stock4_Price vs Time data as CSV
    return dcc.send_data_frame(df_stock4.to_csv, "Stock4_Price_CSV.csv")


"""Callback function to handle date-time change for Stock1_Price graph."""


@dashapp.callback(
    Output(stock1_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock1-date-picker", "date"),
        Input("stock1-time-range-slider", "value"),
        Input(stock1_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def update_stock1_graph_datetime(date_selected, time_range, graph_type):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Refreshing Stock1_Price graph for - "
        + str(date_selected)
        + ", "
        + str(time_range)
        + ", "
        + str(graph_type)
    )
    date_selected = pd.Timestamp(date_selected)
    df_filtered = df_stock1[
        (df_stock1["Time"] >= date_selected + timedelta(hours=time_range[0]))
        & (df_stock1["Time"] <= date_selected + timedelta(hours=time_range[1]))
    ]
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_filtered, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_filtered, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle date-time change for Stock2_Price graph."""


@dashapp.callback(
    Output(stock2_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock2-date-picker", "date"),
        Input("stock2-time-range-slider", "value"),
        Input(stock2_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def update_stock2_graph_datetime(date_selected, time_range, graph_type):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Refreshing Stock2_Price graph for - "
        + str(date_selected)
        + ", "
        + str(time_range)
        + ", "
        + str(graph_type)
    )
    date_selected = pd.Timestamp(date_selected)
    df_filtered = df_stock2[
        (df_stock2["Time"] >= date_selected + timedelta(hours=time_range[0]))
        & (df_stock2["Time"] <= date_selected + timedelta(hours=time_range[1]))
    ]
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_filtered, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_filtered, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle date-time change for Stock3_Price graph."""


@dashapp.callback(
    Output(stock3_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock3-date-picker", "date"),
        Input("stock3-time-range-slider", "value"),
        Input(stock3_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def update_stock3_graph_datetime(date_selected, time_range, graph_type):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Refreshing Stock3_Price graph for - "
        + str(date_selected)
        + ", "
        + str(time_range)
        + ", "
        + str(graph_type)
    )
    date_selected = pd.Timestamp(date_selected)
    df_filtered = df_stock3[
        (df_stock3["Time"] >= date_selected + timedelta(hours=time_range[0]))
        & (df_stock3["Time"] <= date_selected + timedelta(hours=time_range[1]))
    ]
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_filtered, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_filtered, x="Time", y="Value")  # Line plot
    return fig


"""Callback function to handle date-time change for Stock4_Price graph."""


@dashapp.callback(
    Output(stock4_graph, component_property="figure", allow_duplicate=True),
    [
        Input("stock4-date-picker", "date"),
        Input("stock4-time-range-slider", "value"),
        Input(stock4_dropdown, component_property="value"),
    ],
    prevent_initial_call=True,
)
def update_stock4_graph_datetime(date_selected, time_range, graph_type):
    dashapp.logger.info(
        str(datetime.now())
        + " LOG: "
        + "Refreshing Stock4_Price graph for - "
        + str(date_selected)
        + ", "
        + str(time_range)
        + ", "
        + str(graph_type)
    )
    date_selected = pd.Timestamp(date_selected)
    df_filtered = df_stock4[
        (df_stock4["Time"] >= date_selected + timedelta(hours=time_range[0]))
        & (df_stock4["Time"] <= date_selected + timedelta(hours=time_range[1]))
    ]
    if graph_type == "Scatter Plot":
        fig = px.scatter(data_frame=df_filtered, x="Time", y="Value")  # Scatter plot
    if graph_type == "Line Plot":
        fig = px.line(data_frame=df_filtered, x="Time", y="Value")  # Line plot
    return fig


dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Establishing connection with the postgres database"
)

"""Creating an instance of the Db_helper."""
db_helper = Db_helper()

dashapp.logger.info(
    str(datetime.now())
    + " LOG: "
    + "Successfully established connection with the postgres database"
)

"""Initial fetching of data from the database."""
dashapp.logger.info(
    str(datetime.now()) + " LOG: " + "Fetching initial data from the database tables"
)
df_stock1 = db_helper.fetch_data(Stock1_Price)
df_stock2 = db_helper.fetch_data(Stock2_Price)
df_stock3 = db_helper.fetch_data(Stock3_Price)
df_stock4 = db_helper.fetch_data(Stock4_Price)

###################################################
# Server Run
###################################################
dashapp.run_server(host="0.0.0.0", port=8888)
