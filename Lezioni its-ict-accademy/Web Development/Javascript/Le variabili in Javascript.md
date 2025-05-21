# Introduzione
Possiamo immaginare le variabili come delle “scatole” all’interno delle quali immagazzinare dati. In JavaScript per creare delle variabili è sufficiente assegnare un contenuto ed anche se non è obbligatorio, aggiungere sempre la keyword `var` (quando scegliamo un nome alla variabile ricordiamoci di non inserire spazi, usare
la convenzione camelCase. Può iniziare con `_ $  a-z`). 
Ad esempio :
```js
console.log("hello world")
var nome = "Corso JS";
var _tipo = "Linguaggio di programazzione";
var $lato = "Lato client e lato server"
console.log(nome)
console.log(_tipo)
console.log($lato)
```

## Le variabili in JS
### Dichiarazione di una variabile
Come avevamo detto nella scorsa lezione si può scrivere codice inline o in blocco:
inline si poteva farlo fino al 2009, infatti, prima di questa data, per dichirare una variabile bisognava scrivere:
```js
var nome_varibile = valore
```

Dopo il 2009 è stato indrototto la dichiarazione `let`:
```javascript
let nome_variabile = valore
```

Questa nuova keyword è stata introdotta per evitare l'override delle variabili in JS con il `var`:
```js
var nome = "mario"
var nome = "Giacomo"
```

Se facessimo correre questo codice l'ultimo `var` nome sovrascrive il primo:
cioè `var nome` adesso corrisponderà al valore stringa `"Giacomo"` non più `"mario"`. Questo perché il `var` è una keyword per dichiarare una variabile globale in Javascript.
Con il `let` si è ovviato questa problema.
Oltre all'override delle variabili con l'introduzione della keyword `let` si è ovviato ad un altro problema, l' hoisting:
- Sposta tutte le diciharazione di variabili in cima alla scope globale (la pagina):
```
console.log(nome);
var nome = "mario";
var = "luca";

```

Se runniamo questo codice viene stampato in console `undefined` perché sposta tutte le dichiarazioni in cima ma non l'assegnazione dei valori delle variabili, 
Questo problema è stato risolto con l'introduzione di `let`. 


> [!danger] Usare sempre è solo `let`


- Inoltre sposta anche tutte le funzioni.

Su JS la diciharazione delle varibili è implicita:
```js
pippo = 10
```
il codice funziona senza aver usate le due dichiarazioni di varuabuli e JS in questo caso mettte di defualt il `var` per questo è meglio scrivere esplicitamente i due tipi di dicharazione, difatti JS è definito un linguaggio di tipizzazione debole: 
quando ad una variabile gli si assegna un valore e poi si usa un altro valore per quella variabile Js assegna dinamicamente alla variabile quel nuovo valore(stessa cosa vale per Python).
I punti e virgola è fine istruzione, in JS questa cosa non da errori e non è obbligatorio:

```js
let x = 10

console log(x)
```

Se runniamo questo codice non da errore di alcun tipo. 
La pericilosità di questa scrittura e che se non si usa il punto e virogla e che quello che se scrivo nella riga successiva può influenzare la/le righa/e precendente/i 
```js
let x = 10 
+20
console.log(x)
```

Se runniamo questo codice il vlaore di x verrà sommato al 20 e restituirà 30 in console.

### I tipi di variabili in Javascript

