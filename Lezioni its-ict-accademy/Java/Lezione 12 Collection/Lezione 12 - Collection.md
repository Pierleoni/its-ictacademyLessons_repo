
## Collection (Java)

In Java, `Collection` è un’interfaccia del package `java.util` ==che modella un **insieme di oggetti**.==

Rappresenta la **radice (root) della gerarchia delle strutture dati dinamiche:** 
- ==cioè il punto di partenza comune per tutte le principali collezioni del linguaggio.==

Quando si parla di Collection, non si fa riferimento a una struttura dati specifica (come un array o una lista), ==ma a un **contratto generale** che definisce cosa significa “gestire un insieme di elementi==”.

> L’interfaccia `Collection` ==stabilisce quali operazioni di base devono essere disponibili in qualunque struttura dati che contenga oggetti.==

Da questa interfaccia derivano altre sotto-interfacce più specializzate, come:

- `List`
    
- `Set`
    
- `Queue`
    

Ognuna di queste aggiunge regole specifiche sul comportamento degli elementi (ordine, duplicati, modalità di accesso, ecc.).


### Caratteristiche fondamentali di Collection

- Le Collection hanno alcune proprietà comuni importanti:

#### 1. Gestione esclusiva di oggetti

==Le Collection **accettano e gestiscono solo oggetti**, NON tipi primitivi.==

Questo significa che non possiamo inserire direttamente un `int`, un `double` o un `char`. Tuttavia, ==Java fornisce i **wrapper class** (`Integer`, `Double`, `Character`, ecc.) e grazie al meccanismo di **autoboxing** la conversione avviene automaticamente.==


Esempio:
```java
Collection<Integer> numeri = new ArrayList<>();
numeri.add(5);   // il valore 5 viene automaticamente convertito in Integer
```

####  2️. Operazioni generiche comuni

L’interfaccia `Collection` definisce una serie di **operazioni di base**, valide per qualunque tipo di collezione:

- ==aggiungere un elemento==
    
- ==rimuovere un elemento==
    
- ==verificare la presenza di un elemento==
    
- ==conoscere il numero totale di elementi==
    
- ==verificare se la collezione è vuota==
    
- ==ottenere un oggetto per la navigazione sequenziale (`Iterator`)==
    

Questi metodi non dipendono dalla struttura concreta (lista, insieme, coda…), ma rappresentano il **minimo comune denominatore** di tutte le Collection.

#### 3. Non esiste un’implementazione diretta

