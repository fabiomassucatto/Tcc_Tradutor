from flask import Flask, render_template, request, redirect, flash
from db import mysql
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] = 'TCC_banco'

mysql.init_app(app)

from views.views import *
app.register_blueprint(views)



if __name__ == "__main__":
    app.run(debug=True)