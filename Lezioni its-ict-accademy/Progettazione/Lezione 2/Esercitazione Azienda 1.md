


Obiettivi
Si vuole sviluppare un sistema informativo per la gestione dei
dati sul personale di una certa azienda costituita da diversi
dipartimenti.
Durante la fase di raccolta dei requisiti è stata prodotta la
specifica dei requisiti mostrata di seguito.
Si chiede di iniziare la fase di Analisi Concettuale ed in
particolare di:
1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze e produrre un elenco numerato di requisiti il meno ambiguo possibile
2. produrre un diagramma UML delle classi concettuale che modelli i dati di interesse, utilizzando solo i costrutti di classe, associazione, attributo
3. produrre le relative specifiche delle classi.
Specifica dei requisiti
I dati di interesse per il sistema sono impiegati, dipartimenti, direttori dei dipartimenti e progetti aziendali.
Di ogni impiegato interessa conoscere il nome, il cognome, la data di nascita e lo stipendio attuale, il dipartimento(esattamente uno) al quale afferisce.
Di ogni dipartimento interessa conoscere il nome, il numero di telefono del centralino, e la data di afferenza di ognuno degli impiegati che vi lavorano.
Di ogni dipartimento interessa conoscere inoltre il direttore, che
è uno degli impiegati dell'azienda.
Il sistema deve permettere di rappresentare i progetti aziendali nei quali sono coinvolti i diversi impiegati. Di ogni progetto interessa il nome ed il budget. Ogni impiegato può partecipare ad un numero qualsiasi di progetti.


Analisi (raccolta) dei requisiti: 
1. Requisiti sugli impiegati
	1. 1 nome
	2. 2. cognome 
	1.3 data di nascita
	1.4 stipendio (un reale maggiore o uguale a zero)
	1.5 Il dipartimento di afferenza (notare che c'è scritto solo un dipartimento quindi da riportare esattamente uno, vedi req.2)
	1.6 data di afferenza
2. Requisiti sui dipartimenti:
	   2.1 nome
	   2.2 telefono (una stringa)
	   2.3 la data di afferenza degli impiegati che ci lavorano (chi ci lavora e la data in cui ha iniziato a lavorare in quel dipartimento), gli impiegati che vi afferiscono(da d'ora in poi usare questo termine)
		   2.3.1 per ognuno la data di afferenza
	   2.4 il direttore ( è un impiegato, vedi req.1)
3. Requisiti sui progetti:
	   3.1 nome
	  3.2 budget