# Introduzione 

Finora abbiamo visto come TypeScript aggiunge un sistema di tipi alle variabili — attraverso la [[Lezione 1 - Introduzione a Typescript#Type Inference|type inference]] quando un valore iniziale è presente, o le [[Lezione 1 - Introduzione a Typescript#Type Annotations|type annotations]] quando vogliamo [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|dichiarare esplicitamente il tipo senza assegnare subito un valore]]. Abbiamo anche visto come il compilatore sfrutta le [[Lezione 1 - Introduzione a Typescript#Type Shapes|type shapes]] per conoscere proprietà e metodi disponibili su ciascun tipo.

Tutto questo ci ha permesso di rendere il nostro codice più sicuro e prevedibile. Ma fino ad ora abbiamo lavorato solo con variabili isolate — e un programma reale è fatto soprattutto di **funzioni**.

Le funzioni introducono una nuova dimensione al sistema dei tipi: 
- ==non si tratta più solo di dichiarare il tipo di un valore, ma di dichiarare il tipo dei **parametri** che una funzione accetta e il tipo del **valore che restituisce**.== 
Questo permette a TypeScript di verificare non solo che le variabili siano usate correttamente, ma che ==le funzioni vengano chiamate con gli argomenti giusti e che il loro output venga usato in modo coerente.==

## Funzioni e Tipi

### Il problema con JavaScript

Abbiamo visto come TypeScript protegga le variabili da assegnazioni di tipo errato. 
Ma c'è un altro contesto in cui i tipi sono fondamentali: le **funzioni**.

In [[Lezione 5; Le funzioni in Javascript#Le funzioni|JavaScript]], **quando dichiariamo una funzione ci aspettiamo che venga chiamata con argomenti di un certo tipo — ma JS non condivide queste aspettative.** 
Una funzione può essere invocata con qualsiasi argomento senza che venga sollevato alcun errore, con conseguenze spesso silenziose e difficili da diagnosticare:
```js
function printLengthOfText(text) {
  console.log(text.length);
}

printLengthOfText(3); // Stampa: undefined
```

**Passare un `number` invece di una `string` non genera un errore:** 
- ==stampa semplicemente `undefined`, perché i numeri non hanno una proprietà `.length`. Il programma continua a girare come se nulla fosse.==

La soluzione JavaScript classica è gestire il problema manualmente con un controllo esplicito del tipo:
```js
function printLengthOfText(text) {
  if (typeof text !== 'string') {
    throw new Error('Argument is not a string!');
  }

  console.log(text.length);
}

printLengthOfText(3); // Error: Argument is not a string!
```

**Funziona, ma è macchinoso** — ==bisogna ricordarsi di aggiungere questi controlli manualmente in ogni funzione, per ogni parametro.== 
**In un progetto grande, questo approccio diventa rapidamente insostenibile.**

> [!done] **TypeScript risolve questo problema alla radice:** 
> ==invece di gestire gli errori di tipo a **runtime**, li intercetta direttamente a **compile time** — prima ancora di eseguire il codice.== 
> Nelle sezioni successive vedremo esattamente come.

#### Dimostrazione pratica
Un esempio concreto con due funzioni che ricevono argomenti del tipo sbagliato:
```js
function printOperations(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Both arguments must be numbers!');
  }
  console.log(a + b, a / b);
}

printOperations('6', '6'); // ❌ Error: Both arguments must be numbers!
```

Il controllo manuale con `typeof` intercetta l'errore a runtime — ma solo perché lo sviluppatore si è ricordato di aggiungerlo. 
Correggendo la chiamata:
```js
printOperations(6, 6); // ✅ Stampa: 12 1
```

Il secondo caso è più insidioso — nessun errore esplicito, solo un comportamento silenziosamente sbagliato:
```js
function exclaim(name, count) {
  for (let i = 0; i < count; i += 1) {
    console.log(`${name}!`);
  }
}

exclaim(6, 'Muriel'); // ❌ Non stampa nulla — count è una stringa
exclaim('Muriel', 6); // ✅ Stampa 'Muriel!' sei volte
```

Passare `'Muriel'` come `count` non genera alcun errore — ==il `for` semplicemente non esegue mai perché `i < 'Muriel'` non è una condizione numerica valida.== 
Il programma va avanti in silenzio come se nulla fosse.

> [!warning] **Questi sono esattamente i bug che TypeScript elimina alla radice** — ==non servono controlli manuali con `typeof`, perché il compilatore verifica i tipi degli argomenti **prima ancora di eseguire il codice**.==

###  Parameter Type Annotations

Abbiamo visto che le [[Lezione 1 - Introduzione a Typescript#Type Annotations|type annotations]] sulle variabili si scrivono con `: tipo` dopo il nome. 
La stessa identica sintassi si applica ai **parametri delle funzioni** — ed è qui che TypeScript inizia davvero a brillare rispetto ai controlli manuali con `typeof` che abbiamo visto prima:
```ts
function greet(name: string) {
  console.log(`Hello, ${name}!`);
}

greet('Katz'); // ✅ Stampa: Hello, Katz!
greet(1337);   // ❌ Argument of type 'number' is not assignable to parameter of type 'string'
```

Dichiarando `: string` dopo il parametro `name`, TypeScript sa che: 
- ==qualsiasi chiamata a `greet()` deve passare una `string` come primo argomento — e lo verifica **a compile time**, senza bisogno di alcun controllo manuale.==

Vale la stessa regola vista per le variabili: 
- ==un parametro **senza type annotation** viene considerato di [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|tipo `any`]], e accetta qualsiasi valore senza protestare:==
```ts
function printKeyValue(key: string, value) {
  console.log(`${key}: ${value}`);
}

printKeyValue('Courage', 1337);   // ✅ Stampa: Courage: 1337
printKeyValue('Mood', 'scared');  // ✅ Stampa: Mood: scared
```

Qui `value` è `any` — ==TypeScript non ha informazioni sul suo tipo e non può proteggerci da un uso scorretto.== 

> [!ticket] **Come per le variabili, è buona pratica annotare sempre i parametri per sfruttare appieno il sistema dei tipi.**
> 

>[!remember] Le parameter type annotations sono il primo strumento concreto con cui TypeScript elimina la necessità dei controlli manuali con `typeof` che abbiamo visto nella sezione precedente.


#### Dimostrazione pratica

Un esempio con due funzioni che collaborano tra loro:
```ts
function triple(value: number) {
  return value * 3;
}

function greetTripled(greeting: string, value: number) {
  console.log(`${greeting}, ${triple(value)}!`);
}

greetTripled('Hiya', 5); // ✅ Stampa: Hiya, 15!
```

Il punto interessante di questo esercizio è che TypeScript ha trovato il bug **prima ancora di eseguire il codice**. La chiamata originale era:
```ts
greetTripled(5, 'Hiya'); // ❌ gli argomenti sono invertiti
```

Senza type annotations, questo errore sarebbe emerso solo a runtime — o peggio, avrebbe prodotto un output silenziosamente sbagliato. Grazie alle annotations su entrambi i parametri, `tsc` ha individuato immediatamente che `5` non è una `string` e `'Hiya'` non è un `number`.

>[!note] **Questo esempio mostra un caso concreto e frequente: gli argomenti invertiti.** 
>È un bug banale da fare e difficile da individuare in una codebase grande — TypeScript lo intercetta in un secondo.


### Optional Parameters

Per default TypeScript ==richiede che tutti i parametri dichiarati vengano sempre forniti alla chiamata==. 
Ma a volte ha senso che un parametro sia facoltativo — come un nome utente che, se non fornito, viene sostituito da un valore di default:
```ts
function greet(name: string) {
  console.log(`Hello, ${name || 'Anonymous'}!`);
}

greet('Anders'); // ✅ Stampa: Hello, Anders!
greet();         // ❌ TypeScript Error: Expected 1 arguments, but got 0.
```

Il codice JavaScript funzionerebbe correttamente — ==quando `name` è `undefined`, `name || 'Anonymous'` restituisce `'Anonymous'`.== 
Ma TypeScript non lo sa e segnala un errore perché il parametro non è stato fornito.

Per indicare a TypeScript che un parametro è **intenzionalmente opzionale**, si aggiunge `?` dopo il suo nome:
```ts
function greet(name?: string) {
  console.log(`Hello, ${name || 'Anonymous'}!`);
}

greet();         // ✅ Stampa: Hello, Anonymous!
greet('Anders'); // ✅ Stampa: Hello, Anders!
```

Il `?` dice a TypeScript che: 
- ==quel parametro può essere `undefined`, e che quindi è lecito non fornirlo.==

>[!info] **Internamente, `name?: string` è equivalente a dichiarare `name: string | undefined`.** 
>==TypeScript tratta i parametri opzionali esattamente come variabili che possono non avere un valore — coerentemente con tutto quello che abbiamo visto finora su `undefined` e [[Lezione 2 - Il tsconfig.json File#^8b9382|`strictNullChecks`]].==

#### Dimostrazione pratica 
```ts
function proclaim(status?: string) {
  console.log(`I'm ${status || 'not ready...'}`);
}

proclaim();          // ✅ Stampa: I'm not ready...
proclaim('ready?');  // ✅ Stampa: I'm ready?
proclaim('ready!');  // ✅ Stampa: I'm ready!
```

Senza il `?` su `status`, TypeScript avrebbe segnalato un errore sulla prima chiamata `proclaim()` — anche se il comportamento a runtime sarebbe stato corretto. 

> [!rembember] ==Il `?` comunica esplicitamente al compilatore che l'assenza di quell'argomento è **intenzionale**, non un dimenticanza.==


### Default Parameters

Nella sezione precedente abbiamo usato `?` per rendere un parametro opzionale, gestendo il valore di default manualmente con `||`. 
TypeScript offre un modo più pulito per ottenere lo stesso risultato: i **default parameters**.

==Assegnando direttamente un valore di default al parametro, TypeScript inferisce automaticamente il tipo da quel valore== — esattamente come fa con le variabili inizializzate:
```ts
function greet(name = 'Anonymous') {
  console.log(`Hello, ${name}!`);
}

greet();          // ✅ Stampa: Hello, Anonymous!
greet('Anders');  // ✅ Stampa: Hello, Anders!
greet(42);        // ❌ Argument of type 'number' is not assignable to parameter of type 'string'
```

**TypeScript inferisce che `name` è di tipo `string` dal valore `'Anonymous'`** — ==e da quel momento accetta solo `string` o `undefined` come argomento.==

> [!NOTE] **Da notare che un parametro con default value non ha bisogno del `?`**
> ==il fatto di avere un valore di default implica già che il parametro è opzionale. Aggiungere `?` sarebbe ridondante.==

> [!example] **Ricapitolando le tre strade per gestire un parametro opzionale:**
> 
> 
>
>
> | Approccio          | Sintassi             | Quando usarlo                                       |
> | ------------------ | -------------------- | --------------------------------------------------- |
> | Controllo manuale  | `name\|\| 'default'` | ==JavaScript puro, nessun controllo sui tipi==      |
> | Optional parameter | `name?: string`      | ==Il parametro può essere assente, nessun default== |
> | Default parameter  | `name = 'Anonymous'` | ==Il parametro può essere assente, con default==    |

#### Dimostrazione pratica

Partiamo dalla versione con optional parameters che abbiamo visto nell'esercizio precedente:
```ts
function proclaim(status?: string, repeat?: number) {
  for (let i = 0; i < repeat || 0; i += 1) {
    console.log(`I'm ${status || 'not ready...'}`);
  }
}
```

E la riscriviamo usando i default parameters — più pulita e leggibile:
```ts
function proclaim(status = 'not ready...', repeat = 1) {
  for (let i = 0; i < repeat; i += 1) {
    console.log(`I'm ${status}`);
  }
}

proclaim();             // ✅ Stampa 1 volta:  I'm not ready...
proclaim('ready?');     // ✅ Stampa 1 volta:  I'm ready?
proclaim('ready!', 3);  // ✅ Stampa 3 volte: I'm ready!
```

**Notiamo tre miglioramenti rispetto alla versione precedente:**

1. Il primo riguarda le **type annotations** — non servono più. 
	- ==TypeScript inferisce `string` da `'not ready...'` e `number` da `1` automaticamente.==

2. Il secondo riguarda i **valori di default nel corpo della funzione** — ==il `|| 0` su `repeat` e il `|| 'not ready...'` su `status` non servono più, perché i valori di default vengono già gestiti nella firma della funzione. Il codice nel corpo diventa più semplice e diretto.==

3. Il terzo riguarda il **`?`** — ==non serve più su nessuno dei due parametri, perché avere un valore di default implica già che sono opzionali.==

>[!abstract] **La logica del `for`:** 
>==il ciclo parte da `i = 0` e incrementa di `1` ad ogni iterazione finché `i < repeat`.== 
>**Con `repeat = 1` di default, senza argomento la funzione stampa esattamente una volta.**


### Inferring Return Types

Finora abbiamo visto come TypeScript inferisce il tipo delle variabili e dei parametri. 
Lo stesso meccanismo si applica anche ai **valori restituiti dalle funzioni**: 
- ==TypeScript analizza il `return` statement e deduce automaticamente il tipo di ritorno.== 

```ts
function createGreeting(name: string) {
  return `Hello, ${name}!`;
}

const myGreeting = createGreeting('Aisle Nevertell');
```

La catena di inferenza funziona così:

1. Il `return` di `createGreeting()` restituisce un template literal → ==TypeScript inferisce che la funzione ritorna una `string`==
2. `createGreeting('Aisle Nevertell')` ==produce quindi un valore di tipo `string`==
3. `myGreeting` viene inizializzata con quel valore → ==TypeScript la inferisce come `string`==

> [!done] **Questo diventa particolarmente utile per individuare bug.**
>  

Se dichiariamo una variabile di un certo tipo e proviamo ad assegnarle il valore di ritorno di una funzione che restituisce un tipo diverso, TypeScript lo intercetta immediatamente:
```ts
function ouncesToCups(ounces: number) {
  return `${ounces / 16} cups`; // restituisce una string
}

const liquidAmount: number = ouncesToCups(3);
// ❌ Type 'string' is not assignable to type 'number'
```

`ouncesToCups()` restituisce una `string` — ==il valore numerico viene concatenato in un template literal — ma `liquidAmount` è dichiarata come `number`.== 
**TypeScript individua l'incongruenza senza che sia necessario eseguire il codice.**

>[!info] **L'inferenza del tipo di ritorno è un altro tassello del sistema che lavora silenziosamente in background**
> senza annotazioni esplicite, TypeScript traccia i tipi attraverso l'intera catena di chiamate e assegnazioni.

#### Dimostrazione pratica Inferring Return Types

Un esempio che mette alla prova la comprensione dell'inferenza del tipo di ritorno. 
L'obiettivo è dichiarare una variabile di tipo `number` **senza usare `:` né scrivere alcun numero nel codice**:
```ts
function getRandomNumber() {
  return Math.random();
}

let myVar = getRandomNumber();
```

La soluzione sfrutta la catena di inferenza che abbiamo visto:

1. `Math.random()` ==restituisce sempre un `number`==
2. `getRandomNumber()` ==restituisce `Math.random()` → TypeScript inferisce che ritorna `number`==
3. `myVar` ==viene inizializzata con il valore di ritorno → TypeScript la inferisce come `number`==

> **Nessun `:`, nessun numero scritto esplicitamente** — ==eppure TypeScript sa perfettamente che `myVar` è di tipo `number`.==


### Explicit Return Types

Abbiamo visto che TypeScript inferisce automaticamente il tipo di ritorno di una funzione. 
==Ma come per le variabili, a volte è preferibile dichiararlo **esplicitamente** — soprattutto quando si lavora in team o su codice scritto da altri, dove la chiarezza è fondamentale.==

La sintassi è la stessa delle type annotations: `: tipo` dopo la parentesi chiusa dei parametri:
```ts
function createGreeting(name?: string): string {
  if (name) {
    return `Hello, ${name}!`;
  }

  return undefined;
  // ❌ Type 'undefined' is not assignable to type 'string'
}
```

==Dichiarando `: string` come tipo di ritorno, TypeScript verifica che **ogni** `return` statement della funzione restituisca effettivamente una `string`.== 
Nel caso sopra, il secondo `return undefined` viola questa regola e viene segnalato come errore.

La stessa sintassi funziona anche con le **arrow functions**, introdotte in ES2015:
```ts
const createArrowGreeting = (name?: string): string => {
  if (name) {
    return `Hello, ${name}!`;
  }

  return undefined;
  // ❌ Type 'undefined' is not assignable to type 'string'
};
```

Il comportamento è identico — TypeScript tratta le explicit return types allo stesso modo indipendentemente dal tipo di funzione.

>[!faq] **Quando conviene usare le explicit return types invece di affidarsi all'inferenza?** 
>>[!done] ==In generale quando la funzione ha **più return statement** con percorsi diversi, o quando si vuole rendere immediatamente chiaro a chi legge il codice cosa si aspetta di ricevere dalla funzione== — senza dover analizzare il corpo per dedurlo.


#### Void Return Type

Abbiamo visto come annotare il tipo di ritorno di funzioni che restituiscono un valore. Ma cosa succede con le funzioni che non restituiscono nulla — come quelle che si limitano a stampare qualcosa in console?

In questi casi il tipo di ritorno è `void` — ==un tipo speciale che indica esplicitamente l'assenza di un valore restituito==:
```ts
function logGreeting(name: string): void {
  console.log(`Hello, ${name}!`);
}
```

Potrebbe sembrare ridondante annotare qualcosa che "non c'è", ma è considerata buona pratica farlo comunque — ==rende immediatamente chiaro a chi legge il codice che la funzione produce un **side effect** (come stampare in console) senza restituire nulla, e che questo è intenzionale.==

>[!caution] **`void` e `undefined` non sono la stessa cosa.** 
>1. ==`undefined` è un valore assente,== 
>2. `void` ==è l'assenza dichiarata di un tipo di ritorno== 
>>[!fail] Siccome comunicano due concetti diversi e non vanno usati in modo intercambiabile.


#### Dimostrazione pratica

```ts
function makeFruitSalad(fruit1: string, fruit2: string): void {
  let salad = fruit1 + fruit2 + fruit2 + fruit1 + fruit2 + fruit1 + fruit1;
  console.log(salad);
}

makeFruitSalad('banana', 'pineapple');
// ✅ Stampa: bananapineapplepineapplebananapineapplebananabanana
```

Il bug originale era dichiarare `: string` come tipo di ritorno — ma la funzione non restituisce nulla, si limita a stampare in console. 
TypeScript lo segnalava come errore perché si aspettava un `return` con una `string` che non arrivava mai. La correzione è sostituire `: string` con `: void`.


### Documenting Functions

TypeScript supporta la sintassi dei commenti JavaScript classica — sia su singola riga con `//` che su più righe con `/* */`. 
Ma in TypeScript è molto comune vedere un terzo stile: i **documentation comments**.

Un documentation comment inizia con `/**` e termina con `*/`, con ogni riga interna che inizia con `*`:
```ts
/**
 * Questo è un documentation comment
 */
```


Vengono posizionati **direttamente sopra la dichiarazione della funzione** e supportano tag speciali per documentare i dettagli:

- `@param` → ==descrive un parametro della funzione==
- `@returns` → ==descrive il valore restituito==
```ts
/**
 * Returns the sum of two numbers.
 *
 * @param x - The first input number
 * @param y - The second input number
 * @returns The sum of `x` and `y`
 */
function getSum(x: number, y: number): number {
  return x + y;
}
```

Il vantaggio pratico è che la maggior parte degli editor, incluso VS Code, legge questi commenti e li mostra come tooltip quando si passa il cursore sul nome della funzione — ==rendendo la documentazione accessibile direttamente durante lo sviluppo, senza dover aprire il file sorgente.==

>[!abstract] **I documentation comments non sono specifici di TypeScript**
>fanno parte dello standard **JSDoc**, usato anche in JavaScript puro. 
> TypeScript li supporta nativamente e li integra con il suo sistema di tipi.
