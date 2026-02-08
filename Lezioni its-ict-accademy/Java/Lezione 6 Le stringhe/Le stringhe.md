# Introduzione alle stringhe in Java
Nelle lezioni precedenti abbiamo visto come in Java tutto ruoti attorno agli **oggetti**: abbiamo imparato a [[Java/Lezione 5 Le classi/Le classi#Definizione di una classe|definire classi]], creare oggetti con i costruttori, usare attributi e metodi, gestire i riferimenti e comprendere concetti fondamentali come [[Java/Lezione 5 Le classi/Le classi#La keyword `this`|`this`]], [[Java/Lezione 5 Le classi/Le classi#Overloading dei metodi|overloading]] e [[Java/Lezione 5 Le classi/Le classi#Overriding dei metodi|overriding]]. 
Abbiamo anche visto come il [[Java/Lezione 5 Le classi/Le classi#Incapsulamento|concetto di incapsulamento]] protegga lo stato degli oggetti e renda il codice più robusto, e come le classi possano appartenere a pacchetti per organizzare il codice.

Ora ci spostiamo su un argomento fondamentale per la programmazione: le **stringhe**. 
In Java, le stringhe **NON sono tipi primitivi**, ma: 
- ==**oggetti speciali** della classe `String`.== 
Questo significa che, ==pur comportandosi in molti casi come tipi primitivi (possiamo scriverle direttamente con i literal e concatenarle facilmente), internamente sono sequenze di caratteri immutabili==. 
Ogni stringa è quindi un **array di caratteri** nascosto, e possiamo manipolarla tramite metodi dedicati della classe `String`.

Conoscere le stringhe è essenziale perché quasi tutti i programmi lavorano con testi: nomi, messaggi, input/output, file, ecc. 
Nei prossimi paragrafi vedremo come crearle, inizializzarle, concatenarle e gestire i riferimenti, prestando attenzione a concetti chiave come **immutabilità** e gestione di `null`.


## Le stringhe in Java

==Le **stringhe** in Java sono oggetti della classe `String`==.  
È importante ricordare che **i caratteri (`char`) non sono stringhe** e viceversa: 
- ==la classe `String` serve a rappresentare **sequenze di caratteri**, cioè testo alfanumerico==.

Internamente, una stringa è costituita da un **array di caratteri**, ma viene trattata “quasi” come un tipo primitivo, perché Java permette di usarla in modo semplice e immediato.

> [!done] **Vantaggi principali delle stringhe in Java:**
> 
> 
> - ==Si possono creare direttamente senza usare `new` (costruzione implicita)==.
>     
> - ==La concatenazione è immediata usando l’operatore `+`==.
>     
> - ==È possibile aggiungere testo a una stringa esistente con l’operatore `+=`==.


**Esempi di costruzione di stringhe:**
```java
// Costruzione implicita tramite literal
String s = "hello";       

// Costruzione tramite array di char
char[] temp = {'h','e','l','l','o'};
String stringa = new String(temp);  

// Costruzione tramite costruttore
String a = new String("parola");  
String b = "parola";               // equivalente assegnamento da literal

// Stringa vuota
String empty = "";                 

// Riferimento a null
String str = null;                

// Attenzione: invocare metodi su null genera eccezione
System.out.println(str.length());  // NullPointerException
```

> [!NOTE] **Nota:**
>  anche se possiamo assegnare `null` a una stringa, ==finché non viene creata un’istanza vera e propria, non è possibile invocare i metodi della classe senza generare un errore.==

### Concatenazioni delle stringhe
In Java, le stringhe si possono unire tra loro usando l’**operatore `+`** oppure il metodo `concat()`.
Esempio:
```java 
String s = "hello";
s = s + " world";       // concatena " world" alla stringa s
// equivalente a:
s = s.concat(" world");

```

Un’alternativa più compatta è usare l’operatore `+=`:

```java
String s = "hello";
s += " world";          // equivale a s = s + " world";

```

> [!warning] **Attenzione alla memoria:** 
>  
> Anche se sembra che la stringa originale `s` venga modificata, in realtà le stringhe in Java sono **immutabili**, cioè non possono cambiare una volta create.  
> ==Quando si concatena o modifica una stringa, Java crea **una nuova stringa in memoria** e `s` ora punta a questa nuova zona di memoria.==

```java
String n = "Immutabile";
String maiuscolo = n.toUpperCase();

System.out.println(maiuscolo);  // stampa "IMMUTABILE"
System.out.println(n);          // stampa ancora "Immutabile"
```

In questo caso:

- `n` continua a puntare alla stringa originale `"Immutabile"`.
    
- `maiuscolo` punta a una **nuova stringa** `"IMMUTABILE"`.
    

Quindi tutte le operazioni sulle stringhe generano nuovi oggetti, lasciando intatto il valore originale. Questo è un concetto chiave da ricordare quando si lavora con le stringhe in Java.

### Metodi di lettura 
Per **leggere o estrarre informazioni da una stringa**, Java mette a disposizione alcuni metodi molto utili. 
Supponiamo di avere la seguente stringa:
```java
String s = "amazing";
```

1. `length()`: 
	- Restituisce la lunghezza della stringa, cioè il numero di caratteri che contiene.
```java
int l = s.length();  // output: 7
```

2.  `charAt (int i)`: 
	   - Permette di accedere al carattere che si trova in una determinata posizione della stringa.  

> [!remember] Ricorda che gli indici partono da **0**, quindi il primo carattere è alla posizione 0.
>

```java
char c = s.charAt(2);  // output: 'a' (il terzo carattere)
```

3.  `substring(int i)`: 
	   - Restituisce una **sotto-stringa** a partire dalla posizione indicata fino alla fine della stringa.
```java
String ss = s.substring(3);  // output: "zing" (dalla posizione 3 in poi)
```

### Metodi di ricerca nelle stringhe
Java mette a disposizione diversi metodi per **trovare la posizione di caratteri o sottostringhe** all’interno di una stringa.
Supponiamo di avere:
```java
String s = "amazing";
```

1. `indexOf(char c)`: 
	- Restituisce l’indice della **prima occorrenza** del carattere `c`.
```java
int i = s.indexOf('m');  // output: 1
```

2. `indexOf(char c, int i)`: 
	- Restituisce l’indice della prima occorrenza del carattere `c`, **a partire dalla posizione `i`**. 
```java
int i = s.indexOf('a', 1);  // output: 2
```

3.  `lastIndex(char c)`: 
	   - Restituisce l’indice dell’**ultima occorrenza** del carattere `c`.

```java
int i = s.lastIndexOf('a');  // output: 5
```

Questi metodi sono molto utili quando dobbiamo cercare caratteri o sottostringhe senza scorrere manualmente l’array di caratteri sottostante.
### Parsing delle stringhe in numeri
==Spesso in Java capita di avere **stringhe che rappresentano numeri** e di doverle **convertire** in un tipo numerico per poter fare calcoli==. 
Questo processo si chiama **parsing**.

Java mette a disposizione dei metodi pronti nelle classi wrapper come `Integer` e `Double`:

- `Integer.parseInt(String) :int` 
	- ==Converte una stringa in un intero (`int`).==
```java
String numero = "42";
int n = Integer.parseInt(numero);  // n == 42
```


> [!warning] **Se la stringa non rappresenta un numero valido, viene generata un’eccezione `NumberFormatException`.**



2. `Double.parseDouble(String): double`
	- ==Converte una stringa in un numero con virgola mobile (`double`).==
```java
String valore = "3.14";
double d = Double.parseDouble(valore);  // d == 3.14
```
Anche qui, se la stringa non è un numero valido, viene sollevata una `NumberFormatException`.
Questi metodi sono fondamentali quando leggiamo input da console o file e vogliamo trattarlo come valori numerici.
### Confrotro fra stringhe
Nella classe String sono disponibili: 
- boolean equals (String anotherString)
	- torna `true/false` se il contenuto delle Stringhe è uguale/diverso. 
- `int compareTo(String anotherString)`: 
	- confronta le stringhe rispetto all'ordine alfabetico 
L'istruzione `s == t` fa un confrono tra riferimenti 
Due riferimenti uguali "puntano" alla stessa stringa 
Due stringhe uguali potrebbero non avere lo stesso riferimento.
Quindi l'operatore `==` sulle stringhe confronta le reference mentre il `equals` fa un confrotno più profondo: 
confronta partendo dal primo carattere fino all'ultimo e vede se coincidono tutti i caratteri delle due stringhe 

Il compareTo torna un intero: se torna 0 le stringhe sono uguali (ad esempio per un palindromo)
poi `>0`: se la stringa che chiama è maggiore del parametro (`this>parametro`)
- `<0`: se la stringa che chiama è minore del parametro(`this<parametro`). 