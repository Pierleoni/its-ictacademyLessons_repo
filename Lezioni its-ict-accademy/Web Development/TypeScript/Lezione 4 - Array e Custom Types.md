# Array in TypeScript

Fino ad ora abbiamo lavorato con tipi primitivi — `string`, `number`, `boolean` — e abbiamo visto come TypeScript li gestisce attraverso [[Lezione 1 - Introduzione a Typescript#Type Inference|inference]], [[Lezione 1 - Introduzione a Typescript#Type Annotations|annotations]], e [[Lezione 1 - Introduzione a Typescript#Type Shapes|type shapes]]. 
Abbiamo anche visto come questi concetti si applicano alle funzioni, [[Lezione 3 - Le funzioni in Typescript#Parameter Type Annotations|proteggendo i parametri]] e i valori di ritorno.

È arrivato il momento di affrontare una struttura dati fondamentale che useremo continuamente: gli **array**. 
Tipizzare un array introduce una complessità nuova rispetto ai primitivi — ==non si tratta più di tenere traccia del tipo di un singolo valore, ma del tipo di **tutti gli elementi** che quell'array contiene.==

Considera questi due array:
```ts
let firstArray = [1, 2, 3, 4];
let secondArray = [5, '6', [7]];
```

Il primo contiene solo `number` — è omogeneo e prevedibile. Il secondo mescola `number`, `string` e un altro `Array` — è eterogeneo e molto più difficile da gestire in modo sicuro.

In [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Definire Array in JS|JavaScript]] entrambi sono perfettamente validi, senza alcuna distinzione. **TypeScript invece ci permette di essere precisi su cosa un array può contenere** — e nelle sezioni successive vedremo esattamente come.

#### Il problema senza TypeScript

Prima di vedere come TypeScript gestisce gli array, vale la pena capire quanto sia macchinoso farlo manualmente in [[Lezione 3; Array, Indexing, Attributo Length, Operatori, Conversione tra tipi di variabili#Definire Array in JS|JavaScript puro]] — perché è esattamente il problema che TypeScript risolve.

Immagina un array di nomi clienti che non deve contenere valori numerici, pena il crash dell'intero sistema:
```js
let customersArray = [
  'Custy Stomer', 'C. Oostomar', 'C.U.S. Tomer',
  3432434, 'Custo Mer', 'Custopher Ustomer',
  3432435, 'Kasti Yastimeur'
];
```

Per verificare che ogni elemento sia una `string` bisogna scrivere una funzione apposita con un controllo manuale su ogni elemento:
```js
function checkCustomersArray() {
  for (let i = 0; i < customersArray.length; i++) {
    if (typeof customersArray[i] !== 'string') {
      console.log(`Type error: ${customersArray[i]} should be a string!`);
    }
  }
}

checkCustomersArray();
// Type error: 3432434 should be a string!
// Type error: 3432435 should be a string!
```

Ma non basta — qualcuno potrebbe usare `.push()` per aggiungere un valore non stringa all'array. Serve quindi un'altra funzione che controlli il tipo prima di fare il push:
```js
function stringPush(val) {
  if (typeof val === 'string') {
    customersArray.push(val);
  }
}
```

E nonostante tutto questo codice extra, nulla impedirebbe a qualcuno di scrivere direttamente `customersArray[4] = 4` — vanificando tutti i controlli.

>[!todo] **Questo è esattamente il punto:** 
>==in JavaScript mantenere un array tipizzato richiede controlli manuali ovunque, su ogni operazione, senza alcuna garanzia.== 
>TypeScript risolve tutto questo alla radice — come vedremo nelle sezioni successive.


### Array Type Annotations

Nella sezione precedente abbiamo visto quanto sia macchinoso garantire la consistenza dei tipi in un array in JavaScript puro. 
**TypeScript risolve tutto questo con una sintassi semplice e diretta:** 
- ==si aggiunge `[]` dopo il tipo degli elementi.== 

```ts
let names: string[] = ['Danny', 'Samantha'];
```

==Questa annotation dice a TypeScript che `names` è un array che può contenere **solo** elementi di tipo `string`.== 
Esiste anche una sintassi alternativa: 
-  `Array<T>`; ==dove `T` è il tipo degli elementi==
```ts
let names: Array<string> = ['Danny', 'Samantha'];
```

Le due forme sono equivalenti — ==la prima è più comune e concisa, la seconda è utile da conoscere perché la ritroveremo quando studieremo i **generics**.==

La type annotation sugli array protegge da due categorie di errori. 

1. ==La prima è l'assegnazione di un array del tipo sbagliato==:
```ts
let names: string[] = [1, 2, 3]; // ❌ Type Error!
```

2. La seconda — e più interessante — ==è l'aggiunta di elementi del tipo sbagliato dopo la dichiarazione==:
```ts
let names: string[] = ['Damien'];
names.push(666); // ❌ Type Error!
```

Quest'ultimo punto risolve esattamente il problema che abbiamo visto nell'esercizio precedente con `stringPush()` — non serve più una funzione apposita per controllare il tipo prima del push. TypeScript lo fa automaticamente per noi.

>[!remember] **Ricorda la distinzione tra `string[]` e `string`:** 
>==il primo è un array di stringhe, il secondo è una singola stringa. Confonderli è un errore comune all'inizio.==


### Multidimensional Arrays

Abbiamo visto che TypeScript permette di tipizzare array di primitivi come `string[]` e `number[]`. 
Ma possiamo creare array di qualsiasi tipo — inclusi array di array, ovvero **array multidimensionali**:
```ts
let arr: string[][] = [['str1', 'str2'], ['more', 'strings']];
```

**La notazione `string[][]` si legge come `(string[])[]`:**
-  ==un array in cui ogni elemento è a sua volta un `string[]`.== 
**Si può estendere questo concetto a quante dimensioni si vuole:** ==`string[][][]` sarebbe un array di array di array di stringhe.==

**Un altro dettaglio utile:** 
- ==un array vuoto `[]` è compatibile con qualsiasi tipo di array.== 
TypeScript non può inferire il tipo da un array senza elementi, quindi accetta qualsiasi tipo dichiarato:
```ts
let names: string[] = [];   // ✅ nessun errore
let numbers: number[] = []; // ✅ nessun errore

names.push('Isabella'); // ✅
numbers.push(30);       // ✅
names.push(30);         // ❌ Type Error!
```

Una volta dichiarato il tipo, anche un array inizialmente vuoto è protetto — ==TypeScript ricorda la sua type annotation e controlla ogni elemento aggiunto.==

> [!remember] **`string[][]` è utile in molti contesti reali — tabelle di dati, matrici, risultati di query strutturati in righe e colonne.** 
> Tienilo a mente quando inizieremo a lavorare con strutture dati più complesse.

 

---

## Tuples

Finora abbiamo visto array in cui tutti gli elementi sono dello stesso tipo — `string[]`, `number[]`, e così via. 
Ma a volte abbiamo bisogno di una struttura più precisa: 
- ==un array con un numero fisso di elementi, ognuno con il proprio tipo specifico.== 
In TypeScript questa struttura si chiama **tuple**:
```ts
let ourTuple: [string, number, string, boolean] = ['Is', 7, 'our favorite number?', false];
```

==Una tuple non si limita a dichiarare i tipi degli elementi — definisce anche il loro **ordine** e la loro **lunghezza**.== 
**Entrambe le condizioni devono essere rispettate, altrimenti TypeScript segnala un errore:**

```ts
let numbersTuple: [number, number, number] = [1, 2, 3, 4];
// ❌ Type Error! La tuple dovrebbe avere solo tre elementi

let mixedTuple: [number, string, boolean] = ['hi', 3, true];
// ❌ Type Error! Il primo elemento dovrebbe essere un number
```


> [!help] **Array vs Tuple — la differenza fondamentale:**
> 
> 
> ||Array|Tuple|
> |---|---|---|
> |Lunghezza|libera|fissa|
> |Tipi|tutti uguali|specifici per posizione|
> |Esempio|`string[]`|`[string, number, boolean]`|
> 
> La vera distinzione non è "un tipo vs più tipi" — ma **lunghezza fissa + ordine garantito** vs **lunghezza libera + tipo omogeneo**.

**A livello di JavaScript, le tuple si comportano esattamente come array normali:** 
- ==hanno `.length`, si accede agli elementi con `[index]`, e si possono modificare.== 
Ma TypeScript le tratta come tipi **distinti e non intercambiabili**:
```ts
let tup: [string, string] = ['hi', 'bye'];
let arr: string[] = ['there', 'there'];

tup = ['there', 'there']; // ✅ ok — è una tuple letterale
tup = arr;                // ❌ Type Error! Un array non può essere assegnato a una tuple
```

Anche se un `string[]` contiene esattamente gli stessi elementi di una `[string, string]`, per TypeScript sono tipi diversi. Una tuple è una **promessa sul numero e sull'ordine degli elementi** — un array generico non può fare la stessa promessa.

>[!info] Le tuple sono particolarmente utili quando si lavora con funzioni che restituiscono più valori di tipo diverso, o con strutture dati dove la posizione degli elementi ha un significato preciso — come coordinate `[x, y]` o una coppia `[chiave, valore]`.

>[!warning] **Attenzione alle tuple a runtime:** 
>TypeScript garantisce la lunghezza fissa di una tuple solo a **compile time** — ==controlla che la dichiarazione iniziale rispetti il numero e l'ordine dei tipi dichiarati.== 
>==Ma metodi come `.push()` agiscono a **runtime**, dove il `.js` compilato non sa nulla della tupla — la tratta come un array normale e aggiunge elementi senza protestare.==
>```ts
>let tup: [number, number, number] = [1, 2, 3];
>tup.push(4); // ⚠️ nessun errore a compile time, ma viola il contratto della tupla
>tup = [5] // ⚠️ da errore anche al momento di run-time non solo a compile-time perché in questo caso viola il contratto della tupla
>```
> **È uno dei casi in cui il confine tra compile time e runtime ha conseguenze pratiche concrete** — ==la garanzia di TypeScript non è assoluta.==

### Array Type Inference

Abbiamo visto che TypeScript inferisce i tipi automaticamente da variabili e funzioni. Ma con gli array sorge una domanda interessante — considera questo esempio:
```ts
let examAnswers = [true, false, false];
```

TypeScript potrebbe inferire due tipi diversi:

- `boolean[]` → ==un array di booleani di lunghezza libera==
- `[boolean, boolean, boolean]` → ==una tupla di esattamente tre booleani==

Quale dei due sceglie? 
- ==Sceglie sempre **il tipo meno restrittivo** — quindi `boolean[]`.== 
La logica è semplice: 
- ==TypeScript non vuole limitare inutilmente una variabile quando non c'è una type annotation esplicita che lo richieda.== 
Il risultato pratico è che possiamo aggiungere elementi senza errori:
```ts
examAnswers[3] = true; // ✅ nessun errore — è un boolean[]
```

Se invece vogliamo una tuple dobbiamo dichiararlo **esplicitamente** — perché TypeScript non la inferirà mai da solo:
```ts
let tupleOfExamAnswers: [boolean, boolean, boolean] = [true, false, false];
tupleOfExamAnswers[3] = true; // ❌ Type Error! La tuple ha solo 3 elementi
```

==Questo comportamento si ripercuote anche sui metodi che producono nuovi array.== 
Con `.concat()` ad esempio, anche partendo da una tuple il risultato viene inferito come array — perché la concatenazione produce una struttura di lunghezza variabile, non più prevedibile a compile time:
```ts
let tup: [number, number, number] = [1, 2, 3];
let concatResult = tup.concat([4, 5, 6]);
// concatResult → number[], non [number, number, number, ...]
```

>[!ticket] **La regola d'oro:** 
>l'inferenza restituisce **sempre array, mai tuple**. 
>==Questo perché le tuple sono una struttura più restrittiva — e TypeScript non applica restrizioni che non gli sono state richieste esplicitamente.== 
>Vuoi una tuple? Dichiarala con una type annotation. Altrimenti TypeScript sceglierà sempre la strada più flessibile.

> [!link]
> ##### **Ciclo di vita di una tupla TypeScript:**
> Come abbiamo visto nella lezione 1 alla sezione [[Lezione 1 - Introduzione a Typescript#Come funziona TypeScript in pratica|Come funziona TypeScript in pratica]] e come abbiamo maggiormente approfondito nella sezione [[Lezione 1 - Introduzione a Typescript#Compilare ed eseguire TypeScript|Compilare ed eseguire TypeScript]], anche per le tuple, e più in generale per qualsiasi statement/clausola/ regola di TypeScript, valgono le stesse regole spiegate in queste due sezioni:
> 1. **Dichiarazione** → TypeScript applica i contratti della tupla: lunghezza fissa, ordine e tipi specifici per ogni posizione
> 2. **Compile time** → `tsc` compila il file `.ts` in un file `.js` omonimo, verificando che tutti i contratti siano rispettati. Le tuple diventano semplici array JavaScript — i contratti TypeScript spariscono
> 3. **Runtime** → Node.js esegue il file `.js`, non il `.ts`. A questo punto non esiste più nessuna tupla — solo array JavaScript normali, su cui tutti i metodi built-in come `.push()` e `.concat()` funzionano liberamente senza alcun vincolo di lunghezza
> 
> La garanzia di TypeScript sulle tuple è quindi **esclusivamente a compile time**. Tutto ciò che accade a runtime è puro JavaScript.


#### Dimostrazione pratica
Un esercizio che mette alla prova la comprensione dell'inferenza sugli array. L'obiettivo è dichiarare una variabile di tipo `string[]` partendo da una tupla, **senza usare `[]`, `Array`, o type annotations esplicite**:
```ts
let dogTup: [string, string, string, string] = ['dog', 'brown fur', 'curly tail', 'sad eyes'];

let myArr = dogTup.concat(dogTup);
```

La soluzione sfrutta due concetti visti in questa sezione:

- ==`.concat()` su una tupla restituisce sempre un `string[]`, mai una tupla==
- ==l'inferenza sceglie sempre il tipo meno restrittivo==

**La prova che `myArr` è effettivamente un array e non una tupla — possiamo accedere a un indice arbitrario senza errori:**
```ts
myArr[50] = 'not a dog'; // ✅ ok — myArr è string[], lunghezza libera
```

Se `myArr` fosse stata una tupla, accedere all'indice `50` avrebbe generato un errore a compile time — la tupla originale ha solo 8 elementi dopo la concatenazione.


### Rest Parameters

Abbiamo visto come tipizzare parametri singoli e opzionali. 
Ma JavaScript permette anche di definire funzioni che accettano un numero **variabile** di argomenti tramite i **rest parameters** — e TypeScript li supporta con la stessa sintassi degli array.

Considera questa funzione che concatena un numero arbitrario di stringhe:
```ts
function smush(firstString: string, ...otherStrings: string[]) {
  let output = firstString;
  for (let i = 0; i < otherStrings.length; i++) {
    output = output.concat(otherStrings[i]);
  }
  return output;
}

smush('a', 'h', 'h', 'H', 'H', 'H', '!', '!'); // ✅ Restituisce: 'ahhHHH!!'
smush(1, 2, 3); // ❌ Type Error! I parametri devono essere string
```

La sintassi `...otherStrings: string[]` dice che:
- ==TypeScript che tutti gli argomenti aggiuntivi oltre al primo verranno raccolti in un array di `string`.== 
Questo rende la funzione **type safe** — ==chiunque provi a passare valori non stringa riceverà un errore a compile time.==

> [!NOTE] Il rest parameter deve essere sempre **l'ultimo parametro** della funzione — ha senso, perché raccoglie tutti gli argomenti rimanenti. 
>>[!ticket] Può esserci solo un rest parameter per funzione.
> 


> [!example] **Analogia con Python e differenza con lo Spread Operator:**
>
>I rest parameters di TypeScript sono concettualmente identici a [[Funzioni in Python#Funzioni e `*args`|`*args`]] di Python — entrambi raccolgono un numero variabile di argomenti in una struttura iterabile:
>
>```python
># Python
>def smush(*args):
>    return ''.join(args)
>```
>
>```ts
>// TypeScript
>function smush(firstString: string, ...otherStrings: string[]) { }
>```
>
>La differenza principale è che: 
> - ==in TypeScript si possono avere parametri normali **prima** del rest parameter,== 
> - ==mentre in Python `*args` raccoglie tutto il variabile indipendentemente dalla posizione.==
>
>> [!fail] Da non confondere con lo **spread operator** di JavaScript — usano entrambi `...` ma fanno l'opposto:
>> |Simbolo|Direzione|Esempio|
|---|---|---|
|Rest parameter|`...`|**raccoglie** argomenti in un array|`function f(...args: string[])`|
|Spread operator|`...`|**espande** un array in argomenti separati|`f(...myArray)`|
>>
>>Stesso simbolo, direzione opposta.

