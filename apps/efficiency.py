import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
from app import app#, database
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

#df = database.get_csv("airports.csv")
#fig = px.histogram(df, x="Code", height=340)

fig = go.Figure()


graph_1 =  dbc.Card(
    [
        dcc.Graph(id='graph-efficiency'),
    ],
    style={"minHeight":"20rem","maxHeight":"20rem"},
)

slider_steam = dcc.RangeSlider(
        id='slider-steam',
        min=0,
        max=33000,
        step=1000,
        value=[0, 33000]
        )

slider_gas = dcc.RangeSlider(
        id='slider-gas',
        min=0,
        max=1200,
        step=40,
        value=[0, 1200]
        )

slider_borra = dcc.RangeSlider(
        id='slider-borra',
        min=0,
        max=4500,
        step=90,
        value=[0, 4500]
        )

slider_cisco = dcc.RangeSlider(
        id='slider-cisco',
        min=0,
        max=1300,
        step=50,
        value=[0, 1300]
        )


sliders_1 =  dbc.Card(
    [   html.H6("Steam range"),
        slider_steam,
        html.P(id='range-steam'),
        html.Hr(style={'border-color':'black'}),
        html.H6("Gas range"),
        slider_gas,
        html.P(id='range-gas'),
    ],
    style={"minHeight":"18rem","maxHeight":"18rem"},
)

sliders_2 = dbc.Card(
    [   
        html.H6("Borra range"),
        slider_borra,
        html.P(id='range-borra'),
        html.Hr(style={'border-color':'black'}),
        html.H6("Cisco range"),
        slider_cisco,
        html.P(id='range-cisco')
    ],

    style={"min-height":"18rem","max-height":"18rem"},
)





grouped_cards = html.Div(children=[
    dbc.Row(children=[dbc.Col(graph_1, style={'padding-top':'2rem'})]),
    dbc.Row(children=[dbc.Col(sliders_1, style={'padding-top':'2rem'}),dbc.Col(sliders_2, style={'padding-top':'2rem'})])])

        
layout = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "Efficiency Analitycs",
            className = "content-title"
        ),
        grouped_cards],
        className = "corr-icon-container"
    ),
]

@app.callback(
    [Output('graph-efficiency','figure'),
    Output('range-steam','children'),
    Output('range-gas','children'),
    Output('range-borra','children'),
    Output('range-cisco','children')],
    [Input('slider-steam', 'value'),
    Input('slider-gas', 'value'),
    Input('slider-borra', 'value'),
    Input('slider-cisco', 'value')]
)
def update_figure(steam, gas, borra, cisco) :
    df = pd.read_csv("KNN_hourly.csv") #Cambiar esta linea por la base de datos del servidor
    df = df[(df['Steam Flow Rate'] <steam[1]) & (df['Steam Flow Rate'] >steam[0]) \
            & (df['Gas Flow Rate'] <gas[1]) & (df['Gas Flow Rate'] >gas[0]) \
            & (df['Borra Flow Rate_kgh'] <borra[1]) & (df['Borra Flow Rate_kgh'] >borra[0]) \
            & (df['Cisco Flow Rate_kgh'] <cisco[1]) & (df['Cisco Flow Rate_kgh'] >cisco[0])]

    fig = px.histogram(df, x= "Efficiency", height=340, nbins=50)

    fig.update_layout(title = 'Efficiency distribution',
                    xaxis_title='Efficiency',
                    yaxis_title='Count',
                    transition_duration=500)
                    
    range_steam = str(steam[0]) + "kg/h - " + str(steam[1]) + "kg/h"
    range_gas = str(gas[0]) + "m3/h - " + str(gas[1]) + "m3/h"
    range_borra = str(borra[0]) + "kg/h - " + str(borra[1]) + "kg/h"
    range_cisco = str(cisco[0]) + "kg/h - " + str(cisco[1]) + "kg/h"

    return fig, range_steam, range_gas, range_borra, range_cisco
