print("\n")

list = ["Florentin", "Jerry", "Mike", "John", "Jack"]


list.remove("Jerry")
list.remove("Mike")
list.remove("John")
list.remove("Jack")
list.append("Grégory")
list.append("César")
list.append("Maxime")
list.append("Geoffrey")
list.append("Mathias")

print(list)

Prénom = input("Quel est votre Prénom ?")

if Prénom == "Florentin":
    print("Bonjour Florentin, Bonne journée !")
elif Prénom == "Grégory":
    print("Bonjour Gregory, Bonne journée !")
elif Prénom == "César":
    print("Bonjour César, Bonne journée !")
elif Prénom == "Maxime":
    print("Bonjour Maxime, Bonne journée !")
elif Prénom == "Geoffrey":
    print("Bonjour Geoffrey, Bonne journée !")
elif Prénom == "Mathias":
    print("Bonjour Mathias, Bonne journée !")
