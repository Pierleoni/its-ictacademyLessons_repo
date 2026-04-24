
# Design Pattern — Ripasso e Nuovi Pattern

Abbiamo già visto cosa sono i [[Lezione 19 - Design Pattern#Design Pattern|Design Pattern]], le loro categorie e alcuni esempi concreti — in particolare il **[[Lezione 19 - Design Pattern#Esempio implementazione del Singleton in Java|Singleton]]**, l'**[[Lezione 19 - Design Pattern#Adapter (Pattern Strutturale)|Adapter]]** e lo **[[Lezione 19 - Design Pattern#Pattern Strategy|Strategy]]**. 
Ora ampliamo il repertorio con quattro nuovi pattern: il **[[#2. Singleton|Singleton]]** (che riprendiamo), il **[[#1. Factory Method|Factory Method]]**, il **Proxy** e l'**[[#4. Observer|Observe]]r** e il **[[#3. Composite ⚠️ Da portare all'esame|Composite]]**.

Vale la pena ricordare una cosa fondamentale prima di procedere: 
- ==i Design Pattern sono uno **strumento di progettazione**, non una soluzione da applicare meccanicamente.== 
Un buon sviluppatore dovrebbe conoscerne almeno i principali — quelli catalogati dal **[[Lezione 19 - Design Pattern#Classificazione dei Pattern del GoF|GoF (Gang of Four)]]** — e soprattutto sapere **quando** usarli. 
==Il modo migliore per ricordare e riconoscere un pattern è legarlo al **tipo di scenario** che risolve.==

>[!note] **Nota:** 
>il pattern **Proxy** non è del tutto nuovo — lo abbiamo già incontrato indirettamente con la **[[Lezione 22 parte 3 - Dependency Injection#Dependency Injection|Dependency Injection]]** di Spring. Quando Spring usa le annotation come [[Lezione 22 parte 3 - Dependency Injection#2. `@Autowired`|`@Autowired`]] per iniettare le dipendenze, crea internamente un oggetto proxy che "avvolge" il bean da iniettare. Ora vedremo il pattern in modo esplicito e formale.

### Le Famiglie dei Design Pattern

I Design Pattern si dividono in famiglie in base al **tipo di problema** che risolvono. Abbiamo già visto:

- **[[Lezione 19 - Design Pattern#GoF Pattern Structural|Pattern Strutturali]]:**
	- ==riguardano la composizione delle classi e degli oggetti.== 
	- Abbiamo visto l'**[[Lezione 19 - Design Pattern#Adapter (Pattern Strutturale)|Adapter]]**.
	- E aggiungeremo il **Composite** e il **Proxy**
- **[[Lezione 19 - Design Pattern#GoF Pattern Behavioral|Pattern Comportamentali]]:** 
	- ==riguardano la comunicazione e il comportamento tra gli oggetti.== 
	- Abbiamo visto lo **[[Lezione 19 - Design Pattern#Pattern Strategy|Strategy]]**.
Oggi aggiungiamo:

- **[[Lezione 19 - Design Pattern#GoF Pattern Creational|Pattern Creazionali]]:** 
	- ==riguardano il **momento della creazione** degli oggetti, fornendo meccanismi per crearli in modo flessibile e disaccoppiato.== 
	- In questa famiglia troviamo il **Singleton** e il **Factory Method**.


## Pattern Creational
### 1. Factory Method

**Il problema che risolve:** ==A volte si ha la necessità di creare un oggetto di cui si conosce **staticamente** l'interfaccia o la superclasse, ma la classe concreta effettiva viene decisa **dinamicamente** a runtime.== 
È una situazione tipica dei framework — e non a caso è un pattern che abbiamo già incontrato indirettamente con Spring.

**La soluzione:** ==L'idea è semplice ma potente: **separare chi crea gli oggetti da chi li usa**.== 
È come con i vestiti — non li produciamo noi, li compriamo e li usiamo. Qualcuno si occupa della fabbricazione, qualcun altro del consumo. Applicato al codice, questo si traduce in:

- **Definire l'interfaccia** degli oggetti da creare — ==chi usa l'oggetto conosce solo l'interfaccia, non la classe concreta==
- **Incapsulare la logica di creazione** i==n una classe **Factory** dedicata, che si occupa di istanziare gli oggetti specifici che implementano quell'interfaccia==
- **Chi usa gli oggetti non deve conoscere il tipo esatto** — ==sa solo che l'oggetto rispetta il contratto dell'interfaccia==

> [!link] **Il collegamento con Spring:**
>  Questo pattern sta alla base di tutti i framework che usano l'[[Lezione 22 parte 3 - Dependency Injection#Inversione di controllo|IoC]] — e Spring ne è l'esempio perfetto. 
>  Le annotation come [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]], `@Service` e `@Repository` fungono da **interfaccia** verso Spring: 
>  - ==dicono al framework quale tipo di oggetto creare, mentre Spring — tramite il suo Container — si occupa di istanziare la classe concreta nel momento giusto.== 
>  - ==Chi usa l'oggetto (ad esempio il Controller che riceve il Service tramite `@Autowired`) non sa e non gli importa come è stato creato — sa solo che rispetta il contratto dell'interfaccia.==

>[!summary] **In sintesi:** 
>il Factory Method ==è il pattern che permette di **disaccoppiare la creazione degli oggetti dal loro utilizzo** — esattamente il principio che abbiamo visto con la Dependency Injection di Spring.==

### Diagramma Factory Method

Il diagramma mostra chiaramente la separazione dei ruoli che abbiamo descritto:
[![Screenshot-2026-03-29-at-15-10-03-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/TwttyFvP/Screenshot-2026-03-29-at-15-10-03-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/FdJy8PRt)

1. ==Il **Consumer** invoca la **Factory** chiedendole di creare un oggetto==
2. ==La **Factory** istanzia un oggetto di **`ConcreteProduct`** — la classe concreta che implementa l'interfaccia `Product`==
3. ==Il **Consumer** ottiene e usa l'oggetto, ma lo vede solo attraverso il tipo astratto **`Product`** — non sa e non gli importa che sia un `ConcreteProduct`==
Il punto chiave è: 
- ==il **Consumer è completamente disaccoppiato dal `ConcreteProduct`** — conosce solo l'interfaccia `Product`.== 
- ==È la Factory a fare da intermediario tra chi crea e chi usa==

> [!done] **Vantaggi del Factory Method**
> 
> 
> 1. **Polimorfismo trasparente:**
> 	-  ==grazie al polimorfismo, ogni oggetto concreto opera secondo la sua "natura" senza che questa debba essere nota a priori a chi lo usa.== 
> 	- ==Il Consumer chiama i metodi dell'interfaccia `Product` e il comportamento corretto viene eseguito automaticamente in base al tipo concreto dell'oggetto.==
> 
> 2. **Facilmente estensibile:**
> 	- ==aggiungere un nuovo tipo di prodotto significa semplicemente creare un nuovo `ConcreteProduct` che implementa `Product` e aggiornare la Factory.== 
> 	- ==Il Consumer non va toccato — non sa nulla della nuova classe concreta.==
> 
> 3. **Incapsulamento delle politiche di creazione:**
> 	- la Factory può implementare logiche di creazione più sofisticate, ad esempio:
> 
> 	- **Un solo oggetto** — è quello che fa Spring con i bean annotati con [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]]: 
> 		- ==crea una sola istanza della classe Controller e la riusa per tutte le richieste==
> 	- **Un pool di oggetti** — è quello che succede tipicamente con le connessioni al database: 
> 		- ==invece di creare e distruggere una connessione per ogni operazione, una classe gestisce un **pool di connessioni** già pronte che vengono "prestate" al [[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]] quando ne ha bisogno e restituite al pool una volta terminate.==

#### Esempio pratico — Factory Method in Java
Supponiamo di dover sviluppare un sistema di creazione di prodotti per un e-commerce.
Vediamo come le classi si mappano sui ruoli del diagramma che abbiamo visto:
1. **L'interfaccia `Prodotto`:**
```java
package designPattern.factoryMethod;

public interface Prodotto {
	public double getCosto();
	public double getPrezzo();
}
```


1. **La classe `TShirt`**
```java
package designPattern.factoryMethod;

public class TShirt implements Prodotto {
	private String taglia;
	private double costo, prezzo;
	public TShirt() {}
	
	public TShirt(double costo, double prezzo, String taglia) {
	this.costo = costo;
	
	this.prezzo = prezzo;
	
	this.taglia = taglia;
	
	}
	@Override
	public double getCosto() {	
		return costo;
	}
	
	@Override
	public double getPrezzo() {	
	return prezzo;
	}

	@Override
	public String toString() {
	
		return "TShirt [taglia=" + taglia + ", costo=" + costo + ", prezzo=" + prezzo + "]";
	}
}
```


2. **La classe `Zaino`**
```java
package designPattern.factoryMethod;

public class Zaino implements Prodotto {
	private double costo, prezzo;
	private String marca;
	public Zaino() {}
	public Zaino(double costo, double prezzo, String marca) {
		this.costo = costo;
		this.prezzo = prezzo;
		this.marca = marca;
	}
	public String getMarca() {
	return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	public void setCosto(double costo) {	
	this.costo = costo;
	}

	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}

	@Override
	
	public double getCosto() {
		return costo;
	}

	@Override
	public double getPrezzo() {
		return prezzo;
	}

	@Override
	public String toString() {
	return "Zaino [costo=" + costo + ", prezzo=" + prezzo + ", marca=" + marca + "]";
	}
}
```

3. **Classe `Libro`**
```java
package designPattern.factoryMethod;

public class Libro implements Prodotto {
	private String titolo;
	private double costo, prezzo;
	public Libro() {}
	public Libro(String titolo, double costo, double prezzo) {
		this.titolo = titolo;
		this.costo = costo;
		this.prezzo = prezzo;
	}
	@Override
	public double getCosto() {
		return costo;
	}
	@Override
	public double getPrezzo() {
		return prezzo;
	}

	@Override
	public String toString() {
	return "Libro [titolo=" + titolo + ", costo=" + costo + ", prezzo=" + prezzo + "]";
	}
}
```

Quindi l'interfaccia  `Prodotto` è il contratto che tutti i prodotti devono rispettare. Il Consumer conosce solo questa interfaccia — non sa nulla delle classi concrete.

**`Zaino`, `TShirt`, `Libro` — i prodotti concreti (`ConcreteProduct`)** Sono le tre implementazioni concrete dell'interfaccia `Prodotto`. 
Ognuna ha i propri campi specifici — `Zaino` ha `marca`, `TShirt` ha `taglia`, `Libro` ha `titolo` — ma tutti espongono `getCosto()` e `getPrezzo()` come richiesto dal contratto. 
Il Consumer non sa quale di questi tre oggetti sta usando — vede solo `Prodotto`.

4. **La classe `FactoryMethod`**
```java
package designPattern.factoryMethod;
public class FactoryProdotto {

// qui imposto la logica creazionale
	@SuppressWarnings("deprecation")
	public static Prodotto getProdotto(String tipoProdotto) {

 if(tipoProdotto.equals("Libro")) {
	 return new Libro("titolo del libro", 10, 15);
}else {
	 return new TShirt(10,25, "M");
 }
}
```

È il cuore del pattern. 
Il metodo `getProdotto()` è statico — ==non si istanzia mai la Factory, la si usa direttamente==. 
==Riceve in input una **stringa** con il nome del tipo di prodotto da creare e restituisce un oggetto di tipo `Prodotto` — il tipo astratto, non quello concreto.== 
Il Consumer non vede mai `new Zaino()` o `new TShirt()` — quella logica è incapsulata qui dentro.
Da notare come in questo caso si usi il modo "classico" di implementare la factory
un `if/else` che in base alla stringa in input crea l'oggetto corretto. Funziona, ma è rigido: 
- ==ogni volta che aggiungi un nuovo `ConcreteProduct` devi modificare la Factory.==

5. **La classe `Consumer`— il consumatore**
```java
package designPattern.factoryMethod;

public class Consumer {

public static void main(String[] args) {
	// chiedo alla factory di produrre un prodotto concreto,senza chiamare il costruttore
	Prodotto product = FactoryProdotto.getProdotto("designPattern.factory.Zaino");
	System.out.println(product);
	System.out.println(product.getPrezzo());
	}
}
```
**Il Consumer chiede alla Factory di creare un prodotto passando il nome della classe come stringa.** 
==Riceve un oggetto di tipo `Prodotto` e lo usa tramite l'interfaccia — chiama `getPrezzo()` senza sapere se sta parlando con uno `Zaino`, una `TShirt` o un `Libro`.==

> [!NOTE] **Nota il disaccoppiamento totale:**
>  ==il Consumer non importa nessuna delle classi concrete — non vede `Zaino`, non vede `TShirt`, non vede `Libro`. Vede solo `Prodotto` e `FactoryProdotto`.== 
>  **Se domani aggiungiamo un nuovo prodotto `Scarpa`, il Consumer non va toccato.**

##### Java Reflection 
Abbiamo visto che il modo "classico" di implementare la Factory con un `if/else` è rigido: 
- ==ogni volta che aggiungi un nuovo `ConcreteProduct` devi modificare la Factory.== 
La **Java Reflection** risolve questo problema permettendo di istanziare una classe **senza conoscerne il nome a compile time**.
Il concetto è semplice: 
- ==normalmente per istanziare una classe scriviamo `new Zaino()` — ma questo significa che il nome della classe deve essere noto a compile time.== 
- ==Con la Reflection invece possiamo fare la "new" di una classe il cui nome lo scopriamo solo a runtime, ad esempio leggendolo da una stringa.==

1. Caricare la classe per nome — `Class.forName()`
```java
Class cl = Class.forName("designPattern.factoryMethod.Zaino");
```
- ==Questo metodo importa dinamicamente la classe il cui nome è contenuto nella stringa==
- ==restituisce un oggetto di tipo `Class` che rappresenta la classe caricata.== 
2. **Istanziare l'oggetto — `newInstance()`**

Ora che abbiamo l'oggetto `cl:Class`
```java
Object obj = cl.newInstance(); 
```
Questo metodo istanzia la classe appena caricata invocando il **costruttore a zero argomenti:**
- ==per questo motivo tutte le classi che vogliamo istanziare tramite Reflection devono avere un costruttore vuoto.== 
- ==`newInstance()` restituisce un `Object` generico, quindi da solo permette di usare solo i metodi di `Object`.==

**Il problema del tipo generico — il cast all'interfaccia:**
- Se `newInstance()` restituisce un `Object`, come facciamo a chiamare `getPrezzo()` e `getCosto()`? La soluzione è il **cast all'interfaccia** `Prodotto`:
```java
String nomeClasse = "designPattern.factoryMethod.Zaino"; // nome della classe da istanziare

Class cl = Class.forName(nomeClasse); // carico la classe per nome
Prodotto p = (Prodotto) cl.newInstance(); // istanzio e casto all'interfaccia

p.getPrezzo(); // ora posso usare i metodi dell'interfaccia
p.getCosto();
```
**Sappiamo che la classe passata implementa `Prodotto` — quindi il cast è sicuro.** 
==A questo punto possiamo chiamare tutti i metodi dell'interfaccia sull'oggetto, indipendentemente da quale classe concreta è stata istanziata.==

**Il risultato nella Factory** Applicando la Reflection alla `FactoryProdotto`, il metodo `getProdotto()` diventa completamente generico:
```java
public static Prodotto getProdotto(String tipoProdotto) {
    try {
        Class classe = Class.forName(tipoProdotto);
        Prodotto ob = (Prodotto) classe.newInstance();
        return ob;
    } catch (ClassNotFoundException e) {
        e.printStackTrace();
    } catch (InstantiationException | IllegalAccessException e) {
        e.printStackTrace();
    }
    return null;
}
```
**Non c'è più nessun `if/else` — la Factory non conosce `Zaino`, `TShirt` o `Libro`.** 
1. ==Riceve una stringa,== 
2. ==carica la classe corrispondente,==
3. ==la istanzia e la restituisce come `Prodotto`.== 
Se domani aggiungiamo `Scarpa` al sistema, la Factory non va toccata — basta passare la stringa `"designPattern.factoryMethod.Scarpa"` e la Reflection pensa al resto.

> [!link] **Nota il collegamento con Spring:**
>  quando Spring legge l'annotation [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]] su una classe, fa esattamente la stessa cosa — ==carica la classe per nome tramite Reflection, la istanzia tramite il costruttore a zero argomenti (ecco perché è obbligatorio!) e la registra nel Container.== 
>  La Java Reflection è il meccanismo che sta sotto a tutta la magia dell'[[Lezione 22 parte 3 - Dependency Injection#Inversione di controllo|IoC]].


### 2. Singleton

**Il problema che risolve:** 
- ==A volte è necessario garantire che esista **una ed una sola istanza** di una certa classe in tutto il sistema.== 
- Pensiamo alla classe `Database` che abbiamo scritto nell'esercizio JDBC: 
	- ==non ha senso creare più istanze di quella classe — ogni istanza aprirebbe una nuova connessione al database, sprecando risorse e rischiando comportamenti inconsistenti.== 
	- ==Lo stesso vale per i Logger, i Config Server e in generale per tutti i componenti che gestiscono risorse condivise.==

**La soluzione:** 
- ==L'idea è impedire che chiunque possa creare liberamente oggetti di quella classe tramite `new`.== 
In Java questo si implementa con tre elementi che lavorano insieme:

1. **Costruttore privato:**
	- ==nessuno può chiamare `new MiaClasse()` dall'esterno.== 
	- ==L'unico modo per ottenere un'istanza è attraverso il metodo dedicato.==
2. **Attributo privato e statico del tipo della classe:**
	- ==è qui che viene conservata l'unica istanza.== 
	- ==Essendo `static`, appartiene alla classe e non a nessun oggetto specifico — esiste una sola volta in memoria per tutta la durata del programma.==
3. **Metodo pubblico e statico che restituisce l'istanza:**
	- ==è l'unico punto di accesso all'istanza.== 
	- ==Se l'istanza non esiste ancora la crea, altrimenti restituisce quella già esistente.==
```java
public class Database {
    // 2. attributo privato e statico — conserva l'unica istanza
    private static Database istanza = null;

    // 1. costruttore privato — nessuno può fare new Database() dall'esterno
    private Database() { }

    // 3. metodo pubblico e statico — unico punto di accesso all'istanza
    public static Database getInstance() {
        if(istanza == null) {
            istanza = new Database(); // crea l'istanza solo la prima volta
        }
        return istanza; // restituisce sempre la stessa istanza
    }
}
```

**Il meccanismo è semplice:** 
- ==la prima volta che qualcuno chiama `Database.getInstance()`, `istanza` è `null` — quindi viene creata.== 
- ==Tutte le volte successive, `istanza` non è più `null` — quindi viene restituita quella già esistente==. 
In questo modo è **fisicamente impossibile** avere più di un'istanza di `Database` in tutto il sistema.

>[!link] **Nota il collegamento con Spring:** 
>i bean annotati con [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]], `@Service` e `@Repository` sono **Singleton per default** — ==Spring crea una sola istanza di ogni bean e la riusa per tutte le richieste.== 
>È esattamente il Singleton pattern applicato su scala architetturale.
#### Diagramma Singleton 
Il diagramma mostra una struttura molto semplice — il Singleton è uno dei pattern più compatti da implementare, ma uno dei più potenti in termini di impatto architetturale.
Per capire questo pattern analizziamo l'immagine del diagramma: 
[![Screenshot-2026-03-27-at-15-11-22-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/q7tB7DZ7/Screenshot-2026-03-27-at-15-11-22-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/McSJP5wk)
1. Abbiamo una classe `Client` che partecipa a un link di associazione con la responsabilità verso la classe `Singleton`

> [!remember] Il Client inteso come colui che ha l'oggetto della classe o interfaccia di cui è responsabile
> Nei casi dei Design Pattern, quando si parla di **Client**, non ci si riferisce a un Client inteso nella accezione canonica del termine(es: il Client nell'architettura **[[Reti di computer#1. Modello Client/Server|Client - Server]]** ), ma alla classe (può essere anche la classe con il `Main` di Java) che implementa l'oggetto della classe o interfaccia da cui parte il Design Pattern

1. La classe `Singleton`: 
	- ==ha un attributo `instance` tipizzato a se stesso==
	- ==un  metodo `Singleton()` senza parametri e senza ritorno==
	- ==E un metodo `getInstance()` che ritorna un oggetto della classe `Singleton`==
	- Difatti questa classe ha un link di associazione che richiama se stessa
Cosa significa tutto ciò? 
==Il **Client** non può creare oggetti della classe direttamente — il costruttore è privato.== 
L'unico modo per ottenere l'istanza è chiamare il metodo statico `getInstance()`.

Il metodo `getInstance()` può avere due comportamenti:

1. **Lazy initialization:**
	- ==l'istanza viene creata **solo alla prima richiesta**.== 
	- ==È il comportamento che abbiamo visto nell'esempio precedente con il controllo `if(istanza == null)`.== 
	- ==Il vantaggio è che se nessuno chiede mai l'istanza, non viene mai creata — risparmio di risorse.== 
	- **È l'approccio più comune.** 
```java
public static Database getInstance() {
    if(istanza == null) {
        istanza = new Database(); // creata solo alla prima chiamata
    }
    return istanza;
}
```

2. **Eager initialization:**
	- ==l'istanza viene creata **al caricamento della classe**, prima ancora che qualcuno la richieda.== 
	- ==È più semplice da implementare e non ha problemi di [[Lezione 18 - MultiThreading#A prova di Thread (Thread safe)|thread safety]], ma crea l'oggetto anche se non verrà mai usato.==
```java
private static Database istanza = new Database(); // creata subito al caricamento

public static Database getInstance() {
    return istanza; // restituisce sempre quella già creata
}
```


> [!info] **La scelta tra i due approcci dipende dal contesto:**
> se l'oggetto è pesante da creare e potrebbe non essere necessario, si preferisce la **lazy initialization**. 
> Se invece l'oggetto è leggero e sarà sicuramente usato, la **eager initialization** è più semplice e sicura.

## Pattern Strutturali

### 3. Composite ⚠️ Da portare all'esame

Il Composite è un pattern molto particolare che risolve una categoria specifica di problemi — ==quelli in cui gli oggetti hanno una **struttura ricorsiva ad albero**.==

Ricordi gli algoritmi ricorsivi che abbiamo visto a inizio corso? 
La ricorsione è la soluzione più elegante per certi problemi — quando un problema può essere scomposto in sotto-problemi della stessa natura. 
==Il Composite è esattamente questo, ma applicato a livello di **progettazione degli oggetti**: è la ricorsione a livello di design.==
**Il problema che risolve:**

Immagina di dover modellare la struttura di un **filesystem**: 
- ==hai cartelle che contengono file, ma anche cartelle che contengono altre cartelle, che a loro volta contengono altri file e altre cartelle.== 
- ==È una struttura ad albero naturalmente ricorsiva.==

Il problema è duplice:

- **Ridondanza nel codice** — ==senza questo pattern dovresti scrivere codice diverso per gestire le foglie (i file) e i nodi compositi (le cartelle), creando duplicazione e complessità inutile==
- **Accesso non uniforme** — ==vorresti poter chiamare `calcola()` o `stampa()` su qualsiasi elemento dell'albero — sia su una singola foglia che su un intero sottoalbero — senza dover sapere a priori su quale dei due stai agendo==
**La soluzione:**

==Si realizza un'**interfaccia generica `Componente`** che modella sia gli elementi singoli (le foglie) che la composizione (i nodi).== 
**L'interfaccia viene implementata da due classi:**

- **`Foglia`(Leaf)** — ==rappresenta gli elementi terminali dell'albero, quelli che non contengono altri elementi (es. un file).==  ^foglia

- **`Composizione` (Composite)** — ==rappresenta i nodi che possono contenere altri nodi.==  ^composizione

- **`Componente` (Componente)**  — ==sia foglie che altre composizioni (es. una cartella).==  ^componente

Il punto chiave è: 
- ==la [[#^composizione|`Composizione`]] contiene una lista di [[#^componente|`Componente`]] — non di [[#^foglia|`Foglia`]] o di `Composizione` specificamente, ma dell'**interfaccia generica**.== 
Questo è ciò che rende il pattern ricorsivo: 
- ==una [[#^composizione|`Composizione`]] può contenere altre [[#^composizione|`Composizione`]], che a loro volta ne contengono altre, formando un albero di profondità arbitraria.==
#### Diagramma del Composite
Per capire meglio questo design pattern analizziamo l'immagine
[![Screenshot-2026-03-27-at-15-25-49-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/Gp7CvF6d/Screenshot-2026-03-27-at-15-25-49-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/R3HyBHMD)
I ruoli dei tre elementi sono:
1. **Classe `Client`:**
	- ==Partecipa a un link di associazione con responsabilità verso l'interfaccia / classe astratta `Component`.==
	- ==La classe client non sa nulla della struttura del design pattern, implementa l'oggetto della classe `Component`== 



2. **Classe astratta/interfaccia [[#^componente|`Component`]]**
	-  ==è l'interfaccia generica, di base una **classe astratta**, che definisce il contratto comune per tutti gli elementi dell'albero.== 
	- ==Dichiara il metodo di business `Operation()` che verrà implementato sia dalle foglie che dalle composizioni.== 
	- ==Gli altri metodi presenti nell'interfaccia — come `add()`, `remove()`, `getChild()` — non sono operativi ma servono a **gestire i sottocomponenti** e hanno senso solo per `Composite`, non per `Leaf`.== 
> [!remember] **Ricorda:**
> `Component` 9 volte su 10 è una [[Lezione 10 - Classi astratte e interfaccie#Classi astratte|classe astratta]], non un [[Lezione 10 - Classi astratte e interfaccie#Le interfacce|interfaccia]]

3. **Classe [[#^composizione|`Composite`]]**
	-  ==è il nodo dell'albero che può contenere altri `Component`.== 
	- ==Implementa `Operation()` **delegando** la chiamata a tutti i suoi sottocomponenti, che a loro volta la delegano ai propri, fino ad arrivare alle foglie.== 
	- ==È una chiamata ricorsiva che scende lungo l'albero fino agli elementi terminali.==
4. **Classe [[#^foglia|`Leaf`]]:** 
	- ==è l'elemento terminale dell'albero, quello che non può contenere altri elementi.== 
	- ==Implementa `Operation()` con la sua logica specifica — è qui che avviene il lavoro concreto.==


**Il diagramma del Composite mostra due relazioni fondamentali che lavorano insieme:**
1. **Relazione is-a:**
	- ==sia [[#^foglia|`Leaf`]] che [[#^composizione|`Composite`]] implementano l'interfaccia [[#^componente|`Component`]].== 
	- Entrambi **sono** un [[#^componente|`Component`]]: 
		- ==questo è ciò che permette al Client di trattarli in modo uniforme senza sapere con quale dei due sta interagendo.==

2. **Relazione has-a:**
	- ==[[#^composizione|`Composite`]] aggrega una collezione di [[#^componente|`Component`]].== 
	- Non aggrega specificamente `Leaf` o altri `Composite`, ma il tipo astratto `Component` — ed è esattamente questa la chiave della ricorsione. 
		- ==Una `Composite` può contenere foglie, altre composizioni, o entrambe, senza limiti di profondità.== 
**Guardando il diagramma non si può sapere quanto è profonda la ricorsione** — ==dipende interamente da come viene costruito l'albero a runtime.==

>[!example] **Analogia con il filesystem:** 
>`Component` è il concetto generico di "elemento del filesystem", `Leaf` è un file, `Composite` è una cartella. 
>Una cartella può contenere file e altre cartelle — esattamente come `Composite` può contenere `Leaf` e altri `Composite`. Quando chiedi la dimensione totale di una cartella, il sistema delega il calcolo a tutti gli elementi contenuti, che a loro volta delegano ai propri, fino ad arrivare ai singoli file che restituiscono la loro dimensione. 
>È il Composite pattern in azione.

#### Esempio Pratico — Composite in Java: Gestione di un Teatro

L'esercizio modella la struttura di un teatro — un esempio perfetto di struttura ad albero ricorsiva: 
- un teatro ha settori, i settori possono contenere altri settori, e alla fine della gerarchia ci sono le zone con i loro posti.

Vediamo come le classi si mappano sui ruoli del pattern:
**`SettoreComponent` — il `Component`**
```java
public abstract class SettoreComponent {
    private int id;

    public void add(SettoreComponent sc) throws LeafException {};
    public boolean removeSettore(SettoreComponent sc) throws LeafException { return false; };
}
```

- ==È la classe astratta che definisce il contratto comune per tutti gli elementi della gerarchia.== 
- **Dichiara i metodi `add()` e `removeSettore()` con implementazioni vuote di default** — ==non astratti, perché la `Leaf` non dovrebbe implementarli ma solo lanciarli come eccezione.== 
- Contiene l'`id` che identifica ogni settore, sia esso un nodo composito o una foglia.

**`SettoreComposite` — il `Composite`**

```java
public class SettoreComposite extends SettoreComponent {
    private List<SettoreComponent> contiene = new ArrayList<>();

    @Override
    public void add(SettoreComponent sc) throws LeafException {
        this.getContiene().add(sc);
    }

    @Override
    public boolean removeSettore(SettoreComponent sc) throws LeafException {
        return this.getContiene().remove(sc);
    }
}
```

- **È il nodo dell'albero** — ==aggrega una `List<SettoreComponent>`, non una lista di `SettoreComposite` o di `Zona` specificamente, ma del tipo astratto `SettoreComponent`.== 
- Questo è il cuore della ricorsione: 
	- ==un `SettoreComposite` può contenere altri `SettoreComposite` o `Zona`, senza limiti di profondità.== 
	- ==I metodi `add()` e `removeSettore()` aggiungono e rimuovono elementi dalla lista.==
`Zona` — la `Leaf`
```java
public class Zona extends SettoreComponent {
    private List<Posto> posti = new ArrayList<>();

    @Override
    public void add(SettoreComponent sc) throws LeafException {
        throw new LeafException("Errore! La zona non può aggiungere zone o posti");
    }

    @Override
    public boolean removeSettore(SettoreComponent sc) throws LeafException {
        throw new LeafException("Errore! La zona non può rimuovere zone o posti");
    }

    public void addPosto(Posto p) { ... }
    public boolean removePosto(Posto p) { ... }
}
```

- ==È la foglia della gerarchia del pattern — non può contenere altri `SettoreComponent`.== 
- ==Quando qualcuno tenta di chiamare `add()` o `removeSettore()` su una `Zona`, viene lanciata una `LeafException` — il meccanismo che impedisce alla foglia di comportarsi come un nodo composito.==
- **`Zona` ha però una propria lista di `Posto` gestita con metodi dedicati `addPosto()` e `removePosto()`** — ==ma questi non fanno parte della gerarchia del Composite, sono una gestione interna della `Zona`.==

`Posto` — oggetto a sé stante
```java
	public class Posto {
	private int numeroPosto;
	private char fila;
	public Posto(int numeroPosto, char fila) {
		this.setNumeroPosto(numeroPosto);
		this.setFila(fila);
	}
	public Posto() {}
	public int getNumeroPosto() {
		return numeroPosto;
	}
	public void setNumeroPosto(int numeroPosto) {
		this.numeroPosto = numeroPosto;
	}
	public char getFila() {
		return fila;
	}

	public void setFila(char fila) {
		this.fila = fila;
	}
	@Override
	public String toString() {
	return "Posto :{ numero posto : " + getNumeroPosto() + ", fila posto : " + getFila() + "}";
	}
}
```


- `Posto` non fa parte della gerarchia del Composite — non estende `SettoreComponent`. 
- ==È un oggetto autonomo che rappresenta il dettaglio più granulare del sistema — un singolo posto in una zona.== 
- La sua gestione è completamente delegata alla `Zona` tramite i suoi metodi `addPosto()` e `removePosto()`.

**`LeafException` — la guardia della Leaf**

```java
public class LeafException extends Exception {
    public LeafException(String msg) { super(msg); }
}
```

È una **[[Lezione 11 - Gestire gli Errori#1. Eccezioni Checked|checked exception]]** custom che viene lanciata ogni volta che si tenta di usare i metodi strutturali del Composite su una `Zona`. 
Essendo checked, ==il compilatore obbliga chi chiama `add()` o `removeSettore()` a gestirla con un `try-catch` — rendendo esplicito nel codice il fatto che queste operazioni possono fallire se invocate su una foglia.==
**`test` — il Client**
```java
public class test {
    public static void main(String[] args) throws LeafException {
        // ...
    }
}
```

Il `main` costruisce la struttura ad albero del teatro passo per passo. Vale la pena seguire il flusso per capire come il pattern prende vita nel codice.

**Prima parte — costruzione del primo settore:**
```java
Posto p = new Posto(1, 'C');
Posto p2 = new Posto(2, 'A');
Posto p3 = new Posto(3, 'D');

Zona z = new Zona(2, new ArrayList<Posto>());
z.addPosto(p);
z.addPosto(p2);
z.addPosto(p3);
```

Si creano tre posti e si aggiungono alla `Zona z` tramite `addPosto()` — il metodo interno della `Zona`, non quello del pattern.
```java
List<SettoreComponent> listaSC = new ArrayList<SettoreComponent>();
SettoreComponent sc = new SettoreComposite(1, listaSC);
sc.add(z);
```
Si crea un `SettoreComposite` e lo si referenzia con una reference di tipo `SettoreComponent` — il tipo astratto. Questo è il disaccoppiamento in azione: 
- ==`sc` non sa di essere un `SettoreComposite`, vede solo l'interfaccia `SettoreComponent`.== 
Si aggiunge poi `z` al settore tramite `sc.add(z)` — il metodo del pattern.
```JAVA
System.out.println(sc.toString());
```
Stampa la struttura del settore con la zona e i suoi posti.

**Seconda parte — aggiunta di un secondo settore:**

```java
Posto p4 = new Posto(4, 'F');
Posto p5 = new Posto(6, 'T');
Posto p6 = new Posto(8, 'Z');

Zona z2 = new Zona(3, new ArrayList<Posto>());
z2.addPosto(p4);  
z2.addPosto(p5);  
z2.addPosto(p6);  
sc.add(z2);
System.out.println(sc.toString());
```

Si crea una seconda zona `z2` e si aggiunge al settore.

>[!info] **Nota importante:** 
>==il Client dichiara `sc` come `SettoreComponent` — non come `SettoreComposite`.== 
>==Questo significa che quando chiama `sc.add(z)` non sa se sta aggiungendo a un `SettoreComposite` o a una `Zona`.== 
>Se `sc` fosse una `Zona`, riceverebbe una `LeafException`. 
>È il polimorfismo del Composite in azione — il Client opera sull'interfaccia senza sapere cosa c'è dietro.
##### La Struttura ad Albero del Teatro

Mettendo tutto insieme, la struttura che si può costruire con questo pattern è:
```css
Teatro (SettoreComposite)
├── Settore A (SettoreComposite)
│   ├── Zona A1 (Zona/Leaf)
│   │   ├── Posto {1, 'A'}
│   │   └── Posto {2, 'A'}
│   └── Zona A2 (Zona/Leaf)
│       └── Posto {1, 'B'}
└── Settore B (SettoreComposite)
    └── Zona B1 (Zona/Leaf)
        └── Posto {1, 'C'}
```
==Il Client può navigare questa struttura chiamando i metodi di `SettoreComponent` senza sapere se sta interagendo con un `SettoreComposite` o con una `Zona` — è il polimorfismo applicato alla ricorsione.==

> [!done] **Conseguenze del Pattern Composite**
>  
> 
> **Accesso uniforme:**
> 	 - ==foglie e nodi compositi vengono trattati in modo uniforme tramite l'interfaccia [[#^componente|`Component`]].== 
> 	 - ==Il Client non deve sapere con quale dei due sta interagendo — chiama sempre gli stessi metodi e il polimorfismo pensa al resto.==
> 
> **Nessuna ripetizione nel diagramma:**  
> 	- ==la struttura ad albero non genera ridondanza nel codice.== 
> 	- ==Non esiste un metodo diverso per gestire le foglie e uno per gestire i nodi — esiste un'unica interfaccia che vale per entrambi.== 
> 	- ==È la soluzione **[[Lezione 19 - Design Pattern#DRY Principle|DRY]]** (Don't Repeat Yourself) applicata alla progettazione.==
> 
> **Profondità dinamica:**
>	- ==la profondità della struttura non è fissa a compile time ma si decide direttamente **al momento della creazione degli oggetti** a runtime.== 
>	- Nell'esercizio del teatro, il Client costruisce l'albero aggiungendo settori e zone liberamente — il pattern non impone nessun limite sulla profondità o sul numero di nodi.
> 

>[!summary] **In sintesi:**
> il Composite risolve elegantemente il problema della ricorsione a livello di design: 
> - ==una sola interfaccia, nessuna ripetizione, profondità arbitraria.== 
>
>È uno dei pattern più potenti e allo stesso tempo più eleganti del catalogo GoF.
## Pattern Comportamentali

### 4. Observer

**Il problema che risolve:** 
==A volte si ha un oggetto il cui **cambiamento interno** deve produrre delle azioni — e si vuole che queste azioni siano configurabili dinamicamente, senza dover modificare l'oggetto stesso ogni volta.== 
È il contesto classico della **programmazione ad eventi**: ==quando succede qualcosa, qualcun altro deve reagire.==

> [!link] **[[Lezione 2 - Il Props Object#^eventHandlerVsEventListeners|Event Listener in JS]]**
> Lo abbiamo già incontrato senza saperlo — quando in JavaScript associavamo un **event listener** a un bottone HTML:
> ```js
> button.addEventListener('click', () => { ... });
> ```
> Il bottone è l'osservato, l'event listener è l'osservatore. Quando il bottone viene cliccato — cambiamento interno — l'event listener reagisce eseguendo il suo comportamento.

**La soluzione:** Si creano due classi con ruoli distinti:

1. **L'Osservato** — ==è l'oggetto che subisce i cambiamenti.== 
	- **Ha la responsabilità di:**

		- ==**Registrare** gli osservatori interessati ai suoi cambiamenti==
		- ==**Avvisarli** quando si verifica un evento==

2. **L'Osservatore:** 
 - ==è l'oggetto che reagisce ai cambiamenti dell'Osservato.== 
 - ==Esegue comportamenti specifici in funzione dell'evento che si è verificato.==

Il vantaggio fondamentale di questa soluzione è che il **numero e il tipo degli osservatori non deve essere noto a priori:**
- ==si possono aggiungere o rimuovere osservatori dinamicamente a runtime, senza toccare il codice dell'osservato.== 
L'osservato sa solo che esistono degli osservatori e che deve avvisarli — non sa quanti sono né cosa fanno.

#### Diagramma dell'Observer
Guardando il diagramma, il pattern si articola su quattro elementi:
[![Screenshot-2026-03-30-at-10-41-21-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png](https://i.postimg.cc/xd5vZJRh/Screenshot-2026-03-30-at-10-41-21-Microsoft-Power-Point-Design-Pattern-ITS-Compatibility-Mode-Des.png)](https://postimg.cc/jWWnwjB4)
1. **`Subject` — l'Osservato astratto:** 
	- ==È la classe astratta che definisce il contratto per tutti gli osservati.== 
	- Dichiara tre metodi fondamentali:

		- `attach(observer: Observer)` — ==registra un nuovo osservatore==
		- `detach(observer: Observer)` — ==rimuove un osservatore==
		- `notify()` — ==avvisa tutti gli osservatori registrati==

2. **`ConcreteSubject` — l'Osservato concreto:**
	
	- ==Estende `Subject` e contiene lo stato che può cambiare — `subjectState: State`.== 
	- ==Espone `getState()` e `setState()` per leggere e modificare lo stato.== 
	- ==Quando lo stato cambia, chiama `notify()` che scatena la reazione di tutti gli osservatori registrati.==

3. **`Observer` — l'Osservatore astratto:**
- **Partecipa a un link di associazione con `Subject`, la quale ha la responsabilità verso questa classe:** 
	- ==Difatti `Subject` nel suo metodo `notify()` invoca il metodo `update()` di `Observer` tramite oggetto `o:Observer`== 
- ==È un'interfaccia che dichiara un solo metodo: `update()`.== 
- ==È il contratto che tutti gli osservatori concreti devono rispettare.==

**`ConcreteObserver` — l'Osservatore concreto:**
- **Implementa `Observer` e specializza il metodo `update()`** ==con il comportamento specifico da eseguire quando viene notificato.== 
- Partecipa a un link di associazione con responsabilità verso `ConcreteSubject`: 
	- ==per poterne leggere lo stato aggiornato tramite `getState()`.==


> [!NOTE] Il cuore del pattern è il metodo `notify()`, che internamente fa:
>```java
> >void notify() {
   > for(Observer o : observers) {
  >      o.update(); // avvisa ogni osservatore registrato
  >  }
>}
>```
> ==Quando il `ConcreteSubject` cambia stato, chiama `notify()` che itera su tutti gli osservatori registrati e chiama `update()` su ognuno.== 
> Ogni `ConcreteObserver` reagisce al cambiamento eseguendo il suo comportamento specifico — ==che può includere leggere il nuovo stato dell'osservato tramite `getState()` e modificarsi di conseguenza.==
>

> [!ticket] Il punto chiave è che il `Subject` non sa nulla dei `ConcreteObserver` — conosce solo l'interfaccia `Observer`. 
> ==Questo significa che si possono aggiungere nuovi tipi di osservatori senza mai toccare il codice del `Subject` — esattamente come in JavaScript si possono aggiungere più event listener allo stesso bottone senza modificare il bottone stesso.==
> 




> [!done] **Conseguenze del Pattern Observer**
>  
> 
> **L'Observer è esterno e indipendente:** 
> - ==l'osservatore non è parte integrante del `Subject` ma un componente esterno che può essere configurato, aggiunto o rimosso dinamicamente senza toccare il codice dell'osservato.== 
> - È esattamente il principio di **Single Responsibility**: 
> 	- ==il `Subject` si occupa di gestire il proprio stato, gli `Observer` si occupano di reagire ai cambiamenti.==
> 
> **Un Observer può osservare più Subject:** 
> - ==uno stesso osservatore può essere registrato su più oggetti osservati contemporaneamente==. 
> - Ad esempio un logger che registra i cambiamenti di stato potrebbe essere registrato su tutti i microservizi del sistema.
> 
> **L'Observer è autorizzato ad agire sul Subject:**
> -  ==l'osservatore non si limita a leggere lo stato dell'osservato tramite `getState()` — se necessario può anche modificarlo tramite `setState()`.== 
> - ==Il `Subject` autorizza implicitamente questa possibilità nel momento in cui registra l'osservatore.==



> [!tldr] **Observer vs Proxy — Una Distinzione Importante**
>  
> 
> L'Observer può sembrare simile al **Proxy** — entrambi coinvolgono un oggetto che "si mette in mezzo" rispetto a un altro. 
> La differenza fondamentale però è:
> 
> - Nel **Proxy:**
> 	- ==il soggetto filtrato **non sa nulla** del proxy che lo avvolge.== 
> 	- ==Il proxy intercetta le chiamate all'insaputa dell'oggetto originale.==
> - Nell'**Observer** — l'osservato **sa dell'osservatore**: 
> 	- ==è lui stesso a registrarlo tramite `attach()` e ad avvisarlo tramite `notify()`.== 
> 	- ==Non c'è nulla di nascosto — è una relazione esplicita e bidirezionale.==

>[!summary] In sintesi: il Proxy è trasparente all'oggetto originale, l'Observer è una relazione consapevole e dichiarata tra osservato e osservatore.


## Proxy 


### Il problema che risolve:

==A volte si ha un oggetto che **non può o non deve essere accessibile direttamente** dal client.==  
Le ragioni possono essere molteplici:

- **Sicurezza** — l'oggetto contiene dati sensibili che solo alcuni client possono vedere
    
- **Controllo accesso** — bisogna verificare chi fa cosa e quando
    
- **Lazy loading** — l'oggetto è "pesante" da creare e va inizializzato solo quando serve davvero
    
- **Logging** — si vuole tracciare ogni operazione eseguita sull'oggetto
    
- **Caching** — si vogliono memorizzare risultati di operazioni costose
    

In tutti questi casi, ==il problema comune è: **come si fa ad aggiungere questo comportamento extra senza modificare l'oggetto originale?** ==

>[!example] **Esempio quotidiano** 
>Pensiamo al bancomat: Non inseriamo la mano direttamente nel caveau della banca per prendere i soldi. 
>Si inserisce la carta, si digita il PIN, e il **bancomat fa da proxy** — verifica che il cliente sia autorizzato, registra l'operazione, e solo allora consente l'accesso ai soldi. 
>Tu interagisci con il bancomat (il proxy), non con il caveau (l'oggetto reale).


### La soluzione:

==Si crea una classe **Proxy** che si mette **tra il client e l'oggetto reale** (chiamato **Target**).==

Il punto fondamentale è che ==**sia il Proxy che il Target devono implementare la stessa interfaccia**.==

Perché? ==Così il client **non si accorge** di stare parlando con un proxy invece che con l'oggetto reale.==  
Il proxy si "spaccia" per il target agli occhi del client — ma prima di passare la richiesta al target, **può fare operazioni extra** come controlli, logging, caching, ecc.

> [!tip] **L'inganno trasparente**  
> Il client chiama un metodo sull'interfaccia. 
> Pensando di parlare con il Target, in realtà parla con il Proxy. Il Proxy fa le sue verifiche, poi (se tutto ok) chiama lo stesso metodo sul vero Target. 
> Il client non sa nulla di tutto questo.


#### Diagramma del Proxy
```text
┌─────────────────────────────────────────────────────────┐
│                      <<interface>>                       │
│                      `Subject`                           │
│─────────────────────────────────────────────────────────│
│              +request()                                  │
└─────────────────────────────────────────────────────────┘
         △                                    △
         │                                    │
         │                                    │
┌─────────────────┐                  ┌─────────────────┐
│    `Proxy`      │                  │   `RealSubject` │
│─────────────────│                  │─────────────────│
│ -realSubject    │─────────────────►│ +request()      │
│─────────────────│                  │                 │
│ +request()      │                  │                 │
└─────────────────┘                  └─────────────────┘
```
Il diagramma mostra quattro elementi:

1. **`Subject` — l'interfaccia comune:**
    
    - ==È l'interfaccia che sia il Proxy che il Target devono implementare.==
        
    - Dichiara i metodi che il client può chiamare (es. `request()`).
        
    - ==È ciò che permette al Proxy di "spacciarsi" per il Target.==
        
2. **`RealSubject` — il Target, l'oggetto reale:**
    
    - ==È l'oggetto che fa il lavoro vero.==
        
    - Contiene la logica di business — la cosa che il client vuole veramente ottenere.
        
    - ==Non sa nulla del Proxy che eventualmente lo avvolge.==
        
3. **`Proxy` — il filtro/intermediario:**
    
    - ==Mantiene un riferimento al `RealSubject`.==
        
    - ==Implementa la stessa interfaccia `Subject`.==
        
    - Nel suo metodo `request()`:
        
        1. Fa le operazioni **pre-request** (controllo accesso, logging, caching, ecc.)
            
        2. Se tutto ok, chiama `realSubject.request()`
            
        3. Fa le operazioni **post-request** (se necessario)
            
    - ==Può anche creare il `RealSubject` solo quando serve (lazy loading).==
        
4. **`Client` — chi usa l'oggetto:**
    
    - ==Interagisce solo con l'interfaccia `Subject`.==
        
    - **Non sa** se sta parlando con un Proxy o con il RealSubject.
        
    - ==Questa ignoranza è voluta — è ciò che rende il pattern trasparente.==

>[!ticket] **Il punto chiave è la trasparenza**  
>==Il `RealSubject` non sa nulla del `Proxy` che eventualmente lo avvolge.==  
>==Il `Proxy` conosce il `RealSubject` e lo chiama dopo aver fatto i suoi controlli.==  
>==Il `Client` interagisce solo con l'interfaccia `Subject` — quindi può usare indifferentemente un Proxy o un RealSubject senza modificare il suo codice.==

**Questo significa che si possono aggiungere nuove funzionalità (sicurezza, logging, caching, lazy loading) senza toccare né il client né l'oggetto reale.**


##### Conseguenze del Pattern Proxy

> [!done] **Separazione delle responsabilità**
> 
> - ==Il `RealSubject` si occupa solo della sua logica di business (quello che deve fare).==
>     
> - ==Il `Proxy` si occupa delle "preoccupazioni trasversali" (controllo accessi, logging, caching, lazy loading).==
>     
> - ==È il principio di **Single Responsibility** applicato a livello di pattern.==
>     

> [!done] **Trasparenza per il client**
> 
> - ==Il client non sa se sta usando un Proxy o il RealSubject.==
>     
> - ==Questo significa che si può introdurre un Proxy senza modificare il codice del client.==
>     
> - ==Si può anche rimuovere il Proxy (tornare al RealSubject diretto) senza conseguenze.==
>     

> [!done] **Controllo sul ciclo di vita**
> 
> - ==Il Proxy può decidere **quando** creare il RealSubject (lazy loading).==
>     
> - ==Il Proxy può decidere **se** chiamare il RealSubject (in base ai controlli).==
>     
> - ==Il Proxy può decidere **quante volte** chiamarlo (caching).==
>     

> [!warning] **Possibile svantaggio: complessità aggiuntiva**
> 
> - ==Il Proxy introduce un ulteriore livello di indirezione.==
>     
> - ==Se usato ovunque senza criterio, può rendere il sistema più difficile da comprendere e debuggare.==

>[!note] **Proxy in Spring** 
>==Spring usa il pattern Proxy internamente per implementare l'[[Lezione 22 parte 4 - AOP(Aspect oriented Programming)|AOP]].== 
>Quando annoti un metodo con `@Transactional` o un [[Lezione 22 parte 4 - AOP(Aspect oriented Programming)#Aspect|Aspect]] con [[Lezione 22 parte 4 - AOP(Aspect oriented Programming)#^c16a37|`@Around`]], Spring crea automaticamente un proxy dell'oggetto target. 
>Il client (es. un [[Lezione 22 parte 2 - Spring framework#La Classe Controller|Controller]]) chiama il metodo pensando di parlare con il [[Lezione 22 parte 2 - Spring framework#Il Service|Service]] reale — in realtà parla con il proxy generato da Spring, che applica il comportamento trasversale (logging, transazione, ecc.) prima di delegare al metodo vero.

> [!tldr] **Proxy vs Observer — La differenza fondamentale**
> 
> Entrambi coinvolgono un oggetto che si relaziona con un altro. Ma la direzione della consapevolezza è opposta:
> 
> - **Nel Proxy:**
>     
>     - ==Il `RealSubject` (l'oggetto reale) **non sa nulla** del Proxy che lo avvolge.==
>         
>     - ==Il Proxy è trasparente al Target.==
>         
>     - ==L'utente del Proxy (il client) non sa di stare usando un Proxy.==
>         
>     - **La trasparenza è totale in entrambe le direzioni.**
>         
> - **Nell'Observer:**
>     
>     - ==L'osservato **sa dell'osservatore** — lo registra esplicitamente con `attach()`.==
>         
>     - ==L'osservatore sa dell'osservato — lo interroga con `getState()`.==
>         
>     - **La relazione è consapevole e bidirezionale.**
>         
> 
> ||**Proxy**|**Observer**|
> |---|---|---|
> |Il soggetto originale sa dell'altro?|❌ No|✅ Sì (attacca)|
> |L'altro sa del soggetto originale?|✅ Sì (riferimento)|✅ Sì (getState)|
> |Chi si mette in mezzo?|Proxy|Nessuno — è una collaborazione|
> |Trasparenza|Totale (nessuno sa)|Esplicita (tutti sanno)|



> [!summary] **In sintesi:** 
> il Proxy è: 
> - ==un **filtro invisibile** che si inserisce tra client e oggetto reale senza che nessuno dei due lo sappia.== 
> L'Observer è: 
>- ==una **relazione consapevole** dove osservato e osservatore collaborano esplicitamente.== 
>>[!remember] **Ricorda:**
>>Il Proxy risponde alla domanda **_"come aggiungo controlli senza modificare nulla?"_.** 
>>L'Observer risponde alla domanda **_"come faccio reagire altri oggetti ai miei cambiamenti?"_.**

#### Il ruolo della Factory

==Questo pattern sottintende l'uso combinato di una **Factory**.==

Perché? Perché il client **non deve sapere** se sta ricevendo un Proxy o un `RealSubject`. 
==Deve ricevere sempre un oggetto che implementa `Subject`, senza dover decidere lui quale dei due creare.==

**Il flusso è questo:**

1. ==Il **Client** chiede alla **Factory** un oggetto di tipo `Subject`==
    
2. ==La **Factory** decide se restituire un `Proxy` o un `RealSubject` (spesso restituisce il Proxy) ==
    
3. ==Il **Client** riceve quello che crede sia un `RealSubject`, ma in realtà è un `Proxy`==
    
4. ==Il **Proxy** attua le sue politiche di filtro (controlli, logging, caching...)==
    
5. ==Se necessario, il **Proxy** invoca il `RealSubject`==
```text
┌─────────┐      richiede Subject       ┌─────────┐
│ Client  │ ─────────────────────────► │ Factory │
└─────────┘                             └─────────┘
     │                                        │
     │                                 restituisce
     │                                   Proxy
     │                                        │
     │    ┌──────────────────────────────────┘
     │    ▼
     │  ┌───────┐
     │  │ Proxy │
     │  └───────┘
     │      │
     │      │ 1. politiche di filtro
     │      │ 2. se ok, invoca
     │      ▼
     │  ┌────────────┐
     │  │ RealSubject│
     │  └────────────┘
     │
     └──────────────────────────────────────────►
                          usa
```

>[!tip] **Perché la Factory è fondamentale**  
>Senza Factory, il Client dovrebbe decidere da solo se creare un Proxy o un `RealSubject` — il che significherebbe che il Client **sa dell'esistenza del Proxy**, rompendo la trasparenza che il pattern vuole ottenere.
>
>Con la Factory, il Client chiede semplicemente "dammi un `Subject`" — e la Factory decide internamente se avvolgerlo in un Proxy o meno. Il Client non sa (e non gli interessa) cosa gli è stato dato.

