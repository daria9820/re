


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model





df = pd.read_excel('gdprussia.xlsx')





df




get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.oilprice, df.gdp)
plt.xlabel('oil price (US$)')
plt.ylabel('GDP, Russia (bln US$)')




reg = linear_model.LinearRegression()

reg.fit(df[['oilprice']], df.gdp)



reg.predict(df[['oilprice']])





get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.oilprice, df.gdp)
plt.xlabel('oil price (US$)')
plt.ylabel('GDP, Russia (bln US$)')
plt.plot(df.oilprice, reg.predict(df[['oilprice']]))




reg.predict([[150]])





reg = linear_model.LinearRegression()

reg.fit(df[['year','oilprice']], df.gdp)




reg.predict(df[['year','oilprice']])




reg.predict([[2025,100]])






