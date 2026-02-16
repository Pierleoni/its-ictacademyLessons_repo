
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