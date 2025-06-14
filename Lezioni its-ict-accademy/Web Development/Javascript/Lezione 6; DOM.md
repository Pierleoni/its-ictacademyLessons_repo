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

```
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
Ora che abbiamo esplorato le funzioni, torniamo a parlare dei **valori**, e in particolare degli **oggetti**:
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
```
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
