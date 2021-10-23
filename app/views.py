from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify, abort, g
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import functools
import controlador_hotel

main = blueprints.Blueprint('main', __name__)

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

def admin_required(f):
    @functools.wraps(f)
    def decorated_function(**kwargs):
        if 'usr_rol' in session:
            is_rol = session.get('usr_rol')
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

@main.route('/adm/adm_habitaciones/')
@login_required
@admin_required
def adm_habitaciones():
    return render_template('/adm/adm_habitaciones.html')

@main.route('/adm/adm_reservas/')
@login_required
@admin_required
def adm_reservas():
    return render_template('/adm/adm_reservas.html')

@main.route('/adm/adm_comentarios/')
@login_required
@admin_required
def adm_comentarios():
    return render_template('/adm/adm_comentarios.html')
    
@main.route('/adm/adm_users/')
@login_required
@admin_required
def admin_users():
    return render_template('/adm/adm_users.html')

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