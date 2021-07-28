"""
Created on Mon Jul 26 12:20:45 2021

@author: BernieAC
"""

import dash
import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',

    'secondary': '#6E6E6E',
}

df = pd.read_csv(r'C:\Users\BernieAC\Displays\owtmaintenancetracker\Maintenance_Schedule.csv')

app.layout = html.Div([
    html.Div([
        html.H1('Maintenance Tracker'),
    html.Div([    
        dcc.Input(
            id='adding-rows-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-rows-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='adding-rows-table',

        columns=[
        {'name': 'Date', 'id': 'Date', 'type': 'datetime', 'editable': True},
        {'name': 'Equipment Name', 'id': 'Equipment Name', 'type': 'text'},
        {'name': 'Serial Number', 'id': 'Serial Number', 'type': 'any'},
        {'name': 'Frequency', 'id': 'Frequency', 'type': 'text'},
        {'name': 'Maintenance Tech Assigned', 'id': 'Maintenance Tech Assigned', 'type': 'text'},
        {'name': 'Status', 'id': 'Status', 'type': 'text'},
    ],
    editable=True,

        row_deletable=True,
        style_cell={
                'textAlign': 'left',
                'color': 'black'}
    ),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),

])
])

@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows


@app.callback(
    Output('adding-rows-table', 'columns'),
    Input('adding-rows-button', 'n_clicks'),
    State('adding-rows-name', 'value'),
    State('adding-rows-table', 'columns'))
def update_columns(n_clicks, value, existing_columns):
    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'renamable': True, 'deletable': True
        })
    return existing_columns



if __name__ == '__main__':
    app.run_server(debug=True)