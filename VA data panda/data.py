import os
import pathlib
import re
import pandas
import json


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.title = "PANDAS REPORT AND DATA"


fullData = pd.read_csv("file/VAplan4.csv")


#------LAYOUT-------
app.Layout = html.Div(children = [
    html.Div(className='row',
    children=[
        hml.H4("Data Report"),
        html.P("The data collected by “VA Data Pandas” is the census information of each Virginia county as well as the reopening plans for every county in Virginia due to the Covid-19 pandemic. Counties that are completely in person have the highest risk while those that are virtual have the lowest/no risk. This data is meant to be used while deciding how safe it is for schools to open during the Fall. "),
        html.Br(),
        html.P("I used my own perspective of the CDC school reopening guidelines to find the risk type of each county’s plan. ")
        ]
    ])





if __name__ =='__main__':
    app.run_server(debug=True)
