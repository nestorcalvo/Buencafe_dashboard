import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
from app import app#, database
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_dangerously_set_inner_html
import requests
#df = database.get_csv("airports.csv")
#fig = px.histogram(df, x="Code", height=340)
import numpy as np
# import grequests
from joblib import dump, load

features = ["Screw Speed", "Steam Flow Rate", "Steam Pressure", "Oven-Home Temperature",
            "Water Temperature", "Oxygen_pct", "Oven-Home Pressure", "Combustion Air Pressure",
            "Temperature before prear", "Temperature after prear", "Burner Position", "Burner_pct", 
            "Borra Flow Rate", "Cisco Flow Rate"]


fig = go.Figure()

inputs = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[0],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input", value = 37.78, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[0], className = "questionTitle"),
                    html.H6("Cycles per second of the screw. Units (Hz)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs2 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[1],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input2", value = 873.13, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[1], className = "questionTitle"),
                    html.H6("Steam generated in the boiler. Units (Kg/h)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs3 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[2],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input3", value = 26944.99, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[2], className = "questionTitle"),
                    html.H6("Pressure of the steam generated. Units (Bar)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs4 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[3],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input4", value = 17.04, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[3], className = "questionTitle"),
                    html.H6("Temperature of the oven after combustion. Units (Celsius)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs5 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[4],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input5", value = 753.98, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[4], className = "questionTitle"),
                    html.H6("Water's temperature before of entry to the boiler. Units (Celsius)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])

inputs6 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[5],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input6", value = 103.15, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[5], className = "questionTitle"),
                    html.H6("Oxygen percentage of the combustion air. Units (%)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs7 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[6],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input7", value = 12.67, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[6], className = "questionTitle"),
                    html.H6("Pressure of the oven after combustion. Units (mmH2O)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs8 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[7],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input8", value = -8.07, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[7], className = "questionTitle"),
                    html.H6("Pressure of the combustion air. Units (mmH2o)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs9 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[8],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input9", value = 104.95, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[8], className = "questionTitle"),
                    html.H6("Temperature of the combustion gases after boiler, before \"prear\". Units (Celsius)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs10 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[9],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input10", value = 252.17, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[9], className = "questionTitle"),
                    html.H6("Temperature of the combustion gases after \"prear\". Units (Celsius)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])

inputs11 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[10],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input11", value = 186.72, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[10], className = "questionTitle"),
                    html.H6("Burner position given by plc. Units (%)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs12 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[11],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input12", value = 72.192, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[11], className = "questionTitle"),
                    html.H6("Burner position given by transmisor in operation. Units (%)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs13 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[12],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input13", value = 3016.06, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[12], className = "questionTitle"),
                    html.H6("Borra with 60% of humidity consumed in the combustion. Units (%)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])
inputs14 = html.Div(className = "left-input", children = [
    html.Label(className = "wrapper-label", children = [features[13],
        html.Div(className = "wrapper-input", children = [
            dbc.Input(type = "number", id="input14", value = 842.30, debounce=True),
            html.Div(className = "questionMark", children = [
                html.Div("?", className = "questionIcon"),
                html.Div(className = "questionMarkInfo", children =[
                    html.H4(features[13], className = "questionTitle"),
                    html.H6("Cisco with 20% of humidity consumed in the combustion. Units (%)", className = "questionDescription")
                ])
            ])
        ]),
    ])
])



# html_pure = ('''
#     <div class="wrapperPredictions">
#       <div class="pagePredictions">
#         <h2 class="pagePredictionsTitle">Title</h2>
#         <div class="predictionsMainText">
#           <p>
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus quibusdam suscipit totam laboriosam dignissimos libero, amet nesciunt voluptatem obcaecati odit officiis facilis ipsum magni
#             tenetur unde harum commodi, deserunt eaque minima odio ex itaque sed iste. Expedita reiciendis sapiente, vel quidem ad sed neque illum quaerat atque cupiditate culpa dolores harum pariatur
#             optio ab doloremque commodi eum minima qui eveniet quod veritatis! Doloremque inventore iure minima eos velit totam molestiae.
#           </p>
#         </div>
#         <div class="predictionsSecondRow">
#           <div class="predictionsLeftContainer">
#             <div class="left-input">
#               <label for=""
#                 >Input1
#                 <div class="wrapper-input">
#                   <input type="text" />
#                   <div class="questionMark">
#                     <div class="questionIcon">?</div>
#                     <div class="questionMarkInfo">
#                       <h4 class="questionTitle">Lorem, ipsum.</h4>
#                       <p class="questionDescription">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor, quae.</p>
#                     </div>
#                   </div>
#                 </div>
#               </label>
#             </div>
#             <div class="left-input">
#               <label for=""
#                 >Input1
#                 <div class="wrapper-input">
#                   <input type="text" />
#                   <div class="questionMark">
#                     <div class="questionIcon">?</div>
#                     <div class="questionMarkInfo">
#                       <h4 class="questionTitle">Lorem, ipsum.</h4>
#                       <p class="questionDescription">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor, quae.</p>
#                     </div>
#                   </div>
#                 </div>
#               </label>
#             </div>
#           </div>
#           <div class="predictionsRightContainer">
#             <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Asperiores at magnam aperiam cumque numquam molestiae laudantium commodi perferendis fugit tempora.</p>
#             <div class="rangeBar">
#               <span>Numero</span>
#               <div id="rangeBarFill"></div>
#             </div>
            
#           </div>
#         </div>
#       </div>
#     </div>
# ''')
prediction_zone = html.Div(className = "wrapperPredictions", children =[
    html.Div(className = "pagePredictions", children = [
        html.H2('Efficiency Analytics', className = "pagePredictionsTitle"),
        
        html.Div(className = "predictionsMainText", children = [
          html.P("The energetic efficiency is an indication of the boiler’s capacity to burn fuel and absorb the heat generated for the steam. The development of a model capable of estimating the best fuel composition will generate the steam the most efficiently possible, which implies better management of the resources and an improvement in the economic income. Finding the best point of operation of the steam boiler will have a positive impact on the nearby communities and the environment, making the company sustainable and more competitive in terms of energy efficiency, resource management, and social responsibility."),
          html.P()
          # dbc.Card(
              # dbc.CardBody([
              # ]),
          # ),
        ]),
        html.Div(className = "predictionsSecondRow", children = [
            dbc.Card(
              dbc.CardBody([
            # html.Div(children = [
                html.Div(className = "inputs-cards", children = [
                  dbc.Card(
                    dbc.CardBody([
                      inputs,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs2,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs3,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs4,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs5,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs6,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs7,
                    ], className = "card-body_inputs"),
                  ),dbc.Card(
                    dbc.CardBody([
                      inputs8,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs9,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs10,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs11,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs12,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs13,
                    ], className = "card-body_inputs"),
                  ),
                  dbc.Card(
                    dbc.CardBody([
                      inputs14,
                    ], className = "card-body_inputs"),
                  ),
                  # dbc.Card(
                  #   dbc.CardBody([
                  #     inputs15,
                  #   ], className = "card-body_inputs"),
                  # ),

            # ])
            # ], className = "predictionsLeftContainer"),


                ]),
              ]), color="light",className = "predictionsLeftContainer"),
            html.Div(className = "predictionsRightContainer", children = [
                html.P("A model was trained in order to perform predictions on the efficiency, by clicking predict you would be able to obtain the efficiency of the process and find interactively how the variables interact with each other."),
                html.Div(className = "rangeBar", children = [
                    html.Span(children = ["0"], id = "spanNumber"),
                    html.Div(id = "rangeBarFill")
                ]),
                html.Div(className = "wrapper_theButton", children = [
                    dbc.Button("Predict", color = "success", size ="lg", id = 'PredictButton', className = "theButton", n_clicks = 0),
                    # html.Button("Predict", id = 'PredictButton', className = "theButton", n_clicks = 0),
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
    [   html.H3("Steam range", style={'alignSelf': 'center'}),
        slider_steam,
        html.H4(id='range-steam',style={'alignSelf': 'center'}),
        # html.Hr(style={'border-color':'black'}),
        html.Hr(),
        html.H3("Gas range",style={'alignSelf': 'center'}),
        slider_gas,
        html.H4(id='range-gas',style={'alignSelf': 'center'}),
    ],
)

sliders_2 = dbc.Card(
    [   
        html.H3("Borra range",style={'alignSelf': 'center'}),
        slider_borra,
        html.H4(id='range-borra',style={'alignSelf': 'center'}),
        # html.Hr(style={'border-color':'black'}),
        html.Hr(),
        html.H3("Cisco range",style={'alignSelf': 'center'}),
        slider_cisco,
        html.H4(id='range-cisco',style={'alignSelf': 'center'})
    ],
)





grouped_cards = html.Div(children=[
    dbc.Row(children=[dbc.Col(sliders_2)], className = "efficiency-slides"),
    dbc.Row(children=[dbc.Col(graph_1)],className="efficiency-graph"),
    dbc.Row(children=[dbc.Col(sliders_1)], className = "efficiency-slides"),
    
    ], className = "wrapper__efficiency-data")

        
layout = [
    html.Div(children = [
        # html.Img(
        #     src = "/assets/images/C1_icon_1.png",
        #     className = "corr-icon"
        # ),
        html.Img(
            src = "/assets/images/Buencafe-logo.png",
            className = "corr-icon"
        ),
        # dash_dangerously_set_inner_html.DangerouslySetInnerHTML(html_pure),
        prediction_zone,
        grouped_cards],
        className = "wrapper__efficiency"
    ),
]

@app.callback(
            Output('spanNumber', 'children'),
            [Input('PredictButton','n_clicks')],
            [
              State('input','value'),
              State('input2','value'),
              State('input3','value'),
              State('input4','value'),
              State('input5','value'),
              State('input6','value'),
              State('input7','value'),
              State('input8','value'),
              State('input9','value'),
              State('input10','value'),
              State('input11','value'),
              State('input12','value'),
              State('input13','value'),
              State('input14','value'),
            ])
def predict_efficiency(n_clicks,input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14):
    # print(n_clicks)
    if (n_clicks>0):
        
        model = load('./model/randomforest1.joblib')
        X_test = np.array([input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14])


        # print(model.predict(X_test.reshape(1, -1))[0])
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
    #query = f"SELECT * FROM hourly WHERE \"Steam Flow Rate\" < {steam[1]} and \"Steam Flow Rate\" > {steam[0]} and \"Gas Flow Rate\" > {gas[1]} and \"Gas Flow Rate\" > {gas[0]} and \"Borra Flow Rate_kgh\" > {borra[1]} and \"Borra Flow Rate_kgh\" > {borra[0]} and \"Cisco Flow Rate_kgh\" > {cisco[1]} and \"Cisco Flow Rate_kgh\" > {cisco[0]}"
    try:
        query = "SELECT * FROM hourly"
        payload = {
        "query": query
        }
        petition = requests.post('https://k8nmzco6tb.execute-api.us-east-1.amazonaws.com/dev/data',payload)
        test_var = petition.json()['body']
        # print(test_var[0])
        
        df = pd.DataFrame(test_var)
        # print(df.info())
    
        # df = pd.read_csv("data/data_interpolate_hourly.csv") #Cambiar esta linea por la base de datos del servidor
        df = df[(df['Steam Flow Rate'] <steam[1]) & (df['Steam Flow Rate'] >steam[0]) \
                & (df['Gas Flow Rate'] <gas[1]) & (df['Gas Flow Rate'] >gas[0]) \
                & (df['Borra Flow Rate_kgh'] <borra[1]) & (df['Borra Flow Rate_kgh'] >borra[0]) \
                & (df['Cisco Flow Rate_kgh'] <cisco[1]) & (df['Cisco Flow Rate_kgh'] >cisco[0])]

        fig = px.histogram(df, x= "Efficiency", height=340, nbins=50)

        fig.update_layout(title = 'Efficiency distribution',
                        xaxis_title='Efficiency',
                        yaxis_title='Count',
                        transition_duration=500,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)')
                        
        range_steam = str(steam[0]) + "kg/h - " + str(steam[1]) + "kg/h"
        range_gas = str(gas[0]) + "m3/h - " + str(gas[1]) + "m3/h"
        range_borra = str(borra[0]) + "kg/h - " + str(borra[1]) + "kg/h"
        range_cisco = str(cisco[0]) + "kg/h - " + str(cisco[1]) + "kg/h"

        return fig, range_steam, range_gas, range_borra, range_cisco
    except:
        
        fig = px.histogram()

        fig.update_layout(title = 'Efficiency distribution',
                        xaxis_title='Efficiency',
                        yaxis_title='Count',
                        transition_duration=500,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)')
                        
        range_steam = str(steam[0]) + "kg/h - " + str(steam[1]) + "kg/h"
        range_gas = str(gas[0]) + "m3/h - " + str(gas[1]) + "m3/h"
        range_borra = str(borra[0]) + "kg/h - " + str(borra[1]) + "kg/h"
        range_cisco = str(cisco[0]) + "kg/h - " + str(cisco[1]) + "kg/h"

        return fig, range_steam, range_gas, range_borra, range_cisco
