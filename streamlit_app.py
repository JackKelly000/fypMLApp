import streamlit as st
import pandas as pd

st.title('NBAPred')

st.info('Machine Learning For NBA Prediction!')

with st.expander('Data'):
  st.write('**Raw Data**')
  # Read in the data
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df # Display df in the app

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**Y**')
  Y = df.species
  Y
