
Gli array in Java sono un tipo speciale che aggrega un gruppo di variabili dello stesso tipo.
In java gli array sono oggetti e non primitivi!
La loro dimensione è fissa, viene stabilita in fase di creazione e non può mutare

Una variabile array deve indicare il tipo di variabili che conterrà (primitivi o oggetti)
SI può definire 
```java
int[] arrayOfInt; // stile più usato
int arrayOfInt; // vecchio stile (C like)
```
Ovviamente questo può essere scomodo perché immagine il carello di un e commerce, se si usessero gli array classici avremo un tetto massimo di prodotti da mettere dentro inoltre i prodotti possono essere di diversi tipi. 

Gli array classici non possono avere tipi diversi; nell esempio sopra abbiamo dichiarato un array di interi quindi non potra storare altri tipi di dati.
Per indicare il tipo devo infatti prima mettere il tipo di dato seguito dalle parentesi quadre (`[]`)
```java
int[] arrayOfInt; 
String[] arrayOfInt; 
float[] arrayOfFloat; 
//e così via...
```
Un array può essere una matrice di array a sua volta. 
```java
int[][] arrayOfArrayInt; 
```
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
