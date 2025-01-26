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
    # Connexion à la base de données
    conn = get_db_connection(DATABASE)
    #permet d'exécuter les requêtes sql
    curseur = conn.cursor()
    # Récupérer les données
    data = curseur.execute('SELECT * FROM infos_joueur').fetchall()
    # Fermer la connexion
    conn.close()
    # Passer les données à la page HTML si besoin
    return render_template('index.html', data = data)

@app.route('/Contacts')
def Contacts():
    return render_template('Contacts.html')

@app.route('/Connexion')
def Connexion():
    return render_template('Connexion.html')

@app.route('/recherche')
def recherche():
    return render_template('recherche.html')


@app.route('/profil', methods=['POST', 'GET'])
def profil():
    username = request.cookies.get('username')
    conn = get_db_connection(DATABASE)  # Connexion à la base de données
    curseur = conn.cursor()
    datas = curseur.execute("SELECT * FROM infos_joueur WHERE name_id = ? ", (username,)).fetchall()
    datas = [dict(row) for row in datas]

    if request.method == 'POST':
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
        datas = curseur.execute("SELECT * FROM infos_joueur WHERE name_id = ? ", (username,)).fetchall()
        datas = [dict(row) for row in datas]
        conn.close()
        return render_template('profil.html', username = username, datas = datas)


    conn.close()  # Fermer la connexion
    return render_template('profil.html', username = username, datas = datas)


@app.route('/profil_user_/<username>', methods=['POST','GET'])
def profil_user_(username):
    conn = get_db_connection(DATABASE)  # Connexion à la base de données
    curseur = conn.cursor()
    datas = curseur.execute("SELECT * FROM infos_joueur WHERE name_id = ? ", (username,)).fetchall()
    datas = [dict(row) for row in datas]
    conn.close()

    if request.method=='POST':
        return redirect(url_for('recherche'))

    return render_template('profil_user_.html', username = username, datas = datas)

@app.route('/resultats', methods=['POST', 'GET'])
def resultats():
    username = request.form.get('username')
    sexe = request.form.get('sexe')
    age = request.form.get('age')
    jeu = request.form.get('jeu')
    temps = request.form.get('temps')
    addiction = request.form.get('addiction')
    douches = request.form.get('douches')
    exs = request.form.get('exs')
    soda = request.form.get('soda')
    bonbon = request.form.get('bonbon')
    selfcontrol = request.form.get('selfcontrol')
    discord = request.form.get('discord')
    sommeil = request.form.get('sommeil')

    conn = get_db_connection(DATABASE)
    curseur = conn.cursor()

    # Construire la requête dynamiquement
    conditions = []
    params = []

    if sexe:
        conditions.append("sexe = ?")
        params.append(sexe)
    if age:
        try:
            age = int(age)
            conditions.append("age = ?")
            params.append(age)
        except ValueError:
            pass  # Ignorer si non valide
    if jeu:
        conditions.append("fav_game = ?")
        params.append(jeu)
    if temps:
        conditions.append("screen_time_moy = ?")
        params.append(temps)
    if addiction:
        conditions.append("addiction = ?")
        params.append(addiction)
    if douches:
        conditions.append("nb_douches = ?")
        params.append(douches)
    if exs:
        conditions.append("nb_ex = ?")
        params.append(exs)
    if soda:
        conditions.append("fav_soda = ?")
        params.append(soda)
    if bonbon:
        conditions.append("fav_bonbons = ?")
        params.append(bonbon)
    if selfcontrol:
        conditions.append("pourcent_selfcontrol = ?")
        params.append(selfcontrol)
    if discord:
        conditions.append("discord = ?")
        params.append(discord)
    if sommeil:
        conditions.append("heure_sommeil = ?")
        params.append(sommeil)
    if username:
        conditions.append("name_id = ?")
        params.append(username)

    query = "SELECT name_id FROM infos_joueur"
    if conditions:
        query += " WHERE " + " OR ".join(conditions)

    # Debugging
    print("Requête SQL :", query)
    print("Paramètres :", params)

    curseur.execute(query, params)
    data = [row[0] for row in curseur.fetchall()]

    conn.commit()
    conn.close()

    return render_template('resultats.html', data=data)


@app.route('/inscription', methods=['POST'])
def inscription():
    error = None
    # Récupérer les données du formulaire
    username = request.form.get('username')
    sexe = request.form.get('sexe')
    age = request.form.get('age')
    jeu = request.form.get('jeu')
    temps = request.form.get('temps')
    addiction = request.form.get('addiction')
    douches = request.form.get('douches')
    exs = request.form.get('exs')
    soda = request.form.get('soda')
    bonbon = request.form.get('bonbon', )
    selfcontrol = request.form.get('selfcontrol')
    discord = request.form.get('discord')
    sommeil = request.form.get('sommeil')
    
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
