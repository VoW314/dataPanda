
#IMPORTS
#Analytics and path imports
import os #good for working with files
import pathlib #find path
import re #all importable objects are compiled regular expressions
import pandas as pd #data analytics library
import json

#Dash imports
import plotly.express as px #maps
import dash #the main library
import dash_core_components as dcc #dash components
import plotly.graph_objs as go
import dash_html_components as html #html dash components
from dash.dependencies import Input, Output, State #Allows user inputs and outputs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.title = "VA DATA PANDAS"

#IMPORT AND CLEAN DATA
#this is the same code from my datasplitter.ipynb file
VAplan = pd.read_csv('files/VAplan4.csv')
VAplan = VAplan[pd.notnull(VAplan['Risk'])]

#High Risk
highRk = VAplan[ VAplan['Risk'] == "High"]
highRk.to_csv('files/dsplit/Highrisk.csv')

#low Risk
lowRk = VAplan[ VAplan['Risk'] == "Low"]
lowRk.to_csv('files/dsplit/Lowrisk.csv')

#moderate Risk
modRk = VAplan[ VAplan['Risk'] == "Moderate"]
modRk.to_csv('files/dsplit/Modrisk.csv')

#still planning
spRk = VAplan[ VAplan['Risk'] == "still planning"]
spRk.to_csv('files/dsplit/sp.csv')

#only special needs are at risk as they come into school
osn = VAplan [ VAplan['Risk'] == "only special need in-person"]
osn.to_csv('files/dsplit/osn.csv')

VAmap = json.load(open("files/VAmap.geojson", "r"))


#CREATE DATAFRAMES
VAplan = pd.DataFrame(VAplan, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
high = pd.DataFrame(highRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
mod = pd.DataFrame(modRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
low = pd.DataFrame(lowRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
sp = pd.DataFrame(spRk,columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
osn = pd.DataFrame(osn, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])


#-------------------------------
colors = {
    'background' : '#d8dadd',
    'text' : '#fbfbfb'
}


#FIGURES px
high = px.bar(high, x="County", y="Number of Students", color='Risk',
            title="High Risk Counties", barmode='group', height=500, hover_data=['Cases'],
            color_discrete_sequence=['#de7070'])

mod = px.bar(mod, x="County", y='Number of Students',
                        hover_data=['Risk', 'Cases'],color='Risk', height=500, title="Moderate Risk Counties",
                        color_discrete_sequence=['#cfd64c']*len(mod))

low = px.bar(low, x="County", y='Number of Students',
                        hover_data=['Risk', 'Cases'],color='Risk', height=500, color_discrete_sequence=['#6dbd73'],
                         title="Low Risk Counties")


full = px.bar(VAplan, x="County", y='Number of Students',
                        hover_data=['Risk', 'Cases'],color='Risk')

#mapF = px.choropleth(VAplan, geojson=VAmap, color='Risk', locations='FIPS',
#                    projection="mercator", hover_data=["Cases", "Risk"])



#--------------------------------------------------------
#layout


app.layout = html.Div(children = [
    html.Div(className='row',
    children=[
        html.Div(className='four columns div-user-controls',
        children=[
            html.H2("How Safe is it to Open Schools in VA during the Fall?"),
            html.P('The following charts show the objective risk of almost every counties re-opening plan in Virginia.This data was last updated on 08-17-20. The risk is based off the plans for the county. When hovered over, bars will tell the Risk, County, Number of Students, and Number of Cases'),
            html.Br()
        ]),
        html.Div(id='page-content')
        ]),
        html.Div(
        children=[
            dcc.Graph(
            id='rks',
            figure=high,
            )

        ]),
        html.Div(
        children=[
        dcc.Graph(
        id='rks2',
        figure=mod,
        )
        ]),
        html.Div(
        children=[
        dcc.Graph(
        id='rks3',
        figure=low,
        )
        ]),
        html.Div(
            children=[
            html.Br(),
            html.H4("Data Report"),
            html.P("The data collected by “VA Data Pandas” is the census information of each Virginia county as well as the reopening plans for every county in Virginia due to the Covid-19 pandemic. Counties that are completely in person have the highest risk while those that are virtual have the lowest/no risk. This data is meant to be used while deciding how safe it is for schools to open during the Fall. "),
            html.Br(),
            html.P("I used my own perspective of the CDC school reopening guidelines to find the risk type of each county’s plan. ")
            ]
        )
    ])




if __name__ =='__main__':
    app.run_server(debug=True)
