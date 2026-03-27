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
