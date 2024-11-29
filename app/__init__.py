from flask import Flask
from flask_mysqldb import MySQL
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp

mysql = MySQL()  # Crear la instancia global aquí

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'tourism'
    app.config['MYSQL_PORT'] = 3306

    mysql.init_app(app)  # Inicializar MySQL con la app

    # Registrar Blueprints
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    return app
