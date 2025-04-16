# Analisi dei requisiti 
1. Requisiti sui giocatori:
	   1.1 nickname (stringa univoca)
	   1.2 nome
	   1.3 cognome
	   1.4 indirizzo (tipo di dato record):
		   1.4.1 via (Stringa)
		   1.4.2 numero civico (Stringa numerica)
		   
     1.5 rank dichiarato (intero positivo)
     1.6) partite giocate(vedi [[#^partite|req.3]])
 n
2. Requisiti sui tornei:
	2.1 nome (Stringa)
	2.2 descrizione testuale(Stringa)
	2.3 edizione in termini dell'anno (Intero > 2024)
	^tornei

3. Requisiti sulle partite:
	3.1)data di svolgimento(vedi [[#^tornei|req.2]])
	3.2)luogo di svolgimento(vedi [[#^svolgimento|req.4]])
		
	3.3)regole di conteggio(tipo di dato enumerativo):
		3.3.1) giapponesi
		3.3.2) cinesi
	3.4) giocatori
		3.4.1)il giocatore che gioca con le pietre bianche
		3.4.2)il giocatore che gioca con le pietre nere
	3.5) Il fattore di deficit di komi(Reale >=0, tra 0 e 10)
	3.6) eventualmente, l'esito, uno tra
		3.6.1) partita terminata con rinuncia
			3.6.1.1) il giocatore rinunciattario
		3.6.2) partita terminata con punteggi
			3.6.2.1) punteggio del giocatore bianco(intero>=0)
			3.6.2.2)punteggio del giocatore nero(intero>=0)
		3.7)eventualmente, il torneo al quale si riferisce(vedi [[#^tornei|req.2]])
   ^partite
   
4. Requisiti sui luoghi di svolgimento dei tornei:
	4.1) Città
		4.1.1)nome(stringa)
	4.2) regione
		4.2.1)nome(stringa)
	4.3) nazione
		4.3.1)nome(stringa)
	^svolgimento