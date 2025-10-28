# Introduzione 
Per usare React quello che ci servirà è:
- Node.js 
- Chrome, 
- VSCode
- HTML to JSX compiler 
- https://codepen.io/
E bisogna conoscere: 
- [[HTML]]
- [[CSS]]
- [[Lezione 1 I fondamenti Javascript|Javascript]]
- [[Bootstrap]]

## Come funziona il DOM
Per capire come funziona React è utile avere una conoscenza di base di come i browser interpretano il codice per creare interfacce utente interattive.

Quando un utente visita una pagina web, il server restituisce al browser un file HTML. Il browser lo legge e costruisce il [[DOM|Document Object Model]] (o DOM):  
una rappresentazione strutturata della pagina web sotto forma di un **albero di oggetti**.  
Ogni elemento presente nel codice HTML (o XML) diventa un **nodo** all’interno di questo albero, con **relazioni padre-figlio** che ne definiscono la gerarchia.

![[DOM.png]]
I punti chiave per comprendere meglio il DOM sono:
1. Costruzione del DOM:
	- **Parsing dell'HTML:** 
	  Quando un utente visita una pagina web, il browser scarica il file HTML dal server.
	   Successivamente, analizza questo file e costruisce il DOM, ovvero una struttura ad albero che rappresenta tutti gli elementi della pagina.
	- **Relazioni tra i nodi:** 
	  In questa struttura ad albero ogni tag HTML (come `<div>`, `<p>`, `<img>`, ecc.) diventa un nodo dell’albero, e le relazioni di annidamento tra i tag (un tag contenuto in un altro) determinano le relazioni padre-figlio.
2. Interazione con il DOM:
	- **Accesso e manipolazione:** 
		Utilizzando linguaggi di programmazione come JavaScript, è possibile accedere ai nodi del DOM. Il linguaggio fornisce metodi per cercare, aggiungere, aggiornare o rimuovere elementi. Ad esempio, con `document.getElementById()` si può selezionare un elemento specifico.
    
	- **Gestione degli eventi:** 
		 È possibile ascoltare e rispondere ad azioni dell’utente (come click, tasti premuti o movimenti del mouse) associando dei listener agli elementi del DOM, rendendo l’interfaccia interattiva.
3. Ruolo nel contesto di framework come React
	-  **Astrazione della struttura:**
		  In librerie/framework come React il DOM tradizionale viene "astratto" in un Virtual DOM. Questo approccio permette di gestire in maniera più efficiente gli aggiornamenti, confrontando le versioni precedenti e quelle nuove della struttura per minimizzare le operazioni reali sul DOM del browser.
    
	- **Efficienza e prestazioni:** 
		   Utilizzando il Virtual DOM, React ottimizza il processo di aggiornamento della UI, intervenendo solo sui cambiamenti effettivi, il che risulta particolarmente utile per applicazioni complesse e interattive.

React è una libreria di JS per la creazione di interfacce utente (UI o User interface). 
Sviluppata nel 2013 all'intenro di Facebook, adesso React è una liberia open-source supportata da una grnade community di programmatori.
Inoltre consente 


> [!example] Riassumendo JS
> Originariamente, JavaScript è stato creato per essere eseguito nei browser, ma oggi,
grazie a tecnologie come Node.js e Deno, è possibile utilizzarlo anche al di fuori di essi.
Tuttavia, il focus di questo corso sarà su React, una libreria frontend basata su browser
per costruire interfacce utente.
• È utile sapere che JavaScript non è limitato ai browser. Con tecnologie aggiuntive come
Capacitor o React Native, è possibile sviluppare anche applicazioni mobili.
• In questo corso ci concentreremo su JavaScript nel contesto del browser. La sintassi e
le regole generali rimangono le stesse, indipendentemente dall'ambiente in cui si scrive il
codice.
• Per aggiungere JavaScript a un sito web, ci sono due opzioni principali: inserire il codice
direttamente nel file HTML utilizzando il tag `<script>` o importare file JavaScript esterni.
>L'approccio inline è sconsigliato per progetti più grandi, poiché può rendere il codice difficile da mantenere. In genere, è meglio mantenere il codice JavaScript in file separati.
>Nel contesto di un progetto React, è raro dover aggiungere manualmente questi tag di `script` al file HTML. I progetti React utilizzano spesso un processo di compilazione che inietta automaticamente questi tag.

### Import/export
Come in Python, anche in JavaScript l’uso delle istruzioni `import` e `export` è essenziale per mantenere il codice modulare, manutenibile e riutilizzabile, soprattutto nei progetti di grandi dimensioni sviluppati con framework come **React**, **Vue** e **Angular**.

Immagina di avere due file:
- `utils.js`, dove è definita una variabile chiamata `API_KEY`
    
- `App.js`, dove si vuole utilizzare tale variabile, di conseguenza la variabile `API_KEY` va esportata dal primo file, usando la keyword `export`:
```js
export let API_KEY = "chiave secreta"; 
```

