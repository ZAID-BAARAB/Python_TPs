grade = input("Entrez le grade de l'employé (A, B, C, D, ou E) : ").upper()
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))

grades = {'A': {'tarif_horaire': 200, 'prime': 1000, 'heures_par_prime': 20},
          'B': {'tarif_horaire': 150, 'prime': 800, 'heures_par_prime': 20},
          'C': {'tarif_horaire': 120, 'prime': 500, 'heures_par_prime': 15},
          'D': {'tarif_horaire': 100, 'prime': 350, 'heures_par_prime': 15},
          'E': {'tarif_horaire': 80, 'prime': 100, 'heures_par_prime': 10}}

# Vérifier si le grade est valide
if grade not in grades:
    print("Grade invalide. Les grades valides sont : A, B, C, D, E")
else:
    # Calcul du salaire
    tarif_horaire = grades[grade]['tarif_horaire']
    prime = grades[grade]['prime']
    heures_par_prime = grades[grade]['heures_par_prime']

    salaire = (tarif_horaire * heures_travaillees) + (prime * (heures_travaillees // heures_par_prime))
    print(f"Le salaire de l'employé est de {salaire} DH.")