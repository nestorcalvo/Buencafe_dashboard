import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import date
import dash_loading_spinners as dls
from dash.dependencies import Input, Output, ClientsideFunction, State
from app import app

layout= [
    html.Div([
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "Steam Analitycs",
            className = "content-title"
        ),
        html.Div([
            html.P(
                "Select the data frequency:"
            ),
            dcc.RadioItems(
                id='frequency-radioitems',
                labelStyle={"display": "inline-block"},
                options= [
                    {"label": " Weekly  ", "value": "data_weekly"},
                    {"label": " Daily  ", "value": "data_daily"},
                    {"label": " Hourly  ", "value": "data_hourly"}
                ], value= "data_daily",
                style= {"color": "black"}
            )
        ]),
        html.Div([
            html.P(
                "Select date range that you want to see:"
            ),
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(2020, 10, 1),
                max_date_allowed=date(2021, 6, 30),
                initial_visible_month=date(2020, 10, 1),
                end_date=date(2021, 6, 30),
                clearable=True,
                month_format="MMMM, YYYY",
                number_of_months_shown=3
                ),
            html.Div(
                id='output-container-date-picker-range',
                className="month-container")
            ]),
        dls.Hash(
            dcc.Graph(id="graph-steam"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
        ),
        dcc.Store(id='intermediate-value')
        ],
    className = "corr-icon-container"
    ),

]

@app.callback(
    Output('intermediate-value','data'),
    [Input('frequency-radioitems', 'value')]
)

def update_frequency(value):
    if value == "data_weekly":
        df = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
        data = df.set_index(["Time"]).resample("W").mean()
        data["Time"] = data.index
    elif value == "data_daily":
        data = pd.read_csv("data/data_interpolate_daily.csv", parse_dates=["Time"])
        data.set_index(["Time"], inplace=True)
    elif value == "data_hourly":
        data = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
        data.set_index(["Time"], inplace=True)
    return data.to_json(date_format='iso')

@app.callback(
    Output('graph-steam','figure'),
    [Input('intermediate-value', 'data'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')]
)

def update_figure(data, start_date, end_date):
    df = pd.read_json(data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = df.loc[start_date: end_date].index,
        y = df.loc[start_date: end_date]["Steam Flow Rate"],
        mode = "lines",
        name = "Steam"
    ))
    fig.update_layout(title = 'Steam Generation',
                    xaxis_title='Date',
                    yaxis_title='Steam (Kg/day)',
                    transition_duration=500)
    return fig