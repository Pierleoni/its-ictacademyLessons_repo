# Introduzione a JUnit

Finora abbiamo visto come gestire dati in Java attraverso **[[Lezione 12 - Collection#Collection (Java)|Collection]]**, **[[Lezione 13 - Le map in Java#Introduzione alle Map in Java|Map]]** e relative implementazioni concrete come [[Lezione 13 - Le map in Java#Classe `HashMap<K,V>`|`HashMap`]] e [[Lezione 13 - Le map in Java#Classe `TreeMap`|`TreeMap`]].  
Abbiamo anche approfondito il concetto di **tipi primitivi e wrapper**, che è fondamentale per utilizzare correttamente le strutture generiche, come ad esempio:

- `int` → `Integer`
    
- `double` → `Double`
    
- `char` → `Character`
    

Questo perché molte classi generiche, comprese le collection e le mappe, possono lavorare solo con **oggetti reference**, e non con tipi primitivi.

In tutti questi casi, abbiamo definito classi, creato metodi, gestito chiavi, valori e strutture complesse.  
Ma come possiamo essere sicuri che **il nostro codice funzioni correttamente**? Come possiamo verificare che i metodi producano il risultato atteso, anche dopo modifiche successive?

Qui entra in gioco **JUnit**, il framework standard per il **testing unitario in Java**.

## Cos’è JUnit

JUnit è il **framework di testing più diffuso nell’ecosistema Java**.  
Fa parte della famiglia di framework **“xUnit”**, progettati per scrivere e eseguire **Unit Test automatici**, cioè test che verificano il comportamento di singole unità di codice, come **metodi o classi**.

L’uso di JUnit è ormai uno **standard de facto** per garantire la qualità del codice Java, perché permette di individuare errori precocemente, automatizzare il controllo dei comportamenti attesi e facilitare la manutenzione.

####  Breve storia

La storia di JUnit è strettamente legata all’evoluzione della pratica del testing:

- **1977**: ==nasce il concetto di xUnit grazie a Kent Beck, pioniere dell’Extreme Programming, e Erich Gamma, uno degli autori del famoso libro _Design Patterns_.==
    
- **JUnit 3**: ==per creare un test bisognava **estendere una classe base**, scrivendo i metodi di test al suo interno.==
    
- **JUnit 4 (2006)**: con l’introduzione delle annotazioni in Java 5, non era più necessario estendere una classe base. 
	- Le annotazioni (`@Test`, `@Before`, ecc.) rendevano il codice più chiaro e modulare. Questa versione è rimasta lo standard per oltre un decennio.
    
- **JUnit 5 (2017)**: rivoluzione completa. Supporta **lambda expression** e **stream di Java 8**, sfrutta le annotazioni più moderne e introduce un’architettura modulare, più flessibile e potente.
##### Differenze principali tra JUnit 4 e JUnit 5

JUnit 5 non è un unico blocco monolitico come le versioni precedenti, ma è composto da **tre sotto-progetti** distinti:

1. **JUnit Platform**  
    - È il motore che esegue i test, sia direttamente dall’IDE sia tramite strumenti di build come **Maven** o **Gradle**.
    
2. **JUnit Jupiter**  
    - La nuova **[[Lezione 6 - API#API (Application Programming Interface)|API]] per scrivere i test** con le nuove annotazioni, lambda e stream.  
    - È il cuore moderno di JUnit 5.
    
3. **JUnit Vintage**  
    - Modulo di compatibilità che permette di eseguire **test scritti con JUnit 3 o 4** all’interno del nuovo ambiente, garantendo retrocompatibilità.

> [!done] Questa evoluzione rende JUnit 5:
>
>- più modulare e flessibile
  >  
>- compatibile con le vecchie versioni
  >  
>- integrabile con strumenti moderni di sviluppo e build
  >  
>- in grado di sfruttare pienamente le funzionalità avanzate di Java 8 e successive
>

## Come funziona JUnit

Il funzionamento di JUnit può essere paragonato a quello di un **ispettore automatizzato** che verifica il corretto comportamento del nostro codice.

####  1️⃣ Preparazione del test

Il compito del **tester** (cioè dello sviluppatore) è preparare il **caso di test**:

- Si crea una **classe di test**, separata dalle classi di business, in cui si scrivono i metodi che vogliamo verificare.
    
- Per ogni metodo da testare si definiscono:
    
    - ==i **parametri di input**==
        
    - ==i **risultati attesi**, sia in caso di esito positivo sia in caso di errore o eccezione==
        

In pratica, il tester stabilisce **come dovrebbe comportarsi il codice** in ogni situazione prevista.

#### 2️⃣ Esecuzione e valutazione

Una volta preparati i test, JUnit si occupa di:

1. **Preparare l’ambiente**
    
    - Creare eventuali oggetti necessari
        
    - Eseguire i metodi di setup definiti con annotazioni come `@BeforeEach`
        
2. **Eseguire i test**
    
    - Far partire i metodi di test, che a loro volta invocano i metodi delle classi da verificare
        
3. **Valutare i risultati**
    
    - Confrontare i risultati ottenuti con quelli attesi
        
    - Segnalare eventuali discrepanze, indicando esattamente quale test è fallito e perché
        

In questo modo JUnit permette di **automatizzare completamente la verifica del codice**, riducendo al minimo l’errore umano e aumentando la **fiducia nella correttezza delle classi implementate**.


###  Esempio pratico: test della classe `Calcolatrice`

Per capire concretamente come funziona JUnit, consideriamo una **classe semplice di business**: la `Calcolatrice`.  
Questa classe espone alcuni metodi matematici di base, come `somma`, `divisione` e `potenzaPositiva`.

Vogliamo eseguire una serie di test per verificare che ciascun metodo produca il risultato corretto o, nei casi previsti, lanci l’eccezione giusta con il messaggio corretto.

####  1️⃣ Definizione dei casi di test

Alcuni esempi concreti:

|Metodo|Input|Risultato atteso|
|---|---|---|
|`somma(1,1)`|1,1|2|
|`somma(-1,1)`|-1,1|0|
|`potenzaPositiva(2,3)`|2,3|8|
|`potenzaPositiva(-10,2)`|-10,2|eccezione con messaggio: "Numeri non positivi"|
|`divisione(10,4)`|10,4|2.5|
|`divisione(10,0)`|10,0|eccezione con messaggio: "errore divisione per zero"|
Questi casi coprono sia **esiti corretti** sia **situazioni eccezionali**, in modo da testare la robustezza del codice.

#### 2️⃣ Realizzazione del progetto in Eclipse con Maven

Per gestire facilmente le dipendenze necessarie a JUnit, conviene creare un **progetto Maven**:

1. **Creazione del progetto**
    
    - Group Id: `Testing`
        
    - Artifact Id: `Testing`
        
2. **Aggiunta della dipendenza JUnit nel `pom.xml`**

```xml
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter-api</artifactId>
  <version>5.14.2</version>
  <scope>test</scope>
</dependency>
```


> [!attention] ⚠️ Lo `scope` **test** indica che la libreria JUnit sarà utilizzabile solo dalle classi che si trovano sotto `src/test/java`, mentre il codice di business sotto `src/main/java` resta indipendente.


4. **Creazione della classe di business**
    
    - Sotto `src/main/java` creiamo la classe `Calcolatrice` con tutti i metodi da testare.
        
5. **Creazione della classe di test**
    
    - Sotto `src/test/java` creiamo la classe di test, ad esempio `FirstTest`, dove inseriremo i metodi annotati con `@Test`.


###  Il concetto di asserzione

In JUnit, il concetto chiave per valutare il successo di un test è **l’asserzione**.

Un’**asserzione** è: 
- ==una **condizione logica che il programmatore assume essere sempre vera** in un determinato punto del codice.==  
In altre parole, è: 
- ==una **affermazione** sul comportamento atteso di un metodo o di una funzione.==

Con JUnit, le asserzioni permettono di stabilire **se un test ha avuto successo o è fallito**, confrontando il risultato effettivo del metodo con quello previsto.

#### Esempi pratici di asserzioni

Alcuni esempi concreti:

1. **Controllo di uguaglianza**  
    “Affermo che la somma di `1 + 1` **è uguale a 2**.”
    
2. **Controllo di verità di una condizione**  
    “Affermo che **è vero** che la somma di `1 + 1` è 2.”
    
3. **Controllo di eccezioni**  
    “Affermo che **invocando la divisione per zero viene sollevata un’eccezione**.”
    

In tutti questi casi, l’asserzione definisce il **comportamento atteso**, e JUnit verificherà automaticamente se questo comportamento corrisponde al risultato effettivo.

####  La classe `Assertions`

JUnit fornisce la classe **`org.junit.jupiter.api.Assertions`**, che ==mette a disposizione **[[Costruttori e modificatori#2. Metodi `static`|metodi statici]]** per definire le asserzioni dei test.==  
==Questi metodi modellano i vari casi di test e permettono di gestire sia **valori primitivi**, sia **oggetti**, sia **eccezioni**.==

I principali metodi sono:

1. **`assertEquals(expected, actual)`**  ^assertEquals
    
    - ==Verifica che il valore effettivo sia uguale a quello atteso==
        
    - ==Supporta anche **overloading** per tipi primitivi e oggetti==
        
2. **`assertTrue(BooleanSupplier supplier)`**  ^assertTrue
    
    - ==Verifica che la condizione logica fornita sia vera==
        
3. **`assertFalse(BooleanSupplier supplier)`**  ^assertFalse
    
    - ==Verifica che la condizione logica fornita sia falsa==
        
4. **`assertThrows(Class<? extends Throwable> exceptionClass, Executable methodCall)`**  ^assertThrows
    
    - ==Verifica che l’esecuzione di un determinato metodo produca l’eccezione specificata==


> [!NOTE] **Nota sulle interfacce funzionali**
> I parametri `BooleanSupplier` e `Executable` sono **[[Lezione 10 - Classi astratte e interfaccie#Interfacce funzionali|interfacce funzionali]]** che permettono l’uso delle **lambda expression** in Java 8+, rendendo le asserzioni più concise e leggibili.  
>Ad esempio:
>```java
>assertTrue(() -> calcolatrice.somma(1,1) == 2);
>assertThrows(ArithmeticException.class, () -> calcolatrice.divisione(10,0));
>```
>
>In questo modo, possiamo **modellare ogni comportamento atteso** direttamente all’interno della chiamata all’asserzione, senza creare variabili temporanee o blocchi aggiuntivi.

### `Supplier` e `Executable`
In Java, molte [[Lezione 10 - Classi astratte e interfaccie#Interfacce funzionali|interfacce funzionali]] standard ==servono a rappresentare **fornitori di valori** o **comportamenti specifici**.==  
Nel contesto di JUnit, le due interfacce funzionali più rilevanti sono **`BooleanSupplier`** e **`Executable`**.

####  `BooleanSupplier` 

`BooleanSupplier` è un’estensione di **`Supplier<T>`**, l’interfaccia funzionale standard di Java 8 che rappresenta un **fornitore di valori**.

- Nel caso di `BooleanSupplier`, ==il valore fornito è un **boolean**.==
    
- Ha un solo metodo astratto:
```java
boolean getAsBoolean();
```
Grazie alle [[Java/Lezione 16 Lambda Expression/Lambda#Interfacce Funzionali e espressioni Lambda|lambda]], possiamo implementarlo in modo conciso:
```java
() -> calcolatrice.somma(1, 1) == 2
```
- Qui la lambda **non prende parametri**, restituisce un booleano e rappresenta direttamente la condizione che vogliamo verificare con `assertTrue` o `assertFalse`.
    

In altre parole, `BooleanSupplier` permette di: 
- ==**incapsulare una condizione logica come oggetto**, pronta per essere valutata da JUnit.==

### `Executable`

`Executable` è un’interfaccia funzionale specifica di JUnit: 
- ==serve a rappresentare **un’operazione che può generare eccezioni**, utile soprattutto per testare comportamenti eccezionali.==

- Il metodo astratto è:
```java
void execute() throws Throwable;
```
La lambda relativa ha la forma:
```java
() -> { /* codice che può lanciare eccezioni */ }
```
Ad esempio:
```java
assertThrows(ArithmeticException.class, () -> calcolatrice.divisione(10, 0));
```

- Caratteristiche principali:
    
    - ==Non prende parametri==
        
    - ==Non restituisce valori==
        
    - ==Può sollevare eccezioni==
        

In pratica, `Executable` permette a JUnit di: 
- ==**eseguire un blocco di codice e verificarne eventuali eccezioni**, rendendo i test di errori chiari, concisi e sicuri.==


> [!link] **Collegamento con le asserzioni**
> Le due interfacce si integrano perfettamente con le **asserzioni di JUnit 5**:
> 
> |Interfaccia|Metodo|Uso tipico|
>|---|---|---|
>|`BooleanSupplier`|`getAsBoolean()`|`assertTrue`, `assertFalse` per verificare condizioni logiche|
>|`Executable`|`execute()`|`assertThrows` per verificare che un metodo lanci l’eccezione attesa|
>
>Grazie a queste interfacce funzionali e alle lambda expression, i test diventano:
>
>- più **concisi**
  >  
>- più **leggibili**
  >  
>- completamente **automatizzabili**


####  Esempio pratico di test con JUnit: la classe `FirstTest`

Per mettere in pratica quanto visto finora, realizziamo una **classe di test** chiamata `FirstTest` per verificare i metodi della classe `Calcolatrice`.

#### 1️⃣ Struttura della classe di test
La classe di test segue alcune regole fondamentali:

1. **Proprietà per la classe da testare**  
    ==All’interno della classe, definiamo una proprietà che rappresenta l’oggetto della classe di business da testare e lo istanziamo==:
```java
Calcolatrice calcolatrice = new Calcolatrice();
```

2. **Metodi di test**  
	==Ogni caso di test è realizzato come un **metodo `void` senza parametri**, con un nome descrittivo a piacere==.  
	Il metodo è annotato con `@Test`, indicazione che segnala a JUnit che si tratta di un **caso di test**.

#### 2️⃣ Test dei metodi semplici

**Somma con `assertEquals`**

```java
@Test
void testSommaPositiva() {
    assertEquals(2, calcolatrice.somma(1,1));
    assertEquals(0, calcolatrice.somma(-1,1));
}
```

- [[#^assertEquals|`assertEquals(expected, actual)`]] :
	- ==confronta il **risultato atteso** con quello **reale**.==
    
	- ==Se la condizione non è rispettata, il test fallisce automaticamente.==

#### 3️⃣ Test con [[#^assertTrue|`assertFalse`]]
È possibile verificare condizioni logiche negative:
```java
@Test
void testSommaNonDiversa() {
    assertFalse(() -> calcolatrice.somma(1,1) != 2);
}
```

- ==Qui stiamo affermando che **è falso** che `1 + 1` sia diverso da 2.==
    
- ==In altre parole, possiamo usare asserzioni anche per **condizioni negative**, a seconda del comportamento che vogliamo verificare.==


#### 4️⃣ Test di eccezioni con `assertThrows`

Per i metodi che possono generare eccezioni, come `divisione` o `potenzaPositiva` con numeri non validi:
```java
@Test
void testDivisionePerZero() {
    Exception e = assertThrows(ArithmeticException.class, 
        () -> calcolatrice.divisione(10, 0));
    assertEquals("errore divisione per zero", e.getMessage());
}
```

- [[#^assertThrows|`assertThrows(ExceptionClass.class, Executable)`]]:
	- ==verifica che venga lanciata **l’eccezione corretta**.==
    
	- ==Possiamo anche controllare il **messaggio associato all’eccezione** con un’ulteriore asserzione.==

###  Esecuzione dei test con JUnit

Dopo aver creato le classi di **business** (`Calcolatrice`) e di **test** (`FirstTest`), il passo successivo è **lanciare i test** tramite il framework di JUnit.

> [!attetion]  Non è necessario creare un `main` method: JUnit gestisce autonomamente l’esecuzione dei test.


#### Passaggi in Eclipse
1.  **Selezionare la classe di test** (`FirstTest`)
   
2. **Eseguire** tramite il comando:
```vbnet
Run As > JUnit Test
```

L’IDE si occuperà di far partire automaticamente tutti i metodi annotati con `@Test`.

Interpretazione dell'output:
L’esecuzione produce un **report visivo** che segnala lo stato dei test:

- **Linea verde** → tutti i test sono stati eseguiti con successo
    
- **Numero di test eseguiti / totale** → indica quanti test sono stati lanciati
    - Descritti col nome in dettaglio
- **Numero di errori** → indicano problemi imprevisti, come eccezioni non gestite
    
- **Numero di fallimenti** → indicano che un test **ha prodotto un risultato diverso da quello atteso**
[![Screenshot-2026-02-16-at-17-45-45-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png](https://i.postimg.cc/vT5c0691/Screenshot-2026-02-16-at-17-45-45-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png)](https://postimg.cc/n9cFzr3Z)
#####  Esempio di failure

Supponiamo di scrivere un’asserzione sbagliata:
```java
assertEquals(22, calcolatrice.somma(1,1));
```

Il report mostrerà:

- **Linea rossa** → indica un fallimento
    
- **7 test eseguiti su 7**
    
- **0 errori**
    
- **1 fallimento**, specificato nel dettaglio:
```java
sumok() 
expected: 22 but was: 2
```
Così, JUnit fornisce **informazioni precise sul test fallito**, rendendo semplice individuare e correggere l’errore.
[![Screenshot-2026-02-16-at-17-47-14-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png](https://i.postimg.cc/15Pt9Xw2/Screenshot-2026-02-16-at-17-47-14-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png)](https://postimg.cc/hhygsSC1)
In questo modo il ciclo di sviluppo con JUnit diventa **iterativo e sicuro**: puoi modificare il codice della `Calcolatrice` o aggiungere nuovi casi di test, eseguire nuovamente i test e verificare immediatamente se tutto funziona come previsto.

### Diversi tipi di test

Il test che abbiamo appena realizzato sulla classe `Calcolatrice` è un **Unit Test**.

Un **Unit Test** è: 
- ==un test che verifica il comportamento di una **singola unità di codice**, tipicamente un metodo o l’insieme dei metodi di una sola classe, isolandoli dal resto dell’applicazione.==

L’obiettivo è controllare che quella specifica porzione di codice:

- produca il risultato corretto dato un certo input
    
- gestisca correttamente le eccezioni
    
- rispetti il comportamento atteso in ogni condizione prevista
    

Gli Unit Test sono:

- veloci da eseguire
    
- semplici da scrivere
    
- altamente automatizzabili
    
- fondamentali per garantire la correttezza della logica interna
    

Tuttavia, nello sviluppo software esistono anche altri livelli di test, che si collocano in una struttura comunemente rappresentata come una **piramide**.

#### La piramide dei test

La cosiddetta _Test Pyramid_ organizza i test in base a:

- ==livello di astrazione==
    
- ==costo di esecuzione==
    
- ==complessità==
    
- ==numero ideale di test==
    

##### Struttura della piramide

1. **Base – Unit Test**
    
    - Numerosi
        
    - Veloci
        
    - Economici da mantenere
        
    - Testano singole classi o metodi
        
2. **Livello intermedio – Integration Test**
    
    - Verificano l’interazione tra più componenti
        
    - Ad esempio: una classe che comunica con un database o con un servizio esterno
        
    - Più lenti e più complessi degli Unit Test
        
3. **Vertice – End-to-End (E2E) / System Test**
    
    - Testano l’intero sistema come farebbe un utente reale
        
    - Simulano scenari completi
        
    - Sono più costosi e più lenti
        
    - Devono essere meno numerosi
[![Screenshot-2026-02-16-at-17-50-10-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png|491x336](https://i.postimg.cc/DwSKF3jc/Screenshot-2026-02-16-at-17-50-10-Microsoft-Power-Point-JUnit-5-01-Framework-Compatibility-Mode.png)](https://postimg.cc/tsGctwH1)

> [!faq]  Perché la forma a piramide?
>
>La forma a piramide indica che:
>
>- ==Alla base devono esserci **molti Unit Test**==
  >  
>- ==Meno Integration Test==
  >  
>- ==Ancora meno End-to-End Test==
   > 
>
>Questo perché:
>
>- ==Gli Unit Test sono rapidi e danno feedback immediato==
  >  
>- ==I test di livello superiore sono più costosi, fragili e complessi==
  >  
>
>Una buona strategia di testing prevede quindi:
>
>- ==Forte copertura con Unit Test==
   > 
>- ==Test di integrazione mirati==
  >  
>- ==Pochi test end-to-end per verificare i flussi principali==

