from flask import Flask, render_template, blueprints, request, flash, redirect, url_for

main= blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usr_registro/')
def registro():
    return render_template('usr_registro.html')

@main.route('/usr_login/')
def login():
    return render_template('usr_login.html')

@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@main.route('/adm_seguridad/')
def adm_seguridad():
    return render_template('adm_seguridad.html')

@main.route('/adm_habitaciones/')
def adm_habitaciones():
    return render_template('adm_habitaciones.html')

@main.route('/adm_reservas/')
def adm_reservas():
    return render_template('adm_reservas.html')
