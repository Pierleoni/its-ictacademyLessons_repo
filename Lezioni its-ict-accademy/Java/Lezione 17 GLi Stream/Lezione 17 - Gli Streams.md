
# Introduzione 
Le collection rappresetnato la libreria classica per raggruppare e rappresentare dati, ma per eseguire operazioni sui dati prevedono un approccio programmatico 
```java
List<Dish> lowCaloriaDishes = new ArrayList<Dish>(); 
for (Dish d:menu){
	if(d.getCalories()<400){
		lowcaloriesDishes.add(d); 
	}
}
```


I nuovi stream di Java 8 offorno uno strumento alternativo per compiere le più comuni operazioni sui dati ma con un approccio dichiariativo che ricorda la sintassi SQL 
```
select *
From Dish 
Where calorie <400
```

Java 8 introduce nel linguaggio (Java SE) il concetto di programmazione dichiarativa.
La programmazione dichiarativa è alla base degli EJB e dei framework 


Gli streams son una nuova libreria per la manipolazione e la gestione dei dati in forma dichiariativa da usare con o in alternativa alle collections 

Esempio: 
Dato un menu (collection di piatti), si volgiono ecuperare i nomi dei piatti meno calocirici per numero di calorie. 
Vediamo la differenza tra java7 e java8
```
List<Dish> lowCaloriaDishes = new ArrayList<>(); 
for (Dish d: menu){
	if(d.getCaloriers()<400){
		lowCaloriesDishes.add(d); 
	}
}

Collection
```

COn java 8 : usando i nuovi Streams e le lambda ecpression
```
List<String> lowCaloriaDishesNames = 
	menu.stream()
	.filter(d->d.getCalories()<400)
	.sorted(d1,d2)->Integer.compare()
```


Schema delle pipeline delle operazioni dal precendente esempio: 

Possiamo dire che gli stream sono: 
- Dichiarativi →usano le espressioni lambda 
- Componibili → si possono eseguire in ordine arbitrario 
- Parallelizzabili → prevedono di impostare (opzionalmente) una gestione multithreading
Il flusso è: 
Un dato in ingresso(la collection `menu`)
Varie operazioni intermedie 
	- filter
	- sorted
	- lamda

> [!info] QUeste operazioni intemredie possono essere quante ce ne pare e in un rodine che ci pare 

- Una e una sola operazione finale 

```
import java.util.stream.Collectors
import java.util.List; 
List<Sring> threeHighCaloriesDishesNames = 
	menu.stream()
	.filter(d->d.getCalories()<300)
	.map(d->d.getName())
	.limit(3)
	.collect(Collect.toList)
```

Uno stream è un oggetto che rappresenta una sequenza di dati tratti da una sorgente su cui si intende fare delle operazioni. 
Seqeunenza di dati → come per le collections, anche gli stream vengono definiti attraverso una interfaccia che ne definisce il comportamento generale. 
- La differenza fondamentale tra le collections e streams è che le collezioni definiscono strutture dati 

### Collection vs Stream 
Una collection ed uno stream sono concettualemnte cose diverse 
Una collection è una struttura dati che 
- Richiede la presenza di tutti i dati 


### L'archittettura 
L'interfaccia `java.util.Collection` introduce due nuovi metodi per la creazione a partire da una collezzione di dati: 
```
defualt Stream<E> stream(); //single thread
defualt Stream<E> parallelStream()// multiThread
```

Il comportamento di defualt di questi metodi è ritornare uno stream come semplice seuqneza della collezione chiamante 
- È posibile comunque creare uno Stream con i metodi statici della classe Stream: 
```java
static <T> Stream<T> empty() //→ costruisce uno stream nuovo

static <T> Stream<T> of (T t) //costruisce uno stream con un singolo oggetto T

static <T> Stream<T> of (T... values) // costruisce uno stream con 0... n oggetti di tipo T 
```


> [!NOTE] Per metodi di defualt di un interfaccia sono i metodi conreti dell'interfaccia stessa (da Java8 in poi)


### Tipi operazioni
Le operazioni su uno stream sono di due tipi
- Operazioni intermedie: filtraggio, raggrupaemento, limitazione e selezione
- Operazioni finale: stocaggio, ricerca, riduzione 
Le prime




#### Operazioni finale: ricerca
Le ricerche piu raffinate si realizzaono con `xxxFind()`
Le operazioni precedenti sono utili ma ritornano un boolean
Se dobbiamo ottenere uno o più che corrispondono ai criteri impostati, possiamo usare i metodi xxxFind()
I metodi sono: 
`Optional<T> findFirst()`→ ritorna un elemento (il primo) che corrisponde al criterio di ricerca impostato. Quindi ha un comportamento deterministico 
`Oprional<T> findAny`→ 


