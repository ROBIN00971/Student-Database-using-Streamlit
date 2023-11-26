import streamlit as st
import pandas as pd
import plotly.express as px
import time as t
def app():
    st.header("Dashboard:chart_with_upwards_trend:")
    
st.set_page_config(page_icon="📈", page_title='📊Graph📊')

st.markdown('<p style="color:pink; font-size:75px;">Data Evaluation:</p>', unsafe_allow_html=True)
st.success("....Go Ahead....")

teacher_data = pd.read_csv("Teacher.csv")
students_data = pd.read_csv("Students.csv")
course_data = pd.read_csv("Courses.csv")
session_data = pd.read_csv("Sessions.csv")

selected_data = st.selectbox('Select Data', ['Select Data', 'Teacher Data', 'Students Data', 'course data', 'session data'])
selected_chart_type = st.selectbox('Select Chart Type', ['Select Chart Type', 'Line Chart', 'Bar Chart', 'Pie Chart', 'Scatter Plot'])

if selected_data == 'Teacher Data':
    with st.spinner("Processing..."):
        t.sleep(3)

    st.title("Teacher Data")
    st.dataframe(teacher_data, width=1500, height=100)

    if selected_chart_type != 'Select Chart Type':
        if selected_chart_type == 'Line Chart':
            chart_data = st.selectbox('Select a column for the line chart', teacher_data.columns)
            chart = px.line(teacher_data, x=teacher_data.index, y=chart_data)
        elif selected_chart_type == 'Bar Chart':
            chart_data = st.selectbox('Select a column for the bar chart', teacher_data.columns)
            chart = px.bar(teacher_data, x=teacher_data.index, y=chart_data)
        elif selected_chart_type == 'Pie Chart':
            chart_column = st.selectbox('Select a column for the Pie Chart', teacher_data.columns)
            chart = px.pie(teacher_data, names=chart_column)
        elif selected_chart_type == 'Scatter Plot':
            x_axis = st.selectbox('Select x-axis column for scatter plot', teacher_data.columns)
            y_axis = st.selectbox('Select y-axis column for scatter plot', teacher_data.columns)
            chart = px.scatter(teacher_data, x=x_axis, y=y_axis)
        st.plotly_chart(chart)
    else:
        st.warning("Select a valid chart type")

elif selected_data == 'Students Data':
    with st.spinner("Processing..."):
        t.sleep(3)
    st.title("Students Data")
    st.dataframe(students_data, width=1500, height=100)

    if selected_chart_type != 'Select Chart Type':
        if selected_chart_type == 'Line Chart':
            chart_data = st.selectbox('Select a column for the line chart', students_data.columns)
            chart = px.line(students_data, x=students_data.index, y=chart_data)
        elif selected_chart_type == 'Bar Chart':
            chart_data = st.selectbox('Select a column for the bar chart', students_data.columns)
            chart = px.bar(students_data, x=students_data.index, y=chart_data)
        elif selected_chart_type == 'Pie Chart':
            chart_column = st.selectbox('Select a column for the Pie Chart', students_data.columns)
            chart = px.pie(students_data, names=chart_column)
        elif selected_chart_type == 'Scatter Plot':
            x_axis = st.selectbox('Select x-axis column for scatter plot', students_data.columns)
            y_axis = st.selectbox('Select y-axis column for scatter plot', students_data.columns)
            chart = px.scatter(students_data, x=x_axis, y=y_axis)
        st.plotly_chart(chart)
    else:
        st.warning("Select a valid chart type")

elif selected_data == 'session data':
    with st.spinner("Processing..."):
        t.sleep(3)
    st.title("Session Data")
    st.dataframe(session_data, width=1500, height=100)

    if selected_chart_type != 'Select Chart Type':
        if selected_chart_type == 'Line Chart':
            chart_data = st.selectbox('Select a column for the line chart', session_data.columns)
            chart = px.line(session_data, x=session_data.index, y=chart_data)
        elif selected_chart_type == 'Bar Chart':
            chart_data = st.selectbox('Select a column for the bar chart', session_data.columns)
            chart = px.bar(session_data, x=session_data.index, y=chart_data)
        elif selected_chart_type == 'Pie Chart':
            chart_column = st.selectbox('Select a column for the Pie Chart', session_data.columns)
            chart = px.pie(session_data, names=chart_column)
        elif selected_chart_type == 'Scatter Plot':
            x_axis = st.selectbox('Select x-axis column for scatter plot', session_data.columns)
            y_axis = st.selectbox('Select y-axis column for scatter plot', session_data.columns)
            chart = px.scatter(session_data, x=x_axis, y=y_axis)
        st.plotly_chart(chart)
    else:
        st.warning("Select a valid chart type")

elif selected_data == 'course data':
    with st.spinner("Processing..."):
        t.sleep(3)
    st.title("Course Data")
    st.dataframe(course_data, width=1500, height=100)

    if selected_chart_type != 'Select Chart Type':
        if selected_chart_type == 'Line Chart':
            chart_data = st.selectbox('Select a column for the line chart', course_data.columns)
            chart = px.line(course_data, x=course_data.index, y=chart_data)
        elif selected_chart_type == 'Bar Chart':
            chart_data = st.selectbox('Select a column for the bar chart', course_data.columns)
            chart = px.bar(course_data, x=course_data.index, y=chart_data)
        elif selected_chart_type == 'Pie Chart':
            chart_column = st.selectbox('Select a column for the Pie Chart', course_data.columns)
            chart = px.pie(course_data, names=chart_column)
        elif selected_chart_type == 'Scatter Plot':
            x_axis = st.selectbox('Select x-axis column for scatter plot', course_data.columns)
            y_axis = st.selectbox('Select y-axis column for scatter plot', course_data.columns)
            chart = px.scatter(course_data, x=x_axis, y=y_axis)
        st.plotly_chart(chart)
    else:
        st.warning("Select a valid chart type")

else:
    st.warning("---NOTHING TO SHOW---")