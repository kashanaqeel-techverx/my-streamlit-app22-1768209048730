import streamlit as st
import pandas as pd

st.title("My Streamlit App")
st.write("Hello from Streamlit!")

# Sample data
data = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})

st.line_chart(data)
