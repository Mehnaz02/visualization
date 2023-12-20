#!/usr/bin/env python
# coding: utf-8

# 1. Load cars data as dataframe using pandas and create a bar plot between number of cylinders
# and frequency of cars with that many number of cylinders.
# - Set xlabel as Number of cylinders.
# - Set ylabel as Frequency of cars.
# - Draw a bar plot.2.

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


cars=pd.read_csv('/home/mehnaz/Desktop/intellipaat/python/notes/cars-1.csv')
cars.head()


# In[6]:


cars['cyl'].value_counts().plot(kind='bar')
#plt.bar(cars[''],cars[''])
plt.xlabel('Number of cylinders')
plt.ylabel('Frequency of cars')


# In[15]:


cars


# Write code to load data from cars and print a bar graph of count of columns with null values.

# In[12]:


cars.isnull().sum().plot(kind='bar')


# Use the 'mpg' (Miles Per Gallon column) and draw a histogram
# i. Set xlabel: Miles per gallon
# ii. Set ylabel: Frequency
# iii. Set title as Miles Per Gallon Histogram
# iv. Use mpg column to generate a histogram
# 

# In[44]:


x=cars['mpg']
plt.hist(x)
plt.xlabel('Miles per gallon')
plt.ylabel('Frequency')
plt.title('Miles Per Gallon Histogram')


# Draw a boxplot on the card dataframes hp column
# i. Set xlabel: Car Horsepower
# ii. Set title as Boxplot for car horsepower
# iii. Use hp column to generate a boxplot

# In[51]:


sns.boxplot(y=cars['carb'],data=cars)
plt.xlabel('Car Horsepower')
plt.title('Box for car horsepower')


# In[ ]:




