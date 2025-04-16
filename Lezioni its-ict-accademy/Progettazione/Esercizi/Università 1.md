# Obiettivi
Si vuole sviluppare un sistema informativo per la gestione di
dati relativi ad una università. Durante la fase di raccolta dei
requisiti è stata prodotta la seguente specifica dei requisiti.
Si chiede di iniziare la fase di Analisi Concettuale ed in
particolare di
1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze e produrre un elenco numerato di
requisiti il meno ambiguo possibile
2. produrre un diagramma UML delle classi concettuale che modelli i dati di interesse, utilizzando solo i costrutti di
classe, associazione, attributo
3. produrre le relative specifiche delle classi.


## Analisi dei requisiti
1. Requisiti sugli studenti:
	1.1) nome 
	1.2) codice fiscale
	1.3) numero di matricola
	1.4) data di nascita
	1.5) luogo di nascita (città e regione)
		1.5-1) città
			1.5-1.1) nome
		1.5-2) regione
			1.5.2-1) nome
	1.6) facoltà di afferenza(vedi [[#^345c0f|req. 3]])
	1.7) corsi superati(vedi [[#^02ac69|req.4]])
	1.8) anno di iscrizione

2. Requisiti sui Professori:
	2.1) nome 
	2.2) data di nascita
	2.3) corso insegnato(vedi req.4)

3. Requisiti sulla facoltà:
	3.1) nome
	3.2) tipo
		3.2-1) scientifica 
		3.2-2) letteraria 
		3.2-3) Medica
		3.2-4) Sociale
		3.2-5) Economica
		 ^345c0f

4. Requisiti sui corsi:
	4.1) nome
	4.2) numero di ore 
	4.3) facoltà di appartenenza    
	^02ac69

