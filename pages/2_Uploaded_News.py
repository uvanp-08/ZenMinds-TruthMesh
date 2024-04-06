import streamlit as st
import firebase_admin
from firebase_admin import db
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(layout="wide")
# cred_obj = firebase_admin.credentials.Certificate('pages\credss.json')
   # default_app = firebase_admin.initialize_app(cred_obj, {
   #     'databaseURL': "https://truthmesh-default-rtdb.firebaseio.com/"
    # })
ref = db.reference("/posts")
ref2 = db.reference("/users")
all_news = list(ref.get().keys())
    # st.write(ref.child(all_news[0]).get()["content"])
st.title("UPLOADED NEWS")
st.markdown("<hr>",unsafe_allow_html=True)
for i in range(len(all_news)):
    with st.chat_message("human"):
        st.header(ref.child(all_news[i]).get()["title"])
        st.caption(ref.child(all_news[i]).get()["time"])
        st.caption("Uploaded By - " + ref2.child(ref.child(all_news[i]).get()["userid"]).get()["name"])
        st.markdown("<br>",unsafe_allow_html=True)
        st.write(ref.child(all_news[i]).get()["content"])
        st.markdown(f'<p style="font-size: 30px; color: green; background-color: white">{ref.child(all_news[i]).get()["label"]}</p>',unsafe_allow_html=True)
        if st.button("Dive to Discussion !",key=str(i)):
            with open("poster.txt","w") as file:
                file.write(all_news[i])
            switch_page("Veri_Forum")
        st.markdown("<hr>",unsafe_allow_html=True)

