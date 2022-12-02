import streamlit as st

def text_input (question, kb_location, element_number):
    '''This functiono creates a txt input and adds the answer to the dedicated location in the kb
    and in the st.session_state'''

    st.markdown("### " + question["prompt"])
    string = st.columns(4)[0].text_input(question["prompt"], label_visibility="collapsed", key=element_number)
    variable_to_change = question["variable_to_change"]
    kb_location[variable_to_change] = string
    st.session_state[variable_to_change] = string

def yes_no_input (question, kb_location, element_number):
    st.markdown("### " + question["prompt"])
    answer = st.columns([1,9])[0].select_slider(question["prompt"], ["No", "Yes"], label_visibility="collapsed", key=element_number)
    variable_to_change = question["variable_to_change"]
    kb_location[variable_to_change] = "true" if answer=="Yes" else "false"
    st.session_state[variable_to_change] = True if answer=="Yes" else False

def slider_input(question, kb_location, element_number):
    st.markdown("### " + question["prompt"])
    answer = st.columns([1,2])[0].slider(question["prompt"], question["range_min"], question["range_max"], label_visibility="collapsed", key=element_number)
    variable_to_change = question["variable_to_change"]
    kb_location[variable_to_change] = answer
    st.session_state[variable_to_change] = answer

def number_input(question, kb_location, element_number):
    st.markdown("### " + question["prompt"])
    answer = st.columns([1,9])[0].number_input(question["prompt"], question["range_min"], question["range_max"], label_visibility="collapsed", key=element_number)
    variable_to_change = question["variable_to_change"]
    kb_location[variable_to_change] = answer
    st.session_state[variable_to_change] = answer

def time_input(question, kb_location, element_number):
    st.markdown("### " + question["prompt"])
    answer = st.columns([1,2])[0].slider(question["prompt"], question["range_min"], question["range_max"], label_visibility="collapsed", key=element_number)
    variable_to_change = question["variable_to_change"]
    kb_location[variable_to_change] = answer
    st.session_state[variable_to_change] = answer