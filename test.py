import streamlit as st
import pandas as pd

# Initialize a session state for the dataframe
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Name', 'Age', 'City'])

# Function to add data to the dataframe
def add_data(name, age, city):
    new_data = pd.DataFrame({'Name': [name], 'Age': [age], 'City': [city]})
    st.session_state['data'] = pd.concat([st.session_state['data'], new_data], ignore_index=True)

st.title('Add Data to DataFrame')

# Input form
with st.form(key='add_data_form'):
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0)
    city = st.text_input('City')
    submit_button = st.form_submit_button(label='Add Data')

# Add data if the form is submitted
if submit_button:
    add_data(name, age, city)
    st.success(f'Data added: {name}, {age}, {city}')

# Display the dataframe
st.write('Current Data:')
st.dataframe(st.session_state['data'])
