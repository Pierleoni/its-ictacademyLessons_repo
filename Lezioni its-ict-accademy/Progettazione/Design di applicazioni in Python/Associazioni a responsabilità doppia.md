Abbimo visto come fare le assoc a responsabilità singola su "Voli Aerei 1":
Abbiamo creato la classe che coincide con l'associazione.
Ora prendendo il design di Azienda 1 dobbiamo implementare l'assoc. "coinvolto" tra la classe "Progetto" e la classe "Impiegato".
Prima di implementare dobbiamo pensare: come si aggiungono gli impiegati a un progetto?
Abbiamo 3 opzioni:
1. `alice.add_progetto(progetto)`
2. `progetto.add_impiegato(alice)`
3. `coinvolto.add(alice,progetto)`
Dobbiamo scegliere se:
a) implementare la prima opzione
b) implementare la seconda opzione 
c) implementare sia la prima che la seconda opzione
d) implementare la terza opzione 