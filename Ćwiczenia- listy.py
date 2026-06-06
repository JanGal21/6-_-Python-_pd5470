sekwencja_DNA = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G', 'C', 'T']
print(sekwencja_DNA[0]) #znalezienie pierwszej wartości "indeksu" w liście
print(sekwencja_DNA[-1]) #znalezienie ostatniej wartości "indeksu" w liście
if "A" in sekwencja_DNA:
    print("\t\'Adenina jest obecna\'")
sekwencja_DNA[3:5] = ['A','G','C'] # Zamiana wartości na liście: zauważ przecinki i kwadratowe nawiasy
print(sekwencja_DNA)
sekwencja_DNA.insert(3,'G') # W pozycji trzeciej, dodanie nowego indeksu
print(sekwencja_DNA)
# dodanie nowych nukleotydów na koniec listy:
Nowe_nukleotydy = ['A','T','G']
sekwencja_DNA.extend(Nowe_nukleotydy)
print(sekwencja_DNA)
for nukleotyd in sekwencja_DNA:
    print(nukleotyd)
for i in range(len(sekwencja_DNA)):
    print(sekwencja_DNA[i])
Długość_sekwencji = len(sekwencja_DNA)
print(Długość_sekwencji)
#List comprehension - tworzenie nowej listy na podstawie danych z innej
pirymidyny = [nukleotyd for nukleotyd in sekwencja_DNA if nukleotyd in ['C','T']]
print(pirymidyny)






