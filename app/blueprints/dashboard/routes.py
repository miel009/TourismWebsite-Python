from flask import Blueprint, render_template, request, jsonify, url_for, redirect,current_app
import requests
from config import HEADEARS, JSONBIN_URL_DESTINOS
from flask_mysqldb import MySQL
import MySQLdb

mysql = MySQL()

dashboard_bp = Blueprint('dashboard', __name__)

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
    import MySQLdb
    try:
        # Usar la instancia global de mysql
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM reservas")
        reservas = cursor.fetchall()
        cursor.close()
        return render_template('dashboard/reserva.html', reservas=reservas)
    except Exception as e:
        return f"Error al acceder a la base de datos: {e}", 500


@dashboard_bp.route('/test_mysql')
def test_mysql():
    import MySQLdb
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="",
            db="tourism"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        return "Conexión exitosa a MySQL"
    except Exception as e:
        return f"Error al conectar a MySQL: {str(e)}", 500
