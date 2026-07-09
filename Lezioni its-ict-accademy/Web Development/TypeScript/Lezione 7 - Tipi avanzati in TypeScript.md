# Tipi Avanzati in TypeScript

Nel nostro percorso abbiamo costruito una solida base — dai tipi primitivi agli [[Lezione 4 - Array, Custom Types e Generic#Array in TypeScript|array]] e [[Lezione 4 - Array, Custom Types e Generic#Tuples|tuple]], dai [[Lezione 4 - Array, Custom Types e Generic#Tipi Custom in TypeScript|tipi custom]] come [[Lezione 4 - Array, Custom Types e Generic#Enums|enums]] e [[Lezione 4 - Array, Custom Types e Generic#Object Types|object types]], fino alle [[Lezione 5 - Union Type#Definire le Union Types|union]] e al [[Lezione 6 - Type Narrowing#Type Narrowing — Approfondimento|type narrowing]]. Tutti questi strumenti ci hanno permesso di rendere il codice più sicuro e prevedibile.

Ma man mano che i programmi crescono in complessità, emergono nuove sfide. Abbiamo già incontrato le classi nel nostro percorso — ma come si applica il sistema di tipi di TypeScript in un contesto orientato agli oggetti? E cosa succede quando abbiamo bisogno di tipi con proprietà opzionali, o con nomi di proprietà non noti in anticipo?

```ts
class Robot {
  identify(id: number) {
    console.log(`beep! I'm ${id}`);
  }
}
```

Come potremmo usare `Robot` come tipo? E se alcuni robot avessero più funzionalità di altri, o proprietà con nomi variabili?

In questa lezione esploreremo gli strumenti che TypeScript mette a disposizione per rispondere a queste domande: 
1. dalle **interfacce** per descrivere la forma di oggetti e classi, 
2. ai **tipi composti** per combinare più tipi insieme, 
3. fino alle **index signatures** per gestire proprietà con nomi dinamici 
4. e ai **membri opzionali** per rendere i tipi più flessibili.

L'obiettivo è sempre lo stesso: 
- ==rendere il codice più sicuro **senza** imporre restrizioni inutili su come lo scriviamo e organizziamo.==

### Interfaces e Types

Finora abbiamo usato la [[Lezione 4 - Array, Custom Types e Generic#Type Aliases|keyword `type`]] per definire tipi custom. 
TypeScript offre però un secondo strumento per definire tipi di oggetti: la keyword `interface`. Vediamo le due sintassi a confronto:

```ts
// Con type
type Mail = {
  postagePrice: number;
  address: string;
}

// Con interface — stessa cosa, sintassi leggermente diversa
interface Mail {
  postagePrice: number;
  address: string;
}

const catalog: Mail = { postagePrice: 5, address: '123 Main St' };
```

La differenza sintattica è minima:
- ==`interface` non richiede il segno `=` prima dell'oggetto.== 
**Funzionalmente i due `Mail` sono identici:** ==entrambi vengono verificati a compile time.==

La differenza sostanziale è nel **campo di applicazione**:

|                                                             | `type` | `interface` |
| ----------------------------------------------------------- | ------ | ----------- |
| oggetti                                                     | ✅      | ✅           |
| primitivi                                                   | ✅      | ❌           |
| [[Lezione 5 - Union Type#Definire le Union Types\|Union]]   | ✅      | ❌           |
| [[Lezione 4 - Array, Custom Types e Generic#Tuples\|Tuple]] | ✅      | ❌           |

`type` è più versatile — può tipizzare qualsiasi cosa. `interface` può tipizzare **solo oggetti**. Allora perché usare `interface`?

**Proprio perché è più restrittiva:**
- ==in un programma orientato agli oggetti dove si lavora principalmente con oggetti tipizzati, usare `interface` rende il codice più consistente e comunica chiaramente che quel tipo descrive la forma di un oggetto.== 
- ==È un vincolo intenzionale, non una limitazione.==

> Nelle sezioni successive vedremo anche le funzionalità esclusive di `interface` — come l'**extending** — ==che la rendono particolarmente potente nel contesto della programmazione orientata agli oggetti.==

#### Interfaces e Classi con `implements`

Abbiamo detto che `interface`: 
- ==è particolarmente adatta alla programmazione orientata agli oggetti.== 
Il motivo diventa chiaro con la keyword `implements`, che permette di applicare un'interface a una classe:

```ts
interface Robot {
  identify: (id: number) => void;
}

