from flask import Flask
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp

# y en vez de usar IF... esta seccion o archivo es paracorrer el programa y le digo 
#que use el auth y dashboard
#blueprints para org mis carpetas, utilizando rutas etc  
#para usar  auth y dashboard_dp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'vacac'
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
