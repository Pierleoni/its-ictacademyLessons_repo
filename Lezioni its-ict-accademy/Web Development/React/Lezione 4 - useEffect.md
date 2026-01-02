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

### Fetch Data con `useEffect`

Uno dei casi d’uso più comuni dell’**Effect Hook (`useEffect`)** in React è il **recupero dei dati da un server** (fetch dei dati).

Quando un componente React deve ottenere dati esterni (API REST, backend, mock server, ecc.), è fondamentale **controllare con precisione quando l’effetto viene eseguito**.  
Questo perché una chiamata al server è un’operazione costosa e non dovrebbe essere eseguita più volte del necessario.

##### Perché è importante controllare il fetch dei dati

Ogni chiamata non necessaria al server comporta un costo in termini di:

- elaborazione
    
- prestazioni
    
- consumo di dati (soprattutto su dispositivi mobili)
    
- eventuali costi economici nel caso di API a pagamento
    

Per questo motivo, **non è quasi mai corretto eseguire un fetch dopo ogni render del componente**.

#### Comportamento di default di useEffect nel fetch

Per impostazione predefinita, `useEffect` si comporta così:

```jsx
useEffect(() => {
	// fetch dei dati 
});
```

 In questa forma, l’effetto viene eseguito **dopo ogni render** del componente.

Questo è un problema perché:

- ==ogni aggiornamento di stato (ad esempio la digitazione in un input, un click, una modifica locale)==
    
- ==provoca un nuovo render==
    
- ==che a sua volta rilancia l’effetto==
    
- ==e quindi **una nuova chiamata al server**, anche se i dati non sono cambiati==

#### Fetch eseguito solo al primo render (mount)

