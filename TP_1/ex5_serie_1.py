nmbr=int(input("donner moi un nombre seconds ") )
if((nmbr%2)==0):
    print("nombre est paire")
elif((nmbr%2)==1 and (nmbr%3)==0):
    print(f"Ce nombre est impair, mais est multiple de 3")
else:
    print(f"Ce nombre n’est ni pair ni multiple de 3")