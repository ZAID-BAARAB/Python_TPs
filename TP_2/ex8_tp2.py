
input_list = input("Entrez une liste d'entiers séparés par des espaces : ")
user_list = [int(x) for x in input_list.split()]

# Demandez à l'utilisateur de saisir le nombre à rechercher
target_number = int(input("Entrez le nombre à rechercher : "))

occurrence_indices = []

# Parcourez la liste pour rechercher le nombre et ses indices
for index, number in enumerate(user_list):
    if number == target_number:
        occurrence_indices.append(index)

if len(occurrence_indices) == 0:
    print("Le nombre", target_number, "n'a pas été trouvé dans la liste.")
else:
    print("Le nombre", target_number, "a été trouvé", len(occurrence_indices), "fois aux indices suivants:", occurrence_indices)