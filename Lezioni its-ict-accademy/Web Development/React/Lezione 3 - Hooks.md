# Introduzione 
Abbiamo visto [[Lezione 2 - Il Props Object|nella scorsa lezione]] cosa sono le props e come usarle.
Ora vediamo gli hooks e come usarli.
Prima pero di capire cosa sono gli **hooks**  e perché sono così importanti, partiamo da una semplice osservazione:  
- cosa succede in React quando cambia il valore di una variabile?

Immaginiamo di creare un componente che dichiara una variabile con valore iniziale `'ciao'` e una funzione che ne modifica il contenuto in `'arrivederci'`.  
All’interno del `return`, inseriamo un bottone che, al click, richiama quella funzione:

```jsx
const Messaggio = () => {
	let testo = "ciao";

	function onHandleClick() {
		testo = "arrivederci";
		console.log(testo);
	}

	return (
		<div>
			  <p>{testo}</p>
			  <button onClick={onHandleClick}>Cambia testo</button>
		</div>
	);
}

```

Quando proviamo ad eseguire questo codice e apriamo la console, noteremo che il valore della variabile **effettivamente cambia in memoria** (nella console vedremo `"arrivederci"`).  
Tuttavia, **il testo visualizzato sullo schermo non si aggiorna**.  
Questo accade perché React non “sa” che deve rifare il rendering del componente: il cambiamento della variabile non innesca automaticamente un aggiornamento della UI.

 Ed è proprio qui che entrano in gioco gli **Hooks**.

## Cosa sono gli Hooks

Gli _Hooks_ sono funzioni speciali introdotte da React per permetterci di:

- ✅ ==**Gestire lo stato interno** dei componenti (ovvero, memorizzare e aggiornare dati nel tempo);==  
- ✅ ==**Gestire effetti collaterali** (side effects) che avvengono dopo il rendering, come chiamate API o modifiche al DOM;==  
- ✅ ==Fare tutto questo **direttamente all’interno dei componenti funzionali**, senza dover ricorrere alle classi.==

In altre parole, gli Hooks ci consentono di:
- ==**rendere “reattivi” i componenti funzionali**, ovvero capaci di reagire ai cambiamenti di stato aggiornando automaticamente la UI.==



> [!done] I vantaggi dell'uso degli hooks sono : 
> - Possiamo **decidere cosa mostrare all’utente** in base ai dati attuali;
   > 
>- Descriviamo **come deve apparire l’interfaccia** in base allo stato, e React si occupa di renderla coerente;
 >   
>- Rendiamo i componenti **più semplici, leggibili e modulari** rispetto ai vecchi componenti a classe.

### I principali Hooks integrati (built-in)

React mette a disposizione diversi Hooks integrati.  
Tra i più comuni troviamo:

