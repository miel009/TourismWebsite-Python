from flask import Flask
from app.blueprints.auth.routes import auth_bp
from app.blueprints.dashboard.routes import dashboard_bp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'vacac'
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
