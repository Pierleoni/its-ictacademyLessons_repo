# Introduzione
Una volta conclusa la fase di [[Analisi dei requisiti mediante UML|Analisi dei requisiti]] , e completato lo **schema concettuale** del sistema (rappresentato tramite **diagrammi UML** e **specifiche formali**), inizia la **fase di progettazione**.
Questa fase rappresenta un passaggio fondamentale nell'ingegneria del software: si tratta di stabilire **come** realizzare il sistema informativo, a partire da **ciò che esso deve fare**, come definito durante l'analisi.
## Fase di progettazione
L'obiettivo principale è definire le **soluzioni tecniche** per implementare l’applicazione. 
Questo comporta la scelta e l’organizzazione di:

- Linguaggi di programmazione da utilizzare;
    
- Tecnologie e strutture per la **memorizzazione dei dati**;
    
- Architettura dell’applicazione;
    
- Algoritmi per la realizzazione delle funzionalità;
    
- Altri componenti infrastrutturali e metodologici necessari alla messa in opera del sistema.
    

In sintesi: ==mentre l’**analisi** si concentra sul _cosa_ fa il sistema, la **progettazione** si focalizza su _come_ realizzarlo==.

### Struttura della fase di progettazione

Questa fase si può suddividere in due sottosezioni principali:
#### 1.Input/Output della fase di progettazione 

L’input è costituito da quanto prodotto nella fase di analisi, ovvero:

- Lo **schema concettuale** dell’applicazione;
    
- I **diagrammi UML** 
    
