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

features = ["Screw Speed", "Gas Flow Rate", "Steam Pressure", "Oven-Home Temperature",
            "Water Temperature", "Oxygen_pct", "Oven-Home Pressure", "Combustion Air Pressure",
            "Temperature before prear", "Temperature after prear", "Burner Position", "Burner_pct", 
            "Borra Flow Rate_kgh", "Cisco Flow Rate_kgh"]

cardtab_1 = dbc.Card([
        html.Div(
            id='output-container-date-picker-range',
            className="month-container"
        ),
        dls.Hash(
            dcc.Graph(id="graph-steam", className = "graph-card"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
                    )
    ])

cardtab_2 = dbc.Card([
        html.Div(
            id='output-container-date-picker-range',
            className="month-container"
        ),
        dls.Hash(
            dcc.Graph(id="graph-distribution", className = "graph-card"),
            size = 160,
            speed_multiplier = 0.8,
            debounce = 200
            )
    ])

card_3 = dbc.Card(
    [
        dbc.Col([
            dbc.Col([
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
                )
            ]),
            html.Hr(),
            dbc.Col([
                html.P(
                    "Select the data frequency:"
                ),
                dcc.RadioItems(
                    id='frequency-radioitems',
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

card_4 = dbc.Card([
        dbc.Col([
            dbc.FormGroup([
                dbc.Label("Y - Axis"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[{
                        "label": col,
                        "value": col
                    } for col in features],
                    value="Gas Flow Rate",
                ),
            ]),
            html.H6("Efficiency Range"),
            dcc.RangeSlider(
                id='slider-efficiency',
                min=0,
                max=1.00,
                step=0.01,
                value=[0, 1.00]
            ),
            html.P(id='range-efficiency')
        ])
    ])

card_5 = dbc.Card([
        html.Div(
            id='output-container-date-picker-range',
            className="month-container"
        ),
        dls.Hash(
            dcc.Graph(id="graph-comparison", className = "graph-card"),
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
            "Steam Analytics",
            className = "content-title"
        ),
        html.Div(children=[

            html.Div([
                # dbc.Row([
                #     dbc.Col(
                #         dbc.Tabs([
                #             dbc.Tab(cardtab_1, label="Time series"),
                #             dbc.Tab(cardtab_2, label="Distribution"),
                #             ],
                #             id="card-tabs",
                #             card=True,
                #             active_tab="tab-1",
                #         ),
                #         width=9
                #     ),
                #     dbc.Col(
                #         card_3, width=3                  
                #     )
                # ]),
                dbc.Tabs([
                    dbc.Tab(cardtab_1, label="Time series"),
                    dbc.Tab(cardtab_2, label="Distribution"),
                    ],
                    id="card-tabs",
                    card=True,
                    active_tab="tab-1",
                ),
                card_3,

            ], className = "graph_col_1"),
            html.Div(children =[

                # dbc.Row([
                #     dbc.Col(
                #         card_4, width=3
                #     ),
                #     dbc.Col(
                #         card_5, width=9
                #     )
                # ]),
                card_4,
                card_5
            ], className = "data_col_2")
        ], className = "wrapper__steam-data")

    ],className = "wrapper__steam"),
]

@app.callback(
    Output('graph-steam','figure'),
    [Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('frequency-radioitems', 'value')]
)

def update_figure(start_date, end_date, value_radio):
    if value_radio == "data_daily":
        data = pd.read_csv("data/data_interpolate_daily.csv", parse_dates=["Time"])
        data.set_index(["Time"], inplace=True)
    elif value_radio == "data_hourly":
        data = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
        data.set_index(["Time"], inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = data.loc[start_date: end_date].index,
        y = data.loc[start_date: end_date]["Steam Flow Rate"],
        mode = "lines",
        name = "Steam"
    ))
    fig.update_layout(title = 'Steam Generation',
                    xaxis_title='Date',
                    yaxis_title='Steam (Kg/hour)',
                    transition_duration=500)
    return fig

@app.callback(
    Output('graph-distribution','figure'),
    [Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')]
)

def update_figure2(start_date, end_date):
    df = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
    df.set_index(["Time"], inplace=True)

    fig = px.histogram(df.loc[start_date: end_date], x="Steam Flow Rate", nbins=100)
    fig.update_layout(title = 'Steam Flow Rate Distribution',
                    xaxis_title='Steam (Kg/hour)',
                    yaxis_title='Count',
                    transition_duration=500)
    return fig

@app.callback(
    [Output("graph-comparison", "figure"),
    Output("range-efficiency", "children")],
    [Input("y-variable", "value"),
    Input("slider-efficiency", "value"),]
)

def update_figure3(feature, efficiency):
    df2 = pd.read_csv("data/data_interpolate_hourly.csv", parse_dates=["Time"])
    df2.set_index(["Time"], inplace=True)

    fig = px.scatter(
        x = df2[(df2['Efficiency'] < efficiency[1]) & (df2['Efficiency'] > efficiency[0])]["Steam Flow Rate"],
        y = df2[(df2['Efficiency'] < efficiency[1]) & (df2['Efficiency'] > efficiency[0])][feature]
    )
    fig.update_layout(title = 'Steam Flow Rate Comparison',
                    xaxis_title= 'Steam (Kg/hour)',
                    yaxis_title= feature,
                    transition_duration= 500)
    
    range_efficiency = str(efficiency[0]) + " - " + str(efficiency[1])
    return fig, range_efficiency