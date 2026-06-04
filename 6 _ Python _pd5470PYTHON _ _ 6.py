sekwencja_1 = "ATCTGTC"
sekwencja_2 = "AGTCTAT"
sekwencje_połączone = sekwencja_1 + sekwencja_2
print(sekwencje_połączone)
sekwencja_rodzielona = sekwencje_połączone.rsplit("GT")
print(sekwencja_rodzielona)
Ilość_adeniny = sekwencje_połączone.count("A")
print(Ilość_adeniny)
pozycja_CTA = sekwencje_połączone.find("CTA")
print(f"Kodon 'CTA' znajduje się na pozycji:",{pozycja_CTA})
print(f"W połączonych sekwencjach DNA, występuje ilość adeniny równa: \n\t{Ilość_adeniny}")