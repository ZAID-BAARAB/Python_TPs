nombre_a_supprimer = int(input("Saisissez le nombre à supprimer : "))


ma_liste = [3, 5, 2, 6, 3, 8, 1, 3, 5]

# Supprimer toutes les occurrences du nombre choisi
ma_liste = [x for x in ma_liste if x != nombre_a_supprimer]


print("Liste après suppression :", ma_liste)