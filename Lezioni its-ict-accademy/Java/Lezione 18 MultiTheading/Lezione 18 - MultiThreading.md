
## Task e MultiTasking 
==Un **processo** è un programma in esecuzione (o una sua parte).==  
Quando avviamo un’applicazione, il sistema operativo crea un processo che dispone delle risorse necessarie per essere eseguito: [[Il modello di Von Neumann#RAM|memoria]], tempo di [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]], file aperti, ecc.

Il **multitasking** è: 
- ==la capacità del sistema operativo di eseguire più processi “contemporaneamente”.== 
In realtà, soprattutto su una singola CPU, si tratta di una **simulazione del parallelismo**: 
- ==la CPU passa rapidamente da un processo all’altro, dando l’impressione che vengano eseguiti nello stesso momento.==  
Su sistemi multi-core, invece, ==più processi possono realmente essere eseguiti in parallelo.==

Il componente responsabile di questa gestione è lo **scheduler** del sistema operativo.  
Lo scheduler decide:

- ==quale processo deve essere eseguito,==
    
- ==per quanto tempo può utilizzare la CPU,==
    
- quando effettuare il **context switch:**
	- ==cioè il passaggio da un processo a un altro.==
    

Il context switch: 
- ==comporta il salvataggio dello stato corrente di un processo (registri, contatore del programma, ecc.) e il ripristino dello stato del processo successivo.==

###  Caratteristiche del multitasking

- Ogni processo possiede un **proprio spazio di indirizzamento in memoria** (spazio indirizzato). 
- Questo significa che i processi sono isolati tra loro: 
	- uno non può accedere direttamente alla memoria dell’altro.
    
- La **comunicazione tra processi (IPC – Inter Process Communication)** è più complessa e viene gestita dal sistema operativo tramite meccanismi specifici (pipe, socket, memoria condivisa, ecc.).


> [!link] ### Collegamento con i Thread
>
>I **thread** possono essere visti come: 
>- ==unità di esecuzione più leggere rispetto ai processi.==  
>A differenza dei processi:
>
>- ==condividono lo stesso spazio di memoria,==
 >   
>- ==appartengono allo stesso processo,==
  >  
>- ==collaborano per svolgere parti diverse dello stesso compito.==
 >   
>
>Possiamo quindi pensare ai thread non come processi completamente indipendenti, ma come ==**sotto-attività coordinate** che lavorano insieme per raggiungere un risultato comune, condividendo risorse e dati.==
>
>Questo è il passaggio concettuale fondamentale:
>
>- ==il multitasking riguarda più processi separati,==
  >  
>- ==il multithreading riguarda più flussi di esecuzione all’interno dello stesso processo.==



### Thread
Un **thread** è: 
- ==un flusso di esecuzione all’interno di un processo.==  
Se nel paragrafo precedente abbiamo visto che un processo è un programma in esecuzione con un proprio spazio di memoria, ora possiamo precisare che un processo può contenere **uno o più flussi di esecuzione**.

Fino ad ora abbiamo lavorato principalmente con programmi **mono-thread:** 
- ==cioè applicazioni che eseguono un unico flusso: il _thread principale_ (`main`).== 
In questo caso l’esecuzione è sequenziale:
- ==un’istruzione dopo l’altra.==

Tuttavia, a partire dal thread principale è possibile generare **thread secondari**, che permettono di suddividere il lavoro in più attività eseguite in modo concorrente. In questo senso:

- ==un processo può essere **mono-thread** (un solo flusso),==
    
- ==oppure **multi-thread** (più flussi di esecuzione interni).==
    

Un processo multi-thread può essere visto come:
- ==un insieme di flussi che collaborano tra loro per raggiungere un obiettivo comune.== 
I thread non sono completamente indipendenti come i processi:

- ==condividono la stessa memoria,==
    
- ==condividono le stesse risorse del processo,==
    
- ==possono quindi comunicare in modo diretto e più semplice.==



> [!deep]  Thread principale e thread secondari
>
>Ogni processo ha **almeno un thread principale**, ==che rappresenta il punto di ingresso del programma.==  
>Da questo possono essere creati altri thread per delegare specifiche attività (ad esempio operazioni lunghe, I/O, calcoli complessi).
#### Priorità e Scheduler

I thread possono essere ordinati secondo una **priorità**.  
La priorità rappresenta: 
- ==un suggerimento al [[I fundamentals di un Sistema Operativo|sistema operativo]] su quale thread dovrebbe avere maggiore probabilità di ottenere tempo di [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]].==
- 

È importante però sottolineare che:

- ==lo **scheduler** del sistema operativo decide effettivamente quale thread eseguire,==
    
- ==il programmatore può organizzare i flussi e impostare priorità,==
    
- ==ma non controlla direttamente l’ordine reale di esecuzione.==
    

In altre parole, la gestione concreta della CPU rimane sempre a carico del sistema operativo.

### Multithreading
Il **multithreading** indica la possibilità di: 
- ==eseguire più **[[#Thread|thread]]** contemporaneamente all’interno dello stesso processo.==  
In pratica, ==piccole unità di calcolo del programma possono essere eseguite **quasi simultaneamente**, sfruttando meglio la CPU e riducendo i tempi di esecuzione complessivi==.


> [!done]  **Vantaggi**
>
>- **Maggiore velocità di calcolo**: 
>	- ==dividendo il lavoro in più thread, alcune operazioni possono essere eseguite in parallelo.==
  >  
>- **Efficienza**: 
> 	 - ==le risorse della CPU vengono utilizzate meglio, soprattutto nei programmi che prevedono operazioni lunghe o I/O.==
> Contents


Le caratteristiche sono 
- ==I thread diversi **condividono lo stesso spazio di memoria** del processo a cui appartengono== (JAVA Heap). Questo rende la **comunicazione tra thread molto più semplice** rispetto alla comunicazione tra processi separati.
- Tuttavia, la condivisione di memoria introduce **problemi di sincronizzazione**: 
	- ==se più thread accedono contemporaneamente agli stessi oggetti, possono verificarsi **condizioni di race** o incoerenze dei dati.==
### JVM e Schedulazione dei Thread
La **[[Lezione 1 - Introduzione a Java#La JVM e l’indipendenza dalla piattaforma|Java Virtual Machine (JVM)]]** gestisce i thread utilizzando il criterio chiamato **preemptive-priority scheduling**, che combina diversi fattori per stabilire quale thread eseguire in un dato momento:

- **Priorità del thread**: ==ogni thread ha un valore di priorità compreso tra 1 e 10.==
    
- **Ordine di arrivo**: ==l’istante di tempo in cui un thread diventa pronto all’esecuzione (cioè entra nello stato _Runnable_).==
    
- **Time slicing**: ==intervalli di tempo limitati della CPU assegnati a ciascun [[#Thread|thread]].==   ^timeSlicing
#### Come lavora lo scheduler della JVM

1. **Schedulazione dei thread Runnable**: 
	- ==tutti i [[#Thread|thread]] pronti all’esecuzione vengono considerati e viene stabilito per ciascuno un intervallo di tempo della CPU ([[#^timeSlicing|time slicing]]).==
    
2. **Selezione per priorità**: 
	- ==tra i thread pronti, quello con la priorità più alta viene mandato in esecuzione.==
    
3. **Context switch**: 
	- lo scheduler può interrompere un thread in esecuzione e passare a un altro thread nelle seguenti condizioni:
    
	    1. ==Arriva un [[#Thread|thread]] con **priorità maggiore**.==
        
	    2. ==Il thread corrente è stato **interrotto** o ha **terminato il task**.==
        
	    3. ==Lo **slot di tempo assegnato** al thread corrente si è esaurito.==
        
4. **Gestione dei thread con stessa priorità**: ==se più thread hanno la stessa priorità, vengono eseguiti secondo l’ordine di arrivo, applicando la logica **First Come, First Serve (FCFS)**.==

> [!example] **In sintesi:**
>  ogni thread, anche quello principale, viene schedulato secondo priorità, ordine di arrivo e time slicing. 
>  Questo sistema permette alla [[Lezione 1 - Introduzione a Java#La JVM e l’indipendenza dalla piattaforma|JVM]] di gestire efficacemente più flussi di esecuzione concorrenti, massimizzando l’uso della [[Il modello di Von Neumann|CPU]] pur mantenendo una gestione ordinata dei thread.
> 

### Il thread main 
Il metodo `main` viene eseguito all’interno di un **thread principale**, chiamato anche **main thread**.  [![Screenshot-2026-02-19-at-17-11-37-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png](https://i.postimg.cc/c4hqXZv2/Screenshot-2026-02-19-at-17-11-37-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png)](https://postimg.cc/QHFnd2kJ)

==Da questo thread è possibile creare e avviare **thread secondari**, che lavorano in **parallelo** sia tra loro sia rispetto al thread principale.==



Ogni thread, principale o secondario, ==cerca di completare il proprio compito in modo indipendente, pur potendo **interagire con gli altri thread** quando necessario, ad esempio condividendo dati o risorse comuni.==

[![Screenshot-2026-02-19-at-17-12-12-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png](https://i.postimg.cc/L5S7302t/Screenshot-2026-02-19-at-17-12-12-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png)](https://postimg.cc/5YPnxgHy)

### Classi di supporto nella libreria di Java
Il **multithreading** può essere implementato in molti linguaggi, ma Java fornisce delle [[Lezione 6 - API|API]] di base specifiche per gestirlo. Tutte si trovano nel package `java.lang` e le principali sono:

- **[[#Creare un thread|`interface Runnable`]]**   ^interfaceRunnable
    - ==Definisce il comportamento di un thread. Contiene un solo metodo astratto (`run()`), perciò è un’interfaccia funzionale che può essere implementata tramite lambda.==
    
- **[[#Classe `Thread`|`class Thread`]]**    ^classThread
    - ==È una classe concreta che fornisce metodi per **creare, avviare e gestire thread**, come `start()`, `join()`, `sleep()`, e `interrupt()`.==
    
- **`class Object`**   ^classObject
    - Contiene metodi fondamentali per la **sincronizzazione**, come `wait()`, `notify()` e `notifyAll()`, 
    - ==utili per coordinare l’accesso concorrente alle risorse condivise e risolvere problemi di sincronizzazione tra thread.==

### Creare un thread 
Come abbiamo anticipato poco sopra, il comportamento di un thread è definito dall’**[[#^interfaceRunnable|interfaccia `Runnable`]]:**
- ==che rappresenta l’azione che il thread dovrà eseguire==:
```java
public interface Runnable {
    // rappresenta il compito da eseguire dal thread
    public void run();
}

```

La **classe `Thread`** è: 
- ==un’implementazione concreta di `Runnable` e fornisce tutti gli strumenti necessari per **creare e gestire thread**.==  
Il metodo `run()` della classe `Thread` non esegue nulla di predefinito; 
- ==serve come punto di ingresso per il codice del thread.==

Per creare un thread in Java si possono usare due tecniche principali:

- ==**Estendere la classe `Thread`**, sovrascrivendo il metodo `run()`.==
    
- ==**Implementare l’interfaccia `Runnable`**, definendo il comportamento all’interno del metodo `run()`.==
    

> [!attention] **Nota:** 
> ==l’approccio con `Runnable` è utile quando la classe deve estendere un’altra classe, perché Java non consente l’ereditarietà multipla.==

### Classe `Thread`

La [[#^classThread|classe `Thread`]]:
- ==rappresenta un **sotto-processo**, ovvero un’unità di esecuzione indipendente all’interno di un processo.==
Come abbiamo già anticipato poco sopra questa classe è l'implementazione concreta dell'interfaccia `Runnable`, e fornisce tutti gli strumenti necessari per **creare e gestire thread**

**Costruttori principali:**

- `Thread()` – ==crea un thread senza specificare il nome o il target; il nome di default sarà `"Thread-n"`, dove `n` è un numero progressivo.==
    
- `Thread(Runnable target)` – ==crea un thread associato a un oggetto `Runnable`==.
    
- `Thread(Runnable target, String name)` – ==crea un thread con un target e un nome specifico.==
    
- `Thread(String name)` – ==crea un thread con un nome specifico ma senza target.==
    

> [!note] Nota: 
> ==se non viene specificato il target `Runnable`, il thread non eseguirà nulla di predefinito==. 
> Solo il thread principale (`main`) ha un nome di default `"main"`.

**Metodi principali:**

- `getName()` – ==restituisce il nome del thread.==
    
- `setName(String name)` – ==imposta il nome del [[#Thread|thread]].==
    
- `static currentThread()` – ==ritorna il [[#Thread|thread]] corrente in esecuzione.==
    

Questi costruttori e metodi permettono di creare, identificare e gestire thread in modo flessibile all’interno di un’applicazione multithread.
#### Utilizzo di Thread 
Per creare e avviare un thread tramite estensione della classe `Thread` si seguono tre passi principali:

1. ==**Estendere la classe** `java.lang.Thread`.==
    
2. ==**Ridefinire il metodo** `run()`, che contiene il codice da eseguire nel thread.==
    
3. ==**Creare un’istanza del thread** e avviarla tramite il metodo `start()`.==
    

> [!note] **Nota:** 
> il metodo `start()`: 
> - ==**inizializza e avvia il [[#Thread|thread]]**,== 
> mentre `run()`:
> -  ==è il metodo che effettivamente esegue il codice del [[#Thread|thread]].== 
>>[!bug] Non si dovrebbe mai chiamare `run()` direttamente, perché in tal caso il codice verrebbe eseguito nel thread corrente anziché in uno nuovo.
> 
> Questo meccanismo, in cui `start()` prepara e invoca indirettamente `run()`, è un esempio di **Inversione di Controllo (IOC)**: 
> - ==è il thread  a gestire autonomamente l'esecuzione del metodo `run()`, non il programmatore.==
### Schema 
```java
class MyThread extends Thread {
    @Override
    public void run() {
        // codice del thread
    }
}

```

Nel main; 
```java
public class Main {
    public static void main(String[] args) {
        MyThread tr = new MyThread();
        tr.start(); // avvia il thread
    }
}
```
Questo approccio consente di creare thread autonomi, ciascuno con il proprio flusso di esecuzione, pur rimanendo gestibile dal programmatore tramite l’oggetto `Thread`.

### Avviare un Thread 
Quindi, dopo aver creato un’istanza di `Thread` tramite il costruttore, **il thread non è ancora un flusso di esecuzione**. 
Per trasformarlo in un thread operativo, bisogna chiamare il metodo `start()`.

Il metodo **`Thread.start()`** svolge tre compiti principali:

- ==Crea le risorse di sistema necessarie per eseguire il thread.==
    
- ==Schedula il thread per l’esecuzione.==
    
- ==Chiama internamente il metodo `run()` della classe thread.==
>Dopo il ritorno di `start()`, ==il thread entra nello stato **Runnable** e rimane pronto per essere eseguito secondo le regole dello scheduler.==


> [!caution] **Importante:**
>
>- Non si dovrebbe mai invocare direttamente `run()`, perché in tal caso:
>	- ==il codice verrebbe eseguito **nel thread corrente**, non in un nuovo thread, e quindi **non ci sarebbe multithreading**.==
   > 
>- ==Gli oggetti che implementano `Runnable` da soli **non si avviano**, perché non hanno un metodo `start()`.==

**Esempio pratico:**
```java
MyThread t = new MyThread();

// Esecuzione diretta del metodo run() -> NON multithreading
t.run();

for(int i = 0; i < 200; i++)
    System.out.println("ciclo - " + i);
```
In questo caso, il metodo `run()` ==viene eseguito nel **thread corrente**, quindi prima termina `run()` e poi inizia il ciclo del `for`, senza esecuzione parallela.==

Per avere un vero multithreading, è necessario chiamare:
```java
t.start(); // avvia il thread e il suo run() in parallelo
```
Così il thread `t` può lavorare contemporaneamente ad altri thread e al main thread.


> [!Deep] **`run()` vs. `start()`**
> Per capire meglio: 
> 1. **`Runnable`**
>
>- È un’interfaccia funzionale che definisce **un solo metodo astratto**:
>```java
> public void run();
>```
>
>Il metodo `run()` ==contiene il **comportamento che vogliamo far eseguire dal thread**, ma **non crea da solo un thread**.==
>1. **`Thread`**
>    
 >   - La classe `Thread` implementa `Runnable` (o può ricevere un `Runnable` come target).
 >       
 >   - Ha un **metodo `start()`** che:
 >       
  >      - ==Crea le risorse di sistema per il nuovo thread.==
 >           
 >       - ==Schedula il thread per l’esecuzione.==
 >           
  >      - ==**Chiama internamente `run()`** nel nuovo thread.==
 >           
>
>Quindi la differenza chiave è:
>
>- **Chiamare `run()` direttamente** → ==viene eseguito **nel thread corrente**, nessun multithreading.==
  >  
>- **Chiamare `start()`** → ==il thread viene avviato, e Java invoca `run()` nel **nuovo thread**, parallelo al thread chiamante.==
  >  
>
>In altre parole, **`start()` ==è il metodo che crea l’esecuzione parallela**, mentre `run()` contiene solo le istruzioni da eseguire.==



### Utilizzo di Runnable 
passo 1 : implementare l'interfaccia Runnable di `java.lang` implementando il metodo `run()`(sono obbligato a fare l'overriding di run)
passo 2: creare un oggetto `Runnable`(creare una classe che implementa `Runnable`)
passo 3: costruire un Thread attraverso il Runnable utilizzando `Thread(Runnable target)` 
	- Questo significa che costruisco il Therad con l'oggetto della nuova classe 
Passo 4 : avviare il thread invocando `start()` sull'oggetto. 
#### Schema 
```
class MyClass implements Runnable{
	...
	public void run(){...}; 
	...
}
```

Nel main; 
```
MyClass p = new Class(); 
Thread tr = new Thread(p); 
tr.start(); 
```

Questo è utile quando abbiamo una classe che non si estende alla classe `Thread` ma volgiamo che lavori come un thread.

### La priorità
Tutti i thread nascono con la priorità di defualt (5).
La priorità di un Thread è un numero positivo tra 1 a 10.
- Non è detto che la JVM riconosca esattamente 10 valori!
La classe `java.lang.Thread` definisce 
- `public static final int MAX PRIORITY` = 10


### User & daemon
I thread sono essenzialemente di 2 tipi: 
- Thread user 
- Thread daemon
Tutti i thread nascono user, ma si possono impostare daemon con il metodo 
```
void setDaemon(boolean)
```

DEVE essere invocato prima dello `start()`, col valore `true` imposta il Thread come daemon, viceversa rest `user`. 
Il thread Daemon è un Thread ombra del Thread user: quindi è un thread a bassa priorità del thread user da cui dipende , chiudendo un thread user si chuide anche il thread daemon

In particolare un thread daemon termina il suo Thread user termina 
Un thread user e thread daemon sono strutturalmente uguali, tranne che per la schedualzione e la chiusura 


### Ciclo di vita di un Thread 
Un thread viene definito dalla scheduler 

Le fasi sono: 
1. `New`: il thread nasce con la claausola `new`

2. `Runnable`: quando si fa `start()` diventa Runnable non running, quindi diventa eseguibile ma non si esegue ancora. 
3. `Run`: quando la JVM fa `run()` diventa running, quindi viene eseguito. 
4. Dead: quando finisce il running passa in questo stato ma non vuol dire che è morto l'oggetto semplicemente ha finito la sua vita da Thread 
5. Blocked: è uno stato ulteriore, avvine quando ad esempio il Thread viene mandarto in stato `sleep()`. 
Tuttavia il un altro metodo per mandare il Thread in Blocked è il `join`. 

[![Screenshot-2026-02-17-at-09-41-33-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png](https://i.postimg.cc/RV7Z1NDB/Screenshot-2026-02-17-at-09-41-33-Microsoft-Power-Point-Java-18-Thread-Compatibility-Mode-Java-18.png)](https://postimg.cc/PPqHTrH3)
### Passaggi di Stato 
Un Thread eseguibile oscilla continuamente tra Runnable e Running (in base all'utilizzo del processore).

Un Thread viene sospeso/bloccato se: 
- Sono stati invocati `sleep`, `join`
- Ci sono operazioni di I/O bloccanti 
- è stato chiamato il metodo `suspend`
	- questo metodo sospendo il Thread e lo riesegue in un momento non specificato, per questo è stato deprecato perché non assicura quando il Thread venga rieseguito 
- è stato chiamato il metodo wait (usato per gestione )

### Metodi bloccanti 
Si può rallentare il thread corrente (in Running), sospendendolo per un tempo prefissato, con il metodo 
```java
public static void sleep(long millis);
public static void sleep(long milli, int nanos)
```

SI può raccordare il thread corrente con un thread targrt  invocando su quest'utlimo il metodo: 
```java
public final void join(); 
public final void join(long milli); 
public final void join(long milli, int nanos); 
```

### Da running a Runnable 
Molto raramente può capitare di dover interagire con lo scheduler per la gestione dei thread.
Il metodo: 
```
public static void yield()
```
cede il passo ad un altro thread, nel senso che suggerisce allo scheduler di operare lo switch context e mandare in esecuzione uno dei thread con priorità maggiore o uguale di quello corrente.


### Interruzione 
I metodi `suspend()` e `stop()` sono deprecati perché potrebbero interrompere (anche definitivamente) il thread mentre sta eseguendo un operazione atomica.
Dalla versione 1.1 sono stati introdotti: 

```java
public void interrupt();
public static boolean interrupted(); 
```

che offrono un meccanismo di interruzione meno "aggressivo", infatti il thread da chiudere viene sollecitato ad interrompersi, ma questo avverrà solo se (e quando) esso stesso lo consentirà. 

Funzionamento: 
- Il thread che vuole interrompere un altro thead invocherà il metodo `interrupt()` sull'oggetto relativo al thread da chiudere.
	- In questo modo setta una flag che indica la necessità di intterompere il thread
- Il thread 


### La sincronizzazione 

Abbiamo accenato che i thread condividendo spazio in memoria potrebbero avere problemi di sync. 
Ad esempio due processi che lavornao per uno scopo comune si devono sincronizzare tra loro.

#### Esempio: il c/c
La classe account modellla un semplice c/c
```java
public class Account exteds Thread{
	private int balance = 1000; 
	public int getBalance(){
		return balance;
	}
	
	public void withdraw(int amount){
		if (balance>=amount){
			System.out.println(Thread.currentThread().getName()+ " sta per eseguire il prelievo")
			balance = balance - amount;
			System.out.println("prelievo ok per " + Thread.currentThread().getName() + " , saldo attuale: " + balance)
		} 
	}

}
```

Il prelievo (withdraw) si può fare solo se c'è disponibilità → senza mandare il conto in rosso 
I prorpietari Fred e lucy condividono il conto e volgiono fare prelievi 


Il metodo di prelievo esegue questi step: 
1. Controllare il saldo
2. Se ci sono abbastanzi soldi, allora eseguire il prelievo
Se pero si separaono i 2 step, non c'è più coerenza
	- il controllo al punto 1; perde di senso se nel frattempo lo stato del conto è cambiato!
Implementiamo una versione di `Accountmng` (un thread) che condividerano: 

```java
public class Accountmng extends Thread{
	private account cc; 
	public Accountmng(String nome, Account cc){
		super(nome); 
		this.cc = cc; 
	}
	
	public void run(){
		for (int x = 0; x<5; x++){
			cc.withdraw(200); 
			System.out.println("saldo attuale: " + cc.getBalance()); 
		}
	
	}

}
```





### Oggetto "occupato"
L oswitch context operato dallo skeduler non tiene conto della logica del metodo prelievo!
Può accadere infatti che dopo il controllo del saldo, l'esecuzione passi ad un altro thread, mentre controllo del saldo e il prelievo dovrebbero costrutire un'operazione atomica
Per ottenere che nessun thread possa invocare il metodo prima che un altro thread abbia finito le operazioni sul conto, si può utikizzare la keyword `synchronized`.
In questo modo l'oggetto conto risulta occupato/bloccato fino alla fine dell'esecuzione del metodo → l'esecuzione del metodo è asincrona ( i thread lavorano uno alla volta!)

### La keyword synchronized
Un metodo sync, invocato su un oggetto, può essere eseguito al massimo da un singolo Thread
Modificando cosi nell'esempio precedente
```
private synchronized void withdraw(int amount); 
```

si ottiene che le operazioni sono consistenti. 
Entrando nel metodo, il thread acquiscie il lock sull'oggetto corrente che invocato il metodo → l'oggetto è bloccato(non il metodo) e nessun altro metodo synchronized può essere invocaro sullo stesso oggetto
Uscendo dal metodo, il thread rilascia il lock e i thread che erano attrsa hanno la chance di invocare il metofo 
Il `synchronized` può essere fatto SOLO per i metodi, non per gli attributi ne per le classi. 
Per le classi si dice che sono Thread-safe se i suoi metodi di accesso sono `synchronized`.
Tornando all'esempio del Account è il metodo `withdraw` a dover essere `synchronized` per evitare di perdere la coerenza tra i diversi thread, e pure se ci andassi a mettere il `sleep` si è certi che non cambi nulla.
Se invece si nconizzassimo `run()` in `Accountmng` vuol dire che il primo Thread(Fred o Lucy) che viene eseguito blocca il run finché non fa i 5 prelievi consententi
Ma il `synchronized` fa usato con parsimonia.
#### Il lock e synchronized
Ogni oggetto ha un solo lock 
Un thread può acquisire più lock, ma su oggetti diversi 
Un thread in `sleep` non perde il lock sugli oggetti 


### A prova di Thread (Thread safe)
Una classe è thread safe se tutti i metodi che accedono a proprieità modificabili dell'oggetto sono stati implementati 


Se il lock non può essere rialsciato ?
Supponiamo che un thread entra in un metodo sincronizzato e ottiene il lock, ma non ci sono le condizioni per poter eseguire il lavoro.
Cosa potrebbe fare? 
Opzione 1: 
- esce dal metodo, eventualemente senza lavorare e rilascia il lock
- Problema: non sappiamo se esce con lavoro fatto o no!
Opzione 2: 
- rimane nel metodo, in attessa che qualscosa cambi, non rilascia il lock
- PROBLEMA: non è detto che la situazione evolva 
	- in questo caso si parla di Theard Starvation(il thread che attende è "affamato" per lungo tempo)
La soluzione è: 
- RImanere nel metodo, senza lavorare e rilasciare il lock
- I metodi che odbbiamo usare son `wait()` e `notify()`; entrmabi metodi della classe `Object`

>[!note] Nota: gli ultimi metodi di papà `Object` servono per la sync.
>Inoltre i metodi in questione (`wait`, `notify`, `notifyAll`) sono metodi [[Costruttori e modificatori#2. Metodi `final`|`final`]]. 

#### `wait()`
Lo chiama il thread che aspetta di avere una notifica.
In sostanza un Thread entra nel metodo sync e vede il metodo `wait()`→ rilascia il lock senza uscire del metodo e peremtte ad altri thread di entrare nel metodo sync ed eseguire le opreazioni e peremtte di completare il lavoro. 

#### `Notify()`
Questo metodo viene usato per inviare un notifica al Thread lasciato in attesa dal metodo `wait()` affinché riprenda l'esecuzione e quindi rilocka l'oggetto e finisce il suo ciclo di esecuzione 