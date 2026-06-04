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

Le due forme sono equivalenti:
1. ==la prima è più comune e concisa==, 
2. ==la seconda è utile da conoscere perché la ritroveremo quando studieremo i **generics**.==

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
>> [!fail] Da non confondere con lo **[[Lezione 6; DOM e ripasso JS#Spread operator|spread operator]]** di JavaScript — usano entrambi `...` ma fanno l'opposto:
>> |Simbolo|Direzione|Esempio|
|---|---|---|
|Rest parameter|`...`|**raccoglie** argomenti in un array|`function f(...args: string[])`|
|Spread operator|`...`|**espande** un array in argomenti separati|`f(...myArray)`|
>>
>>Stesso simbolo, direzione opposta.

#### Spread Syntax con le Tuple

Nella nota precedente abbiamo visto che lo [[Lezione 6; DOM e ripasso JS#Spread operator|spread operator]] **espande** un array in argomenti separati — ed è esattamente qui che le tuple diventano particolarmente potenti. 
Considera questa funzione con una firma molto lunga e difficile da leggere:
```ts
function gpsNavigate(
  startLatitudeDegrees: number, startLatitudeMinutes: number, startNorthOrSouth: string,
  startLongitudeDegrees: number, startLongitudeMinutes: number, startEastOrWest: string,
  endLatitudeDegrees: number, endLatitudeMinutes: number, endNorthOrSouth: string,
  endLongitudeDegrees: number, endLongitudeMinutes: number, endEastOrWest: string
) { }
```

Chiamarla direttamente è un disastro in termini di leggibilità:
```ts
gpsNavigate(40, 43.2, 'N', 73, 59.8, 'W', 25, 0, 'N', 71, 0, 'W'); // 😱
```

**La soluzione elegante è:** 
- ==usare le tuple per raggruppare i dati correlati, e poi lo spread operator per espanderle nella chiamata.==
```ts
let codecademyCoordinates: [number, number, string, number, number, string] = [40, 43.2, 'N', 73, 59.8, 'W'];
let bermudaTCoordinates: [number, number, string, number, number, string] = [25, 0, 'N', 71, 0, 'W'];

gpsNavigate(...codecademyCoordinates, ...bermudaTCoordinates); // ✅ molto più leggibile
gpsNavigate(...bermudaTCoordinates, ...codecademyCoordinates); // ✅ e il ritorno è banale
```

==La [[Lezione 1 - Introduzione a Typescript#Type Annotations|type annotation]] della tupla garantisce che gli elementi siano esattamente del tipo corretto per i parametri di `gpsNavigate()`== — **se l'ordine o i tipi non corrispondono, TypeScript lo segnala a compile time.**

>[!info] **Questo è uno dei casi in cui tuple e spread operator si combinano perfettamente:** 
> ==la tupla garantisce la **correttezza dei tipi**, lo spread operator garantisce la **leggibilità del codice**.== 
> Insieme risolvono un problema che in JavaScript puro richiederebbe controlli manuali e codice difficile da leggere.


#### Dimostrazione pratica — Array di Tuple con Spread Syntax
Un caso d'uso reale che combatte tre concetti insieme: array di tuple,
spread syntax e funzioni tipizzate:
```ts
// Funzione che accetta una stringa, un numero e un booleano
function performDanceMove(moveName: string, moveReps: number, hasFlair: boolean): void {
  console.log(`I do the ${moveName} ${moveReps} times !`);
  // Se hasFlair è truthy stampa una stringa aggiuntiva
  if (hasFlair) {
    console.log('I do it with flair!');
  }
}

// Array di tuple — ogni elemento contiene esattamente gli argomenti di performDanceMove()
let danceMoves: [string, number, boolean][] = [
  ['chicken beak', 4, false],
  ['wing flap', 4, false],
  ['tail feather shake', 4, false],
  ['clap', 4, false],
  ['chicken beak', 4, true],
  ['wing flap', 4, true],
  ['tail feather shake', 4, true],
  ['clap', 4, true],
];

// Iteriamo sull'array e usiamo lo spread operator per espandere ogni tupla
// come argomenti separati della funzione
danceMoves.forEach((move) => performDanceMove(...move));
```

La type annotation `[string, number, boolean][]` garantisce che ogni elemento dell'array sia una tupla compatibile con la firma di `performDanceMove()` — se qualcuno inserisse una tupla con tipi sbagliati o in ordine diverso, TypeScript lo intercetterebbe a compile time.



---

## Tipi Custom in TypeScript
Fino ad ora abbiamo lavorato con i tipi predefiniti di TypeScript — primitivi come `string`, `number`, `boolean`, e strutture come array e tuple. 
È già un ottimo arsenale, ma TypeScript offre qualcosa di ancora più potente: 
- ==la possibilità di **creare tipi personalizzati**, costruiti sulle nostre esigenze specifiche.==

In realtà abbiamo già incontrato un esempio di tipo custom senza saperlo — le **tuple**. 
Una tupla come `[string, string, number, boolean]` è un tipo custom che descrive esattamente la struttura di un dato, ad esempio le informazioni di un utente: nome, cognome, età e se ha un account premium.



>[!example] **Un modo utile per visualizzare la differenza:**
>>[!done] I tipi predefiniti sono come ingredienti — utili da soli, ma limitati. 
>
>>[!done] I tipi custom sono come ricette complete — ingredienti combinati insieme per creare qualcosa di più preciso e significativo.

La buona notizia è che i tipi custom si usano esattamente come quelli predefiniti — ==come type annotations su variabili e parametri, come return type delle funzioni, e con l'inferenza automatica==:

```ts
let myVar: compType;

function testFn(param: compType): returnedCompType { }

let inferredTypeVariable = testFn(myVar);
// inferredTypeVariable → tipo inferito: returnedCompType
```

Nelle sezioni successive vedremo tutti gli strumenti che TypeScript mette a disposizione per costruire tipi custom — a partire dal primo e più fondamentale.
### Enums

Il primo tipo custom che esploriamo è anche uno dei più utili: gli **enum**. 
Fino ad ora i tipi che abbiamo visto hanno un insieme di valori potenzialmente infinito — una `string` può essere qualsiasi stringa, un `number` qualsiasi numero. 
Gli enum nascono per risolvere il problema opposto: 
- ==quando vogliamo **limitare** i valori possibili di una variabile a un insieme predefinito e finito.==
```ts
enum Direction {
  North,
  South,
  East,
  West
}
```

Questo enum definisce esattamente quattro valori possibili. 
Una variabile di tipo `Direction` può essere solo uno di questi — qualsiasi altro valore genera un errore:
```ts
let whichWayToArcticOcean: Direction;

whichWayToArcticOcean = Direction.North;     // ✅ ok
whichWayToArcticOcean = Direction.Southeast; // ❌ Southeast non esiste nell'enum
whichWayToArcticOcean = West;                // ❌ sintassi sbagliata, serve Direction.West
```

##### Come funzionano sotto il cofano

**TypeScript processa gli enum usando i `number`:**
- ==ogni valore viene associato a un numero in base all'ordine di dichiarazione, partendo da `0`== 
```ts
Direction.North  // 0
Direction.South  // 1
Direction.East   // 2
Direction.West   // 3
```

Questo significa che `whichWayToArcticOcean = Direction.North` è equivalente a `whichWayToArcticOcean = 0`. 
==Si può anche riassegnare direttamente un numero senza errori — TypeScript li considera equivalenti.==

Si può cambiare il numero di partenza assegnando un valore al primo elemento — gli altri seguiranno in sequenza:
```ts
enum Direction {
  North = 7, // 7
  South,     // 8
  East,      // 9
  West       // 10
}
```

Oppure assegnare valori specifici a ciascun elemento indipendentemente:
```ts
enum Direction {
  North = 8,
  South = 2,
  East = 6,
  West = 4
}
```

> [!done] ==Gli enum sono particolarmente utili quando si lavora con valori che hanno un significato semantico preciso — stati di un'applicazione, direzioni, ruoli utente, categorie.== 
> 
> Invece di usare stringhe o numeri magici sparsi nel codice, gli enum raccolgono tutti i valori possibili in un unico posto con nomi significativi.

##### Dimostrazione pratica

Un caso d'uso reale: 
il sistema di ordini di un negozio di animali che vende solo quattro tipi di animali. 
Senza TypeScript, nulla impedisce di ordinare un animale che il negozio non ha in catalogo:
```ts
// ❌ Versione non type safe
let petOnSale = 'chinchilla'; // potrebbe diventare 'Ox' o qualsiasi altra stringa
let ordersArray = [
  ['rat', 2],
  ['chinchilla', 1],
  ['hamster', 2],
  ['chinchilla', 50]
];
```

La versione type safe usa un enum per limitare i valori possibili a esattamente i quattro animali in catalogo:

```ts
enum Pet {
  Hamster,    // 0
  Rat,        // 1
  Chinchilla, // 2
  Tarantula   // 3
}

// Variabile type safe con annotation esplicita
const petOnSaleTS: Pet = Pet.Chinchilla;

// Array di tuple type safe — ogni ordine è [Pet, number]
const ordersArrayTS: [Pet, number][] = [
  [Pet.Rat, 2],
  [Pet.Chinchilla, 1],
  [Pet.Hamster, 2],
  [Pet.Chinchilla, 50]
];

// Tentativo di ordinare un animale non in catalogo
ordersArrayTS.push([Pet.Jerboa, 3]);
// ❌ Type Error! Jerboa non esiste nell'enum Pet
```

L'enum garantisce che nessuno possa inserire un animale non previsto — né direttamente nella variabile, né nell'array degli ordini. TypeScript lo intercetta a compile time prima ancora che il codice venga eseguito.

#### String Enums vs Numeric Enums

Gli enum che abbiamo visto finora sono **numeric enums:**
- ==sotto il cofano usano numeri assegnati automaticamente.== 
TypeScript supporta anche gli **string enums**, dove ogni valore è una stringa esplicita:
```ts
enum DirectionNumber { North, South, East, West }
enum DirectionString { North = 'NORTH', South = 'SOUTH', East = 'EAST', West = 'WEST' }
```

==A differenza dei numeric enums, nei string enums i valori devono essere scritti **esplicitamente**==.
==TypeScript non può assegnarli automaticamente.== 
La convenzione più comune e consigliata è usare il nome del valore in maiuscolo (`North = 'NORTH'`), così i messaggi di errore e i log saranno molto più leggibili e informativi.

> [!faq] **Perché preferire i String Enums**
> 
> 
> I numeric enums hanno un comportamento permissivo che può far passare bug inosservati — accettano qualsiasi numero, anche arbitrario, senza protestare:
> ```ts
> let whichWayToAntarctica: DirectionNumber;
> 
> whichWayToAntarctica = 1;      // ✅ ok — equivalente a DirectionNumber.South
> whichWayToAntarctica = 943205; // ✅ ok — nessun errore, numero arbitrario!
> ```
> 
> I string enums sono molto più **strict** — ==l'unico modo per assegnare un valore è usare esplicitamente l'enum, anche se la stringa coincide esattamente con il valore dichiarato==:
> ```ts
> let whichWayToAntarctica: DirectionString;
> 
> whichWayToAntarctica = 'SOUTH';            // ❌ Type Error!
> whichWayToAntarctica = 'stringa qualsiasi'; // ❌ Type Error!
> whichWayToAntarctica = DirectionString.South; // ✅ unico modo valido
> ```
> 
> 
>
>>[!hint] La raccomandazione è di usare **sempre string enums** — ==sono più sicuri, più leggibili nei log e negli errori, e non permettono assegnazioni numeriche arbitrarie che potrebbero introdurre bug silenziosi.==


### Object Types

Arriviamo ora a uno dei tipi custom più comuni e utili di TypeScript: gli **object types**. 
==Permettono di descrivere con precisione la struttura di un oggetto — quali proprietà deve avere e di che tipo devono essere.==

La sintassi è simile a un [[Lezione 6; DOM e ripasso JS#Gli oggetti in Javascript|oggetto letterale JavaScript]], ma al posto dei valori si specificano i tipi:
```ts
let aPerson: {name: string, age: number};
```

TypeScript verifica sia i **tipi** delle proprietà che i loro **nomi** — entrambi devono corrispondere esattamente:
```ts
aPerson = {name: 'Aisle Nevertell', age: "wouldn't you like to know"};
// ❌ Type Error! age deve essere number, non string

aPerson = {name: 'Kushim', yearsOld: 5000};
// ❌ Type Error! la proprietà si chiama age, non yearsOld

aPerson = {name: 'User McCodecad', age: 22};
// ✅ ok — nome e tipo delle proprietà corretti
```

Le proprietà di un object type non si limitano ai primitivi — ==possono essere enum, array, e persino altri object types annidati==:
```ts
let aCompany: {
  companyName: string,
  boss: {name: string, age: number},
  employees: {name: string, age: number}[],
  employeeOfTheMonth: {name: string, age: number},
  moneyEarned: number
};
```

In questo esempio `boss` e `employeeOfTheMonth` sono object types annidati, mentre `employees` è un array di object types — TypeScript gestisce qualsiasi livello di complessità.

> Gli object types che abbiamo visto qui sono dichiarati **inline** — direttamente dove vengono usati. Nelle prossime sezioni vedremo come dare un nome a questi tipi per poterli riutilizzare in tutto il progetto, evitando di riscriverli ogni volta.


#### Dimostrazione pratica degli Object Types

Un caso concreto dove gli object types rendono una funzione molto più leggibile e type safe. Senza type annotation, il parametro `personObject` è `any` — TypeScript non può aiutarci a verificare che l'oggetto passato abbia le proprietà giuste:
```ts
// Aggiungendo l'object type annotation al parametro
function sayHappyBirthdayWithObject(personObject: {
  name: string,
  age: number,
  giftWish: string,
  success: boolean
}) {
  let output = '';
  output += 'Happy Birthday ' + personObject.name + '! ';
  output += 'You are now ' + personObject.age + ' years old! ';
  output += 'Your birthday wish was to receive ' + personObject.giftWish
         + '. And guess what? You will ';
  if (!personObject.success) {
    output += 'not ';
  }
  output += 'receive it! \n';
  console.log(output);
}

// Array di oggetti con type annotation esplicita
let birthdayBabies: {name: string, age: number, giftWish: string, success: boolean}[] = [
  {name: 'Liam',   age: 0, giftWish: 'karate skills',   success: false},
  {name: 'Olivia', age: 0, giftWish: 'a bright future', success: true},
  {name: 'Ava',    age: 0, giftWish: '$0.25',            success: true}
];

birthdayBabies.forEach(sayHappyBirthdayWithObject);
```

>[!warning] **Da notare che la stessa object type annotation viene ripetuta sia nel parametro della funzione che nell'array `birthdayBabies`.** 
>Questo è esattamente il problema che le prossime sezioni risolveranno — dare un **nome** a un object type per poterlo riutilizzare senza riscriverlo ogni volta.

### Type Aliases

Nella [[#Dimostrazione pratica degli Object Types|dimostrazione precedente]] abbiamo notato un problema: 
- ==la stessa object type annotation veniva ripetuta più volte nel codice — nel parametro della funzione e nell'array. Più si ripete qualcosa, più aumenta il rischio di typo e il codice diventa difficile da mantenere.==

I **type aliases** risolvono esattamente questo problema: 
- ==permettono di dare un **nome** a qualsiasi tipo, per poi riutilizzarlo ovunque con quella parola chiave==:
```ts
type Person = {name: string, age: number};
```

Ora invece di riscrivere `{name: string, age: number}` ogni volta, usiamo semplicemente `Person`:
```ts
let aCompany: {
  companyName: string,
  boss: Person,              // invece di {name: string, age: number}
  employees: Person[],       // invece di {name: string, age: number}[]
  employeeOfTheMonth: Person, // invece di {name: string, age: number}
  moneyEarned: number
};
```

La sintassi per dichiarare un type alias è:
```ts
type <NomeAlias> = <tipo>;
```

==I type aliases funzionano con qualsiasi tipo — primitivi, array, tuple, object types, enum.== 

> [!info] **Anche se creare un alias per un primitivo non è particolarmente utile:**
> 
> ```ts
> type MyString = string;
> let myVar: MyString = 'Hi'; // ✅ ok
> ```

> [!remember] **Un dettaglio importante:**
>  i type aliases sono **solo nomi alternativi** — **non creano tipi distinti.** 
>  ==Due alias che puntano allo stesso tipo sono completamente intercambiabili==:
>```ts
>  type MyString = string;
>type MyOtherString = string;
>
>let firstString: MyString = 'test';
>let secondString: MyOtherString = >firstString; // ✅ ok — sono lo stesso tipo
>```

**I type aliases sono uno degli strumenti più usati in TypeScript nella pratica** — ==soprattutto per gli object types e le tuple che vengono riutilizzati in più punti del codice.== 
Nelle sezioni successive vedremo strumenti ancora più potenti per definire tipi custom riutilizzabili.

#### Dimostrazione pratica dei Type Aliases

Riprendiamo [[#Spread Syntax con le Tuple|l'esempio delle coordinate GPS che abbiamo visto nella sezione sullo spread syntax]]. 
La versione originale aveva una type annotation lunga e ripetuta due volte:
```ts
// ❌ Prima — ripetizione della stessa lunga annotation
let codecademyCoordinates: [number, number, string, number, number, string] = [40, 43.2, 'N', 73, 59.8, 'W'];
let bermudaTCoordinates: [number, number, string, number, number, string] = [25, 0, 'N', 71, 0, 'W'];
```

Con un type alias la situazione migliora drasticamente — ==dichiariamo il tipo una volta sola e lo riutilizziamo ovunque==:
```ts
// ✅ Dopo — type alias riutilizzabile
type Coord = [number, number, string, number, number, string];

let codecademyCoordinates: Coord = [40, 43.2, 'N', 73, 59.8, 'W'];
let bermudaTCoordinates: Coord = [25, 0, 'N', 71, 0, 'W'];
```

> [!done] Il codice è più leggibile, meno soggetto a typo, e se in futuro la struttura delle coordinate dovesse cambiare basterà aggiornare il type alias in un solo punto invece di cercarlo e modificarlo in tutto il progetto.

### Function Types

In JavaScript le funzioni possono essere assegnate a variabili come qualsiasi altro valore. 
TypeScript estende questo concetto permettendo di ==tipizzare **esattamente** che tipo di funzione una variabile può contenere — specificando i tipi dei parametri e il tipo di ritorno.==

La sintassi usa la notazione delle arrow function, ma al posto del corpo della funzione si scrive il tipo di ritorno:
```ts
type StringsToNumberFunction = (arg0: string, arg1: string) => number;
```

**Una variabile di questo tipo può contenere qualsiasi funzione compatibile** — ==ovvero qualsiasi funzione che accetta due `string` e restituisce un `number`.== I nomi dei parametri non contano, solo i loro tipi:
```ts
let myFunc: StringsToNumberFunction;

myFunc = function(firstName: string, lastName: string) {
  return firstName.length + lastName.length; // ✅ ok
};

myFunc = function(whatever: string, blah: string) {
  return whatever.length - blah.length; // ✅ ok — i nomi non contano
};

myFunc = function(a: number, b: number) {
  return a + b; // ❌ Type Error! I parametri devono essere string
};
```

> [!ticket] **Una regola sintattica importante:**
>  i nomi dei parametri e le parentesi sono **sempre obbligatori** nella type annotation di una funzione, anche con un solo parametro:
>```ts
> type StringToNumberFunction = (string) => number;    // ❌ NO
>type StringToNumberFunction = arg: string => number; // ❌ NO
>type StringToNumberFunction = (arg: string) => number; // ✅ ok
>```


I function types sono particolarmente utili con le **callback functions** — funzioni passate come argomenti ad altre funzioni. 
==Tipizzare una callback garantisce che chiunque usi la funzione sappia esattamente che tipo di funzione deve passare come argomento.==


---

## Generic Types

Arriviamo a uno dei concetti più potenti di TypeScript: i **generic types**. Li abbiamo già incontrati senza saperlo — ricordi la sintassi alternativa per gli array `Array<T>`? Quella `T` è esattamente un generic type.

L'idea di fondo è semplice: 
- ==invece di definire un tipo specifico, definiamo un **modello di tipo** con un segnaposto — una variabile di tipo — che verrà sostituita con un tipo concreto quando il generic viene usato.==
```ts
type Family<T> = {
  parents: [T, T],
  mate: T,
  children: T[]
};
```

`Family<T>` non è un tipo utilizzabile direttamente — è un _modello_. Per usarlo bisogna sostituire `T` con un tipo concreto:
```ts
// Family<string> → {parents: [string, string], mate: string, children: string[]}
let aStringFamily: Family<string> = {
  parents: ['stern string', 'nice string'],
  mate: 'string next door',
  children: ['stringy', 'stringo', 'stringina', 'stringolio']
}; // ✅ ok

// Family<number> → {parents: [number, number], mate: number, children: number[]}
let aNumberFamily: Family<number> = {
  parents: [1, 2],
  mate: 3,
  children: [4, 5, 6]
}; // ✅ ok
```

> [!NOTE] **La `T` è solo una convenzione — si potrebbe usare qualsiasi nome come `S` o `GenericType`. L'importante è che il segnaposto sia consistente all'interno della definizione del tipo.**

I generic types sono il modo in cui TypeScript permette di scrivere codice **riutilizzabile ma comunque type safe:**
- invece di duplicare la stessa struttura per ogni tipo possibile, si definisce il modello una volta sola e lo si specializza secondo le necessità. 


> [!LINK] **È lo stesso principio dei [[Lezione 12 - Collection#Il ruolo del generico `<E>`|generics ]]in Java, che abbiamo già incontrato nel tuo percorso ITS.**
>

#### Dimostrazione pratica dei Generics
Un esempio che mostra la potenza dei generic types — lo stesso modello `Family<T>` utilizzato con quattro tipi diversi, dai primitivi agli object types custom:
```ts
type Human = {name: string, job: string};
type Dog = {name: string, tailWagSpeed: number};

type Family<T> = {
  parents: [T, T],
  mate: T,
  children: T[]
};
```

Con i primitivi — `T` viene sostituita con `number` e `boolean`:
```ts
let theFamily: Family<number> = {
  parents: [3, 4], mate: 9, children: [5, 30, 121]
};

let someFamily: Family<boolean> = {
  parents: [true, true], mate: false,
  children: [false, false, true, true]
};
```

Con i type aliases custom — `T` viene sostituita con `Human` e `Dog`:
```ts
let aFamily: Family<Human> = {
  parents: [
    {name: 'Mom', job: 'software engineer'},
    {name: 'Dad', job: 'coding engineer'}
  ],
  mate: {name: 'Matesky', job: 'engineering coder'},
  children: [{name: 'Babesky', job: 'none'}]
};

let anotherFamily: Family<Dog> = {
  parents: [
    {name: 'Momo', tailWagSpeed: 3},
    {name: 'Dado', tailWagSpeed: 100}
  ],
  mate: {name: 'Cheems', tailWagSpeed: 7},
  children: [
    {name: 'Puppin', tailWagSpeed: 0.001},
    {name: 'Puppenaut', tailWagSpeed: 0.0001},
    {name: 'Puppenator', tailWagSpeed: 0.01}
  ]
};
```

Notiamo come `Family<T>` si adatti perfettamente a qualsiasi tipo — primitivo o custom. 
==Senza i generics avremmo dovuto definire `FamilyOfNumbers`, `FamilyOfBooleans`, `FamilyOfHumans` e `FamilyOfDogs` separatamente, con la stessa identica struttura ripetuta quattro volte.==

>[!info] **Questo esercizio mostra anche come type aliases e generic types si combinino naturalmente**
> ==`Human` e `Dog` sono type aliases che vengono usati come argomenti di tipo per `Family<T>`. È la composizione di tutti i concetti visti in questa lezione.==


>[!example] **Analogia con i Generics di Java:**
> 
> I generic types di TypeScript e i [[Lezione 12 - Collection#Collection e Generics|generics di Java]] condividono la stessa idea di fondo: 
> ==definire un **modello riutilizzabile** che funziona con qualsiasi tipo, evitando di duplicare la stessa struttura per ogni tipo possibile.==
> 
> Tuttavia il loro ruolo nei due linguaggi è leggermente diverso:
> 
> >[!link] In **Java**, i generics sono quasi obbligatori per lavorare con le collezioni. 
> >==Senza di essi non sarebbe possibile avere una `ArrayList` che funziona con qualsiasi tipo — il sistema fortemente tipizzato di Java lo impedirebbe.== 
> >I generics sono quindi una necessità strutturale del linguaggio.
> 
>>[!done] In **TypeScript**, il sistema di tipi è già più flessibile di base — si potrebbe sempre ricadere su [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|`any`]] per aggirare i controlli. 
>>I generics non sono una necessità, ma uno strumento per ottenere il meglio dei due mondi: 
>>- ==**riutilizzabilità** senza rinunciare alla **type safety**.== 
>>- Come abbiamo visto con `Family<T>`, il generic garantisce che tutti i campi della struttura siano dello stesso tipo `T` — qualunque esso sia.
> 
> ||Java|TypeScript|
> |---|---|---|
> |Scopo principale|necessità strutturale per le collezioni|riutilizzabilità + type safety|
> |Senza generics|collezioni non type safe|si ricade su `any`|
> |Con generics|collezioni type safe|modelli type safe riutilizzabili|

> [!faq] ##### Cos'è la Type Safety?
> 
> 
> La **type safety** è: 
> - ==la capacità del compilatore di verificare a **compile time** che i tipi siano usati in modo corretto e consistente — prevenendo errori prima ancora di eseguire il codice.==
> 
> La differenza concreta con `any` è questa:
> 
> - Con `any` → si rinuncia alla type safety. 
> 	- ==La variabile accetta qualsiasi tipo di dato e TypeScript smette di controllare. Massima flessibilità, zero garanzie.==
> - Con i **generics** → si mantiene la flessibilità senza rinunciare alla type safety. 
> 	- ==Il tipo `T` è ancora "qualsiasi tipo", ma una volta scelto deve essere **consistente** in tutta la struttura — TypeScript lo verifica a compile time.==
> ```ts
> // Con any — nessuna garanzia
> type Family = {parents: [any, any], mate: any, children: any[]};
> // parents potrebbe essere [string, number], mate un boolean... nessun controllo
> 
> // Con generics — type safe
> type Family<T> = {parents: [T, T], mate: T, children: T[]};
> // Se T è string, TUTTO deve essere string — TypeScript lo garantisce
> ```
> I generics sono quindi il modo in cui TypeScript ottiene il meglio dei due mondi: 
> - ==**riutilizzabilità** senza rinunciare alla **type safety**.==

^82fb09


### Generic Functions

Abbiamo visto i generic types applicati ai type aliases. 
Lo stesso concetto si applica anche alle **funzioni** — e risolve un problema molto concreto.

Immagina una funzione che riempie un array con un valore ripetuto `n` volte:
```ts
function getFilledArray(value, n) {
  return Array(n).fill(value);
}

getFilledArray('cheese', 3); // ['cheese', 'cheese', 'cheese']
```


> [!tldr] **Analisi del codice:**
> `Array(n)` crea un array vuoto di lunghezza `n`, e `.fill(value)` riempie ogni elemento con il valore passato.
>
>Quindi `getFilledArray('cheese', 3)` crea un array vuoto di 3 elementi e lo riempie con `'cheese'` → `['cheese', 'cheese', 'cheese']`.


In JavaScript funziona perfettamente, ma in TypeScript emerge un problema: 
- **come tipizziamo il valore di ritorno?** 
==Il tipo dell'array dipende dal tipo di `value` — che potrebbe essere `string`, `number`, `boolean`, o qualsiasi altro tipo.== 
Dovremmo scrivere una funzione separata per ogni tipo possibile? No — i generic functions ci salvano:
```ts
function getFilledArray<T>(value: T, n: number): T[] {
  return Array(n).fill(value);
}
```

`etFilledArray<string>` è esattamente equivalente ad aver scritto `(value: string, n: number): string[]` — il generic sostituisce la necessità di duplicare la funzione per ogni tipo.

>[!info] **La differenza tra generic types e generic functions è solo il contesto:** 
>==i primi si applicano ai **type aliases**, i secondi alle **funzioni**. Il meccanismo è identico — un segnaposto `T` che viene sostituito con un tipo concreto al momento dell'uso.==


#### Dimostrazione pratica Generic Functions
Un esempio che mostra come `getFilledArray<T>()` si adatti a qualsiasi tipo — dai primitivi agli object types e alle tuple:
```ts
function getFilledArray<T>(value: T, n: number): T[] {
  return Array(n).fill(value);
}

// T = string
let stringArray: string[];
stringArray = getFilledArray<string>('hi', 6);
// → ['hi', 'hi', 'hi', 'hi', 'hi', 'hi']

// T = number
let numberArray: number[];
numberArray = getFilledArray<number>(9, 6);
// → [9, 9, 9, 9, 9, 9]

// T = object type custom
let personArray: {name: string, age: number}[];
personArray = getFilledArray<{name: string, age: number}>({name: 'J. Dean', age: 24}, 6);
// → [{name: 'J. Dean', age: 24}, ...]

// T = tuple
let coordinateArray: [number, number][];
coordinateArray = getFilledArray<[number, number]>([3, 4], 6);
// → [[3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4]]
```

Notiamo come la stessa funzione gestisca correttamente tutti e quattro i casi — TypeScript verifica a compile time che il tipo passato come `T` sia consistente tra il valore passato e l'array restituito. Senza i generics avremmo dovuto scrivere `getFilledArrayOfStrings`, `getFilledArrayOfNumbers` e così via.