import json
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(
    page_title = "tab name here",
    page_icon="🧊",
    layout='wide'
)

st.title("Productivity guide")

kb = json.load(open("kb.json", 'r'))

if "button1" not in st.session_state:
    st.session_state.button1 = False
if "counter" not in st.session_state:
    st.session_state.counter = 0
# session_state is important
# st.write("hello world")   # the default writing thing

# col1, col2, col3 = st.columns(3)   # creates three columns
# col1, col2 = st.columns([1,2])   # creates two columns with respective size
# with st.expander("click here to expand"):  # 1-time loop that expands some text

# col1.markdown("#Markdown text format")

# st.progress(0-100)    # shows progress of page
# st.success("Text success")    # Displays a small div to indicate success
# st.metric()   # some cool way of showing a metric

st.progress(25)

def increase_counter():
    st.session_state.counter += 1

st.markdown("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available. It is also used to temporarily replace text in a process called greeking, which allows designers to consider the form of a webpage or publication, without the meaning of the text influencing the design.")

colLeft, colRight = st.columns([1,4])
colLeft.checkbox("value1", key="first option", value=False, disabled=False, on_change=increase_counter)
colLeft.checkbox("value2", key="second option", value=False, disabled=False)

st.write(st.session_state.counter)
for i in range(st.session_state.counter):
    st.write(st.session_state["button1"])







#=====================OLD THTING=============================================

# st.title('[Title of the project]')


# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text('Loading done! (using st.cache)')

# #raw data
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# #nr of pickups per hour
# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
# )[0]
# st.bar_chart(hist_values)

# #plot data on a map
# st.subheader('Map of all pickups all day')
# st.map(data)

# #plot data on a map for 17:00
# st.subheader("Map of pickups around 17:00")
# hour_to_filter = 17
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.map(filtered_data)
