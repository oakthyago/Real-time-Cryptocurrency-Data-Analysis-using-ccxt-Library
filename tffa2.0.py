import ccxt
import pandas as pd
import pyautogui
import asyncio
#from statsmodels.tsa.arima_model import ARIMA
#import numpy as np
import time
#import datetime
#import matplotlib.pyplot as plt

#Function that calls ARIMA model to fit and forecast the data

async def Bruto (data,sym,tempo):
    data = column(data, 4)
    pd.options.display.float_format = '{:,.8f}'.format
    df = pd.DataFrame(data=data)

    azuldf = df.rolling(window=3).mean()
    brancodf = df.rolling(window=8).mean()
    amarelodf = df.rolling(window=20).mean()

    azul = (azuldf - brancodf).values
    amarelo = (amarelodf - brancodf).values

    if (azul[19] - amarelo[19]) < 0 and (azul[20] - amarelo[20]) > 0:
        print(sym, tempo)


async def main () :

    print("Time First Agulhada")
    exchange = ccxt.binance({
        'rateLimit': 0.01,
       'enableRateLimit': True,
        # 'verbose': True,
    })

    while True:
        exchange.load_markets(True)
        sym = exchange.symbols



        for sym in sym:


                    if ("BTC" in sym) and ("ICN" not in sym)and ("BCC" not in sym):

                  #      if sym != "BCN/BTC" or sym != "ICN/BTC" or sym != "BCC/BTC":
                            print("1")

                            data = exchange.fetch_ohlcv(sym, '1m', limit=21)
                            data2 = exchange.fetch_ohlcv(sym,'5m' , limit=21)
                            data3 = exchange.fetch_ohlcv(sym, '15m', limit=21)
                            data4 = exchange.fetch_ohlcv(sym, '30m', limit=21)
                            data5 = exchange.fetch_ohlcv(sym, '1h', limit=21)
                            print("2")
                            await Bruto(data,sym,'1m')
                            await Bruto(data2,sym,'5m')
                            await Bruto(data3,sym,'15m')
                            await Bruto(data4,sym,'30m')
                            await Bruto(data5,sym,'1h')
                            print("3")





def column(matrix, i):
    return [row[i] for row in matrix]



asyncio.run(main())