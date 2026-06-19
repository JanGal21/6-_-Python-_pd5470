def charakterystyka_białka(sekwencja,masa,punkt_izoelektryczny):
    return f"Białko o sekwencji {sekwencja} i masie {masa} Da oraz pI równym: {punkt_izoelektryczny}"
x = charakterystyka_białka(sekwencja="MKVBS",masa=14,punkt_izoelektryczny= 5.2)
print(x)
def sumuj_cechy_białek(**kwargs):
    masy = []
    for x in kwargs.values():
        masy.append(x['masa'])
    suma_mas = sum(masy)
    pI = []
    for y in kwargs.values():
        pI.append(y['pI'])
    średnia_pI = sum(pI) / len(pI)
    print(f"Suma mas białek wynosi: {suma_mas}, a średnia pI: {średnia_pI}")
sumuj_cechy_białek(
      insulina={'masa': 9877, 'pI': 1.2},
      albumina={'masa': 6877, 'pI': 3.2},
      hemoglobina={'masa': 1234, 'pI': 8.1}
  )
