import streamlit as st
import chart_studio
from streamlit.type_util import Key
chart_studio.tools.set_credentials_file(username='zahraa.berjawi', api_key='7RNqzaXHjH4QY1La6h62')

import chart_studio.plotly as py
import plotly.figure_factory as ff
import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objects as go

import pandas as pd
import numpy as np


st.title("**♟**UFO Sightings**♟**")
st.write("Here, you can see the demo of a simple web-app dashboard."
"It will show you general information on UFO Sightings in USA.")

df = pd.read_csv('complete.csv', error_bad_lines=False, low_memory=False)

df = df.iloc[:2000]

mapbox_access_token = 'pk.eyJ1IjoiemFocmFhYmVyamF3aSIsImEiOiJja3Rlc3J0ZjYwMWt6MnZqeXpvejRsOTd1In0.HyveZary1O9PqpPJNRKk4Q'

site_lat = df.latitude
site_lon = df.longitude
locations_name = df.city


data = [
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=5,
            color='rgb(127, 60, 141)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    ),
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=3,
            color='rgb(220, 176, 242)',
            opacity=0.7
        ),
        hoverinfo='text'
    )]


layout = go.Layout(
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=28.376164985512588,
            lon=-0.3213979460247174
        ),
        pitch=0,
        zoom=0.2695168005796828,
        style='dark'
    ),
)

fig = dict(data=data, layout=layout) 
st.subheader("UFO Sightings in the World between 1949 and 1983")
st.plotly_chart(fig)


df = df[df['country'].notna()]

df = df[df['state'].notna()]

df = df[df['shape'].notna()]

#Sight rates in USA States
states_us = df[df.country == 'us']['state'].value_counts().index

states_ratio = df[df.country == 'us']['state'].value_counts().values

states_us = [i.upper() for i in states_us]

number = states_ratio.tolist()

df2 = pd.DataFrame(list(zip(states_us, number)),
               columns =['US States', 'Number of Sightings'])




st.subheader("Number of Sightings in Different American States")

fig = px.bar(df2, x='US States', y='Number of Sightings', color = 'Number of Sightings', range_y=[0,200],
             color_continuous_scale=px.colors.sequential.Sunsetdark)

st.plotly_chart(fig)



CHOICES = dict(tuple(x) for x in df2.to_records(index=False))

def format_func(option):
    return CHOICES[option]


option = st.selectbox("State", options=list(CHOICES.keys()))
st.write(f"The number of UFO sightings in {option} between 1949 and 1983 is {format_func(option)}")


# Shapes of Sighted UFOs

shape = df['shape'].value_counts().index
shapes_numbers = df['shape'].value_counts().values.tolist()

df3 = pd.DataFrame(list(zip(shape, shapes_numbers)),
               columns =['UFO Shapes', 'Number of Sightings'])

fig = px.bar(df3, x='UFO Shapes', y='Number of Sightings', color = 'Number of Sightings', range_y=[0,400],
             color_continuous_scale=px.colors.sequential.Viridis)

st.subheader("Shapes of Sighted UFOs")
st.plotly_chart(fig)


#Interactive Map on UFO Sightings in USA
data = [
        dict(
        type='choropleth',
        locations = states_us,
        z = states_ratio,
        locationmode = 'USA-states',
        colorscale='sunsetdark',
        text = "Sightings",
        marker_line_color='white',
        colorbar = dict(
            title = "Sight rates by states")
        )
        ]

layout = dict(
        title = 'UFO Sight Numbers in USA',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(55,126,184)'),
              )


fig = go.Figure(data=data, layout=layout)

st.plotly_chart(fig)


CHOICES = {'yes': "Great you did! Thank you!", 'No' : "Please include your further recommendations below. Thank you!"}

def format_func(option):
    return CHOICES[option]


option = st.selectbox("Enjoyed the Visualization?", options=list(CHOICES.keys()))
st.write(f"{format_func(option)}")

sentence = st.text_input('Input your recommendations here:') 

if sentence:
    st.write(my_model.predict(sentence))