                                                        
secondes = int(input("Entrez un nombre de secondes : "))

# Calculer le nombre d'heures, de minutes et de secondes
heures = secondes // 3600  # 1 heure = 3600 secondes
secondes %= 3600

minutes = secondes // 60  # 1 minute = 60 secondes
secondes %= 60

# Afficher le résultat
print("{} secondes = {}h {}min {}sec".format(secondes, heures, minutes, secondes))