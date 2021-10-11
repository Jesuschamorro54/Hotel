from flask import Flask, render_template, blueprints, request, flash, redirect, url_for

main= blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@main.route('/adm_seguridad/')
def adm_seguridad():
    return render_template('adm_seguridad.html')


@main.route('/habitaciones/')
def habitaciones():
    return render_template('habitaciones.html')