In seguito andrà importata in `App.js` utilizzando la chiave `import`:
```js
import {API_KEY} from './utils.js'
console.log(API_KEY) //questo serve solo per stampare in console il valore della variabile
```

#### Varianti di dell'import e dell'export 
Esistono alcuni varianti tra l'esportazione e l'importazione di file e variabili, funzioni e oggetti 
1. **Esportazione predefinita:**
	 ==Si usa quando si vuole esportare **un solo elemento principale** da un file.==
   
   Tornando all'esempio fatto qui sopra dal file `utils.js`, siccome si esporta solo la variabile `API_KEY` si può usare l'export default, la sintassi è:
```js
export default valoreVariabile;
```

Di conseguenza, in questo caso l'esportazione sarà:
```js
export defualt "chiave segreta";
```

L'importazione nel file `App.js` quindi sarà:
```js
import miaChiave from './utils.js';
```

> [!info] Il nome usato durante l’importazione (`miaChiave`) è arbitrario nel caso di export default.



2. **Importazione multipla con alias:**
   ==È utile quando si vogliono importare **tutti gli elementi esportati** da un file in un unico oggetto alias== 
   La sintassi è:
```js
import * as nome_alias from './nomeFile.js';
```

Quindi l'export da `utils.js` in questo caso è:
```js
// utils.js
export let API_KEY = "chiave segreta";
export function saluta() {
  console.log("Ciao!");
}
```

Mentre l'import in `App.js`:
```js
// App.js
import * as util from './utils.js';

console.log(util.API_KEY);
util.saluta();
```
L'importazione multipla torna utile quando si ha un numero consistente di elementi da importare in un file.
In questo caso tutte le variabili (o funzioni, oggetti, etc.) sono raggruppate nell'oggetto `util`, e quindi per accedere a ciascuna di esse si utilizza la notazione a punti:
```js
console.log(util.API_KEY);
```

> [!NOTE] Come in Python, anche in JS è possibile usare degli alias per gli elementi che si importano in un file.
> Gli alias vengono assegnati agli elementi importati per migliorare la leggibilità e l'organizzazione del codice.


> [!NOTE] Nota:
>  In progetti React, Vue e Angular, l'estensione `.js` è spesso omessa durante l'importazione a causa del processo di compilazione.
>  Inoltre al tag `<script>` del HTML viene aggiunto un altro attributo oltre a `src = ""`; 
>  l'attributo **`type = "module"`**: 
>  ==questo attributo è necessario quando si lavora con JS vanilla per abilitare la sintassi di `import`/`export`==. 

3. **Esportazione multipla:**
	  ==Serve per esportare **più variabili o funzioni** dallo stesso file, usando `export` davanti a ciascuna dichiarazione.==
   La sintassi è: 
```
export dichiarazioneVariabile nomeVariabile = valoreVariabile
export dichiarazioneVariabile nomeVariabile2 = valoreVariabile2
```

Nel concreto questa sintassi diventa:
```js
// utils.js
export let API_KEY = "chiave segreta";
export let ANOTHER_VARIABLE = 12;
export function logKey() {
  console.log(API_KEY);
}
```


> [!hint] Tips & Tricks: Esportazione multplipla in blocco (con alias opzionali)
> Esiste un modo più compatto ed elegante per effettuare una esportazione multipla con alias in JS, senza scrivere `export` davanti a ogni singola variabile.
> Per farlo si dichiarano tutte le variabili normalmente e poi si fa un'unica esportazione alla fine del file:
>```js
>// utils.js
const API_KEY = "chiave segreta";
const ANOTHER_VARIABLE = 12;
function saluta() {
  console.log("Ciao!");
}
>
>// esportazione multipla in blocco
>export {
>  API_KEY,
 > ANOTHER_VARIABLE,
 > saluta
>};
>```
>Per rinominare ciascun elemento direttamente nell'`export`: 
>```js
>export {
>  API_KEY as chiave,
>  ANOTHER_VARIABLE as numero,
>  saluta as greet
>};
>```
>Di conseguenza in `App.js` si può importare le variabili con quei nomi:
>```js
>import { chiave, numero, greet } from './utils.js';
>```


Per importare questi elementi nel file `App.js`:

```js
// App.js
import { API_KEY, ANOTHER_VARIABLE, logKey } from './utils.js';
```

✅ In questo caso è necessario **conoscere esattamente i nomi** delle variabili esportate, poiché vanno indicati tra `{ }`.


> [!NOTE] Import nei progetti React, Vue, Angular
> - Nei progetti reali, l’estensione `.js` può essere omessa grazie ai **sistemi di bundling** (come Webpack, Vite o Parcel).
 >   
