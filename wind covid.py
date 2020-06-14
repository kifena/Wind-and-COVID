#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import plotly as py
import plotly.graph_objs as go
file = 'Case.csv'
data = pd.read_csv(file,sep=',',na_values='-')
pd.DataFrame.hist(data[['longitude']])
plt.xlabel('longitude')
plt.ylabel('count')
plt.show()


# In[ ]:





# In[38]:


Weather = 'Weather.csv'
WeatherData = pd.read_csv(Weather, sep=',')
Province = 'Province.csv'
ProvinceData = pd.read_csv(Province, sep=',')

Seoul = ProvinceData[ProvinceData[:]['province'] =='Seoul']
Seoul['difference'] = (Seoul.groupby(['province'])['confirmed']
                       .diff()
                       .fillna(Seoul['confirmed'])
                    .astype(int))

Seoul['date'] = pd.to_datetime(Seoul['date'])
#Seoul = Seoul[Seoul[:]['date']>datetime.date(2020,3,15)][:] #since march
#Seoul = Seoul[Seoul[:]['date']<datetime.date(2020,4,29)][:] #til april

#print(WeatherData['date'][])
#since 2020-01-13 (wind) + 2020-01-27 (confirmed), then 2020-01-12 (wind) + (2020-01-28 (confirmed) - 2020-01-27 (confirmed)) 
#for i in Seoul[1:]['confirmed']:
    #Seoul[i]['difference'] = abs(Seoul[i]['confirmed']-Seoul[i-1]['confirmed'])
#for i in range (1,2244,17):
    #Seoul['difference'] = Seoul.iloc[i].subtract(Seoul.iloc[i-1])

SeoulWeather = WeatherData[WeatherData[:]['province'] == 'Seoul']
SeoulWeather['date'] = pd.to_datetime(SeoulWeather['date'])
Wind = SeoulWeather[SeoulWeather[:]['date']>datetime.date(2020,1,5)][:] #since january

#Wind = SeoulWeather[SeoulWeather[:]['date']>datetime.date(2020,3,1)][:] #since march
#Wind = Wind[Wind[:]['date']<datetime.date(2020,4,15)][:] #til april

#SeoulWind['date'] = 
#SeoulWind = Seoul[:]['difference']
#SeoulWind.index = Seoul[:]['date']
#SeoulWind.to_frame()
#SeoulWind.rename(columns={'date' : 'date','' : 'cases increase'},inplace=True)
#SeoulWind['wind speed'] = Wind[:]['max_wind_speed']
#print(Wind)
#print(SeoulWind)

#Wind.plot(x = 'date',y='max_wind_speed',kind ='line')
#Seoul.plot(x = 'date',y='difference',kind='line')
#plt.legend()
trace_Wind = go.Scatter(
    x = Wind.date, 
    y = Wind.max_wind_speed,
    name = 'wind speed'
)
trace_Cases = go.Scatter(
    x = Seoul.date,
    y = Seoul.difference,
    name = 'cases increase'
)
fig = go.Figure()
fig.add_trace(trace_Wind)
fig.add_trace(trace_Cases)
fig.show()

#print(SeoulWind)
#print(Seoul)


# So I need to 0) GET DATA FOR ONLY ONE PROVINCE 1) get rid of not important info (ALL except wind speed) 2) plot all provinces on ONE plot (??) with different colors & X-axis is number of confirmed cases + Y-axis is the wind speed TWO WEEKS BEFORE THE DATE OF CONFIRMED
# (mb a direct formula like get the dates column of weather and choose those with index [dates_of_confirmed - 14 (days)] 
# 

# In[ ]:




