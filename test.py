# from ltwallet import app, mysql
# from datetime import date
# from functools import reduce

# EMA_LENGTH = 5
# EMA_SOURCE = 'close'

# def qurier():
#     with app.app_context():
#         cursor = mysql.connection.cursor()
#         smt1 = f"select  * from EURUSDH1 where id between 20 and 200;"
#         cursor.execute(smt1)
#         data = cursor.fetchall()
#         epoch_time = date(1970, 1, 1)
#         new_data = []
#         for i in data[:7]:
#             delta = (i[1] - epoch_time).total_seconds()
#             new_data.append({"ts": delta, 'open': i[2], 'high': i[3], 'low': i[4], 'close': i[5]})
#         cursor.close()
#     return new_data

# def calculate_sma(candles, source):
#     length = len(candles)
#     sum = reduce((lambda last, x: { source: last[source] + x[source] }), candles)
#     sma = sum[source] / length
#     return sma

# def calculate_ema(candles, source):
#     length = len(candles)
#     target = candles[0]
#     previous = candles[1]

#     # if there is no previous EMA calculated, then EMA=SMA
#     if 'ema' not in previous or previous['ema'] == None:
#         return calculate_sma(candles, source)

#     else:
#         # multiplier: (2 / (length + 1))
#         # EMA: (close * multiplier) + ((1 - multiplier) * EMA(previous))
#         multiplier = 2 / (length + 1)
#         ema = (target[source] * multiplier) + (previous['ema'] * (1 - multiplier))

#         return ema
# def calculate(candles, source):
#     candles[0]['ema'] = calculate_ema(candles, source)

# candles = qurier()
# position = 0
# while position + EMA_LENGTH <= len(candles):
#     current_candles = candles[position:(position+EMA_LENGTH)]
#     current_candles = list(reversed(current_candles))
#     calculate(current_candles, EMA_SOURCE)
#     position += 1

# print(candles)


import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

cmc = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(cmc.content, 'html.parser')

data = soup.find('script', id='__NEXT_DATA__', type='application/json')
coins = {}
coin_data = json.loads(data.contents[0])
with open('new.txt','a') as f:
    f.write(str(coin_data))
x=json.loads(coin_data['props']['initialState'])
print(x)



