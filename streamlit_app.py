import streamlit as st
import pandas as pd

st.title('NBAPred')

st.info('Machine Learning For NBA Prediction!')

with st.expander('Data'):
  st.write('**Raw Data**')
  # Read in the data
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df # Display df in the app

  # Data excluding the species column
  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  # Species column
  st.write('**Y**')
  Y = df.species
  Y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='island')
