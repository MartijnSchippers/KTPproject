''''main scipt'''
import json
import streamlit as st

from input_types import *

st.set_page_config(
    page_title = "tab name here",
    layout='wide'
)


if "activity" not in st.session_state:
    st.session_state.activity = ""
if "passion" not in st.session_state:
    st.session_state.activity = 0
if "weekly_workload" not in st.session_state:
    st.session_state.weekly_workload = 0

st.title("Productivity guide")

st.markdown("This is a project from Martijn and Mirko for the course \"Knowledge Technology Practical\"")

kb = json.load(open("kb.json", 'r'))

student_activity = kb["student properties"]["activity"]

for i,question in enumerate(student_activity["element_questions"]):
    match question["type"]:
        case "open_answer":
            text_input(question, student_activity, i)
        case "yes/no":
            yes_no_input(question, student_activity, i)
        case "slider":
            slider_input(question, student_activity, i)
# st.session_state.activity = st.columns([1,3])[0].text_input(activity_questions[0]["prompt"])

# st.session_state.passion = st.columns(2)[0].slider(activity_questions[1]["prompt"], 0, 10)

# st.session_state.weekly_workload = st.number_input(activity_questions[2]["prompt"], 0, 80)

# if st.button("Process information"):
#     st.markdown("# You have selected the following:")
#     st.write("You enjoy " + (st.session_state.activity).lower() + " "
#     + str(st.session_state.weekly_workload) + " hours per week")