1. [[#Lo `useState()`|`useState()`]] → ==per gestire lo stato interno dei componenti.==   ^useState
    
    
2. `useEffect()` → ==per gestire gli effetti collaterali (ad es. fetch API, timers, ecc.).==     
    ^useEffect
    
3. `useContext()` → ==per accedere ai dati condivisi nel contesto dell’applicazione.==   ^useContext
    
4. `useReducer()` → ==per gestire stati complessi con logiche di aggiornamento più articolate.==   ^useReducer
    
5. `useRef()` → ==per accedere direttamente a elementi del DOM o mantenere valori persistenti senza triggerare un rendering.==  ^useRef


Quello che impareremo nei prossimi passaggi sarà : 
- Costruire un componente “stateful” (cioè con stato interno)
    
- Usare l’Hook `useState()` per creare e aggiornare uno stato
    
- Inizializzare e modificare i valori di stato
    
- Definire **event handler** per rispondere alle azioni dell’utente
    
- Utilizzare **funzioni di callback** per aggiornare correttamente lo stato
    
- Gestire lo stato anche con **array** e **oggetti**


---

## Modificare un componente con lo State hook (`useState()`)

Quindi come detto poco sopra, quando creiamo un componente React, non abbiamo a disposizione costruttori o altri metodi (come accade nei componenti a classe) per **inizializzare e gestire lo stato interno**.  
Nei componenti funzionali, questa necessità viene soddisfatta tramite una tecnica specifica: **gli Hooks**.

In particolare, l’Hook che utilizziamo per gestire lo stato è **`useState()`** — il più comune e fondamentale tra tutti.

### Lo `useState()`

[[#^useState|`useState()`]] è una funzione fornita da React che ci permette di:

- ==Memorizzare un valore nello stato interno di un componente;==
    
- ==Aggiornare quel valore e fare in modo che il componente venga **nuovamente renderizzato** ogni volta che lo stato cambia.==
    

In pratica, quando vogliamo che la nostra interfaccia utente _reagisca ai cambiamenti dei dati_, `useState()` è lo strumento che ce lo consente.

#### Importazione dell'Hook
Essendo un **named export** della libreria React, deve essere importato tramite **[[Lezione 6; DOM e ripasso JS#Destrutturazione|destrutturazione]]**, in questo modo:
```jsx
import React, { useState } from "react";
```

#### Come funziona 

Quando richiamiamo `useState()`, la funzione restituisce **un array con due valori**:

1. **Lo stato corrente** → ==rappresenta il valore attuale dello stato.==  ^currentValue
   
   
2. **La funzione setter dello stato** → ==è la funzione che consente di aggiornare tale valore.==  ^setterState

Possiamo estrarre questi due valori utilizzando la **[[Lezione 6; DOM e ripasso JS#Destrutturazione degli array|destrutturazione degli array]]**, come segue:

```jsx
const [currentState, setCurrentState] = useState();
```

Dove: 
- [[#^currentValue|`currentState`]] → ==rappresenta il valore attuale dello stato.==
    
- [[#^setterState|`setCurrentState`]] → ==è la funzione che utilizziamo per modificarlo.==


> [!NOTE] Nota:
> Il parametro passato a `useState()` è il **valore iniziale dello stato**, che può essere di qualsiasi tipo: stringa, numero, booleano, oggetto o array.

#### Cosa succede internamente 
Se proviamo a stampare in console il valore di `useState`, noteremo che si tratta di una **funzione**.  
Quando le passiamo un valore iniziale (ad esempio una stringa o un numero), React ci restituisce **un array** contenente:

- ==Il valore iniziale stesso;==
    
- ==Una funzione che serve per aggiornare lo stato.==
    

**Questo meccanismo consente a React di:**

- ==_Tenere traccia_ dei valori di stato;==
    
- ==_Aggiornare automaticamente_ il rendering del componente quando questi cambiano.==

###### Esempio pratico 1: Toogle di stato
```jsx
import React, { useState } from "react";

const Toggle = () => {
	// Inizializziamo lo stato con valore undefined (può contenere qualsiasi tipo)
	const [toggle, setToggle] = useState();

	return (
		<div>
			<p>The toggle is {toggle}</p>

		  {/* La funzione setter viene richiamata sugli eventi onClick */}
			<button onClick={() => setToggle("On")}>On</button>
			<button onClick={() => setToggle("Off")}>Off</button>
		</div>
	);
}

```

**Cosa succede:**

- Quando l’utente clicca su un pulsante, la funzione `setToggle()` aggiorna il valore dello stato.
    
- React rileva il cambiamento e **ricostruisce il rendering** del componente, aggiornando il testo mostrato nella pagina.


###### Esempio pratico 2 – Cambiare il colore dello sfondo

Vediamo ora un secondo esempio più completo, che mostra come usare `useState()` per aggiornare dinamicamente lo stile di un componente.


```jsx
import React, { useState } from "react";

export default const ColorPicker = () => {
	// 1️⃣ Inizializziamo lo stato con il colore 'Tomato'
	const [color, setColor] = useState("Tomato");

	// 2️⃣ Creiamo un oggetto di stile che utilizza il valore di stato
	const divStyle = { backgroundColor: color };

	return (
		<div style={divStyle}>
			<p>The color is {color}</p>

			{/* 3️⃣ Al click di ogni bottone aggiorniamo lo stato con un nuovo colore */}
			<button onClick={() => setColor("Aquamarine")}>Aquamarine</button>
			<button onClick={() => setColor("BlueViolet")}>BlueViolet</button>
			<button onClick={() => setColor("Chartreuse")}>Chartreuse</button>
			<button onClick={() => setColor("CornflowerBlue")}>CornflowerBlue</button>
		</div>
	);
}
```

**Analisi passo-passo:**

1. `useState("Tomato")` imposta il valore iniziale dello stato.
    
2. La variabile `color` rappresenta il colore attuale;
    
3. `setColor()` aggiorna lo stato quando l’utente clicca un bottone;
    
4. React effettua automaticamente il **re-rendering del componente**, aggiornando il colore di sfondo in base al nuovo valore.


>[!ticket] ### Alcune regole fondamentali sugli Hooks
> Per utilizzare correttamente gli Hooks, è importante ricordare alcune regole base:
>
>- Tutti gli Hooks **devono iniziare con la parola `use`** (es. `useState`, `useEffect`, ecc.);
  >  
>- Possono essere richiamati **solo all’interno di componenti funzionali o di altri Hooks personalizzati**;
  >  
>- Non devono essere chiamati **all’interno di cicli, condizioni o funzioni annidate**: vanno dichiarati sempre **a livello superiore** del componente (sopra il `return` statement);
   > 
>- Il nome del componente React deve iniziare con **lettera maiuscola**, altrimenti React non lo riconosce come tale.

#### Inizializzare lo stato
Abbiamo visto che l’Hook `useState()` ci permette di creare e gestire lo stato all’interno di un componente React.  
Ma cosa succede se vogliamo controllare **il valore iniziale** dello stato, oppure utilizzare tipi di dati diversi da una semplice stringa?

Proprio come possiamo usare `useState()` per memorizzare una stringa, possiamo usarlo anche per qualsiasi **tipo di dato primitivo** (booleano, numero, stringa, ecc.) oppure **per collezioni di dati**, come array e oggetti.

##### Esempio di stato booleano
Osserviamo il seguente componente: 
```jsx
import React, { useState } from 'react';

const ToggleLoading = () => {
	const [isLoading, setIsLoading] = useState();

	return (
		<div>
			<p>The data is {isLoading ? 'Loading' : 'Not Loading'}</p>
			<button onClick={() => setIsLoading(true)}>Turn Loading On</button>
			<button onClick={() => setIsLoading(false)}>Turn Loading Off</button>
		</div>
	);
}
```

In questo esempio: 
- il componente `ToggleLoading` utilizza come stato un **valore booleano**, 
	- rappresentato dalla variabile `isLoading`.  

- I booleani sono spesso usati in React per indicare se un dato è stato caricato oppure no, se un elemento è visibile o nascosto, o se un’azione è attiva o disattivata.

- Nel codice, la funzione `setIsLoading()` riceve di volta in volta i valori `true` o `false`, che determinano cosa mostrare sullo schermo.

#### Inizializzare lo stato con un valore predefinito 

Questo codice funziona già correttamente, ma potremmo voler specificare che, **al primo rendering**, lo stato `isLoading` parta già impostato su `true`.

Per farlo, basta passare un valore iniziale come **argomento della chiamata a `useState()`**:

```jsx
const [isLoading, setIsLoading] = useState(true);
```

==In questo modo, React saprà che il valore iniziale dello stato deve essere `true`.==  
==Da quel momento in poi, lo stato potrà essere modificato liberamente tramite la funzione `setIsLoading()`.==

#### Come React gestisce il valore iniziale
Quando inizializziamo uno stato con `useState(valoreIniziale)`, React segue un comportamento preciso:

1.  **Durante il primo render:** 
	- ==React usa il valore passato come argomento per impostare lo stato iniziale.==  
2.  **Quando chiamiamo la funzione setter:**
    - ==React ignora l’argomento iniziale e utilizza invece il nuovo valore fornito.==  
3.  **Nei render successivi:** 
	- ==React mantiene il valore aggiornato dell’ultimo render precedente.==

##### E se non inizializziamo lo stato? 
Se non passiamo alcun valore a `useState()`, durante il primo render **il valore corrente dello stato sarà `undefined`**.  
==Questo non causa errori, ma può rendere il codice meno leggibile o ambiguo per chi lo consulta.==

Per questo motivo, è buona norma **inizializzare sempre lo stato in modo esplicito**, anche solo con `null` o con un valore “vuoto” del tipo previsto. 
Esempio: 
```jsx
// Stato inizializzato a null
const [user, setUser] = useState(null);
```


> [!done] #### Buone pratiche di inizializzazione
> La scelta del valore iniziale dipende dal tipo di dato che vogliamo gestire e dal comportamento del componente.  
> Possiamo seguire alcune regole generali:
>1.  Caso 1 — Tipo di dato non definito a priori
>
>==Se non sappiamo che tipo di dato lo stato conterrà in futuro, è consigliabile **inizializzare con `undefined`**.==  
>Questo approccio esplicita che il valore non è ancora stato impostato e offre massima flessibilità.
>
>Motivazioni:
>
>-  **Chiarezza semantica:** ==`undefined` comunica chiaramente che il valore non è stato ancora assegnato.==
 >   
>-  **Flessibilità tipologica:** ==lo stato potrà contenere in seguito qualsiasi tipo di dato (stringa, numero, array, oggetto...).==
 >   
>-  **Debug più chiaro:** ==in console o negli strumenti di sviluppo, `undefined` segnala in modo esplicito che lo stato è ancora “vuoto”.==
>   
>```jsx
> const [data, setData] = useState();
>```
>
>2.  Caso 2 — Tipo di dato conosciuto
>
>Se invece sappiamo già che tipo di dato lo stato conterrà, è meglio **inizializzarlo coerentemente** con il suo tipo naturale:
>```jsx
>const [items, setItems] = useState([]);   // sempre un array
const [user, setUser] = useState({});     // sempre un oggetto
const [count, setCount] = useState(0);    // sempre un numero
const [isActive, setIsActive] = useState(false); // sempre un booleano
>```
>
>Questo approccio:
>
>- Evita controlli aggiuntivi nel codice (`if (items) ...`);
>    
>- Migliora la leggibilità;
 >   
>- Riduce errori legati a tipi di dato inattesi.
>  
>> [!example] **In Conclusione:**
>> **inizializzare correttamente lo stato** è una buona pratica fondamentale per costruire componenti React più prevedibili, leggibili e facili da mantenere.  
>
>
>>[!ticket] Ricorda sempre che lo stato non serve solo a _memorizzare dati_, ma a _guidare il comportamento e l’aspetto del componente_ in base a quei dati.


#### Utilizzare il setter dello stato al di fuori del JSX
Uno dei casi più comuni in cui si utilizza lo stato (`useState`) è la gestione dei dati inseriti dall’utente nei campi di input.  
Vediamo un esempio pratico in cui vogliamo memorizzare l’indirizzo email digitato in un campo di testo:
```jsx
import React, { useState } from 'react';

export default const EmailTextInput = () => {
	const [email, setEmail] = useState('');

	const handleChange = (event) => {
	    const updatedEmail = event.target.value;
	    setEmail(updatedEmail);
  }

	return (
		<input value={email} onChange={handleChange} />
  );
}
```

##### Analisi passo per passo

1. **Inizializzazione dello stato**
    
    - Usiamo la _[[Lezione 6; DOM e ripasso JS#Destrutturazione degli array|destrutturazione dell’array]]_ restituito da `useState()` per ottenere due elementi:
        
        - `email`: ==il valore corrente dello stato;==
            
        - `setEmail`: ==la funzione setter che aggiorna quello stato.==
            
2. **Gestione del cambiamento**
    
    - Il campo `<input>` in JSX possiede un _event listener_ chiamato `onChange`.  
        - ==Questo evento si attiva ogni volta che l’utente digita qualcosa nel campo.==
        
    - ==Quando ciò accade, React richiama automaticamente la funzione `handleChange`, passando come argomento un _oggetto evento_ (`event`).==
        
3. **Aggiornamento dello stato**
    
    - ==All’interno di `handleChange`, leggiamo il valore digitato (`event.target.value`) e lo memorizziamo nella variabile locale `updatedEmail`.==
        
    - ==Infine, chiamiamo `setEmail(updatedEmail)` per aggiornare lo stato React, che a sua volta causa un _re-render_ del componente, aggiornando il valore visualizzato nel campo di input.== 


#### Perché definire l'event handler fuori dal JSX?
In precedenza abbiamo visto che è possibile scrivere [[Lezione 2 - Il Props Object#Gli event handler nei componenti|event handler]] _inline_, ad esempio:
```jsx
<input value={email} onChange={(e) => setEmail(e.target.value)} />
```

Questo approccio funziona perfettamente, ma **quando la logica dell’evento diventa più complessa (ad esempio include validazioni, condizioni, log o altre operazioni), è buona pratica separarla dal markup JSX.**

Separare la logica dalla struttura visiva rende il codice:

- ==più leggibile e organizzato,==
    
- ==più facile da testare,==
    
- ==e più semplice da mantenere nel tempo.==
    

Questa tecnica segue il principio della **"_separation of concerns:_"** 
==ogni parte del codice ha una responsabilità chiara e limitata.== 


> [!info] #### Scritture equivalenti dell'handler
> Nel nostro esempio, la funzione `handleChange` può essere scritta in modi diversi ma equivalenti:
>```jsx
> const handleChange = (event) => {
  const newEmail = event.target.value;
  setEmail(newEmail);
};
>```
>
>Oppure in forma più compatta: 
>
>```jsx
>const handleChange = (event) => setEmail(event.target.value);
>```
>
>E infine usando la **destrutturizzazione dell'oggetto evento** 
>```jsx
>const handleChange = ({ target }) => setEmail(target.value);
>```
>
>Tutte queste versioni si comportano allo stesso modo: 
>bisogna solo scegliere quella che si trova più leggibile.
>
>> [!note] Di norma, la terza è la più concisa e diffusa nei progetti React moderni.



##### Esempio pratico: convalidare un numero di telefono

Vediamo ora un esempio più avanzato, dove gestiamo un input numerico controllando che l’utente inserisca solo cifre:

```jsx
const validPhoneNumber = /^\d{1,10}$/;

const PhoneNumber = () => {
	const [phone, setPhone] = useState("");

	const handleChange = ({ target }) => {
	    // target rappresenta l'elemento HTML <input> che ha generato l'evento
		const newPhone = target.value; // valore digitato dall'utente
    
	    // Controlla che il valore sia composto solo da numeri (1–10 cifre)
		const isValid = validPhoneNumber.test(newPhone);

	    // Se valido, aggiorna lo stato (React ri-renderizzerà il componente)
	    if (isValid){ setPhone(newPhone)};
  };

  return (
    <div className="phone">
      <label htmlFor="phone-input">Phone: </label>
      <input
        id="phone-input"
        value={phone}
        onChange={handleChange}
      />
    </div>
  );
}

```

^eventCodeBlock



##### Cosa succede nel dettaglio

1. **L’utente digita nel campo input.**
    
    - L’evento `onChange` si attiva e React chiama `handleChange()`.
        
2. **La funzione riceve un oggetto evento.**
    
    - Tramite destrutturizzazione, accediamo a `target`, ovvero l’elemento HTML `<input>` che ha generato l’evento.
        
3. **Lettura e validazione del valore.**
    
    - `target.value` contiene il testo digitato.
        
    - Usiamo l’espressione regolare `validPhoneNumber` per verificare che siano solo cifre (massimo 10).
        
4. **Aggiornamento dello stato condizionale.**
    
    - Se il valore è valido (`isValid === true`), viene chiamato `setPhone(newPhone)`.
        
    - In caso contrario, lo stato non viene modificato, e React ignora l’input errato.
        
5. **Re-render automatico.**
    
    - Quando lo stato cambia, React aggiorna il componente e il campo mostra il nuovo valore.
        

In pratica, il flusso è:

> 👤 Utente digita → 🧠 `onChange` si attiva → ⚙️ `handleChange` valida il valore → ✅ `setPhone()` aggiorna lo stato → 🔁 React ri-renderizza il componente.


> [!abstract] ### **Comprendere `target.value` negli event handler di React**
> Quando utilizziamo eventi in React (come `onChange`, `onClick`, `onSubmit`, ecc.), ==il framework richiama automaticamente una **funzione di gestione dell’evento** (detta _[[Lezione 2 - Il Props Object#Gli event handler nei componenti|event handler]]_) passando come argomento un **oggetto evento**==.
>
>Questo oggetto rappresenta **tutte le informazioni sull’[[Lezione 2 - Il Props Object#^objectAndEvent|evento]] che si è verificato**:  
>==quale elemento l’ha generato, in quale momento, con quale valore, e così via==.
>
>Esempio generico:
>
>```jsx
>function handleChange(event) {
  console.log(event); // Oggetto evento
}
>```
>
>Se questo handler è collegato a un campo `<input>`,  
>l’oggetto `event` contiene, tra le altre proprietà, un riferimento al campo stesso — ed è qui che entra in gioco **`event.target`**.
>
>##### Cosa rappresenta `target`
> ==La proprietà `target` dell’oggetto evento è **un riferimento all’elemento DOM** che ha generato l’evento.==
>
>In altre parole, `event.target`: 
>- ==è **il nodo HTML** su cui l’utente ha interagito.==
>
>Nel caso di un input:
>```jsx
> <input onChange={handleChange} />
>```
>
>#### Cosa rappresenta `target.value`
> ==La proprietà `.value` di un elemento `<input>` contiene **il valore corrente del campo di testo**.==  
Ogni volta che l’utente digita, cancella o modifica qualcosa, il valore cambia, e `event.target.value` viene aggiornato di conseguenza.
>
>Esempio pratico:
>```jsx
> const handleChange = (event) => {
  console.log(event.target.value);
};
>```
>- Se l’utente digita `3`, la console mostrerà `"3"`.
 >   
>- Poi digita `39` → la console mostrerà `"39"`.
 >   
>- Poi `390` → `"390"`, e così via.
  >  
>Questa è la modalità con cui React “ascolta” ciò che l’utente sta scrivendo, passo dopo passo.
>> [!faq] **Perché salviamo `event.target.value` in una variabile locale**
>> Spesso si vede codice di questo tipo in React: 
>>```jsx
>>  const handleChange = ({ target }) => {
>>	const newPhone = target.value;
>>	setPhone(newPhone);
>>};
>>```
>>
>>Qui accade quanto segue:
>>
>>1. **Destrutturizzazione dell’oggetto evento:**  
>>    Scrivendo `({ target })` invece di `(event)`, diciamo a JavaScript di estrarre direttamente la proprietà `target` dall’oggetto evento.  
>>> [!linki]   **È una forma abbreviata di:**
>>>   
>>>```jsx
>>>  const handleChange = (event) => {
>>>	const target = event.target;
>>>		...
>>>	};
>>>```
>>
>>
>>2. **Lettura del valore dell’input:**  
>>    `target.value` rappresenta ciò che l’utente ha appena digitato nel campo `<input>`.
>>    
>>3. **Memorizzazione temporanea:**  
>>    Assegniamo questo valore a una variabile locale, ad esempio `newPhone`, per poterlo usare facilmente in più punti della funzione (ad esempio per validarlo con una regex prima di aggiornare lo stato).
>>    
>>4. **Aggiornamento dello stato:**  
 >>   Se il valore è valido, chiamiamo `setPhone(newPhone)`, che aggiorna lo stato del componente.
 >>   
 >>> [!example]- **Riassumendo:**
 >>> - `event` → ==l’oggetto evento React.==
>>>    
>>>- `event.target` → ==il campo input che ha generato l’evento==.
  >>>  
>>>- `event.target.value` → ==il contenuto (testo) attualmente presente nel campo input.==
  >>>  
>>>
>>>Puoi pensarla così:
>>>
>>> ==Ogni volta che scrivi qualcosa in un input, React crea un “messaggio” (l’oggetto evento) che contiene il riferimento al campo (`target`) e il suo contenuto aggiornato (`target.value`).==  
>>> ==L’event handler riceve questo messaggio e decide come reagire== — ad esempio aggiornando lo stato con `setEmail(event.target.value)` o `setPhone(event.target.value)`.
>
>Quindi il flusso dell'evento, [[#^eventCodeBlock|dell'esempio fatto sopra]] può essere riassunto cosi: 
>1. L’utente digita → `onChange` viene attivato.
 >   
>2. React passa un oggetto evento alla funzione `handleChange`.
  >  
>3. `target` rappresenta l’input HTML che ha generato l’evento.
   > 
>4. `target.value` contiene ciò che l’utente ha digitato.
   > 
>5. Se il valore è valido, lo stato `phone` viene aggiornato.
  >  
>6. React effettua un nuovo render, mostrando il valore aggiornato nel campo.
>   
> ==Nel caso di componenti controllati (come questo), il valore dell’input (`value={phone}`) **non vive più nel DOM**, ma **nello stato React**.==  
>==Ogni volta che digiti, React aggiorna lo stato e poi “restituisce” quel valore all’input, garantendo che l’interfaccia sia sempre sincronizzata con i dati interni del componente.==
> 


#### Aggiornare lo stato precedente in React

Nei paragrafi precedenti abbiamo visto come aggiornare lo stato di un componente
passando direttamente un nuovo valore, ad esempio:

    setState(newStateValue);

Tuttavia, è importante sapere che **gli aggiornamenti di stato in React sono asincroni:**
- ==ciò significa che, quando invochiamo una funzione setter (come `setCount()` o `setEmail()`),==
React *non aggiorna immediatamente* lo stato.  
In alcuni casi, altre parti del codice possono quindi essere eseguite **prima**
che il nuovo stato venga effettivamente applicato.



#### Perché questo comportamento?
Questo meccanismo non è un difetto:  
==è una **scelta progettuale** di React per ottimizzare le prestazioni del rendering.==  
==Infatti, React può raggruppare più aggiornamenti di stato in un unico ciclo di rendering,==
riducendo i costi computazionali.

Tuttavia, questo approccio può portare a un rischio:  
⚠️ ==**l’utilizzo di valori di stato obsoleti**, se il nuovo stato dipende dal valore precedente.==

#### La soluzione: usare una *callback function*
Quando il nuovo valore di stato dipende da quello precedente,
è **buona prassi** utilizzare la versione “funzionale” della funzione setter.

In altre parole, invece di passare un valore diretto,
passiamo a `setState()` una **funzione di callback** che riceve:
- ==il valore precedente dello stato come argomento, e restituisce il nuovo valore.==
###### Esempio pratico

```jsx
import React, { useState } from "react";

export default function Counter() {
	// Dichiarazione dello stato 'count' inizializzato a 0
	const [count, setCount] = useState(0);

	// Definizione dell’event handler che aggiorna lo stato
	const increment = () => setCount(prevCount => prevCount + 1);

	// Rendering del componente
	return (
	    <div>
		  <p>Wow, hai cliccato quel bottone {count} volte!</p>
	      <button onClick={increment}>Clicca qui!</button>
	    </div>
	);
}
```

#### Come funziona 
Quando l’utente clicca sul bottone:

1. React invoca la funzione `increment()`.
    
2. La funzione chiama `setCount()` e le passa una callback.
    
3. React, internamente, fornisce alla callback l’ultimo valore valido di `count`.
    
4. La callback restituisce il nuovo valore (`prevCount + 1`).
    
5. React aggiorna lo stato e ri-renderizza il componente con il valore aggiornato.



> [!faq]  **Perché non scrivere semplicemente `setCount(count +1)`**
> In molti casi funzionerebbe comunque, ma **non sempre in modo sicuro:** 
>Se due o più aggiornamenti vengono eseguiti in rapida successione (ad esempio, due click molto ravvicinati o più update concatenati),  
>potresti finire per usare un valore di `count` non ancora aggiornato.
>
>==Con la callback (`setCount(prevCount => prevCount + 1)`), invece,==  
>==sei certo che React utilizzi **l’ultimo valore effettivo** di `count`, anche se più aggiornamenti sono in coda.==

##### Esempio articolato : navigazione di un quiz
Vediamo ora un caso reale in cui è fondamentale usare lo stato precedente:  
nella navigazione di un quiz.
```jsx
import React, { useState } from "react";

const QuizNavBar = ({ questions }) => {
  const [questionIndex, setQuestionIndex] = useState(0);

  // Event handler per tornare indietro
  const goBack = () =>
    setQuestionIndex(prevQuestionIndex => prevQuestionIndex - 1);

  // Event handler per andare avanti
  const goToNext = () =>
    setQuestionIndex(prevQuestionIndex => prevQuestionIndex + 1);

  // Booleani di controllo per disabilitare i pulsanti
  const onFirstQuestion = questionIndex === 0;
  const onLastQuestion = questionIndex === questions.length - 1;

  return (
    <nav>
      <span>Domanda #{questionIndex + 1}</span>
      <div>
        <button onClick={goBack} disabled={onFirstQuestion}>
          Indietro
        </button>
        <button onClick={goToNext} disabled={onLastQuestion}>
          Avanti
        </button>
      </div>
    </nav>
  );
};

```

- Lo stato `questionIndex` tiene traccia della **posizione corrente** nel quiz.
    
- Gli handler `goBack()` e `goToNext()` utilizzano **callback functions**:  
    in questo modo calcolano il nuovo valore (domanda precedente o successiva)  
    **basandosi sul valore precedente**.
    
- Le costanti `onFirstQuestion` e `onLastQuestion` sono booleani che servono  
    per disabilitare i pulsanti ai limiti del quiz.