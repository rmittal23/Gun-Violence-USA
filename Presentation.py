
# coding: utf-8

# # Gun Violence in United States: 2019-2020  

# <h2>Source: Gun Violence Archive</h2> 

# <b>Current News: Ammo.com shows increase in revenue about 300%<br></br></b>
# 
# The COVID-19 pandemic has caused a surge in gun sales. Estimates based on background checks show that an estimated 2.6 million guns were sold in the United States in March.
# <h1>"The Coronavirus Has Gun Sales Soaring. Fear Is Selling to the Wrong Person."</h1>

# In[1]:


import pandas as pd
from sorted_months_weekdays import *
from sort_dataframeby_monthorweek import *
df_mass = pd.read_csv(r'C:\Users\adi3m\Desktop\presentation\mass shooing.csv')
df_mass['Incident Date'] = pd.to_datetime(df_mass['Incident Date'])


# In[2]:


df_mass.head()


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
#fig, ax = plt.subplots(figsize=(10,5))
import matplotlib.pyplot as plt
df_2019 = df_mass[df_mass['Year']==2019]
df19=df_2019.groupby('Month')[['Killed']].sum().reset_index()
df19=Sort_Dataframeby_MonthandNumeric_cols(df = df19, monthcolumn='Month',numericcolumn='Killed')
df191=df_2019.groupby('Month')[['Injured']].sum().reset_index()
df191=Sort_Dataframeby_MonthandNumeric_cols(df = df191, monthcolumn='Month',numericcolumn='Injured')
df_2020 = df_mass[df_mass['Year']==2020]
df20=df_2020.groupby('Month')[['Killed']].sum().reset_index()
df20=Sort_Dataframeby_MonthandNumeric_cols(df = df20, monthcolumn='Month',numericcolumn='Killed')
df201=df_2020.groupby('Month')[['Injured']].sum().reset_index()
df201=Sort_Dataframeby_MonthandNumeric_cols(df = df201, monthcolumn='Month',numericcolumn='Injured')
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(20, 5))
ax0.plot('Month', 'Injured', data=df191, label='Injured')
ax0.plot('Month', 'Killed', data=df19,label='killed')
ax1.plot('Month', 'Injured', data=df201, label='Injured')
ax1.plot('Month', 'Killed', data=df20,label='killed')
ax0.legend()
ax1.legend()         
ax0.grid(True)
ax1.grid(True)
ax0.set_title('2019 Gun Violence')
ax1.set_title('2020 Gun Violence')


# <h2> Map for Gun Violence in 2019</h2>

# In[6]:


import folium
map_usa = folium.Map(location=[37.0902, -95.7129],zoom_start=4)
for lat, lng, city, state, killed, injured, month in zip(df_2019['Latitude'], df_2019['Longitude'], df_2019['City Or County'],df_2019['State'], df_2019['Killed'], df_2019['Injured'], df_2019['Month']):
    label = 'City: {}, State:{}, Killed: {}, Injured: {}, Month:{}'.format(city,state,killed,injured, month)
    folium.CircleMarker(
        [lat, lng],
        radius=injured,
        popup=label,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.1,
        parse_html=False).add_to(map_usa)
map_usa


# <h2> Map for Gun Violence in 2020</h2>

# In[12]:


import folium
map_usa2 = folium.Map(location=[37.0902, -95.7129],zoom_start=4)
for lat, lng, city, state, killed, injured, month in zip(df_2020['Latitude'], df_2020['Longitude'], df_2020['City Or County'],df_2020['State'], df_2020['Killed'], df_2020['Injured'], df_2020['Month']):
    label = 'City: {}, State:{}, Killed: {}, Injured: {}, Month:{}'.format(city,state,killed,injured, month)
    folium.CircleMarker(
        [lat, lng],
        radius=injured,
        popup=label,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2,
        parse_html=False).add_to(map_usa2)
map_usa2


# In[136]:


get_ipython().system('pip install sorted-months-weekdays')


# In[138]:


get_ipython().system('pip install sort-dataframeby-monthorweek')

