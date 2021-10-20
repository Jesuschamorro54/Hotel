import functools
from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from markupsafe import escape

salt = "misiontic2022Grupo1"

main= blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

def login_required(view):

    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'usr_email' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)
    
    return wraped_view

@main.route('/usr_login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):

        usr_email = request.form['usr_email']
        usr_password = request.form['usr_password']

        if(usr_email =='ricagome@mail.com' and usr_password =='1234'):
            session['usr_email'] = 'ricagome@mail.com' #user[2]
            session['nombre'] = 'Ricardo Gomez' #user[1]
            session['id'] = '1' #user[0]
            session['role'] = 'otro'
            session['acc'] = True
            return redirect(url_for('main.dashboard'))

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

            return redirect(url_for('main.login'))

    return render_template('usr_registro.html')

@main.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/habitaciones/')
@login_required
def habitaciones():
    return render_template('habitaciones.html')

@main.route('/comments/')
@login_required
def comments():
    return render_template('comentarios.html')

@main.route('/adm/adm_habitaciones/')
@login_required
def adm_habitaciones():
    return render_template('/adm/adm_habitaciones.html')

@main.route('/adm/adm_reservas/')
@login_required
def adm_reservas():
    return render_template('/adm/adm_reservas.html')

@main.route('/adm/adm_comentarios/')
@login_required
def adm_comentarios():
    return render_template('/adm/adm_comentarios.html')
    
@main.route('/adm/adm_users/')
@login_required
def admin_users():
    return render_template('/adm/adm_users.html')

@main.route('/logout/')
def logout():
   session.clear()
   return redirect(url_for('main.index'))


