
# Introduzione - Configurare il compilatore: tsconfig.json
Fino ad ora abbiamo esplorato i concetti fondamentali di TypeScript — [[Lezione 1 - Introduzione a Typescript#Type Inference|type inference]], [[Lezione 1 - Introduzione a Typescript#Type Shapes|type shapes]], [[Lezione 1 - Introduzione a Typescript#Type Annotations|type annotations]], e il [[Lezione 1 - Introduzione a Typescript#Il tipo `any`|tipo `any`]]. 
In tutti gli esempi abbiamo sempre compilato un singolo file alla volta con `tsc nomefile.ts`.

Questo approccio va bene per esercizi piccoli, ma in un progetto reale ci sono decine o centinaia di file `.ts`, e ogni sviluppatore del team potrebbe compilare il codice con opzioni diverse. 
Serve un modo per centralizzare la configurazione del compilatore e applicarla in modo consistente all'intero progetto.

È esattamente a questo che serve il `tsconfig.json` — ==un file di configurazione che vive nella root del progetto e dice a TypeScript come comportarsi.== 
Nelle sezioni successive vedremo nel dettaglio come è strutturato e quali opzioni mette a disposizione.

## Il file `tsconfig.json`
Quindi il `tsconfig.json` risolve questi problemi: 
- è il file di configurazione che dice a TypeScript _come_ comportarsi e _su quali file_ agire — una volta per tutte, per tutti.
Va posizionato nella **root del progetto** e contiene le regole che il compilatore dovrà rispettare. 
Un esempio tipico:
```json
{
  "compilerOptions": {
    "target": "es2017",
    "module": "commonjs",
    "strictNullChecks": true
  },
  "include": ["**/*.ts"]
}
```

Il file si divide in due sezioni principali.

1. La prima è **`compilerOptions`** — ==un oggetto che raccoglie tutte le regole che il compilatore dovrà rispettare.== 
Tra le opzioni più comuni:

- `"target"` → ==definisce la versione di EcmaScript del JavaScript prodotto in output. `"es2017"` significa che il codice compilato sarà compatibile con lo standard 2017.==
- `"module"` → ==specifica la sintassi usata per import/export dei moduli. `"commonjs"` è lo standard di Node.js.==
- `"strictNullChecks"` → ==se `true`, le variabili non possono assumere valore `null` o `undefined` a meno che non sia dichiarato esplicitamente nel loro tipo.== ^8b9382

2. La seconda è **`include`** — definisce su quali file applicare le regole. 
	- ==`["**/*.ts"]` è un glob pattern che significa _tutti i file `.ts` in qualsiasi sottocartella del progetto_.==

> TypeScript ha molte altre opzioni di configurazione disponibili — la lista completa è consultabile nella [documentazione ufficiale](https://www.typescriptlang.org/docs/handbook/compiler-options.html).

### Utilizzo pratico

Una volta presente il `tsconfig.json` nella root, ==non è più necessario specificare i file da compilare manualmente.== 
Basta lanciare:
```shell
tsc
```

==Il compilatore legge la configurazione e applica le regole a tutti i file indicati in `include`.== 

>[!note] Si può ancora usare `tsc nomefile.ts` per compilare un singolo file, ma in quel caso il `tsconfig.json` viene ignorato.


#### Path relativi in `outDir`

Un dettaglio importante da tenere a mente: tutti i path nel `tsconfig.json` sono **relativi alla posizione del file stesso**, non alla root del progetto.

Questo significa che se il `tsconfig.json` si trova dentro una sottocartella come `src/`, scrivere `"outDir": "dist"` creerà la cartella `dist/` _dentro_ `src/` — probabilmente non quello che vogliamo.

Per puntare a una cartella fuori da `src/`, si risale di un livello con `../`:
```json
{
  "compilerOptions": {
    "target": "es2017",
    "module": "commonjs",
    "strictNullChecks": true,
    "outDir": "../dist"
  },
  "include": ["app.ts", "utils.ts"]
}
```

In questo caso la struttura risultante sarà:
```css
progetto/
├── dist/
│   ├── app.js
│   └── utils.js
└── src/
    ├── app.ts
    ├── utils.ts
    └── tsconfig.json
```

>[!info] ==Nella pratica, il `tsconfig.json` viene quasi sempre messo nella **root del progetto** proprio per evitare questa complessità nei path.== 
>In quel caso `"outDir": "dist"` funziona esattamente come ci si aspetta.


> [!faq] **Perché separare i file `.js` in una cartella dedicata?**
> **Come abbiamo visto quando un progetto cresce, per ogni file `.ts` il compilatore produce un file `.js` omonimo.** 
> ==Tenere entrambi nella stessa cartella significa raddoppiare il numero di file — rendendo il progetto confusionario e difficile da navigare.==
>
>La convenzione più diffusa è: 
>- ==tenere tutto il codice sorgente TypeScript in una cartella `src/` e configurare `outDir` per mandare i file compilati in una cartella `dist/` separata.== 
>Il risultato è una struttura pulita e con responsabilità chiare:
>```css
>progetto/
>├── src/        ← codice sorgente: si lavora qui
>│   ├── app.ts
>│   └── utils.ts
>├── dist/       ← codice compilato: non si tocca mai direttamente
>│   ├── app.js
>│   └── utils.js
>└── tsconfig.json
>```
>
>>[!remember] **`dist/` è quello che viene effettivamente eseguito o distribuito.** 
>>`src/` è quello che viene versionato e mantenuto dagli sviluppatori. Questa separazione è uno dei pattern più comuni in qualsiasi progetto TypeScript reale.
