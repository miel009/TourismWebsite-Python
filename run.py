from app import create_app
from flask_mysqldb import MySQL

from config import Config

mysql = MySQL()
app = create_app()

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "tourism"
app.config["MYSQL_PORT"] = 3306

mysql = MySQL(app)

app.secret_key = 'c8f22ab97b234c8fb58d69a3f4e88c2d'  # Usa la clave generada
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)
