#Dorian Kwizera 2022-
#Différents Import utiles
import random
import datetime

# Charger le fichier CSV
with open("tableau_projet.csv", "r") as mon_flux:
    tableau = mon_flux.readlines()

# Transformer les lignes en listes et convertir les prix en float
for compteur in range(0, len(tableau)):
    tableau[compteur] = tableau[compteur].strip().split(';')

for compteur in range(1, len(tableau)):
    tableau[compteur][1] = float(tableau[compteur][1])

# Obtenir la date du jour
date = datetime.date.today()

# Générer un numéro de commande aléatoire
numero_commande = random.randint(1044, 9999)

# Fonction pour obtenir une entrée valide
def obtenir_nombre_valide():
    while True:
        try:
            valeur = int(input())  # Tente de convertir l'entrée en entier
            if valeur < 0:  # Vérifie si l'entrée est négative
                print("Veuillez entrer un nombre entier positif ou égal à zéro.")
            else:
                return valeur  # Retourne la valeur si elle est valide
        except ValueError:  # Gère les cas où l'entrée n'est pas un nombre
            print("Entrée invalide. Veuillez entrer un nombre entier positif ou égal à zéro.")

# Programme principal
total = 0
ticket = ""
print("\nSélectionnez le nombre d'aliments que vous désirez dans le menu")

for compteur in range(1, len(tableau)):
    ptit_total = 0
    print(f"\nCombien de {tableau[compteur][0]} voulez-vous ?")
    nombre = obtenir_nombre_valide()  # Redemande tant que l'entrée n'est pas valide

    # Calculer le sous-total uniquement si le nombre est valide
    if nombre > 0:
        ptit_total = nombre * tableau[compteur][1]
        ticket += f"{ptit_total:.2f}€     {nombre}x {tableau[compteur][0]}\n"
        total += ptit_total

# Afficher le ticket
print("\n", date)
print(f"Ticket Commande n° {numero_commande}\n{ticket}")
print(f"TOTAL    {total:.2f}€")

