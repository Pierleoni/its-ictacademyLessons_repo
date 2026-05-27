# TypeScript

## Da JavaScript a TypeScript

JavaScript nasce nel **1995** con uno scopo molto preciso e limitato: essere un piccolo linguaggio di scripting per aggiungere interattività semplice alle pagine web nei browser.
Non era pensato per costruire applicazioni complesse — era pensato per far comparire un messaggio di benvenuto o validare un form.

Solo nel **1999** JS diventa tecnicamente capace di supportare le pagine web dinamiche che oggi diamo per scontate, ma l'uso massiccio in quel senso non diventa pratica comune fino al **2005**.

### Il problema: flessibilità vs. scalabilità

Questa origine spiega molto del carattere di JavaScript.
Per il suo caso d'uso originale, fu progettato per essere **flessibile e facile da usare**
— ed è per questo che ancora oggi è considerato uno dei migliori linguaggi per chi inizia.

Il problema emerge quando un progetto cresce: centinaia di file, decine di sviluppatori,
migliaia di righe di codice. In quel contesto, la flessibilità di JS diventa un rischio.

> I linguaggi più "strict" avvisano il developer quando una modifica in un punto del codice ne rompe un altro. **JavaScript non lo fa** — il problema emerge solo a **runtime**, spesso in produzione, spesso nel modo peggiore.

### La soluzione: TypeScript

Per risolvere questi limiti, **Microsoft** sviluppa TypeScript e lo rilascia pubblicamente
nel **2012**. L'idea di fondo è elegante: 
- ==prendere JavaScript così com'è e aggiungerci un **sistema di tipi**.==

>==TypeScript non *sostituisce* JS — lo *estende*.== 
>==Ogni file `.ts` viene alla fine **compilato in JavaScript** normale, quindi gira ovunque giri JS.==

Il **type system** porta tre vantaggi concreti:
- individua **potenziali bug** prima ancora di eseguire il codice
- chiarisce la **struttura** del codice (cosa si aspetta una funzione? cosa restituisce?)
- facilita il **refactoring** in progetti grandi

TypeScript ha anche anticipato il futuro: ha introdotto **arrow functions** e **classi**
*anni prima* che venissero aggiunte ufficialmente allo standard JavaScript.

#### Adozione

Oggi TypeScript è uno dei linguaggi più amati nella community degli sviluppatori.
Lo usano progetti open source come **Angular** e **Webpack**, e aziende come
**Amazon**, **Google** e Codecademy.

### Come funziona TypeScript in pratica

Ora che sappiamo _perché_ esiste TypeScript, vediamo _come si usa_ concretamente.

**Il flusso di lavoro è semplice e si ripete sempre uguale:**

1. ==Prima di tutto si scrive il codice in file con estensione `.ts`.== 
2. **Poi si passa il codice attraverso il transpiler di TypeScript:**
	- ==uno strumento che legge il codice `.ts`, verifica che rispetti le regole del type system, e segnala eventuali errori.== 
3. ==Se il codice è valido, il transpiler produce in output un file `.js` equivalente, pronto per essere eseguito ovunque giri JavaScript.==

> **Transpiler vs Compiler** — un compiler traduce codice in linguaggio macchina, un transpiler traduce da un linguaggio sorgente a un altro. TypeScript → JavaScript è una transpilazione.

### TypeScript è un superset di JavaScript

Questo è un concetto fondamentale: TypeScript **non è un linguaggio separato**, è un _superset_ di JavaScript. 
==Significa che contiene tutto ciò che JS già offre, con funzionalità aggiuntive sopra.==

Una conseguenza pratica e un po' sorprendente: codice JavaScript valido è già, nella maggior parte dei casi, codice TypeScript valido. Prendendo questo esempio:
```ts
let firstName = 'Anders';
```

Il transpiler produce esattamente questo JavaScript:
```js
let firstName = 'Anders';
```

Sono Identici. 
E ha senso — TypeScript non cambia la logica, aggiunge solo **informazioni sui tipi** che aiutano durante lo sviluppo e spariscono in output.

> [!done] Il vero valore di TypeScript non è quindi nella sintassi, ma in ciò che ti permette di _capire_ del tuo codice — ==e soprattutto negli errori che ti permette di **scoprire prima ancora di eseguirlo**.==


### Compilare ed eseguire TypeScript
Passiamo ora ad un caso concreto per capire meglio questi concetti. 
Come abbiamo detto il flusso di lavoro si divide concettualmente in 3 parti ma nel pratico si divide in **due passaggi distinti** che è importante non confondere tra loro.
#### Passaggio 1 
Il primo passaggio è la **compilazione**: 
- ==si lancia `tsc` passandogli il file `.ts`, e il transpiler produce un file `.js` equivalente nella stessa cartella.==
```shell
tsc nomefile.ts
```

