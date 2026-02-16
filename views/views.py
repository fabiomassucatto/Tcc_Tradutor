from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/login')
def login():
    return render_template("login.html")


@views.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")
