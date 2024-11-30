from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect,current_app
import requests

from config import HEADEARS, JSONBIN_URL_DESTINOS
import mysql.connector 

 # Conector compatible con XAMPP


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
        # Conectar a la base de datos MySQL
        connection = mysql.connector.connect(
            host='localhost',           # Servidor (localhost en XAMPP)
            user='root',                # Usuario de MySQL (por defecto en XAMPP)
            password='',                # Contraseña (vacía por defecto en XAMPP)
            database='tourism'          # Cambia por el nombre de tu base de datos
        )
        cursor = connection.cursor()

        # Consulta SQL para obtener todas las reservas
        sql = "SELECT id, nombre, email, nombre_destino, fecha_reserva, numero_personas, precio FROM reservas"
        cursor.execute(sql)
        reservas = cursor.fetchall()  # Obtener todas las filas de resultados

        return render_template('dashboard/listareserva.html', reservas=reservas)

    except mysql.connector.Error as e:
        flash(f'Error al cargar las reservas: {e}', 'danger')
        return render_template('dashboard/listareserva.html')

    finally:
        # Cerrar conexión y cursor
        cursor.close()
        connection.close()



@dashboard_bp.route('/reserva', methods=['GET', 'POST'])
def dashboardreserva():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        nombre_destino = request.form.get('nombre_destino')
        fecha_reserva = request.form.get('fecha_reserva')
        numero_personas = request.form.get('numero_personas')

        # Calcular precio (ejemplo: 100.0 por persona)
        precio_por_persona = 100.0
        precio = int(numero_personas) * precio_por_persona

        try:
            # Conectar a la base de datos MySQL (ajusta los valores según tu configuración)
            connection = mysql.connector.connect(
                host='localhost',           # Servidor (localhost en XAMPP)
                user='root',                # Usuario de MySQL (por defecto en XAMPP)
                password='',                # Contraseña (vacía por defecto en XAMPP)
                database='tourism' # Cambia por el nombre de tu base de datos
            )
            cursor = connection.cursor()

            # Consulta SQL para insertar la reserva
            sql = """
            INSERT INTO reservas (nombre, email, paquete_id, nombre_destino, fecha_reserva, numero_personas, precio)
            VALUES (%s, %s, NULL, %s, %s, %s, %s)
            """
            # Ejecutar consulta
            cursor.execute(sql, (nombre, email, nombre_destino, fecha_reserva, numero_personas, precio))
            connection.commit()  # Confirmar cambios en la base de datos

            # Notificar éxito
            flash('Reserva creada exitosamente.', 'success')
        except mysql.connector.Error as e:
            # Manejar errores de MySQL
            connection.rollback()  # Revertir cambios en caso de error
            flash(f'Error al crear la reserva: {e}', 'danger')
        finally:
            # Cerrar conexión y cursor
            cursor.close()
            connection.close()

        # Redirigir al listado de reservas
        return redirect(url_for('dashboard.dashboardlistareserva'))

    # Si es GET, renderiza el formulario
    return render_template('dashboard/reserva.html')

@dashboard_bp.route('/eliminar_reserva/<int:id>', methods=['POST'])
def eliminar_reserva(id):
    try:
        # Conectar a la base de datos MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tourism'
        )
        cursor = connection.cursor()

        # Consulta SQL para eliminar la reserva
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