class OneSeries implements Robot {
  identify(id: number) {
    console.log(`beep! I'm ${id.toFixed(2)}.`);
  }

  answerQuestion() {
    console.log('42!');
  }
}
```

==Dichiarando `implements Robot` sulla classe `OneSeries`, TypeScript verifica a compile time che `OneSeries` implementi **tutti** i membri dichiarati nell'interface.== 
In questo caso `OneSeries` deve avere un metodo `.identify()` con la firma corretta — altrimenti TypeScript segnala un errore.

La classe può anche avere metodi e proprietà aggiuntivi — come `.answerQuestion()` — che non fanno parte dell'interface. 
==L'interface definisce un **contratto minimo** che la classe deve rispettare, non un limite massimo.==

>[!link] Questo pattern dovrebbe sembrarti familiare dal tuo percorso con Java: 
>- [[Lezione 10 - Classi astratte e interfaccie#Le interfacce|è esattamente lo stesso concetto delle interfacce in Java.]] 
>==Una classe può implementare un'interface e aggiungere funzionalità extra, ma deve sempre rispettare il contratto definito dall'interface.== 
>>[!note] **La differenza è che in TypeScript il controllo avviene a compile time tramite `tsc`, mentre in Java avviene durante la compilazione con `javac`.**

> [!example] **Analogia con le Interfacce di Java:**
> 
> 
> Le interfacce di TypeScript e quelle di Java sono concettualmente molto simili: 
> - ==entrambe definiscono solo la **firma** dei metodi (nome, parametri, return type) senza implementarne la logica, e le classi che le implementano sono obbligate a rispettare quel contratto.==
> 
> La differenza principale è nel **momento in cui esistono**:
> 
> - **Java** → le interfacce esistono sia a compile time che a **runtime** — ==sono un meccanismo fondamentale per il polimorfismo e permettono l'ereditarietà multipla==
> - **TypeScript** → ==le interfacce esistono **solo a compile time** — come tutto il resto del sistema di tipi, spariscono completamente nel file `.js` prodotto da `tsc`. Sono uno strumento di type checking, non un meccanismo di runtime==
> 
> In entrambi i casi però il contratto è lo stesso: una classe che implementa un'interface **deve** rispettarne la struttura, pena un errore del compilatore.


#### Dimostrazione pratica delle interfacce

Un esempio concreto che simula il filesystem di un sistema operativo — un caso d'uso classico per interface e classi:
```ts
// L'interface definisce il contratto minimo che ogni directory deve rispettare
interface Directory {
  addFile: (name: string) => void;
}

// La classe implementa il contratto e aggiunge funzionalità extra
class DesktopDirectory implements Directory {
  // Metodo richiesto dall'interface
  addFile(name: string) {
    console.log(`Adding file: ${name}`);
  }

  // Metodo aggiuntivo — non richiesto dall'interface
  showPreview(name: string) {
    console.log(`Opening preview of file: ${name}`);
  }
}

const Desktop = new DesktopDirectory();

Desktop.addFile('lesson-notes.txt');    // ✅ 'Adding file: lesson-notes.txt'
Desktop.showPreview('lesson-notes.txt'); // ✅ 'Opening preview of file: lesson-notes.txt'
```

- ==`DesktopDirectory` deve necessariamente implementare `addFile` perché è dichiarato nell'interface `Directory` — TypeScript lo verifica a compile time.== 
- ==Il metodo `showPreview` invece è una funzionalità extra specifica di `DesktopDirectory` che non fa parte del contratto.==

#### Dimostrazione pratica con `type`, `interface` e `class`


Un esempio completo che mostra come `type`, `interface` e `class` lavorano insieme seguendo il paradigma OOP:
```ts
// type → descrive un dato semplice riutilizzabile
type Address = {
    via: string;
    numCivico: string;
    cap: string;
}

