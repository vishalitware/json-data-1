#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd 
import numpy as np
import os 
os . chdir('D:\\New folder (111)\\')


# In[46]:


pip install demjson


# In[62]:


import json

# example dictionary to save as JSON
data  =[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

# save JSON file
# 1st option
with open("data1.json", "w") as f:
    json.dump(data, f)


# In[64]:


print(data)


# In[65]:


data


# In[75]:


def BMI(heigh, weight): 
  bmi = weight/(height**2) 
  return bmi 
height = 1.6616
weight = 57
bmi = BMI(height, weight) 
print("The BMI is", format(bmi))
print("Health status = ",end="")
if (bmi < 18.5): 
  print("Underweight") 
elif ( bmi >= 18.5 and bmi < 24.9): 
  print("Normal weight") 
elif ( bmi >= 25 and bmi < 29.5): 
  print("Overweight") 
elif ( bmi >= 30 and bmi < 34.5): 
  print("Moderately obese") 
elif ( bmi >= 35 and bmi < 39.5): 
  print("Severely obese")  
elif ( bmi >=40): 
  print("Very severely obese")


# In[ ]:




