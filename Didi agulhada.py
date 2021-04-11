import ccxt
import pandas as pd
import pyautogui
import asyncio
from statsmodels.tsa.arima_model import ARIMA
#import numpy as np





import time
#import datetime
#import matplotlib.pyplot as plt

#Function that calls ARIMA model to fit and forecast the data



def clique (tempo):
    pyautogui.click(300, 300)
    pyautogui.typewrite(tempo)
    time.sleep(0.5)
    pyautogui.hotkey('Enter')


async def escreve (sym):

    pyautogui.click(149, 98)   
    time.sleep(0.2)
    pyautogui.typewrite(sym.replace("/", ""),interval=0.1)
    pyautogui.hotkey('Enter')
    time.sleep(10)

async def main () :
    time = ['30m', '1h', '2h', '4h']
    timegui = ['30', '1h', '2h', '4h']
    a = 0
    print("Didi index")
    exchange = ccxt.binance({
        'rateLimit': 100,
       'enableRateLimit': True,
        # 'verbose': True,
    })

    while True:
        exchange.load_markets(True)
        sym = exchange.symbols
        print(time[a])

        clique(timegui[a])
        for sym in sym:
            #print(sym)		
            if ("BTC" in sym) and ("ICN" not in sym)and ("BCC" not in sym)and ("AE" not in sym)and ("TORJ" not in sym)and ("BCN" not in sym)and("TKO" not in sym)and("AUTO" not in sym)and ("EPS" not in sym)and ("CAKE" not in sym)and ("KAVA" not in sym)and ("SUPER" not in sym)and ("CFX" not in sym)and ("ZAR" not in sym):
          #      if sym != "BCN/BTC" or sym != "ICN/BTC" or sym != "BCC/BTC":

                    data = exchange.fetch_ohlcv(sym, time[a], limit=21)
                    data = column(data,4)
                    pd.options.display.float_format = '{:,.8f}'.format
                    df = pd.DataFrame(data=data)


                    azuldf = df.rolling(window=3).mean()
                    brancodf = df.rolling(window=8).mean()
                    amarelodf = df.rolling(window=20).mean()

                    azul = (azuldf-brancodf).values
                    amarelo = (amarelodf-brancodf).values


                    #if (azul[19] - amarelo[19]) > 0 and (azul[20] - amarelo[20]) < 0:
                         #print("Nao")  
			 #print(sym)
                   # else:
                    #    time.sleep(1)

                    if (azul[19] - amarelo[19]) < 0 and (azul[20] -amarelo[20] )> 0:
                            print(sym)
                            await escreve(sym)			
                  			   

        a+=1
	
        if a == 4:
            a=0

def column(matrix, i):
    return [row[i] for row in matrix]



asyncio.run(main())