# crowd sourced news verification

import streamlit as st
import firebase_admin
from firebase_admin import db
import random as r
import time
st.set_page_config(layout="wide")
st.title("ASK CITIZENS - Verify using Crowd Sourcing")
st.markdown("<hr>",unsafe_allow_html=True)

st.subheader("Upload News")
ti = st.text_input("Enter title for the news")
ta = st.text_area("Enter the news")

with open("cred.txt","r") as file:
    userid = file.readline()

postid = ""
if st.button("Upload!"):
    st.success("Uploaded")
    # upload the news
    ref = db.reference("/crowd_posts")
    i = str(r.randint(10000,99999))
    i = ta[0] + i
    postid = i
    
    dic = {
        i : {
            "userid" : userid,
            "True" : 0,
            "False" : 0,
            "content" : ta,
            "title" : ti
        }
    }
    ref.update(dic)
    st.experimental_rerun()

st.markdown("<br>",unsafe_allow_html=True)
st.subheader("News Waiting for Your Decision:")
st.markdown("<hr>",unsafe_allow_html=True)
ref = db.reference("/crowd_posts")
try:
    for i in list(ref.get().keys()):
        with st.chat_message("human"):
            ref2 = db.reference("/users")
            userid_uploaded = ref.child(i).child("userid").get()
            username = ref2.child(userid_uploaded).child("user_name").get()
            st.write("@"+username)
            st.subheader(ref.child(i).child("title").get())

            def voteTrue():
                existing_true = ref.child(i).child("True").get()
                st.success("You Voted It TRUE Now.")
                ref.child(i).update({"True":existing_true+1})

            def voteFalse():
                existing_true = ref.child(i).child("False").get()
                ref.child(i).update({"False":existing_true+1})

            with st.expander("Expand to see full news"):
                st.write(ref.child(i).child("content").get())
            col1,col2,col3,col4 = st.columns(4,gap="small")
            with col1:
                like_button_key = postid + str(i) + "T"
                if st.button("TRUE",key=like_button_key):
                    ref.child(i).update({"True":ref.child(i).child("True").get()+1})
            with col2:
                st.write(str(ref.child(i).child("True").get()) + " Voted True")
            with col3:
                like_button_key = postid + str(i) + "F"
                if st.button("FALSE",key=like_button_key):
                    ref.child(i).update({"False":ref.child(i).child("False").get()+1})
            with col4:
                st.write(str(ref.child(i).child("False").get()) + " Voted False")

        st.markdown("<br>",unsafe_allow_html=True)
except Exception as e:
    st.success("No News Here")
    with st.expander("Full Report Here"):
        st.write(e)