Se i dati **non dipendono da alcuna variabile**, possiamo passare un **[[#Il dependency array|dependecy array]] vuoto** come secondo argomento di `useEffect`:

```jsx
useEffect(() => {
	// fetch dei dati 
}, []);
```

In questo modo:

- il fetch viene eseguito **una sola volta**
    
- subito dopo il primo render del componente (fase di mount)
    
- i dati vengono poi riutilizzati nei render successivi
    

Questo approccio è tipico per:

- dati iniziali
    
- configurazioni
    
- contenuti statici recuperati dal server



### Pattern fondamentale: useEffect + useState

Nel recupero dei dati, `useEffect` viene quasi sempre utilizzato insieme a `useState`.

Il pattern generale è il seguente:


```jsx
const [data, setData] = useState();

useEffect(() => {
  fetch(...)
    .then(response => response.json())
    .then(result => setData(result));
}, []);
```


In questo pattern:

- `useEffect` si occupa del fetch dei dati
    
- `setData` salva i dati nello stato locale del componente
    
- React esegue un nuovo render usando i dati appena recuperati
    
- il fetch **non viene ripetuto inutilmente**
    

Questo è uno dei pattern più importanti in React per la gestione dei dati asincroni.



#### Fetch con dependency array non vuoto

Quando i dati **dipendono da una variabile di stato**, quella variabile deve essere inserita nel dependency array.

Esempio:

```jsx
const [forecastType, setForecastType] = useState('/daily');

useEffect(() => {
  get(forecastType).then(response => {
    setData(response.data);
  });
}, [forecastType]);

```

In questo caso:

- l’effetto viene eseguito dopo il primo render
    
- viene rieseguito **solo quando `forecastType` cambia**
    
- se `forecastType` rimane invariato, il fetch viene saltato
    

In questo modo si ottiene un fetch **reattivo ma controllato**.


### Caso di studio: Forecast component

Di seguito un esempio completo di componente che utilizza:

- `useState` per gestire i dati
    
- `useEffect` per il fetch
    
- un dependency array per controllare quando richiamare il server

```jsx
import { useState, useEffect } from "react";
import { get } from "./mockBackend/fetch";

const Forecast = () => {
  const [data, setData] = useState();
  const [notes, setNotes] = useState({});
  const [forecastType, setForecastType] = useState("/daily");

  useEffect(() => {
    alert("Requested data from server...");

    get(forecastType).then((response) => {
      alert("Response: " + JSON.stringify(response, "", 2));
      setData(response.data);
    });
  }, [forecastType]);

  const handleChange = (itemId) => ({ target }) =>
    setNotes((prev) => ({
      ...prev,
      [itemId]: target.value,
    }));

  // Gestione dello stato di loading
  if (!data) {
    return <p>Loading...</p>;
  }

  return (
    <div className="App">
      <h1>My Weather Planner</h1>

      <div>
        <button onClick={() => setForecastType("/daily")}>5-day</button>
        <button onClick={() => setForecastType("/hourly")}>Today</button>
      </div>

      <table>
        <thead>
          <tr>
            <th>Summary</th>
            <th>Avg Temp</th>
            <th>Precip</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.summary}</td>
              <td>{item.temp.avg}°F</td>
              <td>{item.precip}%</td>
              <td>
                <input
                  value={notes[item.id] || ""}
                  onChange={handleChange(item.id)}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Forecast;

```

#### Import delle dipendenze
```jsx
import { useState, useEffect } from "react";
import { get } from "./mockBackend/fetch";
```

- `useState`: Hook che consente di gestire lo **stato locale** del componente.
    
- `useEffect`: Hook che consente di eseguire **effetti collaterali** dopo il render (in questo caso il fetch dei dati).
    
- `get`: funzione che simula una chiamata HTTP a un backend (mock), restituendo una Promise con i dati meteo.

#### Dichiarazione del componente

```jsx
const Forecast = () => {
```

`Forecast` è un **functional component** React.  
Tutta la logica di stato, effetti e rendering è contenuta all’interno di questa funzione.


#### Dichiarazione degli state

```jsx
const [data, setData] = useState(); 
const [notes, setNotes] = useState({}); 
const [forecastType, setForecastType] = useState("/daily");
```

1. `data`

- Contiene i **dati restituiti dal server**.
    
- Inizialmente è `undefined` perché il fetch è asincrono.
    
- Viene valorizzato dopo la risposta del backend tramite `setData`.
    

2. `notes`

- Oggetto che memorizza le note inserite dall’utente.
    
- La chiave è l’`id` dell’elemento della previsione.
    
- Il valore è il testo digitato nell’input corrispondente.
    
- È uno stato **locale e indipendente** dai dati del server.
    

3. `forecastType`

- Determina quale endpoint deve essere interrogato (`/daily` o `/hourly`).
    
- Influenza direttamente il comportamento del fetch.
    
- È inserito nel dependency array di `useEffect`.



#### useEffect per il fetch dei dati

```jsx
useEffect(() => {
  alert("Requested data from server...");

  get(forecastType).then((response) => {
    alert("Response: " + JSON.stringify(response, "", 2));
    setData(response.data);
  });
}, [forecastType]);
```


#### Cosa fa questo effetto

- Viene eseguito **dopo il primo render** del componente.
    
- Viene rieseguito **solo quando cambia `forecastType`**.
    
- Effettua una chiamata al backend simulato tramite `get(forecastType)`.
    

### Flusso di esecuzione

1. Il componente viene renderizzato.
    
2. `useEffect` viene eseguito.
    
3. Viene richiesta la risorsa `/daily` o `/hourly`.
    
4. Alla risoluzione della Promise:
    
    - i dati vengono salvati nello stato tramite `setData`
        
    - React esegue un nuovo render con i dati aggiornati.
        

Grazie al dependency array `[forecastType]`, **i render causati da input o note non rilanciano il fetch**.

#### Gestione dell’input dinamico (notes)

```jsx
const handleChange = (itemId) => ({ target }) =>
  setNotes((prev) => ({
    ...prev,
    [itemId]: target.value,
  }));
```

Questa funzione:

- è una **higher-order function** (ritorna una funzione)
    
- riceve l’`id` dell’elemento corrente
    
- aggiorna lo stato `notes` in modo immutabile
    

##### Cosa succede internamente

- `prev` rappresenta lo il valore attuale di `notes`
    
- lo spread operator (`...prev`) evita la perdita dei valori già inseriti
    
- `[itemId]` permette di aggiornare dinamicamente la chiave corretta
    

Ogni input della tabella ha così il **proprio valore indipendente**.

#### Gestione dello stato di loading
```jsx
if (!data) {
  return <p>Loading...</p>;
}
```

Poiché il fetch è asincrono:

- al primo render `data` è `undefined`
    
- senza questo controllo, `data.map(...)` genererebbe un errore
    

Questo blocco:

- interrompe il rendering principale
    
- mostra un messaggio di caricamento
    
- ripristina il rendering normale quando `data` è disponibile
    

#### Rendering del JSX

```jsx
return (   
	<div className="App"></div>
```

#### Titolo dell’applicazione

`<h1>My Weather Planner</h1>`

Elemento puramente presentazionale.



#### Bottoni per cambiare il tipo di previsione

```jsx
<button onClick={() => setForecastType("/daily")}>5-day</button> 
<button onClick={() => setForecastType("/hourly")}>Today</button>
```

- Ogni bottone aggiorna lo stato `forecastType`.
    
- Il cambio di stato provoca:
    
    1. un nuovo render
        
    2. la riesecuzione di `useEffect`
        
    3. una nuova chiamata al server
        

Questo è un esempio di **fetch reattivo controllato**.



#### Rendering della tabella dei dati

```jsx
{data.map((item) => (   
	<tr key={item.id}>
```

- `map` itera l’array dei dati ricevuti dal backend.
    
- `key={item.id}` è necessaria per il corretto funzionamento del Virtual DOM.
    

#### Celle della tabella

```jsx
<td>{item.summary}</td> 
<td>{item.temp.avg}°F</td> 
<td>{item.precip}%</td>

```

Visualizzano i dati restituiti dal server.



## Input controllato per le note

```jsx
<input
  value={notes[item.id] || ""}
  onChange={handleChange(item.id)}
/>

```

- È un **controlled component**:
    
    - il valore è sempre sincronizzato con lo stato React
        
- Ogni input è legato alla propria voce tramite `item.id`
    
- La digitazione provoca:
    
    - aggiornamento dello stato `notes`
        
    - re-render del componente
        
    - **nessuna chiamata al server**
        



#### Export del componente

`export default Forecast;`

Rende il componente disponibile per l’importazione in altri file.

> [!example] Conclusione
> 
> L’uso corretto del dependency array nel fetch dei dati permette di:
> 
> - evitare chiamate ridondanti
>     
> - migliorare le prestazioni
>     
> - sincronizzare lo stato con i dati remoti
>     
> - rendere il componente prevedibile e manutenibile
>     
> 
> In React, **fetch + useEffect + useState** costituiscono un pattern fondamentale per la gestione dei dati asincroni.


### Regole fondamentali degli hooks 

Quando si utilizzano gli Hooks in React, è essenziale rispettare **due regole fondamentali**:

1. ==**Gli Hooks devono essere chiamati solo al livello superiore del componente**==
    
2. ==**Gli Hooks possono essere chiamati solo all’interno di funzioni React**==
    

Durante i primi esercizi con `useState` e `useEffect`, queste regole risultano spesso intuitive da rispettare. 
Tuttavia, man mano che la logica dei componenti diventa più complessa e il numero di Hooks aumenta, è facile incorrere in errori se non si ha ben chiaro il motivo di tali vincoli.

#### Perché React impone queste regole

Quando React costruisce e aggiorna il **Virtual DOM**, la libreria **invoca ripetutamente le funzioni che definiscono i componenti** in risposta alle interazioni dell’utente.

==React **non identifica gli Hooks tramite il loro nome**, ma **in base all’ordine con cui vengono chiamati** all’interno del componente.==  
Questo significa che React associa ogni chiamata a `useState`, `useEffect`, ecc. a una precisa posizione nella funzione.

Per questo motivo:

- l’ordine delle chiamate agli Hooks **deve essere sempre lo stesso**
    
- React deve poter “ritrovare” ogni Hook nello stesso punto a ogni render
    

Se un Hook viene chiamato solo in certe condizioni (ad esempio dentro un `if` o un ciclo), l’ordine delle chiamate cambia tra un render e l’altro, causando comportamenti imprevedibili o errori.

##### Cosa **non** fare: Hooks dentro condizioni
Un esempio di codice **non valido** è il seguente:
```jsx
if (userName !== '') {
  useEffect(() => {
    localStorage.setItem('savedUserName', userName);
  });
}
```


In questo caso, `useEffect` viene chiamato **solo se la condizione è vera**, rompendo la regola dell’ordine costante degli Hooks.
##### Approccio corretto

Lo stesso risultato può essere ottenuto **chiamando sempre l’Hook**, ma spostando la logica condizionale _all’interno_ dell’effetto:
```jsx
useEffect(() => {
  if (userName !== '') {
    localStorage.setItem('savedUserName', userName);
  }
});
```

In questo modo:

- l’Hook viene eseguito sempre nello stesso punto
    
- la logica condizionale non interferisce con il meccanismo interno di React

#### Seconda regola: dove è possibile usare gli Hooks

Gli Hooks possono essere utilizzati **solo**:

- ==all’interno di **componenti funzionali React**==
    
- ==all’interno di **Custom Hooks**==
    

Non è possibile utilizzare `useState`, `useEffect`, ecc. in:

- funzioni JavaScript normali
    
- classi
    
- callback esterne ai componenti
    

I **Custom Hooks** sono funzioni che iniziano con `use` e permettono di **incapsulare e riutilizzare logica stateful** tra più componenti, mantenendo il rispetto delle regole degli Hooks.

### Esempio del componente `Shop`
Per comprendere meglio questi concetti prendiamo ad esempio il componente `Shop`: 
```jsx
const Shop = () => {

    const [categories, setCategories] = useState();

    if (categories) {

        const [selectedCategory, setSelectedCategory] = useState();

        const [items, setItems] = useState({});

    }

    if (!categories) {

    useEffect(() => {

        get('/categories').then((response) => {

        setCategories(response.data);

        });

    });

    }

  

  if (selectedCategory && !items[selectedCategory]) {
	useEffect(() => {

		get(`/items?category=${selectedCategory}`).then((response) => {

			 setItems((prev) => ({ ...prev, [selectedCategory]: response.data }));

  });

  });

  }

  

  if (!categories) {

    return <p>Loading..</p>;

  }

  

  return (

    <div className='App'>

      <h1>Clothes 'n Things</h1>

      <nav>

        {categories.map((category) => (

          <button key={category} onClick={() => setSelectedCategory(category)}>

            {category}

          </button>

        ))}

      </nav>

      <h2>{selectedCategory}</h2>

      <ul>

        {!items[selectedCategory]

          ? null

          : items[selectedCategory].map((item) => <li key={item}>{item}</li>)}

      </ul>

    </div>

  );

}
```

Come possiamo notare il componente `Shop` presenta diversi problemi strutturali legati all'uso scorretto degli Hooks.
##### Errore principale: Hooks annidati in condizioni
```jsx
if (categories) {
  const [selectedCategory, setSelectedCategory] = useState();
  const [items, setItems] = useState({});
}
```

Qui:

- due `useState` sono definiti **dentro uno statement condizionale**
    
- questo viola direttamente la prima regola degli Hooks
    

Lo stesso problema si ripresenta con `useEffect`, anch’esso inserito dentro un `if`.

Il risultato è un componente che:

- può funzionare apparentemente in alcuni casi
    
- ma è intrinsecamente **instabile e non conforme al modello React**


#### Refactoring del componente `Shop`
Il refactoring ha come obiettivo principale **ripristinare la correttezza strutturale** del componente, rispettando le regole degli Hooks.
##### 1. Spostare tutti gli Hooks al livello superiore
```jsx
const [categories, setCategories] = useState(null);
const [selectedCategory, setSelectedCategory] = useState(null);
const [items, setItems] = useState({});
```

Tutti gli Hooks vengono:

- dichiarati all’inizio del componente
    
- inizializzati in modo esplicito (`null` o `{}`)
    

Questo rende il codice più leggibile e prevedibile.


##### 2. Fetch delle categorie: uso corretto di `useEffect`

L’intenzione originale era eseguire il fetch delle categorie **una sola volta**.  
Il modo corretto per ottenere questo comportamento è utilizzare un `useEffect` con **array di dipendenze vuoto**:
```jsx
useEffect(() => {
  get('/categories').then((response) => {
    setCategories(response.data);
  });
}, []);
```

In questo modo:

- l’effetto viene eseguito solo dopo il primo render
    
- non è necessario alcun `if (!categories)`
    
- il comportamento è stabile e conforme alle regole

##### 3. Fetch degli item in base alla categoria selezionata
Il secondo `useEffect` gestisce il caricamento degli articoli quando l’utente seleziona una categoria:
```jsx
useEffect(() => {
  if (selectedCategory && !items[selectedCategory]) {
    get(`/items?category=${selectedCategory}`).then((response) => {
      setItems((prev) => ({
        ...prev,
        [selectedCategory]: response.data,
      }));
    });
  }
}, [selectedCategory, items]);
```

Qui la logica è corretta perché:

- l’Hook è sempre chiamato
    
- la condizione è interna all’effetto
    
- il fetch viene eseguito solo se i dati non sono già presenti
    

Questo approccio evita chiamate ridondanti al backend.

#### Hooks separati per effetti separati

Nella sezione precedente abbiamo visto come **gli Hooks debbano essere chiamati sempre al livello superiore del componente** e come la logica condizionale debba essere spostata _all’interno_ degli effetti.  
Un altro principio altrettanto importante riguarda **come organizzare lo stato e gli effetti** quando un componente gestisce più responsabilità.

### Raggruppare o separare i dati nello stato

Come già accennato parlando di `useState`, quando più valori:

- ==sono **strettamente correlati**==
    
- ==cambiano **insieme**==
    
- ==rappresentano un’unica entità logica==
    

può essere sensato **raggrupparli in una struttura unica**, come un oggetto o un array.

Tuttavia, questo approccio non è sempre vantaggioso.  
Raggruppare dati **non correlati** in un unico stato può:

- aumentare la complessità degli aggiornamenti
    
- rendere più difficile capire _perché_ uno stato cambia
    
- creare dipendenze indirette tra parti di codice indipendenti
    

Per questo motivo, una buona pratica in React è **separare le responsabilità**, ==utilizzando **Hook differenti per dati ed effetti differenti**.==


#### Confronto tra due approcci
##### Primo caso: stato ed effetti accorpati

Nel seguente esempio, dati e comportamenti molto diversi vengono gestiti insieme:

```jsx
// Handle both position and menuItems with one useEffect hook.
const [data, setData] = useState({ position: { x: 0, y: 0 } });

useEffect(() => {
  get('/menu').then((response) => {
    setData((prev) => ({ ...prev, menuItems: response.data }));
  });

  const handleMove = (event) =>
    setData((prev) => ({
      ...prev,
      position: { x: event.clientX, y: event.clientY }
    }));

  window.addEventListener('mousemove', handleMove);
  return () => window.removeEventListener('mousemove', handleMove);
}, []);

```

In questo caso:

- lo **stato** contiene sia `position` che `menuItems`
    
- un singolo `useEffect` gestisce:
    
    - una richiesta HTTP
        
    - un event listener sul mouse
        
- ogni aggiornamento richiede l’uso dello spread operator per preservare parti di stato non coinvolte
    

Il codice funziona, ma:
- è più difficile da leggere
    
- è meno modulare
    
- è più complesso da estendere o testare


##### Secondo caso: responsabilità separate

Separando stato ed effetti, il codice diventa più chiaro:

```jsx
// Gestisce menuItems con un solo hook useEffect.
const [menuItems, setMenuItems] = useState(null);
useEffect(() => {
  get('/menu').then((response) => setMenuItems(response.data));
}, []);

// Gestisce position con un hook useEffect separato.
const [position, setPosition] = useState({ x: 0, y: 0 });
useEffect(() => {
  const handleMove = (event) =>
    setPosition({ x: event.clientX, y: event.clientY });

  window.addEventListener('mousemove', handleMove);
  return () => window.removeEventListener('mousemove', handleMove);
}, []);

```

Qui ogni Hook:

- ha **una responsabilità ben definita**
    
- è più facile da comprendere isolatamente
    
- può essere riutilizzato o estratto in un Custom Hook
    

Non esiste una regola assoluta su quando raggruppare o separare i dati, ma con la pratica diventa più naturale riconoscere la soluzione più chiara e manutenibile.


### Caso di studio: `SocialNetwork`

Nel componente `SocialNetwork` troviamo un esempio tipico di codice che **funziona**, ma che può essere migliorato dal punto di vista strutturale.

#### Versione iniziale
```jsx
const [data, setData] = useState(null);

useEffect(() => {
  Promise.all([get('/menu'), get('/news-feed'), get('/friends')]).then(
    ([menuResponse, newsFeedResponse, friendsResponse]) => {
      setData({
        menu: menuResponse.data,
        newsFeed: newsFeedResponse.data,
        friends: friendsResponse.data
      });
    }
  );
}, []);
```

In questo caso:

- più richieste di rete vengono gestite in **un unico effetto**
    
- dati concettualmente distinti (`menu`, `newsFeed`, `friends`) sono accorpati in un solo stato
    
- ogni modifica futura richiederà di intervenire su una struttura complessa
    

Anche se il codice è corretto, **la leggibilità e la manutenibilità possono migliorare**.


##### Refactoring: separare stato ed effetti

##### 1. Stati distinti per dati distinti
```jsx
const [menu, setMenu] = useState(null);
const [newsFeed, setNewsFeed] = useState(null);
const [friends, setFriends] = useState(null);
```

Ogni variabile di stato ora rappresenta **un singolo dominio di dati**, rendendo immediatamente chiaro il suo scopo.

##### 2. Effetti separati per ogni fetch
```jsx
useEffect(() => {
  get('/menu').then((response) => {
    setMenu(response.data);
  });
}, []);
```

```jsx
useEffect(() => {
  get('/news-feed').then((response) => {
    setNewsFeed(response.data);
  });
}, []);
```

```jsx
useEffect(() => {
  get('/friends').then((response) => {
    setFriends(response.data);
  });
}, []);
```

Ogni `useEffect`:

- è responsabile di **una sola richiesta**
    
- viene eseguito una sola volta grazie al dependency array vuoto
    
- rispetta pienamente le regole degli Hooks


