import streamlit as st
import firebase_admin
from firebase_admin import db
import random
st.set_page_config(layout="wide")
with open("cred.txt","r") as file2:
    userid = file2.readline()

file2.close()

with open("poster.txt","r") as file:
    postid = file.readline()

file.close()

ref = db.reference("/posts")
st.title("TruthMesh's VERI-Forum") 
st.markdown("<br>",unsafe_allow_html=True)
st.subheader(ref.child(postid).get()["content"])
st.markdown("<hr>",unsafe_allow_html=True)
ori_like = ref.child(postid).get()["likes"]
c1, c2 = st.columns(2)
with c1:
    st.write(str(ref.child(postid).get()["likes"])+" Likes")
with c2:
    if st.button("Drop A Like ❤️"):
        st.balloons()
        ref.child(postid).update({"likes": ori_like + 1})
        st.experimental_rerun()
st.write("Enter Your Opinion: ")
opinion = st.chat_input("Message...")

ref = db.reference('/posts')
ref1 = db.reference('/comments')
ref2 = db.reference('/users')
try:
    for i in ref.child(postid).child("comment").get():
        with st.chat_message("human"):
            st.write("@"+ref2.child(ref1.child(i).child("userid").get()).child("user_name").get())
            st.write(ref1.child(i).child("message").get())
            cola,colb = st.columns(2)
            with cola:
                st.write(str(ref1.child(i).child("likes").get()) + " Likes")
            with colb:
                like_button_key = postid + str(i)  # Use a unique key for each comment
                if st.button("Drop Like", key=like_button_key):
                    st.warning("Liked this point!")
                    new_likes = ref1.child(i).child("likes").get() + 1
                    ref1.child(i).update({"likes": new_likes})
                    st.experimental_rerun()
            #st.write(str(ref1.child(i).child("likes").get())+"Likes")
except Exception as e:
    st.success("Be first to comment!")

if opinion:
    #add the opinion to the comments of the post
    ref1 = db.reference('/posts')
    ref2 = db.reference('/comments')
    ref3 = db.reference('/users')
    def generate_user_id(length=7):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        user_id = ''.join(random.choice(characters) for _ in range(length))
        return user_id
    ref1 = db.reference('/comments')
    with open("cred.txt","r") as file:
        userid = file.readline()
    comment_id = generate_user_id()

    # lis = ["check12"]
    # st.write(ref.child("YTYre9Z").get(),lis)
    # ref.child("YTYre9Z").update({"comment" : lis})
    # st.write(ref.child("YTYre9Z").child("comment").get())

    ref1.update({ comment_id: {"message" : opinion,"postid" : postid,"userid" : userid,"likes" : 0}})
    ref1 = db.reference('/posts')
    if ref1.child(postid).child("comment").get() is None:
        lis = []
    else:
        lis = ref1.child(postid).child("comment").get()
    lis.append(comment_id)
    ref1.child(postid).update({"comment" : lis})

    st.write("Added your Comment")
    st.experimental_rerun()
