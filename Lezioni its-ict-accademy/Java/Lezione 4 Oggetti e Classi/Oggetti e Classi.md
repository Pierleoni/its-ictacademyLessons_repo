# Object Oriented Programming 
Abbiamo lavorato sugli array e visto la sintassi di base, oggi vedremo le classi e oggetti. 

## Approcci 
Un paradigma di programmazzione è uno stile di programmazione.
È costituito da un insieme di elementi concettuali utilizzati dal progettista e poi da programmatore per la realizzazione di un programma. 
Definisce il modo in cui si modella, si concepisce e si realizza il rpgramma.
I principali paradigmi della programmazione sono: 
- procedurale (o funzionale)
- OOP 
L 'approccio che scegliamo  condiziona tutta la parte centrale del ciclo di vita del software, dall'analisi all'implementazione.
Quindi l'approccio non è solo un modo di scrivere il codice ma come lo progetti. 
![[approcio.png]]

Quindi perchè sono solo due gli approcci? 
La programmazione si riduce ai dati e alle funzioni, quindi questi due aspetti sono principali e complementari tra loro.
Il primo paradigma pone le funzioni come protagonisti e i dati sono i parametri delle funzioni
Mentre nell'OOP i dati sono i protagonisti e le funzioni sono subordinati ai dati: 
le funzioni non possono eseguire nulla se non si è definito l'oggetto.
Per questo è improbabile che nascera un terzo paradigma.
Storicamente il paradigma procedurale è stato il primo ad essere nato, perché la logica funzionale è più vicino alla macchina e al linguaggio macchina. 
Anche quando si passo al linguaggio funzionale era ancora a baso livello ma per capirli serve un certo livello di astrazione da parte del programmatore. 
Mentre un linguaggio oggetti è più smeplice da comprendere perché il modno è popolato da entità (es: Persona, Animale, etc.)
Quindi un paradigma di programmazione non è un solo di pensare ma nacnhe un modo per agire seguendo questi dictact. 
### Esempi funzionali e orientato agli oggetti
Per la scomposizione funzionale prendiamo ad esempio l'applicativo di Amazon
Le prime domande da porsi: 
- Quali sono le funzioni principali ? 
	- Quali sono le sotto-funzioni?
Mentre l'OOP non ragiona per funzione: 
- si parte dai protagonisti del problema 
- SI individuano le caratteristiche 
- Si individuano le funzionalità 
Quindi ripartendo da Amazon e contiuamo a procedere con l' approcio OOP 
- Quali sono i protagonisti principali? 
	- Come sono fatti? → caratteristiche 
	- QUali azioni compiono? →comportamenti/funzioni
Le ultime due sono le specifiche della prima domanda

### Classificazione 
L'analisi ad oggetti passa attraverso il processo di classificazione: 
tutti gli oggetti che hanno stesse caratteristiche e stesse funzionalità appartengono ad una stessa categoria 
Una classe quindi è il frutto del lavoro della classificazione e rappresetna una categoria di oggetti concreti del dominio. 
È quindi una astrazione di oggetti concreti del dominio; ad esempio in Amazon i venditori sono una classe astratta di entità concrete del dominio 

### Classe e oggetto
QUando si descrive un oggetto ci si riferisce sempre alla sau classificazione 
Per usare un oggetto, ho bisogno di un rappresentante della categoria 
#### Esempio: 
Non dico _"questa penna scrive"_, 
ma _"Le penne servono per scrivere"_
Poi se 


### Costruzione delgi oggetti 
Il passaggio dalla classe (concetto astratto) all'oggetto (aspetto concreto) si realizza tramite una speciale funzione della classe → metodo costruttore
Un programma OO quindi manipolerà oggetti e agirà unicamente su di essi 

