# Introduzione
Abbiamo trattato nella scorsa lezione delle [[Lezione 4 ; Espressioni e operatori, statements e cicli#Espressioni e operatori|Espressioni e operatori]], gli [[Lezione 4 ; Espressioni e operatori, statements e cicli#If statements|statements condizionali]],  lo [[Lezione 4 ; Espressioni e operatori, statements e cicli#Switch case|switch case]], [[Lezione 4 ; Espressioni e operatori, statements e cicli#Iterazioni e loop in JavaScript|Le iterazioni e i loop in JavaScript]] con i diversi costrutti.
Ora ci occupiamo delle funzioni.
## Le funzioni 

==Le funzioni in JavaScript sono blocchi di codice riutilizzabili che eseguono un insieme di istruzioni quando vengono chiamate.==
La sintassi è molto semplice: 
```JS
function nomeFunzione(){
… istruzioni …
}
```

- La parola chiave `function` serve per dichiarare una funzione.
    
- Le **parentesi tonde** `()` contengono eventuali **parametri**.
    
- Le **parentesi graffe** `{}` racchiudono le **istruzioni** della funzione.

### Come funziona l'esecuzione delle funzioni
Il browser legge il file JavaScript **in modo sequenziale**, ma **le dichiarazioni di funzione vengono pre-caricate (hoisting)**.  
Una funzione **viene eseguita solo se viene chiamata.**
In genere una funzione può ricevere dei parametri e ritornare un valore (se non torna nulla è `undefined`).

Come per le [[Funzioni in Python|funzioni in Python]] anche in JS sono utili per evitare di ripetere blocchi di codice, riutilizzare comportamenti e organizzare il codice in modo funzionale.
Quindi servono per automatizzare e riusare comportamenti del programma che in caso contrario bisognerebbe ripetere il codice; un concetto è chiamato "Dry concept(Don't Repeat Yourself)":
>evita di scrivere lo stesso codice più volte.


### Esempio pratico 
Per cominciare, scriviamo una funzione semplice che esegue la somma di due numeri:
```JS
<script>
	function somma(num1,num2){
		document.write(num1 + num2);
	}
</script>
```
Questa funzione non torna nulla perché viene scritta direttamente nella pagina: 
tramite il `document.write()` la funzione viene scritta direttamente nella pagina [[HTML]]  e si se esegue la pagina non si trova nulla perché manca la chiamata della funzione.
Infatti questa funzione non torna la somma tra `num1` e `num2` ma la scrive  direttamente nella pagina o documento HTML.

Per richiamare una funzione, come in python, basta riscrivere il suo nome:
```js
<script>
	function somma(num1,num2){
		document.write(num1 + num2);
	}
somma(5,6)

</script>
```

Per **restituire** un valore da una funzione, si utilizza la parola chiave [[Funzioni in Python#Il Return|`return`]]: 
==Anche in JavaScript, `return` serve a restituire in output il valore di una funzione.==

È utile per:
- ==Per **salvare il risultato in una variabile**==
    
- ==Per **stampare il valore** con `console.log()`== 
    
- ==Per **usarlo in altre operazioni**==
Per fare un ulteriore esempio utilizzando il `return`:

```js
function testProva() {
  console.log('corso JS');
  return 'benvenuto';
}

testProva(); // Stampa: corso JS

console.log(testProva()); 
// Stampa: corso JS
// Poi stampa: benvenuto

let risultato = testProva(); // Salva il valore
console.log(risultato);      // Stampa: benvenuto

```

- `testProva()` viene eseguita e stampa `"corso JS"`.
    
- Il valore di ritorno `"benvenuto"` può essere:
    
    - stampato direttamente,
        
    - salvato in una variabile,
        
    - usato in altre espressioni.
Questa funzione, se ignoriamo il `console.log()`, torna una stringa.

### Funzioni con più parametri
E ancora:

```JS
<script>
function saluto(nome1,nome2,nome3){
	document.write(‘’Benvenuto’’ + nome1);
	document.write(‘’Benvenuto’’ + nome2);
	document.write(‘’Benvenuto’’ + nome3);
}
saluto(‘’Mario’’,’’Luca’’,’’Giovanna’’); // cosa succede ?
saluto(‘’Mario’’,’’Luca’’); // cosa succede ?
</script>
```
##### Cosa succede?

- Nella prima chiamata (`saluto("Mario", "Luca", "Giovanna")`):  
    Vengono stampati 3 messaggi di benvenuto.
    
- Nella seconda chiamata (`saluto("Mario", "Luca")`):  
    I primi due messaggi vengono stampati correttamente.  
    Il terzo (`nome3`) è `undefined`, quindi stampa:  
    **"`Benvenuto undefined`"** 

> [!caution] Attenzione!
> JavaScript è "accomodante": a differenza di python, se mancano degli argomenti, li considera come `undefined` e **non dà errore**

### Array arguments
L’oggetto `arguments` è una variabile locale disponibile in tutte le funzioni tradizionali (dichiarate con `function`). 
==Permette di accedere **a tutti gli argomenti passati** alla funzione, anche se non sono dichiarati come parametri.== 
È possibile fare riferimento agli argomenti di una funzione all’interno della funzione utilizzando l’oggetto arguments.
==Questo oggetto contiene una voce per ogni argomento passato a una funzione, che ci aiuterà a conoscere il numero di questi argomenti e ad accedervi.==

> [!NOTE] Nota
> `arguments` **non funziona** con le **[[#Arrow function|arrow functions]]** (`()=>{}`).

Come abbiamo detto, l’oggetto arguments è un oggetto ([[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Definire Array in JS|array]]), quindi ha una proprietà `length()`: ==ovvero possiamo accedere ai valori individuali==
==usando la notazione di indicizzazione dell’array (`arguments [i]`)==
```JS
function myFunction (a,b,c){
	console.log(arguments[0])
	console.log(arguments[1])
	console.log(arguments[2])
}
myFunction(1,2,3)
```
 Inoltre **on** supporta metodi come `map()`, `forEach()` ecc.  
(Per usarli, bisogna convertirlo in array con `Array.from()` o spread `[...arguments]`)
### Variabili locali e globali 
Abbiamo già visto le [[Lezione 2 Le variabili in Javascript#Le variabili in JS|variabili in JS]] nella lezione [[Lezione 2 Le variabili in Javascript]], ma quando si parla di **funzioni**, è fondamentale capire la **visibilità** (o _scope_) delle variabili.
#### Cos'è lo scope?
==Lo **scope** è l'**ambito di visibilità** di una variabile, cioè **dove** è accessibile all'interno del codice.==

#### Variabili locali 
Una variabile è **locale** quando è **dichiarata dentro una funzione** o un blocco (`{}`), ed è accessibile **solo lì dentro.**
Esempio: 
```js
function saluta() {
  let nome = "Mario";
  console.log("Ciao " + nome);
}

saluta();        // ✅ Ciao Mario
console.log(nome); // ❌ Errore: nome is not defined
```
In questo esempio, `nome` è **locale** alla funzione `saluta`.

#### Variabili globali 
Una variabile è **globale** se è dichiarata **fuori da tutte le funzioni**.  
È accessibile **in tutto lo script**, anche **dentro** le funzioni.

```js
let saluto = "Ciao";

function mostraSaluto() {
  console.log(saluto + " a tutti!");
}

mostraSaluto(); // ✅ Ciao a tutti!
console.log(saluto); // ✅ Ciao

```


> [!caution] Attenzione: conflitto tra variabili locali e globali
> Se una variabile **locale ha lo stesso nome** di una globale, **la variabile locale ha la precedenza** **all’interno della funzione**.
> 
> 
>```js
> let nome = "Anna";
>
>function mostraNome() {
 > let nome = "Lucia";
 > console.log(nome); // Lucia
>}
>mostraNome();
>console.log(nome);   // Anna
>
>```


### Espressioni di Funzione 

In JavaScript, oltre al modo classico per definire una funzione, è possibile usare anche le **espressioni di funzione:** 
==cioè **assegnare una funzione a una variabile**.==
Quindi si può dichiarare una funzione in due modi:
1. **Dichiarazione classica (Function Declaration):**
```js
function saluto() {
  console.log("Ciao!");
}
```

2. **Espressione di funzione (Function Expression):**
```JS
var saluto = function () {
  console.log("Ciao!");
};
```
Qui  si sta  **assegnando una funzione anonima** (senza nome) a una variabile chiamata `saluto`.  
Alla fine si mette `;` perché si tratta di **un'assegnazione**, non di una dichiarazione autonoma.

Per richiamare la funzione è sufficiente usare il nome della variabile seguito dalle parentesi tonde (quindi nello stesso modo della dichiarazione di una
funzione normale). La domanda quindi è… effettivamente cosa cambia tra le due modalità ?

La differenza sta nel fatto che se  dichiaro la funzione come Function expression:
**non vengono sollevate con il loro valore**, quindi **non si possono usare prima della riga in cui sono dichiarate.** 
Mentre se la dichiaro come Function Declaration: vengono "sollevate" (hoisted); ovvero sono **disponibili ovunque** nel codice.
Questo comportamento in JS è chiamato **hoisting:** 
**le dichiarazioni di funzione vengono spostate in cima** allo script **prima dell’esecuzione** in modo da poterle richiamare ovunque nel codice. 


#### Esempi a confronto

```JS
test1();//Errore
test2();//OK
var test1 = function(){
	console.log('espressione di funzione);
}
function test2(){
	console.log('funzione classica')
}
```

**Spiegazione:**

- `test1()` lancia un errore perché al momento della chiamata `test1` è `undefined` (la funzione non è ancora assegnata).
    
- `test2()` funziona perfettamente perché è una **function declaration** ed è già disponibile grazie all'**hoisting**.


> [!hint] Quando usare l’una o l’altra?
> - Usa **function declaration** se la funzione è di uso generale e dev'essere disponibile ovunque.
  >  
>- Usa **function expression** se vuoi **limitare la visibilità**, per esempio in una funzione callback, o se preferisci uno stile più funzionale (molto comune con le **[[#Arrow function|arrow functions]]**).



### Arrow function
Con l’introduzione di **ES6 (ECMAScript 2015)**, JavaScript ha aggiunto una nuova sintassi per scrivere le funzioni: le **arrow function** (o **funzioni freccia**)
Sono più **brevi**, **leggibili** e ampiamente usate nel codice moderno, soprattutto per le callback. 
La sintassi delle arrow function è la seguente :
```js
let test = () => {
	console.log('arrow')
}
test();
```
- Le **parentesi `()`** indicano che la funzione **può ricevere parametri**.
    
- La **freccia `\=>`** sostituisce la parola chiave `function`. 
Ad esempio :
```js
let test = (nome,cognome) => {
	console.log('arrow')
	console.log(nome + ' ' + cognome)
}
test('Pippo', 'Sowlo');
```

==Per definizione le arrow function sono funzioni anonime (perché non hanno il nome della funzione)==,  e vengono usati come callback: 
cioè come funzioni **passate come parametro** ad altre funzioni.

Ma quando una funzione viene chiamata automaticamente?
Prima di ES6, una funzione anonima si scriveva così:
```
let y = function(){
	//istruzione da eseguire
}
```


In realtà non cambia solo la sintassi, ma si aggiungono altri vantaggi come quello della sintassi abbreviata:
1. ==Quando il parametro è uno solo le tonde non so obbligatorie==
```js
let saluta = nome => console.log('Ciao ' + nome);
saluta('Luca');

```
2. ==Quando il contenuto della funzione è una sola istruzione le graffe non sono obbligatorie e il `return` è implicito.==
```js
let somma = (a, b) => a + b;
console.log(somma(2, 3)); //   5
```
Quindi se si scrive una arrow function bisogna stare dentro un altra funzione:
```
let x = () => {
	//istruzione da eseguire
}
```
Questo esempio è banale ma non rispecchia la realta: le arrow function vengono utilizzate nella maggior parte dei casi come callback; 
le callback è una funzione che viene passato come parametro ad un'altra funzione.
Quindi 
```
let y = () => {
	console.log("Funzione passata come parametro!");
}

let x = (callback) => {
	callback(); // la funzione y viene eseguita qui
	console.log("Fine esecuzione.");
}

x(y);

```

Si chiama `x` e poi `x` chiamerà `y`.
Per fare un esempio più pratico:
```js
let giorni = ['lunedì', 'martedi'] //posso scorrere questo array con il for, for in, for of ma posso scorrerli anche con il map e il for each

//Partiamo dal ciclo for normale
for (let i = 0; i<giorni.length; i++){
	console.log(giorni[i])
}

//COn il for of stmapa il vlaore
for (let giorno di giorni) {
	console.log(giorno)
}

//Con il for in, stmapa l'indice
for (let indice in giorni){
	console.log(giorni[indice])
}
//for each e map sono metodi di array
//con il forEach
giorni.forEach((giorno)) =>{
	console.log(giorno);
}
//o posso scriverlo cosi perchè si ha un solo parametro e una sola istruzione
giorni,forEach(giorno => console.log(giorno));

//con map()
giorni.map((giorno)) => {
	console.log(giorno);
}

//Si puo scrivere anche cosi
giorno.map(giorno =>console.log(giorno)); //restituisce gli indici degli elementi della lista ma con i valori undefined perché è come se si stesse dicendo di ritornare un console.log di giorno
giorno.map(giorno =>giorno); //in questo caso tornerà un array con i giorni della settimana perché non essendoci le graffe torna gli elementi della lista
```

In alcuni framework e librerie non possono usare costrutti (`if`, `while`, `for`, `do..while`, `for..in`, `for..each`), quindi se si deve iterare su un array si usano `forEach` e `map()`.
La differenza tra questi due:
- `for each`: ==è un ciclo for che non torna nulla; cioè se si dovesse far ritornare qualcosa sull'array giorni usando il `forEach`== 
- `map()`: ==**ritorna un nuovo array**, quindi se non ritorni nulla esplicitamente, ottieni `undefined`==.


| Metodo      | Ritorna un valore?      | Scopo principale                   |
| ----------- | ----------------------- | ---------------------------------- |
| `forEach()` | No                      | Esegue un'azione per ogni elemento |
| `map()`     | Si, cioè un nuovo array | Trasforma ogni elemento dell'array |
### Nota su framework/librerie (es. **JSX**, React)

In alcuni contesti (come JSX in React), **non puoi usare costrutti come `if`, `while`, `for`, `do...while`, `for...in`** dentro l’HTML virtuale.  
Per questo motivo si usano sempre metodi come `map()` per iterare sugli array:
```
{giorni.map(giorno => <li>{giorno}</li>)}
```
Quindi:

- ✅ `forEach()` → utile per side effect (es. `console.log`, invio dati, ecc.)
    
- ✅ `map()` → utile quando vuoi generare un **nuovo array** (es. in JSX)
Ad esempio nella libreria JSX non si possono utilizzare costrutti e si deve scrivere tutto il codice  sulla stessa linea.

### Parametri di default 

Come in [[Funzioni in Python#Argomenti passati per valori di default|Python]], anche in JS dopo il ES6 è possibile dare dei valori di default ai parametri di una funzione. 
Per parametro di default si intende: 
==È un valore che una funzione **usa automaticamente** se non gli viene passato un argomento o viene passato `undefined`.== 
Nel ES5 quando si  aveva una funzione con dei parametri in ingresso dovevamo controllarli con una if ed eventualmente se vuoti assegnargli manualmente dei valori in questo modo :
```JS
function prova (a,b){
	a = a||0
	b = b || 0 
	console.log(a);
	console.log(b);
}
prova(); //0 0
prova (5,6); // 5 6
```

Invece con ES6 è possibile dare dei valori di default (come in per le funzioni di Python) direttamente in ingresso alla funzione in questo modo :
```js
function prova (a = 0, b = 0){
	console.log(a);
	console.log(b);
}
prova(); // 0 0
prova (5, 6); // 5 6
```
