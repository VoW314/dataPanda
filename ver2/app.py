
#Analytics and path imports
import os #good for working with files
import pathlib #find path
import re #all importable objects are compiled regular expressions
import pandas as pd #data analytics library

#Dash imports
import plotly.express as px #maps
import dash #the main library
import dash_core_components as dcc #dash components
import plotly.graph_objects as go
import dash_html_components as html #html dash components
from dash.dependencies import Input, Output, State #Allows user inputs and outputs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

#import and clean the data
VAplan = pd.read_csv('files/VAplan2.csv')
VAplan = VAplan[pd.notnull(VAplan['Risk'])]

VAplan = pd.DataFrame(VAplan, columns =['locations', 'studentNum', 'Elem_plan', 'Second_plan', 'Risk']) #creates a dataFrame based off VAplan
VAplan2 = VAplan.groupby(['locations'])[['studentNum']].mean() #gets the student number per county
VAplan2.reset_index(inplace=True)

print(VAplan2)
print("---------------")
print(VAplan)
#-------------------------------

fig = px.bar(VAplan, x="locations", y='studentNum',
                        hover_data=['Risk'],color='Risk')


app.layout = html.Div(children = [
    html.H1(children='Number of Students Per County'),
    html.P(children="The following is a bar chart. I am  working on making it into a map using plotly and geojson files"),
    html.Div(children='''Dash: A web application framework for Python'''),
    dcc.Graph(
        id='students',
        figure=fig
    )




])

if __name__ =='__main__':
    app.run_server(debug=True)
