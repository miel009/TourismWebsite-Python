# app/blueprints/auth/routes.py

from flask import Blueprint, render_template , jsonify, request
import requests
from config import HEADEARS, JSONBIN_URL_USUARIOS

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
# auth_bp es como usabamos app

@auth_bp.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return jsonify({'mensaje': 'Usuario y contraseña son obligatorios.'}), 400

        # Obtener los usuarios de JSONBin
        response = requests.get(JSONBIN_URL_USUARIOS, headers=HEADEARS)
        if response.status_code != 200:
            return jsonify({'mensaje': 'Error al obtener datos.'}), 500

        # Verificar la estructura de la respuesta 
        data = response.json()
        print("Contenido de la respuesta JSON:", data)  # imprime la respuesta

        # Comprobación de 'record' en el nivel principal
        if 'record' not in data:
            return jsonify({'mensaje': 'El JSON no contiene "record".'}), 500

        if not isinstance(data['record'], list):
            return jsonify({'mensaje': '"record" no es una lista.'}), 500

        users = data['record']

        # Valida
        for user in users:
            if isinstance(user, dict) and user.get('username') == username:
                if user.get('password') == password:
                    
                    return render_template('auth/ingreso.html'), 200
                else:
                    return jsonify({'mensaje': 'Contraseña incorrecta.'}), 401

        return jsonify({'mensaje': 'Usuario no encontrado.'}), 404

    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return jsonify({'mensaje': 'No puede ser vacío'}), 400

        response = requests.get(JSONBIN_URL_USUARIOS, headers=HEADEARS)
        if response.status_code != 200:
            return jsonify({'mensaje': 'Error al obtener datos'}), 500

        # Verificar la estructura de la respuesta JSON
        data = response.json()
        print("Contenido de la respuesta JSON:", data)  #imprime la rsp

        # Comprobación de 'record' en el nivel principal
        if 'record' not in data:
            return jsonify({'mensaje': 'El JSON no contiene "record"'}), 500

        if not isinstance(data['record'], list):
            return jsonify({'mensaje': '"record" no es una lista'}), 500

        users = data['record']

        # Verificar si el usuario ya existe
        for user in users:
            if isinstance(user, dict) and user.get('username') == username:
                return jsonify({'mensaje': 'El usuario ya existe'}), 400

        # Agregar nuevo usuario
        nuevo = {
            'username': username,
            'password': password
        }
        users.append(nuevo)

        # Actualizar datos  sin "record"
        response = requests.put(JSONBIN_URL_USUARIOS, json={"record": users}, headers=HEADEARS)
        if response.status_code == 200:
            return render_template("auth/registerExitoso.html")
        else:
            return jsonify({'mensaje': 'Error al actualizar datos'}), 500

    return render_template('auth/register.html')

@auth_bp.route('/registerExitoso')
def registerExitoso():
    return render_template('auth/registerExitoso.html')