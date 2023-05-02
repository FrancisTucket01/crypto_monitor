import sys
import time
from ltwallet import mysql, app
import re
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
from termcolor import colored
import csv 
from flask_mysqldb import MySQL

class historical_news():

    def __init__(self, url, year):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.wd = webdriver.Chrome("chromedriver", options=self.options)
        self.url = url
        self.year = year

    def get_data(self):
        self.wd.get(self.url)
        sections = self.wd.find_elements(By.CLASS_NAME, 'my-6')
        for section in sections:
            head = section.find_element(By.TAG_NAME, 'h2').text
            sub_section = section.find_elements(By.CLASS_NAME, 'jsdfx-archivearticleList')
            for sub in sub_section:
                headline = sub.find_elements(By.CLASS_NAME, 'dfx-articleListItem__title')
                entry_date = sub.find_elements(By.CLASS_NAME, 'dfx-articleListItem__date')
                author = sub.find_elements(By.CLASS_NAME, 'dfx-articleListItem__author')
                print(head)
                print(headline)
                print(entry_date)
                print(author)



years = [2012,2013,2014]
years1 = [2015,2016,2017]
years2 = [2018,2019,2020,2021]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
months2 = [1,2,3,4,5,6,7,8,9]

for i in years:
    for j in months:
        if j in months2:
            url = f'https://www.dailyfx.com/archive/{i}/0{j}'
        else:
           url = f'https://www.dailyfx.com/archive/{i}/{j}'
        H = historical_news(url,i)
        H.get_data()
