#!/usr/bin/python
print("Content-type: text/html; charset=iso-8859-1\n")
print('''
<html>
    <head>
        <title>Collectivites</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>

    <body>

        <h1 style='text-align:center'>Collectivites</h1>

        <ol>
            <li><a href='ajouterDepartement.py'>Ajouter un departement</a></li>
            <li><a href='afficherDepartements.py'>Afficher la liste des departements</a></li>
        </ol>
    </body>
</html>''')
