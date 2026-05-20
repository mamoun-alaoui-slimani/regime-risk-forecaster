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
        returns: DataFrame with returns for one or multiple indices
        window: int number of days over which returns standard deviation is computed
                (20 by default)
    Returns:
        DataFrame containing rolling volatility values
    """
    return returns.rolling(window).std()

def compute_momentum(returns, window=20):
    """Computes asset momentum for a specified time window
    Args:
        returns: DataFrame with returns for one or multiple indices
        window: int number of days over which momentum is computed (20 by default)
    Returns:
        DataFrame containing momentum values"""
    return returns.rolling(window).sum()

def compute_drawdown(asset):
    """Computes asset drawdown
    Args:
        asset: DataFrame with MultiIndex columns (Close, Open, etc.)
    Returns:
        DataFrame with drawdown values
    """
    rolling_max = asset['Close'].cummax()
    return (asset['Close'] - rolling_max) / rolling_max
    
def compute_all_features(asset, window=20):
    """Computes all features (returns, volatility, momentum, drawdown) for all assets
    Args:
        asset: DataFrame with MultiIndex columns (Close, Open, etc.)
        window: window: int number of days over which volatility and momentum are
                computed (20 by default)
    Returns: DataFrame containing all features
    """
    returns = compute_returns(asset)
    volatility = compute_rolling_volatility(returns, window)
    momentum = compute_momentum(returns, window)
    drawdown = compute_drawdown(asset)
    
    return pd.concat([
        returns.add_suffix("_returns"),
        volatility.add_suffix("_volatility"),
        momentum.add_suffix("_momentum"),
        drawdown.add_suffix("_drawdown"),
    ], axis=1)

print(compute_all_features(equities))