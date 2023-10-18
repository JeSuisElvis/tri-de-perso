# Entrer le nom des perso, leur vitesse, et leur tour de jeu (base 0)
D = {
'A,': (20, 0),
'B,': (30, 0),
'C,': (40, 0),
'D,': (10, 0)
}
nb_iter = 100  # Nombre de passages (base 100 mais ça importe peu)
c = 1
s = ""
max_val = max(D.values())[0]  # Distance d'un tour
while c <= nb_iter:
    for key, value in D.items():
        dist = int(c * value[0])  # La fréquence d'apparition d'un perso est le nombre de tours * sa vitesse
        if dist % max_val <= value[1]:  # Si le perso a effectué plus d'un tour alors (pour le faire apparaitre plus rapidement si il est plus rapide)
            s += key  # Nous notons son nom à chaque fois qu'il dois jouer
        value = (value[0], dist % max_val)  # Nous notons la fréquence d'apparition depuis le début
        D[key] = value  # et nous mettons à jour
    c += 1

print(s)
