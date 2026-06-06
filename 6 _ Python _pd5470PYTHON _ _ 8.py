sekwencja = ['A','T','G','C','A', 'T', 'G', 'A']
zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')
print(sekwencja[0])
print(sekwencja[-1])
print(zasady_azotowe[0])
print(zasady_azotowe[-1])
sekwencja[3:5] = ["T","G","C"]
print(sekwencja)
sekwencja.append('T')
print(sekwencja)
for nukleotyd in sekwencja:
    print(nukleotyd)
for zasada in zasady_azotowe:
    print(zasada)
Nazwy_i_symbole_zasad = sekwencja + list(zasady_azotowe)
print(Nazwy_i_symbole_zasad)