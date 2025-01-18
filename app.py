import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = 'Projet_planetegeekdating.db'

def get_db_connection(DATABASE):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection(DATABASE)  # Connexion à la base de données
    curseur = conn.cursor()
    data = curseur.execute('SELECT * FROM infos_joueur').fetchall()  # Récupérer les données
    conn.close()  # Fermer la connexion
    for elt in data :
        print(dict(elt))
    return render_template('index.html', data = data)  # Passer les données à la page HTML

@app.route('/contact')
def contact():
    return render_template('Contacts.html')



if __name__ == "__main__":
    app.run(debug = True)
