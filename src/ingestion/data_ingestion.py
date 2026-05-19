import yfinance as yf
import pandas as pd

dat = yf.Ticker("MSFT")
print(dat.info)
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')
dat.option_chain(dat.options[0]).calls

test = pd.DataFrame(dat.history(period='1mo'))
test.to_csv('msft.csv')