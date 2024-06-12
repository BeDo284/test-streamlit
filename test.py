import streamlit as st

# Sample project descriptions (replace with your actual data)
project_descriptions = {
    "Project A": "Description of Project A.",
    "Project B": "Description of Project B.",
    "Project C": "Description of Project C.",
    "Project D": "Description of Project D."
}

# Create a sidebar with a dropdown menu
st.sidebar.title("Project Selector")
selected_project = st.sidebar.selectbox("Select a project", list(project_descriptions.keys()))

# Define a session state to keep track of the selected project's description
session_state = st.session_state

if 'selected_project_description' not in session_state:
    session_state.selected_project_description = ""

# Display the selected project's description on a new page
if selected_project:
    session_state.selected_project_description = project_descriptions[selected_project]
    st.title(selected_project)
    st.write(session_state.selected_project_description)