// interface → definisce il contratto che la classe deve rispettare
interface Person {
    id: number;
    name: string;
    lastname: string;
    dataNascita: number;
    userName: string;
    address: Address;
    codiceFiscale: string;
    calcoloEta: (num: number) => void;
}

// class → implementa il contratto con la logica concreta
class User implements Person {
    id: number;
    name: string;
    lastname: string;
    dataNascita: number;
    userName: string;
    address: Address;
    codiceFiscale: string;

    constructor(p: Person) {
        this.id = p.id;
        this.name = p.name;
        this.lastname = p.lastname;
        this.dataNascita = p.dataNascita;
        this.userName = p.userName;
        this.address = p.address;
        this.codiceFiscale = p.codiceFiscale;
    }

    calcoloEta(num: number): void {
        const age = num - this.dataNascita;
        console.log(`Ciao, mi chiamo ${this.name} ${this.lastname} e ho ${age} anni`);
    }
}

// oggetto che rispetta il contratto di Person
const myPerson: Person = {
    id: 1,
    name: 'Marco',
    lastname: 'Pierleoni',
    dataNascita: 1998,
    userName: 'pierleoni',
    address: { via: 'Via Roma', numCivico: '1', cap: '00100' },
    codiceFiscale: 'PRLMRC98...',
    calcoloEta: (num: number) => {} // vuota — la logica reale è nella classe
}

// istanza di User
const u: User = new User(myPerson);
u.calcoloEta(2026); // ✅ Stampa: 'Ciao, mi chiamo Marco Pierleoni e ho 28 anni'
```

**Da notare che `calcoloEta` viene dichiarata due volte:** 
1. ==una volta vuota in `myPerson` per soddisfare il contratto dell'interface,== 
2. ==e una volta con la logica reale nella classe `User`.== 
È la classe che contiene il comportamento concreto — ==l'interface si limita a garantire che quel comportamento esista.==

> [!help] **Type, Interface e Class — quando usarli insieme:**
> Nella pratica quotidiana, specialmente in progetti React e React Native, `type` e `interface` vengono spesso usati in modo intercambiabile per tipizzare oggetti. La differenza diventa importante principalmente quando si lavora con classi e OOP.
>
>Il pattern corretto quando si usano tutti e tre insieme è:
>
>- **`type`** → ==per strutture dati semplici e riutilizzabili, come oggetti di supporto che descrivono un dato==
>- **`interface`** → ==per definire il **contratto** che una classe deve rispettare — cosa deve avere, non come lo implementa==
>- **`class`** → ==per implementare il contratto con la logica concreta, dichiarando tutte le proprietà dell'interface e inizializzandole nel costruttore==
>```ts
type Address = { via: string; numCivico: string; cap: string }; // dato semplice
>
>interface Person {          // contratto
>    name: string;
 >   address: Address;
 >   calcoloEta: (num: number) => void;
>}
>
>class User implements Person { // implementazione
>    name: string;
 >   address: Address;
>    constructor(p: Person) {
 >       this.name = p.name;
 >       this.address = p.address;
 >   }
  >  calcoloEta(num: number): void { 
  > 		const age ? num - this.dataNascita;
  > 		console.log(`Ciao, mi chiamo ${this.name} ${this.lastname} e ho ${age} anni`) 
>	  }
>}
>```
>
>```
>Address (type)     → descrive un dato
>Person (interface) → definisce il contratto
>User (class)       → implementa il contratto
>```


### Deep Types

Man mano che i programmi crescono, le strutture dati diventano più complesse — oggetti annidati dentro altri oggetti, metodi che accedono a proprietà profonde. TypeScript permette di descrivere queste strutture con **tipi annidati** di profondità arbitraria.

Considera questa classe che ha un oggetto `about` con un oggetto `general` annidato al suo interno:
```ts
interface Robot {
  about: {
    general: {
      id: number;
      name: string;
    };
  };
  getRobotId: () => string;
}