#### Passaggio 2 
Il secondo passaggio è l'**esecuzione**: 
- ==il file `.js` generato viene eseguito tramite Node.js, esattamente come qualsiasi altro file JavaScript.==
```shell
node nomefile.js
```


> [!caution] 
> ==`tsc` non esegue il codice — lo _traduce_.== 
> ==È Node.js che lo esegue.== 
> Sono due strumenti con responsabilità separate.


> [!abstract] Più avanti, con un `tsconfig.json` configurato, sarà possibile lanciare `tsc` senza argomenti per compilare l'intero progetto in una volta sola.

>[!info] **Nota:** le versioni recenti di Node.js supportano l'esecuzione diretta di file `.ts` — li transpila al volo in memoria senza creare un `.js` su disco. Comodo durante lo sviluppo, ma in produzione si compila sempre separatamente con `tsc`.

>[!important] **Importante: TypeScript esiste solo a compile time**. 
>Il tipo system, le annotations, e tutti i controlli spariscono completamente nel file `.js` prodotto in output — JavaScript non conosce i tipi e non li applica. Questo significa che un errore segnalato da `tsc` non impedisce l'esecuzione del file `.js` già compilato: il codice gira comunque, ma potenzialmente con comportamenti inaspettati.
> 
> 
> 
> ```ts
> let num: number = 5;
> num = 'Ciao'; // ❌ errore a compile time
> ```
> 
> 
> 
> ```js
> // nel .js compilato:
> let num = 5;
> num = 'Ciao'; // JavaScript non si lamenta — esegue tutto
> ```
> 
> TypeScript è uno strumento per lo **sviluppo**, non per il runtime.



### Type Inference

Come già sappiamo **JavaScript permette di assegnare qualsiasi valore a qualsiasi variabile** — ==massima flessibilità, ma anche fonte di bug e confusione in progetti grandi.==

TypeScript introduce subito un primo meccanismo fondamentale: 
- la **type inference**, ovvero l'**inferenza del tipo**. 
==Quando dichiariamo una variabile con un valore iniziale, TypeScript _deduce automaticamente_ il tipo di quella variabile dal valore assegnato — e da quel momento in poi, quella variabile potrà contenere **solo valori di quel tipo**.==

TypeScript riconosce i tipi primitivi built-in di JavaScript:

- `boolean`
- `number`
- `null`
- `string`
- `undefined`

Se proviamo a riassegnare una variabile con un valore di tipo diverso, TypeScript lo segnala come errore prima ancora di eseguire il codice:
```ts
let order = 'first';
order = 1; // ❌ Type 'number' is not assignable to type 'string'
```

==TypeScript ha inferito che `order` è di tipo `string` dal valore iniziale `'first'`, e non permette di assegnarle un `number`.== 
Per correggere l'errore basta usare un valore del tipo corretto:
```ts
let order = 'first';
order = '1'; // ✅ ok
```

>[!done] ==La type inference è il motivo per cui TypeScript può individuare bug **a compile time** anziché a runtime — senza che lo sviluppatore debba dichiarare esplicitamente il tipo di ogni variabile.==

#### Dimostrazione della type Inferences
Consideriamo questo codice con un bug:
```ts
let aged = true;
let realAge = 0; // TypeScript inferisce: number

if (aged) {
  realAge = '4 years'; // ❌ Type 'string' is not assignable to type 'number'
}

let dogAge = realAge * 7;
console.log(`${dogAge} years`);
```

Eseguendo il `.js` con Node, il programma stampa `NaN years` invece di `28 years` — perché `'4 years' * 7` non è un'operazione numerica valida.

Lanciando invece `tsc index.ts`, il transpiler blocca tutto **prima dell'esecuzione** e segnala esattamente il problema: `realAge` è stato inferito come `number` dal valore iniziale `0`, e non può ricevere una stringa.

La correzione è usare il valore numerico corretto:

```ts
if (aged) {
  realAge = 4; // ✅ number, come atteso
}
// dogAge = 4 * 7 = 28 → "28 years" ✅
```


### Type Shapes
TypeScript non si limita a conoscere il _tipo_ di una variabile — conosce anche la sua **shape**, ovvero la sua _forma_: 
- ==quali proprietà e metodi quella variabile possiede.==