>- Nei file HTML che usano `import/export` con JavaScript vanilla (senza framework), è **obbligatorio** specificare l’attributo:
>```js
><script type="module" src="app.js"></script>
>```
>> [!bug] Senza `type="module"` non potrai usare `import` e `export` nei file JS.


### Variabili 
Come accennato nella lezione 2 di JS sulle [[Lezione 2 Le variabili in Javascript|variabili]] si possono dichiarare le variabili in 3 modi:
1. `var`: 
   ==dichiarazione con **scope globale o di funzione**==
2. `let`: 
   ==dichiarazione con **scope locale (di blocco)**==
3. `const`: 
   ==dichiarazione di **costanti** (cioè, una volta assegnato, il valore non può più essere cambiato)).== 

> [!info] È buona pratica in JS usare `const` quando si assegna un valore che **non deve cambiare** nel tempo, migliorando così la leggibilità e la sicurezza del codice

### Differenze tecniche tra i vari tipi di dichiarazione di una variabile
Abbiamo già introdotto [[Lezione 2 Le variabili in Javascript#Dichiarazione di una variabile|la differenza tra `var` e `let` ]] nella lezione 2, ora la vedremo nel dettaglio:
1. `var`:
   - **Function scope:**
     ==La variabile è visibile solo all'interno della funzione in cui è dichiarata oppure nello scope globale, se dichiarata all’esterno di una funzione== 
   - **Riassegnazione:**
     ==È possibile cambiare il valore più volte== 
   - **Inizializzazione:**
     ==Può essere dichiarata anche senza inizializzazione.==
   - **Può essere dichiarata di nuovo:**
     ==Una variabile `var` può essere dichiarata di nuovo nello stesso scope senza errori..==
```js
var z = 50;
if (true) {
  var z = 100; // Stesso z, viene sovrascritto
}
console.log(z); // 100

```

2. `let`:
   - **Block Scope:**
      ==La variabile è visibile solo all’interno del blocco `{}` in cui è dichiarata.==
   - **Riassegnazione:**
      ==È possibile cambiare il valore più volte.==
   - **Non inizializzata:**
     ==Può essere dichiarata senza inizializzare subito.==
   - **Non può essere dichiarata di nuovo:**
     ==Nel medesimo scope, non è possibile dichiarare di nuovo una variabile con lo stesso nome.==
```js
let x = 10;
if (true) {
  let x = 20; // È un altro x, visibile solo nel blocco
}
console.log(x); // 10

```

3. `const`:
   - **Block Scope:**
    ==Come `let`, anche `const` ha uno scope di blocco==
   - **Non riassegnabile:**
    ==Una volta assegnato un valore a una variabile `const`, non può essere riassegnato==. 
   - **Deve essere inizializzata:**
       ==Una variabile `const` deve essere inizializzata al momento della dichiarazione.==
   - **Non può essere dichiarata di nuovo:**
     ==Come `let`, anche una variabile `const` non può essere dichiarata di nuovo nello stesso scope.==
```js
const y = 30;
 y = 40; // Errore, non può essere riassegnata
```

Dietro queste differenze ci sono due concetti molto importanti in JS:
##### 1. L'hoisting:  
L’**hoisting** è un comportamento specifico di `var` in JavaScript:
 ==la dichiarazione viene "sollevata" all’inizio dello scope di riferimento, ma senza l’inizializzazione.==  
Questo significa che è possibile **accedere a una variabile `var` prima della sua dichiarazione**, ma il suo valore sarà `undefined`.
	Esempio di hoisting con `var`:
```js
console.log(a); // Output: undefined
var a = 5;
console.log(a); // Output: 5
```

> [!bug] Questo comportamento può portare a risultati inaspettati e potenzialmente a bug, ed è una delle ragioni per cui l'uso di `let` e `const` è generalmente preferito, poiché non presentano questo comportamento di hoisting.


> [!abstract] Cos'è davvero l'hoisting?
> Innanzitutto l'hoisting non riguarda l'inizializzazione ma solo la dichiarazione di una variabile.
> ==L’**hoisting** è un comportamento di JavaScript per cui le **dichiarazioni di variabili (con `var`) e funzioni** vengono “**spostate in alto**” (hoisted) **nello scope corrente** **prima dell’esecuzione del codice**.==
> Quindi nell'esempio:
>```js
>console.log(a); // Output: undefined
var a = 10;
console.log(a); //  Output: 10
>```
>Cioè in realtà succede questo dietro le quinte:
>```js
>var a;           //  dichiarazione "spostata in alto"
console.log(a);  //  undefined
a = 10;          //  assegnazione avviene dopo
console.log(a);  //  10
>```
>Come possiamo notare la dichiarazione viene spostata in alto, si prova a stampare in console la variabile `a` ma siccome non ha nessun valore risulta `undefined`, difatti il valore ad `a` viene assegnato dopo e quindi l'output del secondo `console.log()` risulterà `10`.
> ==Con `let` e `const` l'hoisting non avviene perché **esiste una "zona morta temporale" (TDZ)**, cioè una zona di codice in cui la variabile **esiste ma non può ancora essere usata**.== 


##### 2. Scope:
Lo **scope** determina **dove una variabile è visibile** e accessibile nel codice. In JavaScript esistono tre principali tipi di scope:

- **Global scope:**  
    ==La variabile è visibile **in tutto il programma** (tipico di `var` dichiarato fuori da una funzione).==
    
- **Function scope:**  
    ==La variabile è visibile **solo all’interno della funzione** in cui è dichiarata (tipico di `var`).==
    
- **Block scope:**  
    ==La variabile è visibile **solo all’interno del blocco** `{ ... }` in cui è stata dichiarata (tipico di `let` e `const`).==
```js
var number = 10;

if (true) {
  let messaggio = "Ciao!";
  const numero = 42;
}

console.log(messaggio); // ❌ Errore: messaggio non è definito fuori dal blocco
console.log(numero);    // ❌ Errore: numero non è visibile fuori dal blocco
console.log(number);    // ✅ 10 - var ha visibilità globale
```


> [!tip] Anche in questo caso è meglio **evitare `var`** per non incorrere in problemi di visibilità e comportamenti inaspettati legati all’hoisting. Preferisci `let` o `const` per un controllo più chiaro dello scope.


### Differenza tra `function` e  le Arrow Function: **Comportamento di `this`**
La **differenza principale** tra le funzioni normali (definite con `function`) e le **funzioni freccia** riguarda il **comportamento della parola chiave `this`**.
#### [[Lezione 5; Le funzioni in Javascript#Le funzioni|Funzioni normali (`function`)]]:
Il valore di `this` è **dinamico**: dipende **da come la funzione viene chiamata**:
1. Se la funzione è chiamata come **metodo di un oggetto**, `this` si riferisce a **quell’oggetto**.  
2. Se è chiamata **in modo indipendente**, `this` si riferisce all’**oggetto globale** (`window` in browser)  
3. Oppure è `undefined` in **strict mode.**
Per fare un esempio pratico:
```js
function mostraNome() {
  console.log(this.nome);
}

const persona = {
  nome: "Max",
  mostraNome: mostraNome
};

persona.mostraNome();      // ✅ Output: "Max"
const funzioneIsolata = persona.mostraNome;
funzioneIsolata();         // ⚠️ Output: undefined (o errore in strict mode)
```


> [!NOTE] Approfondimento su `this`
> Quando usi una **funzione normale**, `this` cambia **a seconda del contesto di invocazione**.  
>Questo può causare problemi se perdi il riferimento all’oggetto (come nell’ultimo esempio sopra).

#### [[Lezione 5; Le funzioni in Javascript#Arrow function|Arrow Function]] 
==Le **arrow function** non hanno un proprio `this`.==
Invece, **"ereditano" `this` dallo scope esterno** (quello in cui sono state definite). Questo comportamento si chiama **`this` lessicale**.
Esempio:

```js
const persona = {
  nome: "Max",
  mostraNome: function() {
    setTimeout(() => {
      console.log(this.nome); // ✅ funziona!
    }, 1000);
  }
};

persona.mostraNome(); // Output: "Max" dopo 1 secondo
```

In questo caso, la funzione freccia dentro `setTimeout` **eredita** il valore di `this` dal metodo `mostraNome`, permettendo di accedere a `this.nome`.
##### Confronto con `self` in Python
Possiamo vedere il `this` di JS come il [[Le Classi#**`Self` in Python**|`Self`]] in Python:
- entrambi si riferiscono all'oggetto (istanza)
- Permettono l'accesso agli attributi e metodi dell'oggetto
- Sono usati nei metodi degli oggetti
In quest'ultima voce in realtà si può notare la prima differenza:
il `self` di Python è usato come primo parametro dei metodi mentre il `this` è usato solo nei metodi degli oggetti e non inizializzato nel costruttore di una classe come in Python.

Esempio in Python:
```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print(f"Ciao, sono {self.nome}")
```

Qui il `self` viene usato come primo parametro del costruttore `__init__()` e il metodo `saluta()`, per accedere agli attributi di classe, eredita il `self`.

Esempio in JS:
```js
const persona = {
  nome: "Luca",
  saluta: function() {
    console.log("Ciao, sono " + this.nome);
  }
};

```

In questo caso viene creato l'oggetto `persona` e dentro il metodo `saluta()` viene passato come parametro il `this.nome`. 
Ciò significa che in console verrà visualizzato il valore della chiave `nome`, ovvero `"Luca"`.

Quindi le differenze principali possono essere schematizzate in questa tabella:

| Aspetto                    | `this` in JS                                      | `self` in Python                    |
| -------------------------- | ------------------------------------------------- | ----------------------------------- |
| **Esplicito o implicito**  | mplicito (non lo scrivi tra i parametri)          | Esplicito (è il primo parametro)    |
| **Comportamento dinamico** | Dinamico (dipende da **come** chiami la funzione) | Statico (self è sempre l’istanza)   |
| **Può cambiare valore**    | Sì, con `call`, `apply`, `bind`                   | No, è sempre l’istanza della classe |
| **Arrow functions**        | Non hanno `this` proprio (ereditano dallo scope)  | Non esiste un equivalente diretto   |


> [!example] In sinstesi
> - In **Python**, `self` è **sempre chiaro**: fa riferimento all'istanza della classe, punto.
  >  
>- In **JavaScript**, `this` può cambiare **a seconda del contesto** in cui chiami la funzione (tranne nelle arrow function, dove è "fissato").

### Gli oggetti in Javascript
Ora che abbiamo esplorato le funzioni, torniamo a parlare dei **valori**, e in particolare degli **[[Gli oggetti in Javascript#Cos'è un oggetto in JS|oggetti]]**:
==**gli oggetti in JavaScript** servono per **raggruppare più valori** sotto un'unica entità.==
Un oggetto in JS può essere creato in questo modo attraverso la literal object:
Ad esempio, se si ha un nome utente, ome `"Rob"`, e un'età, come `46`, posso raggruppare questi dati in un oggetto chiamato `utente`.

```js
const utente = {
  nome: "Rob",
  eta: 46
};
```
La creazione di oggetti in JS è un array associativo di chiave-valore (come nei [[Collections#I dictionaries|dizionari di python]] o i file [[File in Python#File JSON|JSON]]).
Questo oggetto può essere stampato nella console per ispezionarne il contenuto.  
Si può anche accedere ai suoi **singoli campi** usando la **notazione a punti**, come:
````js`
console.log(utente.nome); // Output: "Rob"
```

#### Metodi: Funzioni dentro oggetti
Oltre a contenere semplici coppie **chiave-valore**, ==gli oggetti possono anche contenere **funzioni**, che in questo contesto vengono chiamate **metodi**==.
Esempio:

```js
const utente = {
  nome: "Rob",
  eta: 46,
  saluta: function() {
    console.log("Ciao!");
    console.log(this.nome); // Accede al nome dell'oggetto
  }
};

utente.saluta(); // Output: "Ciao!" seguito da "Rob"
```

All'interno di un metodo, possiamo usare la parola chiave **`this`** per accedere ad **altre proprietà** dello stesso oggetto.

>[!NOTE]  
>Ricorda: in una funzione **normale** (non arrow), `this` fa riferimento all’oggetto che chiama il metodo — in questo caso `utente`.

### Classi: un altro modo per creare oggetti
Un altro modo per creare oggetti è tramite l'uso delle **classi**, introdotte in ES6.  
Una classe funziona come un **"progetto" (template)** per creare oggetti con la stessa struttura.

Esempio:
```js
class Utente {
  constructor(nome, eta) {
    this.nome = nome;
    this.eta = eta;
  }

  saluta() {
    console.log("Ciao! " + this.nome);
  }
}

const utenteUno = new Utente("Manuel", 35);
utenteUno.saluta(); // Output: "Ciao! Manuel"
```

Qui:

- `Utente` è una **classe**
    
- `utenteUno` è un’**istanza** di `Utente`
    
- Il metodo `saluta()` può accedere a `this.nome` perché fa parte della stessa istanza.

A differenza di **Python**, dove il riferimento all’istanza corrente (`self`) è passato **esplicitamente** come **primo parametro** nei metodi (incluso [[Le Classi#**Definizione di una Classe e il Costruttore** `__init__()`|il costruttore `__init__()`]] ), in JavaScript il riferimento all’oggetto viene gestito **in automatico** tramite la parola chiave `this`.

>[!NOTE]  
>Questo rende `this` in JavaScript **più potente ma anche più insidioso** rispetto a `self` in Python, soprattutto se usi funzioni freccia (\=>) o perdi il contesto.

### Array di Js
Come abbiamo visto nella lezione 3 al capitolo [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Definire Array in JS|Definire Array in JS]], gli array in JS sono oggetti ma rappresentano una categoria speciale di essi.
La sintassi è:
```js
let nomeVariabile = [...]
```

Quindi a differenza degli oggetti veri e propri, che utilizzano coppie di chiave valore, gli array memorizzano solo valori in ordine specifico e sono accessibili tramite l'indice degli elementi, che è zero based (di base sono [[Collections#Le liste|le liste in Python]]).

Ad esempio, se ho una lista di hobby come sport, cucina e lettura, posso accedere a questi valori utilizzando l'indice. 
```js
const hobbies = ['sport', 'cucina', 'lettura'];
// accesso tramite indice
console.log(hobbies[0]); // Output: "sport"
console.log(hobbies[1]); // Output: "cucina"

```
Gli array sono molto comuni in JavaScript perché spesso è necessario memorizzare liste di valori. Possono contenere qualsiasi tipo di valore, inclusi altri array e oggetti.

Gli array offrono vari metodi utili:
- il metodo `push`:
	  aggiunge un nuovo elemento all'array.  ^729767
```js
 hobbies.push('lavoro');
console.log(hobbies); // ["sport", "cucina", "lettura", "lavoro"]
```
^pushMethod

- Il metodo  `findIndex`:
	   ==trova l'indice di un determinato valore.== 
	   Questo metodo accetta una funzione come input, che viene eseguita per ogni elemento dell'array.
```js
const index = hobbies.findIndex(item => item === 'sport');
console.log(index); // 0
```
Un altro metodo frequentemente utilizzato è `map`: 
	 ==trasforma ogni elemento dell'array in un altro elemento.== 
```js
const modified = hobbies.map(item => item + '!');
console.log(modified); // ["sport!", "cucina!", "lettura!", "lavoro!"]
```
 
 Come `findIndex`, anche `map` accetta una funzione come input. Questa funzione viene eseguita per ogni elemento dell'array, e il valore restituito diventa il nuovo elemento dell'array.
 Ad esempio partendo dall'array `hobbies` posso trasformare gli elementi in oggetti:
```js
const objectHobbies = hobbies.map(item => ({ text: item }));
console.log(objectHobbies);
// [{ text: "sport" }, { text: "cucina" }, { text: "lettura" }, { text: "lavoro" }] 
```

In sintesi, gli array sono strumenti potenti per memorizzare e manipolare liste di valori in JavaScript. Offrono una varietà di metodi utili per la manipolazione e l'accesso ai dati, rendendoli strumenti indispensabili per qualsiasi sviluppatore JavaScript.

### Assegnazione per riferimento in JS 
Per comprendere bene come Javascript assegna i valori alle variabili e agli oggetti e array bisogna distinguere l'assegnazione per valore e l'assegnazione per riferimento:
- I **tipi primitivi** (come numeri, stringhe, booleani) sono assegnati **per valore**.
    
- Gli **oggetti** e gli **array** (che sono oggetti complessi) sono assegnati **per riferimento**.

#### Assegnazione per riferimento = stessa posizione in memoria
Quando si assegna un oggetto o un array a una nuova variabile non si sta creando una copia ma si sta dicendo all'interprete di JS che quella variabile sta puntando allo stesso oggetto in memoria:
```js
const persona1 = { nome: 'Mario', eta: 30 };
const persona2 = persona1;

persona2.nome = 'Luigi';

console.log(persona1.nome); // "Luigi"
console.log(persona2.nome); // "Luigi"
```
 Se si modifica `persona2` si modifica anche `persona1`, poiché sono lo stesso oggetto in memoria. 

Per fare un ulteriore esempio con un array:
```js
const array1 = [1, 2, 3];
const array2 = array1;

array2.push(4);

console.log(array1); // [1, 2, 3, 4]
console.log(array2); // [1, 2, 3, 4]
```

Qui `array1` viene assegnato a `array2`, ma **non si crea una copia**: entrambe le variabili puntano **allo stesso array in memoria**.  
Usando [[#^729767|`push(4)`]] su `array2`, anche `array1` viene modificato, perché sono lo **stesso oggetto**.

 
> [!caution] È fondamentale conoscere questa distinzione tra **assegnazione per valore** e **per riferimento**, perché potresti modificare dati in modo **inconsapevole**, causando bug difficili da individuare.


> [!hint] Per evitare che due variabili puntano allo stesso oggetto in memoria
> 
>```js
>const array1 = [1, 2, 3];
const array2 = [...array1]; // Crea una copia indipendente
>
>array1.push(99);
>
>console.log(array1); // [1, 2, 3, 99]
>console.log(array2); // [1, 2, 3] ✅ 
>```
>In questo modo `array2` rimane immutato anche se cambi `array1`, perché ora **sono due array distinti** in memoria.

### Destrutturazione 

Un'altra caratteristica importante di JS, introdotta dall'ES6, è: la destrutturazione di array e oggetti.
==La **destrutturazione** è una funzionalità di JavaScript che permette di **estrarre valori da array o oggetti** e assegnarli a variabili in modo semplice e leggibile.==

#### Destrutturazione degli array
Immaginiamo di avere un array con nome e cognome dell'utente:
```js
const userData = ['Mario', 'Rossi'];
```

Per accedere agli elementi di questo array, secondo il metodo tradizionale, si usa l'indexing:
```js
const userData = ['Mario', 'Rossi'];
const firstname = userData[0];
const lastname = userData[1];
console.log(firstname) //output : 'Mario'
console.log(lastname) //output : 'Rossi'
```

Tuttavia questo metodo può risultare pedante e noioso soprattutto con array molti lunghi, di conseguenza si usa destrutturare un array (cioè estrarre i valori):
```js
const userData = ['Mario', 'Rossi'];
const [firstname, lastname] = userData;
console.log(firstname); // "Mario"
console.log(lastname);  // "Rossi"
```

**Spiegazione:**
- `const [firstname, lastname] = userData;`: 
	  ==estrae i valori di `userData` e li assegna alle variabili `firstname` e `lastname`. Queste variabili conterranno una copia dei valori (tipi primitivi), non un riferimento all'intero array.==


Si usano le parentesi quadre (`[]`) per indicare che si sta destrutturando un array.
Si può scegliere qualsiasi nome per le variabili, ma  si deve rispettare l'ordine e la quantità degli elementi dell'array.



#### Destrutturazione di un oggetto
Come detto prima si possono anche destrutturare gli oggetti.
Immaginiamo un oggetto utente:
```js
const user = {
  name: 'Mario',
  age: 30
};
```

Per estrare i valori dall'oggetto con il metodo tradizionale si fa:
```js
const name = user.name;
const age = user.age;
```

mentre con la destrutturazione:
```js
const user = {
  name: 'Mario',
  age: 30
};

const { name, age } = user;
console.log(name); // "Mario"
console.log(age);  // 30
```

A differenza della destrutturazione degli array, dove si usano le parentesi quadre (`[]`), per gli oggetti si utilizzano le parentesi graffe (`{}`) per indicare che si sta destrutturando un oggetto.
In questo caso, a differenza con gli array, le variabili devono avere lo stesso nome delle proprietà dell'oggetto.

##### Destrutturazione con alias
Quando si destruttura un oggetto si possono rinominare le variabili durante la destrutturazione:
```js
const user = {
  name: 'Mario',
  age: 30
};

const { name: userName, age: userAge } = user;
console.log(userName); // "Mario"
console.log(userAge);  // 30
```

Qui si sta dicendo di prendere la chiave `name` e rinominarla `userName`, e di prendere la chiave `age` e rinominarla `userAge`.


#### Destrutturazione di parametri delle funzioni
==La destrutturazione può essere utilizzata anche direttamente nei **parametri di una funzione**, permettendoti di estrarre le proprietà di un oggetto **senza doverle accedere manualmente** nel corpo della funzione.==
Prendiamo ad esempio una funzione che accetta un parametro che conterrà un oggetto, questo può essere destrutturato per estrarre le proprietà dell'oggetto e renderle disponibili come variabili con scope locale (cioè variabili disponibili solo all'interno del corpo della funzione).
Esempio tradizionale senza destrutturazione:

```js
function storeOrder(order) {
	localStorage.setItem('id', order.id);
	localStorage.setItem('currency', order.currency);
}
```

Invece di accedere alle proprietà dell'ordine tramite la canonica "notazione a punto" all'interno del corpo della funzione `storeOrder` si utilizza la destrutturazione:

```js
function storeOrder({id, currency}) { // destrutturazione
	localStorage.setItem('id', id);
	localStorage.setItem('currency', currency);
};
```

In questo esempio:

- La funzione riceve ancora **un solo oggetto come parametro**.
    
- Solo che le sue proprietà (`id`, `currency`) vengono **destrutturate direttamente** tra le parentesi della funzione.
    
- È come se dicessi: "Appena ricevi l'oggetto, prendi `id` e `currency` e rendili disponibili come variabili locali".
- Quindi nella chiamata della funzione:
```js
storeOrder({ id: 5, currency: 'USD', amount: 15.99 }); 
```

Anche se l’oggetto contiene **più proprietà**, verranno estratte solo quelle specificate (`id` e `currency`), ignorando le altre (`amount` in questo caso).

Quindi la destrutturazione è molto utile quando lavori con oggetti strutturati, come dati provenienti da un'API, e ti permette di scrivere codice più pulito ed esplicito.


### Spread operator

Un’altra caratteristica fondamentale di JavaScript (introdotta con ES6) è **l’operatore di spread**, rappresentato da tre punti: `...`.

==Serve per **espandere** (cioè "spargere") gli elementi di un **array** o le **proprietà di un oggetto** all’interno di un altro array o oggetto.==

#### Spread con gli array
Immaginiamo di avere due array di hobby e di volerli unire:
```js
const hobby1 = ['Nuoto', 'Ciclismo'];
const hobby2 = ['Lettura'];
```

Per fare ciò senza spread:
```js
const unioneSenzaSpread = [hobby1, hobby2];
console.log(unioneSenzaSpread);
// Output: [['Nuoto', 'Ciclismo'], ['Lettura']] (array annidato)
```

In questo caso stiamo **inserendo** gli array `hobby1` e `hobby2` **come interi elementi** all'interno di un nuovo array, ottenendo un array **annidato**.
Il che potrebbe anche andare bene se si volesse ottenere questo risultato.

Mentre con lo spread:

```javascript
const unioneConSpread = [...hobby1, ...hobby2];
console.log(unioneConSpread);
// Output: ['Nuoto', 'Ciclismo', 'Lettura']
```

**Spiegazione:**
-  `...hobby1`: 
	  ==`...hobby1` estrae ciascun elemento dell’array `hobby1` e lo inserisce nel nuovo array come elemento indipendente.==
    
- `...hobby2`: 
	  ==fa lo stesso con `['Lettura']`==
    
- Tutti gli elementi vengono **inseriti come singoli valori** nel nuovo array.

#### Spread con gli oggetti
Lo spread operator può essere usato anche con gli **oggetti** per **unirne le proprietà**.
```js
const utente = { name: 'Mario', age: 30 };
const utenteEsteso = { isAdmin: true, ...utente };
console.log(utenteEsteso);
// Output: { isAdmin: true, name: 'Mario', age: 30 }
```

**Spiegazione:**
- **Lo spread `...utente`:** 
	  ==prende tutte le coppie chiave-valore dall’oggetto `utente`==
    
- ==Le "espande" nell’oggetto `utenteEsteso`==
    
- ==Il risultato è un nuovo oggetto che **unisce** tutte le proprietà== 


> [!danger] **Attenzione:** se ci sono **chiavi duplicate**, prevale **l’ultima definita** (quella più a destra).
>```js
>const obj = { a: 1, ...{ a: 2 } };
>console.log(obj); // { a: 2 } 
>```


#### Clonazione e sovrascrittura
Inoltre lo spread è spesso usato per **clonare** o **modificare** oggetti senza alterare l’originale:

```js
// Clonazione semplice
const originale = { nome: 'Luca', età: 25 };
const copia = { ...originale };
console.log(copia); // { nome: 'Luca', età: 25 }

// Sovrascrittura
const utente = { nome: 'Mario', ruolo: 'user' };
const nuovoUtente = { ...utente, ruolo: 'admin' };
console.log(nuovoUtente); // { nome: 'Mario', ruolo: 'admin' }
```



> [!done] **Quando si usa lo spread operator?**
> - Per evitare array annidati o codice verboso
  >  
>- Per **unire** o **clonare** array e oggetti facilmente
 >   
>- Infine, per scrivere codice più **leggibile e conciso**


> [!example] **In sintesi**
> Lo spread operator `...` permette di:
 >- Espandere gli elementi di un **array** in un altro array
 >   
>- Espandere le proprietà di un **oggetto** in un altro oggetto
  >  
>- È utile per unire, copiare, o modificare dati senza mutare quelli originali


### Rest parameters 
I rest parameters in JS sono l'opposto dello spread operator:
- **Spread operator:**
	  - Espandono scomponendo i valori o gli elementi di un array o un oggetto.
	  - Vengono usati al di fuori dei parametri di una funzione 
	  - Lavorano con array e oggetti
	  - lo spread operator può essere messo in qualsiasi punto della destrutturazione 

- **Rest parameters:**
	- Raccoglie/raggruppa comprimendo i valori di un array
	- Viene usato all'interno dei parametri di funzione
	- Lavora con argomenti di funzioni, array
	- Deve essere messo come ultimo parametro 

Quindi  i Rest parameters, **raccolgono più valori in un array**. 
==Si usa spesso nei **parametri delle funzioni** per gestire un numero variabile di argomenti.== 
Per fare un esempio più concreto:
```js

function somma(...numeri) {
  return numeri.reduce((acc, curr) => acc + curr, 0);
}

console.log(somma(1, 2, 3, 4)); // Output: 10
```

^325e65

**Spiegazione:**

- `function somma(...numeri) {}`  
    La funzione utilizza i **rest parameters** (`...numeri`) per raccogliere tutti gli argomenti in un array chiamato `numeri`.
    
- `numeri.reduce((acc, curr) => acc + curr, 0)`  
    È un metodo che **riduce l’array a un singolo valore**.
    
    - `acc` (accumulatore): 
	    ==è il **valore totale accumulato** fino a quel punto.==
        
    - `curr` (corrente): 
	      ==è il **valore corrente dell’elemento dell’array** durante l’iterazione.==
        
    - `0`: è il **valore iniziale dell'accumulatore**.  
        → ==In questo caso, si parte da `0` e si sommano tutti gli elementi uno dopo l'altro.== 
        

✅ Quindi: `reduce` esegue qualcosa tipo  
`0 + 1 → 1` 

`1 + 2 → 3`  

`3 + 3 → 6`  

`6 + 4 → 10`

> [!example] **In sintesi**
>  La differenza tra gli spread operators e i rest parameters è:
> - Rest parameters: 
>   ==sono utili quando non si sa in anticipo quanti argomenti verranno passati a una funzione come nell'[[#^325e65|esempio poco sopra]].==
> - Spread operators: 
>   ==Utile quando vogliamo espandere un array/oggetto in un altro contesto, evitando strutture annidate o aggiungendo/modificando i valori.==
> 
