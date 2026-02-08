
## Collection (Java)

In Java, una **Collection** è un’interfaccia del package `java.util` che rappresenta **un insieme di oggetti**.  
Si può pensare a `Collection` come alla **radice di tutte le strutture dati principali**: da essa derivano infatti `List`, `Set`, `Queue` e altre strutture più specializzate.

> In pratica, qualsiasi tipo di struttura dati che voglia contenere oggetti e fornire operazioni di base (aggiunta, rimozione, ricerca…) implementa indirettamente `Collection`.


#### Caratteristiche principali

- Le Collection hanno alcune proprietà comuni importanti:

- **Gestiscono solo oggetti**, non tipi primitivi.  
    (Se vuoi usare un tipo primitivo, come `int`, Java lo trasforma automaticamente in un oggetto corrispondente tramite _autoboxing_, ad esempio in `Integer`.)
    
- Definiscono **operazioni generiche** che valgono per tutte le Collection:
    
    - aggiungere elementi
        
    - rimuovere elementi
        
    - cercare un elemento
        
    - verificare se un elemento è presente
        
    - contare quanti elementi ci sono
        
    - ottenere un **iteratore** per navigare sequenzialmente tra gli elementi
        

Queste operazioni costituiscono la base comune che tutte le Collection condividono, anche se le implementazioni concrete possono comportarsi in modo diverso.


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