import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_html_components.Img import Img
import plotly.express as px
from app import app


graph_1 =  dbc.Card(children=[
        dbc.CardBody([html.Div([
                    html.Div(html.Img(src="/../assets/images/Luis.jpeg", className='img-about'), className='wrapper-img-about'),
                    
                    html.Div(children=[
                        html.H3("Project Leader"),
                        html.H4("Luis Fernando Rico"),
                        html.H5("Chemical Engineering"),
                        html.H6("Email: luisf.ricoo@gmail.com"),
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
                    html.Div(html.Img(src="/../assets/images/ana_photo.jpeg", className='img-about'), className='wrapper-img-about'),
                    html.Div(children=[
                        html.H3("Data Analyst"),
                        html.H4("Ana María Gómez"),
                        html.H5("MSc Statistics"),
                        html.H6("Email: anamago3@gmail.com"),
                        html.H6("Cell: 318 383 7029"), 
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
                    html.Div(html.Img(src="/../assets/images/Nestor_calvo_foto.jpeg", className='img-about'), className='wrapper-img-about'),
                    html.Div(children=[
                        html.H3("Full-stack Developer"),
                        html.H4("Néstor Rafael Calvo"),
                        html.H5("Electronic Engineering student"),
                        html.H6("Email: nestorcalvoa@gmail.com"),
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
                    html.Div(html.Img(src="/../assets/images/maryelin_photo.jpeg", className='img-about'), className='wrapper-img-about'),
                    html.Div(children=[
                        html.H3("Data Analyst"),
                        html.H4("Maryelin Del Valle Pérez"),
                        html.H5("Master Business Analytics"),
                        html.H6("Email: perez.c.maryelin@gmail.com"),
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
                    html.Div(html.Img(src="/../assets/images/Foto_Juan_Pablo.png", className='img-about'), className='wrapper-img-about'),
                    html.Div(children=[
                        html.H3("Engineering and Front-end Assistant"),
                        html.H4("Juan Pablo Suárez"),
                        html.H5("Energy engineering student"),
                        html.H6("Email: juan.suarezr@udea.edu.co"),
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
                    html.Div(html.Img(src="/../assets/images/Jorge_Lopez.jpeg", className = "img-about"), className='wrapper-img-about'),
                    html.Div(children=[
                        html.H3("General Assistant"),
                        html.H4("Jorge Hernán López"),
                        html.H5("PhD Physics"),
                        html.H6("Email: jhlopezm2@gmail.com"),
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
        graph_1,
        graph_2,
        graph_3,
        graph_4,
        graph_5,
        graph_6,
], className = "wrapper__about-us-data")
        
layout = [
    html.Div(children = [
        # html.Div(children = [

        #     # html.Img(
        #     #     src = "/assets/images/C1_icon_1.png",
        #     #     className = "corr-icon"
        #     # ),
        # ], className = "icons-wrapper"),
        html.Img(
            src = "/assets/images/Buencafe-logo.png",
            className = "corr-icon"
        ),
        # html.Img(
        #     src = "/assets/images/C1_icon_1.png",
        #     className = "corr-icon"
        # ),
        html.H2(
            "About Us",
            className = "content-title"
        ),
        grouped_cards],className = "wrapper__about-us"),
]