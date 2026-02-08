# Introduzione 
Fino a qui abbiamo trattato tutti gli argomenti base di JS come: 
- I fondamenti di JavaScript 
- Le variabili e la differenza tra i tre tipi di dichiarazione 
- Gli array, Indexing, attributo length, operatori e conversione tra tipi 
- Espressioni, statements e cicli 
- Le funzioni in JavaScript 
- Il DOM 
- E anche una introduzione al framework di React JS 
Ora affrontiamo la asincronia in JavaScript 
## Cos è l'asincronia 
Per comprendere il concetto di asincronia, possiamo partire da un’analogia con la vita quotidiana.

Immaginiamo di dover pulire casa.  
Alcune attività vengono svolte in **modo sincrono**, cioè una dopo l’altra:

- prima si puliscono i pavimenti
    
- poi si spolverano le superfici
    
- successivamente si riordinano le stanze
    

Ogni operazione deve essere completata **prima di passare alla successiva**.

Durante queste attività, però, possono esserci anche operazioni diverse, come **avviare la lavastoviglie**.  
Questa è un’operazione **asincrona**: 
- ==una volta avviata, **non è necessario aspettare che finisca** per continuare a svolgere le altre attività di pulizia.== 
Possiamo proseguire con le operazioni sincrone e, solo quando la lavastoviglie ha terminato, occuparci del risultato (le stoviglie pulite).

###  Applicazione dell’analogia a JavaScript

In JavaScript avviene qualcosa di molto simile.

JavaScript è un linguaggio **single thread**, cioè dispone di **un solo flusso di esecuzione**: 
- ==può eseguire **una sola istruzione alla volta**.==  
Questo significa che, se tutte le operazioni fossero sincrone, una operazione lenta (come una richiesta a un server) bloccherebbe completamente il programma, impedendo l’esecuzione del codice successivo.

Per evitare questo problema, JavaScript utilizza l’**asincronia**.

Le operazioni asincrone come:

- richieste HTTP (`fetch`)
    
- timer (`setTimeout`)
    
- accesso a risorse esterne
    

 vengono **avviate**, ma non bloccano l’esecuzione del resto del codice.  
JavaScript continua a eseguire le istruzioni sincrone e si “occuperà” del risultato dell’operazione asincrona **solo quando questa sarà terminata**.

Nello sviluppo web, la **programmazione asincrona** è notoriamente uno degli argomenti più complessi da comprendere.

Un’operazione asincrona è un’operazione che: 
- ==permette al computer di **continuare a eseguire altri compiti** mentre l’operazione stessa è ancora in corso.==  
In altre parole, le operazioni che richiedono molto tempo **non bloccano l’esecuzione del resto del programma**.

Come abbiamo già detto prima JavaScript è un linguaggio **single thread:** 
- ==cioè può eseguire **una sola istruzione alla volta**.==  
Se tutte le operazioni fossero sincrone, una operazione lenta bloccherebbe l’intero programma.
La programmazione asincrona nasce proprio per risolvere questo problema:  
- ==JavaScript può **delegare** le operazioni lente e gestirne il risultato **solo quando è disponibile**.==

### Le Promise JS 
Per delegare questo compito dell'asincronia dall'ES6 sono state introdotte le Promise.
Una **Promise** è: 
- ==un oggetto che rappresenta **l’esito futuro di un’operazione asincrona**.==

Una Promise può trovarsi in uno dei seguenti stati:
#### Stati di una Promise: 
1. **Pending (in sospeso)**   ^pending
    - ==Stato iniziale della promise: l’operazione non è ancora completata.==
    
2. **Fulfilled (risolta)**   ^fullfilled
    - ==L’operazione è stata completata con successo e la promise ha prodotto un valore.==  
    - Ad esempio, una richiesta HTTP può risolversi con un oggetto JSON.
    
3. **Rejected (rifiutata)**   ^rejected
    - ==L’operazione è fallita e la promise contiene il motivo del fallimento, generalmente un oggetto `Error`.==
    

> ==Una promise si dice **settled** quando non è più in stato pending, cioè quando è rejected o rejected.==

##### Analogia della lavastoviglie applicata alle Promise

Riprendendo l'analogia della lavastoviglie:

1. **Pending**  
    - ==La lavastoviglie è in funzione, ma il ciclo di lavaggio non è ancora terminato.==
    
2. **Fulfilled**  
    - ==Il ciclo è completato con successo e i piatti sono puliti.==
    
