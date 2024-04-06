import streamlit as st
from firebase_admin import db
from firebase_admin import credentials, storage
import firebase_admin
import random
from streamlit_extras.switch_page_button import switch_page
import time

st.set_page_config(layout="wide")

with st.spinner("TruthMesh - Loading WebApp..."):
    time.sleep(2)
st.sidebar.header("TruthMesh")
st.sidebar.subheader("ZenMinds Initiative")
st.sidebar.markdown("<hr>",unsafe_allow_html=True)
st.sidebar.subheader("Developed By:")
st.sidebar.write("> Roshan Muhammed")
st.sidebar.write("> N P Yuvashree")
st.sidebar.write("> Abhinanth Anupkumar")
st.sidebar.write("> Abijith S V")
st.sidebar.write("> Yashwenth S")

def check_user(username,passwd="hello"):
    try:
        flag = 0
        data = list(ref.get().keys())
        for i in data:
            if(ref.get()[i]['user_name']==username):
                flag = 1
                if(ref.get()[i]['passwd']==passwd):
                    flag = 2
        return flag
    except:
        st.error("Account not found!! Please Sign-up", icon="🚨")

def get_user_id(username):
    data = list(ref.get().keys())
    for i in data:
        if(ref.get()[i]['user_name']==username):
            return i
def generate_user_id(length=7):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user_id = ''.join(random.choice(characters) for _ in range(length))
    return user_id
def sign_in():
    with open("cred.txt","w") as file:
        file.write("")
    col1,col2 = st.columns(2)
    with col1:
        username_placeholder = st.empty()
        password_placeholder = st.empty()
        button_placeholder = st.empty()

        # Create input fields for username, password, and sign-in button
        username = username_placeholder.text_input("Username")
        passwd = password_placeholder.text_input("Password", type="password")
        button = button_placeholder.button("Sign In")

        # Check if the sign-in button is clicked
        if button:
            x = check_user(username,passwd)
            if x == 2:
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                    # change page
                    with open("cred.txt","w") as file:
                        file.write(get_user_id(username))
                    switch_page("Trending_Verified_News")

                    st.write("Successfull")
            else:
                if x== 1:
                    with st.spinner('Wait for it...'):
                        time.sleep(2)
                    st.error('Wrong Password', icon="🚨")
                elif x == 0:
                    with st.spinner('Wait for it...'):
                        time.sleep(2)
                    st.error("Account not found!! Please Sign-up", icon="🚨")
    with col2:
        nameCreate = st.text_input("Full Name")
        usernameCreate = st.text_input("User name")
        passwdCreate = st.text_input("New Password", type="password")
        emailCreate = st.text_input("Email")
        x = check_user(usernameCreate)
        def sign_up():
            if x==1 or x==2:
                st.error('User Name already exist', icon="🚨")
            elif (nameCreate=="" or usernameCreate=="" or passwdCreate=="" or emailCreate==""):
                st.success('Retry Signing Up. Network Slow')
            else: 
                userid = nameCreate[0:3]+generate_user_id();
                user = {userid:{"name":nameCreate,"user_name":usernameCreate,"passwd":passwdCreate,"email":emailCreate,"veritas":0,"contributions":{"count":0,"postid":[1,]}}}
                ref.update(user)
                with open("cred.txt","w") as file:
                    file.write(userid)
                st.success('Created Account successfully', icon="✅")
        st.button("sign up",on_click=sign_up)

try:
    cred_obj = firebase_admin.credentials.Certificate('./truthmesh-firebase-adminsdk-qkbxc-42d724ba02.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://truthmesh-default-rtdb.firebaseio.com/"
        })
except:
    pass
ref = db.reference("/users")

st.header("TruthMesh - Verify news with confidence, promoting positivity and accuracy.")
st.subheader("A ZenMinds Initiative")
st.markdown("<hr>",unsafe_allow_html=True)
sign_in()