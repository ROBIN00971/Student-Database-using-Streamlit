import streamlit as st
import pandas as pd
import datetime
import re

df = pd.read_csv("Csv//Teacher.csv")

def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern, email):
        return True
    return False

def app():
    st.header("Teacher Database:male-teacher:")
    st.subheader("Add View Delete")
    choice = st.selectbox('Choose Operation', [
        'Add Teacher', 'View Teacher', 'Delete Teacher'], key="TeacherBox")
    
    if choice == "Add Teacher":
        with st.form(key="Teacherform", clear_on_submit=True):
            teacherName = st.text_input("Name")
            teacherDate = str(datetime.datetime.now())
            teacherEmail = st.text_input("Email")
            teacherGender = st.selectbox("Gender", ['Male', 'Female'])
            teacherPosition = st.text_input("Position")
            teacherSubject = st.text_input("Subject")
            
            if st.form_submit_button("Add"):
                if validate_email(teacherEmail):
                    to_add = {"Name": [teacherName], "Date": [teacherDate], "Email": [
                        teacherEmail], "Gender": [teacherGender], "Position": [teacherPosition], "Subject": [teacherSubject]}
                    to_add = pd.DataFrame(to_add)
                    to_add.to_csv("Csv//Teacher.csv", mode='a',
                                header=False, index=False)
                    st.success("Submitted")
                else:
                    st.warning("Invalid Email")

    if choice == "View Teacher":
        st.table(df)
    
    if choice == "Delete Teacher":
        selectedName = st.selectbox("Search", df, key="DeleteBox")
        if st.button("Delete",key="DeleteButton"):
            cf = pd.read_csv("Csv//Teacher.csv")
            cf = cf[(cf["Name"] != selectedName)]

        
        
