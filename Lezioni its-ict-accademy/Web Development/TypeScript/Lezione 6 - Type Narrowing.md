# Type Narrowing — Approfondimento

Nelle lezioni precedenti abbiamo incontrato il **[[Lezione 5 - Union Type#Type Narrowing|type narrowing]]** nel contesto delle [[Lezione 5 - Union Type#Definire le Union Types|union]]— quando una variabile può essere `string | number`, abbiamo visto come usare `typeof` come [[Lezione 5 - Union Type#^typeguard|type guard]] per restringere il tipo a uno specifico all'interno di un blocco condizionale.

Ora approfondiamo questo concetto perché è più potente di quanto sembri.

Fino ad ora abbiamo detto che TypeScript lavora a **compile time** — ==analizza il codice, verifica i tipi, e segnala gli errori prima dell'esecuzione.== 
Ma il type narrowing dimostra che TypeScript fa qualcosa di più sofisticato:
- ==è in grado di **simulare il comportamento del codice a runtime** e usare quella simulazione per inferire tipi più specifici in punti precisi del codice.==
```ts
function formatDate(date: string | number) {
  // qui date è string | number

  if (typeof date === 'string') {
    // qui TypeScript sa con certezza che date è string
    // e permette di usare tutti i metodi di string
  }
}
```

TypeScript legge il type guard `typeof date === 'string'` e ragiona così: 
- ==_"se il codice è entrato in questo blocco, allora `date` non può che essere una `string`"_ — e restringe il tipo di conseguenza.==

Nelle sezioni successive vedremo tutti gli strumenti che TypeScript mette a disposizione per fare type narrowing in situazioni sempre più complesse.

## Type Guards

Il modo più comune per fare type narrowing è il **type guard:**
- ==un controllo condizionale che verifica il tipo di una variabile in un punto specifico del codice.== 
Lo strumento principale che abbiamo già visto è `typeof`:
```ts
function formatDate(date: string | number) {
  // qui date è string | number

  if (typeof date === 'string') {
    // qui TypeScript ha ristretto il tipo a string
    return date.toUpperCase(); // ✅ ok — toUpperCase() esiste su string
  }

  // qui TypeScript sa che date non può che essere number
  return date.toFixed(2); // ✅ ok — toFixed() esiste su number
}
```

TypeScript riconosce `typeof` come type guard per questi quattro tipi primitivi:

- `'string'`
- `'number'`
- `'boolean'`
- `'symbol'`

>[!note] **Da notare che `typeof` non copre tutti i tipi di TypeScript — non funziona con object types custom come `User` o `Goose`.** 
>==Per quei casi esistono altri operatori come `instanceof` e `in` che vedremo nelle sezioni successive.==

#### Dimostrazione pratica type guards 
Un esempio concreto che usa due type guards per formattare statistiche sportive in modo diverso in base al tipo:
```ts
function formatStatistic(stat: string | number) {
  // Type guard per number — formattiamo con due decimali
  if (typeof stat === 'number') {
    return stat.toFixed(2);
  }
  // Type guard per string — formattiamo in maiuscolo
  if (typeof stat === 'string') {
    return stat.toUpperCase();
  }
}

console.log(formatStatistic('Win'));  // ✅ Stampa: 'WIN'
console.log(formatStatistic(0.364)); // ✅ Stampa: '0.36'
```

Senza i type guards, TypeScript avrebbe bloccato sia `.toFixed()` che `.toUpperCase()` — ==perché con una union `string | number` non può garantire quale dei due tipi sia in uso in quel momento.== 
I type guards forniscono quella certezza, e TypeScript permette di usare i metodi specifici di ciascun tipo all'interno di ogni blocco.
### Type Guards con `in`

Abbiamo visto che `typeof` funziona per i tipi primitivi. 
Ma quando lavoriamo con object types custom, non possiamo usare `typeof` per distinguerli — restituirebbe semplicemente `'object'` in entrambi i casi. 
Per questi scenari TypeScript riconosce l'operatore `in` come type guard.

L'operatore `in` verifica se una proprietà esiste su un oggetto — e TypeScript lo usa per restringere il tipo:
```ts
type Tennis = {
  serve: () => void;
}

type Soccer = {
  kick: () => void;
}

function play(sport: Tennis | Soccer) {
  if ('serve' in sport) {
    // TypeScript sa che sport è Tennis
    return sport.serve(); // ✅ ok
  }

  if ('kick' in sport) {
    // TypeScript sa che sport è Soccer
    return sport.kick(); // ✅ ok
  }
}
```

La logica è semplice: 
- ==se `'serve'` esiste sull'oggetto, allora non può che essere un `Tennis` — e TypeScript restringe il tipo di conseguenza all'interno del blocco condizionale.== 

>[!difference] **`typeof` vs `in` — quando usare quale:**
> 
> ||`typeof`|`in`|
> |---|---|---|
> |Usato per|tipi primitivi (`string`, `number`, `boolean`, `symbol`)|object types custom|
> |Sintassi|`typeof x === 'string'`|`'proprietà' in oggetto`|
> |Esempio|`typeof date === 'string'`|`'serve' in sport`|

#### Dimostrazione pratica del Type Guards con `in`

Un esempio con due object types custom che hanno metodi diversi — esattamente il caso d'uso ideale per il type guard con `in`:

```ts
type Cat = {
  name: string;
  run: () => string;
}

type Fish = {
  name: string;
  swim: () => string;
}

const siameseCat = {
  name: 'Proxie',
  run: () => 'pitter pat'
}

const bettaFish = {
  name: 'Neptune',
  swim: () => 'bubble blub'
}

function move(pet: Cat | Fish) {
  // Se 'run' esiste su pet → TypeScript sa che è un Cat
  if ('run' in pet) {
    return pet.run(); // ✅ Stampa: 'pitter pat'
  }
  // Se 'swim' esiste su pet → TypeScript sa che è un Fish
  if ('swim' in pet) {
    return pet.swim(); // ✅ Stampa: 'bubble blub'
  }
}

console.log(move(siameseCat)); // 'pitter pat'
console.log(move(bettaFish));  // 'bubble blub'
```

>[!note] **Nota:** 
>entrambi i tipi condividono la proprietà `name` — ma hanno metodi diversi. 
>1. ==`typeof` non avrebbe potuto distinguerli perché entrambi sono oggetti.== 
>2. ==L'operatore `in` invece controlla l'esistenza del metodo specifico e permette a TypeScript di restringere il tipo correttamente.==

### Narrowing con `else`

Finora abbiamo usato due `if` separati per gestire ogni tipo della union. 
TypeScript però è abbastanza intelligente da riconoscere il blocco `else` come **il tipo opposto** del type guard nell'`if` — senza bisogno di un secondo controllo esplicito:
```ts
function formatPadding(padding: string | number) {
  if (typeof padding === 'string') {
    // qui TypeScript sa che padding è string
    return padding.toLowerCase();
  } else {
    // qui TypeScript sa che padding è number
    // perché non può essere string — l'if lo ha già escluso
    return `${padding}px`;
  }
}
```

La logica di TypeScript è semplice ma potente: 
- ==se `padding` è una union `string | number` e il blocco `if` ha già verificato che è una `string`, allora nel blocco `else` non può che essere un `number`.== 
- TypeScript lo inferisce automaticamente senza bisogno di un secondo `typeof`.

>[!remember] Questo funziona in modo affidabile solo quando la union ha **esattamente due tipi**
>==se la union fosse `string | number | boolean`, TypeScript non potrebbe restringere il tipo nell'`else` a un singolo tipo, perché ci sarebbero ancora due possibilità.== 
>**In quel caso servirebbero type guards separati per ogni tipo.**

#### Dimostrazione pratica del narrowing con `else` 
Un esempio che combina il type guard con `in` e il narrowing con `else` — invece di due `if` separati, usiamo un `if/else` più pulito e conciso:
```ts
type Pasta = {
  menuName: string;
  boil: () => string;
}

type Meat = {
  menuName: string;
  panFry: () => string;
}

const fettuccine = {
  menuName: 'Fettuccine',
  boil: () => 'Heat water to 212 degrees',
}

const steak = {
  menuName: 'New York Strip Steak',
  panFry: () => 'Heat oil to 350 degrees',
}

function prepareEntree(entree: Pasta | Meat) {
  if ('boil' in entree) {
    // TypeScript sa che entree è Pasta
    return entree.boil(); // ✅ 'Heat water to 212 degrees'
  } else {
    // TypeScript sa che entree è Meat — perché non è Pasta
    return entree.panFry(); // ✅ 'Heat oil to 350 degrees'
  }
}

console.log(prepareEntree(fettuccine)); // 'Heat water to 212 degrees'
console.log(prepareEntree(steak));      // 'Heat oil to 350 degrees'
```

Entrambi i tipi condividono `menuName` ma hanno metodi diversi — `boil` su `Pasta` e `panFry` su `Meat`. 
==Il type guard con `in` verifica l'esistenza di `boil`, e TypeScript usa quel controllo per restringere il tipo sia nell'`if` che nell'`else`, senza bisogno di un secondo type guard esplicito.==

### Narrowing dopo un Type Guard

TypeScript va ancora oltre il narrowing con `else` — ==è in grado di restringere il tipo anche **dopo** un type guard, senza bisogno di un `else`, a condizione che il blocco `if` contenga un `return` statement==:

```ts
type Tea = {
  steep: () => string;
}

type Coffee = {
  pourOver: () => string;
}

function brew(beverage: Coffee | Tea) {
  if ('steep' in beverage) {
    return beverage.steep(); // se siamo qui, beverage è Tea — e usciamo dalla funzione
  }

  // qui TypeScript sa che beverage è Coffee
  // perché se fosse stato Tea, la funzione sarebbe già uscita con il return
  return beverage.pourOver(); // ✅ ok
}
```


#### Dimostrazione pratica sul Narrowing dopo un TypeGuard

Un esempio che usa l'early return per gestire il tipo `Metal` prima di procedere con il tipo `Glass`:

```ts
type Metal = {
  magnetize: () => string;
}

type Glass = {
  melt: () => string;
}

const iron = {
  magnetize: () => 'Electromagnet activated'
}

const bottle = {
  melt: () => 'Furnace set to 2,700 degrees'
}

function recycle(trash: Metal | Glass) {
  // Se trash è Metal — usciamo subito con il return
  if ('magnetize' in trash) {
    return trash.magnetize(); // ✅ 'Electromagnet activated'
  }

  // qui TypeScript sa che trash è Glass
  // perché se fosse stato Metal, la funzione sarebbe già uscita
  return trash.melt(); // ✅ 'Furnace set to 2,700 degrees'
}

console.log(recycle(iron));   // 'Electromagnet activated'
console.log(recycle(bottle)); // 'Furnace set to 2,700 degrees'
```

Il `return` dentro il type guard è fondamentale — ==è ciò che permette a TypeScript di inferire che il codice successivo appartiene esclusivamente al tipo `Glass`, senza bisogno di un `else` o di un secondo type guard esplicito.==