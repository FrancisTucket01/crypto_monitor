#!/bin/bash
apt-get update
apt-get install mysql-server > /dev/null
apt-get update
pip install selenium
apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver /usr/bin > /dev/null
service mysql start
pip -q install PyMySQL flask_sqlalchemy flask_mysqldb flask_wtf flask_session
mysql -u root --password=root -e "CREATE DATABASE litwallet; USE litwallet; CREATE TABLE users(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255), password varchar(255), email_address varchar(255 ) DEFAULT NULL); INSERT INTO users(name, password) VALUES('Francis', 'Tucket');"
mysql -u root --password=root -e "USE litwallet; CREATE TABLE currency(id int PRIMARY KEY AUTO_INCREMENT, heading varchar(255), title varchar(255), time varchar(255), author varchar(255), link varchar(255));"
npm install -g localtunnel
