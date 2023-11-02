import streamlit as st
import pandas as pd
def app():
    st.header("Session Database:calendar:")
    st.subheader("Add View Delete")
    choice=st.selectbox('Choose Operation',['Add Session','View Session','Delete Session'],key="sessionzBox")
    if choice=="Add Session":
        st.write("Add")
    if choice=="View Session":
        st.write("View")
    if choice=="Delete Session":
        st.write("Delete")