nmbr1=int(input("donner le premiere nombre ") )
operateur=(input("donner l'operateur ") )
nmbr2=int(input("donner le deuxieme  nombre ") )

if(operateur=="+"):
    result=nmbr1+nmbr2
    print(nmbr1, operateur, nmbr2 ,"=", result)
elif(operateur=="-"):
    result=nmbr1-nmbr2
    print(nmbr1, operateur, nmbr2 ,"=", result)
elif(operateur=="*"):
    result=nmbr1*nmbr2
    print(nmbr1, operateur, nmbr2 ,"=", result)
elif(operateur=="/"):
    if(nmbr2==0):
        print(f"en peut pas deviser sur zero")
    else:
        result=nmbr1/nmbr2
        print(nmbr1, operateur, nmbr2 ,"=", result)
else:
    print(f"cette operateur est invalide2")
        