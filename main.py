import streamlit as st
import pandas as pd
import numpy as np

st.title('[Title of the project]')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading done! (using st.cache)')

#raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#nr of pickups per hour
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
)[0]
st.bar_chart(hist_values)

#plot data on a map
st.subheader('Map of all pickups all day')
st.map(data)

#plot data on a map for 17:00
st.subheader("Map of pickups around 17:00")
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.map(filtered_data)
