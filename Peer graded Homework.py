#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0105EN-SkillsNetwork/labs/Module2/images/SN_web_lightmode.png" width="300" alt="cognitiveclass.ai logo">
# </center>
# 

# #### Add your code below following the instructions given in the course
# 

# # Title: Peer graded Homework

# Introduction:  
# 
# In this Jupyter NOtebook I will introduce the reader to the main tools for data science and name them

# data science languages:
# 
# Python
# Julia
# R

# data science libraries:
# 
# ggplott2
# caret
# pandas

# a table of Data Science tools:
# 
# Machine learning: scikit-learn, TensorFlow, PyTorch
# 
# Data Visualization: matplotlib, ggplot, Tableau, D3.js
# 
# Data Manipulation: pandas, dplyr, SQL, Apache Spark
# 
# 

# arithmetic expression examples:

# In[16]:


x= 2
y= 3
print(x+y)
print(x*y)


# In[36]:


def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   print("minutes value in hours:",hour)
   
   return "%02d:%02d:%02d" % (hour, min, sec) 

input(n)
print("Time in preferred format :-",convert_to_preferred_format(n))


# Objectives: they were succefully represneted to the reader 
# 

# the Author’s name:
# Faisal Ajin

# In[ ]:




