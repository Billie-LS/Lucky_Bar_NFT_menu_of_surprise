import os 
from dotenv import load_dotenv
import requests 
import json 
import streamlit as st
import time
import random
import pandas as pd
from PIL import Image


st.title("😉 Bartender AI🍸")
st.caption("Powered by GPT-3 & Lucky Bar")

load_dotenv()
api_key = os.getenv('api_key')

model = "text-davinci-002"
completions_url = f"https://api.openai.com/v1/engines/{model}/completions"
headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }


def generate_text(prompt):
    prompt1 = f"{prompt}"
    response = requests.post(completions_url, headers=headers, json={"prompt": prompt1, "max_tokens": 1024, "temperature": 0.4})
    message = response.json()["choices"][0]["text"]
    return message

instrucction = "Pretend to be a bartender at Lucky Bar and recieve and confirm the order coming right up. Based on the order, make a punny joke or a pop culture reference after. The order is: "






st.text("Get a random nft")
if st.button('Generate'):
    df = pd.read_csv('./nft_stores.csv')
    url = df.sample().to_string(header=False, index=False)
    st.image(url, caption='Randomly selected NFT')


    
intro = st.text_input("Place an order and chat with the bartender")
complete_prompt = instrucction+intro
generated_text = generate_text(complete_prompt)

if st.button('Send'):
    with st.spinner('Placing your order...'):
        time.sleep(5)
    st.write(generated_text)
