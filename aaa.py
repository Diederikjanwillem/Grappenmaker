
#%%

import pandas as pd
import pandas_ta as ta
import yfinance as yf
import requests
import matplotlib.pyplot as plt
import numpy as np 
import xlwings as xw 






api_key = ("tSphbGZVPQndGGqwFzOkC9uYOf47GdQI")
ticker ="ARDX"
BASE_URL = "https://financialmodelingprep.com/api/v3/"


def get_profile(symbol,key):
    url = f"{BASE_URL}profile/{symbol}?apikey={key}"
    request = requests.get(url).json()
    data = pd.DataFrame(request)
    return data


get_profile(symbol=ticker,key=api_key)


def income_statement(symbol,key):
    url =f"{BASE_URL}income-statement/{symbol}?apikey={key}"
    request =requests.get(url).json()
    data =pd.DataFrame(request)
    return data 




book =  xw.Book()
sheet =book.sheets[0]

sheet.range("C1").value = income_statement("ARDX",key=api_key).T
