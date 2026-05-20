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

def compute_rolling_volatility(returns, window=20):
    """Computes rolling volatility for a specified time window
    Args: 
        returns: returns used to compute volatility
        window: number of days over which returns standard deviation is computed
                (20 by default)
    Returns:
        DataFrame containing rolling volatility values
    """
    return returns.rolling(window).std()

def compute_momentum(returns, window=20):
    """Computes asset momentum
    Args:
        returns: returns used to compute momentum
        window: number of days over which momentum is computed (20 by default)
    Returns:
        DataFrame containing momentum values"""
    return returns.rolling(window).sum()
    
print(compute_momentum(compute_returns(equities)))