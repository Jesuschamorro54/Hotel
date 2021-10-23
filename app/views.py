import functools
from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import controlador_hotel
import json

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
        #db = get_db()

        #user = "1234"
        #if user is not None:
            # usr_password = usr_password + usr_email
            # sw = check_password_hash(user[4], usr_password)

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

            #agregar SLAT
            usr_password = usr_password + usr_email
            #usr_password = generate_password_hash(usr_password)

            controlador_hotel.insertar_user(usr_name+' '+usr_lastname, usr_email, usr_password)

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

@main.route('/adm/habitaciones/')
@login_required
def adm_habitaciones():
    rooms = controlador_hotel.consultar('rooms')
    return render_template('/adm/habitaciones.html', rooms_list = rooms)

@main.route('/adm/reservas/')
@login_required
def adm_reservas():
    return render_template('/adm/reservas.html')

@main.route('/adm/comentarios/')
@login_required
def adm_comentarios():
    return render_template('/adm/comentarios.html')
    
@main.route('/adm/users/')
@login_required
def admin_users():
    users = controlador_hotel.consultar('users')
    return render_template('/adm/users.html', users_list=users)

@main.route('/logout/')
def logout():
   session.clear()
   return redirect(url_for('main.index'))

#  -------------------  METODOS DE GESTION --------------------------- #
@main.route('/eliminar/', methods = ['GET', 'POST'])
@login_required
def eliminar():
    data = request.get_json(force=True)
    controlador_hotel.eliminar(int(data["id"]), data["table"] )

    users = controlador_hotel.consultar_usuarios()
    lista = []
    for user in users:
        dic = {
            'id': user[0] ,
            'nombre': user[1],
            'email': user[3]
        }
        lista.append(dic)

    print(lista)

    return jsonify({
        'status': 'OK',
        'user': lista   
    })

@main.route('/search/', methods = ['GET', 'POST'])
@login_required
def search():
    data = request.get_json(force=True)
    users = controlador_hotel.find(data["parameter"], data["search"], data["table"])

    return jsonify({
        'status': 'OK',
        'user': 'none'   
    })