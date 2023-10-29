taux_tva = 0.20

total_facture = 0.0

for i in range(1, 3):
    print(f"Article {i}:")
    nom_article = input("Nom de l'article : ")
    prix_ht = float(input("Prix HT de l'article : "))
    quantite = int(input("Quantité : "))

    montant_ht = prix_ht * quantite
    montant_ttc = montant_ht + (montant_ht * taux_tva)

    total_facture += montant_ttc

    print(f"Montant TTC de l'article {nom_article}: {montant_ttc:.2f} €\n")

print(f"Montant total de la facture : {total_facture:.2f} €")