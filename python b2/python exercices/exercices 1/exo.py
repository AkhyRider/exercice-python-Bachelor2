Produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.20
prix_ht = prix_ht * quantite
prix_ttc = prix_ht * (1 + taux_tva)
print("Total TTC :", prix_ttc)
print("Total HT :", prix_ht)
