# import requests
# import streamlit as st
# import firebase_admin
# from firebase_admin import db
# import random
# from datetime import datetime



# # get credentials from file
# userid = "None"
# with open("cred.txt","r") as file:
#     userid = file.readline()
# # end of file extraction

# API_URL = "https://api-inference.huggingface.co/models/hamzab/roberta-fake-news-classification"
# headers = {"Authorization": "Bearer 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"}


# def generate_user_id(length=7):
#     characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     user_id = ''.join(random.choice(characters) for _ in range(length))
#     return user_id

# def get_todays_date():
#     current_datetime = datetime.now()
#     todays_date = current_datetime.date()
#     return todays_date

# def verify(text):
#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response.json()

#     output = query({
#         "inputs": text,
#     })
#     return output


# st.title("News Verifier")
# text0 = st.text_input("Enter the news Title")
# text = st.text_input("Enter the news Article")
# with st.expander("Expand to read the news"):
#     st.subheader(text0)
#     st.write(text)

# share_button_pressed = False  # Variable to track whether the "Share" button has been pressed

# if st.button("Verify", type="primary"):
#     try:
#         output = verify(text)
#         label1 = output[0][0]['label']
#         label2 = output[0][1]['label']
#         score1 = output[0][0]['score']
#         score2 = output[0][1]['score']
#         progress1 = st.progress(score1, text=label1)
#         progress2 = st.progress(score2, text=label2)
#     except:
#         st.write("An Error has occurred. Please try with a shorter input")

# if st.button("Share") and not share_button_pressed:

#     # cred_obj = firebase_admin.credentials.Certificate('pages\credss.json')
#     # default_app = firebase_admin.initialize_app(cred_obj, {
#     #     'databaseURL': "https://truthmesh-default-rtdb.firebaseio.com/"
#     # })

#     ref = db.reference("/posts")
#     # Update the database with the converted datetime strings
#     output = verify(text)
#     label1 = output[0][0]['label']
#     label2 = output[0][1]['label']
#     score1 = output[0][0]['score']
#     score2 = output[0][1]['score']

#     postid = generate_user_id()

#     ref.update(
#         {
#             postid : 
#             {
#                 "comment": [],  # list of comment ids
#                 "likes": 0,
#                 "title": text0,
#                 "content": text,
#                 "userid" : userid,
#                 "time" : str(get_todays_date()),
#                 "score" : score1,
#                 "label" : label1
#             }
#         })
#     share_button_pressed = True  # Set the variable to True after the button is pressed

# st.write(f"Share button pressed: {share_button_pressed}")

# import requests
# import streamlit as st
# import time
# API_URL1 = "https://api-inference.huggingface.co/models/hamzab/roberta-fake-news-classification" #model-1 (roberta_fake_news_classifier)
# #TRUE and FAKE
# API_URL2 = "https://api-inference.huggingface.co/models/jy46604790/Fake-News-Bert-Detect" #model2 (fake-news-Bert-Detect)
# #Label_0 - FAKE, Label_1 - True
# API_URL3 = "https://api-inference.huggingface.co/models/XSY/albert-base-v2-fakenews-discriminator" #model3 (alberta-base-v2-fakenews-discriminator)
# #label_0 : Fake news label_1 : Real news
# API_URL4 = "https://api-inference.huggingface.co/models/littlepinhorse/4_datasets_fake_news" #model4 (4_datasets_fake_news)
# #label_0 : Fake news label_1 : Real news
# API_URL5 = "https://api-inference.huggingface.co/models/ghanashyamvtatti/roberta-fake-news" #roberta-fake-news
#
# headers = {"Authorization": "Bearer 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"}
#
# def verify(text,API):
#     def query(payload):
#         response = requests.post(API, headers=headers, json=payload)
#         return response.json()
#
#     output = query({
#         "inputs": text,
#     })
#     return output
#
# def get_true_val_v1(op):
#     dict = op[0]
#     for i in dict:
#         if i['label'] == "TRUE":
#             return i['score']
#
# def get_true_val_v2(op):
#     dict = op[0]
#     for i in dict:
#         if i['label'] == "LABEL_1":
#             return i['score']
#
# # #
# # #

# #
# # st.title("News Verifier")
# #
# # text = st.text_input("Enter the news Article")
# # with st.expander("Expand to read the news"):
# #     st.write(text)
# #
# # model_accuracies = [0.8918918918918919,0.5405405405405406,0.4864864864864865,0.6486486486486487,0.40540540540540543]
# #
# #
# #
# # if st.button("Verify",type="primary"):
# #     st.write("model 1....")
# #     op1 =  get_true_val_v1(verify(text,API_URL1))
# #     x = 1
# #     st.write("model 2...")
# #     op2 = get_true_val_v2(verify(text, API_URL2))
# #     x = 2
# #     st.write("model 3...")
# #     op3 = get_true_val_v2(verify(text, API_URL3))
# #     x = 3
# #     st.write("model 4...")
# #     op4 = get_true_val_v2(verify(text, API_URL4))
# #     x = 4
# #     st.write("model 5...")
# #     op5 = get_true_val_v2(verify(text,API_URL5))
# #     x = 5
# #     model_outputs = [op1, op2, op3, op4, op5]
# #     total_accuracy = sum(model_accuracies)
# #     weights = [accuracy / total_accuracy for accuracy in model_accuracies]
# #     weighted_average = sum(weight * output for weight, output in zip(weights, model_outputs))
# #     st.progress(weighted_average,"TRUE")
# #     st.progress(1-weighted_average,"FALSE")
# # if st.button("Share"):
# #     pass
#
#

