List=[1,3,5,8,9,10,11,12,13,14,15,16,17]
nombre=input(" donner nombre")
for i in range(0, len(List)):
    if(nombre<List[i]):
        List.insert(nombre, i)
    4
print(List)