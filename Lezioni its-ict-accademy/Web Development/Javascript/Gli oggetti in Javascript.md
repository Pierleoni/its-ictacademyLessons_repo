# Introduzione
Abbiamo dato una prima definizione di cosa sono gli oggetti in JS nella [[Lezione 6; DOM e ripasso JS]] al capitolo [[Lezione 6; DOM e ripasso JS#Gli oggetti in Javascript|Gli oggetti in Javascript]], ora approfondiremo meglio **cosa sono**, **come si usano** e **perché sono importanti**.

## Cos'è un oggetto in JS
Un **oggetto** è una **variabile complessa** che consente di raggruppare più informazioni sotto un’unica struttura.

>**Definizione tecnica:**  
>==Un oggetto è una **collezione di proprietà**: ogni proprietà è una **coppia chiave-valore**(simile ai [[Collections#I dictionaries|_dizionari]]_ in Python o agli _oggetti JSON_).== 


### Sintassi 
La sintassi degli oggetti in JS è la seguente:
```js
const nomeOggetto = {
  chiave1: valore1,
  chiave2: valore2
};

```

Ad esempio il modo per creare un semplice oggetto è :
```js
var automobile = {
  marca: "Fiat",
  modello: "500",
  colore: "Rosso"
};
```

In questo esempio:

- `marca`, `modello` e `colore`: 
	  ==sono le **proprietà** dell’oggetto `automobile`==
    
- `"Fiat"`, `"500"`, `"Rosso"`: 
	  ==sono i relativi **valori**== 
    

> [!note]   **Nota:**
> ==Le **chiavi** (o proprietà) sono separate dai **valori** tramite i `:`==  
> ==L’intero oggetto è racchiuso tra `{}` e **termina con `;==`**

Per accedere ad una proprietà di un oggetto è sufficiente richiamare il nome della variabile e tramite l'**operatore dot (cioè il punto(`.`))** si può accedere all'oggetto richiamando la sua proprietà. 
Tornando all'esempio dell'automobile per stampare a video la marca dell'oggetto si può scrivere:
```js
var automobile = {marca :" Fiat", modello :"500", colore: " Rosso"};
document.write(automobile.marca) //Output:Fiat
```

### Metodo alternativo con `new Object()`
Un altro modo alternativo per dichiarare e istanziare un oggetto è:
```js
var automobile = new Object();
automobile.marca = "Fiat";
automobile.modello = "500";
automobile.colore = "Rosso";
document.write(automobile.marca) //Output: Fiat
```


> [!info] Differenza tra la **literal syntax(`{}`)** e il costruttore `new Object()`
> **Metodo 1: Literal Syntax (sintassi letterale)**
>```js
>const automobile = {
  marca: "Fiat",
  modello: "500",
  colore: "Rosso"
};
>```
>> [!done] **Vantaggi**
>> - Più semplice, leggibile, conciso e moderno
>> - È il metodo consigliato e più utilizzato oggi poiché è il più veloce in esecuzione (internamente è più ottimizzato dai motori JavaScript).
>
>
> **Metodo 2: Costruttore `new Object()`**
> 
> 
>```js
>const automobile = new Object();
>automobile.marca = "Fiat";
>automobile.modello = "500";
>automobile.colore = "Rosso"; 
>```
>
>
>> [!fail] **Svantaggi:**
>> - Più verboso perché si scrive più righe di codice rispetto alla literal syntax.
>> - Meno chiaro e leggibile per chi studia o mantiene il codice
>> - Difatto oggi questo metodo viene considerato obsoleto e si tende molto di più ad usare la literal syntax
>
>
>Di conseguenza la **literal syntax (`{}`)**  è sempre usata per definire gli oggetti in JS, soprattutto con metodi semplici e medi.
>Mentre la `new Object()` non è quasi mai usata se non in casi specifici come quelli didattici o quando si usano metodi dinamici o costruttori personalizzati.
>
>>[!example]  In sintesi:
>> **Usare sempre la sintassi `{}`** per creare oggetti.  
>> Il costruttore `new Object()` è più vecchio e meno pratico.  
>> Entrambi producono lo **stesso tipo di oggetto**, ma il primo è **più moderno e raccomandato**.

### Oggetti innestati 
Si può **inserire un oggetto come valore di una proprietà** di un altro oggetto.  
Questo è utile quando si vuole rappresentare **strutture complesse**, ad esempio una persona con un indirizzo:
```js
const persona = {
	nome: 'Mario',
	cognome: 'Rossi',
	eta: 30,
	indirizzo: {
		via: 'Via casilina',
		civico: 23
		}
}
```

#### Accesso a una proprietà interna

Per richiamare una proprietà di un oggetto innestato, come per gli oggetti non innestati, è sufficiente usare sempre l’operatore dot (`.`) partendo sempre dall'oggetto principale :
```js
document.write(persona.indirizzo.via); //Output: Via Casilina
```

#### Array di oggetti innestati
Immaginiamo il caso in cui si hanno più indirizzi dello stesso utente, per inserirli si possono usare gli array:


```js
var persona = {
	nome: ‘’Mario’’,
	cognome: ‘’Rossi’’,
	eta: 30,
	indirizzo: [{
		via: ‘’Via casilina’’,
		civico: 23
	},{
		via: ‘’Via prenestina’’,
		civico: 110
	}]
}
document.write(persona.indirizzo[1].via); //Output: Via Prenestina
```

`document.write(persona.indirizzo[1].via);`: accede a un oggetto dell'array, in questo caso accede all'oggetto che trova all'indice `1`
### Funzioni negli oggetti in JS

In JavaScript, gli **oggetti** possono contenere:

- ==**Proprietà** (cioè dati)==
    
- ==**Metodi** (cioè funzioni associate a quell'oggetto)==
    

 La **sintassi** per inserire una funzione (metodo) dentro un oggetto:
```js
var persona = {
  nome: "Mario",
  cognome: "Rossi",
  eta: 30,
  indirizzo: [
    {
      via: "Via Casilina",
      civico: 23
    },
    {
      via: "Via Prenestina",
      civico: 110
    }
  ],
  
  stampa: function(nome, cognome) {
    document.write(nome + " " + cognome);
  }
};

// Chiamata del metodo
persona.stampa("Riccardo", "Cattaneo");
 
```

**Spiegazione:**

- `stampa: function(nome, cognome) { ... }`  
    Questo è un **metodo** dell’oggetto `persona`.  
    ==È una **funzione definita come valore** di una proprietà chiamata `stampa`.==
    
- Quando scrivi `persona.stampa("Riccardo", "Cattaneo")`, stai dicendo:  
    “==Chiama il metodo `stampa` dell’oggetto `persona` e passagli questi due argomenti”==.
    
- Dentro il metodo viene stampato il **nome completo** con `document.write`.

### Gli array associativi in JS (oggetti con chiavi stringa)
In JavaScript, può capitare di voler usare **nomi di proprietà** (chiavi) che contengono **spazi, trattini o parole riservate**. In questi casi, non possiamo usare la notazione classica con il punto `.`.  
Dobbiamo usare invece le **parentesi quadre** `["..."]`.

```js
let book={
	"main title":"Libro Javascript",
	"sub-title":"Linguaggio potente",
	for:"Developer",
	author:{
		firtname:"Rob",
		lastname:"Del"
	}
};
```

In questo oggetto:

- `"main title"` e `"sub-title"` contengono **spazi o simboli speciali**
    
- `"for"` è una **parola riservata** in JavaScript
    
- `author` è un **oggetto annidato** (con altre proprietà dentro)

Abbiamo visto che in JS c'è un modo per accedere alle proprietà ed è attraverso la dot notation (`.`):
```js
let book={
	"main title":"Libro Javascript",
	"sub-title":"Linguaggio potente",
	for:"Developer",
	author:{
		firtname:"Rob",
		lastname:"Del"
	}
};

console.log(book.author.firstname); //"Rob"
```
Che è semplice e leggibile, inoltre funziona solo se la chiave è un identificatore valido (cioè non ha spazi o simboli).

Tuttavia si può accedere alle chiavi dell'oggetto con le parentesi quadre `[""]` (come per i [[Collections#Annidare i dizionari|dizionari]] di Python):
```js
console.log(book["main title"]);    // "Libro Javascript"
console.log(book["sub-title"]);     // "Linguaggio potente"
console.log(book["for"]);           // "Developer"
```

Questo metodo funziona sempre, viene utilizzato al posto della dot notation quando la chiave:
- Contiene spazi (`"main title"`)
    
- Ha simboli non validi per un identificatore (`"sub-title"`)
    
- È una parola riservata (`"for"`)

Questo tipo di struttura (dove ogni chiave stringa corrisponde a un valore) è detta array associativo:
==**Gli array associativi non esistono in JS come struttura a sé stante.**==  
Quando si vuole un comportamento da array associativo, si usano gli **oggetti**,  e **non gli array**.
Questo perché come visto prima gli oggetti in JS sono pensati per usare **chiavi stringa** (o simboli) e rappresentare **entità complesse** (es. persona, auto, libro).
Quindi in sostanza in JavaScript, **gli oggetti sono array associativi**:  
==raccolgono coppie chiave–valore, dove le chiavi sono (di solito) stringhe, e i valori possono essere di qualsiasi tipo.== 

### Modello a oggetti

A differenza di linguaggi come **Python** o **Java**, che sono OOP (object-oriented programming) basati su **classi**, JavaScript è un linguaggio **orientato agli oggetti e agli eventi**, ma basato sui **prototipi**.

> Anche se dalla versione **ES6** JavaScript ha introdotto la sintassi `class`, **internamente** continua a usare i **prototipi**.



####  Classi vs Prototipi

Nei linguaggi a classi (come Java o Python), troviamo due concetti distinti:

- **Classi**: sono modelli astratti che definiscono le **proprietà** e i **metodi** condivisi da un gruppo di oggetti.  
    _Esempio_: la classe `Impiegato` definisce cosa significa essere un dipendente (nome, ruolo, stipendio...).
    
- **Istanze**: sono **oggetti reali** creati a partire da una classe.  
    _Esempio_: `Luca` può essere un’istanza della classe `Impiegato`, con nome="Luca" e stipendio="2000€".
    



In JavaScript non ci sono classi tradizionali, ovvero:
JavaScript **non separa classi e istanze**. 
==Invece, **tutto è un oggetto**, e ogni oggetto può **ereditarne le proprietà** da un altro oggetto chiamato **prototipo**==.

#### 👇 Ecco cosa significa:

- ==Invece di creare una "classe Impiegato", puoi creare **un oggetto modello (prototipo)** da cui derivare altri oggetti.==
    
- ==Quando crei un nuovo oggetto, puoi collegarlo a un **prototipo**, così eredita tutte le sue proprietà e metodi.==
    
- ==Questo è chiamato **ereditarietà prototipale**.==

#### Il costruttore
In JavaScript non è necessario definire una classe per creare un oggetto: possiamo semplicemente scriverlo **al momento**, usando la notazione letterale.
Ad esempio: 
```js
var persona = {
	nome: "Mario",
	cognome: "Rossi",
	indirizzo: "Via Garibaldi, 50 - Roma",
	email: "mario.rossi@html.it",
	mostraNomeCompleto: function() { ... },
	calcolaCodiceFiscale: function() { ... }
}
```
Questa modalità è semplice, ma ha un limite: **non è riutilizzabile**.  
Se dobbiamo creare **più oggetti con la stessa struttura**, dovremmo riscrivere tutto ogni volta.

Tuttavia immaginiamo però di aver bisogno di più oggetti dello stesso tipo, ad esempio di più oggetti persona, che condividono la stessa struttura:
Utilizzando la notazione letterale saremmo costretti a ripetere la definizione per ciascun oggetto che vogliamo creare. 
In altre parole, ricorrendo alla notazione letterale nella definizione degli oggetti otteniamo un risultato non riutilizzabile.
Per evitare quindi di dover ridefinire da zero oggetti che hanno la stessa struttura possiamo ricorrere ad un costruttore:
==Un **costruttore** è una normale funzione JavaScript che ci permette di creare più oggetti simili, e si usa insieme all’operatore `new`.== 

Vediamo ad esempio come creare un costruttore per l’oggetto persona:
```js
function Persona() {
	this.nome = "";
	this.cognome = "";
	this.indirizzo = "";
	this.email = "";
	this.mostraNomeCompleto = function() {
		// codice per mostrare il nome completo
	};
	this.calcolaCodiceFiscale = function() {
		// codice per calcolare il codice fiscale
	};
}
```

==Questa funzione definisce le proprietà del nostro oggetto assegnandole a se stessa ([[Lezione 6; DOM e ripasso JS#Differenza tra `function` e le Arrow Function **Comportamento di `this`**|`this`]]) in qualità di oggetto ed impostando i valori predefiniti==. 

Per creare un oggetto di tipo `persona` dovremo a questo punto invocare la funzione premettendo l’operatore `new`:
==serve per creare un nuovo oggetto a partire da una funzione costruttore o da una classe.==   ^newOp

```js
var marioRossi = new persona();
marioRossi.nome = "Mario";
marioRossi.cognome = "Rossi";

var giuseppeVerdi = new persona();
giuseppeVerdi.nome = "Giuseppe";
giuseppeVerdi.cognome = "Verdi";
```

In questo modo possiamo creare quanti oggetti vogliamo **senza duplicare il codice**.  
Modifichiamo solo i valori che ci servono.


> [!abstract] In pratica cosa fa `new`?
>```js
> let persona1 = new Persona("Mario", "Rossi");
>
>```
> JavaScript fa 4 cose **dietro le quinte**:
>
>1. **Crea un nuovo oggetto vuoto**:  
   > ==Come se facesse `let obj = {};`==
  >  
>2. **Imposta il prototipo** dell’oggetto creato:  
 >   ==Collega l’oggetto al prototipo della funzione costruttore:==  
  >  `obj.__proto__ = Persona.prototype`
 >   
>3. ==**Chiama la funzione costruttore** con `this` riferito al nuovo oggetto:==  
 >   ==`Persona.call(obj, "Mario", "Rossi")`==
  >  
>4. **Restituisce l’oggetto creato**:  
 >   ==`persona1` ora è il nuovo oggetto inizializzato.==
 >
 >> [!example] **Esempio semplice**
>>```js
>function Persona(nome, cognome) {
 >this.nome = nome;
 > this.cognome = cognome;
>let persona1 = new Persona("Mario", "Rossi");
>console.log(persona1.nome); // Mario
>>```
>>Se **non usi `new`**, la funzione `Persona()` viene semplicemente **eseguita**, ma `this` **non si riferisce a un nuovo oggetto**, quindi il comportamento sarà sbagliato o imprevedibile.
>>


Nella definizione di un costruttore possiamo prevedere la presenza di parametri che possiamo utilizzare nell’inizializzazione del nostro oggetto.
Consideriamo ad esempio la seguente definizione del costruttore dell’oggetto `persona`:
```js
function persona(nome, cognome) {
	this.nome = nome;
	this.cognome = cognome;
	this.indirizzo = "";
	this.email = "";
	this.mostraNomeCompleto = function() {...};
	this.calcolaCodiceFiscale = function() {...};
}
```

Esso ci consente di creare ed inizializzare un oggetto specificando i valori nella chiamata al costruttore:

```js
var marioRossi = new persona("Mario", "Rossi");
var giuseppeVerdi = new persona("Giuseppe", "Verdi");
```

È fondamentale utilizzare l’operatore `new` nella creazione di
un oggetto tramite costruttore. 
Infatti se lo omettiamo, magari per dimenticanza, quello che otterremo non sarà la creazione di un oggetto ma l’esecuzione della funzione, con risultati imprevedibili. 
Ad esempio, se tentiamo di creare un oggetto persona omettendo l’operatore `new`:
```js
var marioRossi = persona();
```

il valore della variabile `marioRossi` sarà `undefined`, dal momento che la funzione `persona()` non restituisce alcun valore.

#### Utilizzare le classi 
Un altro modo per creare oggetti in JavaScript è tramite le **classi**, introdotte con **ES6** (EcmaScript 2015).

Una **classe** può essere vista come un **modello** o **progetto** per costruire oggetti: ==definisce **quali proprietà** e **quali metodi** avranno gli oggetti creati da essa.==
```js
class Utente {
	constructor(nome, eta) {
		this.nome = nome;
		this.eta = eta;
	}

	saluta() {
		console.log("Ciao! Sono " + this.nome);
	}
}

```

Per creare un nuovo oggetto `Utente`, usiamo l’operatore [[#^newOp|`new`]]:
```js
const utenteUno = new Utente("Manuel", 35);
utenteUno.saluta(); // Output: Ciao! Sono Manuel
```

In questo caso:

- `Utente` è la **classe**.
    
- `utenteUno` è un’**istanza** della classe `Utente`.
    
- La classe ha un metodo chiamato `saluta()`, accessibile da ogni istanza.


> [!NOTE] Nota:
> Le classi non sostituiscono il modello a prototipi:  
>==**sono solo una sintassi più moderna e leggibile** per definire costruttori e prototipi.==
>
>==Internamente, **JavaScript continua a usare l’ereditarietà prototipale**, anche se noi scriviamo `class`.==

### Il concetto di prototype in JS 
Una delle caratteristiche più potenti e flessibili degli oggetti in JavaScript è che **possono essere modificati anche dopo la loro creazione,** come abbiamo già visto sopra con l'operatore [[#^newOp|`new`]].

#### Aggiunta di una proprietà a un singolo oggetto
Anche se un oggetto è stato creato tramite un **costruttore**, possiamo comunque aggiungere nuove proprietà in qualsiasi momento.
Esempio:
```js
var marioRossi = new Persona("Mario", "Rossi");
var giuseppeVerdi = new Persona("Giuseppe", "Verdi");

marioRossi.telefono = "0612345678";
```

In questo caso, solo **marioRossi** ha una proprietà `telefono`.  
L’altro oggetto, `giuseppeVerdi`, **non viene modificato**: ogni oggetto può essere personalizzato singolarmente.

#### Aggiunta di proprietà a tutti gli oggetti dello stesso tipo
Ma se si vuole  ì**aggiungere una nuova proprietà a tutti gli oggetti** creati da un costruttore, senza doverli modificare uno per uno?
Lo si può fare usando la **proprietà speciale `prototype`:**
```js
Persona.prototype.telefono = "123456";
```
Con questa istruzione, tutti gli oggetti creati con `new Persona()` ==avranno **automaticamente accesso** alla proprietà `telefono`, anche se **non è stata definita direttamente dentro di loro**.==

Quindi come funziona esattamente la proprietà `prototype`:
quando si prova ad d accedere a una proprietà su un oggetto, JavaScript:

1. **Cerca la proprietà nell’oggetto stesso**
    
2. Se non la trova, **cerca nel suo prototipo** (cioè in `Persona.prototype`)
    
3. Continua a salire nella "catena dei prototipi" finché non trova la proprietà o raggiunge `null`.


> [!remember] Da ricordare
> - ==La proprietà aggiunta con `prototype` **non viene copiata dentro ogni oggetto**, ma è **condivisa** da tutti.==
>    
>- ==Se un oggetto definisce **una proprietà con lo stesso nome**, quella **locale ha la precedenza** su quella ereditata dal prototipo.==

### I metodi `call()` e `apply()` in JS

In JavaScript, **anche le funzioni sono oggetti**.  
Questo significa che possono avere **proprietà** e **metodi**, proprio come gli altri oggetti.

Due dei metodi più utili per le funzioni sono:

- `call()`
    
- `apply()`

Entrambi permettono di:

✅ **Eseguire una funzione** specificando **manualmente il valore di [[Lezione 6; DOM e ripasso JS#Differenza tra `function` e le Arrow Function **Comportamento di `this`**|`this`]]    
✅ **Passare argomenti alla funzione** (in modi diversi)

#### Cosa fanno esattamente questi metodi 

Entrambi i metodi ti permettono di **eseguire una funzione** scegliendo **qual è il contesto (`this`)** in cui deve essere valutata.
La **differenza principale** sta **in come si passano gli argomenti**:

| Metodo    | `this` (1 parametro) | Altri argomenti     |
| --------- | -------------------- | ------------------- |
| `call()`  | Si                   | Passati uno per uno |
| `apply()` | Si                   | Passati in un array |
Per capire meglio questa differenza facciamo degli esempi:
**Esempio con `call()`**

```js
function myFunction(a, b) {
  return a * b;
}

const result = myFunction.call(null, 10, 2); // 10 * 2 = 20

```
**Spiegazione:**
- Il primo argomento (`null`) indica che non vogliamo cambiare il `this`
    
- Gli argomenti `10` e `2` sono passati **direttamente**

**Esempio con `apply()`**
```js
function myFunction(a, b) {
  return a * b;
}

const args = [10, 2];
const result = myFunction.apply(null, args); // 10 * 2 = 20
```

- Anche qui `null` è usato come `this`
    
- Gli argomenti vengono passati **come array**
    

Quindi i casi d'uso di questi due metodi sono rispettivamente :
- `call()`: ==si usa  quando si hanno dei **parametri singoli**==
- `apply()`: ==si usa quando si ha  **un array** di valori da passare.==

#### Esempio pratico con `this`
```js
const persona = {
  nome: "Luca",
  saluta: function(saluto) {
    console.log(saluto + ", sono " + this.nome);
  }
};

const altraPersona = {
  nome: "Giulia"
};

persona.saluta.call(altraPersona, "Ciao"); // Output: "Ciao, sono Giulia"
persona.saluta.apply(altraPersona, ["Buongiorno"]); // Output: "Buongiorno, sono Giulia"

```


> [!remember] Ricorda
> - `call()` e `apply()` sono strumenti potenti per **controllare il contesto di esecuzione** di una funzione
 >   
>- Sono fondamentali in programmazione JavaScript avanzata, ad esempio per:
  >  
  > 	 - il **Function borrowing** (prendere metodi da altri oggetti)
  >      
 > 	 - la gestione dinamica del `this`
