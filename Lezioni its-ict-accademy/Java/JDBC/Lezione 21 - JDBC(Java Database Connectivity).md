
# Da Java Base a Java Avanzato

Nei moduli precedenti abbiamo costruito le fondamenta del linguaggio: [[Lezione 2 - Sintassi e costrutti di base|sintassi]], [[Lezione 2 - Sintassi e costrutti di base#Tipi di dato primitivi|tipi]], [[Lezione 2 - Sintassi e costrutti di base#Controllo di flusso|strutture di controllo]], [[Oggetti e Classi#Approccio orientato agli oggetti (OOP)|OOP]] ([[Java/Lezione 5 Le classi/Le classi#Definizione di una classe|classi]], [[Lezione 10 - Classi astratte e interfaccie#Le interfacce|interfacce]], [[Ereditarietà e polimorfismo#Concetto di ereditarietà|ereditarietà]]), e i meccanismi di [[Lezione 18 - MultiThreading#Situazioni critiche nella programmazione concorrente|concorrenza]] con il **[[Lezione 18 - MultiThreading|multithreading]]**. Abbiamo anche incontrato alcuni **[[Lezione 19 - Design Pattern|design pattern]]** fondamentali, tra cui lo **[[Lezione 19 - Design Pattern#Pattern Strategy|Strategy]]** (separare l'algoritmo dal contesto che lo usa) e l'**[[Lezione 19 - Design Pattern#Adapter (Pattern Strutturale)|Adapter]]** (fare da ponte tra interfacce incompatibili).

Con Java Avanzato entriamo nell'ecosistema reale delle applicazioni enterprise: 
- comunicazione con database, 
- gestione delle risorse, integrazione con sistemi esterni. 
Non si tratta di nuovi costrutti sintattici, ma di **[[Lezione 6 - API#API (Application Programming Interface)|API]] e architetture** che poggiano esattamente sui concetti già visti — e JDBC ne è l'esempio perfetto.


## JDBC — Java Database Connectivity
**DBC** è un'[[Lezione 6 - API|API]] standard di Java per la comunicazione con [[Lezione 1; Introduzione e modello relazionale|database relazionali]]. 
Il suo ruolo non è implementare la connessione, ma **definire un contratto**: 
- ==un insieme di [[Lezione 10 - Classi astratte e interfaccie#Le interfacce|interfacce]] e regole che qualsiasi driver per qualsiasi DBMS (PostgreSQL, MariaDB, Oracle, MySQL...) deve rispettare.==
>[!link] È un'applicazione diretta del **[[Lezione 19 - Design Pattern#Adapter (Pattern Strutturale)|pattern Adapter]]**
>==JDBC astrae le differenze tra i vari database esponendo un'unica interfaccia uniforme verso il codice Java, mentre ogni driver si occupa di tradurre quella interfaccia nel protocollo specifico del suo DBMS==.

La comunicazione è però **parzialmente** standardizzata. 
La struttura delle chiamate Java è sempre la stessa, ma il **dialetto SQL** sottostante può variare: 
- Oracle, ad esempio, ha funzioni e sintassi che differiscono dallo standard SQL usato da PostgreSQL o MariaDB. JDBC non risolve questo problema — garantisce uniformità nell'**accesso**, non nella **query**.
Il punto di ingresso è il **`DriverManager`**: 
- ==il componente che, dato un URL di connessione (es. `jdbc:postgresql://localhost:5432/mydb`), individua il driver corretto tra quelli registrati e restituisce una `Connection`.==
### Obiettivo di JDBC

**L'obiettivo principale di JDBC è:** 
- ==permettere di sviluppare applicazioni Java che si interfaccino con qualsiasi DBMS **senza dipendere da una scelta specifica**.== 
Il codice Java che usa JDBC **è scritto una volta sola:** 
- ==se un domani si decide di passare da MySQL a PostgreSQL, l'unica cosa che cambia è il driver (e l'URL di connessione) — il codice applicativo rimane invariato.==

> [!ticket] **In termini pratici:** 
> ==**impatto zero sul codice Java** in caso di migrazione tra DBMS.==

Questo è possibile proprio perché JDBC non è un'implementazione, ma un **contratto**: 
- ==le classi e interfacce del package `java.sql` definiscono _cosa_ si può fare, mentre ogni driver definisce _come_ farlo per il suo specifico database.==
[![Screenshot-2026-03-07-at-10-50-03-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png](https://i.postimg.cc/pTzkYFDk/Screenshot-2026-03-07-at-10-50-03-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/2bj4C39B)

###  Cos'è JDBC — nel dettaglio

JDBC è: 
- ==un'**interfaccia a basso livello** verso il database.== 
- ==Non offre astrazioni di alto livello (quelle arriveranno con ORM come Hibernate), ma accesso diretto ed esplicito tramite SQL.==

Si trova nel package standard `java.sql` e copre quattro funzionalità fondamentali:

1. **Connettersi al database** — ==aprire una connessione verso il DBMS==
2. **Eseguire scritture** — `INSERT`, `UPDATE`, `DELETE`
3. **Eseguire query** — `SELECT`
4. **Recuperare i risultati** — ==leggere i dati restituiti dalla query riga per riga==

>[!note] **Nota:** 
>=="basso livello" qui significa che sei tu a scrivere le query SQL per esteso, a gestire la connessione, a iterare sui risultati. Non c'è magia — ed è esattamente questo che lo rende utile da studiare prima di passare a strumenti più astratti.==


### Architettura JDBC 
Per capire come Java e JDBC lavorino insieme, è utile seguire il flusso di una connessione dall'inizio alla fine.
[![Screenshot-2026-03-07-at-10-56-06-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png](https://i.postimg.cc/wj9v68fs/Screenshot-2026-03-07-at-10-56-06-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/GHSrQN1c)
**Analisi dell'immagine:**
Il codice Java applicativo(il file Java sulla sinistra) non comunica mai direttamente con il database:  
- ==parla esclusivamente con le **interfacce** definite nel package `java.sql` (`Connection`, `Statement`, `ResultSet`, ecc.).== 
- ==Questo è il confine che il  codice applicativo non attraversa mai.==

Mentre all'interno di `java.sql` vive il **`DriverManager`**: 
- ==come abbiamo già anticipato sopra questo è  il componente che fa da punto di ingresso.== 
Quando gli si fornisce un URL di connessione come `jdbc:postgresql://localhost:5432/mydb`, il `DriverManager` ==legge il prefisso del protocollo e individua automaticamente il driver corretto tra quelli disponibili, restituendo una `Connection`.==

I **driver** invece vivono **fuori** da `java.sql`: 
- sono librerie fornite da terze parti (il team di PostgreSQL, Oracle, ecc.) e ognuno di essi è un'**implementazione concreta** delle interfacce di `java.sql`. 
>[!link] È esattamente il **[[Lezione 19 - Design Pattern#Adapter (Pattern Strutturale)|pattern Adapter]]**: 
>i driver adattano il protocollo specifico del loro DBMS al contratto comune definito da JDBC.

Il risultato è che: 
- ==il codice applicativo è **completamente ignaro** di quale DBMS si trovi dall'altra parte.== 
Per migrare da PostgreSQL a MariaDB è sufficiente cambiare il driver e l'URL di connessione — il codice Java rimane invariato.




### I Driver JDBC

I driver: 
- ==sono **classi Java** che permettono di lavorare con un database specifico.== 
Come abbiamo visto nell'architettura, JDBC definisce le interfacce e i fornitori di database (PostgreSQL, Oracle, ecc.) ne forniscono l'implementazione concreta.

Esistono 4 tipi di driver, in ordine crescente di "purezza" Java:
####  Tipo 1 — JDBC-ODBC Bridge
**Il più datato, oggi obsoleto.** 
Fa da ponte verso **ODBC:** 
- ==una famiglia di driver nativa di Windows che permette di connettersi a database come Microsoft Access.== 
È implementato dalla classe `sun.jdbc.odbc.JdbcOdbcDriver`, fornita con il Java 2 SDK. 
Il limite principale è la **dipendenza dalla piattaforma**: 
- ==funziona solo su Windows, e si usava solo quando non era disponibile un driver Java nativo per un certo database.==
[![Screenshot-2026-03-07-at-11-20-13-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png|281x338](https://i.postimg.cc/13Yr6HN7/Screenshot-2026-03-07-at-11-20-13-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/87MvgL4L)


####  Tipo 2 — API Nativa

==Utilizza le **API native** disponibili direttamente sulla macchina client (quella dove risiede il database).== 
==Per questo motivo non è scritto interamente in Java e **dipende dal sistema operativo**== — ad esempio Oracle fornisce driver nativi di questo tipo. 

> [!done] **Vantaggi**
> Il vantaggio rispetto al Tipo 1 è che elimina il sovraccarico delle chiamate ODBC, offrendo **più funzionalità e performance migliori**. 

> [!fail] **Svantaggi**
> Tuttavia, per applicazioni che richiedono interoperabilità tra sistemi diversi, è preferibile il Tipo 4.

[![Screenshot-2026-03-07-at-11-23-43-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png|243x341](https://i.postimg.cc/65P8f1Y6/Screenshot-2026-03-07-at-11-23-43-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/WhMp28Bx)


#### Tipo 3 — Protocollo di Rete

==Introduce uno **strato intermedio** (middle-tier) che si occupa di tradurre le chiamate JDBC verso il database.== 
Il middle-tier può a sua volta usare un driver di Tipo 1, 2 o 4 per comunicare col DBMS effettivo.
È scritto **interamente in Java:**
- ==quindi pienamente interoperabile, e può essere configurato per supportare diversi database.== 

> [!done] **Vantaggi**
> Offre ottime performance, maggiore sicurezza e funzionalità avanzate come caching e load balancing. 

> [!failure] **Svantaggi**
> Il contro è che **richiede un server dedicato** per il middle-tier.

[![Screenshot-2026-03-07-at-11-25-34-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png|303x321](https://i.postimg.cc/ZnGhC3xN/Screenshot-2026-03-07-at-11-25-34-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/ctBzzvj1)



#### Tipo 4 — Protocollo Nativo ✅ _(quello che useremo)_

È il driver più moderno e quello che utilizzeremo. ==Comunica **direttamente** con il database usando le [[Lezione 6 - API|API]] di Java networking, senza alcuno strato intermedio==. 
==È scritto interamente in Java, quindi completamente interoperabile, ed è dedicato a un database specifico (es. il driver JDBC di PostgreSQL funziona solo con PostgreSQL).==

È il più **leggero** tra tutti i driver proprio perché non richiede nulla di aggiuntivo: 
- nessun software lato client, 
- nessun server intermedio come nel Tipo 3, 
- nessun bridge come nel Tipo 1. 
==Basta aggiungere la dipendenza al progetto e il driver è pronto.== 
[![Screenshot-2026-03-07-at-11-35-51-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png|143x150](https://i.postimg.cc/fyfbXDBf/Screenshot-2026-03-07-at-11-35-51-Microsoft-Power-Point-Java-20-JData-Base-Connectivity-Compatibilit.png)](https://postimg.cc/XBX36SMr)
### Caricare i Driver JDBC

I driver JDBC vengono caricati **dinamicamente** dall'applicazione leggendo il classpath. 
È però possibile caricarli esplicitamente con:
```java
Class.forName("com.mysql.cj.jdbc.Driver"); // driver nativo MySQL 8
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver"); // driver bridge (obsoleto)
```

`Class.forName()`: 
- ==carica la classe del driver in memoria, rendendolo disponibile al `DriverManager`.== 
- ==Una volta caricato, la connessione avviene tramite i metodi statici di `DriverManager`.==

>[!note] **Nota:** 
>Da Java 4 in poi, la chiamata a `Class.forName()` è **opzionale** — ==il driver viene rilevato automaticamente dal classpath tramite il meccanismo di _Service Provider Interface (SPI)_.==

## I Tipi Chiave di JDBC

| Tipo                                                           | Natura      | Ruolo                                                    |
| -------------------------------------------------------------- | ----------- | -------------------------------------------------------- |
| [[#`DriverManager` — Dal Concetto al Codice\|`DriverManager`]] | classe      | Gestore dei driver; fornisce la `Connection` dato un URL |
| `Connection`                                                   | interfaccia | Rappresenta la connessione attiva al DB                  |
| `Statement`                                                    | interfaccia | Wrapper per l'esecuzione di statement SQL                |
| `ResultSet`                                                    | interfaccia | Accesso ai risultati di una query                        |



>[!note] **Nota:**
> che `Connection`, `Statement` e `ResultSet` sono tutte **interfacce** — non classi. È il driver (Tipo 4, nel nostro caso) a fornire l'implementazione concreta di ognuna di esse.



### `DriverManager` — Dal Concetto al Codice
Come abbiamo visto, il `DriverManager` gestisce i driver registrati e crea le connessioni ai database. Dal punto di vista applicativo, il metodo principale che useremo è `getConnection()`:

```java
Connection connection = DriverManager.getConnection(url, username, password);
```

oppure, se il database non richiede autenticazione:
```
Connection connection = DriverManager.getConnection(url, "", "");
```

> `getConnection()` è un **[[Costruttori e modificatori#2. Metodi `static`|metodo statico]]** — ==non si istanzia il `DriverManager`, lo si usa direttamente.==

#### La Connection String

L'`url` (detta anche **connection string**) segue sempre questo formato:
```java
jdbc:nomeDriver:location
```

Ad esempio:
```java
jdbc:postgresql://localhost:5432/mydb
jdbc:mysql://localhost:3306/mydb
```

```java
Conncection connection = DriverManager.getConnection(url, username, password); 
```

==È proprio leggendo il prefisso `nomeDriver` che il `DriverManager` sa quale driver utilizzare tra quelli disponibili nel classpath.==

>[!note] **Nota:** 
>**`getConnection()` dichiara `throws SQLException`** — ==tutte le operazioni JDBC possono lanciare eccezioni che **devono essere gestite**, cosa che vedremo nel dettaglio a breve.==


#### Creare le connessioni
La firma completa dei metodi disponibili è:

```java
// senza credenziali
static Connection getConnection(String url) throws SQLException;

// con credenziali
static Connection getConnection(String url, String userId, String password) throws SQLException;
```

**Esempi pratici**
```java
// Tipo 1 — ODBC (obsoleto): non ha location, solo un'etichetta configurata su Windows
Connection conn = DriverManager.getConnection("jdbc:odbc:SAMPLEDBASE");

// Tipo 2/4 — Oracle con credenziali
Connection conn = DriverManager.getConnection("jdbc:oracle:oci7:@sample", "scott", "tiger");

// Tipo 4 — PostgreSQL con credenziali
Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb", "admin", "secret");

// Se non serve autenticarsi, si passano stringhe vuote
Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb", "", "");
```

##### Struttura della Connection String
L'URL di connessione, detta anche **connection string**, segue sempre questo formato:
```
jdbc : nomeDriver : location
```
dove:

- `jdbc` — ==prefisso fisso, identifica il protocollo==
- `nomeDriver` — ==identifica il driver da usare (es. `postgresql`, `mysql`, `odbc`)==
- `location` — ==indica dove si trova il database (host, porta, nome del DB)==

> **Eccezione — ODBC (Tipo 1):** 
> ==non ha una `location` di rete vera e propria, ma una semplice etichetta configurata a livello di sistema operativo durante il setup del driver (es. `SAMPLEDBASE`).==

Se il database non richiede autenticazione, si passano stringhe vuote al posto delle credenziali:
```java
DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb", "", "");
```

>[!note] Nel caso di ODBC (Tipo 1) non esiste una vera `location` di rete — al suo posto si usa una **etichetta** configurata a livello di sistema operativo durante la fase di setup del driver.
### Interfaccia `Connection` 
Una `Connection` rappresenta una **sessione di dialogo attiva** con un database specifico. Non è solo un "canale aperto" — è il **contesto** entro cui avvengono tutte le operazioni SQL.

Le sue responsabilità principali sono due:

**1. Creare gli Statement SQL** 
- È attraverso la `Connection` che si creano gli oggetti per eseguire query e scritture sul DB:
```java
java.sql.Connection interface
void close() throws SQLException; 
Statement createStatement() throws SQLException; 
PreparedStatement prepareStatement(String) throws SQLException;
CallableStatement prepareCall(String) throws SQLException;  
```

**2. Gestire le transazioni:**
-  La `Connection` controlla il ciclo di vita delle transazioni:
```java
boolean getAutoCommit() throws SQLException;

void setAutoCommit(boolean) throws SQLException; // disabilita il commit automatico
void commit() throws SQLException; // conferma la transazione
void rollback() throws SQLException; // annulla la transazione
```



> [!NOTE] **Info:**
> Di default, ogni operazione SQL viene committata automaticamente (`autoCommit = true`). Disabilitarlo permette di raggruppare più operazioni in un'unica transazione atomica — o tutto va a buon fine, o si annulla tutto.

###  Interfaccia `Statement`

Uno `Statement` è: 
- ==il componente che permette di **eseguire istruzioni SQL** sul database.== 
Si ottiene sempre a partire da una `Connection` e può fare due cose: 
- ==modificare i dati== 
- ==o interrogarli.==
```java
java.sql.Statement interface

// Per scritture: INSERT, UPDATE, DELETE — restituisce il numero di righe modificate
int executeUpdate(String sql) throws SQLException;

// Per letture: SELECT — restituisce un ResultSet con i risultati
ResultSet executeQuery(String sql) throws SQLException;

// Generico: utile quando non si sa a priori il tipo di istruzione
boolean execute(String sql) throws SQLException;

// Chiude lo statement e libera le risorse
void close() throws SQLException;
```


> [!deep] **Nota:**
> La distinzione tra `executeUpdate()` e `executeQuery()` riflette una separazione netta tra **scrittura** e **lettura** — non si può usare `executeQuery()` per una `INSERT`, né `executeUpdate()` per una `SELECT`.


####  `executeUpdate()`

Si usa per eseguire istruzioni SQL di **scrittura**:
- `INSERT`, `UPDATE`, `DELETE`. 
- ==Restituisce un `int` che rappresenta il **numero di righe coinvolte** nell'operazione.==
```java
// tramite l'oggetto connecction creo lo Statement e lo refernzio con un oggetto di Statement
Statement st = connection.createStatement();

// INSERT — restituisce 1 se la riga è stata inserita
int res1 = st.executeUpdate("INSERT INTO impiegati VALUES ('francesco', 1000, 'programmer')");

// UPDATE — restituisce il numero di righe modificate
int res2 = st.executeUpdate("UPDATE impiegati SET salario = 1500");
```

Il valore restituito è utile per verificare che l'operazione abbia effettivamente modificato dei dati: 
- ==se ritorna `0`, nessuna riga è stata coinvolta.==


####  `executeQuery()`

Si usa per eseguire istruzioni SQL di **lettura**: `SELECT`. 
- ==Restituisce un oggetto `ResultSet`, ovvero un **cursore** per navigare riga per riga la tabella risultato.==

```java
Statement st = connection.createStatement();
ResultSet res = st.executeQuery("SELECT * FROM impiegati");
```


> [!caution]  **Ordine delle Colonne nel `ResultSet`**
>
>L'ordine delle colonne restituite da una `SELECT *` **non è garantito** — dipende dal DBMS e dalla struttura interna della tabella, e può variare.
>
>Per garantire un ordine preciso, occorre **specificare esplicitamente** le colonne nella query:
>```java
> // ❌ ordine non garantito
ResultSet res = st.executeQuery("SELECT * FROM impiegati");
>
>// ✅ ordine garantito
>ResultSet res = st.executeQuery("SELECT >nome, cognome, salario FROM impiegati");
>```
>
>
>>[!done] **Questo è anche una buona pratica in generale:** 
>>==specificare le colonne rende il codice più leggibile, meno fragile a modifiche future della struttura della tabella, e più efficiente evitando di trasferire dati non necessari.==
>>

###  Interfaccia `ResultSet`

Un `ResultSet` rappresenta: 
- il **risultato tabulare** di una query `SELECT`.
Si comporta come un **[[Lezione 12 - Collection#Iterator|Iterator]]**: 
- ==parte da una posizione iniziale **fuori dalla tabella** (riga 0), e si sposta una riga alla volta tramite `next()`.==
```java
java.sql.ResultSet interface

boolean next() throws SQLException;          // avanza alla riga successiva, false se non ce ne sono
void close() throws SQLException;            // chiude il ResultSet e libera le risorse

// Accesso per indice (più efficiente — usare quando si specificano le colonne nella SELECT)
String getString(int columnIndex) throws SQLException;

int getInt(int columnIndex) throws SQLException;
Date getDate(int columnIndex) throws SQLException;


// Accesso per nome colonna
String getString(String columnName) throws SQLException;
int getInt(String columnName) throws SQLException;
Date getDate(String columnName) throws SQLException;

// Accesso generico — utile quando il tipo della colonna non è noto a compile time
Object getObject(int columnIndex) throws SQLException;
Object getObject(String columnName) throws SQLException;

```

> [!NOTE] **Nota:**
> ==L'indice delle colonne **parte da 1**, non da 0 come gli array Java==


> [!warning] **Perché farsi restituire un oggetto anziche un intero o un numero?**
> Come possiamo vedere esistono due metodi che restituiscono un oggetto anziche una Stringa o un intero. 
> Perché questo e a cosa ci può servire? 
> Immaginiamo di dover farci restituire il valore di una singola colonna ma non sappiamo a compile-time che tipo ha quella colonna, questo perché magari stiamo scrivendo un tool generico che legge qualsiasi tabella. 
> Far eseguire il `getString()` o il `getInt()` senza sapere il tipo di dato incastonato nella riga può essere rischioso perché ci obbliga a fare un cast specifico, che non sempre è il cast corretto, per questo si sceglie il `getObject()` perché ==è più generico e se non si sa che tipo di dato si sta estraendo dalla singola riga è la soluzione migliore.== 
> Un altro motivo é quando si vuol gestire un qualsiasi tipo di colonna con lo stesso codice senza scrivere un `if` per ogni tipo possibile: 
>```java
> // invece di fare:
>if (tipo == "String") res.getString("colonna");
>else if (tipo == "int") res.getInt("colonna");
>
>// puoi fare genericamente:
>Object valore = res.getObject("colonna");
>```



**Esempio Completo:**
```java
Statement st = conn.createStatement();
ResultSet res = st.executeQuery("SELECT nome, cognome, salario FROM impiegati");

while (res.next()) {
    System.out.println("Nome: "    + res.getString("nome"));
    System.out.println("Cognome: " + res.getString("cognome"));
    System.out.println("Salario: " + res.getInt("salario"));
}
```


#### Navigare il `ResultSet`

```java
Statement st = connection.createStatement();
ResultSet res = st.executeQuery("SELECT * FROM impiegati");

while (res.next()) {
    System.out.println("Nome: "    + res.getString("nome"));
    System.out.println("Cognome: " + res.getString("cognome"));
}

st.close();
```

Il `ResultSet` si comporta come un **[[Lezione 12 - Collection#Iterator|Iterator:]]** 
- ==all'inizio il cursore si trova in una posizione **fuori dalla tabella** (riga 0), prima di qualsiasi riga.== 
- ==Ad ogni chiamata di `next()` il cursore avanza di una riga e restituisce `true`; quando le righe sono esaurite restituisce `false` e il ciclo termina.==

- ==Fissata la riga corrente, si accede ai valori delle singole colonne tramite i metodi `getTipo()`, passando il **nome della colonna** o il suo **indice**== (che parte da 1): 
```java
res.getString("nome");  // per nome colonna
res.getString(1);       // per indice — più efficiente
```

#####  Note Importanti sul `ResultSet`

**1. Il `ResultSet` consuma gli elementi:** 
- ==Righe e colonne si possono scorrere **una sola volta** — non è possibile tornare indietro o rileggere una riga già letta (a meno di non usare un `ResultSet` scorrevole, che vedremo dopo).==

**2. Riuso dello `Statement`:**
- ==Se si esegue una nuova query sullo stesso oggetto `Statement`, il `ResultSet` precedente viene **chiuso automaticamente**.== 
- È buona pratica chiudere esplicitamente `ResultSet` e `Statement` quando non servono più.

**3. `ResultSetMetaData`**: 
- Se non si conosce a priori la struttura della tabella (numero di colonne, nomi, tipi), si può recuperare questa informazione tramite `ResultSetMetaData`:
```java
ResultSetMetaData meta = res.getMetaData();
int numColonne = meta.getColumnCount();
String nomeColonna = meta.getColumnName(1);
```


### Interfaccia `PreparedStatement`

`PreparedStatement` estende `Statement` e può essere usato per qualsiasi istruzione SQL. 
Il suo vantaggio principale è: 
- ==evitare le **noiose concatenazioni di stringhe** che si sarebbero necessarie con uno `Statement` normale.==

Immagina di dover inserire un impiegato con dei parametri variabili usando uno `Statement` classico:
```java
// ❌ Con Statement — concatenazione fragile e rischiosa
String sql = "INSERT INTO impiegati VALUES ('" + nome + "', " + salario + ", '" + ruolo + "')";
st.executeUpdate(sql);
```

==Questo approccio è scomodo e pericoloso perché bisogna gestire manualmente i delimitatori per stringhe (`'`) e date, ed è vulnerabile a **SQL Injection**.==

Con `PreparedStatement` si usano dei **segnaposto** `?` al posto dei valori variabili, e per ognuno si invoca il corrispondente metodo `setTipo(index, value)`:
- **`index`** — ==posizione del `?` nell'istruzione, **a partire da 1**==

- **`value`** — ==valore da sostituire al segnaposto==

```java
// ✅ Con PreparedStatement
PreparedStatement ps = connection.prepareStatement(
    "INSERT INTO impiegati VALUES (?, ?, ?)"
);
```

Per ogni `?` ==si invoca il corrispondente metodo **setter**, specificando la posizione (che parte da 1) e il valore==:
```java
ps.setString(1, "Francesco");
ps.setInt(2, 1000);
ps.setString(3, "programmer");
ps.executeUpdate();
```

I setter gestiscono automaticamente i delimitatori per stringhe e date — non serve aggiungerli manualmente.

Al termine si esegue l'istruzione con:

- `executeUpdate()` — per `INSERT`, `UPDATE`, `DELETE`
- `executeQuery()` — per `SELECT`

**Esempio — Ricerca per matricola**
```java
public Impiegato cerca(String matricola) {
    PreparedStatement pst = connection.prepareStatement(
        "SELECT * FROM impiegati WHERE matricola = ?"
    );
    
    pst.setString(1, matricola); // nessun delimitatore necessario!
    
    ResultSet result = pst.executeQuery();
    
    // la matricola è chiave primaria, quindi al massimo una riga
    if (result.next()) {
        // leggo le colonne e creo l'oggetto Impiegato
        return imp;
    } else {
        return null; // oppure sollevo un'eccezione
    }
}
```


#### Settare i parametri 
Per ogni tipo di dato esiste il corrispondente setter:
```java
java.sql.PreparedStatement interface

void setByte(int index, byte value) throws SQLException;
void setInt(int index, int value) throws SQLException;
void setString(int index, String value) throws SQLException;

// Per le date si usa il tipo java.sql.Date, non java.util.Date!
void setDate(int index, Date value) throws SQLException;
```


> [!warning] **Attenzione!**
> Attenzione alla distinzione tra `java.sql.Date` e `java.util.Date` — ==JDBC usa il suo tipo `Date` specifico per interfacciarsi correttamente con le date dei DBMS.==

### Il progetto Maven
Finora abbiamo visto come JDBC funzioni concettualmente, ma per usarlo in un progetto reale serve aggiungere il driver come **dipendenza esterna** — ed è qui che entra in gioco **Maven**.

Maven è uno strumento di **gestione delle dipendenze**: permette di dichiarare le librerie di cui il progetto ha bisogno e si occupa automaticamente di scaricarle dal suo repository centrale, insieme a tutte le loro **sottodipendenze**.

Le dipendenze si dichiarano nel file **`pom.xml`** (Project Object Model), il file di configurazione di ogni progetto Maven:
```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.6.0</version>
</dependency>
```


> [!NOTE] **Nota:**
> Aggiungendo questa dipendenza, Maven scarica automaticamente il driver JDBC di PostgreSQL ([[#Tipo 4 — Protocollo Nativo ✅ _(quello che useremo)_|Tipo 4]]) — non serve cercare e aggiungere manualmente il `.jar`.

In sintesi, il flusso è:

1. ==Dichiari la dipendenza nel `pom.xml`==
2. ==Maven scarica il `.jar` richiesto e tutte le sue sotto-dipendenze==
3. ==Il driver è disponibile nel classpath e il `DriverManager` può trovarlo automaticamente==

###  Creare un Progetto Maven su Eclipse

#### Struttura del Progetto

Una volta creato il progetto Maven (`New Maven Project → Create a simple project`), Eclipse genera automaticamente questa struttura:
```text
myproject/
├── src/
│   ├── main/java/      # sorgenti Java
│   └── test/java/      # classi di test
├── JRE System Library  # libreria standard Java
└── pom.xml             # file di configurazione Maven
```

- **`Group Id`** — ==identifica l'organizzazione o il gruppo di progetti (es. `com.miacompany`)==
- **`Artifact Id`** — ==identifica il singolo progetto (es. `gestione-impiegati`)==

#### Aggiungere il Driver JDBC nel `pom.xml`

Per usare JDBC con MySQL, si aggiunge la dipendenza al connettore nel `pom.xml`:
```xml
<dependencies>
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.4.0</version>
        <scope>compile</scope>
    </dependency>
</dependencies>
```
==Maven scaricherà automaticamente i `.jar` necessari, che compariranno sotto **Maven Dependencies** nel progetto.== 
A quel punto sono disponibili sia `java.sql` che il driver di connessione, e il progetto è pronto per connettersi al database.

### Esempio pratico: Gestione di una libreria

Ora che abbiamo visto la parte teorica del JDBC passiamo alla parte pratica; 
ipotizziamo di dover mettere in piedi un sistema di gestione dei libri di una libreria o biblioteca a partire da un database scritto in PostgreSQL. 
Ora il codice in JDBC viene organizzato in 3 strati con responsabilità separate, seguendo il DAO pattern: 
1. Il componente `Database`: 
	- Centralizza la logica di connessione al database. Tutte le credenziali e l'URL sono in un unico posto — se cambiano, si modifica solo qui.
2. `LibroDTO` — La Copia dell'Entità
	- Il **DTO** (Data Transfer Object) è: 
		- ==la rappresentazione Java dell'entità nel database.== 
		- ==Non contiene logica — solo i campi della tabella con i relativi getter e setter.== 
		- Ha **2** costruttori: 
			- uno completo (con `id`, usato quando si legge dal DB) 
			- e uno senza `id` (usato quando si vuole inserire un nuovo libro, perché l'`id` viene generato dal DB).

3. `LibroDAO` — L'Accesso ai Dati

	- Il **DAO** (Data Access Object) è:
		- ==il componente che mette in comunicazione il database con il resto dell'applicazione.== 
	- ==Contiene tutti i metodi che eseguono query SQL, restituendo o ricevendo oggetti `DTO`.==
#### Perché il DAO pattern?

Prima di guardare il codice, vale la pena capire **perché** questa organizzazione esiste.

Immagina di scrivere tutto il codice SQL direttamente nel `main`: 
- ==funziona, ma ogni volta che la struttura del database cambia devi cercare le query sparse ovunque nel codice.== 
- ==Se domani vuoi passare da PostgreSQL a MySQL, devi toccare tutto. Questo è esattamente il problema che il **DAO pattern** risolve.==

L'idea è semplice: 
- ==**separare la logica di accesso ai dati dal resto dell'applicazione**.== 
Il resto del codice non deve sapere nulla di SQL, di connessioni, di driver — parla solo con oggetti Java. 
È un'applicazione diretta del principio di **Single Responsibility**: 
- ==ogni componente ha una sola ragione per cambiare.==

Questa separazione si realizza attraverso due figure chiave:

1. **Il DTO (Data Transfer Object):**
	- è la rappresentazione Java di un'entità del database — in questo caso un libro. 
	- Non contiene logica, solo i dati: 
		- ==è il "contenitore" che viaggia tra i vari strati dell'applicazione al posto delle righe grezze del database.==

2. **Il DAO (Data Access Object):** 
	- ==è l'unico componente che "parla SQL".== 
	- ==Riceve e restituisce oggetti DTO, nascondendo completamente al resto dell'applicazione il fatto che ci sia un database dietro.==