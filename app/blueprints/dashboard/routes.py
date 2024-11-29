from flask import Blueprint, render_template, request, jsonify, url_for, redirect,current_app
import requests
from config import HEADEARS, JSONBIN_URL_DESTINOS
from flask_mysqldb import MySQL

dashboard_bp = Blueprint('dashboard', __name__)
mysql = MySQL()


@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard/nosotros.html')

@dashboard_bp.route('/destinos')
def dashboarddestinos():
   return render_template('dashboard/destinos.html')


@dashboard_bp.route('/paquetes')
def dashboardpaquetes():
    response = requests.get(JSONBIN_URL_DESTINOS,headers=HEADEARS)
    if response.status_code == 200:
        data = response.json() 
        paquetes = data.get('record', []) 
        #print(data) 
        return render_template('dashboard/paquetes.html', paquetes= paquetes)  
    else:
        return jsonify({"error": "Error al cargar los datos."}), response.status_code
    
@dashboard_bp.app_template_filter("format_price")
def format_price(value):
    return "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")



@dashboard_bp.route('/reserva', methods=['GET'])
def dashboardreserva():
    try:
        mysql = current_app.extensions['mysql']  # Acceder al objeto MySQL
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM reservas")
        reservas = cursor.fetchall()  # RESERVAS
        cursor.close()
        
        return render_template('reserva.html', reservas=reservas)
    except Exception as e:
        return f"Error al acceder a la base de datos: {e}", 500

@dashboard_bp.route('/test_db')
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM reservas")
        cursor.close()
        return "Conexión a la base de datos exitosa"
    except Exception as e:
        return f"Error de conexión: {str(e)}"