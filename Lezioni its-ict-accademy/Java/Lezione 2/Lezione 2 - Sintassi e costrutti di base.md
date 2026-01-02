
# Introduzione

[[Lezione 1 - Introduzione a Java|Nella lezione precedente]] abbiamo visto una panoramica su **Java**, le sue caratteristiche principali e i motivi per cui, dagli anni ’90 a oggi, è diventato uno dei linguaggi più utilizzati.

Ora ci concentreremo sul **linguaggio vero e proprio**, analizzando la sua sintassi e i costrutti di base.

## Sintassi e costrutti di base

Come tutti i linguaggi di programmazione, anche Java segue precise **regole di sintassi**. Rispetto a [[Introduzione a Python|Python]], Java ha uno stile più simile al **C** ed è un linguaggio **fortemente tipizzato**, il che significa che ogni variabile e ogni funzione devono dichiarare esplicitamente il tipo di dati che utilizzano.

In altre parole, Java richiede maggiore rigore rispetto a Python, dove è possibile scrivere codice in modo più flessibile. Questa struttura più rigorosa permette però di prevenire molti errori a tempo di compilazione e rende il codice più chiaro e sicuro.

Nei paragrafi seguenti esploreremo i principali **costrutti del linguaggio Java**, partendo dalle basi fino alle funzionalità più avanzate.

### Il metodo `main` in Java

A differenza di **[[Introduzione a Python|Python]]**, dove è possibile scrivere codice direttamente nel file senza doverlo inserire in una funzione specifica, in **Java** il **metodo `main`** rappresenta l’**entry point della JVM**. Questo significa che l’esecuzione di un programma Java inizia sempre dal metodo `main`.

Un esempio di struttura di base di un programma Java:

```java
public class Prova {
    public static void main(String[] args) {
        // istruzione1
        // istruzione2
    }

    // altre funzioni
    funzione1();
    funzione2();
}
```

Alcuni punti importanti:

- Tutte le istruzioni e le funzioni devono essere **definite all’interno di una classe**, perché in Java non esistono funzioni libere come in Python.
    
- Il metodo `main` deve avere **questa esatta firma**: `public static void main(String[] args)`
    
    - `public` indica che il metodo è accessibile alla JVM dall’esterno.
        
    - `static` significa che il metodo può essere eseguito senza creare un’istanza della classe.
        
    - `void` indica che il metodo non restituisce valori.
        
    - `String[] args` permette di passare eventuali **argomenti da linea di comando**.
        

In sintesi, il metodo `main` è fondamentale per avviare un programma Java e tutte le istruzioni devono essere strutturate all’interno della classe a cui appartengono.

### Stile di codifica in Java

In Java, lo **stile di codifica** è importante per rendere il codice leggibile e comprensibile, sia per il compilatore sia per chi legge il programma. 
Alcune regole fondamentali sono:

- **Spaziature**: 
	- gli elementi del codice devono essere separati da almeno uno spazio, per migliorare la leggibilità.
    
- **Terminazione delle istruzioni**: 
	- ogni istruzione deve terminare con un punto e virgola `;`.
    
- **Organizzazione del codice**: 
	- anche se è possibile scrivere più istruzioni sulla stessa riga, è buona pratica mettere **una sola istruzione per riga**, così il codice risulta più chiaro e facile da mantenere.
    

Seguire queste regole non è obbligatorio per la compilazione, ma aiuta a scrivere codice più ordinato e professionale, soprattutto in progetti condivisi con altri sviluppatori.

### Commenti in Java

In Java esistono diversi tipi di commenti, utilizzati per **annotare il codice** senza influenzarne l’esecuzione:

1. **Commenti su una singola riga**
    
    - Sintassi: `//`
        
    - Tutto il testo che segue `//` sulla stessa riga viene ignorato dal compilatore.

```java
// Questo è un commento su una riga
```

2. **Commenti multilinea**

- Sintassi: `/* ... */`
    
- Permette di commentare più righe contemporaneamente.
```java
/* Questo è un commento 
   su più righe */
```


