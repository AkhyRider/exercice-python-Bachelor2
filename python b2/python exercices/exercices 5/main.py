import outils
notes_brutes = ["12,5","15","abc","9", "18,25"]
notes_valides=[]
notes_ignorees=[]
for note in notes_brutes:
    note_nettoyee=outils.covertir_note(note)
    if note_nettoyee is None:
        notes_ignorees.append(note)
    else:
        notes_valides.append(note_nettoyee)
        print(f"Notes valides : {notes_valides}")
        print(f"Notes ignorées : {notes_ignorees}")
