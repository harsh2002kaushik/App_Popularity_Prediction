#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:16:35 2021

@author: harsh
"""


import pickle
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

model = pickle.load(open('model.pkl','rb'))

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    children = [
        html.H1('Enter the details to predict the type of interest rate that will be applied on you',
                style = {
                    'textAlign':'center',
                    }
                ),
        html.Hr(),
        html.P('game_types'),
        dcc.Input(id='game_types', type='text', placeholder='game_types'),
        html.Hr(),
        html.P('comments'),
        dcc.Input(id='comments', type='text', placeholder='comments'),
        html.Hr(),
        html.P('price'),
        dcc.Input(id='price', type='text', placeholder='price'),
        html.Hr(),
        html.P('updated'),
        dcc.Input(id='updated', type='text', placeholder='updated'),
        html.Hr(),
        html.P('size'),
        dcc.Input(id='size', type='text', placeholder='size'),
        html.Hr(),
        html.P('required_android'),
        dcc.Input(id='required_android', type='text', placeholder='required_android'),
        html.Hr(),
        html.P('content_rating'),
        dcc.Input(id='content_rating', type='text', placeholder='content_rating'),
        html.Hr(),
        html.P('game_features'),
        dcc.Input(id='game_features', type='text', placeholder='game_features'),
        html.Hr(),
        html.P('interactive_elements'),
        dcc.Input(id='interactive_elements', type='text', placeholder='interactive_elements'),
        html.Hr(),
        html.P('in_app_products_avg'),
        dcc.Input(id='in_app_products_avg', type='text', placeholder='in_app_products_avg'),
        html.Hr(),
        html.P('has_website'),
        dcc.Input(id='has_website', type='text', placeholder='has_website'),
        html.Hr(),
        html.P('stars'),
        dcc.Input(id='stars', type='text', placeholder='stars'),
        html.Hr(),
        html.Button("Get Prediction", id = 'get_prediction', n_clicks=0),
        html.Hr(),
        html.Br(),
        html.P(id='model_output', style = {
            'textAlign': 'center',
            })
        ])

@app.callback(
    Output(component_id='model_output', component_property='children'),
    Input(component_id='game_types', component_property='value'),
    Input(component_id='comments', component_property='value'),
    Input(component_id='price', component_property='value'),
    Input(component_id='updated', component_property='value'),
    Input(component_id='size', component_property='value'),
    Input(component_id='required_android', component_property='value'),
    Input(component_id='content_rating', component_property='value'),
    Input(component_id='game_features', component_property='value'),
    Input(component_id='interactive_elements', component_property='value'),
    Input(component_id='in_app_products_avg', component_property='value'),
    Input(component_id='has_website', component_property='value'),
    Input(component_id='stars', component_property='value'),
    Input(component_id='get_prediction', component_property='n_clicks')
    )


def get_prediction( game_types, comments, price, updated, size, required_android, content_rating, game_features, interactive_elements, in_app_products_avg, has_website, stars, get_prediction):
    if get_prediction>0:
        if  None in [ game_types, comments, price, updated, size, required_android, content_rating, game_features, interactive_elements, in_app_products_avg, has_website, stars]:
            if  '' in [ game_types, comments, price, updated, size, required_android, content_rating, game_features, interactive_elements, in_app_products_avg, has_website, stars]:
                return 'Please add all the values'
            return 'Please add all the values'
        game_types = int(game_types)
        comments = int(comments)
        price = int(price)
        updated = int(updated)
        size = int(size)
        required_android = int(required_android)
        content_rating = int(content_rating)
        game_features = int(game_features)
        interactive_elements = int(interactive_elements)
        in_app_products_avg = int(in_app_products_avg)
        has_website = int(has_website)
        stars = int(stars)        

        array = [[game_types, comments, price, updated, size, required_android, content_rating, game_features, interactive_elements, in_app_products_avg, has_website, stars]]
        rate = model.predict(array)[0]
        
        return rate
get_interest = 0
n_clicks = 0
if __name__=='__main__':
    PORT = 3000
    app.run_server(port = PORT)
