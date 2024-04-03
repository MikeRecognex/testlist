import streamlit as st
from lib import run_mike  # Replace my_function with the actual function name

st.write('Hello')

if st.button('Click me'):
    result = run_mike()
    st.write(result)
