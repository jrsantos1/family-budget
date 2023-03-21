from config import *
from dash import html
from dash import dcc

app.layout = dbc.Container(children=[
    html.H1(children="Layout works")
])

if __name__ == '__main__':
    app.run(port=8051, debug=True)