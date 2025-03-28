import datetime

nom1= input("Bonjour, quel est ton nom ?")
annee1= input("En quelle année es-tu né ?")
nom2= input("quel est le nom de ton voisin ?")
annee2= input("En quelle année est-elle née ?")

now=datetime.datetime.now()
annee_now=now.year

annee1=int(annee1)
age1=annee_now-annee1
annee2=int(annee2)
age2=annee_now-annee2

print(nom1,"a",age1,"ans")
print(nom2,"a",age2,"ans")

if age1>age2:
   difference=age1-age2
   print(nom1, "est plus agé que",nom2)
   print(nom1,"a",difference,"année de plus que",nom2)
elif age1==age2:
   print(nom1, "et", nom2, "ont le même.")
elif age2>age1:
   difference=age1-age2
   print(nom2, "est plus agé que",nom1)
   print(nom2,"a",difference,"année de plus que",nom1)
else:
   print("une situation innatendue a été rencontrée.")
  
  
