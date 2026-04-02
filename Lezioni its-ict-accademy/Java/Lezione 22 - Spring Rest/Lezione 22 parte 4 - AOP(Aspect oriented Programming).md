
# AOP – Introduzione

Durante il modulo di Java abbiamo esplorato a fondo l'**[[Oggetti e Classi#Approccio orientato agli oggetti (OOP)|OOP (Object-Oriented Programming)]]**: [[Oggetti e Classi#La classe|classi]], [[Oggetti e Classi#Natura degli oggetti|oggetti]], [[Ereditarietà e polimorfismo#Concetto di ereditarietà|ereditarietà]], [[Lezione 8 - L'incapsulamento#Incapsulamento e consistenza degli oggetti|incapsulamento]]. 
Con Spring abbiamo poi visto come questi concetti si traducono in un'architettura a strati — [[Lezione 22 parte 2 - Spring framework#La Classe Controller|Controller]], [[Lezione 22 parte 2 - Spring framework#Il Service|Service]], [[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]] — tenuta insieme dalla [[Lezione 22 parte 3 - Dependency Injection#Dependency Injection|Dependency Injection]].

L'**AOP (Aspect-Oriented Programming):**
- ==non è un paradigma alternativo all'OOP, ma una sua **estensione**.== 
**Nasce dall'osservazione che, nonostante i grandi vantaggi dell'OOP, nel tempo sono emerse alcune carenze strutturali.**

Il problema centrale è il seguente: certi comportamenti — come il logging, la gestione delle eccezioni, il controllo degli accessi o il tracciamento delle statistiche — tendono a **ripetersi trasversalmente** in molte classi e metodi. 
In OOP, classe e oggetto non sono strumenti adatti a modellare questo tipo di logica "orizzontale": 
- ==il rischio è duplicare codice ovunque, violando il principio di responsabilità singola.==

L'AOP risolve questo problema introducendo il concetto di **aspetto (aspect)**: 
- ==un modulo separato che racchiude la logica trasversale e si "aggancia" automaticamente ai punti del codice che ci interessano, senza che le classi coinvolte ne siano consapevoli.==

> [!done] **I benefici pratici sono immediati:**
> 
> 
> - **Progettazione** più pulita, perché ogni classe mantiene una sola responsabilità
> - **Sviluppo** più rapido, perché la logica trasversale si scrive una volta sola
> - **Manutenzione** semplificata, perché modificare un comportamento trasversale significa toccare un solo punto
> - **Evoluzione** più sicura, perché aggiungere nuovi aspetti non richiede di modificare il codice esistente

### Cos'è un Aspetto

Un **aspetto** è: 
- ==un modulo che incapsula un **comportamento trasversale**, detto in inglese _cross-cutting concern_:== 
	- ==una funzionalità che non appartiene logicamente a una singola classe, attraversa più componenti del sistema e si applica in punti diversi dell'esecuzione del programma.==

Un aspetto descrive **cosa fare** e **in quali condizioni farlo**, ma non stabilisce il _dove_ nel codice sorgente — è il framework AOP a occuparsi di questo.


### Il problema: il logging come esempio concreto

Pensa a tutto il codice scritto finora: ogni volta che volevamo monitorare l'esecuzione di un metodo, aggiungevamo una stampa o usavamo la classe `Logger`. 
Quella logica di tracciamento era **trasversale** — ==si ripeteva in classi diverse, senza appartenere davvero a nessuna di esse.== 
**Il risultato era codice "sporcato" da responsabilità che non gli competevano.**

L'OOP tradizionale suggerirebbe di creare una classe dedicata al logging. Ma a quel punto sorge il problema: **come fa quella classe a sapere quando e dove intervenire?** 
Le altre classi dovrebbero conoscerla e chiamarla esplicitamente, creando accoppiamento e di nuovo duplicazione.

L'AOP risolve questo nodo alla radice: 
- ==l'aspetto viene definito una volta sola, e il framework lo **intreccia automaticamente** con il codice nei punti stabiliti, senza che le classi coinvolte ne sappiano nulla.==


#### Perché l'OOP non basta

L'OOP si fonda su un principio chiave: 
- ==**ogni comportamento appartiene a un oggetto**.== 
È proprio qui che emerge il limite:

- I _cross-cutting concern_ — ==come il logging, la gestione della sicurezza o il tracciamento delle statistiche — **non hanno un oggetto naturale di riferimento**.== 
	- ==Non appartengono a una classe in particolare, ma riguardano potenzialmente tutte le classi del sistema.==

> [!example] **Riprendendo l'esempio del logging:**
>  ==non è responsabilità del `Controller` loggare, né del `Service`, né del `DAO`. Eppure tutti ne hanno bisogno.== 
>  **In OOP puro, l'unica soluzione sarebbe creare una classe `Logger` e richiamarla esplicitamente ovunque** — ==ma questo significa accoppiamento, ripetizione e codice sporcato di logica che non compete a nessuno strato.==