3. **Commenti Javadoc**

- Sintassi: `/** ... */`
    
- Servono a generare **documentazione HTML standard** tramite lo strumento `javadoc.exe`.
    
- Consentono di aggiungere **tag speciali** per descrivere classi, metodi e parametri.


```java
/**
 * Questa è una classe di esempio.
 * @author Marco
 * @version 1.0
 */
public class Esempio {
    // codice della classe
}
```

I commenti Javadoc sono particolarmente utili per creare documentazione leggibile e professionale, conforme agli standard Java, senza modificare il comportamento del programma.



### Tipi di dato primitivi
In Java i **tipi primitivi** rappresentano i dati di base del linguaggio. 
A differenza di Python dove ogni dato è un oggetto, in Java i tipi di dato primitivi non sono oggetti ma anche qui e costituiscono i mattoni fondamentali per costruire variabili ed espressioni. 
I principali tipi primitivi sono:

1. **[[#Tipi Interi|Interi]]**: `int`, `short`, `long`, `byte`
    
    - Permettono di memorizzare numeri senza decimali.
        
    - Esistono diverse dimensioni perché occupano **diversi spazi di memoria** e consentono di ottimizzare l’uso delle risorse:
        
        - `byte`: 1 byte
            
        - `short`: 2 byte
            
        - `int`: 4 byte
            
        - `long`: 8 byte
            
2. **[[#Tipi in virgola mobile|Virgola mobile]]**: `float`, `double`
    
    - Permettono di memorizzare numeri con **decimali**, utili per calcoli scientifici o approssimazioni.
        
    - `float` occupa meno memoria di `double` e ha precisione minore.
        
3. **Carattere**: `char`
    
    - Memorizza un singolo **carattere Unicode**, come una lettera o un simbolo.
        
4. **Logico**: `boolean`
    
    - Può assumere solo due valori: `true` o `false`.
        
    - Utile per controllare condizioni e flussi di programma.
        

Questi tipi primitivi sono alla base della programmazione in Java e vengono spesso combinati per creare strutture dati più complesse o per definire variabili nelle classi.
#### Tipi Interi (`int`, `short`, `long`, `byte`): 
I tipi interi in Java permettono di memorizzare **numeri senza decimali**. Esistono diverse varianti per ottimizzare l’uso della memoria a seconda delle esigenze del programma:

| Tipo  | Requisiti | Intervallo(inclusivo)                                              |
| ----- | --------- | ------------------------------------------------------------------ |
| int   | 4 byte    | Da -2.147.483.648 a +2.147.483.648                                 |
| short | 2 Byte    | Da -32.768 a +32.768                                               |
| long  | 8 byte    | - - 9.223.372.036.854.775.808L a<br>+ + 9.223.372.036.854.775.807L |
| byte  | 1byte     | Da -128 a +127                                                     |

> [!NOTE] Nota: il suffisso `L` indica che il numero è di tipo `long`.
> 

#### Tipi in virgola mobile (`float`, `double`): 
I tipi a virgola mobile servono per memorizzare **numeri con decimali**, utili per calcoli scientifici o approssimazioni. 
Java distingue tra precisione singola (`float`) e doppia (`double`):

| Tipo   | Requisiti<br> | Intervallo(inclusivo)<br>                                              |
| ------ | ------------- | ---------------------------------------------------------------------- |
| float  | 4 byte        | circa +- 3.40282347E+38 F<br>(6-7 cifre decimali significative)        |
| double | 8 byte        | circa +- 1.79769313486231570E+308<br>(15 cifre decimali significative) |

> [!NOTE] Nota: il suffisso `F` indica che il numero è di tipo `float`.
> 


> [!info] In Java essendoci questa distinzione tra `float` e `double` per numeri decimali si utilizza per lo più il tipo `double` (in Python utilizzavamo solo il `float`, anche perché per rappresentare e memorizzare i numeri decimali esiste solo il tipo `float`)
>

#### Tipo carattere (`char`): 


Il tipo **`char`** in Java rappresenta un **singolo carattere Unicode**, permettendo di memorizzare qualsiasi simbolo o lettera esistente.

- Ogni `char` occupa **2 byte** in memoria.
    
- I caratteri si scrivono tra **apici singoli**:
    

```java
char c1 = 'A';
char c2 = 'a';
char nullo = '\0';     // carattere nullo
char nulloUnicode = '\u0000';  // stesso valore in Unicode
```

##### Sequenze di escape 
Per rappresentare caratteri speciali o non stampabili, Java utilizza **sequenze di escape**. Alcuni esempi comuni:

| Sequenza | Nome               | Valore Unicode |
| -------- | ------------------ | -------------- |
| `\b`     | backspace          | `\u0008`       |
| `\t`     | tabulazione        | `\u0009`       |
| `\n`     | nuova riga         | `\u000a`       |
| `\r`     | ritorno carrello   | `\u000d`       |
| `\"`     | virgolette doppie  | `\u0022`       |
| `\'`     | virgolette singole | `\u0027`       |
| `\\`     | backslash          | `\u005c`       |
Queste sequenze permettono di inserire nel codice caratteri che altrimenti sarebbero difficili da digitare o interpretabili come istruzioni speciali.


#### Tipo logico (`boolean`)

Il tipo **`boolean`** rappresenta un valore logico, che può assumere solo due possibili stati:

- `true` (vero)
    
- `false` (falso)
    

Al contrario di `char` o stringhe, i valori booleani **non richiedono apici né virgolette**.
```java
boolean flag = false;
boolean attivo = true;
```
I valori booleani sono utilizzati principalmente nelle **istruzioni di controllo di flusso**, come `if`, `while` e `do`, e sono spesso il risultato di **operatori comparativi**:
```java
int a = 5;
int b = 10;
boolean confronto = (a < b); // true
```

In questo esempio, l’espressione `(a < b)` restituisce un valore booleano (`true`), che può essere usato per decidere l’esecuzione di determinate parti del programma.

> [!faq] Perché le stringhe non sono tra i tipi di dato primitivi in Java 
> In Java le **stringhe** non sono tipi primitivi, ma **oggetti**.  
>In molti linguaggi (come C o C++) le stringhe possono essere trattate come tipi primitivi, mentre Sun e Oracle hanno deciso di implementarle come **classi**, per offrire maggiore flessibilità e funzionalità.  
>Il tipo primitivo di base per i caratteri singoli rimane il **`char`**.  
>In linguaggi come Python, invece, tutti i tipi, compresi quelli numerici e le stringhe, sono oggetti, quindi il concetto di tipo primitivo non esiste allo stesso modo.


### Dichiarazione delle variabili

In Java **tutte le variabili devono essere dichiarate esplicitamente** prima di poter essere utilizzate.  
La dichiarazione di una variabile è composta da due elementi fondamentali:

- **il tipo**, che specifica quale genere di dato la variabile può contenere
    
- **l’identificatore**, cioè il nome della variabile
```java
int maxValoreCalcolato;
```
In questo esempio:

- `int` è il **tipo**
    
- `maxValoreCalcolato` è l’**identificatore**

#### Regole per gli identificatori

Gli identificatori in Java devono rispettare alcune regole sintattiche:

- sono **case-sensitive** (`valore` e `Valore` sono variabili diverse)
    
- possono contenere **lettere, numeri, `_` e `$`**
    
- **non possono iniziare con un numero**
    

> [!done] **Esempi validi:**
>```java
int valore1;
int _contatore;
int $somma;
>```
> 


> [!failure] **Esempi non validi:**
>```java
> int 1valore;   // errore
>
>```

#### Convenzioni di denominazione

Oltre alle regole obbligatorie, Java segue alcune **convenzioni di stile** per migliorare la leggibilità del codice:

- l’identificatore inizia sempre con una **lettera minuscola**
    
- se il nome è composto da più parole, si utilizza la **camelCase** (prima parola minuscola, le successive con iniziale maiuscola)
    

Esempio:
```java
int maxValoreCalcolato;
```

Seguire queste convenzioni non è obbligatorio per il compilatore, ma è una **buona pratica** ampiamente adottata nello sviluppo professionale in Java.

### Scope (ambito) delle variabili

In Java, lo **scope** di una variabile rappresenta il suo **ambito di visibilità ed esistenza**, cioè la porzione di codice in cui la variabile è accessibile e può essere utilizzata.

Lo scope è determinato dal **blocco di istruzioni** delimitato dalle parentesi graffe `{ }` in cui la variabile viene dichiarata.

#### Blocchi di istruzioni

I **blocchi di istruzioni** in Java sono delimitati dalle parentesi graffe `{ }` e servono a raggruppare più istruzioni in un’unica unità logica.

Le parentesi graffe vengono utilizzate per delimitare:

- **classi**
    
- **metodi**
    
- **costrutti di controllo** (`if`, `for`, `while`)
    
- **blocchi di codice generici**
```java
{
    // blocco di istruzioni
}
```

Ogni blocco di codice definisce un **ambito di visibilità** per le variabili dichiarate al suo interno. In particolare, una variabile:

- è visibile **solo all’interno del blocco** in cui viene dichiarata
    
- rimane utilizzabile anche dopo eventuali blocchi interni
    
- **cessa di esistere** quando l’esecuzione esce dal suo blocco
    

Quando lo scope termina:

- la variabile non è più accessibile
    
- la memoria associata viene **deallocata**

#### Blocchi annidati e regole sui nomi

In Java **non è consentito dichiarare una variabile con lo stesso nome in un blocco annidato**, se esiste già una variabile con quel nome in un blocco esterno.

Esempio **non valido**:

```java
{
    int a = 10;
    {
        int a = 20; // ERRORE: variabile già dichiarata
    }
}

```

In questo caso, la variabile `a` è già definita nel blocco esterno e non può essere ridefinita in quello interno.

> Nota: in alcuni altri linguaggi di programmazione questo comportamento è permesso, ma **Java lo vieta** per evitare ambiguità e rendere il codice più chiaro e sicuro.

#### Esempio di scope

```java
{
    statement 1;
    statement 2;
    int a;

    {
        statement 3;
        statement 4;
    }

    statement 5;
    a = 10;   // OK: a è ancora nello scope
    statement 6;
}

System.out.println(a); // ERRORE: a non esiste più
```

In questo esempio:

- la variabile `a` è dichiarata nel **blocco esterno**
    
- può essere utilizzata per tutta la durata del blocco
    
- può essere usata anche dopo un blocco interno
    
- **non è accessibile al di fuori del blocco** in cui è stata dichiarata

#### Operatori
`=`: assegnazione 
Artimetici : 
- `+` : somma 
- `-`: sottrazione 
- `/`: la divisione, se gli operando sono interi la divisione è intera ma se uno dei due è floating point il risultato sarà floatign point 
- `%`: ritorna il resto della divsione intera 

Incremento/decremento: 
- `++`: incremento di una unità
- `--`: decremento di una unità
- `+=`: incremento di un valore a scelta 
- `-=`: decremento di un valore a scelta 
- `*=`: moltplico con un valore a scelta 


### Operatori relazionali 
Permettoni il confronto tra due valori che stabiliscono relazioni di ugaglianza e d'ordine 
- `==`: uguale a 
- `!=`: diverso da
- `>`: maggiore 
- `<`: minore
- `>=`: maggiore o uguale 
- `<=`: minore o uguale 


### Operatori booleani
- `||`: OR sc → Short circuit; otimmizza controllo delle condizioni in OR e in AND
- `&&`: AND sc 
- `!`: NOT 
- `^`: XOR; da true se una condizione è vera mentre l'altra no indipendetemente dall'ordine
- `|`: OR
- `&`: AND 

> [!info] Short circuit
> Supponiamo che 
>```java
>int a = 7; 
>int b = 10; 
>//Allora
>(a==7) && (b>0) //→true
>(a==7) || (b>0) //→true
>!(a<4) //→true
>(a==7) ^(b>0) →false
> 
>```

### Controlli di flusso 
1. Istruzioni condizionali
Istruzioni if-else: 
Se ci sono più di una istruzione
```java
if (condizione){
	//istruzione1;
	//istruzione2
}
```

Se c'è una sola istruzione: 
```java
if (condizione)
	//	istruzione;
```

Come in JS anche java non conta l'indentazione.
Se si vogliono mettere più condizioni dopo l'if si usa `else if` 
```java
if (condizione){
	//istruzione1;
	//istruzione2;
}else if (condizione){
	//istruzione;
}else{
	//istruzione
}
```


### Istruzione switch

```java
switch (choice){
	case 1:
		istruz1;
		break;
	case2: 
		istruz2;
		break; 
	case 3:
		istruz3; 
		break;
	case 4: 
		istruz4; 
		break; 
	defualt: 
		//input errato
}
```
Il defualt è l'else, è opzionale 
Anche lui avrebbe il break ma essendo l'ultimo non è obbligatorio

Da java 12 diventa un espressione: può utilizzare la keyword break seguita da un valore
```java
String d = switch(day){
	case "Monday":
		break "Weekday";
	case "Tuesday":
		break "Weekday";
	case "Thursday": 
		break "Weekday"

}
```

Inoltre lo switch può gestire più casi multipli, non si puo utilizzare il range dei valori 
Si utilizza la virgola per separare le costanti 
```
String s=switch (day){
	case "Monday", "Tuesday", "We"
}
```

IE ancora dal java 12 viene introdotto l'operatore arrow (freccia )
### Il blocco `do - while` 
Il while esegue una verifica iniziale
```java
while (condizione)
{
	//blocco instruzione
}
```

Mentre il do-while prima esegue, poi controlla e poi lo riesegue 
```
do 
{
	//blocco istruzioni
	
}
while (condizione); 
```
Da notare il punto e virgola dopo la condizione while: se questa condizione è vera esegue quella istruzione ma logicamente errata ma il compilatore di java compila.
Quindi esegue mentre la condizone è vera risale e riesegue l'istruzione. 

### Il ciclo for 
```
for(inizio; iterazione; passo)
{
	//istruzione
}
```

Esempio: 
```java
for (int i = 1; i<=10, i++)
{
	System.out.println(i)
}
```
Nota ho dichiarato una variabile i dentro il ciclo for e questa variaible vive solo dentro il ciclo for 
Se volgio usare la variabile `i` fuori dal for 
```java
int i = 1;
for (;i<=10, i++)
{
	System.out.println(i);
}
System.out.println(i);
```

continue: 
Consente di procedere all'iterazione successiva del ciclo dove compare (eseguendo una sorta di salto)
Per effettuare un salto di 2 cicli, è nmecessario il costrutto label-continue
```java
for (int i = 0; i<20, i++)
{
	for (int j = 0;j<10;j++)
	{
		if (i ==12 && j ==5)
			continue 
		System.out.println(j);
	}
	System.out.println("--"+i);
}
```

#### Label-continue 
Attraverso un'eticchetta posso identificare un loop e eseguire il continue al loop etichettato 
L'etichetta deve avere un nome composto da una sola parola deve essere seguito da "`:`"
```java
etichetta: 
for (int i = 0; i<20, i++)
{
	for (int j = 0;j<10;j++)
	{
		if (i ==12 && j ==5)
			continue etichetta;
		System.out.println(j);
	}
	System.out.println("--"+i);
}
```

#### Break 
Questa istruzione interrompe il loop dove compare
```java

for (int i = 0; i<20, i++)
{
	for (int j = 0;j<10;j++)
	{
		if (i ==12 && j ==5)
			break;
		System.out.println(j);
	}
	System.out.println("--"+i);
}
```

#### LAbel -break 
Posso etichettare il break come per il continue 


### Stampe e formattazzioni 