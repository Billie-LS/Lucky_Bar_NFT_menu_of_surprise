import os
import json
import streamlit as st
import nft
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv


################################################################################
# Register NFT Artwork: Usecase of the NFT seller
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

contract = load_contract()

# Read accounts from Ganache instance
accounts = w3.eth.accounts

@st.cache(allow_output_mutation=True)
def nft_options():
    df = nft.nft_df()
    values = df['nft_uri'].tolist()
    options = df['nft_id'].tolist()
    return options, values

################################################################################
# Begin of Register Block
################################################################################
st.title('NFT LuckyBar')
st.markdown("---")

st.markdown("## Register NFT Artworks")

# Use a streamlit component to get the address of the artwork owner from the user
owner_address = st.selectbox("Select NFT Owner Address", options=accounts)

# Fetch nft uri and id list
options, values = nft_options()
dic = dict(zip(options, values))

nft_uri_id = st.selectbox('Select NFT URI:', options, format_func=lambda x: dic[x])
# NFT artwork preview
st.image(values[nft_uri_id - 1])

# Get the NFT URI from nft_store.csv
nftwork_uri = nft.nft_uri(nft_uri_id)

st.markdown("NFT Artwork URI")
st.write(nftwork_uri)

if st.button("Register Artwork"):
    # Use the contract to send a transaction to the registerArtwork function
    tx_hash = contract.functions.registerArtwork(
        owner_address,
        nftwork_uri
    ).transact({'from': owner_address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.balloons()
st.markdown("---")

if st.button("Check NFT Balance"):
    count = contract.functions.balanceOf(owner_address).call()
    st.write("Current NFT Counts:")
    st.write(count)

st.markdown("---")

################################################################################
# Display a Token
################################################################################
st.markdown("## Display an Art Token")

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
# End of Register Block