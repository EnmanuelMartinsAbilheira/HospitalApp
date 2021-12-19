from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_DB']   = 'hospital'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)
app.secret_key='skey'