import os 
from dotenv import load_dotenv
import requests 
import json 
import streamlit as st
import time


st.title("😉 Bartender AI🍸")
#st.subtitle("Lucky Bar")
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
    response = requests.post(completions_url, headers=headers, json={"prompt": prompt1, "max_tokens": 1024, "temperature": 0.5})
    message = response.json()["choices"][0]["text"]
    return message

instrucction = "Pretend to be a bartender and recieve and confirm the order coming right up. Based on the order, make a punny joke or a pop culture reference after. The order is: "

intro = st.text_input("Place an order")
complete_prompt = instrucction+intro
generated_text = generate_text(complete_prompt)

if st.button('Send'):
    with st.spinner('Placing your order...'):
        time.sleep(5)
    st.write(generated_text)


toilet = "Royal flush. Free restroom use."
pina_colada = "*singing 'If you like pina coladasss'! Its half-off for tropical cocktails"
shots = "Hit me with your best shot! Get complimentary rounds"
old_fashioned = "Call me old fashioned, but you get an old fashioned for half off."
breadbasket = "you're a breadwinner! Earn coupons after bread refill."
feast = "It's a feast! Parties of 6+ get a 25 percent discount!"
steak = "Well done! Get your main course for free!"

nft_recieved = st.selectbox(
    "What NFT did you win?",
    ('1. Toilet', '2. Piña colada', '3. Shots', '4. Old fashioned', '5. Bread basket', '6. Feast', '7. Steak')
)

if nft_recieved == "1. Toilet":
    nft = toilet
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "2. Piña colada":
    nft = pina_colada
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "3. Shots":
    nft = shots
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "4. Old fashioned":
    nft = old_fashioned
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "5. Bread basket":
    nft = old_fashioned
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "6. Feast":
    nft = feast
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
if nft_recieved == "7. Steak":
    nft = steak
    nft_instrucction = f"Pretend to be a bartender at the Lucky Bar. Recieve a coupon, and give back a reward based on {nft} and elaborate on that reward. Be punny!"
    generated_text = generate_text(nft_instrucction+nft)
    st.write(generated_text)
