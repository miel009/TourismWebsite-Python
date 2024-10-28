# app/blueprints/auth/routes.py

from flask import Blueprint, render_template


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
# auth_bp es como usabamos app

@auth_bp.route('/login')
def login():
    #aca podriamsousar un jsonBin y comosiempre... 
    return render_template('auth/login.html')

@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')