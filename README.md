# VA DATA PANDAS by Shreyas Bera

The following project answers the question "What is the risk of going back to schools in Virginia in the Fall of 2020 during the COVID-19 pandemic?"  The latest update of the school data was 8/17/20. The latest cases data was updated on 8/28/20. The main reason for the latest data dates being different is due to two reasons.

1.	I had to find the data by going to each county web page and looking at specifically what their reopening plan was. 8/17/20 is when I finally the then current information about reopening plans. However, this is no longer the most current information as many hybrid schools have now gone into remote learning. The data is only relevant to the time it was collected and due to the fluidity of the situation plans change.

2.	I do not have a webscraper in place to harvest the data from the VDH database. This means the process of copying, pasting, cleaning, and loading the data is done manually. Doing it manually is time consuming. 

:octocat:
```yaml
VERSION 4 IS THE LATEST VERSION!!
```
:octocat:
## Running the Website

1. Go into the command prompt and select the path where ```app.py``` is located
2. ```python app.py``` in the terminal will create the page.
 * You should get the following from your prompt : 
 ```console
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 
 ```
3. From there go to this link ```http://127.0.0.1:8050/``` which will host the Plotly dash application on your local device. 
* If this page does not load then check the console again. If there is text after the ```Debug mode : on``` line which is not from a print command in the program, then there is an error in the code. It may be a problem with the libraries - goto **Required Libraries**. It may also be a problem with the code if you have been editing the code in ```app.py```.


## Notes and Other Information

 1.**Required Libaries** 
If you are running this on your local machine you will require to have installed the following
libaries: 
  ```
  re
  pandas
  dash
  plotly.express
  ```
  2. **Miniconda terminal** 

If for some reason you are unable to ```pip3``` or ```pip``` install these then I would reccomend
using the **Anaconda Prompt(miniconda3)** terminal. This is the link: https://docs.anaconda.com/anaconda/install/ . 

After you get said terminal then type in the following command : ```conda install -c plotly plotly``` and/or
```conda install -c conda-forge dash```. After it is done searching it will give a list of libraries and imports
that will also be installed. Type ```y``` and enter. Afterwards you should be able to run the program as long as
you have all the pre-requesites listed in note number **1**. 

*If you continue to have problems with libraries continue to the next explanation*



## Plotly Side Error

I have spent about 3-4 months using Plotly. From what I understand, if there is a problem with one of the libaries of Plotly not working as it is supposed to then it is advised to uninstall and then reinstall said libraries https://github.com/plotly/dash-table/issues/496 . Bugs like these will sometimes cause your code to work one day but not work the next. __Before you uninstall any library you should make sure that it is a problem with the library and not any problem with the code or computer.__


## Project Data & Data Report
__Data__ : https://docs.google.com/spreadsheets/d/1SAW-p09weC2KjyDR5pGPScxM79TPL4VIbMWpczjlBJ4/edit?usp=sharing


__Data Report__ : https://docs.google.com/document/d/1hpRszvJcM9FMXhDuTRkwINe9tbEGUBWYZ3cMXpf2t84/edit?usp=sharing

__Original CSS__ (I later changed some of it): https://github.com/plotly/dash-sample-apps/blob/master/apps/dash-uber-rides-demo/assets/style.css

[![Run on Repl.it](https://repl.it/badge/github/TST314/dataPanda)](https://repl.it/github/TST314/dataPanda)

### README last updated: 
#### 9/14/2020
