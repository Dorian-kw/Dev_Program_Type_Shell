#Dorian Kwizera 2022-
#Différents Import utiles
import random
import datetime
import argparse
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def charger_tableau(csv_file):
    """Charge et transforme le tableau depuis un fichier CSV."""
    with open(csv_file, "r") as mon_flux:
        tableau = mon_flux.readlines()

    for compteur in range(0, len(tableau)):
        tableau[compteur] = tableau[compteur].strip().split(';')

    for compteur in range(1, len(tableau)):
        tableau[compteur][1] = float(tableau[compteur][1])

    return tableau

def obtenir_nombre_valide():
    """Demande à l'utilisateur un entier positif ou zéro."""
    while True:
        try:
            valeur = int(input())  # Tente de convertir l'entrée en entier
            if valeur < 0:
                print("Veuillez entrer un nombre entier positif ou égal à zéro.")
            else:
                return valeur
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier positif ou égal à zéro.")

def calculer_total_et_ticket(tableau):
    """Calcule le total et génère un ticket basé sur les choix de l'utilisateur."""
    total = 0
    ticket = ""

    print("\nSélectionnez le nombre d'aliments que vous désirez dans le menu")

    for compteur in range(1, len(tableau)):
        print(f"\nCombien de {tableau[compteur][0]} voulez-vous ?")
        nombre = obtenir_nombre_valide()

        if nombre > 0:
            ptit_total = nombre * tableau[compteur][1]
            ticket += f"{ptit_total:.2f}€     {nombre}x {tableau[compteur][0]}\n"
            total += ptit_total

    return total, ticket

def afficher_ticket(total, ticket):
    """Affiche le ticket de commande."""
    date = datetime.date.today()
    numero_commande = random.randint(1044, 9999)

    print("\n", date)
    print(f"Ticket Commande n° {numero_commande}\n{ticket}")
    print(f"TOTAL    {total:.2f}€")

def main():
    parser = argparse.ArgumentParser(description="Programme de commande interactif en ligne de commande.")
    parser.add_argument("csv_file", type=str, help="Chemin vers le fichier CSV contenant le menu.")
    args = parser.parse_args()

    try:
        tableau = charger_tableau(args.csv_file)
        total, ticket = calculer_total_et_ticket(tableau)
        afficher_ticket(total, ticket)
    except FileNotFoundError:
        logging.error("Le fichier spécifié est introuvable. Veuillez vérifier le chemin et réessayer.")
    except Exception as e:
        logging.error(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    main()
