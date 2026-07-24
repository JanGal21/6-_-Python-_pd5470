try:
    with open("/Users/jasiugalusek/Downloads/sekwencje.txt", "r") as plik:
        zawartość = plik.read()
        print(zawartość)
except FileNotFoundError:
    print("Taki plik nie istnieje")
def sprawdz_sekwencje_dna(sekwencja):
    dozwolone_nukleotydy = set('ATCG')
    if not set(sekwencja.upper()).issubset(dozwolone_nukleotydy):
        print(f"Błąd: podano nieprawidłową sekwencję: {sekwencja}")
        return False
    print("Sekwencja prawidłowa")
    return True
dopisz_sekwencje = input("Podaj nową sekwencje: ")

if sprawdz_sekwencje_dna(dopisz_sekwencje):
    with open("/Users/jasiugalusek/Downloads/sekwencje.txt", "a") as plik:
        plik.write(dopisz_sekwencje + "\n")
    print("Zapisano sekwencję do pliku.")
else:
    print("Sekwencja nie została zapisana.")









