

# Union Types in TypeScript

Nel nostro percorso con TypeScript abbiamo esplorato un ampio spettro di strumenti per tipizzare il codice — dai primitivi come `string` e `number`, agli [[Lezione 4 - Array, Custom Types e Generic#Array in TypeScript|array]] e tuple, fino ai [[Lezione 4 - Array, Custom Types e Generic#Tipi Custom in TypeScript|tipi custom]] come [[Lezione 4 - Array, Custom Types e Generic#Enums|enums]], [[Lezione 4 - Array, Custom Types e Generic#Object Types|object types]], [[Lezione 4 - Array, Custom Types e Generic#Type Aliases|type aliases]] e [[Lezione 4 - Array, Custom Types e Generic#Generic Types|generics]].

Tutti questi strumenti si collocano su un immaginario **asse di specificità**:

- **All'estremo più specifico troviamo tipi come `string` o `number`** — ==TypeScript accetta solo quel preciso tipo e nient'altro==
- All'estremo opposto troviamo [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|`any`]] — ==TypeScript accetta qualsiasi valore, rinunciando completamente alla [[Lezione 4 - Array, Custom Types e Generic#^82fb09|type safety]]==

Nella maggior parte dei casi uno di questi due estremi è sufficiente. 
Ma a volte abbiamo bisogno di qualcosa nel mezzo — un tipo che sia più specifico di `any` ma più flessibile di un singolo tipo primitivo.

> [!example] **Considera questo scenario:**
>  dobbiamo gestire un ID dipendente che potrebbe essere sia una `string` che un `number`. 
>  ==Usare `any` funzionerebbe, ma rinunceremmo a tutti i controlli di TypeScript — un valore `boolean` o un oggetto verrebbero accettati senza protestare, il che non è quello che vogliamo.==
> 
>>[!ticket] La soluzione è la **union** — un modo per combinare più tipi in uno solo, dicendo a TypeScript _"questa variabile può essere questo tipo, oppure quest'altro"_. Nelle sezioni successive vedremo come funziona e quando usarla.

## Definire le Union Types

Per definire una union si usa il carattere `|` tra i tipi che si vogliono combinare — si legge come "oppure":
```ts
let ID: string | number;

ID = 1;     // ✅ ok — è un number
ID = '001'; // ✅ ok — è una string
ID = true;  // ❌ Type Error! boolean non è nella union
```

**`string | number` è più flessibile di un singolo tipo primitivo, ma molto più specifico di `any`** — ==TypeScript continua a proteggerci da qualsiasi valore che non sia né `string` né `number`.==

Le union si possono usare ovunque si definisce un tipo — variabili, parametri, return types. Sono particolarmente utili nei parametri delle funzioni, che spesso devono gestire input di tipo diverso:
```ts
function getMarginLeft(margin: string | number) {
  return {'marginLeft': margin};
}

getMarginLeft(24);    // ✅ ok
getMarginLeft('24px'); // ✅ ok
getMarginLeft(true);  // ❌ Type Error!
```

Le union non si limitano a due tipi — **si possono combinare quanti tipi si vuole:** `string | number | boolean | null`. 
Nelle sezioni successive vedremo come gestire correttamente una variabile union nel corpo di una funzione, dove TypeScript potrebbe non sapere con certezza quale dei tipi si sta usando.


### Type Narrowing

Abbiamo visto che le union ci permettono di accettare più tipi. 
Ma questo introduce una nuova sfida: se una variabile può essere `string | number`, come facciamo a usare metodi specifici di uno dei due tipi senza che TypeScript si lamenti?

La risposta è il **type narrowing:** 
- ==la capacità di TypeScript di dedurre il tipo esatto di una variabile in un determinato punto del codice, restringendo la union a un tipo specifico.==

Lo strumento principale per fare type narrowing è il **[[Lezione 6 - Type Narrowing#Type Guards|type guard]]:** 
- ==un controllo condizionale con `typeof` che TypeScript riconosce e usa per restringere il tipo==:   ^typeguard

```ts
function getMarginLeft(margin: string | number) {
  // qui margin è string | number

  if (typeof margin === 'string') {
    // qui TypeScript sa che margin è string
    return margin.toLowerCase(); // ✅ ok — toLowerCase() esiste su string
  }

  // qui TypeScript sa che margin è number
  return margin + 'px'; // ✅ ok
}
```

**Senza il type guard, TypeScript non permetterebbe di chiamare `.toLowerCase()` su `margin`** — ==perché non può sapere se in quel momento sia una `string` o un `number`, e `.toLowerCase()` non esiste sui `number`==:

```ts
function getMarginLeft(margin: string | number) {
  return margin.toLowerCase();
  // ❌ Type Error! toLowerCase() non esiste su number
}
```

==Il type narrowing non è limitato a `typeof` — TypeScript riconosce diversi pattern come type guards: controlli con `instanceof`, confronti di uguaglianza, e altri.== 
In tutti i casi il principio è lo stesso: 
- ==fornire a TypeScript abbastanza informazioni per restringere il tipo a compile time.==
#### Dimostrazione pratica della type guard

Un esempio concreto che usa due type guards per gestire `string` e `number` in modo diverso all'interno della stessa funzione:
```ts
function formatValue(value: string | number) {
  // Type guard per string — toLowerCase() è disponibile solo su string
  if (typeof value === 'string') {
    console.log(value.toLowerCase());
  }
  // Type guard per number — toFixed() è disponibile solo su number
  if (typeof value === 'number') {
    console.log(value.toFixed(2));
  }
}

formatValue('Hiya'); // ✅ Stampa: 'hiya'
formatValue(42);     // ✅ Stampa: '42.00'
```

Senza i type guards TypeScript non permetterebbe di chiamare né `.toLowerCase()` né `.toFixed()` direttamente su `value`: 
- ==perché con una union `string | number` non può sapere quale dei due tipi sia in uso in quel momento.== 
- ==I type guards forniscono quella certezza a compile time, restringendo il tipo a uno solo all'interno di ogni blocco `if`.==

### Inferred Union Return Types

Abbiamo già visto come TypeScript [[Lezione 3 - Le funzioni in Typescript#Inferring Return Types|inferisca il tipo di ritorno di una funzione analizzando i suoi `return` statements]]. 
Questo meccanismo funziona anche con le union — ==se una funzione può restituire tipi diversi in percorsi diversi, TypeScript inferisce automaticamente il return type come union==:
```ts
function getBook() {
  try {
    return getBookFromServer(); // restituisce Book
  } catch (error) {
    return `Something went wrong: ${error}`; // restituisce string
  }
}
// Return type inferito: Book | string
```


==TypeScript analizza tutti i possibili `return` statements della funzione — in questo caso uno nel blocco `try` e uno nel blocco `catch` — e costruisce la union con tutti i tipi trovati.== 
Non serve scrivere `: Book | string` esplicitamente!

>[!link] Questo si ricollega a quanto abbiamo visto nella lezione sulle funzioni con [[Lezione 3 - Le funzioni in Typescript#Inferring Return Types|l'inferring return types]] — TypeScript traccia i tipi attraverso l'intera funzione, inclusi i blocchi condizionali e i try/catch. 
>==La differenza è che ora invece di inferire un singolo tipo, può inferire una union di tipi quando i percorsi di esecuzione possibili sono più di uno.==

####  Dimostrazione pratica

Un esempio che simula una chiamata a un server che potrebbe fallire — il caso d'uso più comune per i return types union:
```ts
type User = {
  id: number;
  username: string;
};

function createUser() {
  const randomChance = Math.random() >= 0.5;

  if (randomChance) {
    return {id: 1, username: 'nikko'}; // restituisce User
  } else {
    return 'Could not create a user.'; // restituisce string
  }
}

// TypeScript inferisce il return type come User | string
// ma lo dichiariamo esplicitamente per chiarezza
let userData: User | string = createUser();
```

TypeScript inferisce automaticamente che: 
- ==`createUser()` può restituire `User` o `string` — i due tipi corrispondono ai due rami dell'`if`.== 
La variabile `userData` viene quindi dichiarata con la union `User | string` per essere consistente con il return type della funzione.

>[!note] **Da notare:** 
>`Math.random() >= 0.5` introduce casualità a runtime — ma TypeScript non si preoccupa di quale ramo verrà eseguito. 
>==Analizza **entrambi** i percorsi a compile time e costruisce la union con tutti i tipi possibili.== 
>[[Lezione 3 - Le funzioni in Typescript#Inferring Return Types|È lo stesso principio che abbiamo visto con `Math.random()` nell'esercizio sull'inferring return types.]]

### Unions e Array

Le union diventano ancora più potenti quando combinate con gli array. 
Per dichiarare un array che accetta elementi di più tipi si racchiude la union tra parentesi e si aggiunge la notazione `[]`:
```ts
const dateNumber = new Date().getTime(); // number
const dateString = new Date().toString(); // string

const timesList: (string | number)[] = [dateNumber, dateString];

timesList.push('2025-01-01'); // ✅ ok — è una string
timesList.push(1234567890);   // ✅ ok — è un number
timesList.push(true);         // ❌ Type Error! boolean non è nella union
```

==Le parentesi sono **fondamentali** e non vanno mai omesse== — cambiano completamente il significato della type annotation:
```ts
(string | number)[] // ✅ array di elementi che possono essere string O number
string | number[]   // ❌ string OPPURE array di soli number — non è quello che vogliamo
```

Questa distinzione ricorda quella che abbiamo visto con gli [[Lezione 4 - Array, Custom Types e Generic#Multidimensional Arrays|array multidimensionali]] — anche lì le parentesi cambiavano il significato della notazione. 
==In TypeScript le parentesi sono spesso decisive per interpretare correttamente una type annotation complessa.==

#### Dimostrazione pratica Union e Array

Un esempio che combina union array, [[#Type Narrowing|type narrowing]] e `.map()` per formattare una lista di indirizzi e prezzi:
```
function formatListings(listings: (string | number)[]) {
  return listings.map((listing) => {
    // Type guard per string — formattiamo l'indirizzo in maiuscolo
    if (typeof listing === 'string') {
      return listing.toUpperCase();
    }
    // Type guard per number — formattiamo il prezzo come valuta
    if (typeof listing === 'number') {
      return `$${listing.toLocaleString()}`;
    }
  });
}

const result = formatListings([
  '123 Main St',    // string → '123 MAIN ST'
  226800,           // number → '$226,800'
  '580 Broadway Apt 4a', // string → '580 BROADWAY APT 4A'
  337900,           // number → '$337,900'
]);

console.log(result);
// ['123 MAIN ST', '$226,800', '580 BROADWAY APT 4A', '$337,900']
```

Notiamo come i tre concetti visti in questa lezione lavorino insieme: 
1. ==la **[[#Definire le Union Types|union]]** `(string | number)[]` permette all'array di contenere entrambi i tipi,== 
2. ==il **[[#Type Narrowing|type narrowing]]** con `typeof` permette di applicare metodi specifici per ogni tipo,== 
3. ==e l'**[[Lezione 3 - Le funzioni in Typescript#Inferring Return Types|inferenza si occupa del return type]]** della funzione senza bisogno di dichiararlo esplicitamente.==

### Common Key Value Pairs

**Abbiamo visto che le union permettono a una variabile di essere più tipi diversi.** 
Ma questo introduce un nuovo vincolo importante: 
- ==quando usiamo una variabile union, TypeScript permette di accedere **solo a proprietà e metodi condivisi da tutti i tipi della union**.==

Con i primitivi:
```ts
const batteryStatus: boolean | number = false;

batteryStatus.toString(); // ✅ ok — toString() esiste su boolean E number
batteryStatus.toFixed(2); // ❌ Type Error! toFixed() esiste solo su number
```

Lo stesso principio si applica agli object types custom — solo le proprietà presenti in **tutti** i tipi della union sono accessibili:
```ts
type Goose = {
  isPettable: boolean;
  hasFeathers: boolean;
  canThwartAPicnic: boolean;
}

type Moose = {
  isPettable: boolean;
  hasHoofs: boolean;
}

const pettingZooAnimal: Goose | Moose = {isPettable: true};

console.log(pettingZooAnimal.isPettable); // ✅ ok — esiste su Goose E Moose
console.log(pettingZooAnimal.hasHoofs);   // ❌ Type Error! esiste solo su Moose
```

La logica di TypeScript è coerente — se una variabile può essere `Goose` o `Moose`, non può garantire che `.hasHoofs` esista in entrambi i casi. Quindi lo blocca a compile time.

>[!remember] Per accedere a proprietà specifiche di uno solo dei tipi della union bisogna usare il **[[#Type Narrowing|type narrowing]]** che abbiamo visto in precedenza: 
>- ==restringere il tipo con un type guard prima di accedere alla proprietà specifica.==

####  Dimostrazione pratica common key value pairs

Un esempio concreto con due object types che rappresentano eventi social — un like e una condivisione:
```ts
type Like = {
  username: string;
  displayName: string;
};

type Share = {
  username: string;
  displayName: string;
};

function getFriendNameFromEvent(event: Like | Share) {
  return event.displayName || event.username;
}

const newEvent = {
  username: 'vkrauss',
  displayName: 'Veronica Krauss',
};

const friendName = getFriendNameFromEvent(newEvent);
console.log(`You have an update from ${friendName}.`);
// ✅ Stampa: 'You have an update from Veronica Krauss.'
```

Il punto interessante di questo esercizio è l'errore che si ottiene prima della correzione. La versione originale di `Share` non aveva `displayName`:
```ts
type Share = {
  username: string;
  // displayName mancante!
};
```


> [!bug] TypeScript segnalava immediatamente che `event.displayName` non era accessibile sulla union `Like | Share` — perché `displayName` non era una proprietà condivisa da entrambi i tipi. 
> 

>[!done] La soluzione è stata aggiungere `displayName` anche a `Share`, rendendo le due proprietà usate nella funzione comuni a entrambi i tipi.

### Unions con Literal Types

Finora abbiamo usato le union per combinare tipi come `string | number`. 
Ma le union possono anche combinare **valori letterali specifici** — creando un tipo che accetta solo un insieme predefinito di valori esatti.
```ts
type Color = 'green' | 'yellow' | 'red';

function changeLight(color: Color) {
  // ...
}

changeLight('green');  // ✅ ok
changeLight('yellow'); // ✅ ok
changeLight('purple'); // ❌ Type Error! 'purple' non è un Color valido
```

Questo concetto dovrebbe sembrarti familiare — è lo stesso problema che risolvevano gli **[[Lezione 4 - Array, Custom Types e Generic#Enums|enum]]**. 

> [!difference] **La differenza è che:**
> 
> - ==i literal type unions sono più concisi e diretti quando i valori possibili sono pochi e semplici,== 
> - ==mentre gli enum sono preferibili quando i valori hanno un significato semantico più ricco o quando si lavora in team e si vuole un riferimento centralizzato.==
>   
> **Literal type unions vs Enum:**
>
>||Literal Union|Enum|
>|---|---|---|
>|Sintassi|`type Color = 'green' \| 'yellow'`|`enum Color { Green, Yellow }`|
>|Valori|stringhe o numeri esatti|valori con nome e valore numerico/stringa|
>|Quando usarli|pochi valori semplici|molti valori con significato semantico|

#### Dimostrazione pratica delle literal Union

Un esempio concreto che simula gli stati di un download — un caso d'uso classico per i literal type unions:
```ts
type Status = 'idle' | 'downloading' | 'complete';

function downloadStatus(status: Status) {
  if (status === 'idle') {
    console.log('Download');
  }
  if (status === 'downloading') {
    console.log('Downloading...');
  }
  if (status === 'complete') {
    console.log('Your download is complete!');
  }
}

downloadStatus('idle');       // ✅ Stampa: 'Download'
downloadStatus('downloading'); // ✅ Stampa: 'Downloading...'
downloadStatus('complete');    // ✅ Stampa: 'Your download is complete!'
downloadStatus('error');       // ❌ Type Error! 'error' non è un Status valido
```

tre `if` fungono anche da [[#Type Narrowing|type narrowing]] — ==all'interno di ogni blocco TypeScript sa esattamente quale valore letterale ha `status`, e potremmo usarlo per logiche più complesse senza rischi di tipo.==

>[!ticket] **Questo pattern — un literal type union che rappresenta gli stati possibili di un processo — è uno dei più comuni in applicazioni reali.** 
>Lo ritroveremo spesso quando lavoreremo con React e la gestione dello stato.