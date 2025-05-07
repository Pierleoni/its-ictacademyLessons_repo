Raffinamento dei requisiti

1. Degli utenti interessa:
	1.1 Username (univoco)
	1.2 Istante registrazione (DataOra)
	1.3 I loro bid (v.red 4)
	1.4 I loro acquisti "Compralo subito" (	v.req. 2.6)
	1.5 Se utente privato:
		1.5.1 Può solo fare bid (v. req. 4) oppure acquistare post CompraloSubito (v. req. 2.5)
	1.6 Se venditore professionale:
		1.6.1 URL in vetrina
		1.6.2 I post pubblicati (v. req. 2)
		1.6.3 Popolarità, calcolata che hann effetuato bid sulle loro aste negli ultimi 12 mesi + utenti che hanno acquistato post di tipo "CompraloSubito" negli ultimi 12 mesi. Può essere bassa se <50, media se tra 50 e 300 e alta se > 300.
		1.6.4 L'affidabilità, calcolata come:
			1.6.4.1 sia m = media aritmetica dei feedback ricevuti, sia z = fp/ft (fp = insieme dei poisitivi e ft = insieme dei feedback totali), affidabilità = m(1-z)/5 (quindi sempre tra 0 e 1)

	
2. Dei post interessa:
	2.1 Descrizione
	2.2 Prezzo (reale > 0)
	2.3 Metodo di pagamento (bonifico o carta di credito)
	2.4 Se e un asta:
		2.4.1. Prezzo iniziale (reale >= 0)
		2.4.1. Prezzo rialzo ( reale > 0)
		2.4.3  Istante scadenza (DataOra)
		2.4.4 Il Bid (se ce ne sono, v.req. 4)
		2.4.5. Il prezzo corrente (calcolabile)
		2.4.6 Il vincitore dell'asta (se esiste)

	2.5 Se e "Compralo subito":
		2.5.1 Prezzo (reale  > 0)
		2.5.2 L'acquirente, cioe l'utente che ha acquistato
		per primo (v.req. 1)
	2.6 L'oggetto in vendita(v. req. 3)

	2.7 I feedback, di cui interessa:
		2.7.1 Un voto da 0 e 5
		2.7.2 Un commento (opzionale)


3. Dei oggetti in vendita interessa:
	3.1 La categoria (v. req. 5)
	3.2 Se nuovo:
		3.2.1 Anni di garanzia (minimo 2)
	3.3. Se usato:
		3.2.1 Anni di garanzia (minimo 0)
		3.2.2 Condizioni: ottimo, buono, discreto, da sistemare

4. Dei bid interessa:
	4.1 L'istante (DataOra)
	4.2 L'utente (v.req. 1)

5. Delle categorie ci interessa:
	5.1 Nome
	5.2 Sottocategorie (se esistono)
	5.3 L'insieme delle sottocategorie data una categoria principale 

999. Il sistema deve permettere le seguenti funzionalita:
	999.1. Agli utenti deve permettere di pubblicare post
	per oggetti in vendita con o senza asta.

