
Tutte le funzioni che scriviamo deve semrpe stare dentro una classe 


#### Commenti 
`//`: per commenti una riga
`/**/`: commenti multilinea 

Documentazione javadoc: 
```java
/**Commenti javadoc: 
* invocando uno speciale tool (javadoc.exe) sul codice commentato con questa formattazione viene prodotta una documentazione standard 
* Si utilizzano inoltre speciali tag definire caratteristiche delle classi 
*

*
*
*
*
*/ 
```

### Tipi di dato primitivi
Non sono oggetti
1. Interi: int, short, long, byte
	Ce ne sono tanti perché ognuno di questi occupano diversi byte in memoria 
2. Float
3. Carattere 
4. Logico: boolean

Interi: 

| Tipo  | Requisiti | Intervallo(inclusivo)              |
| ----- | --------- | ---------------------------------- |
| int   | 4 byte    | Da -2.147.483.648 a +2.147.483.648 |
| short | 2 Byte    | Da -32.768 a +32.768               |
| long  | 8 byte    |                                    |
| byte  | 1byte     | Da -128 a +127                     |

Float

| Tipo   | Requisiti<br> | Intervallo(inclusivo)<br> |
| ------ | ------------- | ------------------------- |
| float  | 4 byte        |                           |
| double | 8 byte        |                           |

Le stringhe in Java sono oggetti non primitivi, in molte linguaggi le stringhe sono assimiliti ai primitivi ma la sun e la oracle le hanno preferito definire le stringhe come classi quindi il primitivo di tipo carattere è il char


#### Tipo carattere 
È un carattere dello schema unicode (raccoglie tutti i caratteri esistenti), si rappresenta su 2 bytes.
I caratteri occupano 2 byte in memoria 
A differneza di python per i caratteri si usano i singoli apici
```java
char c1 = 'A';
char c2 = 'a'; 
```

Fanno eccezzione le sequenze di escape.

#### Il tipo booleano
Assume sotanto due valori: 
1. true
2. false 
Per dichiararlo: 
```java
boolean flag = false; 
```

Tendezialmente si usano nelle istruzioni di controllo (if, while, do)
Gli operatori comparativi restituiscono 

#### Dichiarazione variabili 
R
Tutte le variabili devono essere dichiarate 
Una variaible viene definita da: 
- un tipo 
- identificatore 
Regole delgi identificatori: 
- sono


#### Blocchi di istruzioni 
Le parentesi graffe delimitano blocchi di istruzioni
Racchiudono classi


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