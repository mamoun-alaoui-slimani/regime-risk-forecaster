import yfinance as yf
import pandas as pd
import yaml
import pyarrow

def load_config(config_path):
    with open(config_path, "r") as f:
        assets = yaml.safe_load(f)
    return assets

def fetch_equities(config):
    return yf.download(config["equities"], config["start_date"], auto_adjust=True)

def fetch_macro(config):
    return yf.download(config["macro"], config["start_date"], auto_adjust=True)

def run_ingestion():
    config = load_config("configs/assets.yaml")
    equities_data = fetch_equities(config)
    macro_data = fetch_macro(config)
    equities_data.to_parquet("data/raw/equities.parquet")
    macro_data.to_parquet("data/raw/macro.parquet")

run_ingestion()