==Ogni tipo primitivo di JavaScript ha proprietà e metodi built-in ben definiti che esistono sempre.== 
Una `string`, ad esempio, avrà sempre `.length` e `.toLowerCase()`:
```ts
"OH".length;        // 2
"MY".toLowerCase(); // "my"
```

TypeScript sfrutta questa conoscenza per individuare un'altra categoria di bug comuni: 
- ==l'accesso a proprietà o metodi che **non esistono** su un tipo.== 
Se proviamo a chiamare un metodo con il nome sbagliato, `tsc` lo intercetta immediatamente:
```ts
"MY".toLowercase();
// ❌ Property 'toLowercase' does not exist on type '"MY"'.
// Did you mean 'toLowerCase'?
```

**Notare il dettaglio:** 
- ==TypeScript non si limita a segnalare l'errore, suggerisce anche la correzione.== 
- ==Questo perché conosce esattamente quali metodi appartengono al tipo `string` e può riconoscere un possibile typo.==

>[!link] **[[#Type Inference|Type inference]] e type shapes lavorano insieme:** 
>==sapere il _tipo_ di una variabile significa automaticamente sapere la sua _forma_ — e quindi poter validare ogni operazione che ci facciamo sopra.==


### Il tipo `any`

**==TypeScript non sempre riesce a inferire il tipo di una variabile.==** 
Il caso più comune è quando una variabile viene **dichiarata senza un valore iniziale** — ==in quel momento TypeScript non ha abbastanza informazioni per dedurre il tipo, e la considera di tipo `any`.==

```ts
let onOrOff;

onOrOff = 1;
onOrOff = false;
```

Una variabile di tipo `any` si comporta esattamente come una variabile JavaScript classica: 
- ==può ricevere qualsiasi valore, e può essere riassegnata a tipi diversi senza che TypeScript sollevi alcun errore.==

> [!info] **`any` è essenzialmente una via d'uscita dal sistema dei tipi** 
>  ==TypeScript smette di controllare quella variabile e la lascia fare quello che vuole.== 
>>[!warning]  **Utile in casi particolari, ma va usato con parsimonia:** 
>>==più `any` si usa, meno TypeScript può aiutarci a trovare bug.==
> 


### Type Annotations

Abbiamo visto che senza un valore iniziale TypeScript assegna il tipo `any` a una variabile, rinunciando a proteggerci. 
Le **type annotations** risolvono esattamente questo problema: 
- ==ci permettono di dichiarare esplicitamente il tipo di una variabile _anche senza assegnarle subito un valore_.==

La sintassi è semplice — ==si aggiunge due punti `:` seguito dal tipo subito dopo il nome della variabile==:
```ts
let mustBeAString: string;

mustBeAString = 'Catdog'; // ✅ ok
mustBeAString = 1337;     // ❌ Type 'number' is not assignable to type 'string'
```

In questo modo TypeScript sa fin dalla dichiarazione cosa quella variabile potrà contenere, e si comporta esattamente come se il tipo fosse stato inferito da un valore iniziale.

>[!note] Le type annotations vengono **rimosse automaticamente** durante la compilazione in JavaScript — sono uno strumento puramente per lo sviluppo, non aggiungono overhead al codice in produzione.

##### Riepilogo: inference vs annotation

|Situazione|Meccanismo|Esempio|
|---|---|---|
|Variabile con valore iniziale|Type inference|`let x = 5` → TypeScript inferisce `number`|
|Variabile senza valore iniziale|Type annotation|`let x: number` → dichiariamo noi il tipo|
|Nessuno dei due|`any`|`let x` → nessun controllo|
#### Dimostrazione pratica della Type Annotations
Un caso reale: vogliamo memorizzare un numero di telefono, inclusi formati internazionali con caratteri non numerici come `+`. 
Dichiariamo la variabile con una type annotation esplicita:
```ts
let phoneNumber: string;

if (Math.random() > 0.5) {
  phoneNumber = '+61770102062'; // ✅ string
} else {
  phoneNumber = 7167762323;    // ❌ Type 'number' is not assignable to type 'string'
}
```

Senza la type annotation `: string`, TypeScript avrebbe assegnato `any` alla variabile e non avrebbe segnalato nulla. 
==Dichiarando esplicitamente il tipo, `tsc` intercetta che uno dei due rami assegna un `number` invece di una `string`.==

>[!info] **Da notare:** 
>==il bug viene trovato **sempre**, indipendentemente da quale ramo esegue `Math.random()` a runtime.== 
>TypeScript analizza **tutto il codice staticamente**, non solo il percorso che verrà effettivamente eseguito.

