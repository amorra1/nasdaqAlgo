import yfinance as yf
import datetime as dt
import numpy as np

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 1, 1)

# Fetch historical data for the S&P 500
data = yf.download('^NDX', start, end)

#print(data)

closePrices = data['Close']


