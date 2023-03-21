from config import *
from dash import html
from dash.dependencies import Input, Output
from dash import dcc

from components import relatorio, extrato, sidebar

content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.laytout
        ], md=2, className="mt-5"),
        dbc.Col([
            content
        ], md=10)
    ])
], fluid=True)

@app.callback(Output(component_id='page-content', component_property='children'),Input(component_id='url', component_property='pathname'))
def render_page(pathname):
    if pathname == '/' or pathname == '/relatorio':
        return relatorio.layout
    else:
        return extrato.layout

if __name__ == '__main__':
    app.run(port=8051, debug=True)