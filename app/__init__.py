from flask import Flask
from flask_mysqldb import MySQL
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp
import mysql.connector 
from config import Config
 # instancia global 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    connection = mysql.connector.connect(
                host='localhost',           # Servidor (localhost en XAMPP)
                user='root',                # Usuario de MySQL (por defecto en XAMPP)
                password='',                # Contraseña (vacía por defecto en XAMPP)
                database='tourism' # Cambia por el nombre de tu base de datos
            )
    # Configuración de la base de datos
    """ 
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'tourism'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_DATABASE_CONNECT_OPTIONS'] = {"reconnect": True}  # Reconectar automáticamente

    mysql.init_app(app)  # Inicializar MySQL 

    """
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    """
    @app.teardown_appcontext
    def close_db_connection(exception):
        if mysql.connection:
            mysql.connection.close()

     PRUEBA DE CONEXION: resultado-> exitoso
    with app.app_context():
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT DATABASE();")  # Consulta de prueba
            db_name = cur.fetchone()
            print(f"Conexión exitosa. Base de datos activa: {db_name[0]}")
            cur.close()
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")

    """
    return app
