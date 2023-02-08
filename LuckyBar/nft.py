import pandas as pd
from pathlib import Path

# Fetch nft uri
def nft_uri(nft_index) -> str:
    """Method to fetch nft uri from LuckyBar nft_store.csv
    
    Args:
        nft_index(int): nft index number value
    
    Returns:
        str: A nft uri corresponding to the index number

    """
    try:
        nft_df = pd.read_csv(Path('Resources/nft_store.csv'))

        # Convert to key-value pair in a dictionary form
        nft_dict = dict(zip(nft_df.nft_id, nft_df.nft_uri))

        nft_index_uri = nft_dict.get(nft_index)
        return nft_index_uri
    except:
        return (f'An error occured while fetching the nft uri')

# Return raw dataframe of nft_store
def nft_df() -> pd.DataFrame:
    """Method to return nft uri list as a dataframe from LuckyBar nft_store.csv
    
    Args:
        None
    
    Returns:
        pd.DataFrame: DataF containing nft id/uri

    """
    try:
        nft_df = pd.read_csv(Path('Resources/nft_store.csv'))
        return nft_df
    except:
        return (f'An error occured while fetching the nft uri')