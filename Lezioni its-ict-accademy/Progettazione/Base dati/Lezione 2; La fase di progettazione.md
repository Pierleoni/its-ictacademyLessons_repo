# Introduzione
In questo momento ci troviamo nella [[Lezione 1; Introduzione e modello relazionale#Fase di progettazione|fase di progettazione]], come abbiamo già visto nella scorsa lezione possiamo suddividere in varie fasi il percorso fatto e quello ancora da fare:
### 1. Analisi concettuale
Lo scopo è comprendere e modellare i requisiti informativi del dominio applicativo, producendo uno **schema concettuale** ad alto livello, indipendente dal DBMS.
**Output:**

- 📘 Diagramma UML concettuale delle classi
    
- 📘 Specifiche dei tipi di dato
    
- 📘 Specifiche delle classi
    
- 📘 Specifiche dei vincoli esterni
    
- 📘 Diagramma UML concettuale degli _use-case_
    
- 📘 Specifiche concettuali degli _use-case_

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
L'obiettivo di questa fase è **generare lo schema relazionale** (comprensivo di vincoli) a partire dallo **schema concettuale UML** dell'applicazione.
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
La classe `esame` è stata tradotta in una **tabella indipendente**, in quanto rappresenta un’associazione n:m con attributi (→ _association class_).
La **correttezza semantica** delle relazioni è mantenuta tramite le foreign key, che garantiscono **l'integrità referenziale** tra `esame` ↔ `Studente` e `esame` ↔ `Corso`.
Difatti la prima foreign key fa **riferimento** al campo `matricola` della tabella `Studente`, che è una **primary key**.
Questo vincolo ==**impone che ogni valore di `studente` presente in `esame` esista già nella tabella `Studente`**.==  
**In altre parole:** ==non puoi registrare un esame per uno studente che **non è presente** nella tabella `Studente`.==

Mentre la seconda foreign key fa riferimento al campo `nome` della tabella `Corso`, che è la **primary key**.
Questo vincolo impone che ogni valore del campo `corso` in `esame` **esista già** come `nome` in `Corso`.
In altre parole: non è possibile registrare un esame per un corso che non esiste nella tabella `Corso`.
Il campo `corso` nella tabella `esame` deve quindi contenere solo valori che sono già presenti nel campo `nome` della tabella `Corso`.  
Questo garantisce l’**integrità referenziale** tra la tabella `esame` e la tabella `Corso`, assicurando che ogni esame faccia sempre riferimento a un corso effettivamente esistente nel sistema.

Tuttavia esaminiamo un caso leggermente più complesso:
![[Esempio2.png]]

Nel diagramma sono presenti:

- Due **classi**: `Studente` e `Corso`
    
- Un'[[Associazioni con attributi in UML#Le association class|association class]]: `insegna`, dotata dell’attributo `da: Date`
- L'associazione tra `Studente` e `Corso` è arricchita da vincoli di molteplicità `1..*` su entrambi i lati:
	- Dal lato **Lato `Docente`**:  
	   la molteplicità `1..*` indica che **ogni docente deve insegnare ad almeno un corso**, quindi ogni docente può essere associato ad almeno un corso.
	- **Dal lato `Corso`**: la molteplicità `1..*` indica che **almeno un corso deve essere insegnato da almeno un docente**, quindi ogni corso può essere associato ad almeno un docente.
In sintesi, l’associazione rappresenta una **relazione molti-a-molti (n:m)** tra le classi `Studente` e `Corso`, e l’attributo `data` presente nell’association class `esame` rappresenta un'informazione legata **all’evento stesso dell’esame** (ovvero _quando_ uno studente ha sostenuto un determinato corso).

**Decisioni progettuali:**

Il progettista decide che:

- Le istanze di `Docente`, `Corso` e `insegna` **devono essere memorizzate nel DB**.
    
- **Ogni istanza di classe o associazione viene mappata su una ennupla** (riga) di una tabella.
Questo si traduce in schema relazionale:
- Tabella `Docente`
```plain
Docente(matricola: integer, nome: varchar)
```



In questo caso, si ha un **vincolo di inclusione** (non una foreign key), derivato dal vincolo di molteplicità `1..*`:

`matricola` deve comparire `insegna(docente)`.
In altre parole: `matricola` deve comparire in almeno un’en­nupla del campo `docente` della tabella `insegna`.

- **Tabella `Corso`**
```plain
Corso(nome: varchar)
```


Anche in questo caso, si ha un vincolo di inclusione (non una foreign key), derivato dal vincolo di molteplicità 1..*:

`nome` deve comparire in `insegna(corso)`.
In altre parole: `nome` deve comparire in almeno un’en­nupla del campo `corso` della tabella `insegna`.

- ****Tabella `insegna`** (association class)** 
```plain
insegna(docente: integer, corso: varchar, da: Date)
```
- **Foreign Key** `docente` → `Docente(matricola)`
    - Il campo `docente` nella tabella `insegna` è **una chiave esterna** (foreign key) che **fa riferimento alla chiave primaria** `matricola` della tabella `Docente`.
    
	- In pratica, **ogni valore presente in `insegna.docente` deve già esistere nella colonna `matricola` della tabella `Docente`**.
    
	- Questo garantisce che **non si possano inserire righe nella tabella `insegna` con un docente che non esiste** nella tabella `Docente`.
- **Foreign Key** `corso` → `Corso(nome)`
	-  Il campo `corso` nella tabella `insegna` è **una chiave esterna** che **fa riferimento alla chiave primaria** `nome` della tabella `Corso`.
    
	- Questo vincolo impone che **ogni valore inserito in `insegna.corso` debba già esistere nella tabella `Corso.nome`**.


> [!NOTE] **Nota:**
> I **vincoli di inclusione** su `Docente` e `Corso` non sono implementati come foreign key, ma sono vincoli esterni **di partecipazione obbligatoria**, imposti dalla molteplicità `1..*` nel modello UML.  
>In altre parole: ogni docente e ogni corso **devono comparire almeno una volta nella tabella `insegna`**, affinché il modello rispetti le cardinalità definite nello schema concettuale.

### Perché è necessaria una ristrutturazione prima della traduzione
Una volta definito il **diagramma UML concettuale delle classi**, ci si trova spesso di fronte a **modelli ricchi di costrutti complessi**, tra cui:
- **Attributi multivalore**
    
- **Gerarchie is-a**, con generalizzazioni:
    
    - **disgiunte / non disgiunte**
        
    - **complete / non complete**
        
- Vincoli concettuali di alto livello (partecipazione, identificazione, ecc.)
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
Adattare lo schema concettuale alle **tecnologie scelte per l’implementazione**, mantenendo intatta la **capacità rappresentativa del modello (equivalenza estensionale)**.

In particolare, **se si adotta una tecnologia basata su basi di dati relazionali**:

- Lo schema ristrutturato **definisce quali classi saranno effettivamente memorizzate nel DB**.
    
- Contiene solo **costrutti semplici e direttamente implementabili**:
    
    - classi
        
    - associazioni
        
    - attributi con tipi di dato SQL (base o definiti dal progettista)
        
    - molteplicità massima **pari a 1**
        
- Tiene conto anche di **requisiti di performance** (efficienza dell’accesso ai dati, ridondanza controllata, ecc.)
    

2. **Traduzione diretta:**
   Una volta ottenuto lo **schema ristrutturato**, si può procedere alla **traduzione diretta**, ovvero:

- Si procede alla **generazione dello schema relazionale** vero e proprio, tenendo conto di:

	- vincoli di integrità (PK, FK, vincoli esterni)
    
	- requisiti di efficienza
    
	- eventuali regole di derivazione, trigger, ecc.
  

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

1. **Eliminazione degli attributi multivalore**  
    ==Gli attributi che ammettono più valori devono essere trasformati in **nuove classi** o **associazioni**, per rispettare la natura relazionale del modello finale.==
    
2. **Sostituzione dei tipi di dato concettuali**  
    Ogni tipo concettuale viene sostituito con un tipo **supportato dal DBMS**:
    
    - Tipo base SQL (es. `VARCHAR`, `INTEGER`, `DATE`)
        
    - Tipo definito dal progettista, se necessario (es. `CHECK`, `ENUM`, domini)
        
3. **Eliminazione delle generalizzazioni tra classi**  
    Le gerarchie `is-a` devono essere risolte in una struttura equivalente, attraverso:
    
    - ==Ereditarietà per sovrapposizione== (`single table`)
        
    - ==Suddivisione in più tabelle== (`multiple table`)
        
    - Strategie miste (in base alla **completezza/disgiunzione** cioè `{dissjoint, complete}`)
        
4. **Eliminazione delle generalizzazioni tra associazioni**  
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

![[Screenshot 2025-07-09 at 12-13-35 Meet - bmb-xnne-ahh.png]]

Nell’immagine proposta, sulla sinistra è rappresentata la classe `Studente`, con i seguenti attributi:

- `matricola: intero {id}` (identificatore univoco)
    
- `nome: stringa`
    
- `email: stringa [x..y]`: l’indicazione `[x..y]` rappresenta il vincolo di molteplicità che rende `email` un attributo multivalore.
Sulla destra, osserviamo come l’attributo multivalore `email` sia stato trasformato in una classe vera e propria, denominata `IndirizzoEmail`, con un attributo `valore: stringa {id}`, che funge da identificatore dell’istanza (questo perché non vogliamo rappresentare nel DB più volte la stessa istanza del tipo). 
Inoltre, i vincoli di molteplicità associati alle classi giocano un ruolo fondamentale nella corretta rappresentazione del modello:

- **Lato `Studente`**, ==il vincolo `1..*` impone che ciascun studente sia associato ad almeno un indirizzo email, garantendo così che il database memorizzi solo indirizzi email effettivamente collegati a studenti.==  
    ==_Si sottolinea che il vincolo `1..*` deve sempre essere applicato in questi casi._==
    
- **Lato `IndirizzoEmail`**, ==si mantiene la molteplicità originaria dell’attributo concettuale `[x..y]`, che definisce il numero minimo e massimo di studenti associabili allo stesso indirizzo email.==

2. **Eliminazione degli attributi multivalore di associazione**
![[eliminazione degli attributi multivalore di associazione.png]]

Nell’immagine a destra si osservano due classi e una association class:
1. Classe `Studente`:
	- con attributo `matricola:intero{id}`
	- con attributo `nome:stringa`
2. association class `esame`:
	
	- attributo multivalore `data: Data [x..y]``data:Data[x..y]`
	
	- attributo`voto: 18..31`
3. La classe `Corso`:
	- con attributo `nome:stringa{id}` 
I vincoli di molteplicità tra le classi e l’association class sono `0..*` su entrambi i lati.

Come si nota, l’attributo `data` di `Esame` è un attributo multivalore, a causa del vincolo di molteplicità `[x..y]`. 
Perciò, nel diagramma ristrutturato a destra, l’attributo `data: Data [x..y]` viene trasformato in una classe autonoma chiamata `DataProva`, con attributo `data: Data {id}`, e partecipa a un link di associazione `esame_prova` con molteplicità `1..*` verso `esame`.

==La molteplicità `1..*`, [[Screenshot 2025-07-09 at 12-13-35 Meet - bmb-xnne-ahh.png|come nell'esempio precedente]], impone che il database memorizzi solo le date effettivamente associate ad almeno un esame, garantendo l’integrità e la coerenza dei dati.==

Parallelamente, l’association class `esame` mantiene il proprio ruolo nel modello, partecipando a un link di associazione con `DataProva` con molteplicità che riflette quella originaria dell’attributo multivalore `data: Data` nel diagramma concettuale delle classi.


Al termine del passo di eliminazione degli attributi multivalore tutti gli attributi del diagramma ristrutturato dovranno avere vincoli di cardinalità `[0..1]` oppure `[1..1]`.


### Scelta dei tipi di dato
Analogamente a quanto avviene nella ristrutturazione di un diagramma delle classi in Python, anche nel contesto della progettazione di basi di dati è necessario trasformare il **diagramma UML concettuale delle classi** in uno **equivalente**, in cui **tutti gli attributi siano espressi tramite tipi di dato (domini) supportati dal DBMS**.
er ciascun attributo del modello concettuale, è necessario **scegliere un tipo di dato SQL compatibile**, eventualmente **definendo nuovi tipi di dato utente** mediante SQL.

###### 1. **Tipi concettuali di base**

Esempi:

- `intero`, `reale`, `stringa`, `Data`, `Ora`, `DataOra`  
    Corrispondenti tipi SQL standard (PostgreSQL):
    
- `integer`, `real`, `varchar(n)`, `date`, `time`, `timestamp`, ecc.  
    Riferimento: [PostgreSQL - Documentazione tipi di dato](https://www.postgresql.org/docs/current/datatype.html)
    

###### 2. **Tipi concettuali specializzati**

Esempi:

- `intero > 0`, `reale ≤ 0`, intervalli numerici (`x..y`), ecc.  
    Soluzione:
    
- Definizione di **domini personalizzati** con vincoli di controllo tramite:
```postgresql
CREATE DOMAIN PosInt AS INTEGER CHECK (VALUE > 0);
```

• Tipi concettuali enumerativi: ad es., {M,F}, etc.
—> definire nuovi tipi di dato supportati dal DBMS usando SQL: CREATE TYPE … AS ENUM (v. slide su
SQL DDL)
• Tipi concettuali composti: ad es., Indirizzo, etc.
—> definire nuovi tipi di dato supportati dal DBMS usando SQL: CREATE TYPE … AS (…) (v. slide su SQL
DDL)

Dobbiamo produrre sostituendo tutti i tipi di dati Python con tipi di dato SQL.
Quindi otteniamo un diagrama che tutti i tipi di dato sono tipi di dato in Postgres.

### Le generalizzazioni
Non ha senso il conetto di eredeitarietà in una base dati: una tabella è un altra tabella, non esiste.
Esiste la FK ma quelli sono attributi di una tabella, stessa cosa per le op di classi: le generalizzazioni vanno via.
Quindi la prima cosa da fare è la fusione che abbiamo già visto, macon la differenza che può essere applicata sempre.
![[Screenshot 2025-07-09 at 12-18-08 Meet - bmb-xnne-ahh.png|500x215]]

![[Screenshot 2025-07-09 at 12-18-25 Meet - bmb-xnne-ahh.png|500x214]]


In realta è molto analogo con roba già vista nell'implementazione delle generalizzazioni in Python.
Nella fase di progettazione: i progettisiti non devono progettare un sistema che rappresetna il mondo reale, di questo si occupa l'analista, mentre i proge si occupano anche delle performance del sistema.
Se ci sono delle classi che non voglio memorizzare non viene scritto nel DBSM:
 prendiamo come esempio questa immagine:
 ![[Screenshot 2025-07-09 at 12-21-24 Meet - bmb-xnne-ahh.png|500x205]]

Mettiamo di avere una operazione che deve restiruire i soli docenti ma essendo sia gli stud che i docenti sono in unica tabella ogno volta deve andarsi a cercare i docenti in mezzo agli studenti, il che costerebbe un sacco di tempo.
Quindi si potrebbe memeorizzare gli stud e i doce in tabelle separate.
Ora anzichè findere `Studnetne` e `docente` in `Persona` andiamo a creare tre tabelle, ovvero, tre classi separate.

Come possiamo collegare queste tre classi senza generalizzazione: con due associazioni, aggiunedo vicnoli `1..1` su Persona su vincoli stu_isa_pers e con vincolo `0..1`.
Sull'altra assoc. doc_isa_pers si aggiunge un vincoli accanto a Persona `1..1` e un vicnolo accanto a `Docente` `0..1`.
Ora dobbiamo fare un altra cosa obbligatoria:
Aggiungere due `{id}` sui vincoli accanto a Persona `1..1` su entrambe le assoc.
Mentre le associazioni tra Studente e corso di Laurea con i vincoli rimangono i dentici stessa cosa per l'assoc. tra Docente e Dipartimento e i loro vincoli.

Ma se mettiamo il vincolo `{disjoint}` sulla generalizzazione? 
La situazione cambia, ci vuole un vincolo esterno perché non si può espriemere:
I vincoli esterni e in questo caso si chiama vincoli di disgiunzione; vuol dire non devono esistere una `p:Persona`, `s:Studente`, `d:Docente` e `(p,s):stu_isa_pers` e `(p,d): doc_isa_pers`.
Abbiamo dovuto espriemrlo cosi perchè non si può espriemere nel diagramma.
Stssa cosa se c'è il complete:
si cihama vincolo di completezza; 
```plain text
per ogni p:Persona:
- esiste s:Studente tale che  (s,p):stud_isa_pers
- oppure esiste d:Docente tale che (p,d):doc_isa_pers
```

Vediamolo su [[Esercitazione GO|go]]:


Ora che abbiamo fatto la ristrutturazione ci mancano le chiavi primarie o identificatori di classe:

![[Screenshot 2025-07-09 at 12-52-22 Meet - bmb-xnne-ahh.png|500x170]]
 L'ultimo passo della ristruttturazione è: scegliere un identificatore primario per ogni classe.
 La metodologia è che se nella classe c'è un `{id}` allora quella diventa quell'attributo un identificatore primario. 
 Il vincolo `1..1{id}` serve quindi per identificare lo studente che è identificato dal codice fiscale della Persona quindi dall'attributo Univoco della classe padre 

Se nella classe non esiste un id allora posso aggiungerlo ad esempio se in corsoDILaurea c'è solo l'attributo nome ma ci devono essere coris di laurea con lo stesso nome allora si aggiunge un attributo `id` e si mette il vincolo `{id}` accanto a questo attributo.
Questi identificatori artificiali non cambiano nulla, è solo un escamotage tencologico.

