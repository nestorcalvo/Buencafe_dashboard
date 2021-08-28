import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
from app import app#, database

#df = database.get_csv("airports.csv")
#fig = px.histogram(df, x="Code", height=340)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length", height=340)

graph_1 =  dbc.Card(
    [
        dcc.Graph(figure=fig),
    ],
    style={"min-height":"20rem","max-height":"20rem"},
)

graph_2 =  dbc.Card(
    [
        dcc.Graph(figure=fig),
    ],
    style={"min-height":"20rem","max-height":"20rem"},
)

graph_3 =  dbc.Card(
    [
        dcc.Graph(figure=fig),
    ],
    style={"min-height":"20rem","max-height":"20rem"},
)

grouped_cards = html.Div(children=[dbc.Row(children=[dbc.Col(graph_1, style={'paddingTop':'2rem'})]),dbc.Row([dbc.Col(graph_2, style={'paddingTop':'2rem'}),
        dbc.Col(graph_3, style={'paddingTop':'2rem'})])])
        
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