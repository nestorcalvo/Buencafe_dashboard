import dash
from flask import Flask
import dash_bootstrap_components as dbc
from database_helper import DatabaseHelper

external_scripts =[
    {
        # Icons libraries
        'src': 'https://kit.fontawesome.com/b359ae410d.js',
        'crossorigin': 'anonymous'
    },
]
#database = DatabaseHelper('buencafeservers3')
server = Flask(__name__)
app = dash.Dash(__name__, server = server,external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts ,suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server