import requests
import streamlit as st
import firebase_admin
from firebase_admin import db
import random
from datetime import datetime
import time
from googletrans import Translator, LANGUAGES
st.set_page_config(layout="wide")
if 'session_state' not in st.session_state:
    st.session_state.temp = 0.0

# get credentials from file
userid = "None"
with open("cred.txt","r") as file:
    userid = file.readline()
# end of file extraction
API_URL1 = "https://api-inference.huggingface.co/models/hamzab/roberta-fake-news-classification" #model-1 (roberta_fake_news_classifier)
#TRUE and FAKE
API_URL2 = "https://api-inference.huggingface.co/models/jy46604790/Fake-News-Bert-Detect" #model2 (fake-news-Bert-Detect)
#Label_0 - FAKE, Label_1 - True
API_URL3 = "https://api-inference.huggingface.co/models/XSY/albert-base-v2-fakenews-discriminator" #model3 (alberta-base-v2-fakenews-discriminator)
#label_0 : Fake news label_1 : Real news
API_URL4 = "https://api-inference.huggingface.co/models/littlepinhorse/4_datasets_fake_news" #model4 (4_datasets_fake_news)
#label_0 : Fake news label_1 : Real news
API_URL5 = "https://api-inference.huggingface.co/models/ghanashyamvtatti/roberta-fake-news" #roberta-fake-news


headers = {"Authorization": "Bearer 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"}


def generate_user_id(length=7):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user_id = ''.join(random.choice(characters) for _ in range(length))
    return user_id

def get_todays_date():
    current_datetime = datetime.now()
    todays_date = current_datetime.date()
    return todays_date

def verify(text,API):
    def query(payload):
        response = requests.post(API, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": text,
    })
    return output

with st.spinner("Awakening ML Models..."):
    try:
        verify("my name is roshan",API_URL1)
    except:
        pass
    try:
        verify("my name is roshan",API_URL2)
    except:
        pass
    try:
        verify("my name is roshan",API_URL3)
    except:
        pass
    try:
        verify("my name is roshan",API_URL4)
    except:
        pass
    try:
        verify("my name is roshan",API_URL5)
    except:
        pass



def get_true_val_v1(op):
    dict = op[0]
    for i in dict:
        if i['label'] == "TRUE":
            return i['score']

def get_true_val_v2(op):
    # st.write(op)
    dict = op[0]
    for i in dict:
        if i['label'] == "LABEL_1":
            return i['score']

model_accuracies = [0.8918918918918919,0.5005405405405406,0.4064864864864865,0.5086486486486487,0.30540540540540543]
def Translate(text1):
    translator = Translator()
    translated = translator.translate(text=text1, dest="english")
    return translated.text
st.title("NEWS VERIFIER - Using Cluster of ML Models")
text0 = st.text_input("Enter the news Title")
text = st.text_input("Enter the news Article")
with st.expander("Expand to read the news"):
    try:
        gg = Translate(text)
    except:
        pass
    st.subheader(text0)
    st.write(text)
    st.markdown("<br>",unsafe_allow_html=True)
    if st.button("Translate To English!"):
        st.write("Translated News")
        st.markdown("<hr>",unsafe_allow_html=True)
        st.write(gg)

share_button_pressed = False  # Variable to track whether the "Share" button has been pressed

def progress_bar(progress_text):
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

temp =0.0


if st.button("Verify"):
    text = text[0:1500]
    progress_bar("model 1...")
    text = Translate(text)
    op1 =  get_true_val_v1(verify(text,API_URL1))
    st.success('model 1...', icon="✅")
    x = 1
    progress_bar("model 2...")
    op2 = get_true_val_v2(verify(text, API_URL2))
    st.success('model 2...', icon="✅")
    x = 2
    progress_bar("model 3...")
    op3 = get_true_val_v2(verify(text, API_URL3))
    st.success('model 3...', icon="✅")
    x = 3
    progress_bar("model 4...")
    op4 = get_true_val_v2(verify(text, API_URL4))
    st.success('model 4...', icon="✅")
    x = 4
    progress_bar("model 5...")
    op5 = get_true_val_v2(verify(text,API_URL5))
    st.success('model 5...', icon="✅")
    x = 5
    model_outputs = [op1, op2, op3, op4, op5]
    total_accuracy = sum(model_accuracies)
    weights = [accuracy / total_accuracy for accuracy in model_accuracies]
    weighted_average = sum(weight * output for weight, output in zip(weights, model_outputs))
    st.progress(weighted_average,"TRUE")
    st.progress(1-weighted_average,"FALSE")
    # cred_obj = firebase_admin.credentials.Certificate('pages\credss.json')
    # default_app = firebase_admin.initialize_app(cred_obj, {
    #     'databaseURL': "https://truthmesh-default-rtdb.firebaseio.com/"
    # })
    ref = db.reference("/posts")
    # Update the database with the converted datetime strings
    # output = verify(text)
    # label1 = output[0][0]['label']
    # label2 = output[0][1]['label']
    # score1 = output[0][0]['score']
    # score2 = output[0][1]['score']
    x = weighted_average
    y = 1-weighted_average
    if x>y:
        label1 = "TRUE"
        score1 = temp
    else:
        label1 = "FALSE"
        score1 = 1-temp
    postid = generate_user_id()

    ref.update(
        {
            postid :
            {
                "comment": [],  # list of comment ids
                "likes": 0,
                "title": text0,
                "content": text,
                "userid" : userid,
                "time" : str(get_todays_date()),
                "score" : score1,
                "label" : label1
            }
        })
    share_button_pressed = True  # Set the variable to True after the button is pressed

#st.write(f"Share button pressed: {share_button_pressed}")
