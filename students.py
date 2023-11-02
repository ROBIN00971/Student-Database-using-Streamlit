import streamlit as st
import pandas as pd
def app():
    st.header("Student Database:male-student:")
    st.subheader("Add View Delete")
    choice=st.selectbox('Choose Operation',['Add Student','View Student','Delete Student'],key="StudentsBox")
    if choice=="Add Student":
        st.write("Add")
    if choice=="View Student":
        st.write("View")
    if choice=="Delete Student":
        st.write("Delete")