from flask import Blueprint, render_template, request, jsonify
import requests
from config import HEADEARS, JSONBIN_URL_DESTINOS

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard/nosotros.html')

@dashboard_bp.route('/destinos')
def dashboarddestinos():
    return render_template('dashboard/destinos.html')

@dashboard_bp.route('/reserva')
def dashboardreserva():
    return render_template('dashboard/reserva.html')

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
