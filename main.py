import streamlit as st
import streamlit_authenticator as stauth
from signup import sign_up, fetch_users
from streamlit_option_menu import option_menu
import dashboard,courses,students,teacher,Sessions
import datetime

def generate_key():
    return f"option_menu_{int(datetime.datetime.now().timestamp())}"

# Callback function for on_change
def on_change(app):
    if app == "Dashboard":
        k="menu_1"               
    if app== "Students":
        k="menu_2"
    if app == "Teachers":
        k="menu_3"
    if app == "Courses":
        k="menu_4"
    if app == "Sessions":
        k="menu_5"


#st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')
def run():
    #with st.sidebar:
    k="menu_1"
                        
    app = option_menu(
                    
                    menu_title='Navigation ',
                    options=['Dashboard','Students','Teachers','Courses','Sessions'],
                    icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    key=k,
                    #on_change=on_change(app),
                    orientation='horizontal',
                    styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
                    
                
    if app == "Dashboard":
        k="menu_1"
        dashboard.app()                   
    if app== "Students":
        k="menu_2"
        students.app()
    if app == "Teachers":
        k="menu_3"
        teacher.app()
    if app == "Courses":
        k="menu_4"
        courses.app()
    if app == "Sessions":
        k="menu_5"
        Sessions.app()




try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                st.sidebar.subheader(f'Welcome {username}❤️')
                Authenticator.logout('Log Out', 'sidebar')
                run()
                # let User see app
                
                 
                

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


except:
    run()
    st.success('Refresh Page')