from flask import Flask, render_template, blueprints, request, flash, redirect, url_for, jsonify

main= blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usr_login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):

        usr_email = request.form['usr_email']
        usr_password = request.form['usr_password']

        if(usr_email =='ricagome@mail.com' and usr_password =='1234'):

            return render_template('dashboard.html')

    return render_template('usr_login.html')

@main.route('/usr_registro/', methods=['GET', 'POST'])
def registro():
    if(request.method == 'POST'):

        usr_name = request.form['usr_name']
        usr_lastname = request.form['usr_lastname']
        usr_email = request.form['usr_email']
        usr_password = request.form['usr_password']
        usr_checkbox = request.form['usr_checkbox']

        if(usr_checkbox =='1'):

            return render_template('usr_login.html')

    return render_template('usr_registro.html')

@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@main.route('/adm_seguridad/')
def adm_seguridad():
    return render_template('adm_seguridad.html')


@main.route('/habitaciones/')
def habitaciones():
    return render_template('habitaciones.html')

@main.route('/comments/')
def comments():
    return render_template('comentarios.html')

@main.route('/adm_habitaciones/')
def adm_habitaciones():
    return render_template('adm_habitaciones.html')

@main.route('/adm_reservas/')
def adm_reservas():
    return render_template('adm_reservas.html')

@main.route('/adm_comentarios/')
def adm_comentarios():
    return render_template('adm_comentarios.html')

