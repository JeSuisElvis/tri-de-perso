import csv
# Ouverture du fichier CSV et création du dictionnaire
tableau = {}
with open('tour_de_jeu.csv', newline='') as f:
    lire = csv.reader(f)
    for ligne in lire:
        # La première colonne du CSV est le nom du personnage, la deuxième est sa vitesse,
        # et la troisième est son seuil d'apparition
        nom_personnage = ligne[0]
        vitesse = int(ligne[1])
        seuil = int(ligne[2])
        tableau[nom_personnage] = (vitesse, seuil)

nb_iter = 100# Nombre d'apparitions (base 100)
c = 1
s = ""
max_val = max([v[0] for v in tableau.values()])  # Distance d'un tour (vitesse maximale parmi tous les personnages)
while c <= nb_iter:
    for key, value in tableau.items():
        dist = int(c * value[0])
        if dist % max_val <= value[1]:
            s += key  # Nous notons son nom à chaque fois qu'il doit jouer
            if key != list(tableau.keys())[-1]:  # Vérifie si ce n'est pas le dernier personnage
                s += ', '  # Ajoute une virgule sauf pour le dernier personnage
            if value[0] == min([v[0] for v in tableau.values()]):  # Si le personnage actuel est le plus lent
                s += '\n'  # Ajoute un retour à la ligne après chaque tour du personnage le plus lent
    c += 1

print(s)