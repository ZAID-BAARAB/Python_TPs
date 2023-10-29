poids = float(input("Entrez votre poids en kilogrammes : "))
taille = float(input("Entrez votre taille en mètres : "))


imc = poids / (taille ** 2)


interpretation = ""
if imc > 40:
    interpretation = "Obésité morbide ou massive"
elif imc >= 35:
    interpretation = "Obésité sévère"
elif imc >= 30:
    interpretation = "Obésité modérée"
elif imc >= 25:
    interpretation = "Surpoids"
elif imc >= 18.5:
    interpretation = "Corpulence normale"
elif imc >= 16.5:
    interpretation = "Maigreur"
else:
    interpretation = "Famine"


print("Votre IMC est de {:.2f}, ce qui correspond à : {}".format(imc, interpretation))