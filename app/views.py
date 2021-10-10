from flask import Flask, render_template, blueprints, request, flash, redirect, url_for, jsonify

main= blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usr_login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):

        user_name= request.form['user_name']
        usrpassword = request.form['usrpassword']

        if(user_name =='ricagome@mail.com' and usrpassword =='1234'):

            return render_template('dashboard.html')

    return render_template('usr_login.html')

@main.route('/usr_registro/')
def registro():
    return render_template('usr_registro.html')

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