Un punto molto importante:  
- ==`Collection` è un’[[Lezione 10 - Classi astratte e interfaccie#Le interfacce|interfaccia]], quindi **non può essere istanziata direttamente**.==

Non possiamo scrivere:

```java
Collection<String> c = new Collection<>(); // ERRORE
```

Esistono invece:

- ==**sotto-interfacce** (`List`, `Set`, `Queue`)==
    
- ==**classi concrete** che implementano tali interfacce (es. `ArrayList`, `LinkedList`, `HashSet`, ecc.)==
    

Questo segue il principio della **programmazione contro interfaccia**: 
- ==si dichiara il tipo più generale possibile (`Collection` o `List`), ma si istanzia una classe concreta.==



#### 4. Duplicati: dipende dall’implementazione

Non tutte le Collection si comportano allo stesso modo:

- ==Alcune permettono **elementi duplicati** (es. le `List`)==
    
- ==Altre **non consentono duplicati** (es. i `Set`)==
    

Questa differenza non è definita direttamente da `Collection`, ma dalle sue sotto-interfacce.

###  Iterator

Per poter accedere agli elementi di una Collection in modo sequenziale, Java utilizza **[[Lezione 10 - Classi astratte e interfaccie#Le interfacce|l’interfaccia]]** `Iterator`, anch’essa nel package `java.util`.


> [!NOTE] **Nota**
> L'interfaccia Iterator è un interfaccia a se di rispetto all'interfaccia Collection

L’`Iterator` è uno strumento che: 
- ==consente di **navigare gli elementi senza conoscere la struttura interna della collezione**.==

Questo è un concetto fondamentale:  
- ==non importa se la Collection è una lista, un insieme o una coda — l’iteratore fornisce un modo uniforme per attraversarne gli elementi.==
#### Ottenere un Iterator

Ogni Collection mette a disposizione il metodo:
```java
iterator()
```
che restituisce un oggetto `Iterator`.

Esempio: 
```java
Collection<String> nomi = new ArrayList<>();
Iterator<String> it = nomi.iterator();
```

####  Metodi principali di Iterator

L’interfaccia `Iterator` definisce tre metodi fondamentali:

#### 1. `boolean hasNext()`

- ==Verifica se esiste un elemento successivo.==  
- ==Serve per controllare se l’iterazione può continuare.==

#### 2. `Object next()`

- ==Restituisce l’elemento successivo e sposta l’iteratore in avanti.==

- ==È importante notare che `next()` modifica la posizione interna dell’iteratore.==

#### 3. `void remove()`

- ==Rimuove l’ultimo elemento restituito da `next()`.==

###### Ciclo tipico con Iterator

L’utilizzo standard è il seguente:

```java
Iterator<String> it = nomi.iterator();  
while (it.hasNext()) {     
	String nome = it.next();     
	System.out.println(nome); 
}
```

Il ciclo continua finché esistono elementi.

> [!info] **Nota importante sull’uso**
>  
>
>==Un `Iterator` può essere utilizzato **una sola volta** per percorrere la Collection.==
>
>Una volta terminata l’iterazione:
>
>- ==non si può “tornare indietro”==
  >  
>- ==non si può riutilizzare lo stesso Iterator==
   > 
>
>==Per effettuare una nuova scansione è necessario chiamare nuovamente `iterator()`.==


> [!link] **Collegamento concettuale**
>
>L’Iterator è un esempio del principio di **separazione tra struttura e navigazione**:
>
>- ==La Collection si occupa di contenere e organizzare gli elementi.==
  >  
>- ==L’Iterator si occupa di attraversarli.==
  >  
>
>Questo rende il codice più flessibile e indipendente dall’implementazione concreta.


> [!faq] `Iterato` vs Loop
> ==Abbiamo detto che `Iterator` è un interfaccia separate e che serve ESCLUSIVAMENTE per navigare una Collection==
> **Perché allora non basta un semplice `for`?**
> Qui la differenza è sostanziale: 
> - un ciclo `for` classico funziona bene ==**solo quando hai accesso tramite indice**, ad esempio con un array o con una `List`:==
>```java
> for (int i = 0; i < lista.size(); i++) {
>    System.out.println(lista.get(i));
>}
>
>```
>Questo funziona perché:
>
>- le liste hanno un ordine definito
 >   
>- esiste il concetto di indice
  >  
>- esiste il metodo `get(i)`
>Ma ora pensiamo ad un `Set`. 
>I `Set` in Java: 
>- ==non garantiscono l' ordine degli elementi==
 >   
>- ==non hanno indici==
 >   
>- ==e quindi non hanno un metodo `get(i)`==
  >  
>
>==Quindi un `for` con indice **non è applicabile a tutte le Collection**.==
>
>Di conseguenza l'`Iterator` serve a fornire un meccanismo uniforme di attraversamento indipendente dal tipo concreto di Collection.
>In altre parole: 
>>**Non importa se si sta usando una `List`, un `Set` o una `Queue`:**
>>-  ==l’Iterator ti permette di scorrerli tutti allo stesso modo.==
>Questo è un esempio di **programmazione contro interfaccia.**
>Quindi si può scrivere codice generico: 
>```java
>public void stampa(Collection<String> c) {
 >   Iterator<String> it = c.iterator();
 >   while (it.hasNext()) {
 >       System.out.println(it.next());
 >   }
>}
>
>```
>
>Quindi l'uso dell'`Iterator` garantisce lo scorrimento e la navigazione su qualsiasi tipo concreto di collection(`ArrayList`, `LinkedSet`, `HashSet`, ecc.), senza sapere quale implementazione concreta sta utilizzando la Collection in questione.
>**E il ciclo `while`?**
>==Il `while` è solo una struttura di controllo.== 
>Non permette di sapere **come ottenere l'elemento successivo** da una struttura dati generica.
>L'`Iterator` invece: 
>- ==incapsula lo stato della posizione corrente==
 >   
>- ==gestisce internamente il modo in cui si passa all’elemento successivo==
  >  
>- ==nasconde la struttura interna della Collection==
>  
>**E allora se si usasse un `for-each` per navigare lungo una qualsiasi  collection?**
>La risposta è si, si può fare!
>MA: 
>quando si scrive
>```java
>for (String s : collection) {
>    System.out.println(s);
>}
>
>```
>
>==In realtà si sta usando internamente un Iterator.==
>Il compilatore lo trasforma in qualcosa di equivalente a: 
>```java
>Iterator<String> it = collection.iterator();
>while (it.hasNext()) {
 >   String s = it.next();
 >   System.out.println(s);
>}
>
>```
>
>Quindi il `for-each` ==è solo una sintassi più compatta sopra l'iterator==.
>Un altro motivo fondamentale è: 
>- ==L'Iterator permette di rimuovere elementi durante l'iterazione in modo sicuro.==
>```java
>Iterator<String> it = collection.iterator();
>while (it.hasNext()) {
>    if (it.next().equals("test")) {
>        it.remove();
>    }
>}
>
>```
>Se provassi a rimuovere elementi con un `for` tradizionale mentre stai iterando, potresti ottenere una `ConcurrentModificationException`.
>Questo perché il `for-each` è pensato, in Java, per iterazioni di sola lettura o comunque senza modifiche strutturali. 
>Quindi se si devono: 
> - ==rimuovere elementi==
>   
>- ==filtrare elementi==
> 
>- ==fare modifiche durante l’attraversamento==
> Allora l'Iterator è lo strumento corretto
>

### Architettura delle Collection
Per comprendere meglio cosa sono le Collection e come sono organizzate, è utile osservare la **gerarchia delle interfacce** che compongono il framework.

Come si può notare dallo schema, l’interfaccia `Collection`: 
- ==rappresenta il **punto di partenza comune** (root) della gerarchia.==

Da essa derivano diverse sotto-interfacce più specifiche, ognuna con caratteristiche proprie.
[![Screenshot-2026-02-13-at-12-05-05-Java-12-Collection-Java-12-Collection-pdf.png](https://i.postimg.cc/ZndF12Y7/Screenshot-2026-02-13-at-12-05-05-Java-12-Collection-Java-12-Collection-pdf.png)](https://postimg.cc/ZvJdNfdp)
#### Struttura principale della gerarchia 
Partendo da sinistra:

- L’interfaccia `Set` **estende** (`is-a`) l’interfaccia `Collection`.  
    ==Un `Set` è quindi una Collection con una regola fondamentale: **non ammette duplicati**.==
    
- L’interfaccia `SortedSet` estende `Set`.  
    ==Aggiunge la caratteristica dell’**ordinamento automatico degli elementi** secondo un criterio naturale o definito da un `Comparator`.==
    
Al centro:

- L’interfaccia `List` estende `Collection`.  
    Una `List` rappresenta ==una sequenza ordinata di elementi==:
    
    - ==mantiene l’ordine di inserimento==
        
    - ==consente duplicati==
        
    - ==permette accesso tramite indice==

A destra:

- L’interfaccia `Queue` estende `Collection`.  
    ==Modella una struttura dati tipicamente utilizzata per gestire elementi secondo una politica==:
    
    - ==FIFO (First In First Out)==
        
    - ==oppure altre varianti a seconda dell’implementazione==

L’albero mostrato nello schema **non rappresenta l’intero framework delle Collection**, ma solo la struttura principale delle interfacce.

Per ciascuna di queste sotto-interfacce esistono diverse **classi concrete** che ne forniscono l’implementazione.

Ad esempio:

- `List` → `ArrayList`, `LinkedList`
    
- `Set` → `HashSet`, `TreeSet`
    
- `Queue` → `LinkedList`, `PriorityQueue`
    

Questo significa che:

> ==Le interfacce definiscono il _contratto_ (cosa si può fare),==  
> ==le classi concrete definiscono il _comportamento reale_ (come viene fatto).==


### Interface `List`

```java
public interface List<E> extends Collection<E>
```

L’interfaccia `List` rappresenta: 
- una **collezione sequenziale di oggetti**, cioè una struttura dati in cui gli elementi vengono mantenuti in un ordine ben preciso.

A differenza di altre Collection, una `List` è caratterizzata dal fatto che:

- ==mantiene l’**ordine di inserimento** (o comunque un ordine definito)==
    
- ==consente l’**accesso diretto agli elementi tramite indice**==
    
- ==**ammette duplicati**==
#### Accesso tramite indice

Uno degli aspetti fondamentali della `List` è che: 
- ==ogni elemento occupa una **posizione numerata** (indice).==

Questo permette operazioni come:
```java
list.get(0);      // recupera il primo elemento
list.set(1, x);   // sostituisce l’elemento in posizione 1
list.add(2, y);   // inserisce un elemento in una posizione specifica
```

L’accesso indicizzato è ciò che distingue concettualmente una `List` da un `Set`, dove non esiste il concetto di posizione.

#### Duplicati
Una `List` può contenere più volte lo stesso elemento:
```java
list.add("A");
list.add("A");
```
Entrambi gli elementi verranno mantenuti.

Questo la rende adatta a rappresentare sequenze, cronologie, raccolte ordinate di dati, ecc.

#### Funzionalità aggiuntive rispetto a Collection

Oltre ai metodi ereditati da `Collection`, l’interfaccia `List` introduce operazioni specifiche per:

- i==nserimento in una posizione precisa==
    
- ==ricerca dell’indice di un elemento (`indexOf`, `lastIndexOf`)==
    
- ==sostituzione di elementi==
    
- ==estrazione di sotto-liste (`subList`)==
    

Queste operazioni sono possibili proprio perché la `List` ha una struttura sequenziale e indicizzata.

#### `ListIterator`

Oltre all’`Iterator` standard, una `List` fornisce un iteratore più potente: `ListIterator`.

==`ListIterator` è una specializzazione di `Iterator` che aggiunge funzionalità avanzate.==

La differenza principale è che consente lo **scorrimento bidirezionale**:

- ==avanti (`next()`)==
    
- ==indietro (`previous()`)==
    

Inoltre permette:

- ==di conoscere l’indice corrente==
    
- ==di modificare elementi durante l’iterazione==
    
- ==di inserire nuovi elementi durante la scansione==
    

Questo è possibile solo nelle `List`, perché solo esse hanno un ordine e un concetto di posizione.

---

#### Metodi principali (concettuali)
cco i metodi più importanti che tutte le Collection offrono:

- `add(E e)` → aggiunge un elemento alla Collection
    
- `remove(Object o)` → rimuove un elemento specifico
    
- `contains(Object o)` → verifica se un elemento è presente
    
- `size()` → restituisce il numero di elementi
    
- `isEmpty()` → controlla se la Collection è vuota
    
- `iterator()` → restituisce un **Iterator**, cioè un oggetto che permette di scorrere gli elementi uno alla volta



#### Implementazione
L’interfaccia `Collection` **non ha implementazioni dirette**: non puoi creare un oggetto di tipo `Collection` da sola.

Al contrario, esistono:

- **Sottointerfacce**, come `List`, `Set` e `Queue`, che definiscono comportamenti più specifici
    
- **Classi concrete** che le implementano, ad esempio `ArrayList`, `HashSet` o `LinkedList`
    

Ogni classe concreta decide **come memorizzare gli elementi** e **quali regole rispettare**, ad esempio se accettare duplicati o mantenere l’ordine di inserimento.


#### Duplicati
Non tutte le Collection si comportano allo stesso modo rispetto ai duplicati:

- Alcune Collection **consentono duplicati**, come `List` (possono esserci più copie dello stesso elemento)
    
- Altre **non li consentono**, come `Set`, dove ogni elemento è unico
    

Questa differenza è fondamentale da ricordare quando si sceglie la Collection più adatta a un certo problema.



### Iterator

#### Cos’è un Iterator
Un **Iterator** è un’interfaccia che serve a **navigare sequenzialmente all’interno di una Collection**.

- Ogni Collection può fornire un Iterator tramite il metodo `iterator()`.
    
- L’Iterator permette di scorrere gli elementi **senza conoscere come la Collection li memorizza internamente**.
    
- È lo strumento principale per leggere gli elementi in modo sicuro e controllato.
    


##### Come si ottiene
```java
Iterator<E> it = collection.iterator();
```

- L’iteratore è **indipendente dalla struttura interna** della Collection.
    
- Permette di attraversare gli elementi **senza conoscerne l’implementazione**.
    



#### Metodi dell’interfaccia Iterator
I metodi principali di un Iterator sono:

- `hasNext()` → ritorna `true` se c’è ancora almeno un elemento da leggere
    
- `next()` → restituisce l’elemento corrente e sposta l’iteratore al successivo
    
- `remove()` → rimuove l’elemento restituito dall’ultimo `next()` dalla Collection
    

> Nota: `remove()` funziona solo subito dopo aver chiamato `next()`.


#### Regole importanti

- **Un Iterator è monouso:** una volta terminata l’iterazione, non può essere riutilizzato.  
    Per scansionare di nuovo la Collection, bisogna crearne uno nuovo.
    
- Usare un Iterator è **più sicuro** rispetto a un ciclo `for` tradizionale se stai rimuovendo elementi durante la navigazione.  
    Questo evita errori di **modifica concorrente**, tipici quando si altera una Collection mentre la si sta scorrendo.
    

### Architetture delle Collection
Per comprendere meglio l'architettura delle collection riferiamoci a questa immagine: 

[![Archiettettura-delle-collection-pdf.png](https://i.postimg.cc/8c1VRS9T/Archiettettura-delle-collection-pdf.png)](https://postimg.cc/KksVbdmW)
**Per ognuna di queste interfacce ci sono diverse implementazioni concrete**

### Interface List 
```java
public interface List extends Collection
```

Una **List** è una **collezione sequenziale di oggetti**, cioè una struttura in cui gli elementi sono ordinati in base all’ordine di inserimento.

- L’accesso agli elementi avviene **tramite indice**, simile a un array: 
	- puoi leggere, aggiornare o rimuovere un elemento conoscendone la posizione.
    
- ==Una List **ammette duplicati**, quindi è possibile inserire più volte lo stesso oggetto.==
    
- Oltre alle funzionalità ereditate da `Collection` (aggiungere, rimuovere, cercare, iterare…), `List` offre **metodi specifici per l’inserimento e la ricerca** in posizioni precise, ad esempio:
    
    - `get(int index)` → ==restituisce l’elemento in una posizione specifica==
        
    - `add(int index, E element)` → ==inserisce un elemento in una posizione specifica==
        
    - `indexOf(Object o)` → ==restituisce l’indice della prima occorrenza di un elemento==
        
- Per scorrere una List esiste un **iteratore speciale**, il `ListIterator`, che **estende Iterator** e permette uno **scorrimento bidirezionale** (sia in avanti che indietro), oltre a consentire modifiche durante l’iterazione.

###  Le Liste in Java

Le **Liste** sono rappresentate da diverse implementazioni concrete, tra le più comuni troviamo:

- `ArrayList<E>` → una lista basata su array dinamici, ideale per accessi rapidi tramite indice
    
- `Vector<E>` → simile ad ArrayList, ma **thread-safe** (sincronizzata)
    
- `LinkedList<E>` → una lista basata su nodi collegati, più efficiente per inserimenti e cancellazioni frequenti all’interno della lista
    

> Il simbolo `E` rappresenta il **tipo generico degli elementi** contenuti nella lista.  
> Quando si crea una lista concreta, è buona pratica specificare il tipo degli oggetti che conterrà, ad esempio:
```java
List<String> nomi = new ArrayList<>();
List<Integer> numeri = new LinkedList<>();
```


Il vantaggio di `E` tra `Object`è: 
Object è la classe padre di tutti gli oggetti di Java, potremo anche tipizzare la lista come lista di Object ma poi se in questa lista ci metto una stringa, il telecomando punta all'oggetto String ma con una freccia Object, Quindi per poter usare i metodi delle stringhe dovrei fare il casting dell'oggetto di Object a stringa e poi utilizzare i metodi delle stringhe. 
Per questo i programmatori della Oracle hanno implementato il placeholder `E`. 
Difatti `E` è solo un placeholder per indicare che la lista o l'ArrayList o la collection prende un qualsiasi tipo di dati 

### Classe ArrayList 

mplementa List attraverso array di dimensione variabile
**Costruttori:**
1. `ArrayList()`: 
	- Costruisce un array di dimensione iniziale 10
2.  `ArrayList(Collection<E> c)`:
	- Costruisce un array a partire da una collezione data di oggetti
3. `ArrayList(int initialCapacity)` :
	- Costruisce un array vuoto specificando la capacità iniziale.
Gli array list ogni volta che lo inizializziamo a 10 elementi e ci mettiamo l'undicesimo, l'array list butta il vecchio array e ne inizializza uno nuovo di undici elementi e cosi via per ogni singolo elemento inserito dopo la inizializzazione. 
Per questo il costruttore n.3 serve per migliorare le prestazioni ma non cambia la sostanza 
Il secondo costruttore invece non trasfomara o castizza le collection ma sfrutta il principio dell'albero binario 
#### Metodi 
**Per l'inserimento**: 
- `public void add(int index, E element)`
	- In base all'indice scala gli elementi gia presenti e aggiunge il nuovo elemento al primo posto libero e non lascia buchi 
- `public boolean add(E element)`: 
	- Aggiunge gli elementi in coda 

- `public E set(int Index, E element)`: 


### Classe LinkedList
La classe **`LinkedList`** è un’implementazione dell’interfaccia `List` basata su una **lista concatenata (linked list)**.  
In questa struttura, ogni elemento è collegato al precedente e al successivo, anziché essere memorizzato in posizioni contigue di memoria come avviene negli array.
#### Caratteristiche principali

- Implementa l’interfaccia `List` utilizzando una **lista linkata**.
    
- Oltre ai metodi standard ereditati da `List`, mette a disposizione **metodi specifici** per:
    
    - inserire elementi all’inizio e alla fine della lista
        
    - leggere elementi all’inizio e alla fine della lista
        
    - rimuovere elementi all’inizio e alla fine della lista
        
- È particolarmente adatta per gestire:
    
    - **code (queue)** → inserimento in coda e rimozione in testa
        
    - **pile (stack)** → inserimento e rimozione in testa
        
- I **costruttori** sono simili a quelli di `ArrayList` (vuota, oppure inizializzata con un’altra Collection).
    
- Come `ArrayList`, **non è sincronizzata**, quindi non è thread-safe di default.

##### Metodi specifici di `LinkedList`

`LinkedList` fornisce metodi aggiuntivi che operano direttamente sugli estremi della lista:

- `addFirst(E element)`  
    → inserisce un elemento all’inizio della lista
    
- `addLast(E element)`  
    → inserisce un elemento alla fine della lista
    
- `getFirst()`  
    → restituisce il primo elemento senza rimuoverlo
    
- `getLast()`  
    → restituisce l’ultimo elemento senza rimuoverlo
    
- `removeFirst()`  
    → rimuove e restituisce il primo elemento
    
- `removeLast()`  
    → rimuove e restituisce l’ultimo elemento


### Interfaccia `Set` in Java

- **Cos’è**:  
    - ==`Set` è un’interfaccia che estende `Collection` e rappresenta una **collezione di elementi senza duplicati**.==  
    - In altre parole, un `Set` modella un **insieme matematico**, dove ogni elemento può comparire **al massimo una volta**.
    
- **Regola fondamentale**:  
    - ==Un `Set` **non può contenere due elementi `e1` ed `e2` tali che `e1.equals(e2)` restituisca `true`**.==  
    - ==Questo significa che l’uguaglianza degli elementi viene determinata tramite il metodo `equals()`, non solo dall’identità degli oggetti.==
    
- **Caratteristiche principali**:
    
    - **Non mantiene un ordine specifico degli elementi** (eccetto alcune implementazioni, come `LinkedHashSet` e `TreeSet`).
        
    - Garantisce l’unicità degli elementi automaticamente: ==se provi ad aggiungere un duplicato, l’operazione sarà ignorata.==
        
- **Implementazioni comuni**:
    
    1. **`HashSet`**:
        
        - ==Basato su hash table.==
            
        - ==Operazioni veloci (`add`, `remove`, `contains` in media O(1)).==
            
        - ==Non mantiene alcun ordine degli elementi.==
            
    2. **`LinkedHashSet`**:
        
        - Simile a `HashSet`, ma mantiene l’**ordine di inserimento**.
            
        - Utile se vuoi iterare sugli elementi nello stesso ordine in cui li hai aggiunti.
            
    3. **`TreeSet`**:
        
        - Basato su **albero rosso-nero** (struttura ordinata).
            
        - ==Mantiene gli elementi **ordinati secondo l’ordine naturale** o un comparatore personalizzato.==
            
        - ==Operazioni più lente (O(log n)) rispetto a `HashSet`.==

[![Screenshot-2026-01-28-at-15-06-11-Java-12-Collection-Java-12-Collection-pdf.png|458x273](https://i.postimg.cc/ZnskhBfM/Screenshot-2026-01-28-at-15-06-11-Java-12-Collection-Java-12-Collection-pdf.png)](https://postimg.cc/m19pYDWY)

Un set non ragiona con equals, abbiamo detto che i set non accettano doppioni.
Come fa: 
guardando l'immagine possiamo vedere che l'interfaccia Set ha implementazioni filgie di HashSet e TreeSet

> [!NOTE] Title
> Il suffisso Hash, Tree indica l'implementazione mentre la seconda parte indica che appartiene all' interfaccia padre Set.

Co'è un HashSet?
Immagianiamo a uno schedario con vari cassetti dove vi sono varie schede, la struttura dati che lo rappresenta è un array i cui elementi sono liste, ciascuna lista è un bucket.
Immaginiamo che in questo schedario contenga libri per ordine alfabetico degli autori, cosi quando andiamo a chiedere un libro del manzoni andiamo al casetto M. 
La suddivsione in casetti ed un ulteriore divisione interna rende più facile l'estrazione del singolo elemento e la ricerca di quell'elemento.
Ogni elemento lo infila in una LinkedList. 
Lo HashSet non ha lettere ma numeri: associa che ogni oggetto entrate abbia un codice numerico; tutti gli oggetti in ingresso con codice da 1 a 200 li mette nel primo casetto e cosi via. 
Il codice in questione è l'hashcode
#### Hashcode 
È un metodo di Object che non ha parametri ma restiusice un long.
L'hashcode è un codice non univoco; due oggetti possono essere diversi ma avere lo stesso hashcode.
Implementarlo non è banale 
A cosa serve? A dare un codice abbastabza univoco all'oggetto.
Riprendendo l'esempio dello schedario se un oggetto ha un hashcode 55 va messo nel primo casetto ma un altro oggetto pouò avere lo stesso codice.
Quindi lavorare con un equals per gli array è sufficiente ma non per gli hashset. 

La regola è che due oggetti uguali per la equals allora devono avere lo stesso hashcode.
Questo si cihama il contratto che collega a filo doppio gli oggetti. 
Quindi facendo l'overriding questa regola deve sempre essere rispettata.
Se $A=>B$ e la stessa cosa nel dire $not B => not A$ 
Quindi se due oggetti hanno due hashcode diversi allora sono due oggetti diversi. 
Quindi in un oggetto Impiegato applica prima l'hashcode che l'equals.
Primo scenario: 
Nessun oggetto ha lo stesso hashcode :
L'oggetto entrate non condivide l'hahscode con nessun oggetto dentro il primo casetto dello scheadrio allora prima applica il teorema all'incotrario, quindi vuol dire che non sono uguali e lo mette nel rpimo casetto 
Seconda scenraio:
L'oggetto entrate condivide lo stesso hashcode con un oggetto già presente nello stesso casetto. 
Quindi in questi casi applica l'equals e vede se: 
I due oggetti hanno lo stesso hashcode ma diverso equals l'oggetto nuvo entra nello schedario 
I due oggetti hanno lo stesso hashcode ma equals uguale, allora l'oggetto entrante è un doppio e non verrà storato. 
Ricordiamoci che equals confronta più valori, campo campo, mentre l'hashcode confronta solo un numero, quindi l'hashcode è più veloce di equals; equals è l'ultima spiaggia per casi al limite. 
Caso limite:
Supponiamo di implementare da solo il metodo hashcode della classe con un return 5, il problema è che tutti gli oggetti hanno lo stesso hashcode quindi chiamerebbe sempre equals e il codice diventerebbe molto lento. 
Inoltre leveremmo la priorità agli oggetti entrati e già storati.
Difatti un hashcode fatto bene è un codice abbastanza univoco: 
possono esserci doppioni ma comunque molti oggetti non condivideranno lo stesso hahscode.
Quindi gli oggetti dell'isnieme hashset dovrebbero ridefinire: 
- il metodo boolean equals Object : per distinguere "doppioni"
- Il metodo int hashcode : per gestione dei buckets


**Esempio d'uso di HashSet**
```java
HashSet<String> ha = new HashSet<String>();
ha.add("serpente");
ha.add("ape");
ha.add("farfalla");
ha.add("farfalla"); // NON viene aggiunto!
ha.add("furetto");
ha.add(“gattino");
for (String entry: ha) {
	System.out.println(“elemento: “ + entry);
}
```

Il metodo add dell'interfaccia Collection ritorna un booleano: 
- finora sempre True 
- l'add con l'indice è void 
- Ma con i set se inseriamo un doppione ritorna False.
In questo esempio è ragionevole stampare il ritorno ma non è obbligatorio, infatti 


#### LinkedHashSet
La differenza con gli HashSet è che questi non hanno un ordine d'inseriemnto, non è randomico ma unpredictable perché sistema gli oggetti in base all'hashcode e se li sistema nei buckets.
Invece i LinkedHashSet qaundo ciclati mantengono l'ordine di inserimento, per il resto è uguale al padre HashSet

### TreeSet
Fratello di Hashset, è ordinato in base agli alberi binari.
I TreeSet non supporta diversi criteri di ordinamento, se volessimo creare un nuvo criterio di ordinamento bisogna fare un nuovo TreeSet.
Il criterio di ordinamento dei TreeSet è l'abero binario: sono perfetti per gli insiemi ordinati. 
Il metodo da implemetare rispetto al HashSet è uno solo: 
CompareTo: se si vuole fare un TreeSet di impiegati ogni Impiegato deve avere il compareTo. 

**Esempio**
VOgliamo creare un TreeSet di String
Le stringhe sono cofrontabili e il criterio è quello che induce l'ordinaamento alfabetico 
```java
TreeSet<String> set = new TreeSet<String>();
set.add("dog");
set.add("ant");
set.add("horse");
set.add(“gorilla");
for (String element: set) {
	System.out.println(element);
}
```

GLi elementi inseriti verrano 