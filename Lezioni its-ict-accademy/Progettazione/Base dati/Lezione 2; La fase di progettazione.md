# Introduzione
In questo momento ci troviamo nella [[Lezione 1; Introduzione e modello relazionale#Fase di progettazione|fase di progettazione]], come abbiamo già visto nella scorsa lezione possiamo suddividere in varie fasi il percorso fatto e quello ancora da fare:
### 1. Analisi concettuale 
Lo scopo è comprendere e modellare i requisiti informativi del dominio applicativo, producendo uno **schema concettuale** ad alto livello, indipendente dal DBMS.
**Output:**

-  Diagramma UML concettuale delle classi
    
-  Specifiche dei tipi di dato
    
-  Specifiche delle classi
    
-  Specifiche dei vincoli esterni
    
-  Diagramma UML concettuale degli _use-case_
    
-  Specifiche concettuali degli _use-case_

### 2. Progettazione Logica (o ristrutturazione concettuale)
In questa fase ==si **traduce e ristruttura** lo schema concettuale per ottenere una struttura più adatta a un **modello relazionale**, tenendo conto dei vincoli e dei requisiti di performance.==
Gli obiettivi di questa fase sono:
- Ristrutturazione UML delle classi e degli use-case
    
- Scelta dei **domini SQL** per ogni tipo di dato concettuale
    
- Definizione di **tutti i vincoli** derivati dallo schema UML

### 3. Traduzione diretta → Schema concettuale relazionale
Si procede alla **traduzione dello schema ristrutturato** in uno **schema relazionale**, pronto per essere implementato in SQL.
**Output:**
- Schema relazionale in SQL
    
- Definizione delle **foreign key, vincoli, chiavi primarie**, tipi di dato, ecc.

### 4. Progettazione delle operazioni
In questa fase si progettano le operazioni realizzative sia a livello di:
- **Use-case** (interazioni dell’utente col sistema)
    
- **Operazioni di classe** (metodi associati alle entità)

**Output:**

- Specifiche operative per la realizzazione in SQL (query, trigger, viste, stored procedure, ecc.).

Per riassumere: 
```plain text
Analisi concettuale
(UML + Specifiche)
         ↓
Progettazione logica
(Ristrutturazione UML + Vincoli + Domini SQL)
         ↓
Traduzione diretta
(Schema relazionale in SQL)
         ↓
Progettazione delle operazioni
(Specifiche realizzative in SQL)
```

Per essere chiari  adesso siamo ancora in fase di ristrutturazione, dopodiché si passerà alla fase di traduzione diretta.


### Produzione dello schema relazionale da schema concettuale
==L'obiettivo di questa fase è **generare lo schema relazionale** (comprensivo di vincoli) a partire dallo **schema concettuale UML** dell'applicazione.==
- Input:

	- Diagramma UML concettuale delle classi
    - Attributi
    - Associazioni (incluse le _association class_)
    - Gerarchie di generalizzazione/specializzazione (`is-a`)
    - Vincoli di identificazione
    - Vincoli esterni
- Output: Un insieme di **relazioni** (tabelle) con i relativi **vincoli di integrità**.

Per comprendere meglio l'obiettivo di questa fase guardiamo l'esempio che segue:
![[Esempio1.png]]

Nel diagramma sono presenti:

- Due **classi**: `Studente` e `Corso`
    
- Un'[[Associazioni con attributi in UML#Le association class|association class]]: `esame`, dotata dell’attributo `data:Date`
- L’associazione tra `Studente` e `Corso` è arricchita da vincoli di molteplicità su entrambi i lati:

	- **Dal lato `Studente`**: la molteplicità `0..*` indica che **uno studente può sostenere zero o più esami**, quindi può essere associato a più corsi, oppure a nessuno.
    
	- **Dal lato `Corso`**: la molteplicità `0..*` indica che **un corso può essere seguito da zero o più studenti**, quindi può non avere studenti associati o essere frequentato da molti.
    

In sintesi, l’associazione rappresenta una **relazione molti-a-molti (n:m)** tra le classi `Studente` e `Corso`, e l’attributo `data` presente nell’association class `esame` rappresenta un'informazione legata **all’evento stesso dell’esame** (ovvero _quando_ uno studente ha sostenuto un determinato corso).

In questo esempio:

- Il **progettista** decide che le **istanze** delle classi `Studente`, `Corso` e dell’associazione `esame` debbano essere **memorizzate nel database**.
    
- Decide inoltre che **ogni istanza di classe o associazione** venga rappresentata come **un’[[Lezione 1; Introduzione e modello relazionale#^ennuple|en­nupla]]** (riga) in una tabella.
Di conseguenza il progettista definisce il seguente schema relazionale con vincoli per il DB:
- Tabella `Studente`

```plain
Studente(matricola: integer, nome: varchar)
```

L'[[Lezione 1; Introduzione e modello relazionale#^colonna|attributo]] `matricola` è la [[Lezione 1; Introduzione e modello relazionale#Chiavi e valori `null`|chiave primaria]].

-  Tabella `Corso`
```plain
Corso(nome: varchar)
```

L'[[Lezione 1; Introduzione e modello relazionale#^colonna|attributo]] `nome` è la [[Lezione 1; Introduzione e modello relazionale#Chiavi e valori `null`|chiave primaria]].

- Tabella `esame`
```plain
esame(studente: integer, corso: varchar, data: date)
```
- `studente` è una **[[Lezione 1; Introduzione e modello relazionale#I vincoli foreign key (integrità referenziale)|foreign key]]** → `Studente(matricola)`
    
- `corso` è una **[[Lezione 1; Introduzione e modello relazionale#I vincoli foreign key (integrità referenziale)|foreign key]]** → `Corso(nome)`.

```plain
foreign key: studente references Studente(matricola)

foreign key: corso references Corso(nome)
```

In conclusione questo schema relazionale rappresenta alla perfezione il diagramma UML concettuale delle classi riportato sopra:
- La classe `esame` è stata tradotta in una **tabella indipendente**, in quanto rappresenta un’associazione n:m con attributi (→ _association class_).

- La **correttezza semantica** delle relazioni è mantenuta tramite le foreign key, che garantiscono **l'integrità referenziale** tra `esame` ↔ `Studente` e `esame` ↔ `Corso`.
Difatti la prima foreign key fa **riferimento** al campo `matricola` della tabella `Studente`, che è una **primary key**.
Questo vincolo ==**impone che ogni valore di `studente` presente in `esame` esista già nella tabella `Studente`**.==  
**In altre parole:** ==non si può registrare un esame per uno studente che **non è presente** nella tabella `Studente`.==

Mentre la seconda foreign key fa riferimento al campo `nome` della tabella `Corso`, che è la **primary key**:
- ==Questo vincolo impone che ogni valore del campo `corso` in `esame` **esista già** come `nome` in `Corso`.==

- In altre parole: ==non è possibile registrare un esame per un corso che non esiste nella tabella `Corso`.==

- Il campo `corso` nella tabella `esame` deve quindi contenere solo valori che sono già presenti nel campo `nome` della tabella `Corso`.  
  
==Questo garantisce l’**integrità referenziale** tra la tabella `esame` e la tabella `Corso`, assicurando che ogni esame faccia sempre riferimento a un corso effettivamente esistente nel sistema==.

Tuttavia esaminiamo un caso leggermente più complesso:
![[Esempio2.png]]

Nel diagramma sono presenti:

- Due **classi**: `Studente` e `Corso`
    
- Un'[[Associazioni con attributi in UML#Le association class|association class]]: `insegna`, dotata dell’attributo `da: Date`
- L'associazione tra `Studente` e `Corso` è arricchita da vincoli di molteplicità `1..*` su entrambi i lati:
	- Dal lato **Lato `Docente`**:  
		 -   la molteplicità `1..*` indica che: 
			 - ==**ogni docente deve insegnare ad almeno un corso**, quindi ogni docente può essere associato ad almeno un corso.==
		   
	- **Dal lato `Corso`**: la molteplicità `1..*`:
		- indica che: 
			- ==**almeno un corso deve essere insegnato da almeno un docente**, quindi ogni corso può essere associato ad almeno un docente.==

In sintesi, l’associazione rappresenta una **relazione molti-a-molti (n:m):**
	tra le classi `Studente` e `Corso`, e l’attributo `data` presente nell’association class `esame` rappresenta un'informazione legata **all’evento stesso dell’esame** (ovvero _quando_ uno studente ha sostenuto un determinato corso).

**Decisioni progettuali:**

Il progettista decide che:

- Le istanze di `Docente`, `Corso` e `insegna` **devono essere memorizzate nel DB**.
    
- **Ogni istanza di classe o associazione viene mappata su una ennupla** (riga) di una tabella.

Questo si traduce in schema relazionale:
1.  **Tabella `Docente`**
```plain
Docente(matricola: integer, nome: varchar)
```



In questo caso, si ha un **[[#^vincoliDiInclusione|vincolo di inclusione]]** (non una foreign key), derivato dal vincolo di molteplicità `1..*`:

- `matricola` deve comparire (occorre) in `insegna(docente)`.

In altre parole: 
- ==`matricola` deve comparire **in almeno un’en­nupla** del campo `docente` della tabella `insegna`.==

2. **Tabella `Corso`**
```plain
Corso(nome: varchar)
```


Anche in questo caso, si ha **[[#^vincoliDiInclusione|un vincolo di inclusione]]** (non una foreign key), derivato dal vincolo di molteplicità `1..*:`

- `nome` deve comparire (occorre) in `insegna(corso)`.

In altre parole: 
- ==`nome` deve comparire in almeno un’en­nupla del campo `corso` della tabella `insegna`.==

- **Tabella `insegna`** (association class)
```plain
insegna(docente:integer, corso:varchar, da:Date)
```

In queste tabella la chiave primaria e composita: è formata dai due campi `docente` e `corso`. 

Le Foreign Key sono: 
```plaintext
foreign key: docente references Docente(matricola)
foreign key: corso references Corso(nome)
```

- **Foreign Key** `docente` → `Docente(matricola)`
    - Il campo `docente` nella tabella `insegna` è **una chiave esterna** (foreign key) che **fa riferimento alla chiave primaria** `matricola` della tabella `Docente`.
    
	- In pratica:
		- ==ogni valore presente in `insegna.docente` deve già esistere nella colonna `matricola` della tabella `Docente`.==
    
	- ==Questo garantisce che **non si possano inserire righe nella tabella `insegna` con un docente che non esiste** nella tabella `Docente`.==
	
- **Foreign Key** `corso` → `Corso(nome)`
	-  Il campo `corso` nella tabella `insegna` è **una chiave esterna** che **fa riferimento alla chiave primaria** `nome` della tabella `Corso`.
    
	- ==Questo vincolo impone che **ogni valore inserito in `insegna.corso` debba già esistere nella tabella `Corso.nome`**.==


> [!NOTE] **Nota: Vincoli di inclusione**
> I **vincoli di inclusione** su `Docente` e `Corso` non sono implementati come foreign key, poichè sono: 
> - ==vincoli esterni **di partecipazione obbligatoria**, imposti dalla molteplicità `1..*` nel modello UML.==  
>In altre parole: 
>- ==ogni docente e ogni corso **devono comparire almeno una volta nella tabella `insegna`**, affinché il modello rispetti le cardinalità definite nello schema concettuale==.  ^vincoliDiInclusione


---

### Perché è necessaria una ristrutturazione prima della traduzione
Una volta definito il **diagramma UML concettuale delle classi**, ci si trova spesso di fronte a **modelli ricchi di costrutti complessi**, tra cui:
- **Attributi multivalore**
    
- **Gerarchie is-a**, con generalizzazioni:
    
    - **disgiunte / non disgiunte**
        
    - **complete / non complete**
        
- **Vincoli concettuali di alto livello (partecipazione, identificazione, ecc.).**

Scrivere direttamente lo schema relazionale a partire da questi diagrammi concettuali è rischioso e soggetto a errori.

> [!warning] **Attenzione:**
> **Scrivere direttamente lo schema relazionale a partire da questi diagrammi concettuali è altamente rischioso**:  
> si possono introdurre **errori di progettazione**, **perdita di informazione**, o vincoli **non rappresentati correttamente**.

Per questo motivo si adotta una **metodologia robusta e scalabile**, articolata in due fasi principali:
1. **Ristrutturazione dello schema concettuale:**
   A partire dal **diagramma concettuale UML iniziale**, il progettista:

	- **Produce un nuovo diagramma delle classi ristrutturato**
    
	- Redige **nuove specifiche ristrutturate**:
    
	    - delle classi
        
	    - degli use-case
        
	    - dei tipi di dato
        
	    - dei vincoli esterni
        
L' **Obiettivo della ristrutturazione** è:  
==Adattare lo schema concettuale alle **tecnologie scelte per l’implementazione**, mantenendo intatta la **capacità rappresentativa del modello (equivalenza estensionale)**==.

In particolare, **se si adotta una tecnologia basata su basi di dati relazionali**:

- ==Lo schema ristrutturato **definisce quali classi saranno effettivamente memorizzate nel DB**==.
    
- Contiene solo **costrutti semplici e direttamente implementabili**:
    
    - ==classi==
        
    - ==associazioni==
        
    - ==attributi con tipi di dato SQL (base o definiti dal progettista)==
        
    - ==molteplicità massima **pari a 1**==
        
- Tiene conto anche di ==**requisiti di performance** (efficienza dell’accesso ai dati, ridondanza controllata, ecc.)==
    

2. **Traduzione diretta:**
   Una volta ottenuto lo **schema ristrutturato**, si può procedere alla **traduzione diretta**, ovvero:

	- Si procede alla **generazione dello schema relazionale** vero e proprio, tenendo conto di:

		- ==vincoli di integrità (PK, FK, vincoli esterni)==
    
		- ==requisiti di efficienza==
    
		- ==eventuali regole di derivazione, trigger, ecc.==
  

> [!example] In sintesi:  
> La **ristrutturazione** è un passaggio **intermedio ma cruciale**, che consente di passare in modo **corretto, coerente e sistematico** da un modello concettuale complesso a uno **schema relazionale ben progettato**.


---

### Obiettivo della Ristrutturazione: _una semplificazione mirata alla realizzazione_

In questa fase, l’obiettivo è:

> ✅ **Trasformare la porzione del diagramma UML concettuale delle classi** (contenente **classi** e **associazioni** le cui istanze devono essere memorizzate nel database)  
> 🔁 in **un nuovo diagramma delle classi equivalente**, ma con una **struttura compatibile con la derivazione diretta dello schema relazionale**.

In altri termini, ==**la ristrutturazione** ha lo scopo di **preparare il modello concettuale alla fase di traduzione diretta**, semplificando la struttura del diagramma senza alterarne il significato informativo.==



#### Metodo adottato: sequenza ordinata di trasformazioni

La metodologia prevede una **sequenza precisa di passi**, che **devono essere seguiti nell’ordine indicato**.

> 📌 Alcuni passi presentano **varie opzioni**, da scegliere **caso per caso** in base a:
> 
> - requisiti applicativi
>     
> - vincoli logici
>     
> - **performance attese** (es. query frequenti, dimensioni delle tabelle, accessi ottimizzati)
>     



#### I 6 passi della Ristrutturazione

1. **[[#Eliminazione di attributi multivalore|Eliminazione degli attributi multivalore]]**  
    ==Gli attributi che ammettono più valori devono essere trasformati in **nuove classi** o **associazioni**, per rispettare la natura relazionale del modello finale.==
    
2. **[[#Scelta dei tipi di dato|Sostituzione dei tipi di dato concettuali]]**  
    Ogni tipo concettuale viene sostituito con un tipo **supportato dal DBMS**:
    
    - Tipo base SQL (es. `VARCHAR`, `INTEGER`, `DATE`)
        
    - Tipo definito dal progettista, se necessario (es. `CHECK`, `ENUM`, domini)
        
3. **[[#1. **Generalizzazioni tra classi**|Eliminazione delle generalizzazioni tra classi]]**  
    Le gerarchie `is-a` devono essere risolte in una struttura equivalente, attraverso:
    
    - ==Ereditarietà per sovrapposizione== (`single table`)
        
    - ==Suddivisione in più tabelle== (`multiple table`)
        
    - Strategie miste (in base alla **completezza/disgiunzione** cioè `{disjoint, complete}`)
        
4. **[[#2. **Generalizzazioni tra associazioni**|Eliminazione delle generalizzazioni tra associazioni]]**  
    ==Le relazioni ereditarie tra **association class** vanno appiattite e trasformate in nuove entità o associazioni con vincoli logici equivalenti.==
    
5. **Definizione di un identificatore per ogni classe**  
    ==Ogni classe deve disporre di un identificatore univoco (una **chiave candidata**), necessario per referenziare correttamente le istanze nelle relazioni.==
    
6. **Selezione di un identificatore primario**  
    ==Tra le chiavi candidate individuate, se ne seleziona **una** da utilizzare come **primary key**, ovvero l’identificatore ufficiale della tabella corrispondente.== 
    


> [!warning] **Importante:**  
> Il diagramma ristrutturato, **dal punto di vista concettuale, è di bassa qualità**:  
> perde l’eleganza e l’espressività del modello UML originale.

 **Ma questo non è un problema!**  
==La ristrutturazione **non ha lo scopo di comunicare o modellare**, bensì di **preparare un artefatto intermedio**, uno **schema tecnico “semilavorato”**, **funzionale alla generazione corretta e diretta dello schema relazionale del DB.**==



### Eliminazione di attributi multivalore
In questa sottofase della ristrutturazione, l’obiettivo è trasformare il diagramma UML concettuale delle classi in un modello equivalente che **non contenga attributi multivalore**, poiché questi non sono supportati dai DBMS relazionali.

La metodologia adottata prevede di:

==creare una nuova classe le cui istanze rappresentano i valori effettivamente utilizzati a livello di oggetti e di link, corrispondenti all’attributo multivalore.==

Vediamo 2 esempi:
1. Esempio classico con attributi multivalore di una classe:

![[Eliminazione attributi multivalore.png]]

Nell’immagine proposta, sulla sinistra è rappresentata la classe `Studente`, con i seguenti attributi:

- `matricola: intero {id}` (identificatore univoco)
    
- `nome: stringa`
    
- `email: stringa [x..y]`: 

	- ==l’indicazione `[x..y]` rappresenta il vincolo di molteplicità che rende `email` un attributo multivalore.==

[[Eliminazione attributi multivalore.png|Sulla destra]]: 
osserviamo come l’attributo multivalore `email` sia stato trasformato in una classe vera e propria, denominata `IndirizzoEmail`, con un attributo `valore: stringa {id}`, che funge da identificatore dell’istanza (questo perché non vogliamo rappresentare nel DB più volte la stessa istanza del tipo). 
Inoltre, i vincoli di molteplicità associati alle classi giocano un ruolo fondamentale nella corretta rappresentazione del modello:

- **Lato `Studente`**, ==il vincolo `1..*` impone che ciascun studente sia associato ad almeno un indirizzo email, garantendo così che il database memorizzi solo indirizzi email effettivamente collegati a studenti.==  
    - ==_Si sottolinea che il vincolo `1..*` deve sempre essere applicato in questi casi._==
    
- **Lato `IndirizzoEmail`**: 
	- ==si mantiene la molteplicità originaria dell’attributo concettuale `[x..y]`, che definisce il numero minimo e massimo di studenti associabili allo stesso indirizzo email.==

2. **Eliminazione degli attributi multivalore di associazione**
![[eliminazione degli attributi multivalore di associazione.png]]

Nell’immagine a destra si osservano due classi e una association class:
1. Classe `Studente`:
	- con attributo `matricola:intero{id}`
	- con attributo `nome:stringa`
2. association class `esame`:
	
	- attributo multivalore `data: Data [x..y]`
	
	- attributo`voto: 18..31`. 
	
3. La classe `Corso`:
	- con attributo `nome:stringa{id}` 
	  
I vincoli di molteplicità tra le classi e l’association class sono `0..*` su entrambi i lati.

Come si nota, l’attributo `data` di `Esame` è un attributo multivalore, a causa del vincolo di molteplicità `[x..y]`. 
Perciò, nel diagramma ristrutturato a destra, l’attributo `data: Data [x..y]` viene trasformato in una classe autonoma chiamata `DataProva`, con attributo `data: Data {id}`, e partecipa a un link di associazione `esame_prova` con molteplicità `1..*` verso `esame` ed `esame` partecipa ad un link di associazione `esame_prova` con un vincolo di `[x..y]` (cioè la cardinalità che prima faceva parte dell'attributo `data`.

==La molteplicità `1..*`, [[Eliminazione attributi multivalore.png|come nell'esempio precedente]], impone che il database memorizzi solo le date effettivamente associate ad almeno un esame, garantendo l’integrità e la coerenza dei dati.==

Parallelamente, l’association class `esame` mantiene il proprio ruolo nel modello, partecipando a un link di associazione con `DataProva` con molteplicità che riflette quella originaria dell’attributo multivalore `data: Data` nel diagramma concettuale delle classi.


Al termine del passo di eliminazione degli attributi multivalore tutti gli attributi del diagramma ristrutturato dovranno avere vincoli di cardinalità `[0..1]` oppure `[1..1]`.


### Scelta dei tipi di dato
Analogamente a quanto avviene nella ristrutturazione di un diagramma delle classi in Python, anche nel contesto della progettazione di basi di dati è necessario trasformare il **diagramma UML concettuale delle classi** in uno **equivalente**, in cui **tutti gli attributi siano espressi tramite tipi di dato (domini) supportati dal DBMS**.
**Obiettivo:**  
==Ottenere uno **schema ristrutturato** in cui **tutti gli attributi** siano associati a **tipi di dato supportati** dal sistema di gestione del database relazionale (in questo caso, PostgreSQL).==

#### Cosa si deve fare 
Per **ogni attributo** del modello concettuale:

-  Occorre **scegliere un tipo SQL compatibile** tra quelli di base offerti dal DBMS
    
-  Oppure **definire un nuovo tipo personalizzato** ([[#2. **Tipi concettuali specializzati→ Domini Specializzati**|dominio]] o [[#2. **Tipi concettuali specializzati→ Domini Specializzati**|tipo composito]]), qualora il tipo concettuale non sia direttamente mappabile

###### 1. **Tipi concettuali di base**

Esempi:

- `intero`, `reale`, `stringa`, `Data`, `Ora`, `DataOra`  
    Corrispondenti tipi SQL standard (PostgreSQL):
    
- `integer`, `real`, `varchar(n)`, `date`, `time`, `timestamp`, ecc.  
    

Riassumendo:

| Tipo concettuale | Tipo SQL (PostgreSQL)      |
| ---------------- | -------------------------- |
| `intero`         | `INTEGER`                  |
| `reale`          | `REAL`, `NUMERIC`, `FLOAT` |
| `stringa`        | `VARCHAR(n)`, `TEXT`       |
| `Data`           | `DATE`                     |
| `Ora`            | `TIME`                     |
| `DataOra`        | `TIMESTAMP`                |
>Riferimento: [PostgreSQL - Documentazione tipi di dato](https://www.postgresql.org/docs/current/datatype.html)

###### 2. **Tipi concettuali specializzati→ Domini Specializzati**
Quando un tipo concettuale ha **restrizioni aggiuntive** (intervalli, vincoli semantici), è possibile creare **domini SQL personalizzati.** 
Alcuni esempi possono essere:

- `intero > 0` →
```postgresql
CREATE DOMAIN Int_gz AS INTEGER CHECK (VALUE > 0);
```

- `reale ≤ 0`, quindi tra intervalli numerici (`x..y`), ecc.
```postgresql
CREATE DOMAIN Voto AS REAL CHECK (VALUE BETWEEN 18 AND 30);
```

In sostanza bisogna definire di **domini personalizzati** con vincoli di controllo.

###### 3. Tipi enumerativi
Per attributi concettuali che assumono **un insieme finito di valori**, è possibile utilizzare gli **ENUM**:

- Tipo concettuale `Genere` che comprende un insieme di valori come `{maschio, femmina}`
```postgresql
CREATE TYPE Genere AS ENUM ('M', 'F');
```

- Oppure tipo concettuale `Ruolo` che comprende un insieme di valori come `{direttore, progettista, analista, programmatore}`
```postgresql
CREATE TYPE Ruolo AS ENUM ('direttore, progettista, analista, programmatore')
```
In sostanza si va a  definire nuovi tipi di dato supportati dal DBMS usando SQL: `CREATE TYPE … AS ENUM(...)` 

- Oppure per il tipo concettuale `Voto`:
```postgresql
CREATE DOMAIN Voto AS Integer
	CHECK (value >= 18 and value <= 31);
```

###### 4. Tipi concettuali composti:  
Per rappresentare tipi concettuali **strutturati** (es. `Indirizzo`, `Periodo`, `Intervallo`, ecc.), è possibile definire **nuovi tipi composti** in PostgreSQL mediante:
```postgresql
CREATE TYPE Indirizzo AS (
    via VARCHAR,
    civico INTEGER,
    cap CHAR(5),
    citta VARCHAR
);
```
In sostanza si va a definire nuovi tipi di dato supportati dal DBMS usando SQL: `CREATE TYPE … AS (…)` 
>==In questo modo si ottiene un **tipo strutturato** che può essere usato come tipo di attributo all’interno delle tabelle relazionali.==

##### Problema: assenza di vincoli nei tipi composti
Tuttavia, questo approccio **presenta un limite importante**:  
**PostgreSQL non permette di specificare vincoli** (es. `NOT NULL`, `CHECK`, ecc.) **direttamente nei singoli campi di un tipo composto**.
Tentativi come il seguente:
```postgresql
CREATE TYPE Indirizzo AS (
    via VARCHAR(100) NOT NULL,
    civico INTEGER NOT NULL CHECK (VALUE > 0)
);

```
==**generano errore di sintassi**, in quanto **i vincoli sono ammessi solo a livello di dominio o tabella**, non all'interno dei tipi composti.==


> [!abstract]- **Perché PostgreSQL non permette l’uso diretto di vincoli (`NOT NULL`, `CHECK`, ecc.) dentro i tipi composti definiti con `CREATE TYPE`?**
>
 >Perché i **tipi composti** (definiti tramite `CREATE TYPE`) non sono progettati per **applicare vincoli di validazione sui singoli campi**, ==ma esclusivamente per **descrivere la struttura** dei dati, ovvero la loro **forma**, non il loro **comportamento vincolato**.==
>
>Da un punto di vista tecnico, il comando `CREATE TYPE ... AS (...)` serve a definire **tipi di dato strutturati** (simili a [[Collections#Tuple|tuple]]), utili ad esempio per:
>
>- ==Parametri e valori di ritorno nelle funzioni SQL/PLpgSQL==
 >   
>==- Colonne composite nelle tabelle==
  >  
>==- Variabili nei blocchi di codice procedurale==
 >   
>
> **Tuttavia, non è concepito per gestire vincoli logici o di integrità**: 
> - ==i campi di un tipo sono "nudi", ovvero privi di qualsiasi controllo.== 
> ==- La responsabilità della validazione ricade **sulle tabelle** o **sui domini** che lo impiegano==.
 >
 >Inoltre un altro motivo è la **separazione delle responsabilità:**
 >In PostgreSQL — come nei DBMS in generale — vige una **chiara separazione dei compiti**: 
 >
 > `TYPE`: ==Descrive la struttura (nome e tipo dei campi).==
 > `DOMAIN`: ==Definisce vincoli su un singolo valore.==
 > `TABLE`: ==Applica vincoli su intere tuple e colonne specifiche.==
 > 
 > Questa distinzione consente:
 > - **Riutilizzabilità** del tipo senza forzare vincoli fissi.
 > - **Maggiore flessibilità**: **Maggiore flessibilità**, poiché uno stesso tipo può essere utilizzato in più contesti, ciascuno con vincoli specifici.
 >  
 > Le conseguenze pratiche sono che, difatti, non è possibile inserire il vincolo `NOT NULL` ovunque perché PostgreSQL **non sa** dove il tipo verrà usato e di conseguenza non può garantire che questo vincolo abbia senso ovunque nel codice.
 > Ad esempio:
>```postgresql
 > CREATE TYPE Persona AS (
  nome VARCHAR NOT NULL  -- ❌
);
>
>```
>Genera un errore perché **PostgreSQL non può garantire che il vincolo `NOT NULL` sia valido in ogni contesto**.  
Ad esempio:
>
>- Cosa succede se `Persona` è usato come parametro di una funzione?
 >   
>- Cosa accade se viene usato in una colonna che può ammettere valori `NULL`?
 >   
>
>==Per evitare **ambiguità semantiche** e **comportamenti incoerenti**, PostgreSQL **non consente l’inserimento di vincoli all’interno della definizione di un tipo composto**.==
>>[!example] **Analogia**
>>Immagina i **tipi** come **stampini per biscotti**: definiscono la **forma** del biscotto (es. rotondo, a stella...).
>>
>>I **vincoli**, invece, sono come le **regole in cucina**: “cuocere per 10 minuti”, “non usare zucchero”, ecc.
>>
>> Non ha senso codificare le regole dentro lo stampo: le **applichi quando usi lo stampo**, non nello stampo stesso.


##### Soluzione: definire **domini ausiliari** con vincoli
Per applicare **vincoli semantici ai campi** di un tipo composto, è necessario **definire prima dei domini SQL**, ovvero **tipi derivati** dotati di `CHECK`, `NOT NULL`, ecc.

```postgresql
CREATE Domain String100_not_null AS varchar(100)
	CHECK (value IS NOT NULL);
	
CREATE DOMAIN Int_gz_not_null AS Integer
	CHECK (value IS NOT NULL and value > 0);
	
CREATE TYPE Indirizzo (
	via String100_not_null,
	civico Int_gz_not_null
);
```

>==In questo modo si riesce a ottenere un tipo strutturato **con vincoli forti su ogni campo**, superando il limite sintattico di PostgreSQL.==

In conclusione:
==La costruzione di **tipi composti robusti** in PostgreSQL **richiede la definizione di domini ausiliari**, per poter garantire la correttezza semantica e l’integrità dei dati.==

Questo approccio è particolarmente utile ==quando si vogliono modellare concetti complessi come `Indirizzo`, `Intervallo`, `PersonaFisica`, ecc., **riutilizzabili** come tipi di attributo all'interno di più tabelle, **senza duplicare la logica di controllo**.==

Al termine del passo di definizione della corrispondenza dei tipi di dato concettuali in tipi supportati dal DBMS, tutti gli attributi del diagramma ristrutturato sono semplici, hanno un dominio supportato dal DBMS ed hanno vincoli di cardinalità `[0..1]` oppure `[1..1]`.


---

## Le generalizzazioni
Nel contesto dei database relazionali, **il concetto di ereditarietà non ha una controparte diretta**.

> In altre parole: **non ha senso dire che “una tabella è anche un’altra tabella”**.

Nel modello a oggetti (come in UML o in Python) le **sottoclassi** ereditano attributi e operazioni dalla **superclasse**.  
Nel modello relazionale, invece, una ==**tabella rappresenta una sola entità ben definita**.==  
==Non esiste quindi un meccanismo naturale per esprimere **relazioni `is-a`** (generalizzazioni/specializzazioni) nel linguaggio SQL.==


Per questo motivo, in fase di **ristrutturazione** dello schema concettuale, le generalizzazioni **vanno eliminate**, ovvero **trasformate in costrutti equivalenti** e implementabili nel modello relazionale.
### Metodo di ristrutturazione delle generalizzazioni

Il progettista deve analizzare ogni livello di generalizzazione presente nel diagramma concettuale e decidere, **caso per caso**, quale delle seguenti strategie adottare:

###### 1. **Generalizzazioni tra classi**

Per ogni relazione `is-a` tra classi (es. `Persona` con sottoclassi `Studente`, `Docente`, ecc.), sono disponibili **tre possibili tecniche**:

1.  **Fusione** delle sottoclassi nella superclasse
    
    > ==Si incorporano gli attributi specifici delle sottoclassi all'interno della superclasse, aggiungendo eventualmente un **attributo discriminante**.==  
    > ==È l’approccio **più semplice e universalmente applicabile**.==  ^primoMetodo
    
2.  **Divisione** della superclasse in più tabelle disgiunte
    > ==Ogni sottoclasse diventa una tabella indipendente con tutti gli attributi, inclusi quelli ereditati.==  
    > ==L’implementazione si basa sulla **disgiunzione** tra le sottoclassi.==  ^secondoMetodo
    
3.  **Sostituzione** della generalizzazione con un’associazione
    > ==Si elimina il legame `is-a` e si rappresentano i collegamenti con **foreign key** e **relazioni tra tabelle**.==    ^terzoMetodo
    

###### 2. **Generalizzazioni tra associazioni**

In modo analogo alle classi, le **relazioni `is-a` tra associazioni** (association class) devono essere gestite con:

- 🔁 **Fusione** delle sotto-associazioni nella super-associazione, **se coerente con le modifiche precedenti**
    
- ⚠️ **Aggiunta di vincoli esterni** per mantenere la semantica originale della generalizzazione (vincoli che verranno gestiti successivamente)
    

> [!important]  **Nota operativa:**  
> Il primo approccio, ovvero **la fusione delle sottoclassi nella superclasse**, è la **tecnica più generale** e può essere **applicata in qualsiasi situazione**.  
> È quindi **il primo tentativo da considerare** nel processo di ristrutturazione delle generalizzazioni

Quindi esistono vari modi per ristrutturare le generalizzazioni e come nella [[Ristrutturazione di generalizzazioni|ristrutturazione delle generalizzazioni in Python]] vi sono vari casi di come ristrutturarle, tenendo anche conto dei vincoli `{disjoint}`, `{complete}` e `{disjoint,complete}`.

### 1. [[#^primoMetodo|Fusione delle classi]] 
Come nella [[Ristrutturazione di generalizzazioni|ristrutturazione delle generalizzazioni in Python]] il metodo della fusione ingloba le sottoclassi nella superclasse ma **preservando le differenze semantiche** tra le sottoclassi mediante:
- ==Aggiunta di un tipo enumerato che distingue le istanze tra loro (in Python avevamo aggiunto flag booleani)==
- ==Inclusione degli attributi delle sottoclassi nella superclasse aggiungendo vincoli sugli attributi che segnalano che solo le istanze del tipo corrispondente valorizzano l'attributo (es: `[0..1]`).==
- ==Rilassamento delle molteplicità minime nelle associazioni che coinvolgono le sottoclassi inglobate dalla classe padre== 
#### Caso 1: ristrutturazione con la fusione senza vincoli.

L'approccio in questo caso è quello di fondere un intero livello della generalizzazione (ovvero fondere le sottoclassi con la superclasse) in un'unica classe.
![[Fusione senza vincoli.png]]
###### Spiegazione:
**A destra** dell'immagine possiamo vedere tre classi:
1. la classe `Persona`, con gli attributi:
	-  `nome:varchar(100)`
	- `genere:Genere`(di tipi `ENUM`)
2. La classe `Studente`, con attributo:
	- `matricola:varchar(12)`
3. La classe `CorsoDiLaurea`, con attributo:
	- `nome:varchar(100)`
Tra la classe `Persona` e la classe `Studente` vi è una relazione is-a, quindi:

>==uno studente è anche una(`is-a`) persona, ma una persona non è uno studente.==

L'associazione `iscritto` tra `Studente` e `CorsoDiLaurea` è arricchita con i vincoli di molteplicità: 
Uno studente partecipa al link di associazione `iscritto` con molteplicità `1..1`, e un corso di laurea partecipa al link di associazione `iscritto` con molteplicità `0..*` 
Questo sta a significare che: 

> ==A un corso di laurea possono essere iscritti tanti studenti o nessuno, ma uno studente può essere iscritto a un solo corso di laurea.==

Ora come possiamo ristrutturare questo diagramma UML concettuale delle classi?
La risposta si trova a [[Fusione senza vincoli.png|sinistra dell'immagine ]]: 
la classe `Studente` viene fusa con la classe `Persona` a cui si aggiungono altri due attributi:
1. `tipo:Persona`; di tipo `ENUM` con un insieme di valori finiti `'Persona', 'Studente'`.

```postgresql
CREATE TYPE TipoPersona AS ENUM ('Persona', 'Studente');
```


> [!NOTE] **Nota**
> Questo tipo di dato serve per distinguere le istanze di `Persona`, difatti agisce da discriminatore


2. Si aggiunge anche l'attributo `matricola:varchar(12)` di `Studente` con molteplicità `[0..1]`.
3. Inoltre l'associazione `iscritto` adesso è solo tra la classe `Persona` e la classe `CorsoDiLaurea`, con vincoli `0..*` ( sul lato di `Persona`), e `0..1` (sul lato di `CorsoDiLaurea`).

#### La scelta dei vincoli non è casuale
il vincolo `[0..1]` sull'attributo `matricola`, rispecchia perfettamente la generalizzazione poichè come detto prima; 
	uno studente è anche una persona, ma una persona non è anche uno studente.

==Per questo si aggiunge questo vincolo che va ad indicare che una persona può avere o meno un numero di matricola, poiché se lo ha allora è uno studente.==

La stessa logica viene usata per rilassare a zero il vincolo `0..1` sul lato di `CorsoDiLaurea` che prima nel diagramma concettuale era `1..1`:
==non tutte le istanze di `Persona` sono `Studenti`, quindi **non tutte possono partecipare all’associazione `iscritto`**.==
Infatti quel vincolo `0..1` sta proprio a indicare ciò: 
```plain
per ogni p:Persona, p.tipo = 'Studente' se e solo se p è coinvolto in un link di associazione 'iscritto'.
```

##### Interpretazione semantica dei vincoli:
 Quindi una volta fatta la fusione e impostato i vincoli sugli attributi della sottoclasse e sulle associazioni che la coinvolgevano, bisogna anche esplicare i vincoli esterni per specificare il comportamento della generalizzazione ristrutturata,
 ==questo perché I vincoli formali **non possono più essere espressi tramite molteplicità** ma devono essere scritti come **vincoli esterni**==:
 
```plain
Per ogni istanza p di Persona:
	1. p.tipo = ‘Studente’ se e solo se p.matricola è valorizzato
	2. p.tipo = ‘Studente’ se e solo se p è coinvolto in un link “iscritto”
```

###### Spiegazione:

- Il campo `tipo` funge da **discriminante**, distinguendo `Studenti` da altre `Persone`
    
- Se `p.tipo = 'Studente'`, allora:
    
    - `p.matricola` **deve essere valorizzata**
        
    - `p` **deve risultare iscritto a un `CorsoDiLaurea`**
        
- Se `p.tipo ≠ 'Studente'`, entrambi i requisiti **non devono essere soddisfatti.**

#### Caso 2: ristrutturazione di generalizzazioni in caso di sottoclassi disgiunte (`{disjoint}`)
Nel secondo caso, affrontiamo la **ristrutturazione di una generalizzazione tra sottoclassi disgiunte**, ovvero con vincolo `{disjoint}`.

##### Definizione del vincolo `{disjoint}`:

Una generalizzazione `{disjoint}` implica che:

> ==**Un'istanza della superclasse può appartenere ad al più una delle sottoclassi coinvolte (oppure a nessuna).**==

![[Fusione con vincolo {disjoint}.png]]
###### Spiegazione:
A destra dell'immagine abbiamo una generalizzazione tra le sottoclassi `Studente` e `Docente` con `Persona` arricchita con il vincolo [[Generalizzazioni#1. `{disjoint}`|`{disjoint}`]].
Questo sta sta a significare che: 
>Un istanza di `Persona` può essere istanza di `Studente` o istanza di `Docente`, ma non di entrambi.

Gli attributi di queste tre classi sono:
1. La classe `Persona`:
	- `nome:varchar(100)`
2. La classe `Studente`:
	- `matricola:varchar(12)`
3. La classe `Docente`:
	- `nascita:Date`

Queste due sottoclassi sono coinvolte in due associazioni rispettivamente:
1. La sottoclasse `Studente` è coinvolta in una associazione `iscritto` con la classe `CorsoDiLaurea` con vincoli di molteplicità `0..*` (sul lato `Studente`) e `1..1` (sul lato `CorsoDiLaurea`):
> 	Un corso di laurea può essere seguito da tanti studenti o da nessuno.
> 	Uno studente può essere iscritto a un solo corso di laurea.

2. Mentre la la sottoclasse `Docente` è coinvolta in una associazione `afferenza` con la classe `Dipartimento` con vincoli di molteplicità `0..*` (sul lato `Docente`) e `1..1` (sul lato `Dipartimento`):
>	A un dipartimento possono afferire più docenti o nessuno.
>	Un docente può afferire a un solo dipartimento.

Le classi `CorsoDiLaurea` e `Dipartimento` hanno i rispettivi attributi:
- `nome:varchar(100)` 
- `nome:varchar(100)`

Ora come si può trattare la fusione in questo caso?
In realtà dobbiamo agire come nel [[#Caso 1 ristrutturazione con la fusione senza vincoli.|caso 1]] aggiungendo solo alcuni valori e vincoli esterni in più.
Infatti se [[Fusione con vincolo {disjoint}.png|guardiamo l'immagine]] possiamo notare molte similitudine con l'esempio di prima:
1. le sottoclassi sono state fuse con la superclasse a cui si aggiungono 3 attributi in più:
- `tipo:TipoPersona`; in questo caso questo tipo di dato ottiene un terzo valore che è `'Docente'`.

```postgresql
CREATE TYPE TipoPersona AS ENUM ('Persona', 'Studente', 'Docente');
```


> [!NOTE] **Nota**
> Questo tipo di dato serve per distinguere le istanze di `Persona`, difatti agisce da discriminatore


- `matricola:varchar(12)[0..1]`;  attributo di `Studente` a cui viene aggiunto il vincolo `[0..1]`.
- `nascita:Date[0..1]`; attributo di `Docente` a cui viene aggiunto il vincolo `[0..1]`.

Inoltre i vincoli accanto alle classi associate (`CorsoDiLaurea` e `Dipartimento`) sono cambiati da `1..1` a `0..1` proprio per rispettare la generalizzazione concettuale con il vincolo `{disjoint}` :

Avendo usato il metodo della fusione con un vincolo di disgiunzione sulla generalizzazione si deve trovare il modo di indicare che:
**Una persona può essere uno studente o un docente o nessuno dei due.**

Di conseguenza [[#Caso 1 ristrutturazione con la fusione senza vincoli.|come nell'esempio precedente]] nella superclasse viene aggiunto un tipo di dato enumerativo (`tipo:TipoPersona`) che racchiude valori finiti relativi proprio a persona, studente e docente, inoltre gli attributi delle sottoclassi vengono inglobati nella superclasse e vengono aggiunti ad ognuno di essi il vincolo `[0..1]` proprio per indicare che un istanza di `Persona` se è istanza di una di queste sottoclassi allora l'attributo è valorizzato.
Anche i vincoli di molteplicità `0..1` vanno a rispettare la generalizzazione nel diagramma concettuale:
Una persona può partecipare ad almeno un link di associazione `iscritto` con `CorsoDiLaurea` solo se il valore dell'attributo `tipo = 'Studente'`, di conseguenza se `tipo = Persona`  non partecipa a nessun  link di associazione `iscritto` (`0..1`).
Stessa cosa per l'associazione `afferenza`: una persona può partecipare ad almeno un link di associazione `afferenza` solo se il valore dell'attributo `tipo= 'Docente'`. 

##### Vincoli esterni 
Poiché la semantica `{disjoint}` non è esprimibile direttamente nel modello relazionale, è necessario introdurre **vincoli esterni** per garantire la coerenza tra:

- l’attributo `tipo`
    
- gli attributi specifici
    
- la partecipazione ad associazioni

```plain
Per ogni istanza p di Persona:
	1. p.tipo = 'Studente' ⇔ (se e solo se) p.matricola è valorizzato
	2. p.tipo = 'Studente' ⇔ (se e solo se) p è coinvolto in un link "iscritto"
	3. p.tipo = 'Docente' ⇔ (se e solo se) p. nascita è valorizzato 
	4. p.tipo = ‘Docente’ se e solo se p è coinvolto in un link “afferenza”
```


> [!NOTE] **Nota:**
> L’aggiunta dell’attributo `tipo` e l’uso del vincolo `[0..1]` sugli attributi delle sottoclassi permettono di rappresentare in modo coerente la generalizzazione `{disjoint}`.  
>Tuttavia, questo approccio richiede **più vincoli esterni** da mantenere, per assicurare la coerenza semantica tra i dati e la struttura del modello originario.


#### Caso 3: Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte e complete (`{disjoint, complete}`)
Nel terzo caso, affrontiamo la **ristrutturazione di una generalizzazione tra sottoclassi disgiunte e complete**, ovvero con vincolo `{disjoint,complete}`.
n questo scenario trattiamo la ristrutturazione di una generalizzazione caratterizzata da entrambi i vincoli:

- [[Generalizzazioni#^defDisjoint|`{disjoint}`]] → un'istanza può appartenere a **una sola** sottoclasse tra quelle o a nessuna.
    
- [[Generalizzazioni#^defComplete|`{complete}`]] → _tutte_ le istanze della superclasse devono appartenere a **una o più** delle sottoclassi coinvolte.

##### Definizione del vincolo [[Generalizzazioni#^db2378|`{disjoint,complete}`]]:
> Una generalizzazione `{disjoint, complete}` implica che ==**tutte le istanze della superclasse devono appartenere a una e una sola delle sottoclassi** coinvolte.== 

 ![[Fusione con {disjoint,complete}.png]]

###### Spiegazione:
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

Detto questo spostiamo l'attenziona a [[Fusione con {disjoint,complete}.png|destra dell'immagine]]:
La fusione procede come nei casi precedenti, con una differenza fondamentale:  
**le istanze della superclasse devono obbligatoriamente appartenere a una sottoclasse.**
Si aggiunge sempre nella superclasse `Persona`, che ingloba le sottoclassi `Studente` e `Docente` l'attributo `tipo:TipoPersona` che serve sempre per distinguere le diverse istanze di `Persona`.
```postgresql
CREATE TYPE TipoPersona AS ENUM ('Studente', 'Docente');
```


> [!NOTE] **Nota Operativa**
> In questo caso il valore `'persona'` viene escluso perché non esistono persone che non siano almeno uno studente o un docente

Come anche nei casi precedenti gli attributi delle sottoclassi vengono inclusi nella superclasse con molteplicità `[0..1]`:
- `matricola : varchar(12) [0..1]`
    
- `nascita : Date [0..1]`
E anche i vincolo di molteplicità nelle associazioni vengono rilassati a `0..1`.
- `iscritto`: `Persona 0..*` ↔ `CorsoDiLaurea 0..1`
    
- `afferenza`: `Persona 0..*` ↔ `Dipartimento 0..1`

Come per gli altri casi anche qui i vincoli sugli attributi e sulle associazioni devono rispettare il vincolo `{disjoint,complete}` della generalizzazione del diagramma UML:
Assumendo che le istanze di `Persona` devono appartenere obbligatoriamente a una e una sola delle sottoclassi coinvolte, se l'istanza di `Persona` è anche istanza di `Docente` il numero di matricola sarà valorizzato (per le proprietà del vincolo `[0..1]` che rendono l'attributo opzionale)né partecipa al link di associazione `iscritto`  ; viceversa se l'istanza di `Persona` è anche istanza di `Studente` l'attributo `nascita` non sarà valorizzato (per le proprietà del vincolo `[0..1]` che rendono l'attributo opzionale) né partecipa al link di associazione `afferenza`.

##### Vincoli esterni da applicare 
Come negli altri casi la semantica `{disjoint, complete}` non è esprimibile unicamente attraverso la struttura, è quindi necessario introdurre **vincoli esterni** per mantenere la coerenza semantica.

```plain
Per ogni istanza p di Persona:
1. p.tipo = 'Studente' ⇔ (se e solo se) p.matricola è valorizzato
2. p.tipo = 'Studente' ⇔ (se e solo se) p partecipa ad almeno un link “iscritto”
3. p.tipo = 'Docente' ⇔ (se e solo se) p.nascita è valorizzato
4. p.tipo = 'Docente' ⇔ (se e solo se) p partecipa ad almeno un link “afferenza”
```



#### Caso 4: Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte
Affrontiamo ora il caso in cui vi sia una generalizzazione tra classe disgiunte ma senza il vincolo esplicito del `{disjoint}`.


![[Screenshot 2025-07-09 at 12-18-08 Meet - bmb-xnne-ahh.png]]

###### Spiegazione:
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

Qui la situazione cambia perché la differenza con la [[Fusione senza vincoli.png|prima immagine]] è che nel primo caso la generalizzazione comprendeva solo un unica classe padre e una sola classe figlia, mentre qui la generalizzazione comprende due classi figlie ma non è presente il vincolo `{disjoint}` in maniera esplicita.
Tuttavia si ha la necessita di differenziare le classi poiché un istanza non può essere contemporaneamente un oggetto di `Studente` e `Docente`.
In altre parole non possono esistere tabelle di tue tipi diversi che ereditano da una tabella, come già detto all'inizio di questa lezione in PostgreSQL non esiste il concetto di [[Ereditarietà delle classi|ereditarietà come in Python ]]. 

Quindi i cambiamenti da fare sono:
1. Inserire due flag booleani come nella [[Ristrutturazione di generalizzazioni|ristrutturazione delle generalizzazioni in Python]];
	- `is_studente:boolean`
	- `is_docente:boolean`



> [!abstract]- **Quando usare un attributo enumerativo oppure i flag booleani**
> La scelta tra l'usare un attributo di tipo enumerativo oppure i flag booleani può sembrare che dipenda solo dalla volontà del progettista di voler memorizzare o meno le sottoclassi nel DBMS, in realtà dipende anche come il progettista intende rappresentare la semantica della generalizzazione e della qualità del modello relazionale.
> Vediamo le **differenze concettuali** e **implicazioni pratiche**.
> **Approccio 1: tipo di dato enumerativo (o stringa) per rappresentare le sottoclassi**
>```postgresql
>CREATE TYPE TipoPersona AS ENUM ('Studente', 'Docente', 'Persona');
>
>CREATE TABLE Persona (
> 	  nome VARCHAR(100),
> 	  tipo TipoPersona,
> 	  matricola VARCHAR(12),
> 	  nascita DATE
>); 
>```
>
>Questo metodo sia nella fase di ristrutturazione che di implementazione ha diversi vantaggi:
>> [!done] **Vantaggi**
>> - **Un solo attributo** discrimina tra le sottoclassi (più semplice e leggibile)
>>    
>>- Più **coerente con generalizzazioni `{disjoint}` e `{disjoint, complete}`**: è impossibile che una persona sia contemporaneamente `Studente` e `Docente`
>>   
>>- **Permette facilmente di memorizzare il concetto di sottoclasse** nel DB, **in forma implicita**, come richiesto nei casi di generalizzazione completa.
>
>> [!failure] **Svantaggi**
>> - In presenza di generalizzazioni **non disgiunte**, non è sufficiente (una persona potrebbe essere sia docente che studente)
>>   
>>- Richiede **vincoli esterni** per validare la coerenza fra tipo e campi (e.g., matricola ⇔ tipo = 'Studente').
>
>**Approccio 2: flag booleani**
>Esempio:
>```postgresql
>CREATE TABLE Persona (
> 	  nome VARCHAR(100),
> 	   is_studente BOOLEAN,
> 	  is_docente BOOLEAN,
> 	   matricola VARCHAR(12),
> 	   nascita DATE
>);
>```
>
>> [!done] **Vantaggi**
>> - Più flessibile in caso di **generalizzazioni sovrapposte/non disgiunte** (una persona può essere entrambe le cose)
>>   
>>- Evita la definizione di un tipo ENUM, quindi più _compatibile_ con DBMS che non supportano ENUM.
>
>
>>[!failure] **Svantaggi**
>>- **Modello meno leggibile**: i flag vanno interpretati e possono creare ambiguità
>>   
>>- Serve **maggiore logica di validazione**: se entrambi i flag sono veri? o entrambi falsi?
>>    
>>- Perde la **semantica forte del tipo** → non rappresenta davvero la sottoclasse come entità nel modello.
>
>In conclusione:
>==Se si usa un attributo di tipo enumerativo si **rappresentano le sottoclassi in forma normalizzata** (anche se non in tabelle distinte), e si tiene traccia della _natura_ dell’istanza.==
>
>==Mentre se si usano flag booleani il progettista **non formalizza le sottoclassi come entità autonome**, ma solo come _proprietà_==

2. inglobare nella classe padre gli attributi delle classe figlie aggiungendo i vincoli `[0..1]` accanto agli attributi delle sottoclassi:
	- `matricola : varchar(12) [0..1]`
	- `nascita : Date [0..1]`
	In questo modo sempre si rispetta la generalizzazione poiché se `p.is_studente = True` se e solo se `p.matricola` è valorizzato, e se `p_is_docente = True` se e solo se `p.nascita` è valorizzato



3. Rilassare i vincoli di molteplicità a zero anche sulle associazioni che coinvolgevano le sottoclassi:
	- `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 0..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 0..1`
	In questo modo stiamo dicendo che una persona può partecipare al link di associazione `iscritto` **oppure** `afferenza` solo se è uno studente **oppure** un docente, quindi di contro se non è ne uno studente non partecipa al link di associazione `iscritto` e se non è uno docente non partecipa al link di associazione `afferenza`.

##### Vincoli esterni 
Come nei casi precedenti anche in questo la semantica non è esprimibile solo attraverso la struttura, quindi è necessario specificare i vincoli esterni per mantenere la coerenza semantica:
```plain
Per ogni istanza p di Persona:
1. p.is_studente = TRUE ⇔ (se e solo) se p.matricola è valorizzato
2. p.is_studente = TRUE ⇔ (se e solo) se p è coinvolto in un link “iscritto”
3. p.is_docente = TRUE ⇔ (se e solo) se p.nascita è valorizzato
4. p.is_docente = TRUE ⇔ (se e solo) se p è coinvolto in un link “afferenza”
```

#### Caso 5: Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte con il vincolo `{complete}`
In questo caso affrontiamo il caso in cui si ha una generalizzazione tra classi con il solo vincolo  `{complete}`.
Come già sappiamo questo vincolo significa:
>_tutte_ le istanze della superclasse devono appartenere a **una o più** delle sottoclassi coinvolte.


![[Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte con il vincolo `{complete}`.png]]

###### Spiegazione 
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

In questo caso dobbiamo tenere conto per l'appunto del significato del vincolo sulla generalizzazione.
Come per [[#Caso 3 Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte|il caso precedente]] le azioni da compiere sono le stesse:
1. applicare due flag booleani:
	- `is_studente:boolean`
	- `is_docente:boolean`
2. inglobare nella classe padre gli attributi delle classe figlie aggiungendo i vincoli `[0..1]` accanto agli attributi delle sottoclassi:
	- `matricola : varchar(12) [0..1]`
	- `nascita : Date [0..1]`
	In questo modo sempre si rispetta la generalizzazione poiché se `p.is_studente = True` se e solo se `p.matricola` è valorizzato, e se `p_is_docente = True` se e solo se `p.nascita` è valorizzato
3. Rilassare i vincoli di molteplicità a zero anche sulle associazioni che coinvolgevano le sottoclassi:
	- `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 0..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 0..1`
	In questo modo stiamo dicendo che una persona può partecipare al link di associazione `iscritto` **oppure** `afferenza` solo se è uno studente **oppure** un docente, quindi di contro se non è ne uno studente non partecipa al link di associazione `iscritto` e se non è uno docente non partecipa al link di associazione `afferenza`.


L'unica differenza è che si aggiunge un vincolo esterno per mantenere la coerenza semantica:
```plain
Per ogni istanza p di Persona:
1. p.is_studente = TRUE se e solo se p.matricola è valorizzato
2. p.is_studente = TRUE se e solo se p è coinvolto in un link “iscritto”
3. p.is_docente = TRUE se e solo se p.nascita è valorizzato
4. p.is_docente = TRUE se e solo se p è coinvolto in un link “afferenza”
5. p.is_docente = TRUE oppure p.is_studente = TRUE
```

In questo caso il quinto e ultimo vincolo sta a significare che una persona può essere sia studente che docente. Difatti in questo caso l'oppure può essere inteso come un OR inclusivo andando così a rispettare pienamente la semantica del vincolo `{complete}`.




### 2. [[#^secondoMetodo|Divisione della superclasse in più classi disgiunte]] 

Consiste nel **eliminare la superclasse** e **replicare tutti i suoi attributi** nelle sottoclassi, creando così tabelle indipendenti per ciascuna sottoclasse. È applicabile **solo se la generalizzazione è `{disjoint, complete}`**.


![[Divisione in classi disgiunte.png]]

###### Spiegazione:
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Citta` con attributo:
	- `nome:varchar(100)`

2. `Persona` è la superclasse con attributo:
    - `cf:CodiceFiscale{id}`(l'id sta a significare che ogni l'attributo `cf` è univoco per ogni istanza `p:Persona`)
    
    - `nome : varchar(100)`
        
3. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
4. Associazioni:
    - `Citta`  ↔  `Persona` (associazione `residenza`)
	    - Molteplicità 
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

> [!abstract]- **Differenze tra la [[#1. primoMetodo Fusione delle classi|fusione]] e la [[#2. secondoMetodo Divisione della superclasse in più classi disgiunte|divisione]]** 
> Assumendo di conoscere il significato del vincolo [[Generalizzazioni#^db2378|`{disjoint, complete}`]], la scelta del progettista di utilizzare la **divisione della superclasse in più classi disgiunte** (anziché la fusione, come nel [[#Caso 3 Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte e complete (`{disjoint, complete}`)|caso 3]]) può essere giustificata da molteplici motivi, tra cui:
> 1. **Necessità di tabelle distinte nel dominio applicativo:**
> 	Quando il dominio di riferimento **distingue concettualmente** `Studente` e `Docente` come entità autonome e trattate con logiche amministrative separate, è opportuno modellarle come tabelle distinte, pur condividendo alcuni attributi (es. `nome`, `cf` come in questo caso).
> 		**Esempio pratico**:
>
>- I **docenti** non si iscrivono ai corsi e non devono figurare in alcun contesto "da studente".
 >   
>- Gli **studenti** non insegnano e non sono associati a dipartimenti.
>    
>- Il sistema informativo gestisce studenti e docenti **con interfacce o flussi separati**.
> 2. **Query prevalentemente specifiche per sottoclasse**
> Se il **95% delle query** riguardano solo `Studente` o solo `Docente`, allora avere tabelle separate:
> 
> - **Evita join su attributi inutili**
>     
> - **Ottimizza le prestazioni**
>     
> - Riduce il rischio di accessi incoerenti (es., leggere `nascita` per uno studente)
> 3. **Attributi specifici molto numerosi**
> 
> Se le sottoclassi hanno molti attributi propri e **pochi in comune**, allora:
> 
> - **Fondere** tutto in un’unica tabella genera tante colonne nullable
>     
> - **Dividere** in due tabelle riduce lo "spreco" di spazio e migliora la **leggibilità dello schema.**
> 4. **Necessità di enforcement della disgiunzione tramite vincoli esterni**
> 
> Con il metodo della divisione, la **disgiunzione logica** tra sottoclassi può essere **espressa con vincoli a livello di database**:
> Nel caso della fusione ([[#Caso 3 Ristrutturazione di generalizzazioni per fusione in caso di sottoclassi disgiunte e complete (`{disjoint, complete}`)|caso 3]]), la disgiunzione è "logica", ma spesso **non enforceable direttamente** nel DB.
> Al contrario, con la **fusione**, la disgiunzione è affidata a logica applicativa o vincoli parziali (`tipo`, flag, ecc.), meno robusti.
> 
> 5.  **Preferenza progettuale o vincolo tecnologico**
> 
> - Alcuni ORM (Object-Relational Mapping) lavorano **meglio con classi separate**
> - Alcuni DBMS o strumenti ETL richiedono tabelle fisicamente distinte.

Andando sulla destra notiamo come nella ristrutturazione della generalizzazione la classe padre `Persona` viene eliminata e i suoi attributi sono replicati in ogni sottoclasse.
Inoltre possiamo notare come entrambi le sottoclassi partecipano a un link di associazione con la classe `Città`:

`Studente` partecipa a un link di associazione `residenza_stud` con `Città`, con molteplicità `1..1`.
`Città` partecipa a un link di associazione `residenza_stud` con `Studente`, con molteplicità `0..*`.
`Docente` partecipa a un link di associazione `residenza_doc` con `Città`, con molteplicità `1..1`, mentre `Città` partecipa al link di associazione `residenza_doc` con molteplicità `0..*`.


Questo perché quando si sceglie la tecnica della divisione per ristrutturare una generalizzazione il fine è quello di trattare le sottoclassi come classi indipendenti a sé.

Quindi in sintesi : 
- La **superclasse `Persona` è scomparsa**.
    
- `Studente` e `Docente` **ripetono** gli attributi `nome` e `cf` (Codice Fiscale).
    
- L'associazione `residenza` è stata **moltiplicata**:
    
    - `residenza_stud` collega `Studente` ↔ `Città`
        
    - `residenza_doc` collega `Docente` ↔ `Città`
        
- Si sono quindi **moltiplicati ruoli e associazioni**, aumentando la complessità.

##### Vincoli esterni 
Poiché nel metodo della **divisione** in sottoclassi disgiunte viene a mancare una tabella comune che centralizzi l’identità concettuale (`Persona`), la **semantica del vincolo di identificazione** (ad esempio su `cf`) **non è più esplicitamente rappresentata** nello schema fisico.

In particolare, non è più garantito che **un’identità (`cf`) compaia in una sola sottoclasse**, come richiesto dal vincolo `{disjoint}`.

Per recuperare questa informazione **semantica persa**, è necessario definire un **vincolo esterno**:
```plain
non devono esistere s:Studente e d:Docente tali che s.cf = d.cf
```

Questo vincolo assicura che **una stessa chiave (`cf`) non appaia contemporaneamente in più sottoclassi**, **preservando la disgiunzione**.


> [!caution] Occhio all'approccio della divisione
> L’approccio di **dividere la superclasse in più tabelle (una per sottoclasse)** va bene **solo in presenza di generalizzazioni `{disjoint, complete}`**.  
>In altri casi è **problematico** e va **usato con estrema cautela**.
> Per comprendere meglio ciò vediamolo nel dettaglio:
> 1. **Generalizzazione non completa ([[Generalizzazioni#^defComplete|`¬complete`]])**
>> ==_tutte_ le istanze della superclasse devono appartenere a **una o più** delle sottoclassi coinvolte.==
>
>
>Il problema nel metodo della divisione è che la la superclasse viene "smontata" e **non esiste più una tabella centrale (in questo caso `Persona`).**
>Se però alcune persone **non appartengono a nessuna sottoclasse**, **non c'è modo di rappresentarle**, e quindi:
>- **Si perdono delle informazioni    
>-  Si viola la semantica del modello concettuale
>  1. Generalizzazione non disgiunta ([[Generalizzazioni#^defDisjoint|`¬disjoint`]]) 
>>==le sottoclassi **non si sovrappongono**, quindi un'istanza può appartenere a **una sola** sottoclasse tra quelle o a nessuna.==
>
>In questo caso nella divisione disgiunta  ogni persona ha una riga **in una sola sottoclasse**. Se invece **può comparire in più sottoclassi (es. essere Studente _e_ Docente)**:
>- Si crea **duplicazione** dei dati comuni (`cf`, `nome`, ecc.)
 >   
>- Si rischia **incoerenza** (es. due `nome` diversi per la stessa `cf`)
>    
>- È necessario **introdurre vincoli esterni** complicati per mantenere l’identità.
>> [!ticket] **In Conclusione**
>> Il metodo della divisione in classi disgiunte funziona bene solo se la generalizzazione è `{disjoint,complete}`, perché:
>> - Nel vincolo `{disjoint}` → le istanze sono sono in una sola tabella (non vi è la sovrapposizione)
>> - Nel vincolo `{complete}`→ le istanze sono in almeno una tabella.
>> Di conseguenza se questi vincoli **non sono garantiti**, il metodo:
>> - **Può rompere la semantica**
>> - **Richiede molti vincoli esterni**
>>   
>> **Quindi va usato con estrema cautela, solo se la modellazione concettuale lo giustifica chiaramente.**


### 3. Sostituzione di relazioni `is-a` con associazioni
Ora affrontiamo il [[#^terzoMetodo|terzo metodo]] della ristrutturazione delle generalizzazioni

#### Caso 1: Ristrutturazione delle generalizzazioni: Ristrutturazione di relazioni `is-a` indipendenti o generalizzazioni non disgiunte e non complete

L'immagine rappresenta un caso in cui si parte da una generalizzazione **non disgiunta e non completa** (oppure da relazioni `is-a` indipendenti). In questo contesto, si adotta una ristrutturazione alternativa in cui la relazione di generalizzazione viene **sostituita da associazioni**.

![[Ristrutturazione di relazioni is-a indipendenti o generalizzazioni non disgiunte e non complete.png]]

###### Spiegazione:
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

Guardando il diagramma a destra dell'immagine notiamo delle differenze rispetto  al metodo di divisione, in questa ristrutturazione:

- La superclasse `Persona` viene **mantenuta**.
    
- Le sottoclassi `Studente` e `Docente` diventano **classi indipendenti** collegate a `Persona` tramite apposite associazioni:
    
    - `s_isa_p`: `Studente` ↔ `Persona` con molteplicità `0..1` ↔ `1..1{id}`
        
    - `d_isa_p`: `Docente` ↔ `Persona` con molteplicità `0..1` ↔ `1..1{id}`


##### Il ruolo dell’identificatore `{id}`
L'identificatore `{id}` sul vincolo dell'associazione agisce come **identificatore esterno** per le ex-sottoclassi `Studente` e `Docente`. In questa ristrutturazione:

- Le classi `Studente` e `Docente` **non ereditano più direttamente** da `Persona`.
    
- Vengono invece trasformate in **classi indipendenti**, collegate a `Persona` attraverso **associazioni uno-a-uno**:
    
    - con **molteplicità obbligatoria `1..1{id}`** dalla parte di `Persona`, che fornisce l'identificativo univoco ([[Lezione 1; Introduzione e modello relazionale#La chiave primaria|chiave primaria]]),
        
    - e **molteplicità opzionale `0..1`** dalla parte di `Studente` o `Docente`.
        

Questa struttura riflette il concetto di **identificazione esterna**:

- ==L'identità delle istanze di `Studente` e `Docente` non è autonoma, ma **deriva dall'identificativo `{id}` della corrispondente istanza di `Persona`**.==
    
- In tal modo, ==**ogni `Studente` o `Docente` deve necessariamente essere associato a una `Persona`**==, **mentre una `Persona` può:**
    
    - non essere né `Studente` né `Docente`,
        
    - essere solo `Studente`,
        
    - essere solo `Docente`,
        
    - oppure essere **entrambe le cose** contemporaneamente.
        

> ==In altre parole, la presenza di un collegamento `s_isa_p` o `d_isa_p` indica che l’istanza della classe `Persona` rappresenta anche uno `Studente` o un `Docente`.==

Inoltre, il fatto che l'identificativo `{id}` sia **comune e condiviso tra `Persona` e le ex-sottoclassi** assicura che:

- ==**non possano esistere due `Studente` (o due `Docente`) con lo stesso identificatore**, ovvero non possono esistere due righe distinte nella tabella `Studente` collegate alla stessa persona==.
    
- ==Questo vincolo **preserva l’univocità dell’identità** delle ex-sottoclassi rispetto alla classe generale `Persona`.==


> [!NOTE] **Nota:**
> la presenza di un collegamento `s_isa_p` o `d_isa_p` indica che l’istanza della classe `Persona` può rappresentare anche rispettivamente uno `Studente` o un `Docente`.

**Inoltre non serve specificare vincoli esterni poiché in questo caso la struttura rappresenta bene la semantica della generalizzazione senza vincoli**

> [!done] **Vantaggi dell’identificazione esterna**
> - **Univocità dell’identità garantita**:  
>    Non possono esistere due `Studente` o due `Docente` con lo stesso `id`, poiché l’identità è **univocamente determinata** dalla chiave primaria della `Persona`.
>    
>- **Separazione logica e semantica** tra la struttura comune (`Persona`) e i ruoli specifici (`Studente` e `Docente`), pur mantenendo l’integrità dei dati.


#### Caso 2: Ristrutturazione in caso di sottoclassi disgiunte (con vincolo `{disjoint}`)

In questo scenario, si parte da una generalizzazione tra sottoclassi disgiunte. Anche in questo caso, è possibile adottare il **terzo metodo** di ristrutturazione, ossia la **sostituzione della relazione di generalizzazione con associazioni**.

![[Ristrutturazione in caso di sottoclassi disgiunte.png]]

###### Spiegazione
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`

Ora partendo dal significato del vincolo [[Generalizzazioni#^defDisjoint|`{disjoint}`]] sappiamo che una persona può essere uno studente o un docente o nessuno dei due.
Analogamente al **[[#Caso 1 Ristrutturazione delle generalizzazioni Ristrutturazione di relazioni `is-a` indipendenti o generalizzazioni non disgiunte e non complete|Caso 1]]**, si procede con:

- **Mantenimento della classe `Persona`** come entità centrale.
    
- Trasformazione delle ex-sottoclassi `Studente` e `Docente` in **classi autonome**, collegate a `Persona` tramite apposite **associazioni identificanti**:
    
    - `s_isa_p`: `Studente` ↔ `Persona`, con molteplicità `0..1` ↔ `1..1{id}`
        
    - `d_isa_p`: `Docente` ↔ `Persona`, con molteplicità `0..1` ↔ `1..1{id}`

##### Il ruolo dell'identificatore `{id}` nella ristrutturazione con il vincolo `{disjoint}`

L’identificatore `{id}` sull'associazione svolge, anche in questo caso, il ruolo di **identificatore esterno** per le classi `Studente` e `Docente`, esattamente come nel **Caso 1**. Tuttavia, **la differenza fondamentale è data dal vincolo `{disjoint}`**.

- Ogni `Studente` o `Docente` deve riferirsi a un’identità presente in `Persona` (vincolo di molteplicità `1..1{id}` sul lato `Persona`).
    
- Una stessa `Persona` può essere:
    
    - solo uno `Studente`,
        
    - solo un `Docente`,
        
    - oppure **nessuno dei due**,
        
    - **ma mai entrambe le cose contemporaneamente** (vincolo `{disjoint}`).
Solo che uno studente è per forza una persona (vincolo sull'associazione `s_isa_p 1..1{id}`) mentre una persona deve essere solo uno studente o un docente ma può non essere nessuno dei due (vincoli sulle associazioni `s_isa_p 0..1`, dal lato `Studente`,  e `d_isa_p 0..1`, dal lato `Docente`).

##### Vincoli esterni per il rispetto della disgiunzione
Poiché la struttura con associazioni **non è in grado di esprimere direttamente il vincolo `{disjoint}`**, è necessario **enunciarlo esplicitamente come vincolo esterno** per mantenere la coerenza semantica del modello concettuale:
```plain
Disgiunzione: non devono esistere p:Persona, s:Studente d:Docente tali che (s, p): s_isa_p e (d, p): d_isa_p
```
^vincDis


==In altre parole, **una stessa istanza di `Persona` non può essere contemporaneamente collegata a entrambe le sottoclassi `Studente` e `Docente`**.== 

#### Caso 3: Ristrutturazione in caso di sottoclassi complete (con il vincolo `{complete}`)

In questo scenario si parte da una generalizzazione **completa** (`{complete}`), ovvero **ogni istanza della superclasse `Persona` deve necessariamente appartenere ad almeno una delle sottoclassi `Studente` o `Docente`**.

Come nei casi precedenti, si procede con la **sostituzione della generalizzazione con associazioni identificanti**.


![[Ristrutturazione in caso di sottoclassi complete.png]]

###### Spiegazione:
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`.


Anche in questo caso, la struttura viene trasformata nel seguente modo:

- La superclasse `Persona` viene **mantenuta**.
    
- Le sottoclassi `Studente` e `Docente` diventano **classi autonome**, collegate a `Persona` tramite:
    
    - `s_isa_p`: `Studente` ↔ `Persona`: `0..1` ↔ `1..1{id}`
        
    - `d_isa_p`: `Docente` ↔ `Persona`: `0..1` ↔ `1..1{id}`

Anche qui, [[#Il ruolo dell’identificatore `{id}`|L'identificatore `{id}`]] svolge il medesimo ruolo del dei due casi visti in precedenza solo che bisogna tener conto del vincolo `{complete}`: 
- Le classi `Studente` e `Docente` **non ereditano più direttamente** da `Persona`.  
    
- Vengono invece trasformate in **classi indipendenti**, collegate a `Persona` attraverso **associazioni uno-a-uno**:
    - con **molteplicità obbligatoria `1..1{id}`** dalla parte di `Persona`, che fornisce l'identificativo univoco ([[Lezione 1; Introduzione e modello relazionale#La chiave primaria|chiave primaria]]).
        
    - e **molteplicità opzionale `0..1`** dalla parte di `Studente` o `Docente`.


##### Vincoli esterni per il rispetto della completezza
Poiché la struttura con associazioni **non è in grado di esprimere direttamente il vincolo `{complete}`**, è necessario **enunciarlo esplicitamente come vincolo esterno** per mantenere la coerenza semantica del modello concettuale:
```plain
Completezza: per ogni p:Persona:
• esiste s:Studente per cui: (s, p): s_isa_p
• oppure esiste d:Docente per cui: (d, p): d_isa_p
```
^vincCompl

In altre parole: 
Ogni istanza della classe `Persona` deve necessariamente essere anche uno `Studente` oppure un `Docente`, o entrambi.

#### Caso 4: Ristrutturazione in caso di sottoclassi disgiunte e complete (con il vincolo `{disjoint, complete}`)

In questo scenario si parte da una generalizzazione **disgiunta e completa** ([[Generalizzazioni#^db2378|`{disjoint,complete}`]]), ovvero tutte le istanze di `Persona` devono appartenere a una sola delle classi coinvolte:
- **`disjoint`** → ogni istanza della superclasse `Persona` **appartiene a una sola** tra le sottoclassi coinvolte (`Studente` o `Docente`);
    
- **`complete`** → ogni istanza della superclasse `Persona` **appartiene ad almeno una** tra le sottoclassi coinvolte.

![[Ristrutturazione in caso di sottoclassi disgiunte e complete.png]]

###### Spiegazione 
partendo a sinistra dell'immagine (dove si trova il diagramma UML concettuali delle classi);
1. `Persona` è la superclasse con attributo:
    
    - `nome : varchar(100)`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12)`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    
    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`.

Anche in questo caso, la struttura viene trasformata nel seguente modo:

- La superclasse `Persona` viene **mantenuta**.
    
- Le sottoclassi `Studente` e `Docente` diventano **classi autonome**, collegate a `Persona` tramite:
    
    - `s_isa_p`: `Studente` ↔ `Persona`: `0..1` ↔ `1..1{id}`
        
    - `d_isa_p`: `Docente` ↔ `Persona`: `0..1` ↔ `1..1{id}`.

Anche qui, [[#Il ruolo dell’identificatore `{id}`|L'identificatore `{id}`]] svolge il medesimo ruolo del dei due casi visti in precedenza solo che bisogna tener conto del vincolo `{complete}`: 
- Le classi `Studente` e `Docente` **non ereditano più direttamente** da `Persona`.  
    
- Vengono invece trasformate in **classi indipendenti**, collegate a `Persona` attraverso **associazioni uno-a-uno**:
    - con **molteplicità obbligatoria `1..1{id}`** dalla parte di `Persona`, che fornisce l'identificativo univoco ([[Lezione 1; Introduzione e modello relazionale#La chiave primaria|chiave primaria]]).
        
    - e **molteplicità opzionale `0..1`** dalla parte di `Studente` o `Docente`.

##### Vincoli esterni per il rispetto della disgiunzione e della  completezza
Negli ultimi due casi precedenti abbiamo visto come le strutture non esprimessero al meglio la semantica e quindi abbiamo dichiarato dei [[#^vincDis|vincoli di disgiunzione]] e di [[#^vincCompl|completezza]], in questo scenario i due tipi di vincoli vengono uniti insieme:
```plain
1. Disgiunzione: non devono esistere p:Persona, s:Studente e d:Docente tali che (s, p): s_isa_p e (d, p): d_isa_p
2. Completezza: per ogni p:Persona:
• esiste s:Studente per cui: (s, p): s_isa_p
• oppure esiste d:Docente per cui: (d, p): d_isa_p
```

**Interpretazione:**
- ==Il **primo vincolo** vieta che una `Persona` sia **collegata a entrambe** le sottoclassi (`{disjoint}`) .==
    
- ==Il **secondo vincolo** impone che una `Persona` **sia collegata almeno a una** delle due (`{complete}`).==

Se ci sono delle classi che non voglio memorizzare non viene scritto nel DBSM:
 prendiamo come esempio questa immagine:
 ![[Screenshot 2025-07-09 at 12-21-24 Meet - bmb-xnne-ahh.png|500x205]]




---

## Identificatori di classe

Al termine della **ristrutturazione del diagramma UML delle classi**, ogni classe deve:

- disporre di **almeno un identificatore** (chiave candidata),
    
- e di un **identificatore primario** ben definito (che diventerà la **chiave primaria** nella futura tabella relazionale).

La metodologia operativa è:
1. Scelta di un identificatore concettuale (se disponibile):
	Se una classe possiede un attributo che rappresenta un identificatore **reale e significativo** (es. codice fiscale, matricola):

	- si verifica se è **sufficientemente stabile** e **semplice** da usare come chiave primaria.
    
		- se sì, si contrassegna con `{id1}` (identificatore primario).   
Esempio:
```plain
Persona
  nome : varchar(100)
  cf   : CodiceFiscale {id1}   ← identificatore concettuale accettabile
```

2. Creazione di un identificatore artificiale (se necessario):
Se una classe:

- **non ha un identificatore concettuale**, oppure
    
- gli attributi esistenti **non sono adatti** come chiave (es. `nome` non è univoco),
    

→ allora si **aggiunge un nuovo attributo artificiale** (es. `id: integer`) e lo si marca con `{id1}`.

Esempio: 
```plain
CorsoDiLaurea
  nome : varchar(100)
  id   : integer {id1}   ← identificatore artificiale
```

Questi identificatori artificiali sono solo escamotage tecnologico: ==**servono solo per supportare l’implementazione relazionale**, ma **non hanno valore concettuale.**==

### Esempio 1
![[Esempio identificatori di classe.png]]

###### Spiegazione 
A sinistra dell'immagine abbiamo un diagramma ristrutturato con:
 1. `Persona`  con attributo:
    
    - `nome : varchar(100)`
    - `cf:CodiceFiscale{id1}`
        
2. Sono presenti due sottoclassi:
    
    2.1 `Studente`, con attributo `matricola : varchar(12){id}`
        
    2.2. `Docente`, con attributo `nascita : Date`
        
3. Associazioni:
    - `Persona` ↔ `Studente` (Associazione: `s_isa_p`)
    
		- Molteplicità: `Persona 1..1 {id2}` ↔ `Studente 0..1`
    
	    - Significato: ogni `Studente` è associato a una sola `Persona`, che viene **identificata dal proprio Codice Fiscale (`cf`)**.
        
	    - L’identificatore `{id2}` sull’associazione indica che **lo studente eredita l’identificatore della `Persona` tramite il legame `s_isa_p`.**
	    - La `matricola` rappresenta un **identificatore secondario**, non utilizzato come **chiave primaria effettiva** nella traduzione logica, poiché l’identità dello studente è veicolata tramite la persona collegata.
	- `Persona` ↔ `Docente` (Associazione: `d_isa_p`)
    
		- Molteplicità: `Persona 1..1 {id}` ↔ `Docente 0..1`
    
		    - Il significato dell' `{id}` è simile al precedente:
        
	        - Ogni `Docente` è associato a una sola `Persona`, riconoscibile tramite il suo `cf`.
            
	        - Anche in questo caso, l’identificatore effettivo del `Docente` è **quello della `Persona` associata**, e quindi non c’è un identificatore proprio.

    - `Studente` ↔ `CorsoDiLaurea` (associazione `iscritto`)
        
        - Molteplicità: `Studente 0..*` ↔ `CorsoDiLaurea 1..1`
            
    - `Docente` ↔ `Dipartimento` (associazione `afferenza`)
        
        - Molteplicità: `Docente 0..*` ↔ `Dipartimento 1..1`.

Ora sul lato destro dell'immagine le modifiche da apportare sono:
- Le classi **che non hanno un identificatore naturale** (cioè un attributo con vincolo `{id}`) vengono **dotate di un identificatore artificiale**;
- Di conseguenza si prepara il terreno per una **traduzione efficace in PostgreSQL**, che richiede chiavi primarie in tutte le tabelle.
###### 1. Classe `Persona`
Difatti nella classe `Persona` l'identificatore accanto all'attributo `cf` diventa 
```
cf : CodiceFiscale {id1}
```

Il vincolo `{id2}` sull’associazione `s_isa_p` viene sostituito da `{id1}`: perché ==questo id diventa l'identificativo primario== 

###### 2. Classe `Studente` 

Nel diagramma a sinistra l'identificativo accanto all'attributo `matricola` da `{id1}` cambia in `{id2}`: ogni istanza di studente ha un numero di matricola univoco alle diverse istanze della stessa classe ma questo identificativo è diverso dall' identificativo sull'attributo `cf` di `Persona`. 

> [!NOTE] **Nota:**
> In fase di ristrutturazione, i vincoli `{id}` vengono rinumerati come `{id1}`, `{id2}`, ... per distinguere **tra identificatori distinti** (anche se con stesso nome) e per individuare **quello primario** nelle successive traduzioni logiche.

Il vincolo sull'associazione con la classe `Persona` (`s_isa_p`), da `{id2}` diventa `{id1}`: quindi lo `Studente` **eredita l’identificatore di `Persona`** (cioè `cf`), e non ha un proprio identificatore autonomo.
Questo è utile **se la `matricola` non è univoca o non è sufficiente** come chiave primaria.

###### 3. Classe `Docente`
Anche qui il vincolo sull'associazione `d_isa_p` da `{id}` diventa `{id1}`: quindi ogni istanza di `Docente` **eredita l’identificatore di `Persona`** (cioè `cf`), e non ha un proprio identificatore autonomo.


> [!ticket] Regola D'Oro
> Per le classi che erano sotto-classi di generalizzazioni ristrutturate mediante sostituzione con associazioni, ==questo identificatore <u>deve essere il primario</u>==


###### 4. Classe `CorsoDiLaurea`
Siccome questa classe non conteneva nessun attributo identificativo (cioè con `{id}` accanto), viene introdotto un identificatore artificiale:
```
id: integer {id1}
```

Come già detto prima, questi identificatori artificiali **servono solo per supportare l’implementazione relazionale**, ma **non hanno valore concettuale.**
In altre parole serve come **chiave primaria autonoma**, necessaria per realizzare la tabella `CorsodiLaurea` in PostgreSQL.
L’attributo `nome` **rimane descrittivo**.
I vincoli sull'associazione `iscritto` rimangono invariati (`Studente 0..*` ↔ `CorsoDiLaurea 1..1` )

###### 5. Classe `Dipartimento`
Anche qui prima non era presente un attributo identificativo per cui viene aggiunto l'attributo:
```
id: integer {id1}
```

E come per la classe `CorsoDiLaurea` serve come **chiave primaria autonoma**, necessaria per realizzare la tabella `Dipartimento` in PostgreSQL.
I vincoli sull'associazione `afferenza` rimangono invariati (`Docente 0..*` ↔ `Dipartimento 1..1` ).


> [!info] **Perché servono gli identificatori artificiali?**
> - ==Alcune classi, come `CorsoDiLaurea` e `Dipartimento`, **non hanno attributi sufficienti per garantire unicità**.==
 >   
>- ==Per garantire **l’integrità referenziale** nel database, ogni tabella deve avere una **chiave primaria**.==
>    
>- Gli identificatori artificiali:
 >
>- ==non derivano da attributi reali del dominio,==
 >       
 >- ==ma sono **necessari per modellare correttamente il sistema informativo**.==


### Il problema dei cicli di identificatori primari esterni 
Come abbiamo già visto nel modello concettuale, un **identificatore primario** (annotato con `{id1}`) può essere composto da:

- un **attributo locale** (es. `a`, `b`, `c`)
    
- e da una **relazione identificante** a cardinalità minima `1` su un'altra classe, che fornisce a sua volta una parte dell'identificatore (via catena).
Per capire meglio questo problema prendiamo ad esempio questa immagine:

![[Cicli di identificaotri primari esterni.png]]

L'immagine rappresenta tre classi: `A`, `B`, `C`, con tre associazioni binarie:

- `A` è identificata da:
    
    - il proprio attributo `a` e
        
    - un oggetto di `B` tramite l’associazione `ab` (`1..1`, `{id1}`)
        
- `B` è identificata da:
    
    - il proprio attributo `b` e
        
    - un oggetto di `C` tramite `bc` (`1..1`, `{id1}`)
        
- `C` è identificata da:
    
    - il proprio attributo `c` e
        
    - un oggetto di `A` tramite `ac` (`1..1`, `{id1}`)
        
 **Questo forma un ciclo chiuso di dipendenze identificanti**:
```plain
A → B → C → A
```

#### Perché è un problema?
in questa situazione:

- Per creare un oggetto di `A`, **servirebbe già esistente** un oggetto di `B`
    
- Ma per creare `B`, serve `C`
    
- E per creare `C`, serve `A`... il che porta a un **vicolo cieco**: non si può creare _nessun_ oggetto senza che un altro esista prima.  
    - **Questo è logicamente impossibile.**
    

In pratica, **nessuna istanza può essere costruita per prima**, e quindi **l’intero schema è bloccato**.
In altre parole: 
per identificare (`id. primario`) un oggetto di `A` serve il valore dell’attributo `‘a’` e un oggetto di `B`.
• per identificare (`id. primario`) un oggetto di `B` serve il valore dell’attributo `‘b’` e un oggetto di `C`
• per identificare (`id. primario`) un oggetto di `C` serve il valore dell’attributo `‘c’` e un oggetto di …`A` (!).

Quindi per risolvere questo problema è necessario **interrompere almeno una delle dipendenze identificanti** del ciclo. Ciò significa:
- **Scegliere una o più classi coinvolte** (ad esempio `A` o `C`) e
    
- **Attribuirle un identificatore primario alternativo**, ad esempio:
    
    - un attributo **già esistente e sufficiente**, oppure
        
    - **aggiungere un identificatore artificiale** (es. `id: integer`), come si fa quando una classe **non è identificabile naturalmente o senza dipendenze cicliche**.

Come mostrato nell'immagine sottostante: 
![[Rompere i cicli di identificatori esterni primari.png]]

il ciclo tra le classi `A → B → C → A` viene **interrotto** sostituendo l’identificatore esterno di una delle classi (in questo caso, `B`) con un **identificatore artificiale**.

In particolare:

- ==`B` ottiene un identificatore artificiale `id: integer {id1}`==
    
- ==L’attributo `b` di `B` diventa `{id2}`, ossia una componente non più partecipante all’identificazione primaria==
    
- ==Le classi `A` e `C` mantengono la dipendenza identificante da `B`, ma il ciclo viene rotto perché `B` ora può essere **creata autonomamente**==
    

In questo modo:

- ==`B` è **la prima classe costruibile** (grazie al suo `id` artificiale)==
    
- ==`C` può essere identificata tramite `c` e una `B`==
    
- ==`A` può essere identificata tramite `a` e una `B`==  
       
    ==Quindi l’intero ciclo è stato **convertito in una catena**, e **la creazione degli oggetti diventa possibile**.==


### In conclusione 
> Al termine del passo di **definizione degli identificatori di classe**, si deve garantire che:

- ==**Ogni classe possieda almeno un identificatore**==
    
- ==**Ogni classe abbia esattamente un identificatore primario**, eventualmente composto==
    
- **Gli identificatori primari esterni non formino cicli**
    
    - ==Ossia, le **dipendenze identificanti tra classi devono essere acicliche**==
        

> Se necessario, questo risultato si ottiene:

- ==**inserendo identificatori artificiali** nelle classi coinvolte in cicli,==
    
- ==oppure **ristrutturando gli identificatori già presenti** per evitare dipendenze cicliche.==