- Le **[[Documenti di specifica|specifiche formali]]**, che descrivono:
    
    - [[Documenti di specifica#specificaDato Specifica dei tipi di dato|I tipi di dato]];
        
    - [[Documenti di specifica#specificaClasse Specifica di classe|Le classi]];
        
    - [[Documenti di specifica#specUse-case Specifica degli use case|Gli use-case]];
        
    - [[Documenti di specifica#specificaVincoliEx Specifica dei vincoli esterni|I vincoli esterni]] (regole di business, requisiti di integrità, ecc.).

![[Input della fase di progettazione.png]]
 L’output consiste in una serie di **documenti di progetto** che guidano la realizzazione concreta del sistema. Tali documenti formalizzano le scelte architetturali e tecnologiche da adottare.

Le decisioni fondamentali includono:

- Quali **linguaggi di programmazione** utilizzare;
    
- Quali **DBMS e modelli di dati** (relazionali, NoSQL, ecc.) adottare;
    
- Come strutturare l’**architettura dell’applicazione** (monolitica, a microservizi, client-server, ecc.);
    
- Quali **algoritmi e logiche di business** implementare;
    
- La definizione dei **moduli funzionali** del sistema.
![[Output della fase di progettazione.png]]


### Focus del modulo: Progettazione della base dati
In questo modulo, ci concentreremo in particolare sulla progettazione della **base dati relazionale**, con l’obiettivo di garantire la **memorizzazione persistente** dei dati identificati nella fase concettuale.

In particolare:

- Si traduce lo schema concettuale (es. diagrammi delle classi) in uno schema logico-relazionale;
    
- Si definiscono le tabelle, chiavi primarie e esterne, vincoli di integrità, ecc.;
    
- Si progettano eventuali viste, indici e procedure associate.

**In altri moduli**, si affronterà la progettazione delle **funzionalità applicative**:

- Backend (interfaccia con la base dati, logica di business);
    
- Frontend (interazione con l’utente tramite interfacce grafiche, web app o app mobili);
    
- Integrazione tra frontend, backend e DBMS.

### In conclusione
La fase di progettazione rappresenta il ponte tra **modellazione concettuale** e **realizzazione tecnica**. 
È cruciale per garantire che l’implementazione sia coerente con i requisiti, efficiente nelle prestazioni, e sostenibile nella manutenzione e nell’evoluzione futura del sistema.

---

## DataBase Management System (DBMS)

### Motivazioni per l’adozione di un DBMS

In linea teorica, potremmo realizzare un sistema informativo persistente utilizzando semplici file (ad esempio JSON o CSV) per memorizzare oggetti e relazioni tra essi sul file system. 
Tuttavia, tale approccio presenta alcune criticità rilevanti:

- **Incoerenza dei dati**: 
  ==ogni file può essere creato, modificato o cancellato indipendentemente dagli altri, il che può causare **incoerenze logiche** tra le informazioni memorizzate;==
    
- **Problemi di concorrenza**: 
  ==in ambienti multiutente o distribuiti, **processi concorrenti** (es. funzionalità invocate simultaneamente da attori diversi) potrebbero interferire tra loro nella lettura/scrittura dei dati, causando **errori e comportamenti imprevisti**;== 
    
- **Gestione manuale della persistenza e del controllo di accesso**: 
  ==la responsabilità di garantire la coerenza, l’accesso controllato e la sicurezza ricade completamente sugli sviluppatori.==
    

Per superare queste limitazioni si ricorre all’utilizzo di un **DBMS (DataBase Management System)**.

### Cos’è un DBMS?

Un **DBMS** è: 
==un sistema software specializzato nella **gestione di grandi collezioni di dati** su memoria di massa, che fornisce servizi fondamentali per la realizzazione di sistemi informativi affidabili ed efficienti.== 

Le principali funzionalità offerte da un DBMS includono:

- **Accesso controllato e granulare ai dati**: 
  ==gestione avanzata di utenti, ruoli, gruppi e privilegi per accedere a dati specifici;==
    
- **Supporto alla concorrenza**: 
  ==esecuzione sicura di **transazioni concorrenti**, anche da parte di applicazioni o utenti diversi, garantendo **coerenza e isolamento**;==
    
- **Persistenza dei dati**: 
  ==i dati vengono memorizzati in modo permanente, anche in caso di interruzioni o malfunzionamenti del sistema;==
    
- ==**Interrogazione e manipolazione efficiente** dei dati tramite linguaggi standardizzati (come SQL);== 
    
- **Gestione dei metadati**: 
  ==i DBMS conservano **dati sui dati**, ovvero informazioni sulla struttura e sui vincoli del database stesso;== 
    
- **Memorizzazione distribuita e/o replicata**: 
  ==alcuni DBMS supportano l’allocazione dei dati su più nodi, aumentando affidabilità e disponibilità;== 
    
- **Semplificazione per sviluppatori e progettisti**: 
  ==molte funzionalità complesse sono già implementate e gestite dal DBMS, evitando la necessità di realizzarle da zero;== 
    
- **Standardizzazione dell’interfaccia**: 
  ==l’interazione con i DBMS avviene tramite **API e linguaggi comuni**, rendendo più semplice l’**eventuale sostituzione** del sistema (a patto di rispettare lo standard adottato).== 
    

> [!Note]  nonostante l’esistenza di standard (come SQL per i DB relazionali), **non tutti i DBMS commerciali li implementano completamente**, e possono esistere differenze sintattiche o semantiche da un sistema all’altro.

### Modelli di dati

I DBMS si distinguono in base al **modello dei dati** su cui si basano. In questo modulo ci concentreremo sul **modello relazionale**, che rappresenta i dati sotto forma di **tabelle (relazioni)** composte da righe (tuples) e colonne (attributi), in coerenza con lo schema concettuale derivante dall’analisi (es. [[Analisi dei requisiti mediante UML#^myImg|diagramma delle classi UML]]). 

## Modello relazionale dei dati e DBMS relazionali

I vari DBSM si distinguono per la tipologia di modello dei dati che offrono:
in questo caso parliamo di DB relazionali secondo cui rappresentare i dati in maniera relazionale.
Esiste anche una altro modello detto DBMS a grafo:
coppie di chiave/valore, etc. (oggetto di altre unità).

### Modello relazionale dei dati

Il **modello relazionale** è un modello logico per l’organizzazione dei dati, 
in cui le **informazioni sono strutturate in tabelle** (dette anche _relazioni_), ognuna delle quali ha:

- ==Un **nome** identificativo==;
    
- ==Un **insieme di attributi**, ognuno con un **tipo di dato** (es. `int`, `string`, `boolean`, ecc.).==
    

Le righe delle tabelle vengono chiamate **ennupla**(o _tuple_ in inglese):
- ==Ogni **riga** della tabella rappresenta un’istanza di dati==.  ^ennuple

Mentre le colonne sono chiamate o attributi o campi:
- ==ogni **colonna o attributo** rappresenta un attributo del dominio==.  ^colonna

#### Esempio
L’esempio seguente rappresenta un database relazionale che descrive un sistema universitario, con informazioni su:

- **Moduli didattici**;
    
- **Aule** in cui si tengono i corsi;
    
- **Docenti** che li tengono.
![[Modello relazionale dei dati.png]]
Il database è quindi composto da tre tabelle:
1. `Modulo`
2. `Aula`
3. `Docente`  

#### Livelli di rappresentazione
Come per il diagramma della classi anche nel modello relazionale si distinguono due livelli fondamentali:
- Livello intensionale (schema del DB): 
	==definisce la struttura delle tabelle, i nomi degli attributi e i loro tipi.== 
- Livello estensionale (contenuto del DB): 
	==rappresenta i dati effettivamente contenuti nel database, ovvero le [[#^ennuple|ennuple]].== 

#### Collegamenti tra le tabelle 
==Il modello relazionale **non utilizza riferimenti diretti o puntatori** come nei linguaggi di programmazione(es: Python).== 
Tuttavia, ==**i valori degli attributi (come `codice aula` o `codice docente`) fungono da collegamenti logici tra le tabelle**.==

Ad esempio:

- Il modulo `java` è associato all’aula con codice `232`, che nella tabella `Aula` corrisponde all’**Aula Gialla**.
    
- Il codice docente `227` della tabella `Modulo` corrisponde, nella tabella `Docente`, a **Biagio Rossi**.
    

Questi **valori numerici funzionano come "chiavi":** 
==permettendo la **navigazione dei dati** tra tabelle, senza che vi siano riferimenti implementati come in una struttura a oggetti.== 

![[Lettura delle tabelle.png]]

> [!remember] **Terminologia**
>|Concetto| Sinonimi comuni|
>|------------|-----------------------|
>|  Tabella | Relazione           |
>|  Riga     |   Ennupla, Tuple,Record| 
>| Colonna| Attributo, Campo |
>|Tipi di dato| Dominio dell'attributo|



Guardiamo meglio:
![[Modello relazionale dei dati2.png]]

Questi riferimenti tra ennuple di tabelle diverse **non sono riferimenti implementati** (come puntatori in Python).  
Tuttavia, grazie ai **valori condivisi** tra le tabelle, è possibile **ricostruire i collegamenti logici**.

==Quindi i valori fungono da "riferimenti a" o "collegamenti" (bidirezionali) tra ennuple di tabelle differenti.==


> [!done] **Vantaggi del modello relazionale**
> -  **Intellegibilità**: i dati sono leggibili e comprensibili anche da non esperti;
>  
>- **Navigabilità**: i dati possono essere esplorati facilmente grazie ai riferimenti logici tra tabelle;
>    
>-  **Portabilità**: il formato relazionale è indipendente dal sistema e può essere trasferito o migrato tra piattaforme diverse.


### Modello relazionale dei dati: informazione incompleta
Il **modello relazionale** impone ai dati una **struttura rigida**:

- I dati sono organizzati in **ennupla** (o _tuple_), ovvero righe delle tabelle;
    
- Le **ennupla ammesse** sono vincolate dallo **schema di relazione**, cioè dalla struttura (intensionale) predefinita della tabella. 
Tuttavia, nella realtà può accadere che **alcuni dati non siano disponibili**, per diverse ragioni, come ad esempio:

![[Informazione incompleta.png]]

**Possibili significati dell'informazione mancante:**

1. Il valore è **sconosciuto** (es. l’utente non ha fornito l’informazione);
    
2. Il valore è **inesistente** (es. non esiste proprio quell’attributo per quel soggetto);
    
3. Il valore è **sconosciuto o inesistente** (non è possibile distinguere i due casi).

###### Come viene rappresentata l’informazione mancante?

I DBMS permettono di associare ad un attributo il **valore speciale `NULL`**, che rappresenta il **caso 3**, ovvero:
==un valore mancante di cui non si conosce se sia assente o sconosciuto.==

Nello specifico:
Nel esempio, l’indirizzo email della docente `Carla Neri` è mancante:
Il valore `NULL` nella colonna `email` **non ci dice se l’indirizzo è ignoto oppure non esiste**.

###### Esempio:
Nel seguente esempio, l’indirizzo email della docente `Carla Neri` risulta mancante:

| codice:int | nome:string | cognome:string | email:string                |
| ---------- | ----------- | -------------- | --------------------------- |
| 1          | Alice       | Bianchi        | `alicebianchi@yahoo.it`     |
| 2          | Biagio      | Rossi          | `biagio.rossi@yourmail.com` |
| 3          | Carla       | Neri           | NULL                        |
| 4          | Daniela     | Verdi          | `dani2001@kmail.com`        |


In questo caso, il valore `NULL` nella colonna `email` **non permette di distinguere se l’indirizzo non esiste o se non è noto**.
###### Come distinguere i casi?
Per distinguere tra le diverse **cause dell’assenza del dato**, è necessario **modificare lo schema** del database.  
Una tecnica comune consiste nell’aggiungere un **attributo esplicativo**, ad esempio:

| codice:int | nome:string | cognome:string | email:string                | ragione_assenza_email:int |
| ---------- | ----------- | -------------- | --------------------------- | ------------------------- |
| 1          | Alice       | Bianchi        | `alicebianchi@yahoo.it`     |                           |
| 2          | Biagio      | Rossi          | `biagio.rossi@yourmail.com` |                           |
| 3          | Carla       | Neri           | NULL                        | 1                         |
| 4          | Daniela     | Verdi          | `dani2001@kmail.com`        |                           |
In questo caso, il valore `NULL` nella colonna `email` **non permette di distinguere se l’indirizzo non esiste o se non è noto**.
Se si vuole distinguere tra 1. o 2. bisogna farlo esplicitamente, ad esempio, aggiungendo nuovi attributi che “spieghino” il significato di NULL:
Ad es., nuovo attributo `ragione_assenza_email:int`.
Dove `ragione_assenza_email` può assumere valori codificati come:

- `1`: sconosciuto
    
- `2`: inesistente
    
- `3`: sconosciuto o inesistente (comportamento predefinito)


> [!example] In conclusione
> Il modello relazionale garantisce **struttura e coerenza**, ma proprio per questo motivo non è nativamente adatto alla **gestione raffinata dell’informazione mancante**.  
>==L’uso di `NULL` è utile, ma insufficiente quando si vuole conoscere la causa dell’assenza.==  
>In tali casi, è necessario **progettare consapevolmente lo schema** per esplicitare tale informazione.


### Vincoli di integrità 
Come abbiamo appena visto **database relazionale** può essere **strutturalmente corretto**, ovvero conforme agli schemi di tabelle, ma **non rappresentare correttamente i requisiti dell’applicazione** (ad esempio viene assegnato il valore `NULL`).  
Per evitare ciò, si introducono nel modello i **vincoli di integrità**, ovvero **regole che devono essere soddisfatte dal contenuto delle tabelle**.
Questi vincoli sono:
	==Proprietà che deve essere soddisfatta dal contenuto delle tabelle del DB affinché rappresentino informazioni corrette per l’applicazione==

>⚠️ Ad uno schema di base di dati associamo un insieme di vincoli di integrità e consideriamo legali (aka accettabili) solo i DB che li soddisfano tutti.

#### Tipologie di vincoli
I vincoli si suddividono in due grandi categorie
1. **Intra-tabella**:
	==Coinvolgono **una singola tabella**, e riguardano condizioni su righe o colonne.==   ^intra-tabella

2. **Inter-tabella**: 
	  ==Coinvolgono **più tabelle** e impongono coerenza tra dati relazionati.==  ^inter-tabella

##### Esempio: dati incoerenti
Per comprendere meglio cosa sono i vincoli di integrità, nel seguente esempio la tabella `Esame` contiene dati che violano diversi vincoli logici:

![[Vincoli di integrità.png]]

ad esempio: 
- alla seconda ennupla il valore `cucina` dell'attributo `modulo`  non esiste in questa tabella, perché non è un modulo d'esame.
- alla terza ennupla anche il valore `35` dell'attributo `voto` supera il range dei voti che vanno da 18 a 30, quindi non è legale.
- alla quarta ennupla il valore  `NULL` dell'attributo `Studente` e il valore `True` dell'attributo `lode` sono entrambi illegali, perché:
	nel primo caso si ha null per il codice di `Studente` quindi non si conosce lo studente che ha sostenuto l'esame, mentre nel secondo il `True` è vero solo se il voto è `30`; ma siccome il valore dell'attributo `voto` in questo caso è 25 allora dovrebbe essere `False`.
- Stessa cosa nell'ultima riga ho uno studente ma non conosco il modulo.


A sua volta i vincoli [[#^intra-tabella|intra-tabella]] si suddividono in due categorie:
1. I vincoli di ennupla.  
2. I vincoli di chiave o di colonna
#### Vincoli di ennupla

Esprimono condizioni sui valori di ciascuna ennupla di una tabella, indipendentemente dalle altre ennuple.
In altre parole:
==sono **condizioni sui valori** di ciascuna riga della tabella, considerate **indipendentemente dalle altre righe**==.

**Esempi:**
- `voto >=18 and voto<=30`
- `IF lode = TRUE THEN voto = 30`

==Quindi si tratta di vincoli, facilmente verificabili su ogni singola riga==. 
#### Vincoli di chiave o di colonna
I **vincoli di chiave** impongono che **non possano esistere due ennuple (righe) che coincidano sugli stessi valori** di uno o più attributi di una tabella.
 In altre parole: 
	 ====servono a garantire **unicità** su determinati attributi, impedendo la duplicazione dei dati==.

##### Definizione di una chiave
Un **insieme K di attributi** è detto **chiave** della tabella se soddisfa due proprietà:
- **Unicità**: ==Non esistono due ennuple con gli **stessi valori per tutti gli attributi di K**==.
    
- **Minimalità**: ==se si rimuove un qualsiasi attributo da K, la proprietà di chiave viene persa.== 
In sostanza: 
- non possono esistere due ennuple che coincidono su tutti tali attributi 
- se togliessimo da k un qualunque attributo, i restanti non formerebbero più una chiave.

Per analogia, una chiave nel modello relazionale corrisponde all’identificatore `{id}` in UML:  
==serve a **distinguere in modo univoco** ogni istanza della relazione.==

**Esempio pratico:**  
Consideriamo due esempi di vincolo di **unicità**:

- 🔹 _Non possono esistere due studenti con lo stesso codice di matricola_ → **il campo `matricola` è una chiave**.
    
- 🔹 _Non possono esistere due studenti con gli stessi valori per `{nome, cognome, data_nascita}`_ → **anche questa può essere una chiave**, ma solo se l’unicità è garantita, cosa che **nella realtà non è sempre vera**.
    

> [!caution] **Attenzione**  
> L’insieme `{nome, cognome, data_nascita}` non è un identificatore affidabile nel mondo reale, perché **persone diverse possono condividere questi dati**.

  Ma allora, ritornando all'immagine [[Vincoli di integrità.png|soprastante]], immaginiamo che io non possa avere due studenti con lo stesso codice,  quindi si potrebbe avere un `NULL` al posto di codice? 
  Sì, è tecnicamente possibile che un attributo di una **chiave generica** (cioè non primaria) abbia valore `NULL`.
Tuttavia, questo **compromette la funzione identificativa** della chiave, perché:

- `NULL` **non è comparabile**: due valori `NULL` non sono mai “uguali”;
    
- Non si può verificare l’unicità su righe contenenti `NULL`.
Quindi per evitare ambiguità e mantenere l'unicità:
==**Si sceglie una chiave tra quelle possibili, detta _chiave primaria_**, su cui **è vietato l’uso di valori `NULL`**.==

Quindi, in questo caso:
si può definire la **chiave primaria** della tabella `Esame` come la **coppia** `{studente, modulo}`:
>uno **studente non può sostenere lo stesso modulo due volte**.

Quindi, righe come queste **non sono valide**:

| studente | modulo | voto | lode  |
| -------- | ------ | ---- | ----- |
| `NULL`   | prog   | 28   | False |
| `NULL`   | prog   | 30   | True  |
In presenza di `NULL` nei campi che compongono la chiave primaria:

- Non è possibile determinare se le due righe si riferiscono allo **stesso studente**;
    
- **Il vincolo di unicità non è verificabile**;
- Il collegamento logico tra tabelle (es. con `Studente`) **non può essere garantito**


### Chiavi e valori `null`
Per spiegare ancora meglio questo concetto:
In presenza di valori `NULL`, i valori degli attributi che formano una chiave di una tabella:
- ==non permettono di identificare univocamente le ennuple della tabella.==
-  ==non permettono di realizzare facilmente i riferimenti con dati di altre tabelle.==


##### Esempio senza chiave primaria
Prendiamo ad esempio tre tabelle:

**Tabella Studente**

| codice:int | nome:stringa | cognome:stringa | nascita: data |
| ---------- | ------------ | --------------- | ------------- |
| 1          | Alice        | Bianchi         | `03/04/2000`  |
| `NULL`     | Biagio       | Rossi           | `08/03/2000`  |
| 3          | Carla        | Neri            | `NULL`        |
| `NULL`     | Daniele      | Verdi           | `07/01/2001`  |
^tabellaStudente

**Tabella Modulo**

| codice: stringa | nome:stringa     |
| --------------- | ---------------- |
| prog            | Progettazione    |
| `NULL`          | Programm. Python |
| java            | Programm. Java   |
| `NULL`          | Data Science     |
^tabellaModulo


**Tabella Esame**

| studente:int | modulo:stringa | voto:int | lode:booleano |
| ------------ | -------------- | -------- | ------------- |
| 1            | prog           | 28       | False         |
| 1            | `NULL`         | 30       | True          |
| 4            | java           | 27       | False         |
| `NULL`       | ds             | 25       | False         |
| 2            | ballo          | 21       | False         |
| `NULL`       | `NULL`         | 30       | False         |
^tabellaEsame

Come si nota:

- Il campo `studente` nella tabella `Esame` contiene `NULL`, che impedisce di determinare l'identità del candidato;
    
- Alcuni codici modulo non corrispondono a quelli presenti nella tabella `Modulo` (es. `ballo`);
    
- La presenza di `NULL` compromette sia **unicità** che **referenzialità**.


> [!link] **Collegamenti tra tabelle e integrità referenziale**
> Nel modello relazionale, i collegamenti tra le tabelle **non avvengono tramite puntatori**, ma tramite **valori condivisi** di attributi (tipicamente chiavi primarie e chiavi esterne).
>
> Se i valori di chiave primaria contengono `NULL` o dati incoerenti, **le relazioni logiche tra le tabelle non possono essere garantite.**

#### La chiave primaria
Per ovviare a queste problematiche si sceglie, tra le chiavi della tabella,  una o più chiavi, che diventa/no la **chiave primaria**. 
Le caratteristiche della **chiave primaria** sono:
- ==Gli attributi della chiave primaria non possono avere valori `NULL`==
- ==Gli attributi della chiave primaria di una tabella sono indicati sottolineati.==   

##### **Esempio pratico di chiave primarie**
**Tabella Studente**

| <u>codice:int<u> | nome:stringa | cognome:stringa | nascita:data |
| ---------------- | ------------ | --------------- | ------------ |
| 1                | Alice        | Bianchi         | `3/4/2000`   |
| `NULL`           | Biagio       | Rossi           | `8/3/2000`   |
| `3`              | Carla        | Neri            | `NULL`       |
| `NULL`           | Daniele      | Verdi           | `7/1/2000`   |
^Primarykey-tabellaStudente


**Tabella Modulo**

| <u>codice:stringa<u> | nome:stringa     |
| -------------------- | ---------------- |
| prog                 | Progettazione    |
| `NULL`               | Programm. Python |
| java                 | Programm. Java   |
| `NULL`               | Data science     |
^Primarykey-tabellaModulo


**Tabella Esame**

| <u>studente:int<u> | <u>modulo:stringa<u> | voto:int | lode:booleano |
| ------------------ | -------------------- | -------- | ------------- |
| 1                  | prog                 | 28       | FALSE         |
| 1                  | `NULL`               | 30       | TRUE          |
| 4                  | java                 | 27       | FALSE         |
| `NULL`             | ds                   | 25       | FALSE         |
| 2                  | ballo                | 21       | FALSE         |
| `NULL`             | `NULL`               | 30       | FALSE         |
^Primarykey-tabellaEsame


##### Differenza tra tabelle senza chiave primaria e con chiave primaria
Nell'esempio [[#Esempio senza chiave primaria|senza chiave primaria]] le tabelle mostrate, non avendo una chiave primaria, presentano alcune criticità strutturali e logiche:
1. **Presenza di valori `NULL` in campi che dovrebbero essere identificativi**
	- Nella tabella [[#^tabellaStudente|`Studente`]], il campo (tabella) `codice`, che rappresenta il numero di matricola, contiene alcuni il valore `NULL`: 
	  ==quindi impedisce univocamente di identificare lo studente associato a quella ennupla==.
	- Nella tabella [[#^tabellaModulo|`modulo`]], il campo `codice` contiene alcuni valori `NULL`: 
	  ==quindi non è possibile distinguere o referenziare in modo sicuro i moduli.==
2. **Assenza di un vincolo di unicità**
	- Nella tabella [[#^tabellaEsame|`Esame`]], ==non è impedita la ripetizione di coppie `studente-modulo` o la presenza di valori `NULL` in entrambi; queste mancanze compromettono l'integrità dei dati.==
3. **Impossibilità di stabilire referenze certe**
	Ad esempio; nella tabella [[#^tabellaEsame|`Esame`]] valori relativi ai campi `studente` e `modulo` come `studente = NULL` o `modulo = "ballo"` non trovano corrispondenza in alcuna tabella: ==**non è possibile garantire la validità del collegamento [[#^inter-tabella|inter-tabella]]**.==

Invece nell'[[#**Esempio pratico di chiave primarie**|esempio con chiavi primarie]], le stesse tabelle sono dotate di chiavi primarie esplicite definite e vanno ad ovviare a questi problemi:

1. **Chiave primaria nella tabella [[#^Primarykey-tabellaStudente|`Studente`]]:**
	Il campo `codice` diventa la chiave primaria della tabella.
	==In questo modo ogni studente è identificato in modo univoco da un valore non `NULL`, garantendo l'identificabilità.==
2. **Chiave primaria nella tabella [[#^Primarykey-tabellaModulo|`Modulo`]]:**
    il campo `codice` diventa la chiave primaria della tabella.
    Così facendo è come dire: ==ogni modulo è univocamente identificato da un codice distinto e non nullo== (`NULL`).
3. **Chiave primaria nella tabella [[#^Primarykey-tabellaEsame|`Esame`]]:**
    la coppia di campi `studente-modulo` diventano entrambi chiave primarie della tabella.
    Così facendo è come dire: ==Uno **stesso studente non può sostenere più volte lo stesso modulo.**==
	    ==Infatti viene così garantita l'integrità dei dati.==
	
    Inoltre, ==entrambi i campi sono non `NULL`, per garantire la possibilità di referenze certe.==

#### Collegamenti tra tabelle tramite chiavi primarie
Quindi l’introduzione delle chiavi primarie abilita la **navigazione logica** tra le tabelle:

- ==Quando nella tabella `Esame` compare `studente = 1`, il sistema può:==  
    ==→ risalire alla tabella `Studente` e trovare l’ennupla con `codice = 1`.==
    
- ==Allo stesso modo, `modulo = 'prog'` permette:==  
    ==→ di accedere alla tabella `Modulo` e identificare il modulo corrispondente.==
    

Questa tecnica di **riferimento tramite chiavi primarie** consente ai [[#Cos’è un DBMS?|DBMS]] di:

- Verificare la **coerenza** dei dati tra le tabelle;
    
- Impedire **inserimenti errati** (es. moduli inesistenti);
    
- Mantenere **l’integrità referenziale** del database.


#### I vincoli foreign key (integrità referenziale)
Dopo aver analizzato i vincoli **intra-tabella** – cioè quelli che coinvolgono una sola tabella – come i [vincoli di ennupla](#Vincoli-di-ennupla) e i [vincoli di chiave o di colonna](#Vincoli-di-chiave-o-di-colonna), possiamo ora esaminare i vincoli **inter-tabella**, ovvero quelli che garantiscono **la coerenza tra dati presenti in tabelle diverse**.

Quando esistono **dati comuni** tra più tabelle (ad esempio, codici o identificativi), questi dati devono essere **coerentemente correlati**. Questa correlazione viene garantita formalmente tramite i **vincoli di integrità referenziale**, detti anche **vincoli di foreign key** (_chiave esterna_).

**Definizione formale:**
Un vincolo di foreign key collega:

==un **insieme di attributi** `A` di una tabella `T1`  
a una **chiave** `K` di un’altra tabella `T2`==.   ^defFK

Espresso formalmente:

```sql
T1(A) references T2(K).
```

##### Significato:

==Tutti i **valori** presenti negli attributi `A` della tabella `T1` devono **apparire anche** come **valori della chiave `K`** in almeno una ennupla (riga) della tabella `T2`==.

In altre parole:
	==Ogni valore della foreign key deve **corrispondere a un valore esistente** nella tabella referenziata.== 



> [!remember] **Come leggere correttamente le foreign key**
> Nel contesto delle foreign key(FK), i termini standard  e universalmente accettati sono:
> - La tabella che contiene la foreign key è la cosiddetta tabella figlia (o child table).
> 	- Esempio:
>```postgresql
>FOREIGN KEY (officina) ...
>```
>- La **tabella referenziata** dalla foreign key è detta **tabella padre** (_referenced table_ o _parent table_).
>	- Esempio:
>```postgresql
>REFERENCES Officina(nome)
>```
>- ==La **colonna nella tabella figlia** (in questo caso, `officina`) è la **foreign key** vera e propria==
>
>- ==La **colonna nella tabella padre** (in questo caso, `nome` in `Officina`) è una **chiave primaria** o **chiave candidata**.==
>
>Per capire meglio, consideriamo il seguente esempio::
>
>```postgresql
>CREATE TABLE Officina (
> 	 nome VARCHAR PRIMARY KEY
>);
>
>CREATE TABLE Riparazione (
> 	 officina VARCHAR,
> 	 FOREIGN KEY (officina) REFERENCES Officina(nome)
>);
>```
>  **Spiegazione:**
>  - ==`Officina` è la **tabella padre (referenziata)**.==
 >   
>- ==`Riparazione` è la **tabella figlia (che contiene la FK)**.==
>    
>- ==`officina` in `Riparazione` è la **foreign key**.==
>    
>- ==`nome` in `Officina` è la **primary key** (o una chiave candidata).==
>
>>[!caution] **Attenzione a non cadere in un errore comune**
>>Si potrebbe pensare che:
>>
>>- La tabella referenziata sia quella "**a cui arriva**" la FK.
>>    
>>- La tabella figlia sia quella "**da cui parte**" la FK.
>>Questa interpretazione, sebbene intuitiva, **è imprecisa**. La foreign key **non è una freccia visiva** (da sinistra a destra nel codice), ma un **vincolo logico** tra due tabelle.
>
>**La definizione corretta è**:
>==Una **foreign key** è un vincolo tra un insieme di attributi `A` di una tabella `T1` (figlia) e una chiave `K` di una tabella `T2` (padre).==
>
>In altre parole:
>
> ==La foreign key parte dalla tabella figlia e **referenzia** (punta a) la tabella padre.==
>
>> [!example] **In conclusione**
>> evita di ragionare in termini visivi (“parte/arriva”, “sinistra/destra”) e preferisci invece la logica relazionale: ==chi **dichiara la FK** è **figlia**, chi **la fornisce** (ossia contiene la chiave referenziata) è **padre**.==
> 


##### Esempio pratico di foreign key

**Tabella Modulo**

| <u>codice:string<u> | nome:string      | crediti:int | aula:int                                      | docente:int |
| ------------------- | ---------------- | ----------- | --------------------------------------------- | ----------- |
| prog                | Progettazione    | 6           | <mark style="background: #00FF02A6;">1</mark> | 1           |
| python              | Programm. Python | 6           | <mark style="background: #E5FF00A6;">3</mark> | 3           |
| java                | Programm. Java   | 3           | <mark style="background: #ADCCFFA6;">2</mark> | 2           |
| ds                  | Data science     | 6           | <mark style="background: #00FF02A6;">1</mark> | 3           |

**Tabella Aula:**

| <u>codice<br>:int<u>                          | nome<br>:string | indirizzo<br>:string |
| --------------------------------------------- | --------------- | -------------------- |
| <mark style="background: #00FF02A6;">1</mark> | Aula Rossa      | via Petriolesi 38    |
| <mark style="background: #ADCCFFA6;">2</mark> | Aula Gialla     | Piazza Garibaldi 22  |
| <mark style="background: #E5FF00A6;">3</mark> | Aula Verde      | Via Cavour 44        |
| 4                                             | Aula Blu        | Piazza Mancini 56    |
###### Analisi

- Il valore `aula = 1` nella tabella `Modulo` **corrisponde** all'`aula` con `codice = 1` nella tabella `Aula`. ✔️
    
- Il valore `aula = 3` in `Modulo` corrisponde al `codice = 3` in `Aula`. ✔️
    
- Il valore `aula = 4` **non è presente** nella tabella `Modulo`: questo è **ammesso**, perché **non esiste alcun modulo che si svolga nell’aula blu**, ma non **viceversa**.

**Definizione della foreign key**
Per esprimere un **vincolo di integrità referenziale** tra due tabelle, si può utilizzare **una notazione descrittiva** o la **sintassi SQL vera e propria**. Ecco le due modalità:
1. **Forma descrittiva (pseudocodice didattico)**
```plaintext
foreign key: Modulo(aula) references Aula(codice)
```


> [!info]-
> - Questa **non è sintassi SQL**, ma una **notazione concettuale** spesso usata in **dispense, slide o diagrammi ER** per esprimere l’idea che il campo `aula` della tabella `Modulo` fa riferimento al campo `codice` della tabella `Aula`.
 >   
>- È utile a **livello didattico** per chiarire la relazione tra le tabelle, **ma non può essere usata nei file `.sql`** o nei DBMS reali.



2. La **dichiarazione del vincolo di integrità referenziale** in forma eseguibile si scrive:
```postgresql
FOREIGN KEY (aula) REFERENCES Aula(codice)
```


> [!info]-
> - Questa è la **sintassi corretta in SQL**, da utilizzare nei comandi `CREATE TABLE` nei file `.sql`, ed è compatibile con **PostgreSQL** e altri RDBMS standard.
  >- Non va indicato il nome della tabella di partenza (Modulo) all’interno delle parentesi, poiché si è già nel contesto della sua definizione.

###### Requisito fondamentale del vincolo

In **entrambi i casi**, l’attributo `codice` della tabella `Aula` **deve costituire una chiave** (tipicamente una **chiave primaria**):

> ==`Aula(codice)` deve essere una chiave della tabella `Aula`, affinché per ogni valore `aula` presente nella tabella `Modulo` **esista al più una ennupla corrispondente** nella tabella `Aula`.==

Questo è ciò che garantisce l’**integrità referenziale**, impedendo la presenza di riferimenti “orfani”.

![[FK.png]]


##### Esempio pratico dei foreign key
Supponiamo di avere **quattro tabelle relazionate tra loro**:

![[FK Esempio.png]]

1. **Tabella `Officina`**

- Contiene i campi:
    
    - `nome` → **chiave primaria**
        
    - `indirizzo`
        

2. **Tabella `Veicolo`**

- Contiene i campi:
    
    - `targa` → **chiave primaria**
        
    - `tipo`
        

3. **Tabella `Riparazione`**

- Contiene i campi:
    
    - `officina` → **parte della chiave primaria** e **foreign key**
        
    - `codice` → **parte della chiave primaria**
        
    - `veicolo` → **foreign key**
        
- La **chiave primaria** è composta da `(officina, codice)`, cioè:
    
    > ==Lo stesso codice di riparazione può esistere in officine diverse.==
    
- Il campo `veicolo` fa riferimento a `Veicolo(targa)`, quindi ogni riparazione è associata a un veicolo registrato.
    

#### 4. **Tabella `RicambioRip`**

- Contiene i campi:
    
    - `officina` → **parte della chiave primaria** e **foreign key**
        
    - `rip` → **parte della chiave primaria** e **foreign key**
        
    - `ricambio` → **parte della chiave primaria**
        
- La **chiave primaria** è composta da `(officina, rip, ricambio)`.
    

> ==In sostanza, lo stesso codice di riparazione (`rip`) nella stessa officina può comparire più volte **solo** se il ricambio è diverso.==

##### Definizione dei vincoli di integrità referenziale
Per garantire la coerenza tra queste tabelle, definiamo i vincoli `FOREIGN KEY` come segue:
1. Vincolo su `Veicolo` in `Riparazione`

==Ogni valore del campo `veicolo` deve corrispondere a una targa esistente in `Veicolo`.==

```plain text
 FK :Riparazione (veicolo) refenrces Veicolo(targa).
```
o
```postgresql
FOREIGN KEY (veicolo) REFERENCES Veicolo(targa)
```

**Requisito fondamentale del vincolo**

Implementando questo vincolo: 
	 ==ogni valore nel campo `veicolo` di `Riparazione` **deve esistere come targa nella tabella `Veicolo`**.==
	 ==Se si tenta di inserire una riparazione per un veicolo inesistente, il DBMS solleverà un errore di violazione dell’integrità referenziale.==

> [!ticket] Regola d'oro
> Le Foreign Key vanno scritte vicino alle tabelle.

2. **Vincolo su `officina` in `Riparazione`**
Serve a collegare il campo `officina` con la tabella `Officina`.
```plain text
FK: Riparazione(officina) references Officina (nome)
```

o
```postgresql
FOREIGN KEY (officina) REFERENCES Officina(nome)
```


**Requisito fondamentale del vincolo**
==Ogni `officina` registrata in `Riparazione` deve esistere come `nome` in `Officina`.==

3. **Vincolo composito su `RicambioRip` verso `Riparazione`**
==Il campo `rip` rappresenta il codice di una riparazione, che ha significato solo in combinazione con `officina`, per formare la chiave `(officina, codice)` di `Riparazione`.==
```plain text
FK: RicambioRip(officina, rip) references Riparazione(officina, codice)
```

o
```postgresql
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice)
```

**Requisito fondamentale del vincolo**
- ==La coppia `(officina, rip)` di `RicambioRip` **deve esistere** nella tabella `Riparazione` come chiave `(officina, codice)`.== 
    
- In questo modo ogni ricambio è legato a una **riparazione ben definita**.


> [!fail] **Errore comune da evitare**:
> ==Non è possibile riferirsi solo a `rip` (senza `officina`) se la chiave nella tabella referenziata è composta.==  
>==Questo produrrebbe una violazione semantica e strutturale del modello relazionale.==


> [!remember] **Regole da ricordare sulle foreign key**
> - Le foreign key **devono fare riferimento a una chiave (primaria o candidata)** della tabella di destinazione.
>    
>- **Tutti gli attributi coinvolti devono avere lo stesso tipo e dominio** di quelli di riferimento.
 >   
>- **I valori devono esistere** nella tabella referenziata al momento dell’inserimento, a meno che non siano `NULL` (in alcuni casi consentito).

### Cosa succede se un’operazione viola un vincolo di foreign key?
Ogni volta che si esegue un’**operazione di modifica del database** (inserimento, aggiornamento, cancellazione), il **DBMS verifica automaticamente i vincoli di integrità referenziale** tra le tabelle coinvolte.

==Se l’operazione **compromette un vincolo `FOREIGN KEY`**, il **DBMS la blocca e genera un errore**, impedendo che la base di dati finisca in uno stato inconsistente.==

#### Caso 1: cancellare un ennupla vincolata da una foreign key
Quindi se si cancella la ennupla di una tabella cosa succede? 
Per spiegare nel dettaglio questo concetto prendiamo ad esempio due tabelle:

**Tabella Riparazione**

| <u>officina<u> | <u>codice<u> | veicolo   |
| -------------- | ------------ | --------- |
| FixIt          | 1            | HK 243 BW |
| CarFix         | 1            | AA 662 XQ |
| FixIt          | 2            | HK 243 BW |
**Tabella Veicolo**

| <u>targa<u> | tipo |
| ----------- | ---- |
| HK 243 BW   | auto |
| AA 662 XQ   | auto |
| HK 243 BW   | auto |
Immaginiamo ci siano anche due FK:
```plain text

FK: Riparazione(officina) ref. Officina(nome)
FK: Riparazione(veicolo) ref. Veicolo(targa)
```

o:

```postgresql
-- Vincolo sulla colonna veicolo
FOREIGN KEY (veicolo) REFERENCES Veicolo(targa)

-- Vincolo sulla colonna officina (presumibilmente esistente in tabella Officina)
FOREIGN KEY (officina) REFERENCES Officina(nome)

```

Il significato di questi vincoli è il seguente:

- ==Ogni valore della colonna `officina` in `Riparazione` deve corrispondere a un `nome` valido nella tabella `Officina`;==
    
- ==Ogni valore della colonna `veicolo` in `Riparazione` deve esistere nella colonna `targa` della tabella `Veicolo`.==

Proviamo a fare un tentativo di modifica:

ovvero modificare l’ennupla (`AA 662 XQ, auto`) nella tabella `Veicolo`: 
	cioè cancellare il valore `AA 662 XQ` del campo `targa` nella tabella `Veicolo`, e al suo posto mettere un nuovo valore a quella ennupla;  `ZZ 111 ZZ, auto`.
```postgresql
UPDATE Veicolo
SET targa = 'ZZ 111 ZZ'
WHERE targa = 'AA 662 XQ';
```

Questa operazione viene **bloccata dal DBMS** perché la targa `AA 662 XQ` è ancora referenziata nella tabella `Riparazione`:
Perché:
	
Il DB rileva che la modifica violerebbe il vincolo di foreign key perché la targa `AA 662 XQ` viene modificata in `Veicolo`, ma è ancora referenziata nella tabella `Riparazione` dal veicolo associato alla riparazione (`CarFix, 1`)
	—> Quindi il DB rifiuta l’operazione, mantenendo il vincolo soddisfatto.
	
Quindi se c'è un operazione che appena completata cancella una ennupla il DBMS riconosce quell'operazione come illegale e non permette la modifica.
![[tentativo di cancellare e aggiungere una nuova ennupla.png]]


> [!info] **Comportamento del DBMS**
> - Il DBMS **controlla tutte le ennuple coinvolte**, in tutte le tabelle correlate.
>    
>- Se anche **una sola ennupla** verrebbe a violare un vincolo, **l’intera operazione viene annullata** (rollback implicito).
 >   
>- Questo comportamento è fondamentale per **garantire la coerenza dei dati**.


> [!ticket] **Regola generale**
> Quando un campo `A` in una tabella `T1` è una **foreign key verso** `T2(K)`, allora:
>
>- ==Non si può **eliminare** un valore da `T2(K)` **se è ancora usato** in `T1(A)`==
 >   
>- ==Non si può **modificare** un valore di `T2(K)` in modo da rompere la relazione==
>    
>
>**A meno che non si specifichi un comportamento esplicito** (es. `ON DELETE CASCADE`, `ON UPDATE SET NULL`, ecc.).

#### Caso 2: **modifica e riparazione delle ennuple orfane con valori `NULL`**
Immaginiamo di avere queste 3 tabelle:

**Tabella Riparazione**

| <u>officina<u> | <u>codice<u> | veicolo   |
| -------------- | ------------ | --------- |
| FixIt          | 1            | HK 243 BW |
| CarFix         | 1            | AA 662 XQ |
| FixIt          | 2            | HK 243 BW |
^tabellaRiparazione

**Tabella Veicolo**

| <u>targa<u> | tipo |
| ----------- | ---- |
| HK 243 BW   | auto |
| AA 662 XQ   | auto |
| HK 243 BW   | auto |
^tabellaVeicolo

**Tabella RicambioRip**

| <u>officina<u> | <u>rip<u> | <u>ricambio<u> |
| -------------- | --------- | -------------- |
| FixIt          | 1         | A755           |
| FixIt          | 1         | A788           |
| CarFix         | 1         | A991           |
| FixIt          | 2         | B332           |
^tabellaRicambioRip

E ipotizziamo che ci siano 3 FK:
```plain text
vincoli su Riparazione

FK: Riparazione(officina) ref. Officina(nome)
FK: Riparazione(veicolo) ref. Veicolo(targa) 

Vincoli su RicambioRip
FK: RicambioRip(officina, rip) ref. Riparazione(officina, codice)
```

In postgresql:
```postgresql
-- Vincoli su Riparazione
FOREIGN KEY (officina) REFERENCES Officina(nome)
FOREIGN KEY (veicolo) REFERENCES Veicolo(targa)

-- Vincolo su RicambioRip
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice)
```


Questi vincoli di FK significano che:

- ==Ogni valore della colonna `officina` in `Riparazione` deve corrispondere a un `nome` valido nella tabella `Officina`;==
    
- ==Ogni valore della colonna `veicolo` in `Riparazione` deve esistere nella colonna `targa` della tabella `Veicolo`.==
- Ogni valore della coppia `officina, rip` in `RicambioRip` deve esistere nella coppia `officina, codice` in `Riparazione`.

**Tentativo di modifica: aggiornare la chiave `(officina, codice)` di `Riparazione`**
Supponiamo di voler **modificare la riga** `(CarFix, 1, AA 662 XQ)` nella tabella `Riparazione`, sostituendo il codice da `1` a `2`:
```postgresql
UPDATE Riparazione
SET codice = 2
WHERE officina = 'CarFix' AND codice = 1;
```

Questa operazione viene bloccata perché:
==La riga `(CarFix, 1)` è attualmente **referenziata** nella tabella `RicambioRip`==, ad esempio da:
```plain text
(CarFix, 1, A991)
```

Poiché la foreign key di `RicambioRip` è definita come:
```postgresql
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice)
```

il **DBMS blocca l’operazione**: non è possibile modificare il valore di una **chiave primaria** se esso è ancora utilizzato come riferimento in un'altra tabella.

>[!info]- **Comportamento del DBMS**
>
>- Il DBMS esegue un controllo di integrità prima di completare l'aggiornamento.
>    
>- Se una modifica a una chiave romperebbe un vincolo di foreign key, l'intera operazione viene **annullata** (rollback implicito).
 >   
>- Questo impedisce la **creazione di riferimenti orfani** (cioè record che fanno r

In questo caso si potrebbe agire usando il modificatore [[#Esempio `ON UPDATE SET NULL`|`ON UPDATE SET NULL`]]. 
^accennoONUpdate


> [!ticket] **Regola generale**
> Se `(A, B)` è una **foreign key** in una tabella `T1` che fa riferimento a una chiave primaria `(A, B)` in `T2`:
>
>- ✅ Non si può modificare né `A` né `B` in `T2` se esistono righe in `T1` che fanno riferimento a quella coppia.
 >   
>- ✅ L’operazione è **consentita solo se nessuna ennupla fa più riferimento a quella chiave**.
 >   
>- ✅ In alternativa, si possono usare clausole come `ON UPDATE CASCADE` per forzare l’aggiornamento anche nei riferimenti.

Quindi in conclusione:
==**Modificare una chiave primaria referenziata da una foreign key composta senza indicare un comportamento esplicito (es. `ON UPDATE CASCADE`) provoca un errore.**==  
==Questo serve a **garantire che tutte le relazioni tra i dati restino valide e coerenti**.==


#### Caso 3: cancellare una ennupla referenziata da una foreign key
Riprendiamo la situazione con le **tre tabelle relazionate** e i rispettivi vincoli di integrità referenziale:

1. **Tabella [[#^tabellaRiparazione|Riparazione]]**
2. **Tabella [[#^tabellaVeicolo|Veicolo]]**
3. **Tabella [[#^tabellaRicambioRip|Ricambio Rip]]**

I vincoli di foreign key attivi sono:
```plain text
vincoli su Riparazione

FK: Riparazione(officina) ref. Officina(nome)
FK: Riparazione(veicolo) ref. Veicolo(targa) 

Vincoli su RicambioRip
FK: RicambioRip(officina, rip) ref. Riparazione(officina, codice)
```

**Tentativo di cancellazione:**
Supponiamo di voler cancellare l’ennupla:
```plain text
('CarFix', 1, 'AA 662 XQ') 
```
dalla tabella `Riparazione`.
Anche in questo caso questa operazione viene **bloccata dal DB**, perché:

- Esistono **riferimenti attivi** nella tabella `RicambioRip`, dove compare la coppia `(CarFix, 1)`, che costituisce **una foreign key verso** `(officina, codice)` in `Riparazione`.

>**In breve:** ==il database rileva che la cancellazione violerebbe il vincolo di integrità referenziale, perché esistono ancora **dati dipendenti** (figli) nella tabella `RicambioRip`.==


> [!info] **Comportamento predefinito del DBMS**
>Se non viene specificata un’azione diversa, il DBMS:
>
>- **Blocca** automaticamente l’operazione di `DELETE`;
 >   
>- **Solleva un errore** di violazione del vincolo referenziale;
>    
>- **Mantiene la coerenza** del database evitando l'inserimento di stati invalidi.

Questo problema può essere risolto con il modificatore [[#Significato di `ON DELETE SET NULL`|`ON DELETE SET NULL`]].   
^accennoONdelete

#### **Caso 4: aggiunta di una colonna e gestione di aggiornamenti/cancellazioni**

Ora come ultimo esempio supponiamo di voler **aggiungere una colonna** nella tabella `Officina`, chiamata `tipo_prefe`, che indica il tipo di veicolo su cui l’officina è specializzata.
Ma è corretto definire un vincolo di questo tipo?
```postgresql
FOREIGN KEY (tipo_prefe) REFERENCES Veicolo(tipo)
```
**Risposta: No.**
Perché ==una Una **foreign key deve sempre riferirsi a una chiave primaria o candidata** (unica) della tabella di destinazione.==  
==Nel nostro caso, `Veicolo(tipo)` **non è una chiave**, ma un attributo generico che **può ripetersi** (es. molti veicoli possono essere "auto").==

> 📌 ==Sarebbe come dire che ogni tipo dichiarato in `tipo_prefe` dell’officina **deve esistere tra i tipi dei veicoli registrati**, ma **non è garantito che ci sia univocità**==.
> 
> Di conseguenza, il vincolo referenziale **non può essere applicato**, perché `Veicolo(tipo)` non soddisfa i requisiti di **destinazione di una foreign key**.


### Azioni compensative per vincoli di foreign key
Come abbiamo visto nei **casi precedenti**, quando un'operazione (come una cancellazione o un aggiornamento) **viola un vincolo di foreign key**, il **DBMS, per impostazione predefinita, rifiuta l’operazione**.
Tuttavia, il **progettista del database** può decidere di **modificare questo comportamento** indicando esplicitamente **un'azione compensativa** da eseguire in caso di violazione.

#### Esempio: `On Delete SET NULL`
Prendiamo il [[#Caso 3 cancellare una ennupla referenziata da una foreign key|Caso n. 3]]: 
Supponiamo che la tabella `RicambioRip` abbia una foreign key verso `Riparazione(officina, codice)`.

```plain text
FK: RicambioRip(officina, rip) ref.Riparazione ON DELETE SET NULL(officina, codice)
```

o per scriverla in postgresql:
```postgresql
FOREIGN KEY (officina, rip) 
REFERENCES Riparazione(officina, codice) 
ON DELETE SET NULL
```

==In questo caso, se si **cancella un’ennupla** da `Riparazione`, il DBMS **non blocca l’operazione**, ma imposta automaticamente i campi `officina` e `rip` nelle ennuple di `RicambioRip` a `NULL`.==


![[Azione Compensativa.png]]

Il DBMS modifica la ennupla problematica di `RicambioRip` in (`NULL, NULL, A991`), mantenendo il vincolo soddisfatto.
In questo caso, **essendo questi attributi parte della chiave primaria**, il DBMS non può lasciare la situazione così, ed è costretto ad annullare tutte le modifiche, poichè le chiavi primarie non possono contenere valori `NULL` e quindi questa operazione causerebbe incoerenza dei dati.
E come sappiamo il DBMS di default annulla le operazioni che causano incoerenza dei dati.
Quindi anche con `ON DELETE SET NULL`, l'operazione viene annullata. 

> [!ticket] **Regola D'oro**
> **le azioni compensative devono essere compatibili con i vincoli della tabella** (es. chiavi primarie, `NOT NULL`, ecc.).

#### Significato di `ON DELETE SET NULL` nelle foreign key
Quando si definisce una **foreign key** in SQL, è possibile specificare un **comportamento personalizzato** da eseguire nel caso in cui venga cancellata una riga dalla tabella referenziata.
Uno di questi comportamenti è:
```postgresql
ON DELETE SET NULL
```

#### Cos'è `ON DELETE SET NULL`?
Quindi il modificatore `ON DELETE SET NULL` è una **clausola opzionale** che si può specificare **all'interno della definizione di una foreign key** in SQL.
Esempio di sintassi:
```postgresql
FOREIGN KEY (campo_ref)
REFERENCES AltraTabella(chiave)
ON DELETE SET NULL
```

**Significa che:**

> ==**Se si cancella un’ennupla dalla tabella referenziata (quella con la chiave primaria), allora il valore del campo nella tabella che la referenzia viene impostato automaticamente a `NULL`.**==

Per fare un esempio pratico:
Ritorniamo al [[#Caso 3 cancellare una ennupla referenziata da una foreign key|Caso 3 cancellare una ennupla referenziata da una foreign key]], in questo caso il modificatore `ON DELETE SET NULL` viene scritto così:
```postgresql
FOREIGN KEY (officina, rip) 
REFERENCES Riparazione(officina, codice)
ON DELETE SET NULL
```

**Spiegazione:**
Questo codice definisce **un vincolo di integrità referenziale con comportamento personalizzato in caso di cancellazione.**
Vediamolo step by step;
1. **Contesto: da dove a dove punta la foreign key:**
	   -  **Tabella con la foreign key** → `RicambioRip`
    
	- **Tabella referenziata** → `Riparazione`
    
	- **Colonne coinvolte**:
    
	    - Nella tabella `RicambioRip`: `(officina, rip)`
        
	    - Nella tabella `Riparazione`: `(officina, codice)`
        
- Questa è una **foreign key composta**: coinvolge due attributi.

2. **Funzione base del vincolo:**
```postgresql
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice)
```
significa:

> ==Ogni ennupla della tabella `RicambioRip` deve contenere una **coppia di valori (`officina`, `rip`)** che **deve esistere** nella tabella `Riparazione`, nella coppia (`officina`, `codice`).==

In altre parole:

> ==Ogni pezzo di ricambio (`ricambio`) deve essere **associato a una riparazione esistente**, identificata dalla combinazione **officina + codice**.==

3. La clausola:
```postgresql
ON DELETE SET NULL
```

modifica il comportamento del vincolo in caso di **cancellazione di un record nella tabella `Riparazione`**.

> **Significato**:  
> ==Se una **riparazione viene cancellata** dalla tabella `Riparazione`, allora il valore della **foreign key `(officina, rip)`** nelle ennuple corrispondenti di `RicambioRip` viene **impostato automaticamente a `NULL`**.==



>[!ticket] **Requisito fondamentale**  
>Affinché il `ON DELETE SET NULL` funzioni:
>
>> [!remember]  
>> ✅ I campi `officina` e `rip` in `RicambioRip` **devono essere `nullable`**, cioè **non devono avere il vincolo `NOT NULL`**.  
>> ❌ Se invece sono dichiarati `NOT NULL`, il DBMS **rifiuterà la cancellazione**, perché **non può impostare `NULL` su un campo che non lo accetta**.

Quindi, come illustrato nel [[#^accennoONdelete|Caso 3]] e visibile nell'immagine [[Azione Compensativa.png]], il problema che normalmente causerebbe **una violazione del vincolo di chiave esterna** viene gestito dal modificatore `ON DELETE SET NULL` in questo modo:

- Il DBMS tenta di aggiornare automaticamente le ennuple corrispondenti in `RicambioRip` impostando i valori di `officina` e `rip` a `NULL`.
    
- Tuttavia, **dato che questi due attributi fanno parte della chiave primaria**, e una **chiave primaria non può mai contenere `NULL`**, il DBMS **non può portare a termine l’operazione**.
    
- **Risultato:** l’intera operazione di cancellazione viene **annullata** per non violare i vincoli di integrità.

> [!example]- Cosa si intende per `nullable`
> Per `nullable` si intende in linguaggio postgresql:
> ```postgresql
> CREATE TABLE RicambioRip (
>    officina VARCHAR(100),  -- nullable
 >   rip INTEGER,            -- nullable
 >   ricambio TEXT,
 >   FOREIGN KEY (officina, rip)
 >       REFERENCES Riparazione(officina, codice)
 >       ON DELETE SET NULL
> );
> ```
> **Spiegazione**
> Oltre a riferirci al codice prendiamo anche come riferimento [[Azione Compensativa.png|l'immagine]]
> Cioè `officina` è una stringa con lunghezza massima di 100 ed è una chiave unica non primaria(questo concetto lo approfondiremo più avanti), stessa cosa per `rip`.
> Entrambi i campi della tabella `RicambioRip` hanno i vincoli `NOT NULL`, quindi è possibile applicare il modificatore `ON DELETE SET NULL`. 
> In questo caso il DBMS verificherà se esistono ennuple nella tabella `RicambioRip` con `(officina = 'CarFix', rip =1)` e controllerà anche l'ennupla presente in `Riparazione` andando a cancellarla e a sostituire i valori dei campi dell'ennupla a cui fa riferimento in `RicambioRip` con `NULL`.

#### Esempio: `ON UPDATE SET NULL` 

Come già accennato nel [[#^accennoONUpdate|Caso 2]], supponiamo che nella tabella `RicambioRip` sia definito un vincolo di foreign key come segue:
```plain text
FK: RicambioRip(officina, rip) ref. Riparazione ON UPDATE SET NULL (officina, codice)
```

==Questa clausola `ON UPDATE SET NULL` **modifica il comportamento del vincolo** quando si effettua **un aggiornamento (update)** su una delle colonne della **chiave primaria** della tabella referenziata, ovvero `Riparazione`.==

Il significato di questo vincolo è:
> ==Se viene modificato (tramite `UPDATE`) il valore della chiave primaria in una tupla della tabella `Riparazione`, allora il DBMS imposterà automaticamente a `NULL` i campi corrispondenti nella tabella `RicambioRip` che la referenziano.==

![[On Update Set Null.png]]


Quindi:
- ==Il DB modifica la ennupla problematica di `RicambioRip` in (`NULL, NULL, A991`), mantenendo il vincolo soddisfatto.==
	- Grazie alla clausola `ON UPDATE SET NULL`, il comportamento previsto è che i campi referenziali (`officina`, `rip`) nelle ennuple di `RicambioRip` vengano **automaticamente impostati a `NULL`**.
	- In pratica, il DBMS intercetta l’aggiornamento e cerca di “disinnescare” il vincolo impostando i valori di riferimento a `NULL`.
- ==Anche in questo caso, sebbene sia stato specificato `ON UPDATE SET NULL`, poiché i campi `officina` e `rip` fanno parte della chiave primaria (e quindi non possono essere `NULL`), il DBMS **non può applicare l’azione** e **blocca l’aggiornamento**, mantenendo l’integrità del database.
	-  In questo scenario, il DBMS **non è in grado di applicare l’azione compensativa** prevista dalla clausola `ON UPDATE SET NULL`.
    
	- Di conseguenza, **l’operazione di aggiornamento viene annullata**, e il DBMS genera un **errore di violazione del vincolo di integrità** per evitare uno stato inconsistente nel database.

##### Cos'è `ON UPDATE SET NULL`?
Come per [[#Cos'è `ON DELETE SET NULL`?|`ON DELETE SET NULL`]], `ON UPDATE SET NULL` è una **clausola opzionale** che può essere associata a un **vincolo di foreign key** (`FOREIGN KEY`) in SQL, e che definisce **il comportamento automatico del DBMS** nel caso in cui la **chiave primaria (o candidata)** referenziata venga **modificata** (tramite `UPDATE`).

La sintassi è la seguente:
```postgresql
FOREIGN KEY (campo_locale) REFERENCES TabellaDiRiferimento(campo_remoto) ON UPDATE SET NULL
```

oppure per chiavi composte:
```postgresql
FOREIGN KEY (campo1_locale, campo2_locale)
REFERENCES TabellaDiRiferimento(campo1_remoto, campo2_remoto)
ON UPDATE SET NULL
```

Il significato di questa clausola è:
>Se nella **tabella referenziata** viene **modificato** uno dei valori della **chiave primaria** (o altra chiave referenziata) a cui punta la foreign key, allora:
>
>⚠️ ==**tutti i riferimenti a quel valore nella tabella che contiene la foreign key verranno impostati a `NULL` automaticamente**.==


> [!ticket] **Requisiti fondamentali**
> Perché `ON UPDATE SET NULL` funzioni:
>> [!remember]
>> - ==**I campi referenziali devono essere `NULLABLE`**, cioè **non devono avere il vincolo `NOT NULL`**==
>>    
>>- **Non devono essere parte di una chiave primaria**  
>>    ==Le chiavi primarie **non ammettono valori NULL**, quindi il DBMS **rifiuterebbe** l’operazione.==
>>    
>>- ==La foreign key **deve puntare a una chiave (primaria o candidata)** esistente nella tabella di destinazione.==


> [!abstract] **Quando usare `ON UPDATE SET NULL`?**
> Può essere utile **quando la relazione è opzionale**, cioè quando **non è obbligatorio** che la tupla figlia (la tabella con la foreign key) mantenga sempre un riferimento attivo.  
Tipico nei seguenti scenari:
>
>- Un oggetto può esistere **senza riferimento** (es. un dipendente senza ufficio)
 >   
>- Si vuole **evitare errori** bloccanti in fase di `UPDATE`
 >   
>- Si prevede che le chiavi referenziate **possano cambiare nel tempo**


### Esempio : `ON DELETE CASCADE`
Per spiegare il funzionamento di questa clausola, riprendiamo il [[#Caso 3 cancellare una ennupla referenziata da una foreign key|Caso 3]].

Supponiamo di voler **cancellare l’ennupla** (`CarFix, 1, AA 662 XQ`) dalla tabella `Riparazione`.  
Come già illustrato in precedenza, questa operazione violerebbe un vincolo di **integrità referenziale**, poiché **esistono ennuple nella tabella `RicambioRip` che referenziano la tupla che si desidera eliminare**.

Abbiamo visto che anche l’uso di:

```postgresql
ON DELETE SET NULL
```

non è sufficiente in questo caso, poiché i campi `officina` e `rip` nella tabella `RicambioRip` **fanno parte della chiave primaria** e quindi **non possono contenere valori `NULL`**.

##### Soluzione alternativa: `ON DELETE CASCADE`

Un modo per **risolvere automaticamente la violazione del vincolo** in questo scenario è utilizzare la clausola:
```plain text
FK: RicambioRip(officina, rip) ref. Riparazione ON DELETE CASCADE (officina, codice)
```

O scritta in codice:
```postgresql
FOREIGN KEY (officina, rip)
REFERENCES Riparazione(officina, codice)
ON DELETE CASCADE
```

**Significato:**

> ==Se si cancella una tupla dalla tabella `Riparazione`, tutte le ennuple in `RicambioRip` che la referenziano vengono **automaticamente eliminate dal DBMS**.==  
> In altre parole, la cancellazione della tupla padre (`Riparazione`) **propaga** la cancellazione anche alle tuple figlie (`RicambioRip`) che la referenziano.

Difatti:
![[On Delete Cascade.png]]

Come possiamo vedere da questa immagine l'uso del `ON DELETE CASCADE` fa in modo che  Il DB cancella la ennupla problematica di `RicambioRip`, mantenendo il vincolo soddisfatto.

> [!important] **Vantaggio principale**  
>==Il vincolo `ON DELETE CASCADE` è utile quando le tuple figlie **non hanno più senso di esistere** senza la tupla padre.==  
>Evita violazioni di integrità e semplifica le operazioni di pulizia dei dati collegati.

##### Cos'è l'`ON DELETE CASCADE`, cancellazione in cascata delle ennuple orfane
`ON DELETE CASCADE` è una **clausola opzionale** che può essere specificata all’interno della definizione di una **foreign key** in SQL, e serve a **modificare il comportamento del DBMS in caso di cancellazione di una riga nella tabella referenziata**.

> ==Se viene cancellata un’ennepla nella tabella referenziata (cioè quella che possiede la chiave primaria), allora tutte le ennuple della tabella corrente (cioè quella che contiene la foreign key) che fanno riferimento a quella riga verranno automaticamente cancellate.==

> In altre parole, si verifica una **cancellazione in cascata**, che impedisce la creazione di ennuple orfane (ovvero righe figlie che non hanno più un genitore valido).

La sintassi è:
```postgresql
FOREIGN KEY (campo_locale)
REFERENCES TabellaReferenziata(campo_referenziato)
ON DELETE CASCADE
```


> [!ticket] Scopo di `ON DELETE CASCADE`
> - **Mantenere l'integrità referenziale** automaticamente
 >   
>- **Evitare errori** quando si cancellano record padre che sono referenziati da altri record
 >   
>- È molto utile quando:
 >   
  > 	 - Le righe **figlie non hanno senso di esistere senza la riga padre**
 >       
  > 	 - Non vuoi gestire manualmente la cancellazione delle righe dipendenti


> [!fail] **Attenzione**
> - L’**uso improprio** di `ON DELETE CASCADE` può portare alla **cancellazione non intenzionale di molti dati**, specialmente se ci sono **catene di foreign key** su più livelli.
 >- È consigliabile utilizzarlo solo quando esiste una dipendenza logica forte tra la tabella padre e quella figlia.


#### Esempio: `ON UPDATE SET NULL`, aggiornamento in cascata
Per spiegare questa clausola riprendiamo il [[#Caso 2 **modifica e riparazione delle ennuple orfane con valori `NULL`**|Caso 2]].

Come già illustrato, **se si tenta di aggiornare uno dei campi coinvolti in una chiave primaria** (nella tabella referenziata), il DBMS normalmente **blocca l’operazione**, per evitare che venga **violato il vincolo di integrità referenziale**.

> Anche con la clausola `ON UPDATE SET NULL`, l'operazione viene **annullata** se i campi referenziati sono parte della chiave primaria nella tabella figlia (come nel caso di `RicambioRip`), poiché le **chiavi primarie non possono contenere valori `NULL`**.

Per ovviare a questo limite, si può usare la clausola `ON UPDATE CASCADE`.


Quindi si vuole aggiornare l'ennupla (`'CarFix', 1, 'AA 662 XQ'`) nella tabella `Riparazione`, modificandola in: (`'CarFix', 2, 'AA 662 XQ'`).

Poiché la chiave primaria di `Riparazione` è composta da `(officina, codice)`, e `(officina, rip)` in `RicambioRip` è una foreign key che fa riferimento a essa, **bisogna istruire il DBMS su come aggiornare automaticamente le ennuple figlie**.
Quindi il vincolo deve essere definito come segue:

**In forma astratta**
```plain text
FK: RicambioRip(officina, rip) ref.Riparazione ON UPDATE CASCADE (officina, codice)
```

**In sintassi PostgreSQL:**
```postgresql
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice) ON UPDATE CASCADE
```

Il che significa:
> ==Quando viene eseguito un aggiornamento sulla **chiave primaria** della tabella `Riparazione`, il DBMS propaga automaticamente la modifica anche ai campi corrispondenti nella tabella `RicambioRip`.==

> In questo modo, l’integrità referenziale viene **mantenuta automaticamente**, **senza generare ennuple orfane** e senza dover intervenire manualmente.

![[ON UPDATE CASCADE.png]]

Come possiamo vedere da l'immagine grazie all'utilizzo di questa clausola il DB modifica la ennupla problematica di `RicambioRip` in (`CarFix, 2, A991`), mantenendo il vincolo soddisfatto.
In altre parole: 
Quando viene aggiornato uno dei campi della **chiave primaria** in `Riparazione`, il DBMS **propaga automaticamente la modifica** a tutte le ennuple della tabella `RicambioRip` che fanno riferimento alla chiave modificata.
In tal modo:

- **l’integrità referenziale viene mantenuta**;
    
- **nessuna ennupla orfana viene generata**;
    
- **nessuna operazione manuale** di aggiornamento è richiesta lato applicazione.


La clausola `ON UPDATE CASCADE` ha una logica analoga a quella del `ON DELETE CASCADE`, con la **differenza sostanziale** che:

- [[#Esempio `ON DELETE CASCADE`|`ON DELETE CASCADE`]] → ==**cancella** automaticamente tutte le ennuple figlie associate alla riga padre eliminata;==
    
- `ON UPDATE CASCADE` → ==**propaga l’aggiornamento** della chiave primaria della riga padre a tutte le ennuple figlie che la referenziano.== 
In entrambi i casi, lo scopo è **mantenere l’integrità referenziale** in modo automatico.

#### `ON UPDATE CASCADE` — Cos'è e cosa fa

`ON UPDATE CASCADE` è **una clausola opzionale** che può essere specificata nella **definizione di una foreign key**. Serve a istruire il DBMS su **come comportarsi quando il valore di una chiave primaria (o candidata) viene modificato** nella **tabella referenziata**.

Il significato di questa clausola è:

> ==Se si modifica (con `UPDATE`) il valore di una **colonna referenziata** in una tabella **padre**, allora **tutte le ennuple nella tabella figlia** che fanno riferimento a quel valore **vengono automaticamente aggiornate** con il nuovo valore.==

Questo consente di **propagare le modifiche** in modo **coerente**, mantenendo **l'integrità referenziale** senza dover aggiornare manualmente i record figli.

La sintassi base di questa clausola è :
```postgresql
FOREIGN KEY (campo_locale) REFERENCES TabellaPadre(campo_primario) ON UPDATE CASCADE
```

Mentre nelle chiavi composte è:
```postgresql
FOREIGN KEY (campo1_locale, campo2_locale) REFERENCES TabellaPadre(campo1, campo2) ON UPDATE CASCADE
```


> [!caution] **Requisiti e limiti**
> - **Le colonne referenziate devono essere parte di una chiave unica o primaria** nella tabella padre.
>    
>- **I campi nella tabella figlia devono essere aggiornabili** (cioè **non devono avere vincoli che impediscano la modifica**, ad es. `ON UPDATE SET NULL` con `NOT NULL`).
>    
>- Il vincolo `ON UPDATE CASCADE` **non funziona se l’aggiornamento violerebbe altri vincoli**, come `UNIQUE`, `NOT NULL`, `PRIMARY KEY`, ecc.


> [!done] **Quando usarlo?**
> `ON UPDATE CASCADE` si usa quando **le chiavi esterne devono sempre rimanere coerenti** con quelle della tabella padre **anche dopo aggiornamenti**.
> I vantaggi sono:
> - Automatizza la propagazione delle modifiche.
  >  
>- Previene errori di integrità.
  >  
>- Semplifica la logica dell'applicazione.
>
>> [!info]- **Confronto con altri comportamenti**
>> |Clausola|Comportamento su aggiornamento nella tabella padre|
>>|----------------|------------------------------------------------------------------------|
>>|`NO ACTION` (default)| Blocca l'operazione se viola il vincolo|
>>|`SET NULL`|  Imposta i campi figli a `NULL` (solo se `NULLABLE`)|
>>|`CASCADE`| Aggiorna automaticamente i valori anche nella tabella figlia|
>



#### Combinazione tra il `ON DELETE` e `ON UPDATE`

Per rendere il comportamento del database **più modulare e flessibile**, è possibile **combinare** le clausole `ON DELETE` e `ON UPDATE` all'interno della **stessa foreign key**.  
Sebbene queste due azioni **lavorino in modo indipendente**, possono essere definite insieme per coprire **entrambi i casi di aggiornamento e cancellazione**.

![[Combinazione del On Delete e On Update.png]]

Il contesto dell'immagine è il seguente: 
- **Tabella referenziata**: `Riparazione(officina, codice)`
    
- **Tabella figlia (con la foreign key)**: `RicambioRip(officina, rip)`
    
- **Chiave esterna composta**: `(officina, rip)` → `Riparazione(officina, codice)`
Il vincolo è definito così:
```postgresql
FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice) ON DELETE SET NULL ON UPDATE CASCADE
```

Questa definizione comporta:
1. `ON DELETE SET NULL`:
	==**Se viene eliminata una riga** dalla tabella `Riparazione` (cioè una chiave primaria `(officina, codice)`), allora tutte le righe della tabella `RicambioRip` che fanno riferimento a quella combinazione verranno automaticamente **aggiornate**:  
	i campi `officina` e `rip` verranno impostati a `NULL`.==   
	
	Questa strategia evita errori e mantiene la **coerenza referenziale**, anche se le tuple risultanti in `RicambioRip` rimarranno orfane (ma valide).
	
2. `ON UPDATE CASCADE`:
	==**Se viene modificato uno dei valori della chiave primaria** della tabella `Riparazione`, il DBMS **propaga automaticamente l’aggiornamento** alle tuple della tabella `RicambioRip` che referenziano quella chiave.==   
	In questo modo si **evita la perdita di riferimenti**, aggiornando coerentemente le ennuple figlie.

Quindi da questa immagine possiamo vedere come:
**Le azioni `ON DELETE` e `ON UPDATE` sono indipendenti e si possono combinare** sulla stessa foreign key.

Questa possibilità quindi ci consente di:

- Gestire **la cancellazione** del record padre → i riferimenti nella tabella figlia vengono **azzerati** (`NULL`);
    
- Gestire **l’aggiornamento** del record padre → i riferimenti nella tabella figlia vengono **aggiornati coerentemente** (`CASCADE`);
    

> [!done] Questo approccio è particolarmente utile quando:
> 
> - le ennuple figlie **dipendono logicamente dalla tupla padre**,
>     
> - si vuole **automatizzare** la gestione delle modifiche senza violare i vincoli di integrità.
>


> [!caution] **Nota importante**
> Affinché `ON DELETE SET NULL` funzioni, è **obbligatorio** che i campi `officina` e `rip` nella tabella `RicambioRip` **siano `NULLABLE`** (cioè **non devono avere il vincolo `NOT NULL`**).  
>In caso contrario, il DBMS **rifiuta l’eliminazione** della tupla padre perché non può impostare i campi a `NULL`.

Quindi la combinazione `ON DELETE SET NULL ON UPDATE CASCADE` offre un **controllo granulare** su come si propagano le modifiche nel database, mantenendo l’integrità referenziale in scenari complessi e riducendo la necessità di interventi manuali o trigger.