Le classi si possono anche vedere come _"fabbriche di oggetti "_ che 
- definiscono l'interfaccia delgi oggetti verso il mondo esterno
- ma ne nascondono l'implementazione (incapsuland dati e funzionalità degli oggetti che istanziano)
Quindi l'analista vede gli oggetti e produce il diagramma UML delle classi 
Il programmatore vede le classi fatte dall'analista e tramite il costruttore itanzian gli oggetti della classe. 
Il memtodo costruttore genera l'oggetto(lo mette in memoria) e lo inizializza.
Ad esempio in Java
```java
public class Studente{
	
}
```

Questo dichiara la classe pubblica `Studente`. 
Quindi la classe ha anche il meccanismo di fabbricazione (il costruttore) ma ha anche l'aspetto di definire i comportamenti degli oggetti (metodi della classe). 

I metodi sono funzioni e si chiamano cosi perché sono le funzioni che appartengono alla classe, in Java un metodo non non appartente ad un classe come ad un Cliente appartiene il metodo cambiaPassword. 
### Nuovo approccio 
![[nuovo approcio.png]]

### Natura degli oggetti 
Tutti gli oggetti di una stessa classe hanno una struttura analoga (attributi) e un comportamento analogo(metodi)(solo in Java non in Python). 
La creazione dell'oggetto è sempre a carico del programmatore
La distruzione è spesso automatica(ma dipende dal linguaggio).
L'oggetto non conitene i metodi della classe ma solo i dati (attributi), in più una volta istanziato l'oggetto non può non avere attributi undefined. 
### Stato dell'oggetto 
Ogni oggetto memorizza dati indipendenti che rappresentato il suo stato 
Durante la vita dell'oggetto, il suo stato può variare, perché possono cvariare i valori dei suoi attributi
	- Il modo in cui può variare è stabilito dalla classe 
Due oggetti (istanze di una stessa classe) possono avere gli stesi valori 

### Inventare i tipi 
In OO è possibile quindi definire i propri tipi di dati, defininendone la struttura e aggiungendo le funzioni a runtime. 
I nuovi tipi potranno poi essere riusati anche in altri programmi 
Prorpio come nella realtà, gli oggetti hanno un identità dei comportamenti e uno stato. 


### Le refenrce 
Per accedere agli oggetti e manipolarli si usano i riferimenti → puntatori a basso livello verso l'oggetto
Le reference sono i telecomandi degli oggetti 

Esempio: la classe Data della libreria modella una data intesa come istante di tempo (data e ora)
Se scrivo 
```
Date dataNascita;
```

Dichiaro una variabile che può fare riferimento ad oggetti della classe Date 
- dataNascita è una reference di tipo `Date` 
- dataNascita non è un oggetto

### Chiamata al costruttore 
Per creare un oggetto occore: 
- l'operatore `new`
- seguito dal metodo costruttore
Esempio: 
```java
Date d = new Date();
```

Cosi si crea un'istanza di Date con la data di sistema e la assegna alla reference d.
Ora d fa riferimento all'oggetto Date appena creato, adesso si possono chiamare i metodi relativi 
```java
d.setMonth(3); //setta il mese a Aprile; i mesi sono storati in uan sorta di array quindi zero-index 
int d = d.getDay() // torna il giorno della settimana in numero non stringa(anche qui da 0(domenica) e 6(sabato))
```


### Regole dei costruttori 
Tutte le classi hanno sempre un costruttore 
Una classe spesso precede diversi costruttori 
I costruttori sono funzioni speciali che seguono delle regole formali e sono facilemente individuabili nella classe 
	- In java il costruttore porta sempre il nome della classe e non dichiara alcun tipo di ritorno. 
I costruttori hanno lo scopo di inizializzare l'oggetto cioe tutti i suoi attributi 
In relata se il costruttore se non viene dichiarato nel momento della compilazione nel file .class viene assegnato un costruttore di defualt ma se ne dichiariamo uno graficamente nel codice allora nel .class non verra messo uno costruttore di default (o per meglio dire di disperazione/emergenza).
