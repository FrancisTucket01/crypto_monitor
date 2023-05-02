import requests as re
import json
import os
import time
from ltwallet import mysql, app
import yfinance as yf
import pandas as pd

SECRET_KEY = "7JWIUY69T87W83GH"

def create_tables(quote):
    q1 = quote.split("-")
    q2 = q1[0] + q1[1]
    q2 = q2.replace("USD", "KSH")
    print(q2)
    s1 = f"mysql -u root --password=root -e 'USE litwallet; DELETE FROM {q2}D';"
    os.system(s1)
    smt = f"mysql -u root --password=root -e 'USE litwallet; CREATE TABLE {q2}D(id INT PRIMARY KEY AUTO_INCREMENT, date DATE, open FLOAT(12), high FLOAT(12), low FLOAT(12), close FLOAT(12), volume FLOAT(12), marketcap FLOAT(12))';"
    os.system(smt)
    ur1 = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_symbol={q1[0]}&to_symbol={q1[1]}&outputsize=full&datatype=json&apikey={SECRET_KEY}"


def get_data(quote):
    q1 = quote.split("-")
    q2 = q1[0] + q1[1]
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={q1[0]}&market={q1[1]}&apikey=7JWIUY69T87W83GH"
    data = re.get(url).text
    data = json.loads(data)
    print(url)
    with app.app_context():
                cursor = mysql.connection.cursor()
                with  cursor as f:
                    for i in data['Time Series (Digital Currency Daily)'].keys():
                        openn = data['Time Series (Digital Currency Daily)'][i]['1a. open (USD)']
                        high = data['Time Series (Digital Currency Daily)'][i]['2a. high (USD)']
                        low = data['Time Series (Digital Currency Daily)'][i]['3a. low (USD)']
                        close = data['Time Series (Digital Currency Daily)'][i]['4a. close (USD)']
                        vol = data['Time Series (Digital Currency Daily)'][i]['5. volume']
                        marketcap = data['Time Series (Digital Currency Daily)'][i]['6. market cap (USD)']
                        smt = f"INSERT INTO {q2}D(date, open, high, low, close, volume, marketcap) VALUES('{i}', {openn}, {high}, {low}, {close},{vol}, {marketcap});"

                        f.execute(smt)   
                        print(smt)
                mysql.connection.commit()
                cursor.close()
# "BNB-USD",
quotes_crypto = ["BTC-USD","ETH-USD","XRP-USD","DOGE-USD", "MATIC-USD", "SOL-USD"]
# quotes = ["GBP-USD", "GBP-EUR","GBP-CAD","GBP-AUD","GBP-CHF", "EUR-USD","EUR-JPY","EUR-CHF","EUR-AUD","USD-CAD","USD-CHF", "USD-AUD","USD-JPY"]
# for quote in quotes_crypto:
#     create_tables(quote)
#     get_data(quote)
#     time.sleep(3)

def get_yf(ticker):
    q1 = quote.split("-")
    q2 = q1[0] + q1[1]
    q2=q2.replace("USD", "KSH")
    data = yf.download(ticker, period="5y", interval="1d")
    data.to_csv(f"{ticker}.csv")
    data2=pd.read_csv(f"{ticker}.csv")
    with app.app_context():
        cursor = mysql.connection.cursor()
        with  cursor as f:
            for row in range(len(data-1)):
                close = data2['Close'][row]
                openn = data2['Open'][row]
                high = data2['High'][row]
                low = data2['Low'][row]
                volume = data2['Volume'][row]
                date = data2["Date"][row]
                smt = f"INSERT INTO {q2}D(date, open, high, low, close, volume) VALUES('{date}', {openn}, {high}, {low}, {close},{volume});"
                print(smt)

                f.execute(smt) 
        mysql.connection.commit()
        cursor.close()
for quote in quotes_crypto:
    create_tables(quote)
    get_yf(quote)