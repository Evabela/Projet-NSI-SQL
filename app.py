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

@app.route('/Contacts')
def Contacts():
    return render_template('Contacts.html')

@app.route('/recherche')
def recherche():
    return render_template('recherche.html')


@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/resultats')
def resultats():
    return render_template('resultats.html')

@app.route('/inscription', methods=['POST'])
def inscription():
    # Récupérer les données du formulaire
    username = request.form.get('name_id', None)  # Récupérer le champ "name_id"
    sexe = request.form.get('sexe', None)
    age = request.form.get('age', None)
    
    # Insérer les données dans la base de données
    conn = get_db_connection(DATABASE)
    curseur = conn.cursor()
    curseur.execute(
        'INSERT INTO infos_joueur (name_id, sexe, age) VALUES (?,?,?)',
        (username,sexe, age)
    )
    conn.commit()
    conn.close()

    # Redirection vers la page d'accueil après l'inscription
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug = True)
