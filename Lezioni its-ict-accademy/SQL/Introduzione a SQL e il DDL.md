# Introduzione
Nella [[Lezione 1; Introduzione e modello relazionale|lezione precedente]] abbiamo costruito le fondamenta del modello relazionale: tabelle, attributi, chiavi primarie e [[Lezione 1; Introduzione e modello relazionale#I vincoli foreign key (integrità referenziale)|foreign key]]. Ora dobbiamo dotarci di uno strumento per *parlare* con il database, ovvero un linguaggio che ci permetta di creare strutture, inserire dati e interrogarli. Questo linguaggio è **SQL**.
## Introduzione a linguaggio SQL.
SQL è un linguaggio di riferimento per le basi di dati relazionali, in origine veniva chiamato Structured Query Language ora solo SQL.
Nasce nel 1974, la prima versione come linguaggio di interrogazione di System R (IBM).
Nel 1983 diventa uno standard de-facto e nel 1986 diventa anche lo standard ANSI con costruttori base (SQL-86). 
Nel 1989 viene aggiunta dai costruttori la gestione di integrità referenziale (SQL-89).

In seguito, nel 1992 fu introdotto di un grande numero di funzionalità (SQL-92 o SQL-2).
Benché era ed è tutt'ora un linguaggio ricco e complesso non tutti i DBMS commerciali non implementano tutto il linguaggio SQL.
dal 1999 fino al 2011 fu rilasciato diverse edizioni del SQL: SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011.
- compatibile con SQL-2, ma offre molte funzionalità in più
-  suddiviso in parti: SQL/XML (gestione XML), etc.
-  ancora lontano dall’essere adottato dai DBMS commercial

Noi vedremo postgresql perché è implementato in quasi tutti i database commerciali, imparando postgresql impareremo anche SQL.
### Architettura a 3 livelli dei DBMS (Standard ANSI/SPARC) 
Un DBMS non è un unico blocco monolitico, ma si struttura in 3 livelli:

#### 1. **Livello interno (fisico):** 
 Si occupa di **come i dati sono memorizzati fisicamente**: ==file sequenziali, file hash, indici B-tree, pagine di memoria.==
 È il livello più vicino all'hardware ed **è completamente nascosto sia agli sviluppatori che agli utenti:** ==né le [[Query|query]] né i modelli logici si preoccupano di come i dati siano effettivamente salvati.==
	  ^livelloInterno
> [!example] **Analogia:** 
> Pensa a come Linux gestisce il filesystem: 
> i file sono sequenze di byte su disco, ma noi li vediamo come cartelle e documenti attraverso l'interfaccia grafica. 
> ==Il livello interno è quella sequenza di byte — reale, ma invisibile nella pratica quotidiana.==
#### 2. **Livello logico (concettuale):**  ^livelloLogico
È il livello del **[[Lezione 1; Introduzione e modello relazionale|modello relazionale]]**: 
- ==qui i dati vengono descritti come **tabelle con attributi e vincoli**.==
    
- ==Fornisce una visione **astratta e indipendente** dalla memorizzazione fisica.==
    
- È il livello su cui lavorano principalmente i **DDL (CREATE TABLE, CREATE DOMAIN, ALTER TABLE, …)** e i **vincoli**.
  
	   
- ==In altre parole i file sono organizzati in modo sconosciuto per gli sviluppatori che li visualizzano come tabelle.==
	
> [!info] Title
> È qui che agiscono i **DDL per CREATE VIEW** e le **query DML per interrogare le viste**.

```sql
-- Esempio: definizione a livello logico 
CREATE TABLE Docente ( 
	mat INT PRIMARY KEY, 
	cognome VARCHAR(50), 
	nome VARCHAR(50), 
	email VARCHAR(100) 
);
```
> [!example] **Analogia con Linux**
>    Su Linux è la stessa cosa le cartelle su Linux sono file che quando c'è uno slash finisce il file e noi vediamo le cartelle su interfaccia grafica

#### 3. **Livello esterno (viste):**  ^livelloEsterno
- ==**Il livello esterno permette di presentare agli utenti **porzioni personalizzate** del database, senza esporre l'intera struttura logica.**==
    
- Le **viste** non sono tabelle reali: 
	- ==sono *query salvate* che proiettano e trasformano i dati sottostanti.==
    
- Servono principalmente a due scopi:
	1.  **Semplificazione** — ==un utente vede solo i campi che gli interessano;==
	2. **Sicurezza** — ==un utente con privilegi ridotti non accede a colonne sensibili (es. email, stipendio).==
        
	- È qui che agiscono i **DDL per CREATE VIEW** e le **query DML per interrogare le viste**.
	  

> [!example] Esempio concreto (dalle slide)
> Dalla join tra le tabelle `Docente`, `Corso` e `Incarico` si può costruire una vista `InfoCorsi` che mostra corso, aula, cognome e nome del docente — senza che l'utente debba conoscere le tre tabelle separate, né scrivere la join ogni volta.

> [!info] SQL e i livelli dell'architettura
> SQL fornisce costrutti per operare su entrambi i livelli superiori:
> - **Livello logico** → DDL (`CREATE TABLE`, …) e DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
> - **Livello esterno** → DDL per le viste (`CREATE VIEW`) e DML per interrogarle


## Avviare PostgreSQL tramite Docker 
Prima di lavorare con il database, è necessario avviare il container Docker che ospita PostgreSQL e accedervi. 
Il flusso si divide in tre fasi: 
1. avvio del container, 
2. accesso alla shell Linux interna, 
3. connessione a PostgreSQL.
### 1. Avviare e accedere al container 
Se il container è già in esecuzione, è sufficiente aprire una shell interattiva al suo interno con:  
```docker
docker exec -it its_postgresql bash
```
A questo punto ci troviamo dentro l'ambiente Linux virtualizzato del container.

### 2. Connettersi a PostgreSQL

Spostarsi nella directory 
`/home`: 
```shell 
cd /home 
```

> [!faq] **Perché `/home`?**  
> **È una convenzione:** 
> - ==`/home` è la directory di lavoro dell'utente nell'ambiente Linux del container.== 
> Non è strettamente necessario trovarsi lì per lanciare `psql`, ma è una buona abitudine partire da una directory "neutra" e ben definita

Dopodiché avviare il client PostgreSQL con l'utente `postgres`: 
```shell 
psql -U postgres
```


Da questo momento ci troviamo dentro la shell interattiva di PostgreSQL.

##### Risoluzione dei problemi: container non in esecuzione

Può capitare — soprattutto dopo un log-out da Docker Desktop o un riavvio della macchina — che il comando `docker exec` restituisca questo errore:
```shell
Error response from daemon: container is not running
```
Questo messaggio indica che il container specificato **esiste**, ma **non è attualmente in esecuzione**, anche se Docker Desktop risulta visivamente "aperto"
Per prima cosa, verificare lo stato di tutti i container con:
```docker
docker ps -a
```
**Il flag `-a`:** 
==mostra anche i container arrestati.== 
Nella colonna `STATUS` è possibile leggere lo stato attuale di ciascun container.

> [!tip] **Soluzione rapida** 
> Se il container risulta semplicemente fermo (nessun errore), è sufficiente riavviarlo:  
> ```docker 
> docker start its_postgresql  
> ```
>  Poi accedervi normalmente con `docker exec -it its_postgresql bash`.

> [!warning] **Se il container si arresta subito dopo l'avvio Il problema è probabilmente di configurazione.** 
> Le cause più comuni sono: 
>  - porta già occupata da un altro processo  
>  - errore nel file `docker-compose.yml` 
>  - variabile d'ambiente mancante o errata 
>  - volume mancante o file corrotto  
>  - Per diagnosticare, consultare i log del container: 
>  ```docker  
>  docker logs its_postgresql 
>  ```

## Data Definition Language (DDL)
Detto questo ora entriamo nel dettaglio e vediamo cosa è il DDL.
SQL non è un unico linguaggio monolitico ma si suddivide in più sotto-linguaggi, ciascuno con uno scopo preciso.
Il primo fra questi è il DDL (Data Definition Language) ed: 
- ==la componente del linguaggio SQL che permette di **definire la struttura del database**.==  
In altre parole il DDL consiste nei comandi SQL per creare e aggiornare gli oggetti nel database come tabelle, indici, viste, stored procedures e triggers(questi due ultimi aspetti in realta li approfondiremo in seguito poiché sono concetti avanzati di SQL).
Ma cos’è un database?  
- ==Un database è un insieme di tabelle popolate di dati.==

I comandi del DDL sono: 
1. [[#Creare e navigare un database|`CREATE`]]: per [[#Creare una tabella|creare una tabella]] nel database o il db stesso 
2. [[#1. `Alter Table`|`ALTER`]]: per cambiare la struttura del database
3. [[#2. `DROP`|`DROP`]]: Per rimuovere un oggetto esistente dal database(es: una tabella o un campo di una tabella o anche il db stesso). 
4. [[#`TRUNCATE TABLE`|`TRUNCATE`]]: per rimuovere tutti i record(righe) da una tabella
Gli altri sotto-linguaggi di SQL sono: 
- **DML (Data Manipulation Language)** → `INSERT`, `UPDATE`, `DELETE` — manipola i dati all'interno delle tabelle
- **DQL (Data Query Language)** → `SELECT` — interroga e recupera dati dal database
- **DCL (Data Control Language)** → `GRANT`, `REVOKE` — gestisce permessi e accessi
- **TCL (Transaction Control Language)** → `COMMIT`, `ROLLBACK` — gestisce le transazioni
In questo momento ci troviamo nel DDL. 
DML e DQL li affronteremo nelle sezioni successive — troverai i riferimenti man mano che avanziamo.

#### Recuperare la definizione DDL di una tabella

Dopo aver creato o modificato una tabella è possibile recuperarne la definizione DDL completa con:
```PostgreSQL
-- In PostgreSQL tramite psql
\d nome_tabella
```

>[!help] **A cosa serve?** 
>È utile quando si vuole ispezionare la struttura esatta di una tabella — vincoli inclusi — oppure quando si vuole replicare una tabella esistente su un altro database. In DBeaver e altri client grafici questa informazione è accessibile direttamente dall'interfaccia senza scrivere query.
### Preparare l'ambiente di lavoro 
Prima di entrare in PostgreSQL (per i passi di accesso via Docker vedi [[#Avviare PostgreSQL tramite Docker|sezione precedente]]), creiamo la struttura di cartelle per salvare i nostri file SQL:  
```shell
mkdir "base dati"  
cd "base dati" 
mkdir esempi 
cd esempi touch esami.sql 
```
 Apriamo subito `esami.sql` con il nostro editor preferito (VS Code, Sublime Text…): 
 - scriveremo qui le istruzioni DDL e le eseguiremo su PostgreSQL.


### Il prompt di PostgreSQL

Una volta connessi con `psql -U postgres`, il terminale mostrerà:
```shell
psql (versione) Type "help" for help.
postgres=#
```

Il prompt `postgres=#` comunica tre cose:
- sei connesso al DBMS PostgreSQL
- l'utente attivo è `postgres`
- il `#` indica che stai operando con privilegi di superutente

Da questo punto in poi, tutto ciò che digiti è un comando PostgreSQL.

> [!NOTE] **Nota:**
> - Da questo punto in poi, tutti i comandi che digiterai saranno **comandi PostgreSQL**.
 >   
>- Puoi eseguire query, creare tabelle, domini, viste, ecc.

### DDL — Creazione di Database, Schemi e Tabelle
Il DDL mette a disposizione tre costrutti principali per definire la struttura del database:

| Comando           | Cosa crea                                  |
| ----------------- | ------------------------------------------ |
| `CREATE DATABASE` | ==un nuovo database==                      |
| `CREATE SCHEMA`   | ==un namespace logico dentro il database== |
| `CREATE TABLE`    | ==una tabella dentro uno schema==          |
#### Creare e navigare un database

```sql 
CREATE DATABASE nome_database [opzioni]; 
```

> [!info] #### Case Sensitivity in SQL
> - **SQL è case-insensitive**: le parole chiave (`CREATE`, `SELECT`, `WHERE`, …) possono essere scritte sia in maiuscolo che in minuscolo, senza differenza.
 >   
>- Per convenzione, nei manuali e in ambito professionale si scrivono **maiuscole** per distinguerle meglio dai nomi di tabelle e colonne.
 >   
>- L’unico elemento davvero obbligatorio è il **punto e virgola `;`**, che indica la fine dell’istruzione (come in JavaScript).
>> [!remember] **Nota:**
>>  i nomi di **tabelle e colonne** possono diventare case-sensitive **solo se scritti tra doppi apici** (`"Studente"` è diverso da `"studente"`). 
>>  Se non si usano apici, PostgreSQL li converte in minuscolo di default.

**Per visualizzare i database disponibili:**
```shell
postgres=# \l
```

> [!example] **Esempio della creazione di un database:**
> per creare un database:
> ```shell
> postgres=# create database esami;
> CREATE DATABASE
> postgres=#
> ```
>> [!note] **Nota:** a questo punto non siamo ancora entrati nel database creato.

> [!warning] Non siamo ancora *dentro* il database — l'abbiamo solo creato. 
> Per connettersi al database appena creato: 
> ```sql 
> postgres=# \c esami 
> You are now connected to database "esami" as user "postgres". 
> ```

##### Il comportamento del prompt

Se digiti un comando incompleto o non valido, il prompt cambia forma per segnalarlo:


`postgres=#`:  ==pronto per un nuovo comando== 
`postgres-#`: ==aspetta la fine di un comando incompleto== 
`postgres(#`:  ==parentesi aperta non chiusa==



Finché non compare `postgres=#`, PostgreSQL non ha ancora eseguito nulla — sta aspettando che tu completi l'istruzione.

### Gli schemi 
Uno **schema** è:
==un sottoinsieme logico di tabelle all'interno di un database==. 
Un namespace che permette di:
- ==raggruppare tabelle affini== 
- ==gestire più facilmente autorizzazioni e query complesse.== 
```sql 
CREATE SCHEMA nome_schema [opzioni]; 
```
 
>[!example] **Esempio concettuale — eBuy** 
> In un database per una piattaforma di e-commerce potremmo avere: 
>  - schema `utenti` → ==tabelle relative agli account== 
>  - schema `oggetti` → ==tabelle relative ai prodotti in vendita.==
>  Separare i contesti riduce il rischio di naming conflict e semplifica la gestione dei permessi per ruoli diversi.
 

 

##### Creare una tabella 
 Sintassi generale:
  ```sql 
  CREATE TABLE [nome_schema.]nome_tabella ( 
  nome_attributo dominio [vincoli di dominio], 
  nome_attributo dominio [vincoli di dominio], 
  ... 
  [vincoli intra-relazionali], -- es. PRIMARY KEY su più colonne 
  [vincoli inter-relazionali] -- es. FOREIGN KEY ); 
  ``` 
  - `[nome_schema.]` → **opzionale;** ==se omesso viene usato lo schema di default== 
  - `dominio` → tipo di dato (`INTEGER`, `VARCHAR`, `DATE`, …) o un dominio definito in precedenza 
  - [[#Lezione 1; Introduzione e modello relazionale Il linguaggio SQL Vincoli di dominio Vincoli di ennupla Vincoli di dominio|`vincoli di dominio`]] → `NOT NULL`, `UNIQUE`, `CHECK`, … 
  - [[#Vincoli di integrità referenziale|`vincoli inter-relazionali`]] → `FOREIGN KEY … REFERENCES` 
  >[!example] **Esempio — Corso e Incarico** 
  > ```sql 
  > CREATE TABLE Corso ( 
> 	 codice INTEGER NOT NULL, 
> 	  nome CHARACTER VARYING(100) NOT NULL, -- stringa fino a 100 caratteri 
> 	  aula CHARACTER VARYING(10) NOT NULL, 
> 	   PRIMARY KEY (codice)
>    );
>    CREATE TABLE Incarico (
> 	   docente INTEGER NOT NULL,
> 	   corso INTEGER NOT NULL,
> 	   PRIMARY KEY (docente, corso), 
> 	   FOREIGN KEY (docente) REFERENCES Docente(matr),
> 	   FOREIGN KEY (corso) REFERENCES Corso(codice)
> );
> ```
> 
  > 	   
  
  
   `Incarico` è una **tabella di associazione**: 
   - ==la sua chiave primaria è composta da due foreign key, il che garantisce che ogni coppia docente-corso sia unica.==

### Domini SQL predefiniti

Quando definiamo un attributo in una `CREATE TABLE`, dobbiamo specificare il suo **dominio** — ovvero il tipo di dato che quell'attributo può contenere. 
SQL mette a disposizione una serie di domini predefiniti, organizzabili in cinque famiglie.

#### 1. Numeri

| Categoria             | Tipi                                           | Quando usarli                                                 |
| --------------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| Interi                | `INTEGER`, `SMALLINT`                          | contatori, ID, quantità senza decimali                        |
| Decimali esatti       | `NUMERIC(prec, scala)`, `DECIMAL(prec, scala)` | valori finanziari, voti, misure precise                       |
| Decimali approssimati | `FLOAT(prec)`, `REAL`, `DOUBLE PRECISION`      | calcoli scientifici dove la precisione assoluta non è critica |
>[!example] `NUMERIC(prec, scala)` `NUMERIC(5, 2)` accetta numeri fino a `999.99` — **5 cifre totali, di cui 2 dopo la virgola.** 
>==Usalo per prezzi o voti dove l'arrotondamento non è accettabile.==

#### 2. Stringhe
```sql
CHARACTER VARYING(100)  -- o VARCHAR(100): stringa fino a 100 caratteri
CHARACTER(10)           -- o CHAR(10): stringa di lunghezza fissa
TEXT                    -- stringa di lunghezza illimitata
```

>[!note] `CHAR` vs `VARCHAR` vs `TEXT`
>
>- `CHAR(n)`: 
>	- ==occupa sempre _n_ caratteri in memoria, anche se la stringa è più corta== 
>	- ==utile per codici a lunghezza fissa come il codice fiscale.==
>- `VARCHAR(n)`: 
>	- ==occupa solo lo spazio necessario, fino a un massimo di _n_.==
>- `TEXT`: 
>	- **non ha limite di lunghezza:** 
>		- ==comodo per descrizioni o contenuti liberi.==

#### 3. Istanti e intervalli temporali
```sql
DATE -- solo la data (anno, mese, giorno)
TIME -- solo l'ora (ora, minuti, secondi)
TIMESTAMP -- data e ora insieme
INTERVAL -- durata di tempo (es. '2 hours', '3 days')
```

>[!example] Nella tabella `Incarico` della lezione precedente I campi `data_inizio DATE` e `data_fine DATE` sono un esempio concreto: 
>- ==memorizzano solo la data senza informazioni sull'ora.==

#### 4. Booleani
Introdotto con SQL:1999. 
Usato per flag e stati binari (es. `attivo BOOLEAN NOT NULL DEFAULT TRUE`).
```sql
BOOLEAN  -- valori: TRUE, FALSE, NULL
```

#### 5. Dati binari di grandi dimensioni

Lo standard SQL prevede `CLOB` (testo) e `BLOB` (binario) per memorizzare oggetti di grandi dimensioni come immagini, audio e documenti.

> [!note] PostgreSQL usa `BYTEA` PostgreSQL non implementa direttamente `BLOB`, ma offre il tipo `BYTEA` per memorizzare sequenze di byte arbitrarie. 
> Per file molto grandi esiste anche il meccanismo **Large Object** con funzioni dedicate.

### Domini personalizzati ed ENUM

Oltre ai tipi predefiniti, SQL permette di creare domini su misura tramite `CREATE DOMAIN` e `CREATE TYPE`. 
È lo stesso principio che abbiamo già visto nella ristrutturazione e implementazione dei diagrammi UML in Python: 
- ==anche qui possiamo definire tipi di dato specializzati che rispecchiano esattamente il dominio del problema che stiamo modellando.==

> [!example] **Prendiamo un esempio concreto: il codice fiscale.**
>  Sappiamo che è una sequenza di esattamente 16 caratteri alfanumerici che segue un pattern preciso. 
>  Usare `VARCHAR(16)` come tipo del campo `codice_fiscale` sarebbe sbagliato sia concettualmente che praticamente — ==lascerebbe al client troppa libertà di inserimento, consentendo valori formalmente validi per il tipo ma semanticamente privi di senso.== 
> Per risolvere questo problema si usa `CREATE DOMAIN`:
> ```sql
> CREATE DOMAIN CodiceFiscale AS CHAR(16) -- o anche varchar(16)
>     CHECK (VALUE ~ '[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]');
> ```
> In questo modo forziamo il rispetto della regex direttamente a livello di tipo: 
> - ==qualsiasi tentativo di inserire un valore che non rispetti il pattern verrà rifiutato dal DBMS.==

Lo stesso principio si applica con `CREATE TYPE`. Supponiamo di dover modellare un campo genere in un form lato server: 
- **invece di usare un `VARCHAR` libero, definiamo un tipo enumerativo che vincola esplicitamente i valori ammessi**: 
```sql
CREATE TYPE genere AS ENUM ('M', 'F', 'non-binary', ...);
```

>[!note] **`ENUM` vs `CHECK`** 
>Usare `ENUM` è concettualmente più pulito di aggiungere un vincolo `CHECK (valore IN ('M', 'F', ...))` su un `VARCHAR`: 
>- ==il tipo diventa parte dello schema e può essere riutilizzato su più tabelle senza ripetere il vincolo ogni volta.==

`CREATE TYPE` non serve solo per gli enumerativi — permette anche di definire **tipi record:**
- ==ovvero tipi composti da più campi.== 
Supponiamo di dover modellare l'indirizzo di un utente:
```sql
CREATE TYPE indirizzo AS (
    via       VARCHAR(100),
    n_civico  VARCHAR(10),
    cap       cod_postale,  -- supponiamo sia un dominio personalizzato
    citta     VARCHAR(50)
);
```

>[!faq] **Quando usare un tipo record invece di una tabella separata?** 
>Un tipo record è utile quando il dato composto non ha identità propria e non ha senso interrogarlo indipendentemente. 
>L'indirizzo di un utente, ad esempio, esiste solo in relazione all'utente stesso — non ha bisogno di una tabella dedicata con chiave primaria e foreign key.

#### Modifica e cancellazione dei domini

Esattamente come le tabelle, anche i domini creati dall'utente possono essere modificati o eliminati dopo la loro creazione.

Per la modifica si usa [[#1. `Alter Table`|`ALTER`]]:
```sql
ALTER DOMAIN nome_dominio azione;
ALTER TYPE nome_dominio azione;
```

Per la cancellazione si usa [[#2. `DROP`|`DROP`]]:
```sql
DROP DOMAIN nome_dominio;
DROP TYPE nome_dominio;
```

> [!note] Analogia con [[#1. `Alter Table`|`ALTER TABLE`]] e [[#2. `DROP`|`DROP TABLE`]] 
> La logica è identica a quella che abbiamo visto per le tabelle: 
> 1. ==`ALTER` per modificare la struttura,== 
> 2. ==`DROP` per eliminare definitivamente.== 
> Vale la stessa regola pratica: 
> - ==se un dominio è già utilizzato da una colonna in una tabella esistente, PostgreSQL potrebbe rifiutare il `DROP` per proteggere l'integrità dello schema.== 
> In quel caso si usa `DROP DOMAIN nome_dominio CASCADE`.

> [!warning] Implementazione non standard `CREATE TYPE` e i comandi correlati (`ALTER TYPE`, `DROP TYPE`) sono implementati in modo non uniforme tra i vari DBMS. La sintassi mostrata qui è quella di PostgreSQL — consultare sempre la documentazione del DBMS in uso prima di usarli in produzione.
### Creazione di tabelle valori di defualt
Quando si inserisce una nuova riga in una tabella, ==non è sempre necessario specificare un valore per ogni colonna — a patto che quella colonna abbia un **valore di default** definito.== 
Se durante un inserimento o una modifica il valore di una colonna viene omesso, PostgreSQL usa automaticamente il default dichiarato.

La sintassi è semplice e si integra direttamente nella definizione della colonna:
```sql
colonna tipo DEFAULT valore
```

Esempio: 
```sql
CREATE TABLE Impiegato (
    nome      ...,
    cognome   ...,
    stipendio INTEGER DEFAULT 0,
    ...
);
```

Se durante un `INSERT` non viene specificato alcun valore per `stipendio`, PostgreSQL assegna automaticamente `0`. 
Il default può essere combinato con altri vincoli sulla stessa colonna:
```sql
stipendio INTEGER DEFAULT 1000 CHECK (stipendio >= 0)
```

In questo caso il [[Lezione 1; Introduzione e modello relazionale#^colonna|campo]] `stipendio` è un intero con valore di default inziale a `1000`; quindi significa che il valore di partenza delle [[Lezione 1; Introduzione e modello relazionale#^ennuple|ennuple]] di stipendio sarà di `1000`  

> [!note] Ordine dei vincoli 
> L'ordine `DEFAULT` → `CHECK` non è casuale: 
> - ==prima si stabilisce il valore di partenza, poi si verifica che rispetti i vincoli imposti.== 
> **Un default che violasse il proprio `CHECK` sarebbe un errore di progettazione** — ==PostgreSQL lo segnalerebbe al momento dell'inserimento.==

> [!faq] Cosa succede se non si definisce nessun default? 
> 1. ==Se una colonna non ha default e non è dichiarata `NOT NULL`, PostgreSQL inserisce automaticamente `NULL`.== 
> 2. ==Se invece è `NOT NULL` senza default, l'inserimento senza quel valore produce un errore.==
#### [[Lezione 1; Introduzione e modello relazionale#Il linguaggio SQL Vincoli di dominio Vincoli di ennupla|Vincoli di dominio]] 

==I vincoli di dominio permettono di imporre restrizioni sui valori che un attributo può assumere.== 
**Vengono controllati automaticamente dal DBMS prima di ogni inserimento o modifica:** 
- ==se una riga viola il vincolo, l'operazione non ha luogo e viene generato un errore.==

Si dichiarano inline nella definizione della colonna tramite la clausola `CHECK`:
```sql
CREATE TABLE Impiegato (
    nome      VARCHAR(100) NOT NULL,
    cognome   VARCHAR(100) NOT NULL,
    stipendio INTEGER DEFAULT 0
		  CHECK (stipendio >= 0),
    ...
);
```
In questo esempio ==ogni [[Lezione 1; Introduzione e modello relazionale#^ennuple|ennupla]] della tabella `Impiegato` deve soddisfare la condizione `stipendio >= 0`.== 
Un tentativo di inserire uno stipendio negativo verrebbe rifiutato dal DBMS prima ancora di toccare i dati.
> [!note] **`CHECK` e `DEFAULT` insieme** 
> Come abbiamo visto nella sezione precedente, `DEFAULT` e `CHECK` possono coesistere sulla stessa colonna. 
> L'ordine logico è: 
> - ==PostgreSQL applica prima il valore di default (se il campo è omesso), poi verifica il vincolo `CHECK`.== 
> Il default `0` qui soddisfa già il vincolo `>= 0`, quindi è una definizione coerente.

> [!faq] Il `CHECK` viene rispettato anche in fase di modifica? Sì — non solo negli `INSERT` ma anche negli `UPDATE`. Se si tenta di aggiornare lo stipendio di un impiegato a un valore negativo, PostgreSQL rifiuta la modifica esattamente come farebbe con un inserimento non valido.
#### Vincoli di chiave:
I vincoli di chiave garantiscono l'**unicità** delle ennuple all'interno di una relazione. SQL distingue due tipi: la chiave primaria (`PRIMARY KEY`) e le chiavi alternative (`UNIQUE`).

##### Chiave primaria
==La chiave primaria si dichiara in due modi equivalenti.== 
Se coinvolge un **singolo attributo**, si può scrivere inline:
```postgresql
matricola INTEGER PRIMARY KEY  -- implica NOT NULL automaticamente
```
Se invece coinvolge **più attributi**, va dichiarata separatamente a fondo tabella:
```sql
PRIMARY KEY (cognome, nome, nascita)
```
posso anche scrivere:
```postgresql
matricola integer primary key
```

>[!info] **`PRIMARY KEY` implica `NOT NULL`** 
>==Dichiarare un attributo come chiave primaria rende superfluo aggiungere `NOT NULL` esplicitamente — PostgreSQL lo impone in automatico.== 
>Una chiave primaria nulla non avrebbe senso: 
>- **non potrebbe identificare univocamente nessuna ennupla.**

##### Chiavi alternative — `UNIQUE`
==Una tabella può avere UNA SOLA chiave primaria, ma può avere **più chiavi alternative**, dichiarate con `UNIQUE`.== 
Esempio completo:
```sql
CREATE TABLE Studente (
    matricola INTEGER NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    nascita DATE,
    cf CHARACTER(16) NOT NULL,
    PRIMARY KEY (matricola),
    UNIQUE (cf),                    -- chiave alternativa su singolo attributo
    UNIQUE (cognome, nome, nascita) -- chiave alternativa su più attributi
);
```

>[!faq] **Qual è la differenza pratica tra `PRIMARY KEY` e `UNIQUE`?** 
>Entrambi impongono unicità, ma `PRIMARY KEY` impone anche `NOT NULL` ed è unica per tabella. `UNIQUE` invece ammette `NULL` (a meno che non si aggiunga `NOT NULL` esplicitamente) e può comparire più volte nella stessa tabella. In sostanza: la chiave primaria è _l'_ identificatore della riga, le chiavi `UNIQUE` sono identificatori alternativi validi ma secondari.

In sostanza in questo esempio vediamo all'atto pratico la differenza tra questi due vincoli di chiave: 
1. `PRIMARY KEY` → ==identifica **univocamente** ogni riga della tabella ed è **obbligatoria** (NOT NULL)==. 
	- **Ogni tabella ne ha esattamente una.**
	- ==La matricola è l'identità dello studente nel database.==
2. `UNIQUE` → ==garantisce che non esistano **due righe con lo stesso valore** su quell'attributo, ma non è il "fulcro" dell'identità della riga.== 
	- ==Il codice fiscale è unico per persona, ma nel contesto del database universitario non è l'identificatore principale — lo è la matricola.==

>[!note] **Chiavi surrogate vs chiavi naturali** 
>**La scelta della chiave primaria non è sempre ovvia.** 
>In teoria il codice fiscale identificherebbe univocamente uno studente quanto la matricola — eppure si preferisce la matricola. Perché?
>
>Si distinguono due tipi di chiave:
>
>- **Chiave naturale** — ==esiste già nel dominio reale (es. il codice fiscale)==. 
>	- Porta con sé informazioni sulla persona, il **che la rende problematica per la privacy e costosa da replicare come foreign key (16 byte contro 4 byte di un intero, su ogni join tra migliaia di righe).**
>- **Chiave surrogata** — ==generata artificialmente dal sistema (es. la matricola).== 
>	- È anonima, compatta e stabile nel tempo.
>
>Per questi motivi le chiavi surrogate sono generalmente preferibili nella progettazione di database reali: 
>- ==separano l'identità nel database dall'identità nel mondo reale, minimizzando l'esposizione di dati sensibili e massimizzando le prestazioni.==

^838a2d

###### Visualizzare le tabelle e primo esempio completo

Per ispezionare la struttura del database direttamente dal terminale PostgreSQL si usano i metacomandi `\d`:
```shell
esami=# \d -- elenca tutte le tabelle del database
esami=# \d nome_tabella -- mostra la struttura di una tabella specifica
```
Questi non sono comandi SQL ma **metacomandi di `psql`** — vengono interpretati direttamente dal client prima di raggiungere il DBMS.

Come primo esempio completo che mette insieme tutto ciò che abbiamo visto finora — tipi, `NOT NULL`, `CHECK`, `DEFAULT` — definiamo la tabella `esame`:

```sql
CREATE TABLE esame (
    studente INTEGER NOT NULL,
    corso    VARCHAR NOT NULL,
    data     DATE    NOT NULL,
    voto     INTEGER NOT NULL
		 CHECK (voto >= 18 AND voto <= 30),
    lode BOOLEAN NOT NULL
);
```

>[!note] **Cosa sta succedendo qui**
>
>- `studente` e `corso` ==referenzieranno in futuro le tabelle `Studente` e `Corso` tramite foreign key== — **per ora li lasciamo semplici.**
>- Il `CHECK` su `voto` ==garantisce che il voto sia sempre compreso tra 18 e 30, rifiutando qualsiasi inserimento fuori range.==
>- `lode` è un booleano — ==`TRUE` se il voto è con lode, `FALSE` altrimenti.==

### SQL e modello relazionale

C'è un dettaglio sottile ma importante che vale la pena sottolineare:
- ==**una tabella SQL non è automaticamente una relazione** nel senso matematico del termine.== 
Il modello relazionale, come abbiamo visto, richiede che ogni ennupla sia unica — ma SQL di per sé non lo garantisce. 
Senza una chiave definita, una tabella può contenere righe duplicate:
```sql
-- Senza PRIMARY KEY: ammette duplicati ❌
CREATE TABLE Studente (
    matr    INTEGER      NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    nome    VARCHAR(100) NOT NULL
);
```


| matr | cognome | nome   |
| ---- | ------- | ------ |
| 1000 | Rossi   | Mario  |
| 1000 | Rossi   | Mario  |
| 1001 | Verdi   | Giulia |
Aggiungere una `PRIMARY KEY` riporta la tabella al comportamento corretto di una relazione:
```sql
-- Con PRIMARY KEY: ogni ennupla è unica ✅
CREATE TABLE Studente (
    matr    INTEGER      NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    nome    VARCHAR(100) NOT NULL,
    PRIMARY KEY (matr)
);
```

>[!remember] Regola pratica 
>==Ogni tabella dovrebbe avere sempre una chiave primaria.== 
>Non definirla è tecnicamente lecito in SQL, ==ma produce una struttura dati che non rispetta il modello relazionale e che è molto più difficile da interrogare e mantenere.==

### Vincoli di integrità referenziale

Abbiamo già incontrato le foreign key nella [[Lezione 1; Introduzione e modello relazionale#Vincoli di integrità|lezione sul modello relazionale]]. 
Vediamo ora come si traducono concretamente in SQL, usando un esempio completo.

Prendiamo un dominio di un'officina meccanica composto da quattro tabelle: 
1. `Officina`, 
2. `Veicolo`, 
3. `Riparazione` 
4. `RicambioRip`. 
Le relazioni tra loro seguono questa logica: 
- ==una riparazione è effettuata da un'officina su un veicolo, e ogni riparazione può richiedere uno o più ricambi.==
```sql
CREATE TABLE Officina (
    nome      VARCHAR(100) NOT NULL,
    indirizzo VARCHAR(500) NOT NULL,
    PRIMARY KEY (nome)
);

CREATE TABLE Veicolo (
    targa CHAR(8)      NOT NULL,
    tipo  VARCHAR(50)  NOT NULL,
    PRIMARY KEY (targa)
);

CREATE TABLE Riparazione (
    officina VARCHAR(100) NOT NULL,
    codice   INTEGER      NOT NULL,
    veicolo  CHAR(8)      NOT NULL,
    PRIMARY KEY (officina, codice),
    FOREIGN KEY (officina) REFERENCES Officina(nome),
    FOREIGN KEY (veicolo)  REFERENCES Veicolo(targa)
);

CREATE TABLE RicambioRip (
    officina VARCHAR(100) NOT NULL,
    rip      INTEGER      NOT NULL,
    ricambio CHAR(5)      NOT NULL,
    PRIMARY KEY (officina, rip, ricambio),
    FOREIGN KEY (officina, rip) REFERENCES Riparazione(officina, codice),
    FOREIGN KEY (ricambio)      REFERENCES Ricambio(codice)
);
```

La sintassi generale per una foreign key è:
```sql
FOREIGN KEY (attributi) REFERENCES Tabella(attributi_chiave)
```

>[!info] **Tabella padre e tabella figlia** 
>Nei vincoli di integrità referenziale si parla di **tabella padre** e **tabella figlia** per descrivere la gerarchia tra le tabelle coinvolte:
>
>- **Tabella padre** → ==la tabella referenziata, quella che contiene la `PRIMARY KEY` o `UNIQUE` a cui si punta.== 
>	- **Nel nostro esempio dell'officina, `Officina` e `Veicolo` sono tabelle padre.**
>- **Tabella figlia** → ==la tabella che referenzia, quella che contiene la `FOREIGN KEY`.== 
>	- **Nel nostro esempio, `Riparazione` è figlia sia di `Officina` che di `Veicolo`.**
>
>>[!remember] **Questa gerarchia ha conseguenze pratiche precise su cosa si può fare e in che ordine:**
>>
>>- ==non si può **creare** la tabella figlia prima del padre — la foreign key punterebbe nel vuoto==
>>- ==non si può **eliminare** il padre prima del figlio — si romperebbe l'integrità referenziale==
>>- ==non si può **inserire** una riga nella figlia con un valore che non esiste nel padre==
>
>In sostanza il padre deve sempre esistere prima del figlio, sia in fase di creazione dello schema che in fase di inserimento dei dati.
>>[!caution]  **Attenzione!! Non confondere questa relazione con la relazione is-a dell'OOP.** 
>>**Con is-a il figlio _eredita_ dal padre:**
>> - ==`Cane` is-a `Animale` significa che un cane è un tipo di animale.== 
>>Con le foreign key invece **il figlio _dipende_ dal padre ma rimane un'entità concettualmente distinta:** 
>>- ==`Riparazione` non è un tipo di `Officina`, semplicemente ogni riparazione deve riferirsi a un'officina che esiste.== 
>>In UML la differenza è netta: freccia di ereditarietà vs linea di associazione.

> [!ticket] **Regola fondamentale:** 
> ==Gli attributi di destinazione di una `FOREIGN KEY` devono necessariamente formare una chiave — `PRIMARY KEY` o `UNIQUE` — nella tabella referenziata.== 
> Non è possibile puntare a una colonna qualsiasi.

> [!example] **`RicambioRip` — foreign key composita** 
> **La tabella `RicambioRip` mostra un caso interessante:** 
> ==la foreign key verso `Riparazione` è **composita**, ovvero coinvolge due attributi insieme (`officina`, `rip`).== 
> ==Questo perché la chiave primaria di `Riparazione` è essa stessa composta da `(officina, codice)` — un singolo campo non sarebbe sufficiente a identificare univocamente una riparazione.==

### Modifica, cancellazione e reset di tabelle

Una volta creata una tabella, non è immutabile. 
SQL/PostgreSQL mettono a disposizioni almeno 3 statement diversi per modificare le tabelle e i loro campi ed ennuple: 
#### 1. `Alter Table`
`ALTER TABLE` è lo statement DDL usato per ==modificare la struttura di una tabella già esistente.== 
Permette di: 
1. ==[[#Aggiungere una colonna|aggiungere]],== 
2. ==[[#Eliminare una colonna|eliminare]] o [[#Modificare il tipo di una colonna|modificare]] colonne,== 
3. ==cambiare tipi di dato,== 
4. ==[[#Impostare o rimuovere un valore di default|gestire valori di default]],== 
5. ==[[#Aggiungere o eliminare un vincolo|aggiungere o rimuovere vincoli]]== 
6. ==[[#Rinominare una tabella o una colonna|rinominare tabelle o colonne]]==
Il tutto senza dover distruggere e ricreare la tabella da zero.
Sintassi generale:
```sql
ALTER TABLE nome_tabella azione;
```

###### Aggiungere una colonna
Per aggiungere un colonna la sintassi è: 
```sql
ALTER TABLE table_name ADD COLUMN column_name datatype [vincoli];
```


> [!example] **Esempio**
>```sql
> -- Esempio: aggiungere il campo email alla tabella Studente
>ALTER TABLE Studente ADD COLUMN email VARCHAR(100) NOT NULL;
>```
>In questo modo aggiungiamo una nuova colonna `email` con il tipo di dato `varchar(100)` e con il vincolo `not null` alla tabella `Studente`

Una variazione sul tema è quando dobbiamo aggiungere più colonne alla stessa tabella
```sql
ALTER TABLE table_name
  ADD (column_name datatype [vincoli],
       column_name datatype [vincoli],
       ...
       column_n  datatype [vincoli]);
```


> [!example] **Esempio**
>```sql
> ALTER TABLE Studente ADD (email Varchar(100) not null,
> citta varchar(225) not null,
> anno_nascita date not null,
> data_imm date not null)
>```

###### Eliminare una colonna
Per eliminare una colonna la sintassi è: 
```sql
ALTER TABLE nome_tabella DROP COLUMN nome_colonna;
```

> [!example] **Esempio**
>```sql
> -- Esempio: eliminare il campo email dalla tabella Studente
ALTER TABLE Studente DROP COLUMN email;
>```

>[!danger] **`DROP COLUMN` è irreversibile** 
>==Eliminare una colonna cancella anche tutti i dati in essa contenuti.== 
>**PostgreSQL non chiede conferma.**

###### Modificare il tipo di una colonna
```sql
ALTER TABLE nome_tabella ALTER COLUMN nome_colonna TYPE nuovo_tipo;
```


> [!example] **Esempio**
>```sql
> -- Esempio: allargare il campo nome da 100 a 200 caratteri
ALTER TABLE Studente ALTER COLUMN nome TYPE VARCHAR(200);
>```

>[!caution] **Compatibilità con i dati esistenti** 
>==Se la tabella contiene già dati, PostgreSQL verifica che siano compatibili con il nuovo tipo prima di applicare la modifica.== 
>**Convertire una colonna da `VARCHAR` a `INTEGER` fallisce se esistono righe con valori non numerici.**

###### Impostare o rimuovere un valore di default
```sql
-- altero la tabella per impostare un valore di defualt su una colonna
ALTER TABLE nome_tabella ALTER COLUMN nome_colonna SET DEFAULT valore;
-- altero la tabella per eliminare il valore di defualt da una colonna
ALTER TABLE nome_tabella ALTER COLUMN nome_colonna DROP DEFAULT;
```

> [!example] **Esempi**
>```sql
> -- Esempio: impostare un default a 0 per lo stipendio
>ALTER TABLE Impiegato ALTER COLUMN stipendio SET DEFAULT 0;
>-- Esempio: rimuovere il default
>ALTER TABLE Impiegato ALTER COLUMN stipendio DROP DEFAULT;
>```

###### Aggiungere o eliminare un vincolo
```sql
ALTER TABLE nome_tabella ADD CONSTRAINT nome_vincolo definizione_vincolo;
ALTER TABLE nome_tabella DROP CONSTRAINT nome_vincolo;
```

> [!example] **Esempio**
>```sql
>-- Esempio: aggiungere un CHECK sulla matricola
ALTER TABLE Studente ADD CONSTRAINT chk_matricola CHECK (matricola > 0);
>
>-- Esempio: eliminarlo
>ALTER TABLE Studente DROP CONSTRAINT chk_matricola;
>```

>[!help] **Perché dare un nome esplicito ai vincoli?** 
>==Il nome del vincolo viene usato nei messaggi di errore e — soprattutto — è necessario per poterlo eliminare con `DROP CONSTRAINT`.== 
>==Senza un nome esplicito PostgreSQL ne genera uno automatico difficile da ricordare.== 
>>[!ticket] **Nominare i vincoli è una buona abitudine di progettazione.**

###### Aggiungere una chiave primaria o una foreign key
```sql
ALTER TABLE nome_tabella ADD PRIMARY KEY (nome_colonna);
ALTER TABLE nome_tabella ADD FOREIGN KEY (nome_colonna) REFERENCES altra_tabella(colonna);
```

> [!example] **Esempio**
>```sql
> -- Esempio: aggiungere una primary key
ALTER TABLE Studente ADD PRIMARY KEY (matricola);
>-- Esempio: aggiungere una foreign key
>ALTER TABLE Esame ADD FOREIGN KEY (studente) REFERENCES Studente(matricola);
>```

###### Rinominare una tabella o una colonna
```sql
ALTER TABLE nome_tabella RENAME TO nuovo_nome;
ALTER TABLE nome_tabella RENAME COLUMN nome_colonna TO nuovo_nome;
```

> [!example] **Esempio**
>```sql
> -- Esempio: rinominare la tabella
ALTER TABLE Studente RENAME TO Alunno;
>
>-- Esempio: rinominare una colonna
>ALTER TABLE Studente RENAME COLUMN cf TO codice_fiscale;
>```


#### 2. `DROP`

==`DROP` è il comando DDL usato per eliminare definitivamente oggetti dal database — che siano tabelle, schemi o interi database.== 
A differenza di `TRUNCATE`, ==che svuota una tabella mantenendone la struttura==, **`DROP` elimina tutto:** 
- ==struttura, dati, vincoli e indici associati.==

Sintassi generale:
```sql
DROP TABLE    nome_tabella;
DROP SCHEMA   nome_schema;
DROP DATABASE nome_database;
```


> [!danger] **`DROP` è irreversibile A differenza di `ALTER TABLE`, un `DROP` elimina definitivamente la struttura e tutti i dati contenuti.** 
> Non esiste un "cestino" — una volta eseguito, non si torna indietro. 
>>[!caution] Usarlo con cautela, specialmente in produzione.


> [!example] **Esempio - `Drop Table` semplice**
> Supponiamo di voler eliminare la tabella `RicambioRip`, che non è referenziata da nessun'altra tabella:
>```sql
> DROP TABLE RicambioRip;
>```
>Nessun problema — ==la tabella non ha dipendenti, PostgreSQL la elimina senza obiezioni.==

##### `DROP` e l'integrità referenziale

Come abbiamo visto nella sezione sui [[#Vincoli di integrità referenziale|vincoli di integrità referenziale]], ==se si tenta di eliminare una tabella che è referenziata da una foreign key in un'altra tabella, PostgreSQL rifiuta l'operazione per preservare la consistenza del database.== 
Ad esempio, tentare di eliminare `Officina` mentre `Riparazione` ha una foreign key che la referenzia produrrebbe un errore.

Per gestire questa situazione SQL mette a disposizione due opzioni:
```sql
-- Elimina la tabella solo se non esistono dipendenze
DROP TABLE nome_tabella RESTRICT; -- comportamento di default

-- Elimina la tabella e tutte le dipendenze in cascata
DROP TABLE nome_tabella CASCADE;
```

>[!caution] **`CASCADE` — usare con cautela** 
>`DROP TABLE nome_tabella CASCADE`: 
>- ==elimina automaticamente anche tutti i vincoli e gli oggetti che dipendono da quella tabella.== 
>È comodo, ma può avere effetti a catena inaspettati su tutto il database.


> [!example] **Esempio — `DROP TABLE` bloccato dall'integrità referenziale**
> Proviamo invece a eliminare `Officina`, che è referenziata da `Riparazione`:
>```
>DROP TABLE Officina;
>```
>
>PostgreSQL risponde con un errore:
>```
>ERROR: cannot drop table Officina because other objects depend on it
DETAIL: constraint riparazione_officina_fkey on table Riparazione depends on table Officina
>```
>Per procedere abbiamo due strade:
>```sql
>-- Strada 1: eliminare prima la tabella dipendente, poi quella referenziata
DROP TABLE Riparazione;
DROP TABLE Officina;
>
-- Strada 2: lasciare che PostgreSQL gestisca la cascata automaticamente
DROP TABLE Officina CASCADE;
>```
>>[!warning] **Con `CASCADE` PostgreSQL elimina anche il vincolo di foreign key in `Riparazione` — la tabella rimane ma perde il vincolo.** 
>>==Controlla sempre cosa viene eliminato in cascata prima di procedere.==

##### `DROP` condizionale

Spesso nei file SQL ==si usa una variante che evita errori se l'oggetto non esiste==:
```sql
DROP TABLE IF EXISTS nome_tabella;
```
>[!example] **Caso d'uso pratico** 
>==Nei file di setup o migrazione del database è buona pratica scrivere `DROP TABLE IF EXISTS` prima di ogni `CREATE TABLE`.== 
>In questo modo lo script può essere eseguito più volte senza errori, ricreando ogni volta la struttura da zero.


> [!example] **Esempio — `DROP TABLE IF EXISTS` in uno script di setup**
>
>Questo è il caso d'uso più comune nella pratica. Immagina di avere un file `setup.sql` che ricrea il database da zero ogni volta che lo esegui:
>```sql
> -- Pulizia delle tabelle esistenti nell'ordine corretto
>-- (prima le dipendenti, poi le referenziate)
>DROP TABLE IF EXISTS RicambioRip;
>DROP TABLE IF EXISTS Riparazione;
>DROP TABLE IF EXISTS Veicolo;
>DROP TABLE IF EXISTS Officina;
>
>-- Ricreazione da zero
>CREATE TABLE Officina ( ... );
>CREATE TABLE Veicolo ( ... );
>CREATE TABLE Riparazione ( ... );
>CREATE TABLE RicambioRip ( ... );
>```
>>[!remember] **L'ordine conta** 
>>==Le tabelle vanno eliminate nell'ordine inverso rispetto alla loro creazione — prima le tabelle che contengono foreign key, poi quelle referenziate==. 
>>**È lo stesso motivo per cui quando si costruisce un palazzo si parte dalle fondamenta, ma quando lo si demolisce si parte dall'ultimo piano.**

####  `TRUNCATE TABLE`

`TRUNCATE` è il comando DDL ==usato per svuotare completamente una tabella mantenendone intatta la struttura — attributi, vincoli e indici rimangono al loro posto==. 
**È l'equivalente di cancellare tutto il contenuto di un foglio senza strapparlo dal raccoglitore.**

Sintassi generale:
```sql
TRUNCATE TABLE nome_tabella;
```

######  Esempio base

Supponiamo di voler svuotare la tabella `RicambioRip` mantenendone la struttura:
```sql
TRUNCATE TABLE RicambioRip;
```

Per verificare che la tabella sia effettivamente vuota si usa `SELECT` — concetto che approfondiremo nel DML:
```sql
SELECT * FROM RicambioRip;
-- risultato: Empty set
```

La tabella esiste ancora con tutti i suoi attributi(colonne) e vincoli, ma non contiene più nessuna riga.

##### `TRUNCATE` e le sequenze

Quando si dichiara una colonna come `SERIAL`, PostgreSQL crea automaticamente due cose dietro le quinte:

1. ==una **sequenza** separata (es. `utente_id_seq`)==
2. ==un **default** sulla colonna impostato a `nextval('utente_id_seq')`==

==La sequenza è un oggetto indipendente che vive per conto proprio nel database== — **esattamente come un [[#Domini personalizzati ed ENUM|dominio personalizzato]].** 
==Non sa e non le importa se la tabella è piena, vuota o non esiste più.== 
Questo spiega perché chiamare `nextval()` incrementa il contatore indipendentemente dallo stato della tabella.

Un `TRUNCATE` semplice svuota la tabella ma non resetta la sequenza. 
Per resettarla si usa:
```sql
TRUNCATE TABLE utente RESTART IDENTITY;
```
Per verificare il valore reale della sequenza dopo il reset si hanno due opzioni:
```sql
-- Valore ricordato dall'ultima chiamata a nextval() nella sessione corrente
SELECT currval('utente_id_seq');

-- Valore reale attuale della sequenza nel database
SELECT last_value FROM utente_id_seq;
```

> [!warning] **`currval()` può ingannare** 
> `currval()` non interroga lo stato attuale della sequenza — ==restituisce l'ultimo valore prodotto da `nextval()` nella sessione corrente.== 
> Dopo un `TRUNCATE RESTART IDENTITY`, `currval()` mostrerà ancora il vecchio valore finché non viene chiamato un nuovo `nextval()`. 
> Per leggere il valore reale della sequenza usare sempre `last_value`.

> [!remeber] **`SERIAL` è una scorciatoia** 
> **`SERIAL` non è un vero tipo di dato SQL standard** — ==è una convenzione di PostgreSQL che automatizza la creazione della sequenza e il collegamento alla colonna.== 
> Nelle versioni più recenti di PostgreSQL è preferibile usare `GENERATED ALWAYS AS IDENTITY`, che è lo standard SQL:2003.

> [!example] Creare una sequenza personalizzata Esattamente come per i domini, è possibile definire sequenze custom:
>```sql
> CREATE SEQUENCE mia_sequenza
  >  START WITH 100
 >   INCREMENT BY 5
  >  MINVALUE 100
  >  MAXVALUE 10000;
>
>SELECT nextval('mia_sequenza'); -- 100
>SELECT nextval('mia_sequenza'); -- 105
>SELECT currval('mia_sequenza'); -- 105
>```

##### `TRUNCATE` e l'integrità referenziale

Esattamente come `DROP`, se la tabella è referenziata da una foreign key PostgreSQL rifiuta il `TRUNCATE` per proteggere l'integrità dei dati. Anche qui si può usare `CASCADE`:
```sql
-- Svuota Riparazione e a cascata anche RicambioRip
TRUNCATE TABLE Riparazione CASCADE;
```

`TRUNCATE` vs `DELETE` vs `DROP`

|                                          | `DELETE`                 | `TRUNCATE`          | `DROP` |
| ---------------------------------------- | ------------------------ | ------------------- | ------ |
| Elimina i dati                           | ✅ filtrabile con `WHERE` | ✅ tutte le righe    | ✅      |
| Mantiene la struttura                    | ✅                        | ✅                   | ❌      |
| Mantiene i vincoli e gli indici          | ✅                        | ✅                   | ❌      |
| Resetta i valori `SERIAL`/auto-increment | ❌                        | ✅                   | —      |
| Supporta `WHERE`                         | ✅                        | ❌                   | ❌      |
| Tipo di comando                          | DML                      | DDL                 | DDL    |
| Velocità su tabelle grandi               | lenta                    | molto veloce        | veloce |
| Reversibile con transazione              | ✅                        | ⚠️ dipende dal DBMS | ❌      |
> [!faq] **Perché `TRUNCATE` è più veloce di `DELETE`?** 
>`DELETE`: 
>- ==registra ogni singola cancellazione nel log delle transazioni riga per riga e applica un lock su ciascuna riga.== 
>`TRUNCATE`: 
>- ==invece opera sull'intera tabella in un colpo solo con logging minimo e un lock a livello di tabella — su milioni di righe la differenza di prestazioni è enorme.==

> [!note] `TRUNCATE` resetta i valori `SERIAL` 
> **Un dettaglio importante:** 
> ==se una colonna usa `SERIAL` (il tipo auto-incrementale di PostgreSQL), dopo un `TRUNCATE` il contatore riparte da capo.== 
> Con `DELETE` ==invece il contatore continua da dove era arrivato==. 
>>[!remember] **Tienilo a mente quando l'ordine degli ID ha importanza.**

> [!example] Caso d'uso pratico `TRUNCATE` è particolarmente utile con le tabelle di **staging** — tabelle usate come appoggio temporaneo per caricare dati grezzi prima di processarli. Alla fine di ogni ciclo si svuotano con `TRUNCATE` e si ricaricano con dati freschi, senza doverle ricreare da zero ogni volta.


### Generazione di valori progressivi

Abbiamo già visto nella sezione sul `TRUNCATE` come funzionano le sequenze e `SERIAL`. 
**Vale però la pena inquadrare il problema da un punto di vista più generale, perché è un concetto che ritorna spesso nella progettazione di database reali.**

==Quando si modella un'entità che non ha un identificatore naturale — o quando, come abbiamo discusso parlando di [[#^838a2d|chiavi surrogate]], si preferisce non usarne uno — è necessario lasciare al DBMS il compito di generare automaticamente valori univoci per la chiave primaria.== 
**Il caso più comune è un campo `id` intero progressivo.**

Il problema è che **non esiste uno standard SQL** per questo — ogni DBMS lo risolve a modo suo.
#### PostgreSQL — sequenze e `SERIAL`

PostgreSQL risolve il problema tramite le **sequenze:**
- ==oggetti indipendenti che vivono nel database e generano valori progressivi.== 
Come abbiamo già visto, `SERIAL` ==è una scorciatoia che automatizza la creazione della sequenza e il collegamento alla colonna==:
```sql
-- Versione esplicita con sequenza
CREATE SEQUENCE Prenotazione_id_seq;

CREATE TABLE Prenotazione (
    id      INTEGER   DEFAULT nextval('Prenotazione_id_seq') NOT NULL,
    istante TIMESTAMP NOT NULL,
    PRIMARY KEY (id)
);

-- Versione abbreviata con SERIAL — equivalente alla precedente
CREATE TABLE Prenotazione (
    id      SERIAL    NOT NULL,
    istante TIMESTAMP NOT NULL,
    PRIMARY KEY (id)
);
```

Durante l'inserimento, poiché `id` ==ha un valore di default, non è necessario specificarlo esplicitamente==:
```sql
INSERT INTO Prenotazione (istante)
VALUES ('2011-08-24 13:15:05')
RETURNING id;
```

> [!info] **`RETURNING id`** 
> ==`RETURNING` è un costrutto non standard di PostgreSQL che permette all'`INSERT` di restituire immediatamente il valore generato dal DBMS per la colonna specificata.== 
> È particolarmente utile quando si inserisce una riga e si ha subito bisogno del suo `id` — ad esempio per inserire righe correlate in una tabella figlia.

> [!note] `SERIAL` vs `GENERATED ALWAYS AS IDENTITY` 
> `SERIAL` è una convenzione storica di PostgreSQL — comoda ma non standard. 
> ==Nelle versioni più recenti è preferibile usare `GENERATED ALWAYS AS IDENTITY`,== introdotto con SQL:2003:
>```sql
> CREATE TABLE Prenotazione (
  >  id   INTEGER  GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
>    istante TIMESTAMP NOT NULL
>);
>```
>>[!ticket] **Il risultato è lo stesso, ma con una sintassi aderente allo standard SQL.**

Inseriemto di ennuple:
Come inserire i valori:
l’istruzione per inserire M ≥ 1 ennuple in una tabella è insert
```postgresql
insert  into  tabella( attributo1 , . . . , attributo N )
values
( valore 1_1 , . . . , valore1_N ) ,
. . .
( valoreM_1 , . . . , valoreM_N )
```

Se abbiamo la tabella veicolo:
```

```

possiamo avere la tabella riparazione:
```
create table riparazione
```

QUesto è legale 


Per modificare una tabella: 
Prendiamo la tabella corso: ha gli attributi nomi e crediti, se se si volessi cancellare la colonna credti:
```sql
esami_fs=# alter table corso drop column crediti
ALTER TABLE
```

Notiamo che se canclelliamo la colonna nome che però è una foreign key della tabella esame, non me lo fa fare:
```
esami=# alter table corso drop column nome;
ERROR: cannot drop column nome of table corso because other objects depend on it
Detail: constraint esame_corso_key on table esame depends on column nome of table corso
HINT: use DROP ... CASCADE to drop the dependet objects too,
```

Per modificare la tabella corso:
```
esami=# alter table corso add constraint crediti_not_null check (crediti is not null)
ALTER TABLE
```


Per creare i tipi di dato:
```
esami_fs=#create domain stringa as varchar;
CREATE DOMAIN
esami_fs=# create domain intges as integer
esami_fs -# check (value>=0);
CREATE DOMAIN

esami_fs=# \dT
Schema   | 
---------|
```


Il vincolo corso chechk lo posso buttare perché abbiamo modificato il tipo della colonna crediti:
```
esami =# alter table corso alter column crediti type intgz
```

Quindi `corso_crediti_check` lo buttiamo:

Ad esempio se si sbalgia una foreign key: 
```
alter type
Display all (numero di tipi) tipies?(y or n)
alter type (nome tipo di dato)
```


### Definizione di domini SQL di tipo enum
```
create type nome_domino
```

Per i tipi record:
Ad esempio indirizzo:
```
create type nome_dominio as (campo1 dominio1, ...,campo N dominioN)
```

QUi c'è la prima differenza tra SQL e postgres: 
```sql
create domain varchar_not_null as varchar check (value is not null);
CREATE DOMAIN
```
Un volta creato il tipo stringa not null:
```
esami_fs=#create type indirizzo as(
esami_fs(#via varchar_not_null,
civico varchar_not_null
cap char (5))
CREATE TYPE

esami=# \dT -- mostra la tabella con tutte le ennuple e le colonne

```

Come possiamo fare l'export e l'imoprt del database su un file: 
per fare il dumping del database:
```
esami_fs=#quit
```

Dopodiche tramite terminale spostarci tra le cartelle con il comando `cd` finché non arriviamo nella working directory dove vogliamo scrivere il nostro file. Per esportare il database
```
pg_dump -U postgres esami_fs >dump_esami_fs.sql
```

Mi crea un file con commandi sql per ricostruire il nostro database, quindi esporta il nostro databse esattamente come l'avevamo configurato anche se alcune cose cambiano della sisntassi, in realta la completa inserendo la sintassi completa.
Esempio prima crea le tabella ma le chiavi le aggiunge dopo.

Per importare il dub possiamo fare due cose:
copiare e incollare oppure usare il comando, nel file:
```
psql -U postgres -X esami_fs_da_dump < esami_fs
```

Da notare questo comando ma prima lo dibbiamo creare, in relata possiamo sovrascrivere anche il nostro database:
```
psql -U postgres esami_fs < dump_esami_fs.sql
```

Da un po errori di alcune cose che già esistono.
```
psql -U postgres
```


Ora serve una altra cosa ovvero inserire i dati: questa è la prima cosa del data manipulation language serve per inserire i dati e per fare le quesry.
Per inserire un numero di ennuple in una tabella:
```
insert into nome_tabella(colonna1, colonna2)
values(valore1, valore2)
```
QUesti vlaori vanno dati in ordine, esempio
```
insert into Officina(nome,indirizzo)
values("Motor Go", "Via Garibaldi")
```

Adesso per riconneterci alla tabella:
```
postgres=#\c esami_fs
You are now connected to database "esami_fs" as user "postgres"
```

Quindi:
```

esami_fs=# insert into corso (nome, crediti)
esami_fs-# values
esami_fs-# ('progettazione',20)
esami_fs-# ('python',30)
esami_fs-# ('web',15)
esami_fs-# ('bd.1-2',35)
INSERT 0 4   -- indica che abbiamo inserito con successo 4 valori
```

Adesso inseriamo qualche persona:
```
esami_fs=#insert into studente(matricola, nome) values
esami_fs-# (1, 'Alice')
esami_fs-# (2, 'Mario')
esami_fs-# (3, 'Andrea')
esami_fs-# (4, 'Isabella')
esami_fs-# (5, 'Toni')
INSERT 0 5
esami_fs=# \d esame
```

Ora inseriamo gli esami
```
insert into esame (studente, corso, data, voto,lode)
esami_fs-#values
esami_fs-# (1, 'progettazione', '09-08-2024', 30, true)
esami_fs-# (1, 'python', '10-10-2024, 28,false)
```

Se mettisimo il true dopo il 28 si accorgerebbe prima di questo errore, perché ci vuole meno calcolo computazionale per rilevare gli errori di vincoli di ennupla, dopodichè si passa ei vincoli di chiave e per ultimo si controlla i vincoli di foreign key.
Se si mettesse:
```
esami_fs=# insert esame (studente, corso, data, voto, lode) values
esami_fs-# (3, 'bd.1-2', '19-03-2023', 28, false)
```

BIsogna ricordare che per inserire le date vanno prima i mesi e poi i giorni perchè l'annotazione è americana, quindi darrebbe un errore di sintassi.
Per modificare questa cosa:
```
esami_fs=# insert esame (studente, corso, data, voto, lode) values
(5,'web', today(), 25, false);
-- today non esiste da errore
esami_fs=# insert esame (studente, corso, data, voto, lode) values
(5,'web', CURRENT_DATE, 25, false);
-- oppure
(4,'web', CURRENT_DATETIMESTAMP, 25, false);
```

Per cancellarli:
```
delete from tabella
-- scelgie una tabella
where condizione
-- sarebbe come dire cancella tutte le ennuple che soddisfano la condizione
```

Se si dimentica di definire la condizione, di defualt viene cancellato tutto il contnetuto della tabella.
```
esami_fs=# delete from esame where studente =4 and corso='web';
DELETE 1
```

Se facciamo:
```
insert into esame (studente, corso, data, voto, lode) values
(53, 'web', CURRENT_DATE, 25, false)
-- da errore perchè viola il voncolo di fk "esame_corso_fkey" e inoltre non esiste lo studente 53
```

Per fare le query:
```
select tabella 1
```

Prima viene eseguita la clausola from, poi viene eseguita la clasuola where e infine viene eseguita la clausola select
QUando non c'è ambiguita delgi attributi posso

Se voglio selezionare tutte le tuple metto select *
```
select * from esame
-- mi mostra tutte le ennuple della tabella esame
```

```
select studente
from esame
where lode = true;
```

Quindi il flusso è: from, where, select


mettiamo caso che lo studente 1 abbia preso due lodi 
```
select studente as studente_bravo
```

Distinct vuol dire dammi tutte le ennuple diverse:
in questo caso sta per dire dammi tutte le ennuple di tutti gli esami che hanno preso le lodi.

