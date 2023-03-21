import dash_bootstrap_components as dbc
from dash import html

laytout = html.Div(children=[
    dbc.Nav([
        dbc.NavLink(children="Relatório", href="/relatorio", active="exact"),
        dbc.NavLink(children="Extrato", href="/extrato", active="exact")
    ])
])