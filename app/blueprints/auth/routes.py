# app/blueprints/auth/routes.py

from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    from app import mysql
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Usuario y contraseña son obligatorios.', 'error')
            return redirect(url_for('auth.login'))

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password FROM usuarios WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard.dashboard')) 
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    from app import mysql
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Usuario y contraseña son obligatorios.', 'error')
            return redirect(url_for('auth.register'))

        cur = mysql.connection.cursor()
        
        cur.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            cur.close()
            flash('El usuario ya existe.', 'error')
            return redirect(url_for('auth.register'))

        # ingresa un user
        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cur.close()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente.', 'success')
    return redirect(url_for('auth.login'))