class OneSeries implements Robot {
  about;

  constructor(props: {general: {id: number; name: string}}) {
    this.about = props;
  }

  getRobotId() {
    return `ID: ${this.about.general.id}`;
  }
}
```

L'interface `Robot` descrive esattamente la struttura annidata: 
- ==`general` è un oggetto tipizzato dentro `about`, che è a sua volta un oggetto tipizzato.== 
- ==TypeScript verifica a compile time che ogni livello di annidamento rispetti i tipi dichiarati.==

>[!link] **I deep types si combinano naturalmente con i [[Lezione 4 - Array, Custom Types e Generic#Type Aliases|type aliases]] che abbiamo visto in precedenza** 
>==invece di annidare le definizioni direttamente nell'interface, si possono estrarre in alias separati per rendere il codice più leggibile==:
>```ts
>type General = {id: number; name: string};
>type About = {general: General};
>
>interface Robot {
  >about: About;
 > getRobotId: () => string;
>}
>```


> [!NOTE] **Nota:** [[#Dimostrazione pratica con `type`, `interface` e `class`|nella dimostrazione pratica della sezione precedente]] abbiamo già usato un deep type senza saperlo — `interface Person` contiene `address` di tipo `Address`, un oggetto annidato dentro un altro oggetto:
>
>
>
>```ts
>interface Person {
 >   address: Address; // ← deep type con alias separato
>}
>```
>
>>[!ticket] La differenza rispetto all'esempio inline è che abbiamo estratto il tipo annidato in un type alias separato — esattamente la best practice suggerita in questa sezione.

####  Dimostrazione pratica

Un esempio che aggiunge un deep type all'interface `Directory` — la proprietà `config` contiene un oggetto `default` annidato con le impostazioni della directory:

```ts
interface Directory {
  addFile: (name: string) => void;
  // deep type — oggetto annidato dentro un altro oggetto
  config: {
    default: {
      encoding: string;
      permissions: string;
    }
  }
}

class DesktopDirectory implements Directory {
  config = {
    default: {
      encoding: 'utf-8',
      permissions: 'drw-rw-rw-',
    }
  }

  addFile(name: string) {
    console.log(`Adding file: ${name}`);
  }

  showPreview(name: string) {
    console.log(`Opening preview of file: ${name}`);
  }
}

const Desktop = new DesktopDirectory();
console.log(Desktop.config);
// ✅ Stampa: { default: { encoding: 'utf-8', permissions: 'drw-rw-rw-' } }
```

==TypeScript verifica a compile time che `config` in `DesktopDirectory` rispetti esattamente la struttura annidata dichiarata nell'interface — `default` deve essere un oggetto con `encoding` e `permissions` di tipo `string`.==


### Composed Types

Man mano che le strutture dati crescono, i deep types annidati diventano difficili da leggere e mantenere. 
Considera questa interface con due livelli di annidamento:
```ts
interface About {
  general: {
    id: number;
    name: string;
    version: {
      versionNumber: number;
    }
  }
}
```

All'aumentare della complessità emergono due problemi:

> [!fail]
> 1. l'interface diventa così annidata da essere difficile da leggere
> 2. non è possibile riutilizzare solo una parte del tipo — ad esempio solo `version` — senza portarsi dietro tutta la struttura

La soluzione è la **composizione di tipi** — ==si definiscono più interface separate e si referenziano l'una dentro l'altra==:

```ts
interface Version {
  versionNumber: number;
}

interface General {
  id: number;
  name: string;
  version: Version; // ← riferimento a Version
}

