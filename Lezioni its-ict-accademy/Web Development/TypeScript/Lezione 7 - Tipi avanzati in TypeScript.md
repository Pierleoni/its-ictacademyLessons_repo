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

#### Interfaces e Types

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
| [[Lezione 5 - Union Type#Definire le Union Types\|Union]]   |        | ❌           |
| [[Lezione 4 - Array, Custom Types e Generic#Tuples\|Tuple]] |        | ❌           |

`type` è più versatile — può tipizzare qualsiasi cosa. `interface` può tipizzare **solo oggetti**. Allora perché usare `interface`?

**Proprio perché è più restrittiva:**
- ==in un programma orientato agli oggetti dove si lavora principalmente con oggetti tipizzati, usare `interface` rende il codice più consistente e comunica chiaramente che quel tipo descrive la forma di un oggetto.== 
- ==È un vincolo intenzionale, non una limitazione.==

> Nelle sezioni successive vedremo anche le funzionalità esclusive di `interface` — come l'**extending** — ==che la rendono particolarmente potente nel contesto della programmazione orientata agli oggetti.==

