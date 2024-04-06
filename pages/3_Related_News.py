import streamlit as st
import requests
import json
st.set_page_config(layout="wide")
st.title("RELATED NEWS")
title = st.text_input("Title: ")
content = st.text_area("Content: ")
button = st.button("SUBMIT")
st.markdown("<hr>", unsafe_allow_html=True)

if button:

    API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
    headers = {"Authorization": "Bearer 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"}


    def query(payload):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        except:
            st.success("Check Network Again / Refresh")
            query(payload)

    data=""

    if content!="":
        output = query({
            "inputs":  content,
        })
        data = output[0]["summary_text"]
        #st.write(data)

        API_URL2 = "https://api-inference.huggingface.co/models/yanekyuk/camembert-keyword-extractor"
        headers2 = {"Authorization": "Bearer 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"}


        def query(payload):
            try:
                response = requests.post(API_URL2, headers=headers2, json=payload)
                return response.json()
            except:
                st.success("Check Network Again / Refresh")
                query(payload)


        output1 = query({
            "inputs": data,
        })

        #st.write(output1)
        lis=[]
        for keyword in output1:
            key = keyword["word"]
            if key not in lis:
                lis.append(key)
                st.write(key)
                st.caption('https://newsapi.org/v2/everything?q='+key+"&apiKey=d4605492f0d04848a4c486dcc56a4a04")
                response1 = requests.get('https://newsapi.org/v2/everything?q='+key+"&apiKey=d4605492f0d04848a4c486dcc56a4a04")
                #try:

                for i in range(0, 3):
                    data1 = response1.json()["articles"][i]
                    #st.write(data1)

                    st.markdown("<hr>", unsafe_allow_html=True)
                    try:
                        st.header(data1["title"])
                    except:
                        pass

                    try:
                        st.write(data1["description"])
                    except:
                        pass

                    try:
                        st.image(image=data1["urlToImage"])
                    except:
                        pass

                    try:
                        st.write("For more information "+ data1["url"])
                    except:
                        pass
            else:
                continue