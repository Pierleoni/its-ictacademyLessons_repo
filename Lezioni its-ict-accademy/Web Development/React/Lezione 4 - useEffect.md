# Introduzione 
Prima dell'introduzione degli Hooks, i componenti funzionali venivano usati quasi esclusivamente per ricevere _[[Lezione 2 - Il Props Object#Il Props Object|props]]_ e restituire JSX.  
Con l’arrivo dello **State Hook** ([[Lezione 3 - Hooks#Lo `useState()`|`useState`]]) abbiamo potuto gestire dati dinamici nei componenti funzionali.
Tuttavia, molte operazioni non riguardano direttamente il rendering dell’interfaccia:

- recuperare dati da un backend
    
- iscriversi a flussi di eventi
    
- avviare timer o intervalli
    
- modificare il DOM o leggere informazioni esterne al componente
    

Queste operazioni sono chiamate **side effects**: 
- ==effetti collaterali che devono essere eseguiti in momenti specifici del ciclo di vita del componente.==  
Per gestirli in modo corretto e prevedibile, React mette a disposizione l’**Effect Hook**, cioè `useEffect`.

## Lo `useEffect`
Un effetto può essere eseguito in tre momenti fondamentali del ciclo di vita del componente:

1. ==**Quando il componente viene montato** (render iniziale)==
    
2. ==**Quando stato o props cambiano**, causando un nuovo render==
    
3. ==**Quando il componente viene smontato**, se l’effetto prevede una cleanup function==
    

La frequenza con cui l’effetto viene eseguito dipende dalla _[[#Il dependency array|dependency array]]_, che vedremo più avanti.

##### Esempio pratico: Aggiornare il titolo della pagina
Questo esempio mostra tre concetti fondamentali:

- come usare `useState` per gestire un valore dinamico (`name`)
    
- come usare `useEffect` per reagire ai cambiamenti dello stato
    
- come gestire un input controllato in React
```jsx
eexport default function PageTitle() {

    // Stato locale: contiene il nome digitato dall’utente.
    const [name, setName] = useState('');

    /* 
    ======================
    Effetto con useEffect
    ======================
    La funzione passata a useEffect viene eseguita:
    - dopo ogni render,
    - ma solo quando cambia una delle dipendenze elencate nell’array.

    In questo caso, aggiorniamo il titolo del browser ogni volta che cambia 'name'.
    */
    useEffect(() => {
        document.title = `Hi, ${name}`;
    }, [name]);   // Esegui l’effetto solo quando 'name' cambia

    return (
        <div>
            <p>Use the input below to rename this page!</p>

            <input 
                type="text"

                // Input controllato: il valore dell’input è sempre sincronizzato con lo stato
                onChange={({ target }) => setName(target.value)}

                value={name}
            />
        </div>
    );
}
```

###### Spiegazione: 
1. **Lo stato locale:**
`useState('')` crea una variabile di stato (`name`) e una funzione per aggiornarla (`setName`).  
Ogni volta che `setName()` viene chiamato, React esegue un nuovo render del componente.

2. **L’effetto (`useEffect`)**  
`useEffect(() => { ... }, [name])` definisce un effetto che:

- viene eseguito **dopo il rendering**
    
- aggiorna il titolo della scheda del browser usando il valore corrente di `name`
    
- si attiva **solo** quando cambia `name`, grazie alla _dependency array_
    

Comportamenti alternativi della dependency array:

- **senza array**: l’effetto viene eseguito _ad ogni render_
    
- **array vuota `[]`**: l’effetto viene eseguito _solo al montaggio_ del componente

3. **Input controllato:**
L’input è sincronizzato con lo stato tramite:
```jsx
value={name}
onChange={({ target }) => setName(target.value)}
```

Questo implica che:

- il testo mostrato è sempre quello presente nello stato
    
- ogni modifica dell’utente aggiorna il valore dello stato tramite `setName`
    
- l’aggiornamento dello stato innesca un nuovo render
    
- e l’effetto si riattiva aggiornando il titolo della pagina
    

Questo è il classico comportamento dei _controlled components_ in React.


> [!abstract] **Cosa sono i controlled components**
> In React, un **controlled component** è un elemento del form (come `<input>`, `<textarea>`, `<select>`) il cui **valore è interamente gestito dallo stato React**.
> In altre parole:
>
>> Un componente è “controllato” quando **React è l’unica fonte di verità del suo valore**.
>>
>
> 
> **Come funziona un controlled component**
>Quando un input è controllato:
>
>1. ==Il suo valore visibile proviene da una variabile di stato (`value={...}`)==
  >  
>2. ==Ogni modifica dell’utente genera un evento `onChange`==
 >   
>3. ==L’handler dell’evento aggiorna lo stato con il nuovo valore==
  >  
>4. ==Il nuovo stato provoca un re-render → e React aggiorna l’input==
  >  
>
>Quindi il flusso è:
>
>> [!todo] **UI → onChange → setState → render → aggiorna valore dell’input**
>
>Per capire meglio facciamo un esempio semplice
>```jsx
>const [name, setName] = useState("");
><input 
>    value={name} 
 >   onChange={(e) => setName(e.target.value)}
>/>
>```
>
>Qui l’input mostra sempre il valore presente nello stato `name`.  
>Se provi a togliere `onChange`, l’input diventerebbe _a sola lettura_, perché React controlla tutto.
>> [!faq] **Perché usarli?**
>>  I controlled components permettono a React di:
>>
>>- ==validare il contenuto in tempo reale==
 >>   
>>- ==formattare automaticamente i dati (es. uppercase)==
  >>  
>>- ==bloccare input non validi==
   >> 
>>- ==sincronizzare più campi tra loro==
  >>  
>>- ==mantenere uno stato affidabile e prevedibile durante tutto il ciclo di vita del form==
  >>  
>>
>>In pratica, i form diventano **parte del flusso dichiarativo di React**, invece di “vivere di vita propria” nel DOM.

### Gli effetti nei componenti funzionali
L’**Effect Hook** (`useEffect`) permette a un componente funzionale di **eseguire del codice ogni volta che viene renderizzato o ri-renderizzato**.  
Si usa per gestire tutte quelle operazioni che producono *effetti collaterali* rispetto al semplice rendering, come:

- aggiornare il DOM manualmente  
- sincronizzare dati esterni  
- recuperare informazioni da un back-end  
- ascoltare eventi del browser  
- gestire timer o intervalli

In combinazione con lo stato, `useEffect` consente di introdurre **comportamenti dinamici** nella nostra applicazione.

Supponiamo, ad esempio, di voler aggiornare il **titolo della scheda del browser** ogni volta che l’utente digita nell’input.  
Riprendiamo il componente usato come esempio:
```jsx
import React, { useState, useEffect } from 'react';

function PageTitle() {
  const [name, setName] = useState('');

  useEffect(() => {
    document.title = `Hi, ${name}`;
  });

  return (
    <div>
      <p>Use the input field below to rename this page!</p>
      <input 
        onChange={({ target }) => setName(target.value)} 
        value={name} 
        type='text' 
      />
    </div>
  );
}
```

##### Spiegazione 
1. Import dello useEffect: 
```jsx
import { useEffect } from 'react';
```

`useEffect` **non restituisce alcun valore e non viene utilizzato per ottenere dati dal componente:**  
==serve esclusivamente a **registrare una funzione da eseguire dopo il render**.==

2. Passare la funzione di effetto: 
la struttura base è: 
```jsx
useEffect(() => {
    // codice dell’effetto
});
```

Quindi nel nostro esempio: 
```jsx
useEffect(() => {
  document.title = `Hi, ${name}`;
});
```

Questa funzione viene eseguita **dopo ogni render del componente**.  
==Ogni volta che l’utente digita nell’input, si verifica un re-render e l’effetto aggiorna il titolo del documento.==

3. Relazione tra stato ed effetto
L’handler `onChange` aggiorna lo stato tramite `setName(target.value)`.  
Ogni aggiornamento dello stato provoca un nuovo render, e quindi:

-  ==React aggiorna il DOM==
    
-  ==Dopo l’aggiornamento del DOM, React esegue la funzione passata a `useEffect`==
    
-  ==L’effetto modifica il titolo della pagina usando il valore _corrente_ di `name`==
    

È importante notare che, anche se l’effetto viene eseguito _dopo_ il render, esso ha comunque accesso alle variabili presenti nello scope del componente (quindi allo stato aggiornato).

##### Esempio aggiuntivo: Incremento con effetto
In questo esempio l'effetto mostra un alert ogni volta che il valore dello stato cambia. 
```jsx
const Counter = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    alert(`Il valore corrente del contatore è: ${count}`);
  });

  const handleClick = () => {
    setCount(prevCount => prevCount + 1);
  };

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={handleClick}>
        Click me
      </button>
    </div>
  );
}
```

**Spiegazione:**
- `useState(0)` crea uno **stato locale** `count` e una funzione **updater** `setCount`.

- Ogni pressione del pulsante **aggiorna lo stato** usando la forma funzionale dello state setter:
```jsx
setCount(prevCount => prevCount + 1);
```
- Poiché React esegue un **re-render** del componente ogni volta che lo stato cambia, l’**effect** definito con `useEffect` viene rieseguito, mostrando un alert con il **valore aggiornato di `count`**.
    

Questo esempio evidenzia come `useEffect` permetta di **rispondere in modo dichiarativo ai cambiamenti dello stato**, senza dover gestire manualmente il ciclo di aggiornamento del DOM.

### Pulire gli effetti con `useEffect` 
Alcuni effetti nei componenti React richiedono una **pulizia** quando non sono più necessari.

Un esempio tipico è l’aggiunta di **event listener** direttamente al DOM, oltre agli elementi JSX presenti nel componente.

> ⚠️ È importante rimuovere questi listener quando non servono più, per **evitare perdite di memoria**, bug o degrado delle prestazioni.

##### Esempio pratico: gestione di un contatore di click sul documento 
```jsx
import React, { useState, useEffect } from 'react';

const Count = () => {
  // Stato locale: tiene traccia del numero di click sul documento
  const [clickCount, setClickCount] = useState(0);

  // Event handler: incrementa il contatore di 1
  const increment = () => setClickCount(prevClickCount => prevClickCount + 1);

  useEffect(() => {
    // Aggiunge un listener per l'evento 'mousedown' sull'oggetto document
    document.addEventListener('mousedown', increment);

    // Funzione di pulizia: rimuove il listener quando il componente viene re-renderizzato o smontato
    return () => {
      document.removeEventListener('mousedown', increment);
    };
  });

  return (
    <h1>Document Clicks: {clickCount}</h1>
  );
};
```

**Spiegazione passo-passo:**
1. **Stato locale**
    
    - `useState(0)` crea lo stato `clickCount` e la funzione updater `setClickCount`.
        
    - Ogni click sul documento aggiorna lo stato tramite la forma **funzionale**: `prevClickCount => prevClickCount + 1`.
        
    - Questo assicura che ogni aggiornamento parta dal **valore precedente** corretto.
        
2. **Effetto con `useEffect`**
    
    - L’hook `useEffect` viene chiamato **dopo ogni render**.
        
    - Aggiunge un listener `mousedown` al `document` che richiama `increment`.
        
    - Ogni pressione del mouse sul documento triggera la funzione `increment`, aggiornando lo stato e causando un re-render.
        
3. **Funzione di pulizia**
    
    - React chiama automaticamente la funzione di pulizia **prima di ogni nuovo render** o quando il componente viene smontato.
        
    - La funzione di pulizia rimuove il listener:
```jsx
document.removeEventListener('mousedown', increment)
```

 - Senza questa funzione, ad ogni render verrebbe aggiunto un nuovo listener, causando:
        
	- ==incrementi multipli per singolo click==
            
	- ==comportamento apparentemente “randomico” del contatore==
            
	- ==potenziali perdite di memoria==
            
4. **Dettagli sull’evento `mousedown`**
    
    - Si attiva **quando il pulsante del mouse viene premuto**, non quando viene rilasciato.
        
    - Se vuoi rilevare il rilascio del pulsante, usa invece `mouseup`.
        
    - L’evento è utile per azioni immediate al click, come drag & drop o disegno su canvas.
        
    - Viene seguito da un eventuale `click` se il pulsante viene rilasciato sullo stesso elemento.


> [!example] **In sintesi**
> - Gli effetti in React **possono avere conseguenze collaterali** sul DOM.
  >  
>- Quando creano risorse esterne, come **event listener**, è necessario fornire una **funzione di pulizia**.
 >   
>- La funzione di pulizia evita **duplicazioni di listener**, **bug** e **problemi di prestazioni**.
 >   
>- In questo esempio, ogni click sul documento incrementa **sempre correttamente** il contatore, grazie alla combinazione di:
 >   
>    - **useState funzionale**
>        
>    - **useEffect con funzione di cleanup**


### Controllare quando vengono richiamati gli effetti 

==La funzione `useEffect()` esegue il suo **primo argomento**, cioè la funzione di effetto, **dopo ogni rendering** di un componente.==  

Finora abbiamo visto come restituire una **funzione di pulizia** per evitare bug e problemi di prestazioni, ma a volte vogliamo **saltare del tutto l’esecuzione dell’effetto sui re-render** successivi.

È comune, ad esempio, voler eseguire un effetto **solo al montaggio del componente** (cioè alla prima renderizzazione), ma **non ad ogni re-render**.

#### Il dependency array

L’Effect Hook ci permette di gestire questo comportamento in modo semplice:  
- passando un **array vuoto** come secondo argomento di `useEffect()`.  

Questo array è chiamato **dependency array** (matrice di dipendenze): 
- ==serve a dire a React **quando eseguire l’effetto** e **quando ignorarlo**.==
- ==Se l’array è vuoto `[]`, l’effetto viene eseguito **solo una volta**, al montaggio del componente.==
- ==Se l’array contiene variabili di stato o props, l’effetto viene rieseguito **solo quando una di queste cambia**.==
    
> In altre parole, l’array di dipendenze permette di **controllare con precisione il comportamento dell’effetto**.

##### Esempio: effetto eseguito al primo render e pulizia al dismount

```jsx
useEffect(() => {
    alert("Component rendered for the first time");

    return () => {
        alert("Component is being removed from the DOM");
    };
}, []);
```

Senza l’array vuoto `[]`:
- i messaggi di alert verrebbero mostrati **ad ogni render**, cosa indesiderata.  
**Passando `[]`, invece:** 
- ==il messaggio di “primo render” appare solo all’inizio, e la funzione di pulizia viene richiamata **solo quando il componente viene smontato**.==

##### Esempio pratico: un timer con `useEffect`
```jsx
import React, { useState, useEffect } from 'react';

const Timer = () => {
    // Stato per il timer
    const [time, setTime] = useState(0);

    // Stato per un input controllato
    const [name, setName] = useState("");

    // Event handler compatto per aggiornare lo stato dell'input
    const handleChange = ({ target }) => setName(target.value);

    // Effetto: avvia un timer che incrementa il contatore ogni secondo
    useEffect(() => {
        const intervalId = setInterval(() => {
            // Forma funzionale dello state setter: garantisce che l'ultimo valore venga sempre aggiornato
            setTime(prevTime => prevTime + 1);
        }, 1000);

        // Pulizia dell'effetto: rimuove il timer quando il componente viene smontato
        return () => {
            clearInterval(intervalId);
        };
    }, []); // Array di dipendenze vuoto: effetto eseguito solo al mount

    return (
        <>
            <h1>Time: {time}</h1>
            <input
                type="text"
                value={name}          // Controlled component
                onChange={handleChange}
            />
        </>
    );
};
```

**Spiegazione passo-passo**

1. **Stati locali**
    
    - ==`time` tiene traccia dei secondi trascorsi.==
        
    - ==`name` gestisce il valore dell’input controllato.==
        
2. **Effetto del timer**
    
    - ==`useEffect` crea un intervallo con `setInterval` che incrementa `time` di 1 ogni secondo.==
        
    - ==Grazie alla forma funzionale `setTime(prevTime => prevTime + 1)`, il timer utilizza **sempre l’ultimo valore dello stato**, evitando problemi di “[[Lezione 3 - Hooks#Quando lo stato diventa "stale" (obsoleto)|stale state]]”.==
        
3. **Funzione di pulizia**
    
    - ==`return () => clearInterval(intervalId)` rimuove il timer quando il componente viene smontato.==
        
    - ==Senza la pulizia, ogni re-render aggiungerebbe **un nuovo intervallo**, causando incrementi multipli e potenziali problemi di prestazioni.==
        
4. **Array di dipendenze vuoto**
    
    - Garantisce che il timer venga creato **solo una volta**, al montaggio.
        
    - ==La funzione di pulizia viene eseguita **solo al dismount**, evitando duplicazioni di intervalli.==
        
5. **Input controllato**
    
    - Il valore dell’input è sempre sincronizzato con lo stato `name`.
        
    - Ogni modifica aggiorna lo stato, causando un re-render, ma non riavvia il timer grazie all’array di dipendenze vuoto.



> [!example] **In sintesi**
> Con `useEffect` e l’array di dipendenze possiamo **controllare con precisione quando eseguire effetti** e **gestire correttamente le risorse** come timer o listener, evitando bug e perdite di memoria.