interface About {
  general: General; // ← riferimento a General
}
```

> [!done] **Il risultato è più leggibile:**
> 
> - ==ogni interface ha un nome significativo==
> - ==e più flessibile== 
> - ==Di conseguenza `Version` e `General` possono essere riutilizzate separatamente in altre parti del codice.==

 **I composed types, quindi, sono la naturale evoluzione dei [[#Deep Types|deep types]] e dei [[Lezione 4 - Array, Custom Types e Generic#Type Aliases|type aliases]] che abbiamo visto in precedenza.** 
 Il principio è lo stesso della **separazione delle responsabilità** in OOP: 
 - ==ogni tipo descrive una cosa sola e le strutture complesse si costruiscono componendo tipi più semplici.==

#### Dimostrazione pratica

Partiamo dalla versione con deep types annidati che abbiamo scritto in precedenza e la refactorizziamo in tipi composti separati:

**Prima — deep type annidato:**
```ts
interface Directory {
  addFile: (name: string) => void;
  config: {
    default: {
      encoding: string;
      permissions: string;
    }
  }
}
```

**Dopo — tipi composti:**
```ts
// Livello 1 — il tipo più interno
interface DefaultConfig {
  encoding: string;
  permissions: string;
}

// Livello 2 — referenzia DefaultConfig
interface Config {
  default: DefaultConfig;
}

// Livello 3 — referenzia Config
interface Directory {
  addFile: (name: string) => void;
  config: Config;
}
```

La struttura si legge dall'interno verso l'esterno:

1. **`DefaultConfig` descrive le impostazioni di base** — ==`encoding` e `permissions`==
2. **`Config` descrive la configurazione** — ==contiene un oggetto `default` di tipo `DefaultConfig`==
3. **`Directory` descrive la directory** — ==contiene `addFile` e un oggetto `config` di tipo `Config`==

La classe rimane invariata — TypeScript verifica a compile time che `config` rispetti la catena di tipi composti:
```ts
class DesktopDirectory implements Directory {
  config = {
    default: {
      encoding: 'utf-8',      // ✅ rispetta DefaultConfig
      permissions: 'drw-rw-rw-', // ✅ rispetta DefaultConfig
    }
  }

  addFile(name: string) {
    console.log(`Adding file: ${name}`);
  }
}

const Desktop = new DesktopDirectory();
console.log(Desktop.config);
// ✅ { default: { encoding: 'utf-8', permissions: 'drw-rw-rw-' } }
```

**Il refactoring da [[#Deep Types|deep types]] a [[#Composed Types|composed types]] non cambia il comportamento del programma — l'output è identico.** 

> [!done] **Cambia solo la leggibilità e la riusabilità del codice:** ==`DefaultConfig` e `Config` ora possono essere usate separatamente in altre parti del progetto.==


### Estendere le interfacce
La composizione di tipi ci permette di referenziare un tipo dentro un altro. 
Ma a volte vogliamo qualcosa di più diretto — ==**copiare** tutti i membri di un tipo in un altro, estendendolo con proprietà aggiuntive.== 
TypeScript permette di farlo con la keyword `extends`:
```ts
interface Shape {
  color: string;
}

interface Square extends Shape {
  sideLength: number;
}

const mySquare: Square = {sideLength: 10, color: 'blue'};
// ✅ Square richiede sia sideLength che color
```

`Square` estende `Shape` — eredita la proprietà `color` e aggiunge `sideLength`. Chiunque usi il tipo `Square` dovrà fornire entrambe le proprietà.

>[!link] **Anche questo concetto dovrebbe sembrarti familiare da Java — [[Lezione 10 - Classi astratte e interfaccie#Ereditarietà multipla tramite interfacce|è lo stesso meccanismo dell'ereditarietà tra interfacce]].** 
>
>>[!difference]  **La differenza è:**
>>- ==che in TypeScript `extends` tra interface è principalmente uno strumento per **organizzare e riutilizzare** i tipi,== 
>>- ==mentre in Java ha implicazioni più profonde sul polimorfismo a runtime.==
> 
> **`extends` vs composizione — quando usare quale:**
> 
> ||`extends`|Composizione|
> |---|---|---|
> |Cosa fa|==copia tutti i membri nel nuovo tipo==|==referenzia un tipo come proprietà==|
> |Relazione|**is-a** — ==Square è una Shape==|**has-a** — ==Directory ha una Config==|
> |Quando usarlo|==tipi con membri in comune==|==tipi annidati con responsabilità diverse==|

####  Dimostrazione pratica

Un esempio che mostra come `extends` permette di costruire tipi più specifici partendo da tipi più generali:

**Prima — senza `extends`:**
```ts
interface Developer {
  code: () => void;
}

