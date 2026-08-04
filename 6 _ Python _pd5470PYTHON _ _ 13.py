import os
import biologia as b

nazwa_folderu = "dane_bio"
if not os.path.exists(nazwa_folderu):
    os.mkdir(nazwa_folderu)
    print(f"Utworzono folder: {nazwa_folderu}")
else:
    print(f"Folder '{nazwa_folderu}' już istnieje, pomijam.")

sciezka_pliku = os.path.join(nazwa_folderu, "nukleotydy.txt")

with open(sciezka_pliku, "w") as plik:
    ilość_nukleotydów = b.licz_nukleotydy("AGCTTAGCTAAGGCT")
    plik.write(str(ilość_nukleotydów))

with open(sciezka_pliku, "r") as plik:
    print(plik.read())

import datetime
aktualny_czas = datetime.datetime.now()
with open(sciezka_pliku, "a") as plik:
    plik.write(str(aktualny_czas))

print(b.opis_komórki())

