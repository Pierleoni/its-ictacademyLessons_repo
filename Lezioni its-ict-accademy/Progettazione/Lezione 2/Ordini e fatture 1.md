1. Requisiti sui dipartimenti aziendali:
	1.1) nome del dipartimento(Stringa)
	1.2) Indirizzo del dipartimento (vedi [[#^8db6f0|req.2]])
	1.3) direttore (classe [[#^direttore|req.3]]).
	^dipartimento
 

2. Requisiti sull'indirizzo:
	2.1) nome della via (Stringa)
	2.2) n. indirizzo civico(intero > 0).
	^8db6f0

3. Requisiti sul direttore:
	3.1)  nome del direttore (Stringa)
	3.2)cognome del direttore (Stringa)
	3.3) codice fiscale (Stringa)
	3.4) data di nascita (Data)
	3.5) luogo di nascita (vedi [[#^citta|req.4]],[[#^regione|5]],[[#^36aa60|6]])
	3.6) anni di servizio in azienda (intero>0)
	^direttore

4. Requisiti sulla città:
	5.1)nome
	^citta

5. Requisiti sulla Regione:
	6.1) nome
	^regione

6. Requisiti sulla Nazione:
	7.1) nome
	^36aa60

7. Requisiti sui fornitori:
	8.1) nome della ditta(Stringa)
	8.2) partita Iva (Stringa = partita iva tramite nota)
	8.3) indirizzo(vedi [[#^8db6f0|req.2]])
	8.4) numero di telefono(Stringa)
	8.5) Indirizzo email(Stringa)
 ^5f21a7
9. Requisiti sugli ordini:
	9.1) nome del dipartimento (vedi [[#^dipartimento|req.1]])
	9.2) data di stipula(attr. della associazione tra ordine e dipartimento) (vedi [[#^dataStipula|req.10]])
	9.3) nome del Fornitore(associazione vedi [[#^5f21a7|req.8]])
	9.4) descrizione dei beni e/o servizi(Stringa)
	9.5) lo stato dell'ordine (Stringa)
		9.5.1) preparazione
		9.5.2) inviato
		9.5.3) da saldare
		9.5.4) saldato
	9.6) aliquota IVA(0< Reale <1)
	

 10. Requisiti sulla data di stipula:
	10.1)data (Data)
	^dataStipula

11. Requisiti sulle fatture:
	11.1) importo imponibile(Reale > 0)
	11.2)data di emissione(Data)
	11.4) dati dell'acquirente(vedi [[#^dipartimento|req.1]])
	11.5) Importo Tot netto (reale > 0)
	