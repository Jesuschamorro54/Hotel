from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify, abort, g
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import functools
import controlador_hotel
from datetime import datetime, timedelta, date
main = blueprints.Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    comments = []
    for id in controlador_hotel.consultar('general_comments'):
        comments.append(list(id))
    #print(comments) 
    rooms = []
    for id in controlador_hotel.consultar('rooms'):
        rooms.append(list(id))
    #print(rooms) 
    return render_template('index.html', rooms_list = rooms, comments_list = comments)

def login_required(view):
    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'usr_email' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)   
    return wraped_view

@main.route('/usr_login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        usr_email = escape(request.form['usr_email'])
        usr_password = escape(request.form['usr_password'])
        
        info_user = controlador_hotel.obtener_user(usr_email)

        if info_user is not None:
            usr_password = usr_password + usr_email
            vpw = check_password_hash(info_user[3], usr_password)

            if(vpw):
                session['id'] = info_user[0]
                session['usr_name'] = info_user[1]
                session['usr_email'] = info_user[2]
                session['usr_rol'] = info_user[4]
                session['acc'] = True
                return redirect(url_for('main.dashboard'))            
        
        return render_template('usr_login.html')

    return render_template('usr_login.html')
    

@main.context_processor
def login_acc():
    if 'acc' in session:
        return {'is_login':True}
    else:
        return {'is_login':False}

@main.route('/usr_registro/', methods=['GET', 'POST'])
def registro():
    if(request.method == 'POST'):
        usr_name = escape(request.form['usr_name'])
        usr_lastname = escape(request.form['usr_lastname'])
        usr_email = escape(request.form['usr_email'])
        usr_password = escape(request.form['usr_password'])
        usr_checkbox = escape(request.form['usr_checkbox'])
 
        if(usr_checkbox =='1'):
            #agregar SLAT
            usr_password = usr_password + usr_email
            usr_password = generate_password_hash(usr_password)
            controlador_hotel.insertar_user(usr_name+' '+usr_lastname, usr_email, usr_password)
            return redirect(url_for('main.login'))
    
    return render_template('usr_registro.html')

@main.route('/usr_reservas/', methods=['GET', 'POST'])
def addReserva():
    if(request.method == 'POST'):
        user_id = session.get('id')
        room_id = escape(request.form['room_id'])
        descriptions = escape(request.form['descriptions'])     
        solicitado = datetime.today()
        date_inicio = escape(request.form['date_inicio'])
        date_final = escape(request.form['date_final'])
        state = 1 
        q_adults = escape(request.form['q_adults'])
        q_childrens = escape(request.form['q_childrens'])
        d1 = request.form['date_final']
        d2 = request.form['date_inicio']
        q_days = abs(((datetime.strptime(d1, '%Y-%m-%d'))-(datetime.strptime(d2, '%Y-%m-%d')))/ timedelta(days=1))
        #controlador_hotel.addreg('reservas',1,1,'prueba 1','2021-10-31 11:00:00','2021-10-31 11:00:00','2021-11-06 11:00:00',1,2,3,365)
        controlador_hotel.insertar_reservas(user_id,4,descriptions,solicitado,date_inicio,date_final,1,q_adults,q_childrens,q_days)
        #controlador_hotel.addreg('reservas',[user_id, room_id, descriptions, solicitado, date_inicio, date_final, state, q_adults, q_childrens, q_days])
        print(room_id)
        return redirect(url_for('main.index'))
    return render_template('usr_reservas.html')


def admin_required(f):
    @functools.wraps(f)
    def decorated_function(**kwargs):
        if 'usr_rol' in session:
            #is_rol = session.get('usr_rol')
            is_rol = 'admin'
            is_admin = True if is_rol=='admin' else False      
        
            if not is_admin:
                is_moder = True if is_rol=='moderador' else False
        
                #if not is_moder:
                    #is_free = True if is_rol=='free' else False
                    #print('es el basico', is_free)

                if not is_admin or not is_moder:
                    #abort(401)
                    return redirect(url_for('main.error', errores = (401)))
        return f(**kwargs)
    return decorated_function

@main.route('/dashboard/')
@login_required
def dashboard():
    #is_rol = session.get('usr_rol')
    is_rol = 'admin'
    g.is_admin = True if is_rol=='admin'else False
    g.is_moder = True if is_rol=='moderador' else False
    g.is_free = True if is_rol=='free' else False
    return render_template('dashboard.html')

@main.route('/habitaciones/')
@login_required
def habitaciones():
    return render_template('habitaciones.html')

@main.route('/comments/')
@login_required
def comments():
    comments = []
    for id in controlador_hotel.consultar('comments'):
        comments.append(list(id))
    return render_template('comentarios.html', comments_list = comments)

@main.route('/adm/habitaciones/')
@login_required
@admin_required
def adm_habitaciones():
    rooms = controlador_hotel.consultar('rooms')
    return render_template('/adm/habitaciones.html', rooms_list = rooms)

@main.route('/adm/reservas/')
@login_required
@admin_required
def adm_reservas():
    return render_template('/adm/reservas.html')

@main.route('/adm/comentarios/')
@login_required
@admin_required
def adm_comentarios():
    return render_template('/adm/comentarios.html')
    
@main.route('/adm/users/')
@login_required
@admin_required
def admin_users():
    users = controlador_hotel.consultar('users')
    return render_template('/adm/users.html', users_list=users)

@main.route('/error/')
@login_required
def error():
    mensa_error = (401)
    return render_template('error.html', errores = 'Error '+ str(mensa_error))

@main.errorhandler(404)
def page_not_found(error):
	return render_template("error.html", errores = "Página no encontrada..."), 404

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

    users = controlador_hotel.consultar('users')
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