class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
    def opisz(self):
        return f"Nazwa tego organizmu to: {self.nazwa}, pochodzący od: {self.rodzaj}"
    @staticmethod
    def transkrybcja(kod):
        return kod.replace("T","U")
class Bakteria(Organizm):
    def __init__(self,nazwa,rodzaj,kształt):
        super().__init__(nazwa,rodzaj)
        self.kształt = kształt
    def opisz(self):
        return super().opisz(), f"jest to bakteria, mająca kształt {self.kształt} "
Eserichia_Coli = Bakteria("Escherichia coli", "Gram -", "pałeczkowaty")
print(Eserichia_Coli.opisz())
Klebsiella_pneumoniae = Bakteria("Klebsiella pneumoniae", "Gram - ", "pałeczkowaty")
print(Klebsiella_pneumoniae.opisz())
print(Organizm.transkrybcja("AUTCGTCA"))



