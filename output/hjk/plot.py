import datetime

import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as web

def plot_rub_usd():
    yf.pdr_override()
    df=web.DataReader('USDRUB=X', datetime.datetime.today()-datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()


def plot_usd_btc():
    yf.pdr_override()
    df=web.DataReader('BTC-USD', datetime.datetime.today()-datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()

def plot_usd_yn():
    yf.pdr_override()
    df = web.DataReader('USDJPY=X', datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()

def plot_more():
    plt.plot([2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010 ], [0.99, 1.43, 1.30, 1.20, 1.72, 1.84, 2.67, 2.18, 3.05])
    plt.show()
