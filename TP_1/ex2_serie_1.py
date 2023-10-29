age = input("Quel est votre âge ? ")
taille = input("Quelle est votre taille en mètres ? ")

age = float(age)
taille = float(taille)

message = "Vous avez {} ans et vous mesurez {:.2f} m.".format(age, taille)
print(message)