# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:27:59 2024
@author: Vijay.Babu
"""
import os
import pandas as pd
import numpy as np
from GPT_API_Extract.chat_GPT_API_client_summary_extract import get_client_Data_main
from generate_client_summary_html.generate_summary_html import fn_generate_summary_html
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Get the current working directory
current_directory = os.getcwd()

def fn_create_line_chart(df_chart_data):
    plt.figure(figsize=(12, 6))
    df_chart_data['yearmonth'] = pd.to_datetime(df_chart_data['yearmonth'].astype(str) + '01', format='%Y%m%d')
    for inventory in df_chart_data['INVENTORY'].unique():
        subset = df_chart_data[df_chart_data['INVENTORY'] == inventory]
        plt.plot(subset['yearmonth'], subset['Rev-Lac'], marker='o', label=inventory)
    plt.xlabel('Year-Month')
    plt.ylabel('Revenue (Lac)')
    plt.title('Revenue by Inventory Type')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return image_base64

def fn_create_bar_chart_new(df_chart_data):
    df_chart_data['yearmonth'] = pd.to_datetime(df_chart_data['yearmonth'].astype(str) + '01', format='%Y%m%d')
    fig = px.bar(
        df_chart_data,
        x='yearmonth',
        y='Rev-Lac',
        color='INVENTORY',
        title='Revenue by Inventory Type',
        labels={'Rev-Lac': 'Revenue (Lac)', 'yearmonth': 'Year-Month'}
    )
    fig.update_layout(
        xaxis_title='Year-Month',
        yaxis_title='Revenue (Lac)',
        xaxis_tickangle=-45,
        legend_title='Inventory Type',
        barmode='group',
        bargap=0.2,
        width=400,
        height=300
    )
    return fig

def fn_adex_create_pie_chart_new(df_chart_data):
    df_pie_data = df_chart_data.groupby('Parent_Publication')['Vol_scm'].sum().reset_index()
    df_pie_data = df_pie_data.sort_values(by='Vol_scm', ascending=False)
    top_5 = df_pie_data.head(5)
    others = df_pie_data.iloc[5:].sum()
    if len(df_pie_data) > 5:
        others_row = pd.DataFrame([['Others', others['Vol_scm']]], columns=['Parent_Publication', 'Vol_scm'])
        df_pie_data = pd.concat([top_5, others_row], ignore_index=True)
    fig = px.pie(df_pie_data, values='Vol_scm', names='Parent_Publication', title='Volume Distribution by Parent Publication, Source: ADEX')
    fig.update_traces(textinfo='label+percent', pull=[0.1 if i < 5 else 0 for i in range(len(df_pie_data))])
    fig.update_layout(
        legend=dict(
            itemsizing='trace',
            title='Parent Publication',
            traceorder='normal',
            itemclick='toggleothers'
        )
    )
    return fig

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
app.layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f4f4f9', 'padding': '20px'},
    children=[
        # Header Section
        html.Section(
            className="header",
            style={'width': '100%', 'height': '70px', 'textAlign': 'center', 'backgroundColor': '#2b3e50', 'color': 'white', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'},
            children=[
                html.Label(
                    "Client Lead Generation AI",
                    style={'fontSize': '28px', 'fontWeight': 'bold'}
                )
            ],
        ),
        html.Div(
            style={'textAlign': 'center', 'marginTop': '20px'},
            children=[
                dcc.Input(id='input-box', type='text', placeholder='Enter Client Name...', style={'padding': '10px', 'width': '300px', 'borderRadius': '5px', 'border': '1px solid #ccc'}),
                html.Button('Submit', id='submit-button', n_clicks=0, style={'padding': '10px 20px', 'borderRadius': '5px', 'border': 'none', 'backgroundColor': '#2b3e50', 'color': 'white', 'marginLeft': '10px'}),
            ]
        ),
        html.Div(id='output-container', style={'marginTop': '20px'})
    ]
)

@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-box', 'value')
)
def update_output2(n_clicks, client_name):
    if n_clicks is None:
        raise PreventUpdate
    
    check_input_st_count = len(client_name)
    if not client_name:
        return "No input provided"
    if check_input_st_count <= 5:
        return "Kindly provide valid prompt"
    
    client_name = client_name.upper()
    df_API_client_summary= get_client_Data_main(client_name, current_directory)
    company = df_API_client_summary.iloc[0]
    html_result = fn_generate_summary_html(company, current_directory)
    
    df_bw_client_actual_data = pd.read_excel("df_bw_client_actual_data.xlsx")
    if len(df_bw_client_actual_data) > 0:
        df_bw_client_actual_data['Calendar_Date'] = pd.to_datetime(df_bw_client_actual_data['Calendar_Date'])
        df_bw_client_actual_data['yearmonth'] = df_bw_client_actual_data['Calendar_Date'].dt.strftime('%Y%m')
        df_bw_client_actual_data['yearmonth'] = df_bw_client_actual_data['yearmonth'].astype(int)
        df_bw_client_actual_data = df_bw_client_actual_data.sort_values(by='yearmonth')
        df_bw_client_actual_data = df_bw_client_actual_data.groupby(['yearmonth', 'INVENTORY']).agg({'Rev-Lac': 'sum'})
        df_bw_client_actual_data = df_bw_client_actual_data.reset_index()
        if len(df_bw_client_actual_data) > 0:
            plotly_fig = fn_create_bar_chart_new(df_bw_client_actual_data)
            result_display_bw = html.Div([dcc.Graph(figure=plotly_fig)])
        else:
            result_display_bw = None

    str_bw_client_search = "Found in BW & existing client"
    
    df_adex_result = pd.read_excel("df_adex_result.xlsx")
    if len(df_adex_result) > 0:
        df_adex_result['YearMonth'] = df_adex_result['YearMonth'].astype(int)
        df_adex_result = df_adex_result.sort_values(by='YearMonth')
        df_adex_result_print = df_adex_result[df_adex_result['Medium'] == 'PRINT']
        df_adex_result_print = df_adex_result_print.groupby(['YearMonth', 'Parent_Publication']).agg({'Vol_scm': 'sum'})
        df_adex_result_print = df_adex_result_print.reset_index()
        if len(df_adex_result_print) > 0:
            plotly_fig = fn_adex_create_pie_chart_new(df_adex_result_print)
            result_display = html.Div([dcc.Graph(figure=plotly_fig)])
        else:
            result_display = None
    else:
        result_display = None
    
    output_div_price_tab = html.Div(
        [
            html.Div(
                children=[
                    html.Iframe(srcDoc=html_result, style={'width': '900px', 'height': '550px', 'border': 'none', 'textAlign': 'left', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'margin': '20px 0'})
                ],
                style={'textAlign': 'left', 'margin': '0 auto'}
            ),
            html.Div(
                children=[
                    html.Div(
                        str(str_bw_client_search),
                        style={'textAlign': 'left', 'marginLeft': '50px', 'fontSize': '24px', 'color': 'blue', 'marginBottom': '6px'}
                    ),
                    html.Div(
                        children=[result_display_bw], style={'width': '400px', 'height': '300px', 'border': 'none', 'margin': '10px auto'}
                    ),
                    html.Div(
                        children=[result_display], style={'width': '400px', 'height': '300px', 'border': 'none', 'margin': '10px auto'}
                    )
                ],
                style={'textAlign': 'left', 'marginLeft': '5px'}
            )
        ],
        style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start', 'flexWrap': 'wrap'}
    )

    return output_div_price_tab

if __name__ == '__main__':
    app.run_server(debug=False)
