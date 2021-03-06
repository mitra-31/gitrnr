from flask import Flask
from flask_assets import Bundle,Environment
from flask_mysqldb import MySQL
import os

app = Flask (__name__)

imgfolder = os.path.join('static','img')
app.config['UPLOAD_FOLDER'] = imgfolder

css = Bundle ('css/admin.css','css/home.css','css/login.css','css/payment.css',output='gen/main.css')
assets = Environment(app)
assets.register('main_css',css)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'demo'
mysql = MySQL(app)

from app import admin,sign