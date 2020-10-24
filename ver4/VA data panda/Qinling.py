
'''
webscraper for VA data Pandas!
-----------
This will probably go into the main file unless because that is where all the
cleaning happens. That is for later.
'''

#IMPORTS
from bs4 import BeautifulSoup
import pandas as pd
import requests

#this data should be getting updated every 24 hours
#we will have to clean counties because not all counties have schools
res = requests.get("https://www.vdh.virginia.gov/coronavirus/coronavirus/covid-19-in-virginia-locality/")
print(res)
