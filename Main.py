from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

from views.views import *
app.register_blueprint(views)




#@app.route('/cadastro')
#def cadastro():
    #return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)