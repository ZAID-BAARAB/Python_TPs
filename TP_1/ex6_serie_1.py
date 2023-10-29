nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
    resultat = "positif"
elif nombre1 == 0 or nombre2 == 0:
    resultat = "nul"
else:
    resultat = "négatif"

print("Le produit de ces deux nombres est", resultat)