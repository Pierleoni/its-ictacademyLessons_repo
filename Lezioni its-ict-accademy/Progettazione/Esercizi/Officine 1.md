## Raffinamento dei requisiti

1. Requisiti sulle officine:
	1.1) nome(Stringa)
	1.2)Indirizzo 
	1.3)dipendenti che vi lavorano (v. req. 2)
		1.3.1) per ognuno la data di presa di servizio(vedi req. 2.2.1)
	1.4)numero di dipendenti che vi lavorano (calcolabile a partire da req. 1.3)
	1.5) direttore (vedi req. [[#^a8bd45|3]])


2. Requisiti sulle persone:
	2.1) nome
	2.2) cognome
	2.3) numero di telefono
	2.4) email
	2.5) indirizzo

3. Requisiti sui dipendenti:
	2.1) sono persone
	2.2) le officine nelle quali lavora(un qualsiasi numero, anche nessuna) (v. req. 1)
		2.2.1) per ognuna, la data di presa di servizio(v. req. 1.3.1) %% Gli anni di servizio si calcolano perché si devono aggiornare  %%
		2.2.2) gli anni di servizio (calcolabiel a partire da req. 2.2.1)

4. Requisiti sui direttori:
	3.1) sono persone(v.req.2)
	3.2) Data di nascita(Data) ^a8bd45
	3.3) officine che dirige (v. req. 1)

5.  Requisiti sulle riparazioni dei veicoli:
	4.0) officine che se ne occupano(almeno una)
	4.1) codice(Stringa univoco)
	4.2) veicolo (vedi req. [[#^244a02|5]])
	4.3) (Istante)Data e ora di accettazione (DataOra)
	4.4) (istante)Data e ora di consegna (opzionale, solo se la riparazione è terminata)(DataOra)
	
6. Requisiti sui veicoli:
	5.1) modello(Stringa)
	5.2) tipo (v. req. 7)
	5.3) targa(Stringa alfanumerica di massimo 8 caratteri secondo lo standard UE).
	5.4)data di immatricolazione
	5.5) I Proprietari (almeno uno), sono persone(vedi req. [[#^48ee07|6]])
 ^244a02

7. Requisiti sui proprietari:
	6.1) nome (Stringa)
	6.2) Codice fiscale(Stringa alfanumerica di 16 caratteri secondo standard)
	6.3) indirizzo 
	6.4) numero di telefono (Stringa numerica di 15 caratteri secondo standard)
 ^48ee07
 
8. Requisiti sui modelli di veicolo:
	7.1) tipo (automobile, motociclo, autocarro, ecc.)
	7.2) nome
	7.3) anno (di presentazione del modello)
	7.4) casa produttrice (vedi req. 8)

9. Requisiti sulle case produttrici:
	8.1) nome(univoco)

10. Requisiti sulle città:
	5.1) nome(Stringa)
11. Requisiti sulle regioni:
	6.1) nome(Stringa)
12. Requisiti sulle nazioni:
	7.1) nome(Stringa)