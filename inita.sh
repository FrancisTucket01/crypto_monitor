#!/bin/bash
apt-get update 
apt-get install mysql-server
apt upgrade
service mysql start
pip -q install PyMySQL flask_sqlalchemy flask_mysqldb flask_wtf flask_session
npm install -g localtunnel
mysql -u root --password=root -e "CREATE DATABASE litwallet;"
mysql -u root --password=root litwallet < database_dumps/litwtt.sql
lt --subdomain cyan-mirrors-smile-34-86-111-132 --port 5000