// ❌ TypeScript si lamenta — name e hobbies non esistono su Developer
const me: Developer = {
  code: () => console.log('Headphones on. Coffee brewed. Editor open.'),
  name: 'Corrina',
  hobbies: ['Building rockets']
}
```

Dopo — con `extends`:
```ts
// Interface base — proprietà comuni a tutti gli esseri umani
interface Human {
  name: string;
  hobbies: string[];
}

// Developer estende Human — eredita name e hobbies e aggiunge code
interface Developer extends Human {
  code: () => void;
}

// ✅ Developer ora richiede name, hobbies E code
const me: Developer = {
  code: () => console.log('Headphones on. Coffee brewed. Editor open.'),
  name: 'Corrina',
  hobbies: ['Building rockets']
}

me.code(); // ✅ 'Headphones on. Coffee brewed. Editor open.'
```

La relazione è **is-a** — ==un `Developer` è anche un `Human`.== 
Questo significa che `me` rispetta sia il contratto di `Developer` che quello di `Human`:  
- ==TypeScript lo verifica a compile time richiedendo tutte e tre le proprietà.== 

### Index Signatures

Finora abbiamo sempre conosciuto in anticipo i nomi delle proprietà dei nostri tipi. 
Ma a volte — specialmente quando si lavora con [[Lezione 6 - API#API (Application Programming Interface)|API]] esterne — non sappiamo quali saranno i nomi delle proprietà a compile time. Sappiamo solo che tipo avranno le chiavi e che tipo avranno i valori.

Per questi casi TypeScript offre le **index signatures** — ==un modo per dichiarare il tipo di tutte le proprietà di un oggetto senza conoscerne i nomi==:
```ts
interface SolarEclipse {
  [latitude: string]: boolean;
}
```

Questa interface dice a TypeScript: _"questo oggetto può avere qualsiasi numero di proprietà, purché ogni chiave sia una `string` e ogni valore sia un `boolean`"_.
```ts
const eclipse: SolarEclipse = {
  '40.712776': true,
  '41.203323': true,
  '40.417286': false,
}; // ✅ ok

const eclipse2: SolarEclipse = {
  '40.712776': 'yes', // ❌ Type Error! il valore deve essere boolean
};
```


Il nome `latitude` dentro `[latitude: string]` è puramente descrittivo — ==serve solo allo sviluppatore come riferimento leggibile nei messaggi di errore.== 
Potremmo scrivere `[key: string]` o `[propName: string]` con lo stesso risultato.

>[!info] Le index signatures sono particolarmente utili quando si lavora con risposte di [[Lezione 7 - Sistemi REST#Sistemi REST|API REST]] o dati da database — strutture dove le chiavi sono dinamiche ma i valori hanno sempre lo stesso tipo.


#### Dimostrazione pratica index signatures

Un caso d'uso reale — una chiamata a un'API che restituisce un budget suddiviso per categorie. I nomi delle categorie non sono noti a compile time, ma sappiamo che saranno sempre `string` con valori `number`.
Il progetto è diviso in due file:
1. `api.ts` — la chiamata API:
```ts
// Funzione asincrona che restituisce una Promise
export default async function getBudgetAsync(): Promise<any> {
  // Restituisce una Promise che si risolve con i dati del budget
  return new Promise((resolve, _) => {
    resolve({
      'shopping': 150,
      'food': 210,
      'utilities': 100
    });
  });
}
```

2. `index.ts` — il consumatore:
```ts
import getBudgetAsync from './api';

// Le categorie sono dinamiche — non sappiamo quali saranno
// ma sappiamo che ogni chiave è string e ogni valore è number
interface Budget {
  [category: string]: number;
}

async function getBudget() {
  const result: Budget = await getBudgetAsync();
  console.log(result);
}

