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
import dash_table

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


#other data
osn = VAplan [ VAplan['Risk'] == "only special need in-person"]
sp = VAplan [ VAplan['Risk']== 'still planning']
osn.to_csv('files/dsplit/osn.csv')
sp.to_csv('files/dsplit/osn.csv')

VAmap = json.load(open("files/VAmap.geojson", "r"))


#CREATE DATAFRAMES
VAplan = pd.DataFrame(VAplan, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
high = pd.DataFrame(highRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
mod = pd.DataFrame(modRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
low = pd.DataFrame(lowRk, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])
osn = pd.DataFrame(osn, columns =['County', 'Number of Students', 'Elementary School Plan', 'Secondary School Plan', 'Risk', 'FIPS', "Cases"])

#-------------------------------
colors = {
    'background' : '#d8dadd',
    'text' : '#fbfbfb'
}


#FIGURES px
high = px.bar(high, x="County", y="Number of Students",
            title="High Risk Counties", barmode='group', height=500, hover_data=['Cases', 'Secondary School Plan'],
            color_discrete_sequence=['#de7070'])


mod = px.bar(mod, x="County", y='Number of Students',
                     height=500, title="Moderate Risk Counties", hover_data=['Cases', 'Secondary School Plan'],
                        color_discrete_sequence=['#cfd64c'])

low = px.bar(low, x="County", y='Number of Students',
                         height=500, color_discrete_sequence=['#6dbd73'],
                         title="Low Risk Counties", hover_data=['Cases', 'Secondary School Plan'])

cases = px.bar(VAplan, x="County", y="Cases",
                hover_data=['FIPS', 'Cases', 'County'], title="Risk of All Counties")


mapF = px.choropleth(VAplan, geojson=VAmap, color='Risk', locations='FIPS',
                    projection="mercator", hover_data=["Cases", "Risk"])



#--------------------------------------------------------
#layout


app.layout = html.Div(children = [
    html.Div(className='row',
    children=[
        html.Div(className='four columns div-user-controls',
        children=[
            html.H2("How Safe is it to Open Schools in VA during the Fall?"),
            html.P('The following is a project that answers the question "What is the risk of going back to schools in Virginia in the Fall?" The latest update of the school data was 8/17/20. The latest cases data is 8/28/20. The main reason for the latest data dates being different is made up of two reasons. '),
            html.Br(),
            html.P('1. I had to find the data by going to each county web page and looking at specifically what there plan was. 8/17/20 is when I finally finished the search and a bit after I had finished the search for the information a local news station had collected all the data (which were just links to PDFs the school had given for their plans) for the reopening plans.'),
            html.P('2. I do not have a webscraper in place to harvest the data from VDH. The VDH data table for cases sometimes has multiple dates mixed meaning that one could find two of the same county in a list that should only have 1 of the county on a particular date.'),
            html.P("Data : https://docs.google.com/spreadsheets/d/1SAW-p09weC2KjyDR5pGPScxM79TPL4VIbMWpczjlBJ4/edit?usp=sharing ")
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
        dcc.Graph(
        id='cas1',
        figure=cases,
        )
        ]),
        html.Div(
            children=[
            html.Br(),
            html.H4("Data Report"),
            html.Br(),
            html.P('Made with Plotly - Dash'),
            html.P("Data Report : https://docs.google.com/document/d/1hpRszvJcM9FMXhDuTRkwINe9tbEGUBWYZ3cMXpf2t84/edit?usp=sharing")
            ]),


    ],
    )




if __name__ =='__main__':
    app.run_server(debug=True)

# this comment is here as I am just doing some practice with github desktop

#Created a new branch to practice even more! :D