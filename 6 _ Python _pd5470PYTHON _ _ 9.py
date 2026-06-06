geny = {
    "BRCA1" : "gen supresorowy nowotworów",
    "MC1R" : "produkcja melaniny",
    "FOXP2" : "rozwój mowy i języka"
}
kodony = {"ACT", "CGA","TAC"}
geny["TP53"] = "regulacja cyklu komórkowego"
print(geny)
kodony.add("TGA")
print(kodony)
if "ACT" in kodony:
    print("W sekwnecji obecny jest kodon 'ACT'")
if "BRCA1" in geny:
    print("Gen 'BRCA1 jest obecny")
kodony.remove("TAC")
print(kodony)
for x,y in geny.items():
    print(x,y)
Długość = len(kodony)
if Długość > 3:
    print("W zbiorze występują ponad 3 kodony")
else:
    print("W zbiorze jest mniej niż 3 kodony")
if "MC1R" in geny:
    print(geny["MC1R"])
kodony_2 = {"TP53", "FOXP2", "recA"}
zespolone = kodony.union(kodony_2)
print(zespolone)



