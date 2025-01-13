#!/usr/bin/python

import sqlite3

def select_region():
    retour = '<select name="idRegion">'
    connexion = sqlite3.connect('collectivites1.db')
    # lancement d'une requete sql
    curseur = connexion.execute('''SELECT idRegion, nomRegion
                                   FROM Region
                                   ORDER BY nomRegion''')
    # recuperation des elements de reponse de la requete, en utilisant une liste
    for region in curseur:
        option = "<option value='" + str(region[0]) + "'>"
        option += region[1]
        option += "</option>\n"
        retour += option
    retour += "</select>"
    connexion.close()
    return retour

print("Content-type: text/html; charset=iso-8859-1\n")


# Ecriture d'une page Web avec un formulaire
print('''
<html>
    <head>
        <title>Requete</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <h1 style='text-align:center'>Ajouter une region</h1>

        <form method='get' action='insertionDepartement.py'>
            Numero du departement : <input type='text' name='numeroDep'/><br/>
            Nom du departement : <input type='text' name='nomDep'/><br/>
            Region :''')

print(select_region())

print('''
            <br/>
            <input type='submit' value='Ajouter'/>
        </form>


        <hr/>
        <a href='index.py'>Retour au menu</a>

    </body>
</html>''')
