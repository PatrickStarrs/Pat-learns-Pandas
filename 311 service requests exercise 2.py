#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


complaints = pd.read_csv('311-service-requests.csv')


# In[3]:


# looks at the  first 10 rows of the complaints dataframe 
complaints[:10]


# In[4]:



#sets noise_complaints where the complaint type == Noise is true. the first complaints selects the dataframe, the "complaints" in the bracket is used to select the column
noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]
noise_complaints[:3]


# In[5]:


# takes the Complaint column and returns true for when the complaints type = noise- street/sidewalk
complaints['Complaint Type'] == "Noise - Street/Sidewalk"


# In[6]:


# sets two variables, one where is_noise is defined as noise, annd in_brooklyn, which looks for Brooklyn. using the "&" you can select where the compalint is noise and located in brooklyn
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == "BROOKLYN"
complaints[is_noise & in_brooklyn][:5]


# In[7]:



#selects additional columns and displays the first 10 rows
complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10]


# In[8]:


#is_noise = where Complaint type is noise
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()


# In[11]:



noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()


# In[12]:


noise_complaint_counts / complaint_counts.astype(float)


# In[13]:




(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')


# In[ ]:




