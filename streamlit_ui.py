import streamlit as st
import requests

st.title('MiningNiti - Mines and Coal Industry ChatBot')

url = 'http://localhost:8000/chat'

input_query = st.text_input('Enter the input query: ')

payload = {
    "input_query": input_query
}

if st.button('Get Answers'):
    resposne = requests.post(url=url, json=payload)

    if resposne.status_code == 200:
        st.markdown(
            f"""<h6 style='color: #3CB371;'>
                {resposne.text}
            </h6>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<h6 style='color: #3CB371;'>
                An error occured, Please try again later
            </h6>""",
            unsafe_allow_html=True
        )