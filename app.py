import sqlite3
from flask import Flask, render_template, request, redirect, url_for, make_response

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

@app.route('/Connexion')
def Connexion():
    return render_template('Connexion.html')


@app.route('/recherche')
def recherche():
    return render_template('recherche.html')

@app.route('/exampleflask', methods=['POST', 'GET'])
def exampleflask():
    username = request.form.get('nm', None)  # Récupérer le champ "username"
    sexe = request.form.get('gdr', None)
    age = request.form.get('age', None)
    conn = get_db_connection(DATABASE)  # Connexion à la base de données
    curseur = conn.cursor()
    curseur.execute("UPDATE infos_joueur SET sexe = ?, age = ? WHERE name_id= ? ", (sexe, age, username,))
    conn.commit()
    conn.close()

    return render_template('exampleflask.html')



@app.route('/profil')
def profil():
    username = request.cookies.get('username')
    conn = get_db_connection(DATABASE)  # Connexion à la base de données
    curseur = conn.cursor()
    datas = curseur.execute("SELECT * FROM infos_joueur WHERE name_id = ? ", (username,)).fetchall()
    datas = [dict(row) for row in datas]


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
    sommeil = request.form.get('sommeil', None)


    curseur.execute("UPDATE infos_joueur SET sexe = ?, age = ?, fav_game= ?, screen_time_moy= ?, heure_sommeil= ?, addiction= ?, nb_douches= ?, nb_ex= ?, fav_soda = ?, fav_bonbons= ?, pourcent_selfcontrol= ?, discord= ? WHERE name_id= ? ",
        (sexe, age, jeu, temps, sommeil, addiction, douches, exs, soda, bonbon, selfcontrol, discord, username,))
    conn.commit()

    conn.close()  # Fermer la connexion
    return render_template('profil.html', username = username, datas = datas)

@app.route('/resultats', methods=['POST', 'GET'])
def resultats():
    username = request.form.get('username', None)  # Récupérer le champ "username"
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
    sommeil = request.form.get('sommeil', None)

    conn = get_db_connection(DATABASE)
    curseur = conn.cursor()
    data = [row[0] for row in curseur.execute("SELECT name_id FROM infos_joueur WHERE sexe = ? AND age = ? AND fav_game = ? AND screen_time_moy = ? AND heure_sommeil = ? AND addiction = ? AND nb_douches = ? AND nb_ex = ? AND fav_soda = ? AND fav_bonbons = ? AND pourcent_selfcontrol = ? AND discord = ? AND name_id = ?",
    (sexe, age, jeu, temps, sommeil, addiction, douches, exs, soda, bonbon, selfcontrol, discord, username)).fetchall()]
    conn.commit()
    conn.close()
    return render_template('resultats.html', data = data)

@app.route('/inscription', methods=['POST'])
def inscription():
    error = None
    # Récupérer les données du formulaire
    username = request.form.get('username', None)  # Récupérer le champ "username"
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
    sommeil = request.form.get('sommeil', None)
    
    conn = get_db_connection(DATABASE)
    curseur = conn.cursor()
            
    nameid = [row[0] for row in curseur.execute('SELECT name_id FROM infos_joueur').fetchall()]

    if username in nameid :
        error = f"Le nom d'utilisateur {username} est déjà utilisé, veuillez en choisir un autre."
        conn.commit()
        conn.close()
        return render_template('index.html', error = error)

    curseur.execute(
        'INSERT INTO infos_joueur (name_id, sexe, age, fav_game, screen_time_moy, heure_sommeil, addiction, nb_douches, nb_ex, fav_soda, fav_bonbons, pourcent_selfcontrol, discord) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (username,sexe, age, jeu, temps, sommeil, addiction, douches, exs, soda, bonbon, selfcontrol, discord)
    )
    conn.commit() #validation des modifications 
    conn.close()

    #on le met à la fin car contient un return
    if request.method == 'POST':
        resp = make_response(render_template('index.html'))
        resp.set_cookie('username', username)
        return resp

    # Redirection vers la page d'accueil après l'inscription
    return redirect(url_for('index'))






if __name__ == "__main__":
    app.run(debug = True)
