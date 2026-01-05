# Introduzione 
Nella scorsa lezione abbiamo trattato gli [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Definire Array in JS|array]] (e il loro indexing), l'attributo [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Attributo `length`|`.length`]], i [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Gli operatori in Javascripts|diversi tipi di operatori]], la [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Coercizione in Javascript Implicita vs. esplicita|conversione tra tipi di variabili (coercizione)]] e il [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Il metodo prompt()|metodo `prompt()`]].

## Espressioni e operatori 
==Un’espressione è qualsiasi frammento di codice che **produce un valore**.== 
Nel dettaglio, un'espressione è una combinazione di valori, [[Lezione 2 Le variabili in Javascript#Le variabili in JS|variabili]] e [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Gli operatori in Javascripts|operatori]] che rappresentano un nuovo valore.
Un esempio classico di espressione è:
```
x + 1 
```

In questo caso, si combina una variabile `x` con il valore numerico `1` tramite l'operatore `+`, ottenendo l'incremento di una unità del valore contenuto in `x`.

Come si può notare, gli **operatori** svolgono un ruolo centrale nelle espressioni, poiché determinano il tipo e il risultato dell'operazione effettuata.

---

## If statements
Come in [[Cicli e condizionali#Conditional Statements|Python]], anche in JavaScript esistono blocchi di codice che permettono al programmatore di **eseguire istruzioni diverse a seconda che una certa condizione sia vera o falsa**.

Questi blocchi si basano su condizioni logiche e consentono al codice di **prendere decisioni** in fase di esecuzione.

In JavaScript esistono principalmente due strutture condizionali: `if` e `switch`.

L'istruzione `if` può presentarsi in tre forme principali:

- [[#If semplice|`if` semplice]]
    
- [[#`if...else`|`if...else`]] (con alternativa)
    
- `if...else if...else` (a cascata)

### If semplice
L'istruzione `if` semplice esegue un blocco di codice **solo se una condizione è vera**.
La sintassi è:
```js
if (condizione) {
    // istruzioni da eseguire se la condizione è vera
}

```

- `condizione`: un'espressione booleana (cioè che restituisce `true` o `false`)
    
- le **istruzioni** all'interno delle parentesi graffe vengono eseguite **solo se** la condizione è `true`


### `If...else` 

La seconda forma è il costrutto `if...else`.  
==In questa forma viene eseguito **un blocco di codice oppure un altro**, a seconda che la condizione specificata sia vera o falsa.==
La sintassi è:
```js
if (condizione){
	//istruzioni1
} else{
	//istruzioni2
}
```
- Se la condizione nell'`if` è vera, vengono eseguite le `istruzioni1`.
    
- Altrimenti, vengono eseguite le `istruzioni2`.

### `if...else if...else`

La terza forma è il costrutto a cascata `if...else if...else`, che permette di gestire **più condizioni alternative**.
In questo caso vengono messe a disposizioni più alternative di esecuzione:
```js
if (condizione1){
	//istruzioni1
}else if (condizione2){
	istruzioni2
}else{
	//istruzioni3
}
```


> [!NOTE]  la key word `else if` corrisponde alla parola chiave dell' [[Cicli e condizionali#^elif-Def|`elif`]] di Python.  ^elseIfJS
> 


In questo caso:

- Se `condizione1` è vera, vengono eseguite le `istruzioni1`.
    
- Se `condizione1` è falsa, ma `condizione2` è vera, vengono eseguite le `istruzioni2`.
    
- Se nessuna delle due condizioni è vera, vengono eseguite le `istruzioni3`.

#### Esempio pratici
```js
let value = 10;

// Prima forma: if semplice
if (value > 20) {
    console.log(`${value} è maggiore di 20`);
}

// Seconda forma: if...else
if (value > 20) {
    console.log(`${value} è maggiore di 20`);
} else {
    console.log(`${value} è minore o uguale a 20`);
}

// Terza forma: if...else if...else
if (value > 20) {
    console.log(`${value} è maggiore di 20`);
} else if (value === 20) {
    console.log(`${value} è uguale a 20`);
} else {
    console.log(`${value} è minore di 20`);
}

```


### Switch case
L'istruzione `switch` in JavaScript viene utilizzata come alternativa ai costrutti `if...else if...else`, ==in particolare **quando si vuole confrontare una variabile con molti possibili valori**==.

Questa struttura è **preferibile** nei casi in cui:

- ==Ci sono molte condizioni da verificare==.
    
- ==Si vuole migliorare la **leggibilità** del codice.==
    
- ==Si cerca una sintassi più **ordinata e compatta** rispetto a una serie di `if...else`.==
    

Inoltre, l’uso di `switch` può essere leggermente più efficiente, poiché ==il motore JavaScript **non valuta tutte le condizioni una per una**, ma **cerca direttamente il valore corrispondente** tra i `case`.==
La sintassi è:

```js
switch (espressione) {
	case valore1:
		// istruzioni1
		break;
	case valore2:
		// istruzioni2
		break;
	// ...
	default:
		// istruzioni di default
		break;
}

```

**Spiegazione:**
- `espressione`: 
	  ==è la variabile (o valore) che viene confrontata con ciascun `case`.==
    
- `case valore`: 
	  ==definisce un possibile valore da confrontare.==
    
- `break`: 
	  ==interrompe l'esecuzione del blocco `switch` e impedisce l'esecuzione dei casi successivi.==
     ^7f53b0
- `default`: 
	  ==è opzionale e rappresenta il blocco di codice da eseguire se nessun `case` corrisponde.==


Alcune volte si può decidere di non mettere l'istruzione break in corrispondenza di uno o più `case` perché si vuole eseguire uno stesso blocco di codice per un gruppo di valori.

#### Esempio Pratico:
```js
let voto = 5;
let giudizio;

switch (voto) {
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:
		giudizio = "insufficiente";
		break;
	case 6:
		giudizio = "sufficiente";
		break;
	case 7:
		giudizio = "discreto";
		break;
	case 8:
		giudizio = "buono";
		break;
	default:
		giudizio = "non classificato";
		break;
}

console.log(giudizio);  // Output: "insufficiente"

```
Come si nota, più `case` possono condividere lo stesso blocco di istruzioni se non si mette il `break` tra di essi.

> [!NOTE] Il costrutto `switch...case` di JavaScript è concettualmente simile al [[Match Statement|**`match` statement**]] introdotto in Python 3.10.
> > [!Abstract]- **Differenze tra match statement e lo switch case** 
> > **`switch...case` in JavaScript**
>>
>>-  Confronta il **valore** di un'espressione con **valori fissi** (=\==)
 >>   
>>-  È utile per **ramificazioni semplici** (es. numeri, stringhe)
 >>   
>>-  Necessita di `break` per evitare il "fall-through" (cioè l'esecuzione anche dei `case` successivi)
 >>   
>>-  Non supporta destrutturazione o condizioni complesse
>> 
 >>**`match` in Python (da 3.10 in poi)**
>>
>>- 🔹 Può confrontare valori **fissi**, come fa `switch`
 >>   
>>- 🔹 Ma in più, fa **pattern matching avanzato**
 >>   
 >>   - Su tuple, liste, dizionari, oggetti
 >>       
 >>   - Con **destrutturazione**, condizioni (`if`), e wildcard (`_`)
 >>       
>>- 🔹 Non richiede `break`, esegue **solo il blocco corrispondente**
  >>  
>>- 🔹 Molto potente in scenari con strutture dati complesse


---
## Iterazioni e loop in JavaScript
In JavaScript, per ripetere l'esecuzione di un blocco di codice finché una condizione è vera, si usano **i cicli di iterazione**.
A differenza di Python, dove le iterazioni vengono fatte principalmente tramite `while` e `for`, in JavaScript esistono **cinque diversi costrutti** per i loop:

1. [[#Il ciclo `while`|`while`]]
    
2. [[#Il ciclo `do...while`|`do...while`]]
    
3. [[#Il ciclo `for`|`for`]]
    
4. `for...in`
    
5. `for...of`

### Il ciclo `while` 
==Il costrutto `while` ripete un blocco di codice **fin tanto che la condizione è vera**.==

La sintassi è:
```js
while (condizione) {
  // istruzioni da ripetere
}
```


> [!NOTE] **Nota Importante:**
> Il ciclo `while` valuta la **condizione prima** di eseguire il blocco di codice. 
> Se la condizione è `false` all'inizio (ovvero non si verificherà mai), il blocco **non viene eseguito** nemmeno una volta.

 >[!bug] Dall'altro canto se la condizione non diventa mai `false` o non viene impostato uno statements condizionale per uscire dal ciclo, questo andrà avanti fino all'infinito.


#### Esempio pratico: scorrere un'array
```js
let array = [10, 20, 30, 40];
let i = 0;

while (i < array.length) {
  console.log(array[i]);
  i++;
}
```

### Il ciclo `do...while`
Il ciclo `do...while` è simile a `while`, ma con una differenza fondamentale:
==**La condizione viene controllata dopo l'esecuzione** del blocco di codice==.  
Questo garantisce che il blocco venga eseguito **almeno una volta**, anche se la condizione è `false`.

La sintassi è:
```js
do {
  // istruzioni da eseguire almeno una volta
} while (condizione);
```

#### Esempio pratico
```js
let numero = 0;

do {
  console.log("Numero:", numero);
  numero++;
} while (numero < 3);
```

In questo caso:
-  Viene dichiarata la variabile `let numero = 0`.
    
- Il blocco `do` stampa la variabile `numero` e, a ogni iterazione, ne incrementa il valore di 1.
    
- Il ciclo continua **finché** la condizione `numero < 3` è vera.
Quindi, quando `numero` è uguale a `3`, la condizione del `while` diventa falsa e il ciclo si interrompe.
In sostanza il `do...while` possiamo vederlo come:
==Nel ciclo `do...while`, le istruzioni scritte nel blocco `do` vengono **sempre eseguite almeno una volta**, **prima** che venga controllata la condizione nel `while`==.  
Dopo la prima esecuzione, la condizione viene valutata:  
- Se è **vera**, il blocco viene eseguito di nuovo.  
- Se è **falsa**, il ciclo termina.

> [!bug] Attenzione: se non viene impostata una condizione che può diventare `false`, si rischia un **ciclo infinito**, proprio come nel `while`.

#### `while` vs `do...while`
- **Nel `while`:**  
    ==la **condizione viene controllata prima** di eseguire il blocco di codice.==  
    ==→ Il codice **viene eseguito solo se** la condizione è `true`.==
    
- **Nel `do...while`:**  
    ==il blocco di codice dentro `do` **viene eseguito almeno una volta**,==  
    ==e **poi** si controlla se la condizione nel `while` è `true` per decidere se ripetere il ciclo.==

Ma quando torna utile usare il `while` e quando invece il `do...while`?
Per rispondere a questa domanda partiamo da due esempi:
##### Esempio con il `while`
```js
let numero = 10;

while (numero < 5) {
  console.log("Valore:", numero);
  numero++;
}
```
**Cosa succede?**

-  La variabile `numero` vale 10, mentre la condizione `numero < 5` è **falsa**.
    
- Di conseguenza, il ciclo **non parte mai** e non stampa nulla.

> [!ticket] **In conclusione:**
> ==Il `while` è utile **quando vuoi eseguire il codice solo se la condizione è già vera**.==

##### Esempio con il `do...while`
```js
let numero = 10;

do {
  console.log("Valore:", numero);
  numero++;
} while (numero < 5);
```

**Cosa succede?**

- Anche se la variabile `numero` è pari a `10` e la condizione del ciclo è `numero < 5`, quindi è **falsa**
    
- Tuttavia, il blocco `do` viene comunque **eseguito una volta**!
    
- Risultato: stampa una sola volta `Valore: 10`.

> [!ticket] **Conclusione**:  
> ==Il `do...while` è utile **quando vuoi che il blocco di codice venga eseguito almeno una volta**, anche se la condizione iniziale non è soddisfatta.==

### Il ciclo `for`
Una **alternativa al `while`** è l'istruzione `for`, utile quando si vuole **ripetere un blocco di codice per un numero noto di volte**.

La sintassi è:
```js
for (inizializzazione; condizione; modifica) {
  // istruzioni da eseguire
}
```

- **`inizializzazione`**: 
  ==viene eseguita **una sola volta** all’inizio. Di solito si inizializza un contatore.==
    
- **`condizione`**: 
  ==viene valutata **prima di ogni iterazione**. Se è `true`, il ciclo continua; altrimenti termina.==
    
- **`modifica`**: 
  ==viene eseguita **alla fine di ogni iterazione**. Tipicamente un incremento/decremento del contatore.== 

#### Esempio concreto 
```js
for (let i = 0; i < 5; i++) {
  console.log("Iterazione numero:", i);
}
```

In questo caso:
- `let i = 0`: viene inizializzato un contatore `i` uguale a zero
- `i<5`: viene impostata la condizione per cui se il contatore rimane minore di 5 il ciclo continua ad eseguire l'istruzione
- `i++`: è la modifica del ciclo, viene eseguita ad ogni iterazione e incrementa il contatore di un'unità.

> [!NOTE] Nota:
> A differenza di Python, dove la [[Cicli e condizionali#For Loops|sintassi del ciclo `for`]] è più verbosa e richiede l’uso di `range()` per iterare su indici, in JavaScript il ciclo `for` ha una sintassi **più compatta** in una sola riga:

### Il ciclo `for...in`
==Questa variante del `for` è utile per iterare sugli **indici** di un array (o sulle **chiavi** di un oggetto).==
Infatti serve esclusivamente per iterare sugli indici di un array (o le chiavi di un oggetto).
La sintassi è :
```
for (var indice in nomeArray){
	//istruzioni da eseguire
}
```

Spiegazione:
- `indice`: è una **variabile** che assume il valore di ogni **indice** dell’array (come `"0"`, `"1"`, ...).
- `nomeArray`: è il nome dell’array su cui si itera.
Quindi il `for..in` non parte da un indice per trovare quanti indici ci sono in un array, itera soltanto
In sostanza ==**il ciclo `for...in` serve a iterare su tutti gli indici (o chiavi) di una struttura iterabile come un array o un oggetto.**==  
==Ad ogni iterazione, la variabile assume il valore di un indice (nell’array) o di una chiave (nell’oggetto).==
Sfruttando questa variante del `for` non si ha bisogno di specificare la lunghezza dell’array né l’istruzione di modifica della condizione.
Javascript rileva che la variabile quantità è un array ed assegna ad ogni iterazione alla variabile indice il valore dell’indice corrente.

#### Esempio concreto del `for...in`

```js
let quantita = [12, 24, 42, 11, 29];
let totale = 0;

for (let indice in quantita) {
  totale += quantita[indice];
}
console.log("Totale:", totale);
```

**Spiegazione:**
1. `let quantita = [12, 24, 42, 11, 29];`: viene dichiarato l'array `quantità` che contiene 5 numeri
2. `let totale = 0;`: viene creato una variabile `totale` che servirà per sommare tutti i valori presenti nell'array.
3. ciclo `for...in`: **itera sugli indici** dell’array `quantita`, non sui valori direttamente.
	- - Alla **prima iterazione**: `indice = "0"` → `quantita[0] = 12` → `totale = 0 + 12 = 12`
    
	- Seconda: `indice = "1"` → `quantita[1] = 24` → `totale = 12 + 24 = 36`
    
	- Terza: `indice = "2"` → `quantita[2] = 42` → `totale = 36 + 42 = 78`
    
	- Quarta: `indice = "3"` → `quantita[3] = 11` → `totale = 78 + 11 = 89`
    
	- Quinta: `indice = "4"` → `quantita[4] = 29` → `totale = 89 + 29 = 118`.

> [!NOTE] Anche se `indice` è una **stringa** (`"0"`, `"1"`, ...), JavaScript la converte automaticamente in numero quando accediamo a `quantita[indice]`.



### Il ciclo `for...of`
Questa è l'ultima variante del ciclo `for` in JS:
==È utile per iterare direttamente sui **valori** di un array (o di qualsiasi oggetto iterabile)==.
La sintassi è:
```js
for (let valore of nomeArray){
	//istruzione da eseguire
}
```
Spiegazione:
- `let valore`: è una variabile che, ad ogni iterazione, contiene **il valore corrente** dell’array.
  
- `nomeArray`: è l’array (o l’oggetto iterabile) su cui si sta iterando.
A differenza del ciclo `for...in` che scorre **gli indici** (o le chiavi di un oggetto), il ciclo `for...of` lavora **direttamente con i valori** contenuti nella struttura.


#### Esempio pratico del `for...of`
```js
let quantita = [12, 24, 42, 11, 29];
let totale = 0;

for (let valore of quantita) {
  totale += valore;
}
console.log("Totale:", totale);

```
 **Cosa succede:**

- Alla prima iterazione: `valore = 12` → `totale = 0 + 12 = 12`
    
- Poi `valore = 24` → `totale = 12 + 24 = 36`
    
- Poi `valore = 42` → `totale = 36 + 42 = 78`
    
- Poi `valore = 11` → `totale = 78 + 11 = 89`
    
- Poi `valore = 29` → `totale = 89 + 29 = 118`.

Come possiamo notare questo esempio è uguale all'esempio del `for...in`, ma allora quando è utile usare la prima variante e quando è utile usare la seconda?

#### `for...in` vs. `for...of`
Entrambi sono cicli utili in JavaScript, ma servono a **scopi diversi**, soprattutto quando si lavora con array o oggetti.
==Nel caso degli **array**, è preferibile usare `for...of` per iterare direttamente sui valori, perché è **più leggibile** e **più sicuro** (evita proprietà aggiunte al prototipo dell’array).==  
==Tuttavia, `for...in` **è molto utile per iterare sulle proprietà di un oggetto**.==

Il `for...in` è utile quando si deve iterare sulle **proprietà (chiavi)** di un oggetto:
```js
let persona = { nome: "Luca", età: 25, città: "Roma" };

for (let chiave in persona) {
  console.log(chiave + ": " + persona[chiave]);
}
// Output:
// nome: Luca
// età: 25
// città: Roma
```


Il `for...of` è invece utile quando si vogliono scorrere i **valori** di una struttura iterabile, come un array, una stringa, un Set o una Map: 
```js
let numeri = [10, 20, 30];

for (let numero of numeri) {
  console.log(numero); // stampa 10, poi 20, poi 30
}

```



> [!caution] Attenzione sugli array
> Anche se `for...in` può essere usato sugli array, è **fortemente sconsigliato** perché può iterare anche su **proprietà personalizzate** o **ereditarie** dell’array:
>```js
>Array.prototype.saluto = "Ciao";
>let arr = [1, 2, 3];
>
>for (let i in arr) {
>  console.log(i); // stampa 0, 1, 2, saluto ❌
>} 
>```
>> [!done] In conclusione:
>> usare sempre `for...of` per gli array, poiché è più **chiaro**, **sicuro** e **intuitivo**.


