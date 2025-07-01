
SIamo nella fase progettazione: un iterazione dell'analisi concettuale è temrinata, abbiamo lo scchema conc. completo, adesso dobbiamo scelgiere quale tecnologia: mix di linguaggi di prog da usare, tecnologia e strutture per la memo dei dati, archittettura dell'app., algoritmi per realizzare le funzionalità.
In questo modello scelgiamo di scegliere una fase di progettazione della base sati relazionale per consenitre la memo perisistente dei dati di interesse (come definiti nel diagramma delle classi).

Tencincamente se abbiamo deciso di rappr. in modo perisistente possiamo scelgiere un file JSON, ma qual'è il prob di questo approccio? 
Se ho il livello estensionale su tanti file diveris ma se si modificano uno cade tutta la struttura, ma anche quando lavoriamo con file abbiamo problemi concorennti: due processi provano a scrivere/ leggere la stessa risorsa possono generarsi errori andnando ad innefficare tutta la correttezza dell'app.
Per risolvere questi problemi esiste il DSBM: permette ddi gestire una collezzione di dati; prendiamo una scala di ampiezza di dati più grnade che esiste( l'anagrafe di un paese, ecc.) in questo modo possiamo rappresentare tutti i sistmei grandi che possiamo immaginare e offre una serie di funzioanlità senza che l'utente o lo sviluppatore se ne accorga:
accesso grnaulare ai dati (possima gestire un singiolo attr. a cui può accedere l'utente o alcuni dati non possono essere presi da alcuni utenti).
supporto all'esecuzione dei dati controllati, grnaulari e disciplianti
persistenza dei dati memorizzati 
meccanismi sosfisticati per l'interrogazione e manipolazione efficiente dei dati 
metadati(dati che descivono la struttura dei dati memorizzati).
possibilità di memorizzazione distribuita e/o replicata dei dati
enorme semplificazioni del lavoro dei progettisiti e degli sviluppatori (che non devono implementare le funzionalità offerte dal DBMS)
standiridazzione dell'utilizzo (API e linguaggi di interoggazione e manipolazione) dei DMBS, rendendo "semplice" la sostituzione del DBMS usato da un sistema esistente.
In più non tutti i DMBS inn commericio supportanto lo standard, ad esempio il SQL sia standard ci sono comunque delle differenze da sistema e sistema.
Vedremo alcuni casi d'uso di questa cosa ma più avanti

I vari DBSM si disntunguono dal modello dei dati che offorno:
in questo caso parliamo di DB relazionali secondo cui rappr. i dati in maniera relazionale.

![[Modello relazionale dei dati.png]]


Cos'è una tabella nel modello relazionale
Una tabella è rettangolare, latirmenti non è una tabella inoltre nel modello relazionale sono bidimensionale.
Stesso numero di colonne per ogni riga.
Un database: mette insieme il livello estensionale(i nomi delle coleonene) e le righe, in un database abbiamo dei dati.
In questo esempio questo database sta rappr. un sistema uni, il corso Java è tenuto dal docente BIagio ROssi e si tiene nell'aula gialla.
Per capire questa cosaa dobbiamo guardare alla colonna codice del modulo, dell'aula e del docente.
Guardiamo meglio:
![[Modello relazionale dei dati2.png]]

Le colonne sono anche chiamate attributi, le righe sono ennnuple (in inglese tuple) o record.
Il concetto fond. qui è: quando c'è il tre nel codice Modulo e trova lo stesso tre nel codice di Aula non è un riferimento python, non c'è un puntatore tra le due tabelle ma grazie a quel tre sappiamo ripercorre quei dati ma non è impl. per davvero.
QUesto database sono facilemte interpretabili e portabili (possono essere trasferite da un sistema all'altro). 
Tuttavia non è detto che tutte le celle sono occupate da dati:
![[Informazione incompleta.png]]

Non sappiamo l'indirizzo email di Carla Neri, quando manca un dato è sconuscituto o assente. Se si volesse distiinguere i due casi dobbiamo avere un'attributo che ci speighi il perchè manca quel dato.
La struttura pero è rigda.
Nonostante ciò un database possono rispettare la struttura delle tabelle, ma non moella corettamente i requisiti:
![[Vincoli di integrità.png]]

Il probelma della tabella Esame ad esempio il vlaore cucina non esiste in questa tabella, non è un modulo, anche il 35 supera il range dei voti che vanno da 18 a 30.
Stessa cosa nell'ultima riga ho uno studente ma non conosco il modulo.
In realtà sia gli int sbalgiati che le ennuple nella colonna 

I vincoli di prorietà sono: una proprietà che deve essere soddisfatta dal contnetuto delle tablella del DB affinchè rappresentino informazioni corette per l'app.


Esistono due vincoli:
intra-tabella: una sola tabella ad esempio il 35 è scoretto semplicemente guardandolo 
inter-tabella: i vincoli per capire se sono vincoli coretti devo guardare diverse tabelle

Vincoli ennula
Esrimono condizioni dui valori di ciascuna ennupla di una tabella, indipendentemente dalle altre ennuple
- voto >=18 and voto<=30

Vincoli di chiave o di colonna sono quelli inter-tabella: dice che non eisitpno più ennuple della stessa tabella che coincidono sul valore di uno o più attributi 
Esempio: 
non esistono due studenti con la stessa matricola 
non esistono due studenti che hanno gli stessi valori 
per nome, cognome, nascita 

Una chiave è un insieme di valori per quella chiave:
- non possono esistere due ennuple che coincidono su tutti tali attributi 
- se togliessimo da k un qualunque attributo, i restanti non formerebbero più una chiave (sono analoghi agli `{id}` in UML).
  Ma allora ritornando la tabella studente, immaginiamo che io non possa avere due studenti con lo stesso codice, ma quindi potrei avere un null al posto di codice? Si, 
Come risolvere questo problema: tra tutte le chiavi della tabella ne sceglie una detta chiave primaria; è una chiave ma i valori non possono essere `null`.
Quindi qui la chiave primaria è la coppia studente-modulo infatti non possono ripetersi perché uno studente non può passare due volte lo stesso modulo. 
Se ci sono due studenti con codice `null` e poi in Esame ho due `null` su studente e modulo.

### Chiavi e valori `null`
I vincoli intrateabella hanno solo a che fare con quella tabella
vincoli chiavi: non sono valori duplicati
Non possono essere due ennuple della tabella ESAme che coinciodno con il voto e il modulo, ne possono essere null.
Quindi come implementare i collegamenti tra le tabelle:
quando dicihamo che la prima ennupla di esame; lo studente ha codice 1 e quindi nella tabella studente mi aspetto di trovare uno studente con codice 1.
I dati in tabella diverse sono correlati attraversi i vlaori delle loro chiavi o chiave primarie 
#### I vincoli foreign key (integrità referenziale)

![[Foreign Key.png]]

Da un insieme di attributi A in Tabella T1 verso tutti gli attributi di una chiave K di tabella T2:
T1(A) references T2(K), 
Tutti i valori di t1(A) devono occoree come valori della chiave K in un ennupla T2.
Vediamo un altro esempio 
![[FK Esempio.png]]

La talbella di Officina è fatta da nome e in idrizzo:
La chiave primaria  della tabella Officina è `nome` 
La tabella Veicolo è formata dalle colonne targa e tipo:
	la chiave primarina è targa

La tabella Riparazione è formata dalle colonne Riparazione:
	le chiave primarie sono officina e codice: qui si sta dicendo che il codice di riparazione può essere lo stesso se sono di due officine diverse.

I valori della colonna veicolo della tabella Riparazione devono coincidere con la colonna targa della tabella Veicolo: quindi ogni ennupla della colonna veucolo devono coincidere con la targa del veicolo.
QUini per implementare questi rifeirmenti li dobbiamo implementare attraveros le foreign key:
- FK :Riparazione (veicolo) refenrces Veicolo(targa).
Abbiamo impl il vincolo se scriviamo in Riparazione un ennupla qualsiasi con un veicolo e non è riferita a una targa di Veicolo il DB da errore.

Le FK vanno scritte vicino alle tabelle.

FK: (officina) references Officina (nome), si sta dicendo che il nome dell'officina della tabwlla riparazione deve riferirsi al nome dell'Officina della tabella Officina

Prendiamo in considerazione la tabella RIcambioRIP:
mi deve dire chi è la riparazione (quindi l'offiicina)
il codice di riparazione(chiamato rip, ed è il codice che si trova in Riparazione)
e il pezzo di ricambio di riparazione 
FK: RicambioRip(officina, rip) references Riparazione(officina, codice)
Quindi officina, codice mi garnatisce di arrivare a un ennupla di RIparazione.
Non posso avere una chiave da una colonna di RIcambio RIP alle tre colonne di Riparazione. 

Ogni volta che inserisco un ennupla il DBSM fa il giro di tutte le tabelle per vedere se quella ennupla garatinsce e rispetta i vincoli di integrità.
Ma se io cancello la ennupla di veicolo cosa succede? Essendoci una FK che da questa tabella si riferisce alla tabella Riparazione il DBMS non te lo fa fare, rifiuta l'operazione. 
QUindi se c'è un operazione che appena completata cancella una enupla il DBMS riconsce quell'operazione come illegale e non te lo lascia fare.
E se volessimo fare che aggiungimao una colonna `tipo_prefe`, cioè il tipo  di cui si occupa quella officina si potrebbe fare
FK officina (tipo_prefe) refences Veicolo(tipo)?
No perchè sarebbe come dire che ci sono die freccie cha vanno su tutte le ennuple della tabella Veicolo.
Il DBMS di defualt annula le operazioni che causerebbero incoerenza dei dati.
Non solo se un ennupla di Veicolo diventasse un update cioè si aggiorna il valore non va comunque più bene, quindi cosa posso fare quando ci sono canclellazionei o update?
Per quanto riguarda le cancellazzioni: se dimentico un veicolo le riparazuioni di quell veicolo le cancello? 
Mettiamo che cancelliamo il prio valore di nome in Officina in RIparazione il primo valore di officina è una chiave primaria quindi non posso farlo a meno che non accetto i vlaori Null e cosi a catena su tutte le chiavi e le ennuple a cui fanno rifeirmento.
Quindi se cancello o aggiorno un ennupla di una tabella tutte le ennuple delle diverse tabelle a cui si riferiscono la prima ennupla modificata la cancellazione o l'aggiornamento devono essere fatta a cascata su ttute le altre ennuple di tutte le tabelle.
COme si fa a indicare cosa volgio fare? Se voglio accettare una modifica che viola il vincolo di FK in DBMS devo scirvere FK Riparazione (veicolo) references Veicolo(targa) ON DELETE SET NULL oppure ON  DELETE CASCADE(cancella a cascata tutte le cose problematiche del mio sistema).

