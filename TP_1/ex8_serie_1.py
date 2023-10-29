total_notes = 0
total_coefficients = 0


for i in range(4):
    note = float(input(f"Note {i+1} : "))
    coefficient = int(input(f"Coefficient : "))
    
    total_notes += note * coefficient
    total_coefficients += coefficient


moyenne = total_notes / total_coefficients

print(f"Moyenne de ces 4 notes : {moyenne:.2f}", end=", ")


if moyenne >= 10:
    print("semestre validé")
elif 10 > moyenne >= 7:
    print("rattrapage")
else:
    print("non validé")