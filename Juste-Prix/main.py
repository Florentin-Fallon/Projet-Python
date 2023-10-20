import random
choix = "o"
score = 100
tentatives = 0
prix = random.randint(1, 20)

print("Tentez de devinez le bon nombre compris entre 1 et 20")

while True :
  choix = int(input())
  tentatives += 1
  if choix < prix:
    print("Le nombre est plus haut")
  if choix > prix :
    print("Le nombre est plus bas ")
  if choix == prix :
    print(f"Félicitations vous avez gagner ! Vous avez fais {tentatives} tentatives pour trouver le bon nombre !")
    print("\n")
    choix = input("Voulez vous rejouer ? (o/n)")
    print("\n")
  if choix == "o":
    print("Tentez de devinez le bon nombre compris entre 1 et 20")
  if choix == "n":
    print("Partie Terminée")