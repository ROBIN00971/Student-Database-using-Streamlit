import streamlit as st
import pandas as pd
import uuid 


def app():
    st.header("Session Database:calendar:")
    st.subheader("Add View Delete")
    choice = st.selectbox('Choose Operation', ['Add Session', 'View Session', 'Delete Session'], key="sessionzBox")
    df = pd.read_csv("Csv//Sessions.csv")
    
    if choice == "Add Session":
        with st.form(key="Teacherform", clear_on_submit=True):
            # id = uuid.uuid1() 
            sessionId = st.number_input("Id",min_value=1000,max_value=9999)
            
            sessionName = st.text_input("Name")
            sessionDate = st.date_input("Date")
            startTime = st.time_input("Start Time")
            endTime = st.time_input("End Time")
            sessionType = st.text_input("Type")
            sessionPart = st.number_input("Participants")

            if st.form_submit_button("Add"):
                to_add = {
                    "Name": [sessionName],
                    "Date": [sessionDate],
                    "SessionId": [sessionId],
                    "StartTime": [startTime],
                    "EndTime": [endTime],
                    "SessionType": [sessionType],
                    "Participants": [sessionPart]
                }
                to_add = pd.DataFrame(to_add)
                df = pd.concat([df, to_add], ignore_index=True)
                df.to_csv("Csv//Sessions.csv", index=False)
                st.success("Submitted")

    if choice == "View Session":
        st.table(df)

    if choice == "Delete Session":
        selectedName = st.selectbox("Search", df["Name"], key="DeleteBox")
        if st.button("Delete", key="DeleteButton"):
            df = df[df["Name"] != selectedName]
            df.to_csv("Csv//Sessions.csv", index=False)
            st.success("Deleted Teacher: {}".format(selectedName))