L'AOP nasce esattamente per rispondere a questa carenza: 
- ==offre un modo per modellare i concern trasversali **fuori** dalle classi di business, mantenendo ogni componente focalizzato sulla propria responsabilità.==
[![Screenshot-2026-04-01-at-16-55-19-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/KjByDBhF/Screenshot-2026-04-01-at-16-55-19-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/sGj8VB20)

### Separation of Concerns

Il principio di **Separation of Concerns** afferma che:
- ==è auspicabile separare le diverse questioni — i diversi _concern_ — che caratterizzano un sistema, in modo da poterle analizzare e gestire singolarmente.==

Detto questo, nella realtà gli aspetti sono spesso **interconnessi e intrecciati**: 
- ==non possono essere valutati in completo isolamento, perché agiscono sulle stesse componenti del sistema.== 
==È proprio da questa tensione — separare ma anche incrociare — che nasce l'esigenza della programmazione orientata agli aspetti==.

In pratica, il modello AOP introduce due categorie di classi:

1. Le **classi target**:  ^classiTarget
	- ==sono le classi di business, come i [[Lezione 22 parte 2 - Spring framework#Il Service|`Service`]].== 
	- ==Rappresentano la logica principale del sistema e si sviluppano **orizzontalmente** nell'architettura.==    
2. Le **classi aspetto**:   ^classiAspetto
	- ==modellano i concern trasversali — logging, statistiche, sicurezza — e si sviluppano **verticalmente**, incrociando più classi target contemporaneamente.==   

Questa separazione permette di: 
- ==mantenere ogni classe target focalizzata sulla propria responsabilità,== 
- ==mentre gli aspetti vengono applicati trasversalmente dal framework, senza che i target ne siano consapevoli.== 

> [!ticket] ==Si programmano aspetti **SOLO** per gestire questo tipo di situazioni trasversali== — **NON per logica di business ordinaria**.
> 


[![Screenshot-2026-04-02-at-11-12-48-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png|343x322](https://i.postimg.cc/d35GfDy6/Screenshot-2026-04-02-at-11-12-48-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/64G72Wz4)

####  Cross-Cutting Concerns

I **cross-cutting concern** sono: 
- ==quelle caratteristiche funzionali di un applicativo che attraversano trasversalmente la logica di business.== 
Non appartengono a un singolo strato o a una singola classe, ma riguardano l'intero sistema.

> [!example] **Servizi Infrastrutturali: esempi classici**
>  1. **il logging,** 
>  2. **la sicurezza,** 
>  3. **la gestione della concorrenza,** 
>  4. **il tracciamento delle statistiche.** 
> ==Nessuno di questi è logica di business — non calcolano nulla, non gestiscono dati del dominio — eppure sono necessari ovunque.==
> 

Affrontare questi concern con l'OOP classico porta inevitabilmente a due problemi:

> [!failure]
> - **Duplicazione del codice**: 
> 	- ==la stessa logica — ad esempio una chiamata al Logger — viene riscritta in ogni classe che ne ha bisogno.==
> - **Frammentazione del codice**: 
> 	- ==la logica trasversale si sparpaglia in punti diversi del sistema, rendendo difficile trovarla, modificarla o rimuoverla.==
> 

In entrambi i casi il risultato è lo stesso: 
- ==le classi di business vengono inquinate da responsabilità che non gli competono, violando il Single Responsibility Principle che abbiamo già incontrato studiando i principi SOLID.==

L'AOP risolve entrambi i problemi raccogliendo ogni concern trasversale in un unico aspetto, applicato automaticamente nei punti stabiliti.
>[!faq] **I Principi SOLID** 
>I principi **SOLID** sono 5 linee guida fondamentali della progettazione object-oriented, formulate da Robert C. Martin. 
>==Il loro obiettivo è rendere il software più manutenibile, estensibile e leggibile nel tempo.==
>
>Le cinque lettere corrispondono a:
>
>1. **S** – _Single Responsibility Principle_: ==una classe deve avere una sola ragione per cambiare, ovvero una sola responsabilità.==
>>[!example]- **Immaginiamo di avere una classe `OperazioneService`:**
>> calcola le operazioni algebriche. 
>> Se aggiungessimo anche il logging e il conteggio delle statistiche dentro di lei, avrebbe tre responsabilità distinte. 
>> Ogni responsabilità va in una classe separata.
>> 
>>>[!failure] **Esempio errato**
>>>Aggiungiamo quindi, oltre al calcola della somma algebrica, anche il conteggio delle statistiche.
>>> ```java
>>> // Sbagliato: troppe responsabilità
>>>  @Service 
>>>  public class OperazioneService { 
>>> 	public int somma(int a, int b) { 
>>> 		System.out.println("Chiamata a somma"); // logging 
>>> 		contatoreSomma++; // statistica return 
>>> 		a + b; // calcolo 
>>> 	} 
>>> }
>>>```
>>>Questo viola la _Single Responsibility Principle_: aggiungiamo troppe responsabilità ad un unica classe.
>>>
>>
>>>[!done] **Esempio corretto:**
>>>Suddividiamo le classi in base alla loro responsabilità
>>>1. **Classe Service `OperazioneService`**
>>>
>>>```java
>>>// ✅ Corretto: una sola responsabilità per classe 
>>>@Service 
>>>public class OperazioneService { 
>>>	public int somma(int a, int b) { 
>>>		return a + b; 
>>>		}
>>> }
>>>```
>>>
>>>
>>>Essendo questa una classe [[Lezione 22 parte 2 - Spring framework#Il Service|Service]], questo ha perfettamente senso, perché: 
>>>- Deve contenere solo la logica di business ad alto livello
>>>- Questa operazione non è nè coordinamento ([[Lezione 22 parte 2 - Spring framework#La Classe Controller|Controller]]) né, tantomeno, accesso ai dati ([[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]]). 
>>>Quindi è giusto che la somma algebrica stia dentro una classe di servizio.
>>>
>>>2.**Classe Bean `StatisticheComponent`** 
>>>
>>>```java
>>> @Component 
>>> public class StatisticheComponent { 
>>>	 private int contatoreSomma = 0; 
>>>	 public void incrementaSomma() { 
>>>		 contatoreSomma++; 
>>>	 } 
>>>	 public int getContatoreSomma() { 
>>>		 return contatoreSomma; 
>>>	 } 
>>> }
>>>
>>>```
>>Notare come questa classe è annotata con [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]]. 
>>Questa classe contiene, difatti, il contatore della somma e i metodi per incrementare il contatore e ritornarlo.
>> 
>2. **O** – _[[Ereditarietà e polimorfismo#^openClose|Open/Closed Principle]]_: ==una classe deve essere aperta all'estensione ma chiusa alla modifica.==
>>[!example]- **Esempio: Classe `Sconto`**
>>Supponiamo di avere una classe `Sconto` che implementa un blocco `if/else` per ogni tipo di sconto, quindi si modifica la classe ogni volta che si aggiunge un nuovo tipo di sconto. 
>>In questo caso è meglio definire un'[[Lezione 10 - Classi astratte e interfaccie#Le interfacce|interfaccia]] e creare sotto classi concrete che rappresentano una nuova implementazione per ogni tipo di sconto — senza toccare il codice esistente.
>>>[!failure] **Esempio errato**
>>```java
>>>public class Sconto { 
>>>	public double calcola(String tipo, double prezzo) { 
>>>		if (tipo.equals("studente")) { 
>>>			return prezzo * 0.80; 
>>>		} else if (tipo.equals("anziano")) { 
>>>			return prezzo * 0.75; 
>>>		} 
>>>		return prezzo; 
>>>	} 
>>>}
>>>``` 
>>> Questo esempio viola il principio open/closed, poiché ogni volta che si vuole aggiungere un nuovo tipo di sconto di deve modificare il codice del metodo `calcola()`.
>>
>>>[!done] **Esempio Corretto:**
>>>```java
>>>// ✅ Corretto: aperta all'estensione, chiusa alla modifica public interface Sconto { 
>>>	double calcola(double prezzo); 
>>>} 
>>>public class ScontoStudente implements Sconto { 
>>>	public double calcola(double prezzo) { 
>>>		return prezzo * 0.80; 
>>>	} 
>>>} 
>>>public class ScontoAnziano implements Sconto { 
>>>	public double calcola(double prezzo) { 
>>>	return prezzo * 0.75; 
>>>	} 
>>>}
>>>```
>>> Questo esempio segue alla perfezione questo principio: le sottoclassi implementano l'interfaccia sconto la quale dichiara un metodo astratto comune per ogni sotto classe, senza che si debba andare a cambiare il codice dell'interfaccia poiché essa è perfettamente estendibile alle sue sotto classi. 
>>> Quindi per ogni sotto tipologia di sconto verrà specializzato il metodo `calcola()` senza però che questo venga modificato e cambiato ogni volta.
>
>3. **L** – _Liskov Substitution Principle_: ==una sottoclasse deve poter sostituire la sua superclasse senza alterare il comportamento del programma.==
>>[!example]- **Esempio: La classe `Quadrato` che estende la super classe `Rettangolo`**
>>Ipotizziamo di avere due classi: una sotto classe `Quadrato` che estende `Rettangolo`, ma sovrascrive i setter per mantenere i lati uguali. 
>>Chi usa un `Rettangolo` non si aspetta questo comportamento — la sottoclasse rompe il contratto della superclasse.
>>>[!failure] **Esempio Errato**
>>>```java
>>>// ❌ Sbagliato: Quadrato rompe il contratto di Rettangolo public class Rettangolo { 
>>>	protected int larghezza; 
>>>	protected int altezza; 
>>>	public void setLarghezza(int larghezza) { 
>>>		this.larghezza = larghezza; 
>>>	} 
>>>	public void setAltezza(int altezza) { 
>>>		this.altezza = altezza; 
>>>	} 
>>>	public int calcolaArea() { 
>>>		return larghezza * altezza; 
>>>	} 
>>>} 
>>>
>>>public class Quadrato extends Rettangolo { 
>>>	@Override public void setLarghezza(int larghezza) { 
>>>		this.larghezza = larghezza; 
>>>		this.altezza = larghezza; // effetto collaterale inatteso! 
>>>	} 
>>>	@Override public void setAltezza(int altezza) { 
>>>	this.altezza = altezza; 
>>>	this.larghezza = altezza; // effetto collaterale inatteso! 
>>>	} 
>>>}
>>>```
>>>Quindi la sotto classe overrida i setter della super classe, cosi facendo pero sovrascrive il comportamento della classe padre rompendo il programma
>>
>>
>>>[!done] **Esempio corretto:**
>>>```java
>>>// ✅ Corretto: modella le forme come concetti separati public 
>>>interface Forma { 
>>>	int calcolaArea(); 
>>>} 
>>>public class Rettangolo implements Forma { 
>>>	private int larghezza; 
>>>	private int altezza; 
>>>	public Rettangolo(int larghezza, int altezza) { 
>>>		this.larghezza = larghezza; 
>>>		this.altezza = altezza; 
>>>	} 
>>>	public int calcolaArea() { 
>>>	return larghezza * altezza; 
>>>	} 
>>>} 
>>>
>>>public class Quadrato implements Forma { 
>>>	private int lato; 
>>>	public Quadrato(int lato) { 
>>>		this.lato = lato; 
>>>} 
>>>
>>>public int calcolaArea() { 
>>>	return lato * lato; 
>>>	} 
>>>}
>>>```
>>>
>>>Anche in questo caso abbiamo definito una interfaccia con un metodo comune a tutte le sue sotto classi: questo metodo poi lo andiamo a specializzare per ciascuna sotto classe, in questo modo ogni sotto classe calcola l'area in modo diverso e di conseguenza il metodo della super classe(in questo caso dell'interfaccia) non viene  overridato e quindi il comportamento del programma non viene alterato.
>4. **I** – _Interface Segregation Principle_: ==è preferibile avere molte interfacce specifiche piuttosto che una sola interfaccia generica.==
>>[!example]- **Esempio: interfaccia `Animale`**
>>Supponiamo di avere una interfaccia `Animale` con i metodi `mangia()`, `vola()` e `nuota()`.
>>Ora abbiamo anche una classe concreta `Cane` che implementa l'interfaccia ma cosi facendo costringiamo questa classe ad implementare metodi che non gli competono.
>>Per risolvere questo problema una buona pratica spezzare l'interfaccia `Animale` in interfacce più piccole.
>>>[!failure] **Esempio errato** 
>>>```java
>>>// ❌ Sbagliato: interfaccia troppo generica 
>>>public interface Animale { 
>>>	void mangia(); 
>>>	void vola(); 
>>>	void nuota(); 
>>>} 
>>>public class Cane implements Animale { 
>>>	public void mangia() { System.out.println("Il cane mangia");} 
>>>	public void vola() { /* non implementato, non ha senso */ } 
>>>	public void nuota() { System.out.println("Il cane nuota"); }
>>>}
>>>```
>>>Come possiamo notare da questo esempio la classe `Cane` è costretta a implementare metodi totalmente errati a livello logico per un Cane (es: `vola()`)
>>
>>>[!done] **Esempio corretto**
>>>```java
>>> // ✅ Corretto: interfacce specifiche per capacità 
>>> public interface Mangiatore { 
>>> 	void mangia(); 
>>> } 
>>> public interface Volatore { 
>>> 	void vola(); 
>>> } 
>>> public interface Nuotatore { 
>>> 	void nuota(); 
>>> } 
>>> public class Cane implements Mangiatore, Nuotatore { 
>>> 	public void mangia() { System.out.println("Il cane mangia"); } 
>>> 	public void nuota() { System.out.println("Il cane nuota"); } 
>>> } 
>>> 	public class Aquila implements Mangiatore, Volatore { 
>>> 	public void mangia() { System.out.println("L'aquila mangia"); } 
>>> 	public void vola() { System.out.println("L'aquila vola"); }
>>> }
>>>```
>>>
>>>Spezzando l'interfaccia `Animale` in altre interfacce più piccole possiamo implementare i comportamenti corretti per ciascuna classe concreta. 
>>>Questo è il principio _Interface Segregation_ in azione.
>
>5. **D** – _Dependency Inversion Principle_: ==i moduli di alto livello non devono dipendere da quelli di basso livello; entrambi devono dipendere da astrazioni.==
>>[!example]- **Esempio: `OperazioneController`**
>>Questo principio, senza saperlo, l'abbiamo già riscontrato con Spring.
>>Supponiamo di avere una classe una [[Lezione 22 parte 2 - Spring framework#La Classe Controller|classe Controller]], `OperazioneController`, che come attributo un oggetto dell'interfaccia `OperazioneService`.
>>Come abbiamo già visto `OperazioneController` non istanzia direttamente `OperazioneService` con `new` ma la riceve tramite l'annotation [[Lezione 22 parte 3 - Dependency Injection#2. `@Autowired`|`@Autowired`]]: - ==questa cosa dipende dall'astrazione gestita dal container Spring, non dall'implementazione concreta.==
>>
>>>[!failure] **Esempio Errato**
>>>```java
>>>// ❌ Sbagliato: dipendenza diretta dall'implementazione concreta 
>>>public class OperazioneController { 
>>>	private OperazioneService service = new OperazioneService(); // accoppiamento forte 
>>>}
>>>```
>>
>>>[!done] **Esempio corretto**
>>>```java
>>>// ✅ Corretto: dipendenza dall'astrazione, gestita da Spring 
>>>@RestController 
>>>@RequestMapping("/operazioni") 
>>>public class OperazioneController { 
>>>	@Autowired
>>>	private OperazioneService service;// Spring inietta l'implementazione  
>>>}
>>>```
>>>==In questo caso, tramite l'annotazione [[Lezione 22 parte 3 - Dependency Injection#2. `@Autowired`|`@Autowired`]], Spring inietta(cioè istanzia) la classe concreta della Service a partire dalla reference dell'interfaccia della Service.==
>>>Questo è _Dependency Inversion Principle_ in azione.
>
>Nel contesto dell'AOP, il principio più rilevante è l'**SRP**: 
>	- ==inserire logica trasversale come il logging direttamente nelle classi di business significa assegnare a quella classe più di una responsabilità, rendendo il codice più difficile da mantenere e modificare.==



##### Dimostrazione Cross-Cutting Concerns
Per comprendere meglio questo concetto guardiamo l'immagine:
[![Screenshot-2026-04-02-at-14-54-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/63j8VWQJ/Screenshot-2026-04-02-at-14-54-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/S29Qkp8D)
Rappresenta visivamente il concetto di cross-cutting concern in un sistema con tre classi di servizio: 
1. `CourseService`, 
2. `StudentService`  
3. `MiscService`.

Le frecce **orizzontali** rappresentano i **[[#^classiTarget|target]]** — ==le classi di business che si sviluppano ciascuna per conto proprio, ognuna con la propria logica.==

Le frecce **verticali** — Security, Transactions, Other — rappresentano gli **[[#^classiAspetto|aspetti]]**: 
- ==attraversano trasversalmente tutte e tre le classi contemporaneamente, indipendentemente da cosa fa ciascuna di esse.==

Il messaggio visivo è immediato: 
- ==Security non appartiene a `CourseService`, né a `StudentService`, né a `MiscService` — appartiene a tutte e tre allo stesso tempo.== 
- ==Lo stesso vale per Transactions e per qualsiasi altro concern trasversale.==

**In OOP puro, ogni classe dovrebbe gestire questi comportamenti da sola — con il risultato di duplicare la stessa logica in tre posti diversi.** 
Con l'AOP invece ogni freccia verticale diventa ==un unico **Aspect**, scritto una volta sola, che il framework applica automaticamente su tutti i target coinvolti.==

> [!info] **È importante notare che nella realtà un aspetto non attraversa necessariamente tutti i target del sistema. **
> 
> Tramite il **Pointcut** — che vedremo a breve — ==è possibile definire con precisione su quali classi e su quali metodi un aspetto deve essere applicato. Il diagramma è una semplificazione visiva del concetto.==


## AOP: Terminologia

### Aspect

Un **Aspect:**
- ==rappresenta la modularizzazione di una caratteristica trasversale del sistema== — ad esempio il logging, la sicurezza o il tracciamento delle statistiche. 
- Ha principalmente un **significato progettuale**: 
	- ==descrive _cosa_ vogliamo separare e isolare, ma non ha una traduzione diretta a livello di codice.== 
	- ==È il concetto astratto da cui tutto parte.==
### Advice

Un **Advice** è: 
- ==l'**implementazione effettiva** di un Aspect.== 
- ==È il codice concreto che viene eseguito quando l'aspetto entra in azione.== 
- **I framework AOP — Spring incluso — implementano gli advice tramite degli interceptor:** 
	- ==componenti che si interpongono nell'esecuzione del target e ne filtrano il lavoro.==

**È importante capire che questo filtraggio lo decidiamo noi, e il _quando_ dipende dalla natura del concern:**

> [!example]
> - il **logging:** 
> 	- ==tipicamente si applica _dopo_ l'esecuzione del metodo, per tracciarne l'esito==
> - la **sicurezza e l'autenticazione:** 
> 	- ==si applicano _prima_, per bloccare l'esecuzione se le condizioni non sono soddisfatte==
> 

**L'interceptor inoltre non si limita a osservare:** 
- ==può anche **trattenere o modificare** il flusso di esecuzione.==



### Target

Un **Target** è: 
- ==il metodo — o la classe — a cui vogliamo applicare uno o più advice.== 
- ==È più preciso dire che il target è un **metodo specifico** di una classe, non la classe nel suo insieme, anche se per convenzione si parla spesso della classe come target.==

### Pointcut

Un **Pointcut** è un'**espressione** che: 
- ==individua tutti i metodi su cui deve agire un advice.== 
- **È il meccanismo con cui diciamo al framework _dove_ applicare l'aspetto:** 
	- ==su quali classi, su quali metodi, con quali condizioni.== 
- ==Come abbiamo visto, un pointcut può essere selettivo — non deve necessariamente coprire tutti i target del sistema.==
### JoinPoint

Un **JoinPoint** è: 
- ==il **punto del workflow** in cui l'advice si incrocia con il target.== 
In altre parole: 
- ==è il momento preciso in cui l'aspetto entra in azione durante l'esecuzione del programma.== 
**Può corrispondere a:**

- ==la **chiamata a un metodo**==
- ==il **sollevamento di un'eccezione**==
- ==il **cambiamento di stato di un attributo**==

Il modulo AOP di Spring prevede advice che agiscono esclusivamente sui metodi, e li classifica in base al _quando_ rispetto all'esecuzione del target:

- **Before** – ==prima dell'esecuzione del metodo==
- **After** – ==dopo l'esecuzione del metodo==
- **Around** – ==sia prima che dopo, con controllo completo sul flusso==
### AOP: I Tipi di JoinPoint in Spring

Spring mette a disposizione 5 tipi di joinpoint, ciascuno dei quali dà vita a un corrispondente tipo di interceptor:

1. **Before** — ==l'interceptor scatta **prima** che il metodo del target vada in esecuzione.==  ^7d1682

> [!example] **Tipico caso d'uso:**
>  ==la sicurezza e l'autenticazione, dove vogliamo verificare le condizioni _prima_ di permettere l'esecuzione.==

2. **After** — ==l'interceptor scatta **dopo** che il metodo del target va in esecuzione, **indipendentemente dall'esito** — che sia andato a buon fine o che abbia sollevato un'eccezione.== 

> [!example] **Utile per operazioni di cleanup o rilascio di risorse.**
> 

3. **After Returning** — ==l'interceptor scatta dopo l'esecuzione del metodo, ma **solo se ha avuto successo**.== 

> [!example] **Tipico caso d'uso:**
> il logging del risultato di un'operazione andata a buon fine.

4. **After Throwing** — ==l'interceptor scatta dopo l'esecuzione del metodo, ma **solo se è stata sollevata un'eccezione**.== 

> [!Example] **Tipico caso d'uso:**
>  il logging degli errori o la notifica di un fallimento.

5. **Around** — ==l'interceptor scatta **sia prima che dopo** l'esecuzione del metodo. Combina le caratteristiche di Before e After, ed è il tipo più potente perché ha controllo completo sul flusso — può decidere se far proseguire l'esecuzione del target oppure no.==

### Weaving e Proxy

#### Il Design Pattern Proxy

Per capire come Spring applica concretamente gli aspetti, bisogna prima richiamare il **Design Pattern Proxy**.

Il diagramma UML mostra la struttura: 
[![Screenshot-2026-04-02-at-15-36-46-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/8cW3SC3q/Screenshot-2026-04-02-at-15-36-46-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/GTLzPbbQ)


il `Client` non parla direttamente con il `RealSubject` — il componente che contiene la logica reale — ma con un `Proxy` che implementa la stessa interfaccia `Subject`. Il `Proxy` si **spaccia per l'oggetto reale** agli occhi del client, ma internamente delega la chiamata al `RealSubject`, potendo intervenire prima, dopo o intorno all'esecuzione.

Nel contesto AOP:

- il `RealSubject` corrisponde al **[[#Target|Target]]** — ==la classe di business==
- il `Proxy` corrisponde all'**[[#Advice|Advice]]** — ==il componente che intercetta e aggiunge il comportamento trasversale==

### Weaving

Il **Weaving** è: 
- ==il processo concreto con cui un framework AOP applica gli [[#Advice|advice]] alle classi [[#Target|target]] nei [[#JoinPoint|joinpoint ]] stabiliti, secondo la definizione dei [[#Pointcut|pointcut]].==

Spring realizza il weaving **a runtime** — come mostra questo diagramma:
[![Screenshot-2026-04-02-at-15-36-58-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/0y94TPfQ/Screenshot-2026-04-02-at-15-36-58-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/9rN1T3s5)
creando un **Spring Proxy** che avvolge il `TargetObjectImpl`. 
Quando il client chiama un metodo del target, in realtà sta chiamando il proxy: ==è lui che coordina l'esecuzione dell'Aspect e del `TargetObjectImpl`, senza che il target sappia nulla di ciò che lo circonda.==

Entrambi — Proxy e `TargetObjectImpl`: 
- ==implementano la stessa interfaccia Java (`TargetObject`), garantendo che il client non si accorga della differenza.==


#### AOP: Vantaggi

##### High Cohesion, Low Coupling

Il diagramma mostra visivamente il risultato concreto dell'applicazione dell'AOP — e più in generale di una buona architettura — attraverso due concetti fondamentali: **Cohesion** e **Coupling**.
[![Screenshot-2026-04-02-at-15-45-12-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/sg2kB3ZY/Screenshot-2026-04-02-at-15-45-12-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/2VPcMRGy)

Nel lato **Without:**
- **i componenti del sistema sono tutti interconnessi tra loro in modo caotico:** 
	- ==ogni elemento conosce e dipende da molti altri.== 
	- ==Questo è il risultato di un sistema senza separazione delle responsabilità — logica di business, logging, sicurezza e statistiche mescolati insieme ovunque.== 
	- ==È difficile da leggere, modificare e testare.==

Nel lato **With:**
- ==i componenti sono raggruppati in **moduli coesi** con poche connessioni tra loro.== 
- ==Ogni gruppo si occupa di una cosa sola, e i gruppi comunicano tra loro solo dove necessario.==

Questo corrisponde esattamente a due obiettivi architetturali che l'AOP aiuta a raggiungere:

- **High Cohesion** — ==ogni classe e ogni modulo ha una responsabilità ben definita e concentrata.== 

> [!example] **La `OperazioneService` fa solo calcoli, l'Aspect fa solo logging, il `StatisticheComponent` tiene solo i contatori.**


- **Low Coupling** — l==e classi di business non sanno nulla degli aspetti che le circondano.== 
	- **Non li importano, non li chiamano, non dipendono da loro.** 
	- **Il framework applica tutto in modo trasparente tramite il weaving.**

> [!summary] **I vantaggi in sintesi**
>
> 
> L'AOP permette di modellare i concern trasversali in classi apposite e di applicarne i comportamenti alle classi target in modo **dichiarativo** — cioè tramite annotazioni e pointcut, senza toccare il codice del target.
> 
> I benefici diretti sono due:
> 
> - **Elimina la duplicazione** del codice trasversale: 
> 	- ==la logica di logging, sicurezza o tracciamento si scrive una volta sola nell'Aspect, non in ogni classe che ne ha bisogno.==
> - **Rende la logica trasversale indipendente** dalla logica di business: 
> 	- ==si può aggiungere, modificare o rimuovere un aspetto senza toccare nessuna delle classi target.==

### AOP: Esempio — Il Logging del Cavaliere

#### Il problema: dipendenza forte

Ipotizziamo di avere un progetto che modella un **Cavaliere della Tavola Rotonda** che parte per la missione, e un **Menestrello** che ne deve narrare le gesta — una metafora perfetta per il logging.

Un primo approccio OOP classico potrebbe essere questo: il Cavaliere porta il Menestrello come **attributo**, e lo chiama direttamente dentro il metodo `partiPerMissione()`.

java

```java
public class CavaliereTavolaRotonda {
    private String nome;
    private Menestrello menestrello;

    public void setMenestrello(Menestrello m) {
        this.menestrello = m;
    }

    public SantoGraal partiPerMissione() {
        menestrello.cantaGesta(this.nome + " parte per la missione");
        return new SantoGraal();
    }
}
```

```java
public class Menestrello {
    public void cantaGesta(String verso) {
        System.out.println(verso);
    }
}
```

##### Perché questo modello è sbagliato

**Questo approccio funziona, ma viola tutto quello che abbiamo detto finora.** 
Il Cavaliere ha una **dipendenza forte** dal Menestrello: 
- ==lo conosce, lo porta con sé, lo chiama esplicitamente.== 
**Il Cavaliere non dovrebbe sapere nulla del Menestrello — narrare le gesta non è responsabilità sua, è un concern trasversale.**

In termini architetturali:

- il **Cavaliere** è il **[[#Target|Target]]** — ==contiene la logica di business==
- il **Menestrello** è l'**[[#Aspect|Aspect]]** — ==contiene la logica trasversale di logging==

> [!ticket] **Un Target non dovrebbe MAI conoscere i propri Aspect. **
> 

##### Il problema nel dettaglio

La soluzione OOP vista prima presenta due criticità concrete:

1.  il Cavaliere deve **interrompere la propria missione** per chiamare il Menestrello. 
	- ==La logica di business — partire per la missione e trovare il Graal — viene spezzata da una chiamata a un servizio trasversale che non gli compete.== 
	- ==Il processo di business viene interrotto per invocare un servizio di sistema==.

[![Screenshot-2026-04-02-at-16-15-30-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/Kz6KjZvm/Screenshot-2026-04-02-at-16-15-30-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/VrFsHPCh)


2.  problema di **scalabilità**: 
	- se nel sistema avessimo altri personaggi — un altro cavaliere, un paladino, un arciere — ognuno di loro dovrebbe portarsi dietro il proprio Menestrello. 
	- **Il risultato sarebbe:**
		- ==tanti Menestrelli istanziati, uno per ogni personaggio==
		- ==ogni personaggio accoppiato al proprio Menestrello, con una dipendenza forte e ripetuta ovunque==

##### La soluzione AOP

Con l'AOP il modello cambia radicalmente:

- il **Menestrello è uno solo** — ==un unico [[#Aspect|Aspect]] condiviso da tutto il sistema==
- il **Menestrello non è legato a nessun personaggio** — ==non è attributo di nessuno, non viene chiamato da nessuno esplicitamente==
- ==il Menestrello **incrocia la sua vita** con quella dei personaggi nei punti stabiliti dal [[#Pointcut|pointcut]], tramite il [[#Weaving|weaving]] di Spring== 
- tutti i personaggi **non sanno dell'esistenza del Menestrello** — ==il [[#Target|Target]] ignora completamente i propri Aspect==

> [!ticket] **Questo è il cuore dell'AOP:**
>  ==separare chi fa la logica di business da chi la osserva, la traccia o la intercetta — senza che i due si conoscano.==

#### AOP: La Soluzione in Codice

##### Definizione dell'Advice

Modelliamo il Menestrello come un **[[#Aspect|Aspect]]:**  
- non più una classe con dipendenza forte, ma un componente autonomo annotato con [[Lezione 22 parte 3 - Dependency Injection#1. `@Component`|`@Component`]] e `@Aspect`

```java
@Component
@Aspect
public class Menestrello {

    @Before("execution(* tavola.CavaliereTavolaRotonda.partiPerMissione(..))")
    public void cantaGesta() {
        System.out.println("il cavaliere è in partenza..");
    }
}
```

Analizziamo le annotazioni:

- `@Component` — ==rende il Menestrello un bean gestito da Spring==
- `@Aspect` — ==dichiara che questa classe è un Aspect AOP==
- [[#^7d1682|`@Before`]] — definisce il ** [[#AOP I Tipi di JoinPoint in Spring|tipo di joinpoint]]**: ==l'interceptor scatta *prima* dell'esecuzione del metodo target==
- La stringa `execution(* tavola.CavaliereTavolaRotonda.partiPerMissione(..))` è il **[[#Pointcut|pointcut]]**: 
	- ==individua esattamente il metodo su cui l'advice deve agire.== 
La sintassi è:
```java
execution(* package.ClasseTarget.metodoTarget(..))
```

==dove `*` indica qualsiasi tipo di ritorno e `(..)` indica qualsiasi lista di parametri.== 

#####  Il risultato: il Cavaliere libero dal Menestrello

A questo punto la classe `CavaliereTavolaRotonda` può essere riscritta eliminando **qualsiasi riferimento** al Menestrello:
```java
public class CavaliereTavolaRotonda {
    private String nome;

    public SantoGraal partiPerMissione() {
        return new SantoGraal();
    }
}
```
Il Cavaliere non sa nulla dell'esistenza del Menestrello, non lo importa, non lo chiama. 
==Si occupa esclusivamente della propria logica di business — trovare il Graal.==

È Spring che, tramite il **[[#Weaving|weaving a runtime]]**, ==fa sì che il Menestrello intercetti la chiamata a `partiPerMissione()` nel momento giusto, avvolgendo il Target con il proprio Proxy.== 
Non esiste più alcun legame diretto tra il servizio trasversale e la logica di business.
[![Screenshot-2026-04-02-at-16-12-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/1R7whQZG/Screenshot-2026-04-02-at-16-12-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/qgnzyWqq)
### AOP: Il Proxy a Runtime

#### Come Spring collega Target e Advice

Il motore AOP di Spring collega Target e Advice creando un **Proxy a runtime**. Questo avviene tramite la classe `ProxyFactoryBean`, che agisce esattamente come il Design Pattern Proxy che abbiamo già visto.

Il diagramma UML mostra la struttura nel caso in cui il target implementi una interfaccia — che è il caso più comune in Spring:

- **`Cavaliere`** è l'interfaccia Java che dichiara il metodo `partiPerMissione()`
- **`CavaliereTavolaRotonda`** è l'implementazione concreta — il Target — che implementa `Cavaliere`
- **`ProxyFactoryBean`** implementa anch'essa `Cavaliere`, e al suo interno possiede:
    - un'istanza di `CavaliereTavolaRotonda` — il Target
    - un'istanza di `Menestrello` — l'Advice

### Il flusso di esecuzione

Quando il client chiama `partiPerMissione()`, in realtà sta chiamando il metodo della `ProxyFactoryBean` — non direttamente il Cavaliere. 
È la `ProxyFactoryBean` a decidere, in base al tipo di advice configurato, l'ordine di esecuzione:
[![Screenshot-2026-04-02-at-16-23-09-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/CLjvF5LY/Screenshot-2026-04-02-at-16-23-09-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/yk8hjVZr)
Il diagramma chiarisce le relazioni tra i componenti con precisione:

1. `Cavaliere` ==è l'**interfaccia** che dichiara il metodo comune `partiPerMissione()`.==

2. `CavaliereTavolaRotonda` **realizza** l'interfaccia `Cavaliere` — ==relazione rappresentata in UML con una freccia tratteggiata con punta triangolare vuota, che in Java corrisponde a `implements` — e specializza il metodo con la propria implementazione concreta.==

`ProxyFactoryBean` implementa anch'essa l'interfaccia `Cavaliere`, e al suo interno **aggrega** due attributi tramite composizione:

- `-CavaliereTavolaRotonda k` — ==dove `k` sta per _knight_, il Target==
- `-Menestrello adv` — ==dove `adv` sta per _advice_, l'Aspect==

> [!link] I rombi vuoti nel diagramma, come sappiamo, indicano una **[[Responsabilità#Le responsabilità|aggregazione o responsabilità]]**: 
> 
> - ==In questo caso`ProxyFactoryBean` **referenzia** i due oggetti, ma non ne è responsabile del ciclo di vita — se viene distrutta, `k` e `adv` continuano ad esistere.==
> 

Il punto chiave è che sia `CavaliereTavolaRotonda` che `ProxyFactoryBean` implementano la stessa interfaccia `Cavaliere`: questo rende il proxy **trasparente** al client, che vede solo il contratto dell'interfaccia senza sapere che in mezzo c'è un proxy.


##### Implementazione in Java
1. **Interfaccia `Cavaliere`** 
```
// Interfaccia comune 
public interface Cavaliere { 
	SantoGraal partiPerMissione(); 
}
```

2. **Classe Concreta `CavaliereTavolaRotonda`(Target)**
```java
// Target - implementa l'interfaccia 
public class CavaliereTavolaRotonda implements Cavaliere { 
	private String nome; 
	public CavaliereTavolaRotonda(String nome) { 
		this.nome = nome; 
	} 
	@Override public SantoGraal partiPerMissione() { 
		return new SantoGraal(); 
	} 
}
```


3. **Classe `Menestrello`(Advice)**
```java
// Advice - il Menestrello come Aspect 
@Component 
@Aspect 
public class Menestrello { 
	@Before("execution(* tavola.CavaliereTavolaRotonda.partiPerMissione(..))") 
	public void cantaGesta() { 
		System.out.println("il cavaliere è in partenza.."); 
		} 
	} 
```

4. **Classe `ProxyFactoryBean`**
```java
// ProxyFactoryBean - implementa la stessa interfaccia 
public class ProxyFactoryBean implements Cavaliere { 
	private CavaliereTavolaRotonda k; // Target private
	Menestrello adv; // Advice public 
	ProxyFactoryBean(CavaliereTavolaRotonda k, Menestrello adv) { 
		this.k = k; 
		this.adv = adv; 
	} 
	@Override 
	public SantoGraal partiPerMissione() { 
		adv.cantaGesta(); // @Before - prima della logica di 
		business return k.partiPerMissione(); // delega al Target 
	} 
}
```
### AOP: Il Proxy senza Interfaccia

#### Il diagramma UML

Questo secondo scenario mostra l'architettura nel caso in cui il target **non implementi una interfaccia** — `CavaliereTavolaRotonda` è una classe concreta senza contratto.
[![Screenshot-2026-04-02-at-16-42-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png](https://i.postimg.cc/fLP9nc08/Screenshot-2026-04-02-at-16-42-39-Microsoft-Power-Point-Spring-Core-Aspect-oriented-programming-C.png)](https://postimg.cc/BLx621pF)
In questo caso la `ProxyFactoryBean` non può implementare una interfaccia comune, quindi Spring adotta una strategia diversa: la `ProxyFactoryBean` **estende** direttamente `CavaliereTavolaRotonda` tramite ereditarietà (`<<extend>>`).

Le differenze rispetto al diagramma precedente sono due:

- Non esiste più l'interfaccia `Cavaliere` — ==non c'è contratto comune tra i due==
- La relazione tra `ProxyFactoryBean` e `CavaliereTavolaRotonda` passa da **realizzazione** a **ereditarietà** — ==freccia continua con punta triangolare vuota in UML, che in Java corrisponde a `extends`==

- ==`ProxyFactoryBean` aggrega comunque il `Menestrello` tramite l'attributo `-Menestrello adv`, esattamente come nel caso precedente.==

Il risultato per il client rimane lo stesso: vede una `CavaliereTavolaRotonda` — in questo caso la sottoclasse proxy — senza sapere di essere intercettato.

##### Implementazione in Java
1. **Classe `CavaliereTavolaRotonda`(Target)**
```java
// Target - classe concreta, nessuna interfaccia 
public class CavaliereTavolaRotonda { 
	private String nome; 
	public CavaliereTavolaRotonda(String nome) { 
		this.nome = nome; 
	} 
	public SantoGraal partiPerMissione() { 
		return new SantoGraal(); 
	} 
}
```

2. **Classe `Menestrello`(advice)**
```java
// Advice - rimane identico 
@Component 
@Aspect 
public class Menestrello { 
	@Before("execution(* tavola.CavaliereTavolaRotonda.partiPerMissione(..))") 
	public void cantaGesta() { 
		System.out.println("il cavaliere è in partenza.."); 
	} 
}
```

3. **Classe `ProxyFactoryMethod`**
```java
// ProxyFactoryBean - ESTENDE il Target invece di implementare una interfaccia 
public class ProxyFactoryBean extends CavaliereTavolaRotonda { 
	private Menestrello adv; // Advice public 
	ProxyFactoryBean(String nome, Menestrello adv) { 
		super(nome); // chiama il costruttore della superclasse 
		this.adv = adv; 
	} 
	@Override 
	public SantoGraal partiPerMissione() { 
		adv.cantaGesta(); // @Before - prima della logica di business 
		return super.partiPerMissione(); // delega alla superclasse 
	} 
}
```
### Il flusso di esecuzione

Quando il client chiama `partiPerMissione()`, in realtà sta chiamando il metodo della `ProxyFactoryBean` — non direttamente il Cavaliere. È la `ProxyFactoryBean` a coordinare l'ordine di esecuzione in base al tipo di advice configurato:

1. invoca `cantaGesta()` del Menestrello — perché il joinpoint è `@Before`
2. invoca `partiPerMissione()` di `CavaliereTavolaRotonda` — la logica di business

Il client non si accorge di nulla. Questo è il **weaving a runtime** in azione.
### AOP: filtraggio 
Gli intercettori usati come filtri
SI possono applicare anche più filtri
Pensiamo a i filtri di un rubinetto: posso applicare il filtro per il calcare come applicare un ulteriore filtro subito dopo o prima 
Ogni intercettore possiede riferimenti diretti al target, al metodo intercettato ed a tutti i suoi parametri che può utilizzare e/o modificare 
In questo caso si dice che l'intercettore filtra il metodo target
Questo meccanismo di filtraggio: al ritorno l'ordine si inverte 

Gli intrecettori usati come filtri sono potenti al punto di poter alterare le funzioni target 
Tipicamente gli intercettori dovrebbero incasulare solo funzionalità trasversali che non alterano le funzionalità principali. 
Tutto questo permette di non modificare/sporcare la classe target 

### Interceptor Aroudn 
é possibile applicare più advices sullo stesso target, dove ogni adivce si occupa di implementare uno specifico apsetto.
In questo caso si parla di catena di intercetori 


### Configurazione per spirn boot
Aggiungiamo due dipendenze al `pom.xml`: 
```xml
<dependecy>
	<groupId>org.springframework</groupId>
</dependecy>
<dependecy></dependecy>
```

### AOP via annotatiosn
Le configurazione degli intercettori si realizzano mediante annotazioni 


#### Esempio advice con vari koinpoint

```java
@Aspect
@Component
public class Spettatore{
	@Pointcut("execution(* esempio.Artista.perform())")
	public void performance(){}; 
	@Before("performance()")
	public void prendePosto(){
		System.out.println("Il pubblico prende posto");
	}
	
	@Before("performance()")
	public void spegneCellulari
}
```


#### Esempio con Around
```java
@Around("performance()")
// il metodo prende un oggetto ProceedingJoinPoint e torna void oppure
public void guardaPerformance(ProceedingJoinPoint joinpoint){
	try{
		// pre-processing
		System.out.println("Il pubblico prende posto"); 
		System.out.println("Il pubblico spegne i cellulari");
		long start = System.currentTimeMillis(); 
	
		// invocazione al prossimo advice oppure al metodo target
	joinpoint.proceed(); 
	
		//post-processing
		long end = System.currentMillis(); 
		 System.out.println("CLAP CLAP CLAP CLAP CLAP");
		 System.out.println("La performance è durata " + (end-start) + " millisecondi");
	}catch(Throwable t){
		System.out.println("Lo spettacolo è stato interroto"); 
	}
}
```

Il parametro può essere il Target oppure l'elemento dopo che potrebbe non essere necessariamente il Target ma anche un altro intercettore (advice)