getBudget();
// ✅ Stampa: { shopping: 150, food: 210, utilities: 100 }
```

Il flusso completo:

1. `getBudgetAsync()`: ==costruisce una `Promise` che si risolve con l'oggetto budget==
2. `await` ==aspetta che la Promise si risolva e assegna il risultato a `result`==
3. L'interface `Budget` ==con l'index signature garantisce che `result` sia un oggetto con chiavi `string` e valori `number`== — **indipendentemente da quante categorie restituisce l'API**

>[!link] Da notare che `getBudgetAsync()` è tipizzata come `Promise<any>`
>==si potrebbe rendere più preciso usando `Promise<Budget>` al posto di [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|`any`]], così TypeScript conoscerebbe il tipo esatto restituito dalla Promise senza bisogno di ridichiararlo in `result`.==

### Optional Type Members

Finora tutte le proprietà delle nostre interface erano obbligatorie — chiunque usasse il tipo doveva fornire tutti i membri. 
**Ma nella pratica è comune avere oggetti con alcune proprietà obbligatorie e altre facoltative.**

Esattamente come per i [[Lezione 3 - Le funzioni in Typescript#Optional Parameters|parametri opzionali delle funzioni]] che abbiamo visto in precedenza, TypeScript usa il `?` per dichiarare un membro opzionale di un'interface:
```ts
interface OptionsType {
  name: string;   // obbligatorio
  size?: string;  // opzionale
}

function listFile(options: OptionsType) {
  let fileName = options.name;

  // size potrebbe essere undefined — controlliamo prima di usarlo
  if (options.size) {
    fileName = `${fileName}: ${options.size}`;
  }

  return fileName;
}

listFile({name: 'readme.txt'});              // ✅ ok — size omesso
listFile({name: 'readme.txt', size: '2kb'}); // ✅ ok — size fornito
```

Da notare il [[Lezione 6 - Type Narrowing#Type Guards|type guard]] su `options.size` — ==poiché il membro è opzionale potrebbe essere `undefined`, quindi TypeScript ci spinge a verificarne l'esistenza prima di usarlo.== 
È lo stesso principio del [[Lezione 2 - Il tsconfig.json File#^8b9382|`strictNullChecks`]] che abbiamo configurato nel `tsconfig.json`.

>[!remember] **I membri opzionali si ritrovano in tutti i contesti che abbiamo visto — non solo nelle interface, ma anche nei [[Lezione 4 - Array, Custom Types e Generic#Type Aliases|type aliases]] e negli [[Lezione 4 - Array, Custom Types e Generic#Object Types|object types]].** 
>==La sintassi `?` è consistente ovunque in TypeScript.==


#### Dimostrazione pratica sui Optional Type Members

Un caso d'uso reale — un sistema di autenticazione dove alcuni utenti hanno nome e cognome, altri solo uno username:
```ts
// firstName e lastName sono opzionali — non tutti gli utenti li hanno
// username è obbligatorio — ogni utente deve averne uno
interface UserNameOptions {
  firstName?: string;
  lastName?: string;
  username: string;
}

function getUserName(options: UserNameOptions) {
  // Se lo user ha sia il nome che il cognome li mostriamo entrambi
  if (options.firstName && options.lastName) {
    return console.log(`${options.firstName} ${options.lastName}`);
  }
  // Altrimenti mostriamo solo lo username
  return console.log(options.username);
}

// Utente con nome e cognome
getUserName({
  firstName: 'Mr.',
  lastName: 'Oshiro',
  username: 'hotelowner304'
}); // ✅ Stampa: 'Mr. Oshiro'

// Utente con solo nome e username — lastName omesso
getUserName({
  firstName: 'Madeline',
  username: 'mountainClimber'
}); // ✅ Stampa: 'mountainClimber'
```

==Il [[Lezione 6 - Type Narrowing#Type Guards|type guard]] su `options.firstName && options.lastName` è necessario perché entrambi sono opzionali — potrebbero essere `undefined`.== 
TypeScript con [[Lezione 2 - Il tsconfig.json File#^8b9382|`strictNullChecks`]] attivo ci spinge a fare questo controllo prima di usare i membri opzionali, esattamente come abbiamo visto con i parametri opzionali delle funzioni.

