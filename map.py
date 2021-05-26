import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image
import pydeck as pdk
from urllib.error import URLError
import altair as alt
from collections import Counter 

 #mapdata
map_df2 = pd.read_csv('olive_3dmap.csv')

st.header("Map")
st.write("In progress...")
# st.write(map_df)
    
coordinates = pd.DataFrame({
        'lat':[36.240895,36.152476],
        'lon':[-86.756770,-86.857713],
        'name':['Split at Nashville','Merge at Nashville']
    })

@st.cache
def from_data_file(filename):
    url = (
            "https://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename)
    return pd.read_json(url)
st.dataframe(map_df2)
layer2 =  pdk.Layer(
                "HexagonLayer",
                data=map_df2,
                get_position=["lon", "lat"],
                radius=3700,
                elevation_scale=150,
                elevation_range=[0, 500],
                extruded=True,
            ),

st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={"latitude": 36.174465,
                                        "longitude": -86.767960, "zoom": 11, "pitch": 50},           
                    layers=[layer2],
                    tooltip={
        'html': '<b>Name:</b> {name}',
        'style': {
            'color': 'black'
        }
    },       
                ))


