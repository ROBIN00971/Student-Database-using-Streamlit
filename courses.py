import streamlit as st
import pandas as pd
import re


def app():
    st.header("Courses Database:book:")
    st.subheader("Add View Delete")
    choice = st.selectbox('Choose Operation', ['Add Course', 'View Courses', 'Delete Course'], key="coursesBox")
    df = pd.read_csv("Csv//courses.csv")

    if choice == "Add Course":
        with st.form(key="CourseForm", clear_on_submit=True):
            courseCode = st.text_input("Course Code")
            courseTitle = st.text_input("Course Title")
            creditHours = str(st.number_input("Credit Hours"))+"hr"
            semester = st.text_input("Semester")
            department = st.text_input("Department")
            instructor = st.text_input("Instructor")

            if st.form_submit_button("Add"):
                to_add = {
                    "CourseCode": [courseCode],
                    "CourseTitle": [courseTitle],
                    "CreditHours": [creditHours],
                    "Semester": [semester],
                    "Department": [department],
                    "Instructor": [instructor]
                }
                to_add = pd.DataFrame(to_add)
                df = pd.concat([df, to_add], ignore_index=True)
                df.to_csv("Csv//courses.csv", index=False)
                st.success("Submitted")

    if choice == "View Courses":
        st.table(df)

    if choice == "Delete Course":
        selectedCourseCode = st.selectbox("Search", df["CourseCode"], key="DeleteCourseBox")
        if st.button("Delete", key="DeleteCourseButton"):
            df = df[df["CourseCode"] != selectedCourseCode]
            df.to_csv("Csv//courses.csv", index=False)
            st.success("Deleted Course: {}".format(selectedCourseCode))
