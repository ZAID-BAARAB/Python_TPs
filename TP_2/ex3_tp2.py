import random

correct_number= random.randint(1,100) 
# print (correct_number)
for i in range (0,7):
    print(" essai N:" , i)
    nombre=input(" donner nombre entre 1 est 100")
    nombre=int(input(" donner un nombre entre 1 est 100"))
    if(nombre==correct_number):
        print(" coungrats, you WON 1000$, winning number is :"+nombre) 
        break  
    elif(nombre < correct_number):
        print("votre nombre est plus petit")
    else:
        print("votre nombre est plus grand")    
print("OOPS , votre essai est epuizee") 
