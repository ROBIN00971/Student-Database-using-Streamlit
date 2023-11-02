import streamlit as st
import pandas as pd
def app():
    st.header("Course Database:book:")
    st.subheader("Add View Delete")
    choice=st.selectbox('Choose Operation',['Add Course','View Course','Delete Course'],key="Coursebox")
    if choice=="Add Course":
        st.write("Add")
    if choice=="View Course":
        st.write("View")
    if choice=="Delete Course":
        st.write("Delete")