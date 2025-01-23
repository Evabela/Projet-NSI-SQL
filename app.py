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
    for elt in data :
        print(dict(elt))
    print("Antoine datas")
    anto = curseur.execute("SELECT * FROM infos_joueur WHERE name_id = 'Antoine'").fetchall()
    anto = [dict(row) for row in anto]
    print(anto[0]["age"])
    conn.close()  # Fermer la connexion
    return render_template('index.html', data = data)  # Passer les données à la page HTML

@app.route('/Contacts')
def Contacts():
    return render_template('Contacts.html')

@app.route('/recherche')
def recherche():
    return render_template('recherche.html')

@app.route('/exampleflask')
def exampleflask():
    name = "Antoine"

    return render_template('exampleflask.html', person = name)


@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/resultats')
def resultats():
    return render_template('resultats.html')

@app.route('/inscription', methods=['POST'])
def inscription():
    # Récupérer les données du formulaire
    username = request.form.get('username', None)  # Récupérer le champ "name_id"
    sexe = request.form.get('sexe', None)
    age = request.form.get('age', None)
    jeu = request.form.get('jeu', None)
    temps = request.form.get('temps', None)
    addiction = request.form.get('addiction', None)
    douches = request.form.get('douches', None)
    exs = request.form.get('exs', None)
    soda = request.form.get('soda', None)
    bonbon = request.form.get('bonbon', None)
    selfcontrol = request.form.get('selfcontrol', None)
    discord = request.form.get('discord', None)
    
    conn = get_db_connection(DATABASE)
    curseur = conn.cursor()
    curseur.execute(
        'INSERT INTO infos_joueur (name_id, sexe, age, fav_game, screen_time_moy, addiction, nb_douches, nb_ex, fav_soda, fav_bonbons, pourcent_selfcontrol, discord) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
        (username,sexe, age, jeu, temps, addiction, douches, exs, soda, bonbon, selfcontrol, discord)
    )
    conn.commit() #validation des modifications 
    conn.close()

    # Redirection vers la page d'accueil après l'inscription
    return redirect(url_for('index'))





if __name__ == "__main__":
    app.run(debug = True)
