import os
import json
import streamlit as st
import nft
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

################################################################################
# Purchase NFT Artwork: Usecase of the customer who wishes to purchase NFT Token
################################################################################

# Load configuration settings related to Ganache URL and Solidity Contract ABI
load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

# Tab settings
# tabMain, tabAbout, tabHelp = st.tabs(["Main", "About", "Help"])

contract = load_contract()

# Read accounts from Ganache instance
accounts = w3.eth.accounts


################################################################################
# Purchase NFT Artwork
################################################################################
st.title('NFT LuckyBar')
st.markdown("---")

st.markdown("## Purchase LuckyBar NFT")

# Use a streamlit component to get the address of the artwork buyer from the owner
buyer_address = st.selectbox("Your Wallet Address", options=accounts)

# Raffle names
options = ('Ice-cream', 'Chocolatebar', 'Golden-toilet', 'Something', 'Nothing')
raffle_index = st.selectbox("Choose Your Raffle", range(len(options)), format_func=lambda x: options[x])

nft_uri_id = raffle_index + 1

st.write("Raffle:", options[raffle_index])
st.write("Raffle Index:", nft_uri_id)

# Get the NFT URI from nft_store.csv
artwork_uri = nft.nft_uri(nft_uri_id)
st.write(artwork_uri)

# Use a streamlit component to set the address of the luckybar
luckybar_address = st.selectbox("LuckyBar Owner Address", options=accounts)

# st.write(buyer_address)

token_amount = st.text_input("Raffle Token Price (Wei)", "100")

if st.button("Buy NFT Artwork"):
    # Approve the buyer to transfer token from the NFT owner
    contract.functions.approve(
        buyer_address,
        0   # TokenID: Make it dynamic to get from nft-stores
    ).call()
    st.write("Buyer approved")
    
    # Use the transferFrom function to transfer the ownership of the nft token to the buyer
    contract.functions.transferFrom(
        luckybar_address,
        buyer_address,
        0   # TokenID: Make it dynamic to get from nft-stores
    ).call()

    st.write("Transaction receipt mined")
    st.balloons()
st.markdown("---")

################################################################################
# Display a Token
################################################################################

st.markdown("### Display Your Purchased Art Token")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()
st.write(f"This address owns {tokens} tokens")

token_id = st.selectbox("Artwork Tokens", list(range(tokens)))

if st.button("Display NFT URI"):
    # Use the contract's `ownerOf` function to get the art token owner
    owner = contract.functions.ownerOf(token_id).call()

    st.write(f"The token is registered to {owner}")

    # Use the contract's `tokenURI` function to get the art token's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)

st.markdown("---")

##########