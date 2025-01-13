#!/usr/bin/python

import sqlite3
import cgi

formulaire = cgi.FieldStorage()

# Récupération des valeurs du formulaire
nouveau_nom = formulaire.getvalue("nomDep")
nouveau_numero = formulaire.getvalue("numeroDep")
id_region = formulaire.getvalue("idRegion")


connexion = sqlite3.connect('collectivites1.db')

#Pour générer une nouvel identifiant, on récupère l'identifiant max existant...
curseurId = connexion.execute('SELECT max(idDepartement) FROM Departement')
tupleId = curseurId.__next__()
idMax = int(tupleId[0])
#... et on rajoute 1
nouvel_id = idMax + 1

connexion.execute('''INSERT INTO Departement(idDepartement, nom, numero, idRegion)
                     VALUES (?, ?, ?, ?)''',
                     (nouvel_id, nouveau_nom, nouveau_numero, id_region))
connexion.commit()
connexion.close()

import afficherDepartements