I tipi di variabili in JS sono 
- `String`
- `Number` 
- `Boolean` 
- `Undefined`
Tutti questi tipi (eccetto `undefined`) sono oggetti. 
#### Le stringhe in Javascript
Una stringa in JavaScript è una sequenza di caratteri delimitata da doppi o singoli apici. Le seguenti sono esempi di stringhe:
• "stringa numero uno"
• 'stringa numero due'
Non c’è una regola per stabilire quale delimitatore utilizzare. L’unica regola è che il delimitatore finale deve essere uguale al delimitatore iniziale. 
Questo ci consente di scrivere stringhe come le seguenti senza incorrere in errori:
• "l'altro ieri"
• "questa è una 'stringa'"
Un tipo speciale di stringa è la stringa vuota, cioè una stringa senza caratteri. 
Essa può essere rappresentata indifferentemente come "" oppure ''.
Nella fase 1 quando si  aveva una variabile per far capire all'interprete che era una stringa bastava usare il singolo o il doppio apice, infatti per concatenare le stringhe si poteva farlo tramite i valori delle variabili o nelle variabili stesse
```js
let x = 10 
+20
console.log(x);

var nom = "Mario"
var nom2= "Mario" + x + "Rossi"
```
^codeJs

Nella fase 2 è stato deciso oltre ad aver introdotto il let  stato indrotto il template string usando le backticks (\`\`) `alt + 96` su windows
```js
let x = 10 

console.log(x);

let nom = `Mario ${x} Rossi è il mio collega`;
console.log(nom)
```

##### Gli escape character delle stringhe 
All'interno di una stringa per mettere caratteri speciali si usa il backslash (`\`)

```js
let nom = "Mario è \"bello\" ";
```

All’interno delle stringhe è possibile indicare alcuni caratteri speciali di JavaScript ovvero delle sequenze che costituiscono un mezzo per formattare il testo:

| Sintassi | Significato                 |
| -------- | --------------------------- |
| `\&`     | visualizza la & commerciale |
| `\n `    | nuova riga                  |
| `\r`     | ritorno a capo              |
| `\t `    | tab orizzontale             |
| `\\ `    | visualizza il backslash     |
#### Concatenazione delle Stringhe 
Come abbiamo visto nell'[[#^codeJs|esempio precedente]], l’unico operatore su stringhe specifico è l’operatore di concatenazione. Esso consente di creare una nuova stringa come risultato della concatenazione di due stringhe ed è rappresentato dal simbolo del “più” (`+`):
`"piano" + "forte" // "pianoforte"`
Il suo utilizzo è abbastanza immediato, ma con le variabili si possono ottenere risultati non previsti dal momento che il simbolo utilizzato è lo stesso dell’addizione. Ad esempio, nella seguente espressione:
`x + y`
come fa JavaScript a stabilire se deve sommare o concatenare?
Vedremo più avanti la risposta a questa domanda e i possibili effetti indesiderati che si possono generare.
==Come detto in precedenza le stringhe in javascript sono oggetti, in quanto tali ha proprietà e metodi.== 
L’unica proprietà è `length`: 
==restituisce il numero di caratteri presenti all’interno di una stringa==. 
Mentre gli altri metodi più importanti sono :
1. `toUpperCase()` : ==trasforma la stringa tutta in maiuscolo==.
2. `toLowerCase()` : ==trasforma la stringa tutta in minuscolo.==
3. `split()` : ==divide la stringa in array prendendo come delimitatore il carattere passato all’ingresso del metodo.==
4. `replace()` : ==sostituisce una parte della stringa prendendo la stringa passata per prima e la sostituisce con la stringa passata per secondo parametro.== 


#### Numeri in JS 
JavaScript ha un unico tipo di dato numerico, **cioè non c’è distinzione formale, ad esempio, tra intero e decimale.**
Internamente tutti i valori numerici sono rappresentati come numeri in virgola mobile, ma se non è specificata la parte decimale il numero viene trattato come intero (sono a 64 bit i numeri da `−9.223.372.036.854.775.808` a
`+9.223.372.036.854.775.807`).

• `var interoNegativo = -10;`
• `var zero = 0;`
• `var interoPositivo = 123;`
• `var numeroDecimale = 0.52;`
• `var altroNumeroDecimale = 12.34;`
• `var decimaleNegativo = -1.2;`
I numeri invece in Js sono più semplici. 
```
let anni = 10
```

Può capitare, e capita spesso, quando su HTML si lavora con i form e devo prendere questi il valore con il dom di questo input, HTML mi restituirà solo stringhe

```js
let anni =document.getElementById("mionumero").value
console.log(typeof(anni))
```

Siccome in JS dobbiamo lavorarwe con in numeri dobbiamo usare il casting
```js
let anni =document.getElementById("mionumero").value
console.log(typeof(anni))

parseInt(anni) // Converte una stringa in intero
parseFloat(anni) //Converte una stringa in Reale
```

`parseInt`: 

La funzione parseInt in Javascript viene generalmente utilizzata per convertire il suoprimo argomento in un numero intero. La sintassi è la seguente: `parseInt(stringa)`. 
Dove stringa rappresenta la stringa da convertire.
```js
var importo = "12"
console.log(parseInt(importo)) //12 adesso è un integer
```

`parseFloat()`:
La funzione `parseFloat()` fa la stessa cosa del `parseInt()` con l’unica differenza che torna un numero decimale invece di un numero intero.

```js
var importo = "12.6789"
console.log(parseFloat(importo)) //12.6789 ora è un reale
```

### La costante Nan

La particolarità di JS esiste una costante globlae chiamata `Nan`(not a number) viene chiamata da JS per dire che quella variabile non è un numero.
NaN (Not a Number) è una costante globale che viene invocata quando si esegue una funzione matematica con i numeri e questa operazione torna qualcosa che non è un numero.
La prima cosa da dire è che NaN non è uguale a se stesso. Questo vuol dire che se ad esempio scrivo :
```js
console.log( 1 === 1 ); // true
console.log( NaN === NaN ) // false
```

Questo vuol dire che se noi vogliamo verificare se un risultato è uguale a NaN non posso confrontarlo con NaN. Ad esempio se scrivo:
```js
var risultato = 10 * ‘prova’;
console.log(risultato);
```
Mi restituirà in console `NaN`. Ma se noi facciamo un confronto come ad esempio `(risultato === NaN)` non sarà mai `true`… anche se risultato in questo caso
vale `NaN`.
Quindi viene invocata a video ma non posso riutilizzarla nel codice.

### La funzione IsNan()
Per ovviare a questo problema si può utilizzare la funzione globale `IsNan()`.
**==La funzione globale `IsNaN()` ritornerà `true` se gli viene passato qualsiasi valore diverso da un numero.==**
In ogni modo cerca di fare un cast ad un numero (ad esempio stringa vuota e false la converte a 0). Se riprendiamo l’ esempio di prima e scrivo :
```js
console.log(IsNaN(‘ciao’)); // true
console.log(IsNaN(‘’)); // false
console.log(IsNaN(false)) // false
```
Pero IsNan non mi da una soluzione al 100% vera, perché una stringa vuota ritorna false perché per JS è 0 mentre se è piena è 1 quindi true.
Perchè se io scrivo in Js:
```js
let z = ""
if (z){

}
```
Scrivo questo perché in JS come in altri linguaggi di programmazione una stringa vuota viene trattato come un booleano, quindi sto dicendo che se z è una stringa bvuota fai qualcosa. 
Quindi se la variabile è vuota è False quindi è zero e se la passo in `IsNan()` per lui è un numero.
Se io in JS scrivessi:
```
console.log(""+3) //stampa 3
```
Fa una concatenazione tra una stringa vuota e l'intero `3`.

> [!hint] Consiglio
> Anziché usare il `IsNaN` per controllare se quel valore è un numero o meno è meglio usare `typeof()`.
>```js
> if (typeof(z)=="number"){
> }
>```
>Cosi stiamo dicendo che se `z` è uguale a numero allora fai qualcosa


> [!info] Info
> `Number.isNaN()` ritorna True solo se gli arriva `NaN`, e serve a controllare se si ha un `NaN`


La differenza tra null e undefinde è che null è un vlaore e undefined no:
```
let r = null //null
let w //undefined
```
Undefined è qualcosa che non è mai stato inizializzato