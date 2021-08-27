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
                        html.H3("Project Leader", style={'margin-bottom':'6px'}),
                        html.H4("Luis Fernando Rico", style={'margin-bottom':'6px'}),
                        html.H5("Chemical Engineering", style={'margin-bottom':'6px'}),
                        html.H6("Email: luisf.ricoo@gmail.com", style={'margin-bottom':'6px'}),
                        dbc.CardLink("Luis Fernando Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/luis-fernando-rico-ortiz/"),], 
                        className="about-text")
                    ])
                ])
    ], className = "cards-about"
)

graph_2 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H3("Data Analyst", style={'margin-bottom':'6px'}),
                        html.H4("Ana María Gómez", style={'margin-bottom':'6px'}),
                        html.H5("MSc Statistics", style={'margin-bottom':'6px'}),
                        html.H6("Email: anamago3@gmail.com", style={'margin-bottom':'6px'}),
                        html.H6("Cell: 318 383 7029", style={'margin-bottom':'6px'}), 
                        dbc.CardLink("Ana María Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/ana-g%C3%B3mez-51a5b1180/"),],
                        className="about-text")
                    ]) 
                ])
    ],
    className = "cards-about"
)

graph_3 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H3("Full-stack Developer", style={'margin-bottom':'6px'}),
                        html.H4("Néstor Rafael Calvo", style={'margin-bottom':'6px'}),
                        html.H5("Electronic Engineering student", style={'margin-bottom':'6px'}),
                        html.H6("Email: nestorcalvoa@gmail.com", style={'margin-bottom':'6px'}),
                        dbc.CardLink("Néstor Rafael Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/nestor-calvo-476294195/"),],
                        className="about-text")
                    ])
                ])
    ],
    className = "cards-about"
)

graph_4 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto.png", className='img-about')),
                    html.Div(children=[
                        html.H3("Data Analyst", style={'margin-bottom':'6px'}),
                        html.H4("Maryelin Del Valle Pérez", style={'margin-bottom':'6px'}),
                        html.H5("Master Business Analytics", style={'margin-bottom':'6px'}),
                        html.H6("Email: perez.c.maryelin@gmail.com", style={'margin-bottom':'6px'}),
                        dbc.CardLink("Maryelin Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/maryelin-p%C3%A9rez-70481b83/"),],
                        className="about-text")
                    ])
                ])
    ],
    className = "cards-about"
)

graph_5 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Foto_Juan_Pablo.png", style={'height':'22%', 'width':'30%'}, className='img-about')),
                    html.Div(children=[
                        html.H3("Engineering and Front-end Assistant", style={'margin-bottom':'6px'}),
                        html.H4("Juan Pablo Suárez", style={'margin-bottom':'6px'}),
                        html.H5("Energy engineering student", style={'margin-bottom':'6px'}),
                        html.H6("Email: juan.suarezr@udea.edu.co", style={'margin-bottom':'6px'}),
                        dbc.CardLink("Juan Pablo Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/juan-pablo-su%C3%A1rez-ram%C3%ADrez-810667200/"),],
                        className="about-text")
                    ])
                ])
    ],
    className = "cards-about"
)

graph_6 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Jorge_Lopez.jpeg", className='img-about')),
                    html.Div(children=[
                        html.H3("General Assistant", style={'margin-bottom':'6px'}),
                        html.H4("Jorge Hernán López", style={'margin-bottom':'6px'}),
                        html.H5("PhD Physics", style={'margin-bottom':'6px'}),
                        html.H6("Email: jhlopezm2@gmail.com", style={'margin-bottom':'6px'}),
                        dbc.CardLink("Jorge Hernán Linkedin", 
                                    style={'font-family': 'Times', 'font-weight': 'bold'}, 
                                    href="https://www.linkedin.com/in/jorge-hern%C3%A1n-lopez-b50a5394/"),],
                        className="about-text")
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