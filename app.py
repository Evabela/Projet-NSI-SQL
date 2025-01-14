import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = 'Projet_planetegeekdating.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()  # Connexion à la base de données
    data = conn.execute('SELECT * FROM informations').fetchall()  # Récupérer les données
    conn.close()  # Fermer la connexion
    return render_template('index.html', data=data)  # Passer les données à la page HTML



if __name__ == "__main__":
    app.run()