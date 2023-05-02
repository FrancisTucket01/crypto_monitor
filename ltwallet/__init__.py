from flask import Flask
# import flask_monitoringdashboard as dashboard
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
# from dynamic_sitemap import ChangeFreq, FlaskSitemap
#dashboard.config.init_from(file='/<path to file>/config.cfg')

app = Flask(__name__)
# dashboard.bind(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////content/drive/MyDrive/Envs/Flaskt/flaskt/mydb.sqlite3'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'litwallet'

 
mysql = MySQL(app)

# sitemap = FlaskSitemap(app, 'https://cyan-mirrors-smile-34-86-111-132.loca.lt')
# sitemap.build()
 

from ltwallet import routes
