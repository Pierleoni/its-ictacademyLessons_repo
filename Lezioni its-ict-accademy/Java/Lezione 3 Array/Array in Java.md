
# Introduzione
Fino a questo punto abbiamo visto come [[Lezione 2 - Sintassi e costrutti di base#Dichiarazione delle variabili|dichiarare variabili]] di tipo primitivo e oggetti, gestire lo **[[Lezione 2 - Sintassi e costrutti di base#Scope (ambito) delle variabili|scope]]**, usare cicli e strutture condizionali. Tuttavia, molto spesso capita di dover memorizzare **più valori dello stesso tipo** e di volerli gestire in modo ordinato e indicizzabile.
## Gli array in Java 
In Java, questo compito è svolto dagli **array**, un tipo speciale di struttura dati che permette di raggruppare più variabili dello stesso tipo sotto un unico nome.  
Gli array in Java hanno alcune caratteristiche fondamentali:

- ==Sono **oggetti**, non tipi primitivi, anche quando contengono valori primitivi.==
    
- ==La **dimensione** dell’array è **fissa** e viene definita al momento della creazione.== 
	- Non è possibile modificarla successivamente.
    
- ==Ogni array contiene valori **omogenei**, cioè dello stesso tipo, che può essere sia un tipo primitivo (`int`, `double`, `boolean`, ecc.) sia un oggetto.==



### Dichiarazione degli array
Per dichiarare un array, bisogna indicare:

1. Il **tipo di elementi** che conterrà
    
2. Il nome della variabile array
    

Esempi di dichiarazione:
```java
int[] arrayOfInt;    // stile più moderno e consigliato
int arrayOfInt[];    // stile "vecchio", simile al C
```

- La prima forma (`int[] arrayOfInt`) è:  
	- ==quella **più usata in Java moderno** ed è più chiara, perché indica subito che si tratta di un array di `int`.==
    
- La seconda forma (`int arrayOfInt[]`): 
	- ==viene ereditata dal linguaggio C e funziona ancora, ma oggi è considerata meno leggibile.==

Gli array classici hanno alcune limitazioni importanti:

- **Dimensione fissa**: 
	- ==una volta creato, un array può contenere solo un numero prestabilito di elementi.== 
	- Ad esempio, se immaginiamo il carrello di un e-commerce, usare un array classico significherebbe avere un “tetto massimo” di prodotti.
    
- **Tipi omogenei**: 
	- ==tutti gli elementi devono essere dello stesso tipo==. 
	- ==Non è possibile inserire interi, stringhe e oggetti diversi nello stesso array.==
    

Per definire un array, si scrive prima il tipo di dato seguito dalle parentesi quadre `[]`:
```java
int[] arrayOfInt;
String[] arrayOfString;
float[] arrayOfFloat;
```

Gli array possono anche essere **multidimensionali:** 
- ==cioè contenere a loro volta altri array==, come nel caso delle matrici:
```java
int[][] matrix;   // matrice di interi
```


In sintesi, un array in Java è :
- ==**un contenitore ordinato di elementi omogenei**, indicizzabile tramite numeri interi==
e rappresenta un passo importante verso strutture dati più complesse come **liste, matrici e collezioni** che vedremo in seguito.
### Creare un array
Per creare un array si utilizza l'operatore `new`: 
```java
int[] array = new int[100]; //crea un array che contiene 100 numeri interi
```
Cosi pero la istanzaiato: è andato in memoria ed ha allocato 100 int in memoria. 
Inoltre la gia inizializzato con i valori di defualt: 
0 per i tipi int e float 
Quindi prima di un'asseganzione tutti gli elementi sono zero, se sono numeri
sono rifierimenti a null, se sono oggetti
Una forma abbreviata di costruzione e inizializzazione: sintassi di array anonimo
```java
int[] smallPrime = {2,3,5} //ometto la new
```

L'array anonimo si usa quando si sa quanti sono gli elementi e quali sono. 
Un esempio può essere l'array con i giorni della settiamana. 
Difatti in un array anonimo è utile quando deve contenere costanti e non variabili mutabili. 
### Accesso agli elementi 
Gli elementi sono accessibili mediante indice 
Per convenzione gli indici sono da 0 a (liunghezza -1)
L'accesso all'elemento contenste di leggerlo, stamparlo e modificarlo.
```
for (int i=0; i<100; i++0)
	array[i] = i;
```
Tuttavia  utilizzare un array senza averlo creato, generare un errore di compilazione(oltre che logico)
```java
int[] array; 
array = 3
```

### Proprieta length 
Questa proprietà è la lunghezza fissata di un array si può leggere accedendo alla proprietà length secodno la sintassi 
```java
nomeArray.length
```
QUesta proprietà e read-only. 

#### Stampare un array
Sebbene l'array sia un oggetto la stampa tramite printIn non stampa gli elementi, ma stampa solo una locazione di memoria
Per visualizzaee gli elementi bisogna stampari uno alla volta tramite un loop
```java
for (int i = 0; i<array.length; i++)
{
	System.out.println(array)

}
```


#### Il cpstruttore forEach
Come in JS, è l'evoluzione del costrutto for
Viene usato usato per scorrere gli elementi di un Array 
Non bisonga definire ne incrementare l'indice
```java
int[] giorniMese = {31,28,30}
for (int giorni: giorniMese){
	System.out.println(giorni);
}
```

Il limite del forEach, come in JS, è che si scorre dalla posizione 0 fino alla posizione n-1 socrrendo tutti gli elementi della lista uno per uno.

### Sfondamento
Se si tenta di accedere ad un elemento chwe non esiste, cioè fuori da range, si avra un errore di run-time 
```shell
ArrayIndexOutOfBoundsException
```


### Array multidimensionali
In Java si possono creare array multidimensionali: essi sono modellati come array di array 
Si può creare un array di array qualsiasi dimensione (2,3,4...n)
Per ogni dimensioni bidogna specificare il valore 
Per modelallrw una matrice dimensioni(2), bisonga indicare il numero delle righe 
#### Accesso elementi
La proprietà lenght di una matrice è il valore della prima dimensione 
Nel caso di una matrice si riferisce alla lunghezza dell'array di array, cioè al numro di righe 
```
for (int i = 0; j<matrix.length; i++)
{
	for (int j = 0; j<matrix[i].length; j++)
	{
		System.out.println()
	}
}
```
