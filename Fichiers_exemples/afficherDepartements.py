#!/usr/bin/python

import sqlite3

print("Content-type: text/html; charset=iso-8859-1\n")


# création d'une page web, incluant un tableau
print('''
<html>
    <head>
        <title>Liste Departement</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>

    <body>

        <h1 style='text-align:center'>Liste des departements</h1>

        <table border='1'
        <tr><th colspan='3'>Departements</th></tr>
        <tr><th>Numero</th><th>Nom</th><th>Region</th></tr>
''')

connexion = sqlite3.connect('collectivites1.db')

# lancement d'une requete sql
curseur = connexion.execute('''SELECT numero, nom, nomRegion
                               FROM Departement JOIN Region USING (idRegion)
                               ORDER BY numero''')

# recuperation des elements de reponse de la requete, en utilisant une liste
for tuple in curseur:
    ligne = list(tuple)
    print("<tr><td>", ligne[0], "</td>",
          "<td>", ligne[1], "</td>",
          "<td>", ligne[2], "</td></tr>")

connexion.close()

# fin de la page web
print('''
        </table>
        <hr/>
        <a href='index.py'>Retour au menu</a>
    </body>
</html>''')
