def effectif_notes(notes_eval):
    liste_effectifs = [0] * 11
    for x in notes_eval:
        liste_effectifs[x] += 1
    return liste_effectifs

def notes_triees(notes_eval):
    liste_triee = []
    liste_effectifs = effectif_notes(notes_eval)
    for note, eff_note in enumerate(liste_effectifs):
        for _ in range(eff_note):
            liste_triee.append(note)

    return liste_triee

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
print(eff)
print(notes_triees(eff))