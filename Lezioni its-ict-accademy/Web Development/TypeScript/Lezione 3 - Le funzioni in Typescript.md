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
