import dash_bootstrap_components as dbc
from dash import html
from dash import dash_table
from bll import bll
import pandas as pd

layout = dbc.Col(children=[
    dbc.Col(children=[
        dbc.Row([
            html.H1("Extrato")
        ], style={'height': '10vh'})
    ], md=12),
    dbc.Col([
        dbc.Row([
            dbc.Col([
                html.H4("últimos lançamentos"),
                dash_table.DataTable(data=bll.getGastos(), columns=[{'id': c, 'name': c} for c in pd.DataFrame(bll.getGastos()).columns], id='tb_extrato_id')
            ], md=6, style={'height': '90vh'}),
            dbc.Col([
                html.H1("Extrato")
            ], md=6)
        ], className='w-100')
    ], md=12)

])