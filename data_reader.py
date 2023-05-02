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
#from flask_mysqldb import MySQL

years = [2012,2013,2014]
years1 = [2015,2016]
years2 = [2018,2017]
years3 = [2019,2020]
years4 = [2021, 2022]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
months2 = [1,2,3,4,5,6,7,8,9]



def get_historical_news(url):
    #setting chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    News = []
    wd = webdriver.Chrome("chromedriver", options=options)
    url = url
    #getting the html document en text
    wd.get(url)
    
    sections = wd.find_elements(By.CLASS_NAME, 'my-6')
    
    
    for section in sections:
      head = section.find_element(By.CLASS_NAME, 'dfx-h-3').text
      sub_sections = section.find_elements(By.CLASS_NAME, 'dfx-articleListItem__inner')
      for sub_section in sub_sections:
          headline = sub_section.find_element(By.CLASS_NAME, 'dfx-articleListItem__title').text
          date = sub_section.find_element(By.CLASS_NAME, 'jsdfx-articleListItem__date').text
          author = sub_section.find_element(By.CLASS_NAME, 'dfx-articleListItem__author').text.replace(', by ', '')
          current = [head, headline, date, author]
          News.append(current)
    wd.close()
    return News


def write(x, name):
  file_name = f'{name}.csv'
  with open(file_name, 'a', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(x)



def main(year_count):
  for i in year_count:
      for j in months:
          if j in months2:
              url = (f'https://www.dailyfx.com/archive/{i}/0{j}')
          else:
              url = (f'https://www.dailyfx.com/archive/{i}/{j}')
          write(get_historical_news(url), year_count)

# my_years = [years1, years2, years3, years4]
# for i in my_years:
#   main(i)
 
# opening the CSV file
def inserter(linker):
    with open(linker, mode ='r')as file:
    
        # reading the CSV file
        csvFile = csv.reader(file)
        with app.app_context():
            cursor = mysql.connection.cursor()
            with  cursor as f:
                for lines in csvFile:
                    date =lines[0].replace(',','').replace('(','').replace(')','')
                    info = lines[1]
                    author = lines[3].replace("'","")
                    year = int(re.findall(r'\d+', date)[1])
                    smt = f"INSERT INTO sentiment(date, year, info, author) VALUES('{date}', {year}, '{info}', '{author}');"
                    print(smt)
                    f.execute(smt)
                mysql.connection.commit()
                cursor.close()

f= ['/content/drive/MyDrive/Envs/Flaskt/CCsvs/[2017].csv', '/content/drive/MyDrive/Envs/Flaskt/CCsvs/[2018, 2017].csv', '/content/drive/MyDrive/Envs/Flaskt/CCsvs/news.csv', '/content/drive/MyDrive/Envs/Flaskt/CCsvs/[2015, 2016].csv', '/content/drive/MyDrive/Envs/Flaskt/CCsvs/[2016].csv']
for vals in f:
    inserter(vals)


