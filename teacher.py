import streamlit as st
import pandas as pd
import datetime
import re


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

    df = pd.read_csv("Csv//Teacher.csv")

    if choice == "Add Teacher":
        with st.form(key="Teacherform", clear_on_submit=True):
            teacherName = st.text_input("Name")
            teacherDate = st.date_input("Date")
            teacherEmail = st.text_input("Email")
            teacherGender = st.selectbox("Gender", ['Male', 'Female'])
            teacherPosition = st.text_input("Position")
            teacherSubject = st.text_input("Subject")

            if st.form_submit_button("Add"):
                if validate_email(teacherEmail):
                    to_add = {"Name": [teacherName], "Date": [teacherDate], "Email": [
                        teacherEmail], "Gender": [teacherGender], "Position": [teacherPosition], "Subject": [teacherSubject]}
                    to_add = pd.DataFrame(to_add)
                    df = pd.concat([df, to_add], ignore_index=True)
                    df.to_csv("Csv//Teacher.csv", index=False)
                    st.success("Submitted")
                else:
                    st.warning("Invalid Email")

    if choice == "View Teacher":
        st.table(df)

    if choice == "Delete Teacher":
        selectedName = st.selectbox("Search", df["Name"], key="DeleteBox")
        if st.button("Delete", key="DeleteButton"):
            df = df[df["Name"] != selectedName]
            df.to_csv("Csv//Teacher.csv", index=False)
            st.success("Deleted Teacher: {}".format(selectedName))
