#Dorian Kwizera 2022-
#Différents Import utiles
import random
import datetime

#Usage d'information d'un fichier csv
mon_flux = open("tableau_projet.csv","r")

tableau =mon_flux.readlines()

mon_flux.close()

for compteur in range(0,len(tableau)):
    tableau[compteur] = tableau[compteur].split(';')

for compteur in range(1,len(tableau)):
    tableau[compteur][1] = float(tableau[compteur][1])

#Avoir la date du ticket datetime(year, month, day, hour, minute, second, microsecond)
date = datetime.date.today()

#Avoir un nombre élévé au hasard comme numéro de commande
numero_commande = random. randint(1044, 9999)

#Programme principal
total = 0
ticket = ""
print("\nSéléctionner le nombre d'aliment que vous désirez dans le menu")
for compteur in range(1,len(tableau)):
    ptit_total = 0
    print("\nCombien de",tableau[compteur][0],"voulez vous ?")
    try :
        nombre = int(input())
    except ValueError :
        print("Vous n'avez pas entré de nombre entier, donc pas de",tableau[compteur][0],"pour vous.\n")
    else:
        total = total + nombre * tableau[compteur][1]
        ptit_total = nombre * tableau[compteur][1]
        print(" ")
        print("nombre de",tableau[compteur][0],":", nombre)
        print(" ")
        if nombre>0:
            ticket = ticket +str(ptit_total) +"€     "+str(nombre) +"x " + tableau[compteur][0] +"\n"

print(date)
print("Ticket Commande n°",numero_commande,"\n"+ticket)
print("TOTAL   ",total,"€")


