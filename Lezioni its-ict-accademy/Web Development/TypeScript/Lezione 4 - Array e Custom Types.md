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