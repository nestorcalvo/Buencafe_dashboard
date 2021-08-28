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

features = ["Screw Speed", "Steam Flow Rate", "Steam Pressure", "Oven-Home Temperature",
            "Water Temperature", "Oxygen_pct", "Oven-Home Pressure", "Combustion Air Pressure",
            "Temperature before prear", "Temperature after prear", "Burner Position", "Burner_pct", 
            "Borra Flow Rate_kgh", "Cisco Flow Rate_kgh"]

cardtab_11 = dbc.Card([
        dls.Hash(
            dcc.Graph(id="graph-fuel"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
                    )
    ])

cardtab_21 = dbc.Card([
        dls.Hash(
            dcc.Graph(id="graph-distribution2"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
            )
    ])

card_31 = dbc.Card(
    [
        dbc.Col([
            dbc.Col([
                html.P(
                    "Select date range that you want to see:"
                ),
                dcc.DatePickerRange(
                    id='my-date-picker-range2',
                    min_date_allowed=date(2020, 10, 1),
                    max_date_allowed=date(2021, 6, 30),
                    initial_visible_month=date(2020, 10, 1),
                    end_date=date(2021, 6, 30),
                    clearable=True,
                    month_format="MMMM, YYYY",
                    number_of_months_shown=3
                )
            ]),
            html.Hr(),
            dbc.Col([
                html.P(
                    "Select the data frequency:"
                ),
                dcc.RadioItems(
                    id='frequency-radioitems2',
                    labelStyle={"display": "inline-block"},
                    options= [
                        {"label": "Daily", "value": "data_daily"},
                        {"label": "Hourly", "value": "data_hourly"}
                    ], value= "data_daily",
                    style= {"color": "black"}
                )
            ])
        ])
    ])

card_41 = dbc.Card([
        dbc.Col([
            dbc.FormGroup([
                dbc.Label("Y - Axis"),
                dcc.Dropdown(
                    id="y-variable2",
                    options=[{
                        "label": col,
                        "value": col
                    } for col in features],
                    value="Steam Flow Rate",
                ),
            ]),
            html.H6("Efficiency Range"),
            dcc.RangeSlider(
                id='slider-efficiency2',
                min=0,
                max=1.00,
                step=0.01,
                value=[0, 1.00]
            ),
            html.P(id='range-efficiency2')
        ])
    ])

card_51 = dbc.Card([
        dls.Hash(
            dcc.Graph(id="graph-comparison2"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
        )
    ])

layout= [
    html.Div([
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "Fuel Analitycs",
            className = "content-title"
        ),
        html.Div([
            dbc.Row([
                dbc.Col(
                    dbc.Tabs([
                        dbc.Tab(cardtab_11, label="Time series"),
                        dbc.Tab(cardtab_21, label="Distribution"),
                        ],
                        id="card-tabs2",
                        card=True,
                        active_tab="tab-0",
                    ),
                    width=9
                ),
                dbc.Col(
                    card_31, width=3                  
                )
            ]),
            dbc.Row([
                dbc.Col(
                    card_41, width=3
                ),
                dbc.Col(
                    card_51, width=9
                )
            ]),
        ])
    ],
    className = "corr-icon-container"
    )
        ]

@app.callback(
    Output('graph-fuel','figure'),
    [Input('my-date-picker-range2', 'start_date'),
    Input('my-date-picker-range2', 'end_date'),
    Input('frequency-radioitems2', 'value')]
)

def update_figure(start_date, end_date, value_radio):
    if value_radio == "data_daily":
        data2 = pd.read_csv("data/data_interpolate_daily.csv", parse_dates=["Time"])
        data2.set_index(["Time"], inplace=True)
    elif value_radio == "data_hourly":
        data2 = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
        data2.set_index(["Time"], inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = data2.loc[start_date: end_date].index,
        y = data2.loc[start_date: end_date]["Gas Flow Rate"],
        mode = "lines",
        name = "Gas"
    ))
    fig.update_layout(title = 'Gas Consumption',
                    xaxis_title='Date',
                    yaxis_title='Gas (Kg/hour)',
                    transition_duration=500)
    return fig

@app.callback(
    Output('graph-distribution2','figure'),
    [Input('my-date-picker-range2', 'start_date'),
    Input('my-date-picker-range2', 'end_date')]
)

def update_figure2(start_date, end_date):
    df = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
    df.set_index(["Time"], inplace=True)

    fig = px.histogram(df.loc[start_date: end_date], x="Gas Flow Rate", nbins=100)
    fig.update_layout(title = 'Gas Flow Rate Distribution',
                    xaxis_title='Gas (Kg/hour)',
                    yaxis_title='Count',
                    transition_duration=500)
    return fig

@app.callback(
    [Output("graph-comparison2", "figure"),
    Output("range-efficiency2", "children")],
    [Input("y-variable2", "value"),
    Input("slider-efficiency2", "value"),]
)

def update_figure3(feature, efficiency):
    df2 = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
    df2.set_index(["Time"], inplace=True)

    fig = px.scatter(
        x = df2[(df2['Efficiency'] < efficiency[1]) & (df2['Efficiency'] > efficiency[0])]["Gas Flow Rate"],
        y = df2[(df2['Efficiency'] < efficiency[1]) & (df2['Efficiency'] > efficiency[0])][feature]
    )
    fig.update_layout(title = 'Gas Flow Rate Comparison',
                    xaxis_title= 'Gas (Kg/hour)',
                    yaxis_title= feature,
                    transition_duration= 500)
    
    range_efficiency2 = str(efficiency[0]) + " - " + str(efficiency[1])
    return fig, range_efficiency2