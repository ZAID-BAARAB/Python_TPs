def euro_to_mad(euro):
    return euro * 10.86

def mad_to_euro(mad):
    return mad * 0.092

direction = input("Choisissez la direction de la conversion (euro en mad ou mad en euro) : ").lower()

if direction == "euro en mad":
    values = []
    euro_value = float(input("Entrez une valeur en euro (saisissez un nombre négatif pour arrêter) : "))
    while euro_value >= 0:
        mad_value = euro_to_mad(euro_value)
        values.append((euro_value, mad_value))
        euro_value = float(input("Entrez une autre valeur en euro (saisissez un nombre négatif pour arrêter) : "))
    
    print("Valeurs converties en dirhams (MAD) :")
    for euro, mad in values:
        print(f"{euro} EUR = {mad} MAD")

elif direction == "mad en euro":
    values = []
    mad_value = float(input("Entrez une valeur en dirham (MAD) (saisissez un nombre négatif pour arrêter) : "))
    while mad_value >= 0:
        euro_value = mad_to_euro(mad_value)
        values.append((mad_value, euro_value))
        mad_value = float(input("Entrez une autre valeur en dirham (MAD) (saisissez un nombre négatif pour arrêter) : "))
    
    print("Valeurs converties en euros (EUR) :")
    for mad, euro in values:
        print(f"{mad} MAD = {euro} EUR")

else:
    print("Direction de conversion non valide. Veuillez choisir 'euro en mad' ou 'mad en euro'.")
