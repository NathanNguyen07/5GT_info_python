from math import sqrt #on importe le module permettant de calculer des racines carrées

print("Bonjour et bienvenue dans ce programme de calcul des racines d'une fonction du deuxième degré.")#on affiche un message de bienvenue
print("Dans l'équation y=ax²+bx+c,")#on précise le contexte et le nom des variables

a=input("Quelle est la valeur de a? ")#on récupère la valeur de a et on la stocke dans la variable a
b=input("Quelle est la valeur de b? ")#même chose pour b
c=input("Quelle est la valeur de c? ")#même chose pour c

a=float(a) #on converti en un nombre décimal
b=float(b) #même chose
c=float(c) #même chose

delta=b**2-4*a*c #on calcul le discriminant

if delta<0:
  print("il n'y a pas de racines")

elif delta==0:
  print("il y a une racine")
  x=-b/(2*a)
  print("la racine est",round(x,3))

elif delta>0:
  print("il y a deux racines")
  x1=(-b-sqrt(delta)/2*a)
  x2=(-b+sqrt(delta)/2*a)
  print("les racines sont",round(x1,3),"et",round(x2,3))

else:
  print("il y a un petit problème")
