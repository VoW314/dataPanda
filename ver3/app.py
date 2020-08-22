
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
app.title = "VA DATA PANDAS"

#import and clean the data
VAplan = pd.read_csv('files/VAplan3.csv')
VAplan = VAplan[pd.notnull(VAplan['Risk'])]

VAplan = pd.DataFrame(VAplan, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk']) #creates a dataFrame based off VAplan


print("---------------")
print(VAplan)
#-------------------------------

#figure properties
fig = px.bar(VAplan, x="County", y='Number of Students',
                        hover_data=['Risk'],color='Risk')


#layout
app.layout = html.Div(children = [
    #import css styling here
    html.H1(children='Number of Students Per County'),
    html.P(children="The following is a bar chart. The data is updated as of 8/17/20. If your county is not any of the charts then it means that your county did not post a plan before the date when this was last taken. "),
    dcc.Graph(
        id='students',
        figure=fig
    )


])

if __name__ =='__main__':
    app.run_server(debug=True)
