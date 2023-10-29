L = [1, 3, 5, 7, 9]

# Valeur à insérer
val = 6

# Trouver l'emplacement d'insertion
index = 0
while index < len(L) and L[index] < val:
    index += 1

# Insérer la valeur dans la liste
L.insert(index, val)

# Afficher la liste mise à jour
print(L)