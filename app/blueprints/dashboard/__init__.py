from flask import Flask
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp

from flask_mysqldb import MySQL



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '$2a$10$kjPH5qzt5aYGcmnK3TYaD.7infnWlLTlBdrV/0Ak5zpOhoOlUQ8eS'
    app.config['JSONBIN_URL'] = 'https://api.jsonbin.io/v3/b/6719dadce41b4d34e447e513'
        
    print("Configuración de la base de datos iniciada...")    
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "Davinci2023"
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_DB"] = "tourism"
    app.config["MYSQL_PORT"] = 3306

    
    #iniciar mysql
    mysql = MySQL(app)
    
   
    dashboard_bp.mysql = mysql  # Pasar la instancia de MySQL al blueprint
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
