temperatures =  [12.5, 14, 9.5, 17, 21, 19.5, 11]
moyenne = sum(temperatures)/len(temperatures)
print("la moyenne est de :", moyenne)
for t in temperatures: 
    if t == 9.5:
        print("la température minimale est à :",t)
    elif t == 21:
        print("la température maximale est à:",t)
for c in temperatures:
    f= c*9 / 5+32 
    print("la température en fahrenheit est de :",f)
    for c in enumerate(temperatures):
        print(f"jour{c[0]}: {c[1]}")





