distance_km = float(input("Entrez la distance en kilomètres : "))
temps_minutes = float(input("Entrez le temps en minutes : "))

temps_secondes = temps_minutes * 60

vitesse_ms = distance_km * 1000 / temps_secondes
print("La vitesse est de {:.2f} m/s.".format(vitesse_ms))