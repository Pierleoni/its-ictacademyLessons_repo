
Obiettivo:
• Ristrutturare le specifiche concettuali delle classi e degli use-case in nuove specifiche sul diagramma UML
delle classi ristrutturato.
Metodologia:
• Definire un algoritmo (in forma di pseudo-codice) per ogni operazione di classe o di use-case che verifichi le
sue precondizioni e, se soddisfatte, garantisca il raggiungimento delle sue post-condizioni.

Partiamo da un esempio 
![[Screenshot 2025-07-17 at 18-49-50 Meet - osn-sttm-fkt.png|500x206]]

La specifica concettuale dell'operazione `voto_medio()` della classe `Studente` è:
```plain 
voto_medio(): Reale tra 18 e 30
	pre-condizioni:
		Lo studente this è coinvolto in almeno un link di associazione esame.
	post-condizioni:
		• Sia E l’insieme dei link di associazione esame che coinvolgono lo studente this.
		• Sia S la somma dei valori dell’attributo voto dei link di E
		• result = S / |E| (dove |E| è il numero di elementi di E)
```

La ristrutturazione del diagramma è la seguente:
![[Diagramma ristrutturato op di classe.png]]

DOve la specifica realizzativa della classe `Studente` tramite pseudo-codice:

```plain
voto_medio(): float | None
algoritmo:
se |this.esame| == 0: return None
s = 0
altrimenti:
per ogni l in this.esame:
s = s + l.voto
return s / |this.esame|
```

Vediamo un esempio concreto: 

```plain
ultimo_bid(): Bid [0..1]
precondizione: nessuna
postcondizioni:
	- Non ha side effect
	- Sia B l'insieme dei b:BId coinvolti in un link asta_bid di associazione tra b e this prendo solo i b.istante <=adesso
	- result è il bid nell'insieme B con il valore dell'attributo istante maggiore.


ultimo_bid(): Bid|None
	B = {}
	
	per ogni l in this.asta_bid:
		se l.bid.istante <= datetime.now:
			B.add(b) 
	se |B| ==0 return None
	
	max_b = B[0]
	per b in B: 
		se b.istante >max_b.istante:
			max_b = b
	return max_b
```

In questo caso non serve fare due cicli ma si può fare tutto dentro il primo ciclo:
```
ultimo_bid(): Bid|None
	max_b = this.asta_bid.bid[0]
	per ogni l in this.asta_bid:
		se l.bid.istante >max_b.istante:
			max_b = b 
	return max_b

```

`ultimo_bid` quindi diventa quindi in Python diventa un metodo nella classe `Asta` in Ebuy :

```python
def ultimo_bid(self)->Bid:
	max_b = self._bids[list(self._bids.keys())[0]]
	for l in self._bids.values():
		if l.bid().istante()>max b.istante():
			max_b = l.bid()
	return max_b
```

Ora guardiamo il caso di `vincitore()` che ci ritronta il vincotre dell'asta:
```plain
conclusa():bool
	se this.scadenza <= datetime.now():
		return True
	return False


vincitore(): Privato[0..1]
precondizioni: il res dell'operazione this.conclusa() deve essere True
postcondizioni:
	- Non ha side effect 
	- b = this.ultimo_bid()
	- result è p:Privato coinvolto nel link bid_ut di assoc. con b

vincitore():Privato|None
	se this.conclusa() == False:
		return none
	b = this.ultimo_bid()
	result b.bid_ut.privato


```

In python diventa in asta:
```py
def conclusa(self) -> bool:
	if self.scadenza()<=datetime.now():
		return True
	return False

def vincitore (self) ->UtentePrivato:
	if not self.conclusa():
		raise ValueError("L'asta non è conclusa")
	ultimo_bid = self.ultimo_bid()
	return ultimo_bid.bid_ut_link.utente_privato()
```