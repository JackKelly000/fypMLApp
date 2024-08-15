import streamlit as st
import pandas as pd

st.title('NBAPred')

st.info('Machine Learning For NBA Prediction!')

# Read in the data
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
