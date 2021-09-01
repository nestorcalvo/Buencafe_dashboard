import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
from app import app#, database
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_dangerously_set_inner_html

#df = database.get_csv("airports.csv")
#fig = px.histogram(df, x="Code", height=340)
import numpy as np
from joblib import dump, load



fig = go.Figure()

inputs = html.Div(className = "left-input", children = [
    html.Label(children = ["Input 1",
        html.Div(className = "wrapper-input", children = [
            dcc.Input(id="input2", type="text", placeholder="", debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4("Lorem, ipsum", className = "questionTitle"),
                    html.P("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor, quae", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
html_pure = ('''
    <div class="wrapperPredictions">
      <div class="pagePredictions">
        <h2 class="pagePredictionsTitle">Title</h2>
        <div class="predictionsMainText">
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus quibusdam suscipit totam laboriosam dignissimos libero, amet nesciunt voluptatem obcaecati odit officiis facilis ipsum magni
            tenetur unde harum commodi, deserunt eaque minima odio ex itaque sed iste. Expedita reiciendis sapiente, vel quidem ad sed neque illum quaerat atque cupiditate culpa dolores harum pariatur
            optio ab doloremque commodi eum minima qui eveniet quod veritatis! Doloremque inventore iure minima eos velit totam molestiae.
          </p>
        </div>
        <div class="predictionsSecondRow">
          <div class="predictionsLeftContainer">
            <div class="left-input">
              <label for=""
                >Input1
                <div class="wrapper-input">
                  <input type="text" />
                  <div class="questionMark">
                    <div class="questionIcon">?</div>
                    <div class="questionMarkInfo">
                      <h4 class="questionTitle">Lorem, ipsum.</h4>
                      <p class="questionDescription">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor, quae.</p>
                    </div>
                  </div>
                </div>
              </label>
            </div>
            <div class="left-input">
              <label for=""
                >Input1
                <div class="wrapper-input">
                  <input type="text" />
                  <div class="questionMark">
                    <div class="questionIcon">?</div>
                    <div class="questionMarkInfo">
                      <h4 class="questionTitle">Lorem, ipsum.</h4>
                      <p class="questionDescription">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor, quae.</p>
                    </div>
                  </div>
                </div>
              </label>
            </div>
          </div>
          <div class="predictionsRightContainer">
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Asperiores at magnam aperiam cumque numquam molestiae laudantium commodi perferendis fugit tempora.</p>
            <div class="rangeBar">
              <span>Numero</span>
              <div id="rangeBarFill"></div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
''')
prediction_zone = html.Div(className = "wrapperPredictions", children =[
    html.Div(className = "pagePredictions", children = [
        html.H2('Title', className = "pagePredictionsTitle"),
        html.Div(className = "predictionsMainText", children = [
            html.P("Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus quibusdam suscipit totam laboriosam dignissimos libero, amet nesciunt voluptatem obcaecati odit officiis facilis ipsum magni")            
        ]),
        html.Div(className = "predictionsSecondRow", children = [
            html.Div(className = "predictionsLeftContainer", children = [
                inputs,
                inputs
            ]),
            html.Div(className = "predictionsRightContainer", children = [
                html.P("Lorem ipsum dolor sit amet consectetur, adipisicing elit. Asperiores at magnam aperiam cumque numquam molestiae laudantium commodi perferendis fugit tempora."),
                html.Div(className = "rangeBar", children = [
                    html.Span(children = ["0"], id = "spanNumber"),
                    html.Div(id = "rangeBarFill")
                ]),
                html.Div(children = [
                    html.Button("Predict", id = 'PredictButton', className = "theButton", n_clicks = 0),
                ])
            ])
        ])
    ])
])
# <div><button class="theButton" id="PredictButton">Predict</button></div>

graph_1 =  dbc.Card(
    [
        dcc.Graph(id='graph-efficiency', className = "graph-card"),
    ],
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
        # html.Hr(style={'border-color':'black'}),
        html.Hr(),
        html.H6("Gas range"),
        slider_gas,
        html.P(id='range-gas'),
    ],
)

sliders_2 = dbc.Card(
    [   
        html.H6("Borra range"),
        slider_borra,
        html.P(id='range-borra'),
        # html.Hr(style={'border-color':'black'}),
        html.Hr(),
        html.H6("Cisco range"),
        slider_cisco,
        html.P(id='range-cisco')
    ],
)





grouped_cards = html.Div(children=[
    dbc.Row(children=[dbc.Col(sliders_2)]),
    dbc.Row(children=[dbc.Col(graph_1)]),
    dbc.Row(children=[dbc.Col(sliders_1)]),
    
    ], className = "wrapper__efficiency-data")

        
layout = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        # dash_dangerously_set_inner_html.DangerouslySetInnerHTML(html_pure),
        prediction_zone,
        html.H2(
            "Efficiency Analytics",
            className = "content-title"
        ),
        grouped_cards],
        className = "wrapper__efficiency"
    ),
]

@app.callback(Output('spanNumber', 'children'),[Input('PredictButton','n_clicks')])
def predict_efficiency(n_clicks):
    print(n_clicks)
    if (n_clicks>0):
        
        model = load('./model/randomforest1.joblib')

        X_test = np.array([32.78, 873.1317110666666, 26944.993760166668, 17.038507456333335, 753.9847037783333,
        103.151764405, 12.6772637935, -8.071795385133333, 104.95246840333331, 252.17223876,
        186.72663326, 76.19234134666667, 3016.064416257234, 842.3078503490352])

        print(model.predict(X_test.reshape(1, -1))[0])
        return [str(round(model.predict(X_test.reshape(1, -1))[0]*100, 2))]
    else:
        return [str(0)]
    
    

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
    df = pd.read_csv("data/data_interpolate_hourly.csv") #Cambiar esta linea por la base de datos del servidor
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
