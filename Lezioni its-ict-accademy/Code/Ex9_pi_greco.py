from fractions import Fraction
soglie:list[float] = [3.14, 3.141, 3.1415, 3.14159]
termini_per_soglie:list[float] = [0] * len(soglie)
numeratore = 4
denominatore = 3
pi_greco_somma = 0.0
cont = 0
while cont <100 :
    termini = 4 - (Fraction(numeratore,denominatore + 2))
    pi_greco_somma += termini
    for i, soglia in enumerate(soglie):
        if termini_per_soglie [i] == 0 and abs(pi_greco_somma - soglia ):
            termini_per_soglie[i] = cont +1 
    cont+=1
for i, soglia in enumerate(soglie):
    print(f" I termini necessari per raggiungere π ≈ {soglia}: {termini_per_soglie[i]}" )
print(f"Valore finale di π: {pi_greco_somma}")