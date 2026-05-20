import numpy as np
import pandas as pd

equities = pd.read_parquet("data/raw/equities.parquet")

def compute_returns(asset):
    """Compute daily log returns for all assets
    Args:
        asset: DataFrame with MultiIndex columns (Close, Open, etc.)
    Returns:
        DataFrame of log returns, one column per asset
    """
    
    return np.log(asset['Close'] / asset['Close'].shift(1))

