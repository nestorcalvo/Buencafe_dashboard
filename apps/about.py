import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_html_components.Img import Img
import plotly.express as px
from app import app


graph_1 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)

graph_2 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)

graph_3 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)

graph_4 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)

graph_5 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)

graph_6 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H5("Card title", style={'margin-bottom':'6px'}),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus maximus lacus ut libero mattis placerat. Aenean metus nisi, consequat eget luctus et, sagittis a est. Nam mattis maximus diam, nec finibus lorem. Sed ultrices neque sapien, ac tempor justo sagittis id.",
                            className="card-text")], className="about-text")
                    ])

                    
                ])
    ],
    className = "cards-about"
)


grouped_cards = html.Div(children=[
        dbc.Row([dbc.Col(graph_1, style={'padding-top':'2rem'}),
                dbc.Col(graph_2, style={'padding-top':'2rem'})]),
        dbc.Row([dbc.Col(graph_3, style={'padding-top':'2rem'}),
                dbc.Col(graph_4, style={'padding-top':'2rem'})]),
        dbc.Row([dbc.Col(graph_5, style={'padding-top':'2rem'}),
                dbc.Col(graph_6, style={'padding-top':'2rem'})])
        ])
        
layout = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "About Us",
            className = "content-title"
        ),
        grouped_cards],
        className = "corr-icon-container"
    ),
]