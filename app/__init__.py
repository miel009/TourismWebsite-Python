from flask import Flask
from flask_mysqldb import MySQL
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp
from config import Config

mysql = MySQL()  # instancia global

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configurar MySQL
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_DB'] = 'tourism'
    app.config['MYSQL_PORT'] = 3306

    mysql.init_app(app)

    app.secret_key = Config.SECRET_KEY

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    return app
