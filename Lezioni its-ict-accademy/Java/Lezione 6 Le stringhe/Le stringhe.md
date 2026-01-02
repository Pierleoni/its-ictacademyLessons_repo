
Le stringhe sono una classe, i caratteri non sono stringhe e le struinghe non sono caratteri
Quindi questa classe modella le sequenze alfanumeriche 
Una stringa è costituita da un array di caratteri 
Sono oggetti speciali e vengono trattati "quasi" come tipi primitivi : 
Perchè in  realta sono tipi base 
I vantaggi principali sono: 
- Costruzione implicita, senza la `new`.
- Concatenazione con operatore `+`
- Incremento con `+=`
Costruzione 
```java
String s = "hello"; //equivale a 
char[] temp = {'h','e','l','l','o'};
String stringa = new Stringa (temp); 

String a = new String("parola") //tramite costruttore
String b = "parola"; //tramite assegnamento di un literal


String empty = ""; //costruisce una stringa vuota 

//Inizializza il riferimento a null
String str = null; //non si possono invocare metodi 

//Invocando su null, genera NullPointerExcpetion
System.out.println(str.length());
```

### Concatenazioni 
Hanno un solo operatore:  `+`. 
Le stringhe si possono concatenare con altre strighne o con altre variabili. 
```java 
String s = s +"world"; //ewuivale a
String s = s.concat("world"); 
```

Una variazione sul tema è : 
```java
String s += "world"; //equivale a 
String s = s +"world"; //equivale a 
String s = s.concat("world"); 
```

Quindi in memoria s ad esempio punta a "hello" e quando la concateno a world a noi smebra che sia evoluta ma in realta s punta a un nuovo riferimento di memoria dove c'è la stringa "helloworld". 
Le stringhe sono immutabili quindi non possono essere cambiate. 

```
String n = "Immutabile"; 
String maiuscolo = n.toUpperCase(); 
System.out.println(maiuscolo);
System.out.println(n); 
```

La stringa qui non viene modificata ma viene cambiata e rigenerata una nuova stringa. 
Quindi n punta alla zona di memoria dove si trova "immutabile" ma maisucolo punta a una zona di memoria dove c'è la stringa `"IMMUTABILE"`. 

### Metodi di lettura 
Supponiamo di avere `String s = "amazing"`
- length(): ritorna la lunghezza (int) della stringa 
```
int l = s.length(); //output: 7

```

- `charAt (int i)`: ritorna il carattere (char) nella posizione i-esima (il primo occupa la posizione `0`)
```
char c = s.charAt(2); //Output: 'a'
```
- `substring(int i)`: ritorna la sotto-stringa partendo dalla posizione i-esima
```
String ss = s.substring(3); // i == 2
```

### Metodi di ricerca 

- indexOf(char c): ritorna l'indice (int) della prima ooccrenza del carattere c 
```java
int i = s.indexOf('m'); //i==1
```

- `indexOf(char c, int i)`: ritorna l'indice (int) della prima occorenza del carattere c partendo dalla posizione i-esima 
```
int i = s.indexOf('a', 1); //i==2
```

- `lastIndex(char c)`: ritorna l'indice (int) dell'ultima occorenza del carattere c 
```
int i = s.lastIndexOf('a'); // i==2
```


### Parsing 
Spesso capita di dover trasformare (convertire una stringa) in un numero. 
Per fare cio esistono metodi di parsing `Integer` e `Double`

- `Integer.parseInt(String) :int` 
	- Trasofmra da String a int (se non puo sollevare un eccezzione)
- `Double.parseDouble(String): double`
	- Trasforma da String a double (se non può sollevare eccezione)

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