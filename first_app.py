import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('My First Streamlit App')
st.write('Using data to create a table')

data = pd.DataFrame({
    'name': ['Rafael', 'Fernanda', 'Maicon', 'Henrique'],
    'lastname': ['Garcia', 'Menezes', 'Jobim', 'Boneto'],
    'age': [18, 22, 20, 22],
    'score': [9, 6, 10, 7],
    'course': ['Applied Physics', 'Computer Science', 'Engineering', np.nan] 
})
st.write(data)

st.write('Some charts')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write('Testing Checkbox')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

'Now a selectbox'
option = st.selectbox(
    'Which student do you want to select?',
     data['name'])

'You selected: ', option

option = st.sidebar.selectbox(
    'Select the best student of the year',
     data['name'])

'You selected:', option, 'for the best student of the year'