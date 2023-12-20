#!/usr/bin/env python
# coding: utf-8

# 1. Sam has to build a bar-plot for the ‘Contract’ column
# a. Set the x-axis label to be ‘Contract Type of customer’
# b. Set the y-axis label to be ‘Count’
# c. Set the title of the plot to be ‘Distribution of Contract’
# d. Assign ‘orange’ color to all the bars 

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


customer=pd.read_csv('/home/mehnaz/Downloads/customer_churn.csv')


# In[5]:


customer


# In[10]:


customer['Contract'].value_counts()


# In[9]:


fig=plt.subplots()
customer['Contract'].value_counts().plot(kind='bar',color='orange')
#plt.bar(customer['Contract'].value_counts())


# Sam has to build a histogram for the ‘MonthlyCharges’ column
# a. Set the x-axis label to be ‘Monthly Charges Incurred’
# b. Set the y-axis label to be ‘Count’
# c. Set the title of the plot to be ‘Distribution of Monthly Charges’
# d. Assign ‘forestgreen’ color to the bins

# In[11]:


x=customer['MonthlyCharges']
plt.hist(x,color='forestgreen')
plt.xlabel('Monthly Charges Incurred')
plt.ylabel('Count')
plt.title('Distribution of Monthly Charges')


# 3. Sam has to build a scatter-plot between ‘TotalCharges’ & ‘tenure’. ‘TotalCharges’ should be on
# the y-axis and ‘tenure’ should be on the x-axis
# a. Set the x-axis label to be ‘Tenure of the customer’
# b. Set the y-axis label to be ‘Total charges Incurred’
# c. Set the title of the plot to be ‘Total Charges vs Tenure’
# d. Assign ‘indigo’ color to the points

# In[ ]:


import matplotlib.pyplot as plt
y=customer['TotalCharges']
x=customer['tenure']
plt.scatter(x,y)


# 4. Sam has to build a box-plot between ‘MonthlyCharges’ & ‘PaymentMethod’.
# ‘MonthlyCharges’ should be on the y-axis and ‘PaymentMethod’ should be on the x-axis.
# a. Set the x-axis label to be ‘Payment Method of customer’
# b. Set the y-axis label to be ‘Monthly Charges Incurred’
# c. Set the title of plot to be ‘Monthly Charges vs. Payment Method’
# d. Assign ‘olive’ color to the box-plots

# In[ ]:


import seaborn as sns
sns.boxplot(x='PaymentMethod',y='MonthlyCharges',data=customer,color='olive')


# In[ ]:




