from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect,current_app
import requests

from config import HEADEARS, JSONBIN_URL_DESTINOS
import mysql.connector 

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



@dashboard_bp.route('/listareserva', methods=['GET', 'POST'])
def dashboardlistareserva():
    try:
        connection = mysql.connector.connect(
            host='localhost',           
            user='root',                
            password='',               
            database='tourism'          
        )
        cursor = connection.cursor()

       
        sql = "SELECT id, nombre, email, nombre_destino, fecha_reserva, numero_personas, precio_total, imagen FROM reservas"
        cursor.execute(sql)
        reservas = cursor.fetchall()  # obtenemos todas las filas de resultados

        return render_template('dashboard/listareserva.html', reservas=reservas)

    except mysql.connector.Error as e:
        flash(f'Error al cargar las reservas: {e}', 'danger')
        return render_template('dashboard/listareserva.html')

    finally:
        # cerrar 
        cursor.close()
        connection.close()



@dashboard_bp.route('/reserva', methods=['GET', 'POST'])
def dashboardreserva():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        paquete_id_str = request.form.get('paquete_id')

        if not paquete_id_str:
            flash("No se recibió el ID del paquete.", "danger")
            return redirect(url_for('dashboard.dashboardpaquetes'))

        paquete_id = int(paquete_id_str)
        fecha_reserva = request.form.get('fecha_reserva')
        numero_personas = int(request.form.get('numero_personas'))

        # Obtener JSONBin
        response = requests.get(JSONBIN_URL_DESTINOS, headers=HEADEARS)
        paquetes = response.json()['record']

        # buscar el paquete 
        paquete = next((p for p in paquetes if p["id"] == paquete_id), None)
        if not paquete:
            flash("Paquete no encontrado.", "danger")
            return redirect(url_for('dashboard.dashboardpaquetes'))

        nombre_destino = paquete["destino"]
        duracion = paquete["duracion"]
        mes = paquete["mes"]
        incluye = ", ".join(paquete["incluye"])
        precio_por_persona = float(paquete["precio_por_persona"])
        imagen = paquete["imagen"]
        precio_total = numero_personas * precio_por_persona

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='tourism'
            )
            cursor = connection.cursor()

            sql = """
            INSERT INTO reservas (
                nombre, email, paquete_id, nombre_destino, duracion, mes, incluye,
                fecha_reserva, numero_personas, precio_total, imagen
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                nombre, email, paquete_id, nombre_destino, duracion, mes, incluye,
                fecha_reserva, numero_personas, precio_total, imagen
            ))
            connection.commit()
            flash('Reserva creada exitosamente.', 'success')
        except mysql.connector.Error as e:
            connection.rollback()
            flash(f'Error al guardar reserva: {e}', 'danger')
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('dashboard.dashboardlistareserva'))

    # GET - mostrar formulario con ID del paquete
    paquete_id = request.args.get('paquete_id', type=int)
    if not paquete_id:
        flash("No se especificó un paquete.", "danger")
        return redirect(url_for('dashboard.dashboardpaquetes'))

    return render_template('dashboard/reserva.html', paquete_id=paquete_id)

@dashboard_bp.route('/eliminar_reserva/<int:id>', methods=['POST'])
def eliminar_reserva(id):
    try:
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tourism'
        )
        cursor = connection.cursor()

        
        sql = "DELETE FROM reservas WHERE id = %s"
        cursor.execute(sql, (id,))
        connection.commit()

        flash('Reserva eliminada exitosamente.', 'success')
    except mysql.connector.Error as e:
        flash(f'Error al eliminar la reserva: {e}', 'danger')
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('dashboard.dashboardlistareserva'))
    
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
