
## Task e MultiTasking 
Un processo è un programma in esecuzione(o una parte di esso).
Per multitasking o multithreading simula il parallelisom di esguire più processi contemporanemente sulla CPU o su più CPU.
Questo processo è eseguito dallo sckeduler: 
- è il componente del sistema operativo che si occupa di decidere come distribuire l'accesso alla CPU per eseguire i processi →come eseguire il contenxt switch 

Le caratteristiche del multitasking: 
- ogni processo ha un proprio spazio indirizzato nella memoria RAM 
- La comunicazione tra processi è complessa ed è a carico del SO. 
I thread li possimao pensare come processi indipendenti che pero lavorano insieme per arrivare a porteare a casa un certo risultato.
### Thread
Un thread è un flusso di esecuzione all'inetro di un processo. 
Per ora abbiamo fatto solo processi mono-thread ovverro programmi che esguivano solo il processo principale, ma dall processo principael posso eseguire processi paralleli. 
Quindi un processo può avere un solo thread(mono-thread)
oppure potrebbe avere più sotto flussi (multithread). 
Quindi i thread sono indipendenti ma collaborano tra loro.
In oltre ogni processo ha almeno un thread principale, che può dare origine a quelli secondari, e ogni thread si possono ordinare in base alla priorità.
Lo skeduler non viene pilotato da noi, il programattore organizza i flussi ma non li esegue in base alla priorità. 

### Multithreading
Rappresenta la possibilità di eseguire più processi "contenmporaneamente" (la vera contemporaneata avviene solo quando si hanno più processori). 

Quindi piccole untià di calcolo relative ad uno stesso programma vengono eseguite in modo quasi simultaneo. 

Risultato → aumentare la velocita di calcolo e l'efficienza 

Le caratteristiche sono 
- Thread diverse girano nello stesso spazio di memoria ([[Sinta|JAVA Heap]]).
- La comunicazione efficiente (memoria condivisa) ma potenziali problemi di sincronizzazione (per l'accesso a oggetti condivisi). 
### Come viene fatta la schedulazione
Questo criterio dei thead della JVM è il preemptive- priority scheduling
che sfurttta la priorità, l'ordine di arrivo e il time slicing. 
Ogni thread ha una priotià (valore 1 e 10) e un tempo di arrivo (istante di tempo in cui il thread risulta pronto all'esecuzione, cioè Runnable).

Quindi ogni thread, anche il principale, ha la stessa priorità anche dei thread principali. 
Ma il thread che arriva prima anche con priorità più bassa viene eseguito prima di un thread che arriva dopo con priorità più alta.
Come lavora lo scheduler in Java? 
1. Vnegono schedulati tutti i thread runnable e viene stabilito un intervallo di tempo adella CPU per ciadcun thread(Time slicing).
2. IL thread a priorità più alta viene mandato in esecuzione (priority)
3. Lo switch context può avvenire se 
	1. sopraggiunge un thread a priorità più alta 
	2. Il thread è stato interotto (o terminato il task) oppure
	3. Lo slot di tempo assegnato 

### Il thread main 
Il metodo main gira anch'esso in un thread chiamato thread principala (main thread).
Dal main possiamo lancare thread secondari 
- I nuovi thread lavorano in parallelo tra loro e rispetto al main stesso 
- Ognuno cerca di completare il proprio lavoro, interagendo eventualemente con gli altri 
### Classi di supporto nella libreria di Java
Per inciso il multithreading si fa con qualsiasi tipo di linguaggio non solo con Java.

Le API di base a supporto del multiithreading sono tutte nel package `java.lang` e sono: 
- `interface Runnable`
- `class Thread`
- `class Object`

- Runnable: definisce il funzionamento di un thread 
	- Dentro runnable c'è un solo metodo astratto, quindi è un interfaccia funzionale 
- Thread : classe concreto, fornisce metodi per creare e gestire thread 
- Object: fornisce i metodi per la sincronizzazione degli acessi ai thread
	- Serve per i problemi di sincronizzazione 

### Creare un thread 
Il comportamento di un thread è definito, quindi dall'Interfaccia Runnable
```
public interface Runnable{
	public void main()
}
```

La classe Thread è un implementazione di Runnable 
- fornisce strumenti per gestione dei thread (creazione inclusa)
- Implemnte `run()`, il quale per on on esegue nulla (anche se in realta non è vuoto ).
Quindi un thread comporta eseguire una della 2 tecniche: 
- estendere la classe Thread 
- Implementare l'interfaccia Runnable 

### Classe Thread 
Rappresenta il sotto processo
I costruttori sono 
- `Thread()`
- `Thread(Runnable target)`
- `Thread (Runnable target, String name)`
- `Thread(String name)`
Quando 

I metodi sono: 
- `getName()`: torna il nome del threwad
- `setName(String name)`: imposta il nome del thread
- `currentThread`: metodo statico; torna il thread corrente. run
#### Utilizzo di Thread 
passo 1 : estendete la classe `java.lang.Thread`
passo 2 : ridefiniere il metodo `run()`
passo 3 : creare il thread e avviarlo con `start()`
Start è il metodo che inizializza e avvia il thread mentre run è il metodo che runna il thread e viene prima preparato e chiamato dentro start.

Questa maniera indiretta di chiamare i metodi in questo modo si cjhima *Inversione di controllo (IOC)* 
### Schema 
```java
class MyThread extends Thread{
	...
	public void run(){...}; 
	...
}
```

Nel main; 
```java
myThread tr = new MyThread(); 
tr.start(); 
```

### Avviare un Thread 
Dopo la chiamata al costruttore il Thread non è già un thread of execution, infatti bisogna avviarlo con il metodo `start()`

Il metodo `Thread.start()`: 
- Crea le risorse di sistema necessarie per eseguire il thread 
- Schedula il thread per eseguirlo 


#### esempio
Omettendo la chiamata a `start()` il programma 



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