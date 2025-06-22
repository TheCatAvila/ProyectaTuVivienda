from flask import Blueprint, session, redirect, render_template, request
from app.models.user import User

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return render_template("index.html")

    return render_template('index.html', user_login_data=user_login_data)

