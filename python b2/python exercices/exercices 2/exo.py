temperatures = [-3, 0, 15, 31]
for temp in temperatures:
    if temp < 0:
        etat = "gel"
    elif temp == 0:
        etat = "froid"
    elif temp <= 15:
        etat = "doux"
    else:
        etat = "chaud"
    print("État de la température :", etat)

année = [2024, 1900, 2000]
for annee in année:
    if annee < 2000:
        print(annee, "non bissextile")
    elif annee < 1900:
        print(annee, "bissextile.")
    else:
        print(annee, "bissextile.")