#AI Bartender
#This program is an experimental feature which the restaurants can use to interact with their clients. The purpouse is that customers can recieve a random
#NFT, retrieved from the nft_stores.cvs file which contains the NFTS which the restaurant created. AFter, the user can caht with the bartender and place an order.
#We made our bartender to be very sassy, but the idea is that resaturants can personalize their bartenders by vhanging the prompt.


#Import required dependencies
import os 
import requests 
import json 
import streamlit as st
import time
import random
import pandas as pd
from dotenv import load_dotenv
from PIL import Image

#Add a title to the Streamlit page
st.title("😉 Bartender AI🍸")
st.caption("Powered by GPT-3 & Lucky Bar")

#Retrieve the api key from env file
load_dotenv()
api_key = os.getenv('api_key')

#Set the variables for the API. We will use the DaVinci-002 model to generate text.
model = "text-davinci-002"
completions_url = f"https://api.openai.com/v1/engines/{model}/completions"
headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

#Create a function that sends a prompt to the API, and is returned the answer.
def generate_text(prompt):
    prompt1 = f"{prompt}"
    response = requests.post(completions_url, headers=headers, json={"prompt": prompt1, "max_tokens": 1024, "temperature": 0.4})
    message = response.json()["choices"][0]["text"]
    return message

#Create the button to get an NFT
st.text("Get a random nft for free.")
#Will randomly select an already AI-generated NFT image
if st.button('Generate'):
    df = pd.read_csv('./nft_stores.csv')
    url = df.sample().to_string(header=False, index=False)
    st.image(url, caption='Randomly selected NFT')
    st.text("Your NFT has been selected and processed. Token sent to wallet.")


#Create the first part of the prompt so that no matter what text the user inputs, the AI will pretend to be a bartender at LuckyBar.
instrucction = "Pretend to be a sassy bartender at Lucky Bar and recieve and confirm the order coming right up. Based on the order, make a very funny joke or pop culture reference after. The order is: "

#Generate a complete prompt by appending the user input to the instrucction for the API.
intro = st.text_input("Place an order and chat with the bartender")
complete_prompt = instrucction+intro

#Make a variable that stores the AI response using the generate_text() function.
generated_text = generate_text(complete_prompt)

#Create a button (to not waste API calls and make the Streamlit run smoothly) that will display the API response to the user.
if st.button('Send'):
    with st.spinner('Placing your order...'):
        time.sleep(5)
    st.write(generated_text)
