# Introduzione
Abbiamo visto nella scorsa [[Lezione 1; Introduzione e modello relazionale|lezione]] una introduzione al modello relazionale.
Per creare e manipolare tabelle, chiavi e definire le [[Lezione 1; Introduzione e modello relazionale#I vincoli foreign key (integrità referenziale)|foreign key]], più in generale per manipolare i dati in un database, si usano diversi linguaggi, uno dei tanti è SQL.

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
### Struttura di un DBMS 
UN DBMS si strutturano in 3 livelli:
1. **Livello interno (fisico):** 
	- Si occupa di **come i dati sono memorizzati fisicamente**: file sequenziali, file hash, indici, pagine su disco.
	- È completamente **nascosto agli sviluppatori** e agli utenti: né le [[Query|query]] né i modelli logici si preoccupano di come i dati siano effettivamente salvati.
	  ^livelloInterno
	  
2. **Livello logico (concettuale):**  ^livelloLogico
	- È il livello del **[[Lezione 1; Introduzione e modello relazionale|modello relazionale]]**: 
		- ==qui i dati vengono descritti come **tabelle con attributi e vincoli**.==
    
	- Fornisce una visione **astratta e indipendente** dalla memorizzazione fisica.
    
	- È il livello su cui lavorano principalmente i **DDL (CREATE TABLE, CREATE DOMAIN, ALTER TABLE, …)** e i **vincoli**.
  
	   
   In altre parole i file sono organizzati in modo sconosciuto per gli sviluppatori che li visualizzano come tabelle.
	
> [!info] Title
> È qui che agiscono i **DDL per CREATE VIEW** e le **query DML per interrogare le viste**.


> [!example] **Analogia con Linux**
>    Su Linux è la stessa cosa le cartelle su Linux sono file che quando c'è uno slash finisce il file e noi vediamo le cartelle su interfaccia grafica

3. **Livello esterno (viste):**  ^livelloEsterno
	- Consente di definire **viste personalizzate** dei dati.
    
	- Le viste non sono tabelle reali, ma **proiezioni e trasformazioni** delle tabelle logiche (query salvate).
    
	- Servono per:
    
	    - **semplificazione** (es. un utente vede solo i campi che gli interessano);
        
	    - **sicurezza** (es. un utente con meno privilegi non vede i dati sensibili come l’email).
        
	- È qui che agiscono i **DDL per CREATE VIEW** e le **query DML per interrogare le viste**.
	  

### SQL e livelli 
Innanzitutto bisogna lanciare il Docker dove si trova il database tramite il comando:
```docker
docker exec -it its_postgresql bash
```


> [!NOTE] Nota:
> Se si effettua il **log-out da Docker Desktop** (tramite l’icona nella system tray di Windows) dopo aver chiuso l’interfaccia utente, un eventuale tentativo successivo di eseguire il comando:
>```docker
> docker exec -it its_postgresql bash
>```
>Restituirà l'errore
>```docker
>Error response from daemon: container 601b8410aa933bad27fdb59c55871ee725cb540dd8e520e260d54910cb0b37a0 is not running
>```
>Questo messaggio indica che il container specificato **esiste**, ma **non è attualmente in esecuzione**, anche se Docker Desktop risulta visivamente "aperto"
>Per risolvere questo problema bisogna seguire una serie di passaggi:
>> [!hint]- **Consiglio**
>> Prima di tutto, è utile verificare lo stato dei container con il comando:
>>```docker
>> docker ps -a
>>```
>>Questo comando mostra l’elenco completo di tutti i container (inclusi quelli **arrestati**), con lo stato specificato nella colonna `STATUS`. 
>>Cercare il container desiderato (es. `its_postgresql`) per valutare il suo stato attuale.
>
>
>> [!ticket] **Soluzioni:**
>> Se il container è semplicemente **fermo**, senza errori, è sufficiente riavviarlo con:
>>```docker
>> docker start its_postgresql  /\*(o il nome del container che si vuole far partire )\*/
>>```
>> Poi è possibile accedervi con:
>>```docker
>> docker exec -it its_postgresql bash
>>```
>
>
>> [!warning] **Attenzione**
>>Se il container **si arresta immediatamente dopo l'avvio**, è possibile che ci siano problemi di configurazione, come ad esempio:
>>- porta occupata.
>>  
>>- errore nel file `docker-compose.yml`.
 >>   
>>- variabile d’ambiente mancante o errate..
>>  
>>- mancanza del volume o file corrotto.
>>
>>Per identificare l’errore, consultare i log del container:
>>```docker
>>docker logs its_postgresql (o qualsiasi altro nome di qualsiasi altro container)
>>```





Dopodiché bisogna spostarsi nella cartella `home` dell'ambiente virtualizzato di Linux:
```shell
601b8410aa93:/# cd /home
```

In seguito digitare questo commando:
```shell
601b8410aa93:/home# psql -U postgres
```

Da questo momento in poi ci troviamo dentro PostgreSQL.


#### Data Definition Language (DDL)
Detto questo ora entriamo nel dettaglio e vediamo cosa è il DDL.
==Il DDL è la componente del linguaggio SQL che permette di **definire la struttura del database**.==  

Ma cos’è un database?  
- Un database è un insieme di tabelle popolate di dati.

### Accesso a PostgreSQL via Docker
Per accedere a PostgreSQL via Docker ci sono una serie di passaggi da compiere attraverso comandi di riga di comando (CLI). 

1. **Creazione della cartella per gli esercizi:** 
```shell
mkdir "base dati"
cd "base dati"
mkdir esempi
cd esempi/
touch esami.sql
```
- Qui creiamo la struttura per salvare i file SQL.
    
- Apriamo subito il file `esami.sql` con il nostro editor preferito (VS Code, Sublime Text, ecc.).

2. **Controllo dei container Docker:** 
 Prima di  entro nel [[Docker#1. Docker container vs. Docker Images|container docker]] è meglio vedere i [[Docker#^dockerPs|container attivi]] 
```docker
docker ps 
```
- Mostra i container **attivi**.

> [!info]
> 
> ```docker
> docker ps -a
> ```
> - Mostra tutti i container, **anche quelli chiusi**.


3. **Aprire un terminale interattivo dentro un container già in esecuzione:**

```docker
docker exec -it [nome_container] bash
```


- `-it` apre un terminale **interattivo** dentro il container.
    
- Ora possiamo eseguire comandi all’interno del container.

> [!info] Per vedere l’utente con cui siamo loggati all’interno del container.
> 
> ```shell
> whoami
> ```


4. **Entrare in PostgreSQL**

Ora entriamo in postgres:
```postgresql
psql -U postgres
```

- `-U postgres` indica l’utente con cui ci connettiamo (di default `postgres`).
    
- Uscirà qualcosa come:
```sql
psql (versione)
Type "help" for help.
postgres=#
```


`postgres=#` significa:

- sei connesso al **DBMS PostgreSQL**;
    
- l’utente è `postgres`;
    
- il prompt `=#` indica che PostgreSQL sta **aspettando un comando**.


> [!NOTE] **Nota:**
> - Da questo punto in poi, tutti i comandi che digiterai saranno **comandi PostgreSQL**.
 >   
>- Puoi eseguire query, creare tabelle, domini, viste, ecc.


#### CLI per SQL
Vediamo ora i principali comandi da riga di comando (CLI) per creare **database, tabelle, domini e vincoli**.  

1. **Creazione di un database:**
```sql
create database nome_database[opzioni];
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


> [!important] **Schemi in un database**
> Una schema in un database è : 
> un sottoinsieme logico delle tabelle all'interno di un database. 
> Gli schemi sono utili per organizzare meglio i dati quando ci sono molte tabelle in un database. 
>> [!example] **Esempio:**
>> Prendiamo come esempio il diagramma delle classi UML di Ebuy;
>> Abbiamo la classe `Utenti` che contiene le tabelle relative agli utenti
>> E la classe `Oggetti` che contiene le tabelle relative agli oggetti in vendita.
>>
>
>
> Questa approccio permette di separare i contesti e gestire più facilmente autorizzazioni e query complesse. 
 

2. **Per visualizzare i database disponibili:**
```bash
postgres=# \l
```

> [!example] **Esempio della creazione di un database:**
> per creare un database:
> ```
> postgres=# create database esami;
> CREATE DATABSE
> postgres=#
> ```
>> [!note] **Nota:** a questo punto non siamo ancora entrati nel database creato.

4. **Connettersi a un database:**
```shell
postgres=# \c esami; 
```

Output previsto: 
```shell
You are now connected to database "esami" as user "postgres"
```

> [!NOTE] **Nota: esempio di comando non valido**
>
> ```postgresql
> postgres=# perpeorpero
> postgres-#
> postgres=#(
> postgres(#
> ```
> 
> - Se digiti qualcosa di non corretto, il prompt cambia (`postgres-#`, `postgres(#`) per indicare che **PostgreSQL aspetta la fine dell’istruzione**.
 >   
>- Finché compare il prompt `postgres=#`, il comando è stato eseguito correttamente.


5. **Creazione di una tabella:** 

	**Sintassi generale:**

```postgresql
CREATE TABLE [nome_schema.]nome_tabella (
    nome_attributo dominio [vincoli],
    nome_attributo dominio [vincoli],
    ...
    [constraint nome_vincolo vincolo_su_colonne]
);

```

- `[nome_schema.]` → opzionale, serve se vuoi inserire la tabella in uno schema specifico.
    
- `dominio` → tipo di dato (integer, varchar, date, ecc.) o **domain** creato precedentemente.
    
- `[vincoli]` → ad esempio `NOT NULL`, `UNIQUE`, `CHECK`, ecc.
    
- `constraint` → per definire vincoli di chiave primaria, chiave esterna, o altri vincoli su più colonne.

> [!example] **Esempio di tabella**
> 
> ```postgresql
> create table Corso(
> 	codice integer not null,
> 	nome character varying (100) not null, //dice che questa è una sequenza di 100 caratteri, standrd sql
> 	aula character varying (10) not null,
> 	primary key (codice)
> );
> create table Incarico(
> 	id SERIAL PRIMARY KEY,
 >   docente INTEGER NOT NULL REFERENCES Persona(cf),
 >   corso INTEGER NOT NULL REFERENCES Corso(codice),
 >   data_inizio DATE NOT NULL,
 >   data_fine DATE
> );
> ```
> 

> [!remember] **Tipi di dato comuni in PostgreSQL**
>
> 
> 1. **Integer / Numeric / Real** → numeri interi o decimali.
>     
> 2. **Character / Varchar / Text** → stringhe di lunghezza fissa o variabile.
>     
> 3. **Date / Time / Timestamp** → date, ore, o combinazioni di data e ora.
>     
> 4. **Boolean** → vero/falso.
>     
> 5. **BLOB (Binary Large Object)** → oggetti binari di grandi dimensioni, usati per **immagini, file, audio, video**.
>     
>     - PostgreSQL usa il tipo **`BYTEA`** per memorizzare dati binari.
>         
>     - Esempio: immagini caricate in un’applicazione possono essere salvate come `BYTEA`.
>         
>
>Altri tipi specializzati:
>
>- **ENUM** → valori limitati predefiniti (es. `{M, F}`).
 >   
>- **Domain personalizzati** → domini con vincoli aggiuntivi (es. `CREATE DOMAIN CodiceFiscale AS CHAR(16) CHECK (…)`).
>[Per maggiori informazioni: clicca su questo link](https://www.postgresql.org/docs/current/datatype.html)

#### Creazione di tabelle valori di defualt
Quando si crea una tabella, se **non si inserisce un valore in un campo**, PostgreSQL può impostare un **valore di default** se definito.
Sintassi per un default:
```sql
colonna tipo DEFAULT valore
```

Esempio: 
```sql
stipendio INTEGER DEFAULT 1000 CHECK (stipendio >= 0)
```

In questo caso il [[Lezione 1; Introduzione e modello relazionale#^colonna|campo]] `stipendio` è un intero con valore di default inziale a `1000`; quindi significa che il valore di partenza delle [[Lezione 1; Introduzione e modello relazionale#^ennuple|ennuple]] di stipendio sarà di `1000`  


#### [[Lezione 1; Introduzione e modello relazionale#Il linguaggio SQL Vincoli di dominio Vincoli di ennupla|Vincoli di dominio]] 

Permettono di imporre **restrizioni sui valori degli attributi**.
Esempio: `stipendio` deve essere maggiore o uguale a zero:
```postgresql
CHECK (stipendio >= 0)
```
- Questo vincolo viene controllato per **ogni ennupla inserita**.


#### Vincoli di chiave:
Se devo definire un unica primary key su un solo attributo anziché scrivere:
```postgresql
primary key (matricola)
```

posso anche scrivere:
```postgresql
matricola integer primary key
```

- La clausola `primary key` impone unicità e le ennuple di quel campo non possono avere valori `NOT NULL`

Se ho più attributi da far diventare chiavi primarie
```postgresql
PRIMARY KEY (nome, cognome, nascita)
```

3. **Altri vincoli di unicità:**
```postgresql
unique(cf)
unique(cognome, nome, nascita)
```
- Impedisce la duplicazione di righe che coincidono su uno o più attributi.


##### Esempio di tabella `Studente`
```postgresql
CREATE TABLE Studente (
    matricola INTEGER PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    cf CHAR(16) UNIQUE,
    data_nascita DATE,
    stipendio INTEGER DEFAULT 1000 CHECK (stipendio >= 0)
);
```

- `matricola` → chiave primaria.
    
- `nome` e `cognome` → obbligatori (`NOT NULL`).
    
- `cf` → unico (unico codice fiscale per ogni studente).
    
- `stipendio` → default a 1000 e non negativo.



> [!example] **Esempio concreto di copia/ incolla del codice sul terminale dentro il  DBSM:**
> ```postgresql
> esami=#create table(
> esami(# matricola integer not null,
> esami(# nome varchar not null,
> esami(#primary key (matricola)
> esami(#);
> CREATE TABLE
> ```
> 
> ```postgresql
> create table corso (
> 	nome varchar primary key,
> 	crediti integer not null
> 		check(crediti>0)
> );
> ```
> 
> 
> - `matricola` → chiave primaria.
 >   
>- `nome` e `cognome` → obbligatori (`NOT NULL`).
 >   
>- `cf` → unico (unico codice fiscale per ogni studente).
 >   
>- `stipendio` → default a 1000 e non negativo.

Se su temrinale scriviamo:
```
esami=#\d
```

Va visualizzare a schermo tutte le tabelle create 
mentre se voglio solo vedere una tabella specifica:
```
esami=#\d nome_tabella
```

```postgresql
create table esame (
	studente integer not null,
	corso varchar not null,
	data date not null,
	voto integer not null
		check (voto>=18 and voto <=30)
	lode boolean not null,
);
```


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

