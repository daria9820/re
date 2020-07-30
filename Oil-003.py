#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Импортируем модули и библиотеки


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[5]:


df = pd.read_excel('gdprussia.xlsx')


# In[24]:


df


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.oilprice, df.gdp)
plt.xlabel('oil price (US$)')
plt.ylabel('GDP, Russia (bln US$)')


# In[12]:


# Тренируем модель


# In[13]:


reg = linear_model.LinearRegression()

reg.fit(df[['oilprice']], df.gdp)


# In[14]:


# Предсказываем


# In[15]:


reg.predict(df[['oilprice']])


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.oilprice, df.gdp)
plt.xlabel('oil price (US$)')
plt.ylabel('GDP, Russia (bln US$)')
plt.plot(df.oilprice, reg.predict(df[['oilprice']]))


# In[18]:


reg.predict([[150]])


# In[20]:


# Модель, предсказывающая ВВП в зависимости от 1) года и 2) от цены на нефть


# In[21]:


reg = linear_model.LinearRegression()

reg.fit(df[['year','oilprice']], df.gdp)


# In[22]:


reg.predict(df[['year','oilprice']])


# In[23]:


reg.predict([[2025,100]])


# In[ ]:




