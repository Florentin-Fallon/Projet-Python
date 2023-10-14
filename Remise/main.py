age = int(input("Quel est votre âge ?"))

if(age <= 18):
    print("Remise Ado : -20% de remise")
elif(age > 18):
    print("Remise Adulte : -15% de remise")