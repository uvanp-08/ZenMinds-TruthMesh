import streamlit as st
import requests
import re
import time
import webbrowser
st.set_page_config(
        page_title="TruthMesh - An ZenMind Initiative",
        page_icon="🌐",
        layout="wide"
    )
def main():
    st.title("TruthMesh© - A ZenMinds Initiative")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Trending Verified News ")
    # fetch data from API
    # news api.org = API Key = d4605492f0d04848a4c486dcc56a4a04
    with st.spinner("Loading You The Hot News..."):
        time.sleep(2)
    response_API = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d4605492f0d04848a4c486dcc56a4a04")
    titles = []
    imgurl = []
    contenturls = []
    sources = []
    timestamps = []
    contents = []
    buttons = []
    for i in range(10):
        titles.append(response_API.json()["articles"][i]["title"])
        imgurl.append(response_API.json()["articles"][i]["urlToImage"])
        sources.append(response_API.json()["articles"][i]["author"])
        contenturls.append(response_API.json()["articles"][i]["url"])
        timestamps.append(response_API.json()["articles"][i]["publishedAt"])
        contents.append(response_API.json()["articles"][i]["content"])

    def getsource(text):
        pattern = r' - (.+?)$'
        match = re.search(pattern, text)
        return match.group(1) if match else None

    button_clicked = {i: False for i in range(10)}
    
    for i in range(10):
        keyer = str(i)
        with st.chat_message("user"):
            try:
                st.header(titles[i])
            except:
                pass
            try:
                st.caption(getsource(titles[i]))
            except:
                pass
            try:
                st.image(image=imgurl[i])
            except:
                pass
            try:
                st.caption(timestamps[i])
            except:
                pass
            try:
                st.write(contents[i].split("[")[0])
            except:
                pass
            try:
                st.write("To read more: "+contenturls[i])
            except:
                pass
            try:
                st.markdown("<hr>",unsafe_allow_html=True)
            except:
                pass

main()