3. **Rejected**  
    - ==Si è verificato un problema (ad esempio manca il detersivo) e il lavaggio non è riuscito.==
    

Se la promise viene **fulfilled:** 
- ==possiamo eseguire operazioni successive, come scaricare i piatti puliti.==  
Se la promise viene **rejected:**
- ==possiamo gestire l’errore, ad esempio riavviando il ciclo o scegliendo un’alternativa.==


### Creare un oggetto Promise 
Per creare una nuova Promise in JavaScript si utilizza la parola chiave `new` insieme al **costruttore `Promise`**.
###### Sintassi di base
```js
const executorFunction = (resolve, reject) => { };

const myFirstPromise = new Promise(executorFunction);
```

Il costruttore `Promise` accetta come parametro una funzione chiamata **executor function**.

#### Executor Function 

La **executor function** è una funzione che ==viene **eseguita automaticamente** nel momento in cui viene creata la Promise.==

Il suo compito è:

- ==avviare un’operazione (spesso asincrona)==
    
- ==stabilire se la Promise deve **risolversi(fullfilled)** o **rifiutarsi(rejected)**==
##### Parametri della executor function 
La executor function riceve **due parametri**, che sono a loro volta funzioni:

1. [[#`resolve()`|`resolve`]]  
    
2. [[#`reject()`|`reject`]]
    

Queste funzioni:

- ==**non sono definite dal programmatore**==
    
- ==vengono **fornite automaticamente da JavaScript**==
    
- ==permettono di cambiare lo stato della Promise==
###### `resolve()`

`resolve()` è una funzione che ==accetta **un argomento**==.

- Quando viene chiamata:
    
    - ==lo stato della Promise passa da `pending` a `fulfilled`==
        
    - ==il valore passato a `resolve()` diventa il **valore risolto della Promise**==
Esempio concettuale:
```js
resolve("Operazione completata");
```

###### `reject()`

`reject()` è una funzione che ==accetta **un motivo o un errore** come argomento.==

- Quando viene chiamata:
    
    - ==lo stato della Promise passa da `pending` a `rejected`==
        
    - ==il valore passato rappresenta il **motivo del fallimento**==

Esempio concettuale:
```js
reject("Si è verificato un errore");
```

#### Esempio completo di Promise
```js
const executorFunction = (resolve, reject) => {
    if (someCondition) {
        resolve('I resolved!');
    } else {
        reject('I rejected!');
    }
};

const myFirstPromise = new Promise(executorFunction);
```

##### Spiegazione del codice

- Viene dichiarata la variabile `myFirstPromise`.
    
- `myFirstPromise` ==viene inizializzata usando `new Promise()`, che invoca il costruttore della Promise.==
    
- La `executorFunction` ==viene passata al costruttore ed eseguita immediatamente.==
    
- Alla `executorFunction` vengono forniti due parametri funzione:
    
    - `resolve`
        
    - `reject`
        
- Se `someCondition` è vera:
    
    - ==viene invocata `resolve('I resolved!')`==
        
    - ==la Promise passa allo stato `fulfilled`==
        
- Se `someCondition` è falsa:
    
    - ==viene invocata `reject('I rejected!')`==
        
    - ==la Promise passa allo stato `rejected`==

### Creare una Promise: esempio pratico
Per comprendere meglio come funziona una Promise, utilizziamo un esempio concreto basato su un **inventario di prodotti**.

#### 1. Inventario di partenza
```js
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};
```

Questo oggetto rappresenta un inventario in cui a ogni prodotto è associata la quantità disponibile.

#### 2. Executor function
Definiamo ora una **executor function**, che verrà passata al costruttore `Promise`.

```js
const myExecutor = (resolve, reject) => {
  if (inventory.sunglasses > 0) {
    resolve('Sunglasses order processed.');
  } else {
    reject('That item is sold out.');
  }
};
```
##### Spiegazione

- `myExecutor` è la executor function della Promise.
    
- Riceve due parametri forniti automaticamente da JavaScript:
    
    - `resolve`
        
    - `reject`
        
- All’interno della funzione viene controllata la disponibilità del prodotto `sunglasses`.
    

In particolare:

- se `inventory.sunglasses > 0`:
    
    - viene chiamata `resolve()`
        
    - la Promise passerà allo stato **fulfilled**
        
- altrimenti:
    
    - viene chiamata `reject()`
        
    - la Promise passerà allo stato **rejected**


#### 3. Funzione che restituisce una Promise
Ora definiamo una funzione che **crea e restituisce una Promise**.
```js
function orderSunglasses() {
  return new Promise(myExecutor);
}
```

###### Spiegazione

- `orderSunglasses()` è una funzione che:
    
    - ==non esegue direttamente l’ordine==
        
    - ==**restituisce una Promise**==
        
- ==Il costruttore `new Promise()` riceve come argomento la executor function `myExecutor`==
    
- Nel momento in cui la Promise viene creata:
    
    - ==la executor function viene eseguita immediatamente==

#### 4. Creazione della Promise
```js
const orderPromise = orderSunglasses();
console.log(orderPromise);
```

##### Cosa succede in questo punto

1. Viene chiamata la funzione `orderSunglasses()`
    
2. Viene creata una nuova Promise
    
3. La executor function `myExecutor` viene eseguita
    
4. In base allo stato dell’inventario:
    
    - la Promise viene **fulfilled**
        
    - oppure **rejected**
        
5. `orderPromise` contiene l’oggetto Promise risultante
    

Il `console.log(orderPromise)` mostrerà una Promise:

- **fulfilled**, se gli occhiali sono disponibili
    
- **rejected**, se il prodotto è esaurito


### La funzione `setTimeout()` e l’asincronia
Sapere come **costruire** una Promise è utile, ma nella pratica è ancora più importante sapere come **consumare le Promise:**
- ==cioè come utilizzarle nel codice.==
Nella maggior parte dei casi, infatti:

- ==**non creiamo manualmente nuove Promise**==
    
- ==lavoriamo con Promise restituite da **operazioni asincrone** già esistenti==
    

Queste Promise:

- ==iniziano nello stato [[#^pending|`pending`]]==
    
- in un secondo momento vengono:
    
    - ==**[[#^fullfilled|fulfilled]]**, se l’operazione ha successo==
        
    - ==**[[#^rejected|rejected]]**, se l’operazione fallisce==

### Simulare operazioni asincrone
Nei prossimi esempi simuleremo il comportamento delle operazioni asincrone utilizzando funzioni che restituiscono Promise **risolte dopo un certo intervallo di tempo**.

Per farlo useremo la funzione `setTimeout()`.

#### Cos’è `setTimeout()`

`setTimeout()` ==è un’[[Lezione 6 - API#API (Application Programming Interface)|API]] disponibile sia in **Node.js** sia nei **browser**.==

==Serve per **programmare l’esecuzione di una funzione dopo un determinato ritardo**.==

##### Parametri di `setTimeout()`

`setTimeout()` accetta due parametri:

1. ==una funzione callback==
    
2. ==un tempo di attesa espresso in millisecondi==

**Esempio base**
```js
const delayedHello = () => {
  console.log('Hi! This is an asynchronous greeting!');
};

setTimeout(delayedHello, 2000);
```

###### Spiegazione

- La funzione `delayedHello` stampa un messaggio in console.
    
- `setTimeout()` riceve:
    
    - ==la funzione `delayedHello`==
        
    - ==un ritardo di `2000` millisecondi==
        
- Dopo **almeno** 2 secondi, `delayedHello()` viene eseguita.

Ma perché si sceglie un ritardo di 2 secondi? 
==Perché `setTimeout()` rappresenta un’operazione **asincrona**.==

JavaScript utilizza un meccanismo chiamato **event loop** per gestire l’asincronia.

Il funzionamento, in modo semplificato, è il seguente:

1. ==Dopo 2 secondi, la callback `delayedHello()` viene inserita nella **task queue**==
    
2. Prima che la callback venga eseguita:
    
    - ==deve terminare tutto il codice sincrono in esecuzione==
        
    - ==devono essere completate eventuali altre operazioni già presenti nella coda==
        
3. ==Solo quando il thread principale è libero, la callback viene eseguita==
    

Per questo motivo il tempo indicato in `setTimeout()` rappresenta un **ritardo minimo**, non garantito al millisecondo.

### Creare Promise asincrone con `setTimeout()`
Possiamo usare `setTimeout()` per simulare operazioni asincrone che restituiscono una Promise.
```js
const returnPromiseFunction = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('I resolved!');
    }, 1000);
  });
};

const prom = returnPromiseFunction();
```

###### Spiegazione del codice

- `returnPromiseFunction()` restituisce una nuova Promise.
    
- All’interno del costruttore `Promise`:
    
    - viene usato `setTimeout()`
        
    - dopo 1 secondo viene chiamata `resolve()`
        
- Fino allo scadere del timeout:
    
    - la Promise rimane nello stato `pending`
        
- Dopo 1 secondo:
    
    - la Promise passa allo stato `fulfilled`
        
    - il valore risolto è `'I resolved!'`
        

La variabile `prom` contiene quindi una Promise che inizialmente è **pending** e che verrà risolta in un secondo momento.

Questo comportamento è analogo a quello delle Promise reali restituite da:

- richieste HTTP (`fetch`)
    
- accesso a database
    
- operazioni su file
    
- chiamate a servizi esterni
    

In tutti questi casi:

- l’operazione richiede tempo
    
- la Promise rappresenta un valore che **sarà disponibile in futuro**


###  Consumare le Promise

Una Promise asincrona, come gia detto in precedenza, nasce sempre nello stato **[[#^pending|`pending`]]**, ma JavaScript garantisce che **prima o poi si stabilizzerà** (_settle_), cioè passerà in uno dei due stati finali:

- **[[#^fullfilled|fulfilled]]** → ==l’operazione ha avuto successo==
    
- **[[#^rejected|rejected]]** → ==l’operazione è fallita==
    

Il problema da risolvere è quindi il seguente:

> Come possiamo dire al programma **cosa fare quando la Promise cambia stato**?

####  Il metodo `.then()`

Gli oggetti `Promise` mettono a disposizione un metodo fondamentale: **`.then()`**.

==Questo metodo permette di specificare il comportamento da adottare **quando la Promise viene risolta o rifiutata**.==

Concettualmente, `.then()` esprime l’idea:

> ==“Ho una Promise; **quando** si stabilizza, **allora** esegui questo codice.”==

##### Analogia della lavastoviglie 
Riprendendo l'analogia della lavastoviglie: 
- Se la Promise viene **fulfilled**  
    → le stoviglie sono pulite → le mettiamo via
    
- Se la Promise viene **rejected**  
    → le stoviglie sono sporche → interveniamo (ad esempio aggiungendo il detersivo e riavviando il ciclo)
    

`.then()` serve proprio a descrivere queste due possibili azioni.

#### `.then()` come Higher-Order Function

Il metodo `.then()` è una **Higher-Order Function:**
- ==perché **accetta funzioni come argomenti**.==

In particolare, può ricevere **due funzioni callback**, dette _handler_:

1. **onFulfilled**  ^onFulfillef
    
    - ==viene eseguito se la Promise è risolta con successo==
        
    - ==riceve come argomento il **valore risolto**==
        
2. **onRejected**  ^onRejected
    
    - ==viene eseguito se la Promise viene rifiutata==
        
    - ==riceve come argomento il **motivo dell’errore**==

###### Sintassi Generale 
```js
promise.then(
  (value) => {
    // gestisce il successo
  },
  (error) => {
    // gestisce il fallimento
  }
);
```

##### Flessibilità di `.then()`

Il metodo `.then()` è molto flessibile. Può essere chiamato con:

- solo l’[[#^onFulfillef|handler per il successo]]
    
- solo l’[[#^onRejected|handler per il fallimento]]
    
- entrambi gli handler
    
- nessun handler
    

Se un handler **non viene specificato**, `.then()` **non genera errori**:  
- ==la Promise risultante manterrà lo stesso esito della Promise originale.==

####  `.then()` restituisce sempre una Promise

Un aspetto fondamentale da ricordare è che:

> ==**Ogni chiamata a `.then()` restituisce sempre una nuova Promise.**==

Questo comportamento è cruciale perché consente di:

- ==concatenare più operazioni asincrone (_chaining_)==
    
- ==gestire flussi asincroni complessi in modo ordinato==
    
- ==controllare la sequenza delle operazioni==
    

Questo concetto sarà centrale quando si parlerà di:

- chaining delle Promise
    
- gestione degli errori
    
- `async / await`


> [!ticket] **Concetti chiave**
> - Una Promise si stabilizza sempre (fulfilled o rejected)
 >   
>- `.then()` serve per reagire allo stato finale della Promise
  >  
>- `.then()` accetta funzioni callback
  >  
>- `.then()` è una Higher-Order Function
  >  
>- `.then()` restituisce sempre una nuova Promise

#### Esempio 
Riprendiamo l'esempio fatto in precedenza: 
```js
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};

const myExecutor = (resolve, reject) => {
  if (inventory.sunglasses > 0) {
    resolve('Sunglasses order processed.');
  } else {
    reject('That item is sold out.');
  }
};

function orderSunglasses() {
  return new Promise(myExecutor);
}

const orderPromise = orderSunglasses();
```

Fino a qui abbiamo creato la Promise, ma **non l’abbiamo ancora consumata**.
##### Consumare la Promise con `.then()` e `.catch()`
```js
orderPromise
  .then((successMessage) => {
    console.log('SUCCESS:', successMessage);
    // Operazioni successive se l’ordine è andato a buon fine
  })
  .catch((errorMessage) => {
    console.log('ERROR:', errorMessage);
    // Azioni alternative se l’ordine fallisce, ad esempio:
    // alert dell’utente o riavvio del ciclo
  });
```

###### Spiegazione

1. **`then()`**
    
    - ==Riceve una funzione callback (`successMessage`) che viene eseguita se la Promise viene **fulfilled**==
        
    - Nel nostro esempio stampa: `SUCCESS: Sunglasses order processed.`
        
2. **`catch()`**
    
    - ==Riceve una funzione callback (`errorMessage`) che viene eseguita se la Promise viene **rejected**==
        
    - Nel nostro esempio stampa: `ERROR: That item is sold out.`
        
3. **Chaining**
    
    - `.then()` ==restituisce sempre una nuova Promise==
        
    - ==Possiamo concatenare più `.then()` per gestire operazioni successive==

#### Consumare la Promise dell’ordine di occhiali da sole

**Codice originale dell’ordine**
```js
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};

const myExecutor = (resolve, reject) => {
  if (inventory.sunglasses > 0) {
    resolve('Sunglasses order processed.');
  } else {
    reject('That item is sold out.');
  }
};

function orderSunglasses() {
  return new Promise(myExecutor);
}

const orderPromise = orderSunglasses();
```

Fino a qui abbiamo creato la Promise, ma **non l’abbiamo ancora consumata**.

**Consumare la Promise con `.then()` e `.catch()`**

```js
orderPromise
  .then((successMessage) => {
    console.log('SUCCESS:', successMessage);
    // Operazioni successive se l’ordine è andato a buon fine
  })
  .catch((errorMessage) => {
    console.log('ERROR:', errorMessage);
    // Azioni alternative se l’ordine fallisce, ad esempio:
    // alert dell’utente o riavvio del ciclo
  });
```

**Spiegazione**

1. **`then()`**
    
    - ==Riceve una funzione callback (`successMessage`) che viene eseguita se la Promise viene **fulfilled**==
        
    - Nel nostro esempio stampa: `SUCCESS: Sunglasses order processed.`
        
2. **`catch()`**
    
    - ==Riceve una funzione callback (`errorMessage`) che viene eseguita se la Promise viene **rejected**==
        
    - Nel nostro esempio stampa: `ERROR: That item is sold out.`
        
3. **Chaining**
    
    - `.then()` ==restituisce sempre una nuova Promise==
        
    - ==Possiamo concatenare più `.then()` per gestire operazioni successive==


---

### Funzioni di callback per successo e fallimento
Quindi, abbiamo detto che per consumare una promise **si deve specificare cosa fare quando l'operazione termina**. 
Questo lo si fa tramite il metodo `.then()`.
Una promise parte sempre dallo stato di [[#^pending|pending]], in seguito cambia stato e diventa: 
- **fulfilled** → esegue una logica di successo.
    
- **rejected** → esegue una logica di fallimento.
Il metodo `.then()` permette di definire questi comportamenti tramite **funzioni di callback**.


> [!abstract] ### Cos’è una callback
>
>Una **callback** è: 
>- ==**una funzione passata come argomento a un’altra funzione**, con l’obiettivo di essere **eseguita successivamente**, in un momento deciso dalla funzione che la riceve.==
>
>In altre parole:
>
>> **Una callback non viene eseguita subito**, ==ma viene “richiamata” (_called back_) quando si verifica un certo evento o quando un’operazione termina.==
>
>Esempi tipici di situazioni in cui si usano callback:
>
>- al termine di un’operazione asincrona (Promise, `setTimeout`, `fetch`)
  >  
>- in risposta a un evento (click, submit)
  >  
>- per personalizzare il comportamento di una funzione generica
>> [!remember] **Callback ≠ funzione anonima**
>> È importante chiarire un equivoco comune:
>>
> ❌ **Una callback non è necessariamente una funzione anonima**
>>
>>==Una callback è definita **dal ruolo che svolge**, non dalla sua forma.==
>
>
>> [!example] **Funzione anonima usata come callback**
>>```js
>> prom.then((value) => {
  console.log(value);
});
>>
>>```
>>
>>- ==la funzione è **anonima**==
 >>   
>>- ==è comunque una **callback**, perché viene passata a `then()`==
  >>  
>>- ==non ha un nome perché viene usata una sola volta==
>>  
>
> **Perché si usano spesso funzioni anonime come callback:**
>
>Le funzioni anonime sono molto comuni come callback perché:
>
>- ==rendono il codice **più compatto**==
  >  
>- ==evitano di creare funzioni che non servono altrove==
  >  
>- ==migliorano la leggibilità quando la logica è semplice==
  >  
>
>Esempio tipico con Promise:
>```js
>prom.then(
  value => console.log(value),
  error => console.error(error)
);
>
>```


> [!abstract] **`resolve` e `reject` sono callback?**
> Si, sono funzioni di callback che non vengono definite dal programmatore ma dal costruttore `Promise`. 
> **Analisi del costruttore `Promise`** 
>```js
> const prom = new Promise((resolve, reject) => {
  // ...
});
>
>```
>
>1. **La funzione passata a `new Promise(...)` è una callback**
>```js
>(resolve, reject) => {
  // codice
}
>
>```
>- Questa funzione è chiamata **[[#Executor Function|executor]]**
  >  
>- È una **callback** perché:
 >   
  >  - ==viene **passata come argomento**==
  >      
   > - ==viene **eseguita automaticamente** dal costruttore `Promise`==
   >     
>- Viene eseguita **subito**, ma il suo scopo è avviare un’operazione asincrona.
>  
>2. **`resolve` e `reject` sono callback da `Promise`**
>```js
>(resolve, reject) => {
  resolve('OK');
  reject('Errore');
}
>
>```
>- `resolve` e `reject` sono **funzioni**
  >  
>- Sono **callback** perché:
>    
 >   - ==non le hai scritte il programmatore==
  >      
  >  - ==vengono chiamate **per notificare a Promise l’esito**==
  >      
>- Servono a comunicare a `Promise`:
>    
  >  - **successo → `resolve(value)`**
  >      
  >  - **fallimento → `reject(reason)`**
  >    
  >> [!faq] **Chi chiama chi? (flusso mentale)**
>> - **Il programmatore** passa una funzione a `Promise` → _callback executor_
>>  
>>- **Promise** chiama quella funzione
>>  
>>- **Promise** passa due callback:
>>    
 >>   - `resolve`
 >>       
 >>   - `reject`
>>      
>>- **Il programmatore** decidi **quando** chiamarle
>>    
>>- **Promise** reagisce:
>>    
 >>  - esegue i `.then()` o `.catch()`



#### Callback di successo (Promise fulfilled)
Quindi per gestire una Promise che cambia stato da [[#^pending|pending]] e [[#^fullfilled|fulfilled]], si utilizza il metodo `.then()` passando una funzione di callback che verrà eseguita quando la Promise è fulfilled.
**Esempio**
```js
const prom = new Promise((resolve, reject) => {
  resolve('Yay!');
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

prom.then(handleSuccess);
```

**Spiegazione**
- `prom` ==è una Promise che viene immediatamente risolta con il valore `'Yay!'`==
    
- `handleSuccess` è una funzione che:
    
    - ==riceve il valore risolto della Promise==
        
    - ==lo stampa in console==
        
- chiamando `.then(handleSuccess)`:
    
    - ==JavaScript registra la funzione `handleSuccess`==
        
    - ==quando la Promise viene fulfilled, `handleSuccess('Yay!')` viene eseguita==

**Output:**
```js
Yay!
```

####  Gestire sia successo che fallimento

Nella pratica reale, quando consumiamo una Promise **non sappiamo in anticipo** se verrà risolta o rifiutata.  
Per questo motivo è necessario gestire **entrambi i casi**.

Il metodo `.then()` può ricevere **due callback**:

1. ==una per il successo==
    
2. ==una per il fallimento== 

**Esempio con successo e fallimento**
```js
const prom = new Promise((resolve, reject) => {
  const num = Math.random();

  if (num < 0.5) {
    resolve('Yay!');
  } else {
    reject('Ohhh noooo!');
  }
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

const handleFailure = (rejectionReason) => {
  console.log(rejectionReason);
};

prom.then(handleSuccess, handleFailure);
```

 **Spiegazione del codice:**

- `prom` è una Promise che:
    
    - ==viene risolta con `'Yay!'` se `num < 0.5`==
        
    - ==viene rifiutata con `'Ohhh noooo!'` altrimenti==
        
- Vengono definite due funzioni:
    
    - `handleSuccess` → gestisce il caso di successo
        
    - `handleFailure` → gestisce il caso di fallimento
        
- Passando entrambe le funzioni a `.then()`:
    
    - se la Promise è [[#^fullfilled|fulfilled]] → viene chiamata `handleSuccess`
        
    - se la Promise è [[#^rejected|rejected]] → viene chiamata `handleFailure`.



### Separation of Concerns (separazione delle responsabilità)
La separazione delle responsabilità si riferisce a una regola di buona programmazione: 
- organizzare il codice in **sezioni distinte**;
    
- assegnare a ciascuna sezione **una responsabilità specifica**.
Questo rende il codice più leggibile e manutenibile.

> [!warning] **Questo concetto non è rilegato solo a JavaScript ma si estende a qualsiasi linguaggio di programmazione, poiché interessa la logica stessa di programmazione**

Nel contesto delle Promise, questo significa:

- **separare la logica del successo**
    
- dalla **logica del fallimento**

Come detto ampiamente il metodo `.then()`: 
- **restituisce sempre una nuova Promise**
    
- se **non** gestisce un certo esito (successo o fallimento),  
    la nuova Promise **mantiene lo stesso stato** della precedente.
In altre parole:

- se la Promise originale è `fulfilled` e non c’è un handler di successo → il valore passa avanti
    
- se è `rejected` e non c’è un handler di fallimento → l’errore passa avanti
    

Questa caratteristica rende possibile il **chaining**.


#### Gestire successo e fallimento con `.then()`
Fino ad ora abbiamo gestito gli stati di successo e fallimento con il metodo `.then()` poiché restituisce sempre una nuova Promise: 
```js
prom.then(
  (resolvedValue) => {
    console.log(resolvedValue);
  },
  (rejectionReason) => {
    console.log(rejectionReason);
  }
);
```

Qui:

- il primo `.then()` gestisce **solo il successo**
    
- il secondo `.then()` gestisce **solo il fallimento**

Tuttavia, questo **mescola due responsabilità** nello stesso punto del codice.

#### Separazione successo e fallimento (separation of concerns)
Per seguire i principi della separazione delle responsabilità e quindi per rendere il codice più chiaro JS mette a disposizione `.catch()`
##### Caratteristiche di `.catch()`
- accetta **un solo handler**: `onRejected`
    
- viene eseguito **solo se una Promise è rifiutata**
    
- è equivalente a:
```js
.then(null, onRejected)
```

##### Uso consigliato: `.then()` + `.catch()`
```js
prom
  .then((resolvedValue) => {
    console.log(resolvedValue);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
```

In questo modo:

- `.then()` → ==gestisce il **caso di successo**==
    
- `.catch()` → ==gestisce il **caso di errore**==
    

Difatti viene rispettata la separazione delle responsabilità e il codice diventa più chiaro e leggibile.

###### Cosa succede davvero quando la Promise viene rifiutata?
**Scenario: la Promise viene rifiutata**
```js
prom
  .then((resolvedValue) => {
    console.log("SUCCESS:", resolvedValue);
  })
  .catch((rejectionReason) => {
    console.log("ERROR:", rejectionReason);
  });
```
Supponiamo che `prom` faccia:
```js
reject("Ohhh noooo!");
```

**Flusso di esecuzione:**

1. ==La Promise `prom` è **rejected**==
    
2. Il `.then()`:
    
    - ==**non esegue** l’handler di successo==
        
    - ==restituisce comunque **una nuova Promise**==
        
3. Questa nuova Promise è:
    
    - `rejected`
        
    - con **lo stesso motivo**: `"Ohhh noooo!"`
        
4. ==La Promise rifiutata arriva a `.catch()`==
    
5. ==`.catch()` intercetta l’errore e lo gestisce==
Output finale:
```text
ERROR: Ohhh noooo!
```

Il codice nel `.then()` **non viene eseguito**.


> [!faq] **Perché si dice "`.then()` propaga l' errore"?**
> Perché `.then()`:
>
>- ==**non elimina** la Promise==
  >  
>- ==ne crea una nuova==
  >  
>- ==se non gestisce il fallimento, **lascia passare l’errore invariato**==
  >  
>
>Questo permette a `.catch()` di intercettarlo più avanti nella catena.


> [!abstract] **Schema mentale (molto importante)**
>```text
>prom (rejected)
 >  |
 >  v
>.then(handlerSuccess)
>   - handlerSuccess NON eseguito
 >  - ritorna una Promise rejected con lo stesso errore
>   |
>   v
>.catch(handlerFailure)
>   → gestisce l’errore
>
>```

### Esercizio: uso di `.then()` e `.catch()` con una Promise reale

L’obiettivo dell’esercizio è **simulare un controllo di magazzino asincrono** e consumare la Promise risultante usando `.then()` e `.catch()`.
1. **Oggetto `inventory`**
```js
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};
```

`inventory` rappresenta il **magazzino**:

- la chiave è il nome dell’articolo
    
- il valore è la quantità disponibile
2. La funzione `checkInventory(order)`
```js
const checkInventory = (order) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let inStock = order.every(item => inventory[item[0]] >= item[1]);

      if (inStock) {
        resolve(`Thank you. Your order was successful.`);
      } else {
        reject(`We're sorry. Your order could not be completed because some items are sold out.`);
      }
    }, 1000);
  });
};
```
**Cosa fa questa funzione:**

- **restituisce una Promise**
    
- simula un’operazione asincrona tramite `setTimeout`
    
- controlla se **tutti gli articoli richiesti** sono disponibili in quantità sufficiente

**Il parametro `order`**

`order` è un array di ordini nella forma:

```js
[
  ['nomeArticolo', quantitàRichiesta],
  ...
]
```
Esempio:
```js
[['sunglasses', 1], ['bags', 2]]
```

3. **Uso di `.every()`**
```js
let inStock = order.every(item => inventory[item[0]] >= item[1]);
```

- `.every()` ==restituisce `true` **solo se tutti gli elementi** soddisfano la condizione==
    
- per ogni `item`:
    
    - `item[0]` → nome dell’articolo
        
    - `item[1]` → quantità richiesta
        
- confrontiamo la quantità richiesta con quella disponibile in `inventory`
    

Risultato:

- `true` → tutti gli articoli sono disponibili
    
- `false` → almeno un articolo non è disponibile
4. **Risoluzione o rifiuto della Promise:**
```js
if (inStock) {
  resolve(`Thank you. Your order was successful.`);
} else {
  reject(`We're sorry. Your order could not be completed because some items are sold out.`);
}
```

- `resolve()` → Promise **fulfilled**
    
- `reject()` → Promise **rejected**

Qui nasce la Promise che verrà poi consumata con `.then()` e `.catch()`

5. **Consumo della Promise con `.then()` e `.catch()`**
```js
const order = [['sunglasses', 0], ['bags', 2]];

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

const handleFailure = (rejectReason) => {
  console.log(rejectReason);
};

checkInventory(order)
  .then(handleSuccess)
  .catch(handleFailure);
```

6. **Flusso di esecuzione completo**

Caso 1: ordine valido (Promise fulfilled)

1. `checkInventory(order)` viene invocata
    
2. la Promise entra in stato **pending**
    
3. dopo 1 secondo:
    
    - `inStock === true`
        
    - viene chiamato `resolve(...)`
        
4. la Promise diventa **fulfilled**
    
5. `.then()` riceve il valore risolto
    
6. `handleSuccess()` viene eseguita
    

Output:
```text
Thank you. Your order was successful.
```

Caso 2: ordine non valido (Promise rejected)
- `checkInventory(order)` viene invocata
    
- la Promise entra in stato **pending**
    
- dopo 1 secondo:
    
    - `inStock === false`
        
    - viene chiamato `reject(...)`
        
- la Promise diventa **rejected**
    
- `.then()` **non esegue** il suo handler
    
- la Promise rifiutata viene propagata
    
- `.catch()` intercetta l’errore
    
- `handleFailure()` viene eseguita
```text
We're sorry. Your order could not be completed because some items are sold out.
```