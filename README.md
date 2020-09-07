# VA DATA PANDAS

The following is a project that answers the question "What is the risk of going back to schools
in Virginia in the Fall?" The latest update to the data was 8/17/20. Typing the command:
```python app.py``` in the terminal will create the page. From there go to this link ```http://127.0.0.1:8050/```
which will host the Plotly dash application on your local device. 

# Notes and Other Information

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



### If there is an error with Plotly

I have spent about 3-4 months with Plotly. From what I understand, if there is a problem with one of the libaries of Plotly not working as it is supposed to then it is advised to uninstall and then reinstall said libraries. https://github.com/plotly/dash-table/issues/496

If you have a problem when trying to find a tutorial on the plotly website it will be better for you to go to the Plotly forums or github issues to look for your question. Much of the time when there is an error with the code you have even if it is the same as the Plotly code, it is likely because the Plotly website code was not updated yet. 

README last updated: 
9/6/2020
