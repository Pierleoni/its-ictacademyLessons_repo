Abbiamo già visto il concetto di Design Pattern, le categorie dei DP e ne abbiamo descritti alcuni(Singleton, Adapter e Strategy). 

Ora vedremo 
Il singleton
Il Factory 
Il Proxy 
L'Observer 

In realte il pattern proxy è stato accenato con la dependency injection(con le annotation di Spring). 

I Desgin pattern sono uno struemnto di progettazione, il bravo sviluppatore dovrebbere conscerne almeno un po almeno quelli elencati dal GoF. 

Per ricordare/riconoscere un pattern dobbiamo legarlo al tipo di scenario che deve risolvere. 

Esistono le famiglie dei DP: 
Arcihetteturali


Abbiamo gia visto lo strategy e l'adapter.
Oggi vedremo il Factory method e il Singleton che appartengono alla famiglia dei creazionali(quindi al momento della creazione dell'oggetto)


### Pattern Creational
Factory method: 
SI vuole creare un oggetto di cui staticamente si conosce l'interfaccia (o la super clase ) mentre la classe effettiva viene decisa dinamicamente. 
Tipicamente situazioni che compare nei Framework.

Il meccanismo di facotry l'abbiamo già visto nei progetti di Spring 
Vuole separare chi fabbrica l'oggetto da chi lo usa. 
Analogalmente i vestiti che indossiamo non li fabbrichiamo noi ma li compriamo e li utilizziamo, quindi anche qui c'è chi fabbrica gli oggetti che usiamo e i consumatori che li usano. 
- Separare chi crea l'oggetto da chi li usa 
- Definire l'interfaccia degli oggetti da creare 
- Incapsulare la logica di creazione ini iiuna classe Factory che crea oggetti specifici(che concretizzano l'interfaccia)
- Si ottiene che ci usa gli oggetti non deve conoscere il tipo esatto dell'oggetto. 

QUesto pattern sta dietro a tutti i framework che utilizzano il IoC: in spring le annotation collegano(fanno da interfaccia) e si occupa di istanziare l'oggetto.

### Diagramma Facotry Method
C'è il consumer che invoca la Facotry e gli chiede di 
La facotry istanzia un oggetto di COncreteProduct che implementa l'interfaccia Product. 
Chi consuma deve sapere solo come usarla 


Vantaggi: 
Grazie al polimorfismo, ogni oggetto conreto opera seconda la sua "natura" senza debba essere nota a priori 
La struttura è facilmente estensibile aggiungendo COnreteProduct.
La classe Facotry potrebbe incapsulare politche di creazione(un solo oggetto(quello che fa Spring ad esempio sull'oggetto della classe Controller, un pool di oggetti(ad esempio quando si opera con le connessioni con un db tramite classe che gestisce un pool di conn e le presta alla DAO), ecc)

#### Java Reflection 
Io voglio poter istanziare una classe senza sapere il nome delal classe da istanziare? 
2 metodi: 
1. Tramite `Class`: 
	- Immaginiamo di fare la new di una certa classe, quello che si vuole fare moralmente è `new x()` ma java non premette di fae cio 
	- Permette di istanziare una classe a partire dal nome: 
```java

String s = "....";
Class cl = Class.forName("java.lang.String")
```
Ti importa dinamicamente la classe che vogliamo istanziare ma non consosciamo.
Quindi questo metodo carica la classe per nome. 
Torna un oggetto `Class`. 
Ora che ho `cl:Class`
```java
Object obj = cl.newInstance(); 
```
questo metodo istanzia la classe che ha appena importato tramite il metodo precedente.
Quindi istanzia l'oggetto della classe. 
Ora di solito le factory sono sviluppate in questo modo. 
Gli oggetti della classe da istanziare in questo modo deve avere un costruttore a 0 args(quello di default), al 99% dei casi va bene. 
`newIstance` torna un `Object`, quindi quando provo a fare 
```
obj.
```
Potro utilizzare solo i metodi di object.
Pero adesso vlogliamo che qualsiasi classe passiamo istanzia l'oggetto senza dover rimettee mano ogni volta al codice della factory
```
String s = "..."; // implementazione di Prodotto

Class cl = Class.forName(s); // carico la classe per nome 
Prodotto p = (Prodotto) cl.newInstance(); //istanzio l'oggetto delal classe 
p.getPrezzo(); 
p.getCosto(); 
```


### Singleton 
SI usa per garantire che eisista una ed sola istnaza di una certa classe 
Soluzione 
Impedire la possibilità di creare liberamente oggetti di una certa classe tramite costruttore 
L'idioma Java per implementare il pattern del SIngleton prevede di dichiarare 
1. Costruttore privato
2. Un metodo pubblico e statico che restituisce l'istanza richiesta (agendo all'occorenza sul costruttore o sull'attributo)
3. Un Attributo privato e statico del tipo della classe. 
### Diagramma Singleton 
Il Client usa il metodo statico getInstance per ottenere l’istanza unica dell’oggetto (poiché 
non ha accesso al costruttore)
Il metodo getInstance potrà avere un comportamento lazy (crea alla prima richiesta) oppure 
crea al caricamento della class
[![Screenshot-2026-03-27-at-15-11-22-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/q7tB7DZ7/Screenshot-2026-03-27-at-15-11-22-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/McSJP5wk)

### Composite (Da portare all'esame)
Pattern molto particolare, risolvere problemi specifici
Quando abbiamo fatto gli algoritmi a inizio corso abbiamo parlato degli algoritmi ricorsivi(es: l'algoritmo ricorsivo). 
Non tutti gli algo possono essere fatti in maniera ricorsiva ma in alcuni casi è la soluzione più elegante. 
Questo pattern è la ricorsione a livello di progettazione. 
Serve per risolvere problemi quando c'è una ricorsione a livello delgi oggetti.
Problema: 
- VOlgiao rappresentare un oggetto con una struttura ricorsiva, ad albero, senza aver ridondanza nel diagramma e di conseguenza nel codice (es: struttura di directories di un file system)
- VOgliamo agire sulle folgie e sulla struttura in modo unifomre, senza conoscere a priori la parte su cui stiamo agendo → accesso tramite un interfaccia comune. 
**Soluzione:**
- Realizzare un interfaccia generica Componente, che modella gli elementi della composizione e la composizione stessa
- L'interfaccia viene implementata salla folgia e dalla composizione.
[![Screenshot-2026-03-27-at-15-25-49-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/Gp7CvF6d/Screenshot-2026-03-27-at-15-25-49-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/R3HyBHMD)
Guardando il diagramma abbiamo una relazzione is-a e una relazione has-a.
Il componete fornisce l'interfaccia d'uso con operazioni di business. 
La classe Composite fornisce le operazioni di business deleganfdo i suoi sotto componenti a realizzarle, fino ad arrivare all'elemento singolo Leaf. 
Guardando questo diagramma non si puo sapere quanto è profonda la ricorsione. 
Composite ha una relazione has-a con component quindi aggregga component.
Come in un file system possiamo aggragere più branch e foglie costituite da direcotry e files nel nostro file system. 
Il generico Component ha la sua operazione di bussiness `Operation()`, gli altri metodi non sono operativi ma serovno per gestire i sotto componenti.
Component è di base una classe Astratta. 

### Observer
Problema: 
- Si vuole gestire un oggetto per cui un cambiamento interno produce delle azioni sull'oggetto stesso che si volgiono configurare dinamicamente 
- Classico contesto della programmazione ad eventi 
**Soluzione:**
- Creare 2 classi: 
	- L'osservato → registra gli Osservatori e li avvisa (registrs gli osservatori e li avvisa)
	- L'osservatore → esegue comportamenti in funzione dell'evento generatorsi sull'Osservato(non è un guardone )
Questo pattern l'abbimao riscontrato ad esempio con i bottoni htlm a cui associavamo un event listener di JS 
Con questa selezione il numero e il tipo degli osservoatori può anche non essere noto a priori. 


### Proxy 
