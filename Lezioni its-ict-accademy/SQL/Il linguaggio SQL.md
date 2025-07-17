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
UN DBMS si strutturano in 3 livelli:
1. Livello interno: implementa strutture fisiche di memorizzazione (file sequenziali, file hash, indici, etc.). 
   Questa parte non viene visualizzata dagli sviluppatori.
2. Livello logico: è quello del modello relazionale, usato per ragionare; 
   fornisce un modello logico dei dati, indipendente da come sono memorizzati fisicamente.
   In altre parole i file sono organizzati in modo sconosciuto per gli sviluppatori che li visualizzano come tabelle.

> [!example] **Analogia con Linux**
>    Su Linux è la stessa cosa le cartelle su Linux sono file che quando c'è uno slash finisce il file e noi vediamo le cartelle su interfaccia grafica

3. Livello esterno: 
   per comodità si possono definire le liste; 
   visualizzazioni particolare dei dati che hanno la forma di tabelle, non sono tabelle non si puo inserire dati ma è utile per visualizzarli. Inoltre utenti diversi con privilegi diversi possono visualizzare due liste diverse, esempio utenti con privilegi più alti mostro le email a utenti con privilegi più bassi le nascondo.


### SQL e livelli 
Innanzitutto bisogna lanciare il Docker dove si trova il database tramite il comando:
```docker
docker exec -it its_postgresql bash
```

Dopodiché bisogna spostarsi nella cartella `home` dell'ambiente virtualizzato di Linux:
```shell
601b8410aa93:/# cd /home
```

In seguito digitare questo commando:
```shell
601b8410aa93:/home# psql -U postgres
```

Ora siamo dentro postgreSQL.
Data definition language:

un database è in insieme di tabelle popolate di dati.
Il comando per creare il DB è:
```sql
create database nome_database[opzioni];
```

SQL è case insenstive: si può scrivere maisucoli e minuscoli come mi pare, una volta non si poteva perché non eistivenao i colori sullo schemro.
QUindi se creo una tabella Studente maisucolo o minuscolo non cambia, l'unica cosa che veramente conta è il punto e virgola come JS.
In un database si possono definire schemi: una schema è un sottoinseme delle tabelle. In Ebuy ad esempio può avere uno schema Utenti e Oggetti, servono a definire quando si hanno tante tabelle quindi per gestirle.

Creiamo in una cartella `bd` al cui interno creiamo altre cartelle
```shell
mkdir esempi
cd esempi/
touch esami.sql
```

Dopodichè settiamo subito con che editor aprirlo e apro un altro terminale con cui entro nel container:
```docker
docker ps 
```
mostra gli altri container attivi
Per vedere tutti i container anche quelli chiusi è 
```docker
docker ps -a
```

Per aprire una bash in un contaier già in esecuzione:
```docker
docker exec -it [nome_container] bash
```
Stiamo dicendo di aprire in modo interrativo il temrinale dentro la container

```shell
whoami
```

Ora entriamo in postgres:
```postgresql
psql -U postgres
psql (versione)
type "help" for help.
postgres=#
```
Ora siamo entrati nella riga di comando dentro il DBMS, quindi adesso vediamo solo comandi di `postgres`. 
`postgres=#`: si cihma postgres sia l'utente che è entrato nel postgres e dentro il DBMS di default ha un DB postgres, l'uguale significa che sta spettando il comando.
Per vedere quali database sono disponibili:
```
postgres=# \l
```

per creare un database:
```
postgres=# create database esami;
CREATE DATABSE
postgres=#
```

Da notare no siamo ancora entrati nel database creato, per accedrvi:
```
postgres=# \c esami;
You are now connected to database "esami" as user "postgres"
```

Ora se scrivo qualcosa:
```postgresql
postgres=# perpeorpero
postgres-#
postgres=#(
postgres(#
```

Ti dice cosa manca, finchè c'è l'uguale dopo postgres vuol dire il comando è stato eseguito con successo.

Come si fa a definire una tabella?
```postgresql
create table [nome_schema] nome_tabella(
nome_attributo dominio [vincolo di dominio] //se ce ne sono
nome_attributo dominio [vincoli di dominio]
);
```

Esempio
```postgresql
create table Corso(
	codice integer not null,
	nome character varying (100) not null, //dice che questa è una sequenza di 100 caratteri, standrd sql
	aula character varying (10) not null,
	primary key (codice)
);
create table Incarico(

);
```

I tipi che abbiamo sono:
BLOB: binary large object 


### Creazione di tabelle valori di defualt
quando creo una tabella se inserisco una ennupla e non inserisco il valore allora postgres imposta un valore di defualt

Vincoli di dominio:
ad esempio stipendio e un integer maggiore di zero e per controllare cio scrivo check(stipendio>=0), quindi ogni ennupla deve anche rispettare questo vincolo.

Vincoli di chiave:
Se devo definire un unica primary key su un solo attributo anziche scrivere:
```
primary key (matricola)
```

Scrivo:
```
matricola integer primary key
```

mentre per scrivee tutte le altre chiavi non primaria:
```
unique(cf)
unique(cognome, nome, nascita)
```
Ciò significa che non possono essereci due studenti con lo stesso codice fiscale, nome, cognome e data di nascita.


Proviamo ad implementare delle tabelle
```postgresql
create table studente(
	matricola integer not null,
	 
	nome varchar not null,
	
	primary key(matricola)
);
```


Se prendiamo questo codice e lo copiamo e incolliamo sul temrinale (sempre se ci troviamo dentro il DBSM):
```
esami=#create table(
esami(# matricola integer not null,
esami(# nome varchar not null,
esami(#primary key (matricola)
esami(#);
CREATE TABLE
```

```
create table corso (
	nome varchar primary key,
	crediti integer not null
		check(crediti>0)
);
```

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

