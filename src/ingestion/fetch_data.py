import yfinance as yf
import yaml

def load_config(config_path):
    """Loads the desired start date, equities, and macros from a yaml file
    Args:
        config_path: "path to the configuration file
    Returns:
        Dictionary containing equities, macros, and start date"""
    with open(config_path, "r") as f:
        assets = yaml.safe_load(f)
    return assets

def fetch_equities(config):
    """Fetches equities daily OHLCV (Open, High, Low, Close, Volume) values 
    from yfinance from a start date to today
    Args:
        config: dictionary containing the desired equities and start date
    Returns:
        DataFrame containing OHLCV values for all equities"""
    return yf.download(config["equities"], config["start_date"], auto_adjust=True)

def fetch_macro(config):
    """Fetches macro daily OHLCV (Open, High, Low, Close, Volume) values 
    from yfinance from a start date to today
    Args:
        config: dictionary containing the desired macro and start date
    Returns:
        DataFrame containing OHLCV values for all macro (Colume is 0 for all macro)"""
    return yf.download(config["macro"], config["start_date"], auto_adjust=True)

def run_ingestion():
    """Fetches configuration (equities, macro, start date) from configuration file
    Fetches the corresponding data from yfinance
    Saves the data to parquet files"""
    config = load_config("configs/assets.yaml")
    equities_data = fetch_equities(config)
    macro_data = fetch_macro(config)
    equities_data.to_parquet("data/raw/equities.parquet")
    macro_data.to_parquet("data/raw/macro.parquet")

run_ingestion()