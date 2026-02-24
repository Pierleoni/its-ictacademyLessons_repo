
è un api che funziona allo stesso modo dei connettori; sono vincoli entro in cui i connettori JDBC deono mouversi.
Se ci si deve conntee con PostGesql, MariaDB, etc. la connessione deve avvenire allo stesso modo. 
La comunicazione è parzale: non tutti i db sql sono identici, è una stringa di comunicazione sempre uguale. 
Tuttavia c'è il problema del linguaggio sql: Oracle ha un sistema che è diverso da quello che si fa nei diversi DB. 
In questo modo si fanno semi-query sugli oggetti JAVA. 
Il driverManager 

## Obiettivo 
Sviluppare applicazioni java che si interfaccino con un DBMS, senza avere dipendenze dal particola tipo di scelta 
Il risultato: migrare i dati da un DBMS ad un altro, avrà impatto zero sul codice. 

### JBC Drivers 
Sono classi per lavorare con i DB 
- JDBC definisce l'interfaccia verso il driver
- I fornitori di DB implementano l'interfaccia 

Esistono 4 tipi di driver: 
- Tipo 1: il JDBC-ODBC bridge
- Tipo 2: API nativa 
- Tipo 3: Protocollo di rete 
- Tipo 4 : protocollo nativo (useremo questo!).
#### Driver di tipo 1 
È il driver JDBC-ODBC bridge.
Si usa per dialogare con ODBC
ODBC è una componente di windows costtuita da una famiglia di driver 
- con oBDC ci sipuo connettere ad Access 
Questi driver è implementato dalla classe `sun.jdbc.odbc.JdbcOdbcDriver`
ed è fornito con Java 2 SDK, standard edition 
È dipendente dalla piattaforma, si scelgie quando non è disponibile un driver in java per un certo database. 
Ad oggi obsoleto

#### Driver di tipo 2
Anche detto API nativa 
È il driver che utilizza le API disponibili sul client(ciè sulla macchian dove risiede il database)

Non è scritto interamente in java e dipende dal sistema operativo 
- per maggiore interoperabilità sono da prefire i driver di tipo 4 
- per oravle esistono dirver nativi 
Fornisce più funzionalità e migliori performance perché sfrutta le API native 
Rispetto al driver di tipo 1 


#### Driver di tipo 4 
Anche detto protocollo nativo 
 È il driver che comunica direttamente con il database usando le API di java networking 
 È scritto intermamente in java → interoperabile 
 È deciato ad iuno specifico db
 È più legrro fra tutti i driver 
 - non si necessita di driver intermedi 
 Non sono necessari software aggiuntivi 
 - Nè lato client, cioè sulla macchina dove c'è il DB
### I tipi di chiave 
DirverManager class
- Gestore 


### DriverManager class
Gestisce i driver 
Crea le connessioni ai db 

```
Conncection connection = DriverManager.getConnection(url, username, password); 
```

ulr: anche detta connection string è composta da `jdc:nomeDriver:location` 

### Interfaccia Connection 
Una connessione 




