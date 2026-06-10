# Introduzione 
Nelle lezioni precedenti abbiamo esplorato [[Lezione 1 - Introduzione a React Native#React Native|cos'è React Native]] e [[Lezione 2 - Le basi di React Native#I tre pilastri dello sviluppo in React Native|i suoi pilastri fondamentali]]: componenti, stato e props. 
Con quella base, sappiamo già costruire schermate e gestire la logica di un'interfaccia mobile. 
Tuttavia, nei progetti moderni — e in particolare in quelli aziendali — si è affermato un approccio diverso per la struttura e la navigazione: **Expo Router**.

Expo Router è: 
- ==un sistema di routing basato sul **file system**, lo stesso principio che sta alla base di framework web come Next.js.== 
L'idea è semplice: 
- ==la struttura delle cartelle e dei file diventa automaticamente la struttura delle route dell'applicazione.== 
Non si definiscono le route in modo programmatico dentro il codice — ci pensa il framework a inferirle dalla posizione dei file.

Questo cambia le carte in tavola rispetto all'approccio classico con `@react-navigation`, dove ogni route veniva dichiarata esplicitamente in un navigator. 
Con Expo Router quel lavoro di configurazione scompare quasi del tutto, a vantaggio di una struttura di progetto più leggibile e prevedibile.

> [!info] Versione di riferimento Questi appunti fanno riferimento a **Expo SDK 55** con `expo-router` v4, che è la versione utilizzata nel progetto `dashboard-mo`.

Nelle sezioni seguenti vedremo come è strutturata la cartella `app/`, come funzionano i file di layout, i navigatori principali e i redirect — gli elementi che insieme formano lo scheletro di qualsiasi progetto Expo Router.

### Le basi di un progetto Expo Router SDK 55
==Il cuore di qualsiasi progetto Expo Router è la cartella `app/`.== 
Questa cartella è speciale: 
- ==expo-router la riconosce automaticamente come la **root del routing** dell'applicazione, e si aspetta che al suo interno ci siano esclusivamente **screen** e **file di layout**.== 
Nient'altro.
```txt
/app              ← root del routing
    index.tsx     ← screen principale
    _layout.tsx   ← layout globale
package.json
```

>[!warning] **Cosa va dentro `app/`** 
>La cartella `app/` non è un posto generico dove mettere codice. 
>==Contiene solo screen (`index.tsx`, `profile.tsx`, ecc.) e file di layout (`_layout.tsx`).== 
>Componenti riutilizzabili, utilities, hook e simili **non appartengono qui**.

#### Perché usare `src/`

Nella pratica, tenere `app/` direttamente nella root del progetto diventa scomodo non appena il progetto cresce:
- ==si vorrebbe affiancarle una cartella `components/`, una `utils/`, magari una `hooks/`, ma tutte finirebbero nella root insieme a `package.json`, `tsconfig.json` e gli altri file di configurazione — disordinato.==

La soluzione standard è wrappare tutto dentro una cartella `src/`, che diventa la **vera root del codice sorgente**:
```txt
/src
    /app
        index.tsx
        _layout.tsx
    /components
    /utils
    /hooks
package.json
tsconfig.json
```

In questo modo `app/` rimane pulita e dedicata al routing, mentre tutto il resto del codice ha il suo posto ordinato sotto `src/`. 
Expo Router rileva automaticamente questa struttura senza configurazioni aggiuntive.

> [!tip] Best practice Usa sempre `src/` come root del codice sorgente. 
> È la convenzione più diffusa nei progetti Expo Router moderni e quella che si usa in un progetto aziendale.


### Index Route

**Ogni progetto Expo Router DEVE avere un file `index.tsx` da qualche parte dentro `app/`.** 
==Questo file rappresenta la **route di ingresso** dell'applicazione — lo screen che viene mostrato al primo avvio.==

> [!ticket] Regola fondamentale: 
> ==Senza un `index.tsx`, il progetto non sa da dove partire. La sua presenza è obbligatoria.==

**Se si vuole che al primo avvio l'app mostri uno screen diverso, si può usare un `<Redirect />`** — ==ma anche in quel caso il file `index.tsx` deve comunque esistere come punto di partenza.== 
Ne parleremo meglio nella sezione sui [[#Navigatori e reindirizzamenti|redirect]].

#### Dove può stare `index.tsx`

**Non è obbligatorio** ==che `index.tsx` si trovi direttamente nella root di `app/`.== 
Grazie alle **cartelle di raggruppamento** — di cui parleremo in dettaglio più avanti — ==può essere annidato anche a più livelli di profondità, e Expo Router lo riconoscerà comunque come route di ingresso.==

**Esempio 1 — index dentro un gruppo:**
```txt
/app
	/(group)
		index.tsx
	_layout.tsx
package.json
```

**Esempio 2 — index annidato in più gruppi:**

```txt
app/
	/(group)
		/(another)
			index.tsx
	_layout.tsx
package.json
```

>[!info] **Cartelle di raggruppamento** 
>==Le cartelle con il nome tra parentesi come `(group)` o `(tabs)` sono invisibili alla URL/route dell'app — servono solo a organizzare i file.== 
>Per questo `index.tsx` dentro `/(group)` viene comunque trattato come la root. Le approfondiremo nella sezione dedicata.

#### Cartelle di raggruppamento

Le cartelle di raggruppamento si creano usando le **parentesi tonde** intorno al nome, e vanno posizionate dentro `app/`. 
La loro caratteristica principale è che sono **invisibili al routing**: 
- ==il loro nome non appare mai nell'URL o nel path dell'app, servono esclusivamente per organizzare i file.==
```txt
/(tabs)        ✅ cartella di raggruppamento
/(myGroup)     ✅ cartella di raggruppamento
/tabs          ❌ NON è un gruppo — diventa una route /tabs
```

>[!difference] **Differenza cruciale** 
>>[!failure] `/products` → ==diventa una route raggiungibile (`/products`)== 
>
>>[!done] `/(products)` → ==è invisibile al routing, serve solo per organizzare i file==

Il minuscolo nel nome non è tecnicamente obbligatorio — `(Tabs)` o `(myGroup)` funzionano ugualmente — ma ==è la **convenzione standard** per tenere i nomi consistenti con il resto delle route==.

>[!FAQ] **Perché usarle?** 
>==Permettono di raggruppare screen correlati (es. tutte le tab, tutte le schermate di autenticazione) senza introdurre un livello di navigazione in più.== 
>>[!remember] Il raggruppamento è puramente organizzativo.
### Navigatori e reindirizzamenti

==Un progetto Expo Router può avere **più file `_layout.tsx`**, uno per ogni livello della struttura.== 
Ogni layout definisce come vengono visualizzate e navigate le schermate che si trovano nella stessa cartella — le sue "schermate adiacenti".
```txt
/app
    /(tabs)
        /(home)
            index.tsx
            more.tsx
            _layout.tsx    ← gestisce home e more
        /products
            index.tsx
            details.tsx
            _layout.tsx    ← gestisce index e details
        _layout.tsx        ← gestisce i gruppi (home) e products
    modal.tsx
    _layout.tsx            ← layout globale
```
Ogni `_layout.tsx` ha un `export default` che può restituire una di queste cose.

#### I tre navigatori principali

1. **Stack** — ==navigazione a pila, ogni screen si impila sul precedente con una freccia "indietro"==: ^752b8b
```tsx
import {Stack} from 'expo-router';
export default function Layout(){
	return <Stack/>;
}
```

2. **Tabs** — ==navigazione a schede, con una tab bar in basso o in alto==: ^8085ac
```tsx
import { Tabs } from 'expo-router';

export default function Layout() {
    return <Tabs />;
}
```
3. **Slot:** ^a43585
	- ==un navigatore "trasparente", senza alcuno stile o chrome aggiunto.== 
	- ==Mostra semplicemente la schermata corrente, utile quando si vuole gestire la navigazione manualmente==:
```
import {Slot} from 'expo-router';
export default function Layout(){
	return <Slot/>;
}
```

>[!deep] **I navigatori non devono stare da soli** 
> È perfettamente valido wrappare un navigatore dentro provider globali, temi, o altri componenti. 
> Il layout globale in `app/_layout.tsx` è il posto tipico dove si mettono cose come un `ThemeProvider` o un context di autenticazione:
>```tsx
> export default function RootLayout() {
  >  return (
 >       <AuthProvider>
 >           <Stack />
 >       </AuthProvider>
 >   );
>}
>```


### Redirect

Un layout può anche restituire un `<Redirect />` invece di un navigatore. 
Questo componente di Expo Router:
- ==reindirizza automaticamente verso un'altra route, utile ad esempio per mandare l'utente non autenticato alla schermata di login:==
```tsx
import {Redirect} from "expo-router";
export default function Layout(){
	return <Redirect href = "home"/>
}
```

>[!warning] **Limite attuale Al momento** 
>==non è possibile usare un `<Redirect />` nel layout della **root** (`app/_layout.tsx`).== 
>>[!info] **È una limitazione nota di Expo Router SDK 55 che potrebbe essere rimossa in versioni future.**

#### Restituire un componente qualsiasi (o nulla)

Tecnicamente un layout può restituire qualsiasi componente React Native, o addirittura nulla. 
In questo caso però **nessuna delle screen figlie sarà raggiungibile** — non verranno renderizzate né navigate
```tsx
import { View, Text } from 'react-native';

export default function Layout() {
    return (
        <View>
            <Text>Nothing to see here!</Text>
        </View>
    );
}
```

>[!danger] Attenzione Restituire un componente arbitrario senza un navigatore o uno `<Slot />` blocca completamente la navigazione verso le screen figlie. Da evitare salvo casi molto specifici.

### Struttura del progetto 
per creare un progetto utlizziamo il comando `npx create-expo-app@latest NomeProgetto --template default@sdk-55` .
La struttura è: 
```txt
src/
    app/
        _layout.tsx ← root layout, setup navigatori e provider globali
        index.tsx  ← screen di ingresso (home)
        explore.tsx   ← eliminabile

    components/
        ui/
            collapsible.tsx  ← componente accordion (expand/collapse)
        app-tabs.tsx         ← tab navigator nativo (iOS/Android)
        app-tabs.web.tsx     ← tab navigator per web
        animated-icon.tsx    ← icona con animazione (iOS/Android)
        animated-icon.web.tsx
        animated-icon.module.css ← stili CSS solo per web
        external-link.tsx    ← link che apre il browser esterno
        hint-row.tsx         ← riga con testo hint/suggerimento
        themed-text.tsx      ← <Text> che rispetta il tema chiaro/scuro
        themed-view.tsx   ← <View> che rispetta il tema chiaro/scuro
        web-badge.tsx    ← badge visibile solo su web

    constants/
        theme.ts  ← colori, font, spacing — i valori del design system

    hooks/
        use-color-scheme.ts      ← rileva tema chiaro/scuro (iOS/Android)
        use-color-scheme.web.ts  ← stessa cosa ma per web
        use-theme.ts             ← restituisce i colori del tema corrente

    global.css  ← stili base globali (usati da NativeWind)
```

>[!hint] Cosa tenere e cosa eliminare 
>Puoi eliminare `explore.tsx` subito. 
>==Tutto il resto è infrastruttura utile — specialmente `themed-text.tsx`, `themed-view.tsx`, `use-theme.ts` e `theme.ts` che formano il tuo **design system di base**.==

#### Costruire una navigazione da zero

Al fine di evitare errori sia a compile-time che, soprattutto, a run-time, dobbiamo eliminare i file obsoleti che il template `default@sdk-55` genera di default ma che non useremo:
```txt
src/app/explore.tsx

src/components/ui/collapsible.tsx
src/components/animated-icon.module.css
src/components/animated-icon.tsx
src/components/animated-icon.web.tsx
src/components/app-tabs.tsx
src/components/app-tabs.web.tsx
src/components/external-link.tsx
src/components/hint-row.tsx
src/components/themed-text.tsx
src/components/themed-view.tsx
src/components/web-badge.tsx

src/hooks/use-color-scheme.ts
src/hooks/use-color-scheme.web.ts
src/hooks/use-theme.ts

src/constants/theme.ts
```

I file da tenere sono solo:
```txt
src/app/_layout.tsx    ← puliscilo dai riferimenti ai componenti eliminati
src/app/index.tsx      ← puliscilo, lascia solo una View con un Text base
src/global.css         ← serve a NativeWind, non toccarlo
```

##### `_layout.tsx`

Il root layout minimale da cui partire:
```tsx
import { Stack } from "expo-router";

import "../global.css";

import React from "react";

import { StatusBar } from "expo-status-bar";

  

export default function RootLayout() {

  return (

    <>

      <StatusBar style="auto" />

      <Stack />

    </>

  );

}
```

`<Stack/>`: 
- ==**dichiara il tipo di navigatore** che gestirà le schermate di quel livello.== 
- In pratica dice a Expo Router: "le schermate in questa cartella si navigano a pila, con la possibilità di tornare indietro". 
- ==Senza di esso non esiste nessuna struttura di navigazione.==

> [!info] `React.Fragment` vs `<>` vs `<View>` Esistono tre modi per wrappare più elementi senza aggiungere un nodo visivo:
> 
> - **`<></>`** — ==Fragment shorthand, il modo moderno e preferito quando non devi passare props==
> - **`<React.Fragment>`** — ==versione esplicita, utile solo se devi passare la prop `key` (caso raro, tipicamente nelle liste)==
> - **`<View>`** — **tecnicamente funziona ma è semanticamente sbagliato in un layout root:** 
> 	- ==aggiunge un nodo reale con implicazioni di stile che possono interferire con `flex`==
> 
>>[!ticket] **Regola pratica**: ==usa sempre `<></>`. Tieni `<React.Fragment key={...}>` in mente solo per le liste.==
>
>> [!tip] `React` non serve più importarlo Da React 17 in poi il JSX transform è automatico — non è più necessario `import React from "react"` nei file che usano solo JSX. Lo trovi ancora in molti esempi online per retrocompatibilità, ma puoi ometterlo.

#### `index.tsx`

Lo screen di ingresso minimale:
```tsx
import { View, Text, StyleSheet } from "react-native";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Index Screen</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 16,
  },
  heading: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
  },
});
```

>[!caution] Import inutilizzati Nel tuo `index.tsx` 
>Hai `Link`, `Pressable` importati ma non usati. 
>TypeScript non blocca il build per questo, ma è buona abitudine tenerlo pulito — rimuovi gli import solo quando li aggiungi davvero.
### Linking tra le schermate
Per navigare tra le diverse schermate possiamo usare il componente `<Link>` di Expo Router:
- **è il corrispettivo mobile del tag `<a>` HTML,** ==ma pensato per la navigazione tra route dell'applicazione.==
```tsx
export default function HomeScreen() {

  return (

    <View style={styles.container}>

      <Text style={styles.heading}>Index Screen</Text>

      <Pressable style={styles.button}>

  

        <Link href="/secondIndex" push>Push To second</Link>

      </Pressable>

    </View>

  );

}
```


>[!info] **`<Link>` dentro `<Pressable>`** 
>Annidare `<Link>` dentro un `<Pressable>` è opzionale: 
>- ==il link funziona anche da solo.== 
>==Si fa quando si vuole applicare uno stile al contenitore del bottone tramite `style={}`, dato che `<Link>` di per sé ha uno styling limitato come elemento testuale.==

`<Link></Link` nelle schermate: 
- ==**è il meccanismo di trigger** che consente all'utente di spostarsi da una schermata all'altra.== 
- ==Sfrutta il navigatore dichiarato dal layout per sapere _come_ effettuare la transizione.==
#### Le props principali

1. **`href`:**
- ==il path della route di destinazione,== 
- **corrispondente alla posizione del file dentro `src/app/`:**
```tsx
// naviga verso src/app/secondIndex.tsx
<Link href="/secondIndex">Vai a Second</Link>

// naviga verso src/app/settings/profile.tsx
<Link href="/settings/profile">Profilo</Link>
```

2. **`push`:** 
- ==forza l'aggiunta della schermata di destinazione in cima allo [[#I tre navigatori principali|Stack]], anche se la route è già presente nello stack.== 
- Senza `push`, il comportamento di default è `replace` — ==la schermata corrente viene sostituita invece di impilata:==
```tsx
// sostituisce la schermata corrente (default)
<Link href="/secondIndex">Vai a Second</Link>

// aggiunge la schermata in cima allo stack (con freccia indietro)
<Link href="/secondIndex" push>Push To second</Link>
```

>[!faq] **Quando usare `push`?** 
>- ==Usa `push` quando vuoi che l'utente possa tornare indietro alla schermata precedente.==
>>[!example]  ad esempio da una lista a un dettaglio. 
>
>- Usa il comportamento default (`replace`) quando non ha senso tornare indietro 
>>[!example] ad esempio dopo un login.

##### Il ruolo dello `<Stack />` nella navigazione

La freccia "indietro" è una funzionalità dello **`<Stack />`**, non di `<Link>`. Lo Stack mantiene una cronologia delle schermate visitate — ogni volta che navighi verso una nuova schermata, quella precedente rimane in memoria. La freccia non fa altro che fare un `pop` — rimuove la schermata corrente e torna a quella sotto.

`<Link>` in questo meccanismo fa solo una cosa: **aggiunge una schermata allo stack**. Il resto — la freccia, l'animazione di transizione, il gesto di swipe per tornare indietro su iOS — è tutto gestito dallo `<Stack />`.

> [!info] `push` vs `replace` rivisitato Ora che è chiaro il ruolo dello Stack, la differenza è più intuitiva:
> 
> - **senza `push`** (default `replace`) → l==a schermata corrente viene **sostituita** nello stack → niente freccia indietro perché non c'è nulla sotto==
> - **con `push`** → ==la schermata viene **aggiunta sopra** a quella corrente → la freccia indietro appare perché sotto c'è ancora la schermata precedente==
> 
> La freccia indietro non dipende da `push` in sé, ma dal fatto che ci sia qualcosa nello stack sotto la schermata corrente.

**Scenario con `replace` (default):**
```txt
// Navighi da Home a Lista (replace)
STACK: [ Lista ]         ← Home è sparita, sostituita

// Navighi da Lista a Dettaglio (replace)
STACK: [ Dettaglio ]     ← Lista è sparita, sostituita

// Risultato: niente freccia indietro in nessuna schermata
```

**Scenario con `push`:**
```txt
// Navighi da Home a Lista (push)
STACK: [ Home, Lista ]         ← Home è ancora lì sotto

// Navighi da Lista a Dettaglio (push)
STACK: [ Home, Lista, Dettaglio ]  ← tutto lo storico è conservato

// Risultato: Dettaglio ha freccia indietro → torna a Lista
//            Lista ha freccia indietro → torna a Home
```

**Scenario misto — il più comune nella pratica:**
```
// L'app si apre su Home (sempre replace, è la root)
STACK: [ Home ]

// Navighi da Home a Lista (push)
STACK: [ Home, Lista ]      ← freccia indietro su Lista ✅

// Navighi da Lista a Dettaglio (push)
STACK: [ Home, Lista, Dettaglio ]  ← freccia indietro su Dettaglio ✅

// L'utente preme indietro su Dettaglio (pop automatico dello Stack)
STACK: [ Home, Lista ]      ← torna a Lista
```

>[!tip] **Caso d'uso reale** 
>- **`replace` si usa tipicamente dopo il login** — ==non vuoi che l'utente prema indietro e torni alla schermata di login dopo essersi autenticato.== 
>- `push` si usa per la navigazione normale — ==lista → dettaglio, home → profilo, ecc.==

#### `useRouter()`
Un altro modo per navigare tra le schermate è il hook `useRouter()` di Expo Router. 
A differenza di `<Link>` che è un componente dichiarativo nel JSX, `useRouter()` è **imperativo** — ==si chiama nel codice TypeScript e si usa tipicamente dentro un `onPress` o dopo una logica asincrona.== 
```tsx
import { Link, useRouter } from "expo-router";
import { View, Text, StyleSheet, Pressable } from "react-native";

export default function HomeScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Index Screen</Text>

      {/* navigazione dichiarativa con <Link> */}
      <Pressable style={styles.button}>
        <Link href="/secondIndex" push>Push To second</Link>
      </Pressable>

      {/* navigazione imperativa con useRouter */}
      <Pressable style={styles.button} onPress={() => router.push("/ThirdIndex")}>
        <Text style={styles.textBtn}>Push to third</Text>
      </Pressable>
    </View>
  );
}
```

##### Metodi di navigazione di `useRouter()`
`useRouter()` restituisce un oggetto `router` con i metodi di navigazione. 
I principali:
```tsx
router.push("/percorso")      // aggiunge la schermata allo stack (= <Link push>)
router.replace("/percorso")   // sostituisce la schermata corrente (= <Link> default)
router.back()                 // torna alla schermata precedente (= freccia indietro)
```


>[!faq] `<Link>` vs `useRouter()` — quando usare quale
>
>- **`<Link>`** → quando la navigazione è diretta e statica, legata a un elemento visivo nel JSX (un bottone, una voce di menu)
>- **`useRouter()`** → quando la navigazione dipende da una logica — ad esempio dopo una chiamata API, una validazione di un form, o una condizione:
>```tsx
> const handleLogin = async () => {
  >const success = await login(email, password);
 > if (success) {
 >   router.replace("/home");  // dopo il login, replace per non tornare indietro
 > }
>}; 
>```

#### `asChild` — Link con componente custom

`asChild` **trasferisce il comportamento di navigazione di `<Link>` direttamente al suo figlio(es: `<Pressable/>`, `<Button/>`, etc.)**. 
Senza `asChild`, `<Link>` e `<Pressable>` sono due elementi separati con responsabilità diverse — `<Pressable>` gestisce il touch, `<Link>` gestisce la navigazione. Con `asChild` il `<Pressable>` diventa lui stesso il link, gestendo entrambe le cose:
```tsx
{/* ❌ senza asChild — due elementi separati */}
<Pressable style={styles.button}>
  <Link href="/secondIndex" push>
    <Text>Push to second</Text>
  </Link>
</Pressable>

{/* ✅ con asChild — un solo elemento */}
<Link href="/fourthIndex" push asChild>
  <Pressable style={styles.button}>
    <Text>Push to fourth</Text>
  </Pressable>
</Link>
```
Con `asChild` il `<Pressable>` diventa un **contenitore puramente stilizzato** — ti dà lo stile del bottone e il feedback visivo al touch, ma la navigazione la gestisce interamente `<Link>`. 
==!!!Non serve `onPress` su `<Pressable>`!!!!==

> [!info] `Pressable` vs `TouchableOpacity` vs `Button`
> 
> - **`Button`** — componente nativo minimale, pochissimo controllo sullo stile. Quasi mai usato in app reali.
> - **`TouchableOpacity`** — il vecchio standard, abbassa l'opacità al touch. Ancora funzionante ma considerato legacy.
> - **`Pressable`** — il componente moderno e raccomandato. Permette di controllare lo stile in base allo stato del press:
>```tsx
> <Pressable style={({ pressed }) => [
  styles.button,
  pressed && styles.buttonPressed
>]}>
>```

Ma attenzione a una distinzione sottile: 
Non è `asChild` da solo che elimina `onPress`. 
È la **combinazione** di `<Link>` + `asChild` insieme:

- ==**`<Link>`** porta la logica di navigazione==
- ==**`asChild`** la trasferisce al figlio (`<Pressable>`)==

Quindi `<Pressable>` riceve automaticamente la navigazione da `<Link>` e non ha bisogno di `onPress` per quello scopo.
```tsx
{/* ✅ Link si occupa della navigazione, Pressable solo dello stile */}
<Link href="/fourthIndex" push asChild>
  <Pressable style={styles.button}>
    <Text>Push to fourth</Text>
  </Pressable>
</Link>
```

>[!warning] `onPress` non sparisce del tutto: 
>==`asChild` elimina la necessità di `onPress` **solo per la navigazione**.== 
>Se hai bisogno di fare qualcos'altro al press — tipo loggare un evento, aggiornare uno stato — puoi comunque affiancarlo:
>```TSX
><Link href="/fourthIndex" push asChild>
>  <Pressable 
>    style={styles.button}
>    onPress={() => console.log("premuto!")}  // ← eseguito IN AGGIUNTA alla navigazione
  >
>    <Text>Push to fourth</Text>
>  </Pressable>
></Link>
>```
>I due non si escludono — `onPress` e la navigazione di `<Link>` coesistono.


### Percorsi e cartelle
Per capire la struttura delle route del nostro progetto possiamo usare il comando:
```shell
npx expo-router-sitemap
```

Che ci restituisce una mappa di tutte le route attualmente registrate:
```shell
/
/fourthIndex
/secondIndex
/thirdIndex
```
Una route per ogni file `.tsx` dentro `src/app/`. 
Ora vediamo come cambia la struttura delle route in base a come organizziamo file e cartelle.
#### File nella root di `app/`

Ogni file direttamente in `src/app/` diventa una route il cui percorso corrisponde al nome del file:
```shell
src/app/thirdIndex.tsx   →   route: /thirdIndex
src/app/secondIndex.tsx  →   route: /secondIndex
```
#### File dentro una cartella

Se spostiamo `thirdIndex.tsx` dentro una cartella `third/`, il percorso diventa `third/thirdIndex` — vengono usati sia il nome della cartella che il nome del file:
```shell
src/app/third/thirdIndex.tsx   →   route: /third/thirdIndex
```

```shell
/
/fourthIndex
/secondIndex
/third/thirdIndex
```

#### Il file `index` è sempre implicito

Se rinominiamo il file `thirdIndex.tsx` in `index.tsx`, il percorso torna a essere semplicemente `/third` — **`index` è sempre invisibile nella route**, rimane solo il nome della cartella padre:
```shell
src/app/third/index.tsx   →   route: /third
```

```shell
/
/fourthIndex
/secondIndex
/third
```

Questo vale a qualsiasi livello di annidamento:
> [!info] Regola generale
> 
> - Il **nome della cartella** diventa il segmento della route
> - Il **nome del file** diventa il segmento successivo, tranne se si chiama `index` — in quel caso è invisibile
> - Di conseguenza, `index.tsx` è sempre lo screen "principale" di una cartella, esattamente come nel web

> [!tip] Convenzione pratica Quando una cartella contiene una sola schermata principale, usa sempre `index.tsx`. 
> Quando contiene più schermate correlate (es. lista + dettaglio), usa nomi espliciti:
>```shell
> src/app/products/index.tsx    →  /products       (lista prodotti)
>src/app/products/details.tsx  →  /products/details (dettaglio prodotto)
>```


### Cartelle di raggruppamento e percorsi

Un altro modo per ottenere lo stesso risultato è usare le [[#Cartelle di raggruppamento|cartelle di raggruppamento]]. Se rinominiamo il file da `index.tsx` a `third.tsx` ma avvolgiamo la cartella tra parentesi, il nome della cartella sparisce dalla route e rimane solo il nome del file:
```shell
src/app/(group)/third.tsx   →   route: /third
```

```shell
/
/fourthIndex
/secondIndex
\third
```

Il risultato è identico ad avere `third/index.tsx` — il percorso è sempre `/third` — ma la logica è diversa: 
- ==qui è il nome della **cartella** ad essere invisibile, non il nome del file.==

> [!info] Il nome dentro le parentesi è arbitrario Il nome che si mette tra parentesi non ha nessun significato speciale per il routing. `(group)`, `(tabs)`, `(auth)`, `(navigazione)` sono tutti equivalenti: 
> - sono solo convenzioni per comunicare l'intenzione organizzativa a chi legge il codice. 
>>[!example] Ad esempio, chiamare una cartella `(tabs)` non attiva automaticamente una tab bar: 
>>==quella è responsabilità del `_layout.tsx` al suo interno.==

#### Quando il nome del gruppo diventa rilevante

Il nome della cartella di raggruppamento diventa importante solo in un caso: 
- quando due schermate in gruppi diversi hanno lo stesso percorso. 
Senza un nome distinto, Expo Router non saprebbe distinguerle:
```shell
src/app/(auth)/profile.tsx      →   /profile
src/app/(settings)/profile.tsx  →   /profile  ← collisione!
```

In questo caso il sitemap segnalerebbe una **route collision**. Il nome del gruppo serve proprio a disambiguare:
```shell
⚠️ Route collision detected: /profile
  - (auth)/profile.tsx
  - (settings)/profile.tsx
```

>[!ticket] Convenzione pratica: 
>Scegli nomi di gruppo che descrivono il **contesto** delle schermate contenute:
>1. `(auth)` ==per le schermate di autenticazione,== 
>2. `(tabs)` ==per le schermate nella tab bar,== 
>3. `(onboarding)` ==per il flusso iniziale.== 
>Rende la struttura del progetto leggibile a colpo d'occhio.

#### A cosa servono davvero le cartelle di raggruppamento

Le cartelle di raggruppamento non sono solo un modo per accorciare i path — risolvono due problemi distinti e fondamentali.

**1. Organizzazione senza inquinare le route**

Puoi raggruppare schermate correlate in cartelle senza che quei nomi appaiano nel path. In un progetto grande con molti moduli:
```css
src/app/
  (auth)/
    login.tsx            →  /login
    register.tsx         →  /register
    forgot-password.tsx  →  /forgot-password
  (dashboard)/
    home.tsx             →  /home
    analytics.tsx        →  /analytics
  (settings)/
    profile.tsx          →  /profile
    notifications.tsx    →  /notifications
```

Senza le parentesi, tutti quei path diventerebbero `/auth/login`, `/dashboard/home`, `/settings/profile` — introducendo un livello di navigazione in più che non hai voluto e che dovresti gestire esplicitamente nei layout.

**2. Layout condivisi per gruppi di schermate**

Questo è il vantaggio più importante. Ogni cartella di raggruppamento può avere il suo `_layout.tsx` che si applica **solo alle schermate del gruppo**, senza influenzare il resto dell'app:
```css
(auth)/
  _layout.tsx      ← layout solo per login/register (es. sfondo diverso, niente tab bar)
  login.tsx
  register.tsx

(dashboard)/
  _layout.tsx      ← layout solo per le schermate autenticate (es. con tab bar)
  home.tsx
  analytics.tsx
```

>[!tip] **Regola pratica:** 
>==Non pensare alle cartelle di raggruppamento come "accorciatori di path" — pensale come **contenitori logici di schermate che condividono lo stesso layout e contesto**.== 
>Il path corto è una conseguenza, non lo scopo principale.

>[!example] Ricapitolando — tre modi per ottenere `/third`
>```css
>src/app/third.tsx    →  /third  (file nella root)
>src/app/third/index.tsx  →  /third  (index implicito)
>src/app/(group)/third.tsx →  /third  (cartella di raggruppamento)
>```
>Stessa route, tre strutture diverse — la scelta dipende da quante schermate ha quel modulo e se condividono un layout.

##### Esercizio — Percorsi annidati

Per consolidare il concetto di cartelle di raggruppamento e percorsi annidati, creiamo una struttura volutamente profonda. Aggiungiamo dentro `src/app/` una serie di cartelle annidate:
```css
src/app/
  (third)/
    (fourth)/
      fifth/
        sixth/
          index.tsx    ←  DeeplyNestedScreen
```

Le prime due cartelle sono di raggruppamento (con le parentesi), le ultime due sono cartelle normali. Il componente dentro `index.tsx`:
```tsx
import { View, Text } from 'react-native';

const DeeplyNestedScreen = () => {
  return (
    <View>
      <Text>DeeplyNestedScreen</Text>
    </View>
  );
}

export default DeeplyNestedScreen;
```

###### Come ricavare il path

Il modo più veloce per ricavare il path corretto è fare **click destro sul file nell'IDE → Copy Relative Path**:
```shell
myProject\src\app\(third)\(fourth)\fifth\sixth\index.tsx
```

Poi si eliminano:

- il nome del progetto (`myProject`)
- la cartella `src`
- le cartelle di raggruppamento (`(third)`, `(fourth)`)
- il nome del file ([[#Il file `index` è sempre implicito|`index.tsx` è sempre implicito]])
Il path risultante è:
```shell
/fifth/sixth
```

>[!faq] **Perché spariscono solo le cartelle di raggruppamento** 
>==Le cartelle normali (`fifth`, `sixth`) contribuiscono al path — sono segmenti reali della route.== 
>Le cartelle di raggruppamento (`(third)`, `(fourth)`) ==sono invisibili al routing — esistono solo per organizzare il codice.==

###### Collegare la schermata dalla Home

Aggiungiamo il link in `src/app/index.tsx`:
```tsx
<Link href='/fifth/sixth' push asChild>
  <Pressable style={styles.button}>
    <Text>Push to the Nasty Deep</Text>
  </Pressable>
</Link>
```

Nonostante la schermata sia fisicamente a quattro livelli di profondità nel filesystem, il path è semplicissimo — `/fifth/sixth` — proprio grazie alle cartelle di raggruppamento che non lasciano traccia nella route.
>[!abstract] **Lezione pratica:** 
>==Puoi organizzare il codice con quanta profondità vuoi usando le cartelle di raggruppamento, senza che la complessità organizzativa si rifletta nella complessità dei path.== 
>==L'utente (e il codice di navigazione) vedono sempre path puliti e brevi.==
### Schermate e file di Layout

Nelle cartelle che abbiamo creato finora non è presente nessun `_layout.tsx` — e va benissimo così. 
**Non è obbligatorio che ogni cartella abbia un proprio layout.**

Quando Expo Router deve renderizzare una schermata, segue una logica di ricerca a risalita:

1. ==Cerca un `_layout.tsx` nella stessa cartella della schermata==
2. ==Se non lo trova, sale di una cartella e cerca di nuovo==
3. ==Continua a salire fino a trovarne uno==
4. ==Il primo layout trovato è quello che governa la schermata==

#### Lo stack di navigazione

Per capire bene il ruolo del layout, è utile visualizzare lo stack di navigazione come una **pila di fogli**:
```txt
Quando apri l'app:
┌─────────────┐
│    Home     │  ← unico foglio nella pila
└─────────────┘

Quando premi "Push to the Nasty Deep":
┌─────────────┐
│DeeplyNested │  ← foglio nuovo aggiunto sopra
├─────────────┤
│    Home     │  ← ancora lì sotto
└─────────────┘
```

Lo `<Stack />` nel root layout è quello che **gestisce questa pila** — sa che sotto c'è Home e mostra la freccia indietro su DeeplyNested perché sa che c'è qualcosa sotto.


#### Aggiungere un layout a `sixth/`

Aggiungiamo un `_layout.tsx` dentro `src/app/(third)/(fourth)/fifth/sixth/`:
```tsx
import { Slot } from 'expo-router';

const Layout = () => {
  return <Slot />;
}

export default Layout;
```
Come abbiamo gia detto in precedenza [[#^a43585|`<Slot />`]] è il navigatore trasparente:
- ==non aggiunge nessuno stile né chrome visivo.== 
**Il risultato è identico a prima:** 
- ==la schermata viene renderizzata normalmente.==
#### Cosa succede senza un navigatore

Ora sostituiamo `<Slot />` con una `<View>` qualsiasi, senza restituire nessun navigatore:
```tsx
import { StyleSheet, Text, View } from 'react-native';

const Layout = () => {
  return (
    <View style={styles.container}>
      <Text>You Sassy!</Text>
    </View>
  );
}

export default Layout;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#8e2a2ab8',
  },
});
```

La `DeeplyNestedScreen` sparisce completamente — ==viene renderizzato solo il testo "You Sassy!" su sfondo rosso.==

Vediamo perché:
```css
Expo Router cerca dove renderizzare DeeplyNested
  │
  ├── trova _layout.tsx in sixth/
  │     └── restituisce solo <View><Text>You Sassy!</Text></View>
  │         ← non c'è nessuno Stack, nessuno Slot, nessun "posto"
  │           dove mettere DeeplyNested
  │
  └── DeeplyNested non viene mai renderizzata ❌
```


Con `<Slot />` invece:
```css
Expo Router cerca dove renderizzare DeeplyNested
  │
  ├── trova _layout.tsx in sixth/
  │     └── restituisce <Slot />
  │         ← Slot è un "segnaposto" che dice:
  │           "la schermata figlia va renderizzata QUI"
  │
  └── DeeplyNested viene renderizzata dentro lo Slot ✅
```

Con `<Stack />`:
```css
Expo Router cerca dove renderizzare DeeplyNested
  │
  ├── trova _layout.tsx in sixth/
  │     └── restituisce <Stack />
  │         ← Stack è come Slot ma in più gestisce
  │           la pila e mostra la freccia indietro
  │
  └── DeeplyNested viene renderizzata dentro lo Stack ✅
      con freccia indietro ✅
```

> [!faq] **Perché sparisce la schermata?** 
> Il layout più vicino alla schermata è quello che vince. 
> Questo layout non restituisce né `<Stack />`, né `<Tabs />`, né `<Slot />` — nessun navigatore che sappia dove renderizzare le schermate figlie. ==Di conseguenza le child screen non vengono mai visualizzate, esattamente come abbiamo visto nella sezione sui [[#I tre navigatori principali|navigatori]].== 
 
> [!tip] **Regola fondamentale** 
> ==Un `_layout.tsx` che non restituisce un navigatore **blocca completamente la visualizzazione delle schermate figlie**.== 
>>[!tip] Se aggiungi un layout, assicurati sempre che contenga almeno uno `<Slot />` — anche se non hai bisogno di nessuno stile particolare.

>[!info] `Slot` vs `Stack` vs nessun navigatore
>```css
>_layout.tsx senza navigatore
>  ├── le schermate figlie non vengono renderizzate  ← problema principale
>  └── niente freccia indietro  ← conseguenza
>
>_layout.tsx con <Slot />
>  ├── le schermate figlie vengono renderizzate  ✅
>  └── niente freccia indietro (Slot è unstyled) ← a volte è il comportamento voluto
>
>_layout.tsx con <Stack />
>  ├── le schermate figlie vengono renderizzate  ✅
>  └── freccia indietro presente                 ✅
>```

###  Perché avere più file di layout

Abbiamo già detto che [[#`_layout.tsx`|Il root `_layout.tsx`]] ==è l'entry point dell'app==, ma da solo ha un limite importante: 
- ==**applica lo stesso layout e lo stesso navigatore a tutte le schermate dell'app**.==

Nella realtà, ==schermate diverse hanno bisogno di layout diversi.==
L'esempio più classico è la distinzione tra schermate autenticate e non autenticate:
```css
root _layout.tsx  →  <Stack />  (governa tutto)
  ├── login.tsx         ← non dovrebbe avere la tab bar
  ├── register.tsx      ← non dovrebbe avere la tab bar
  ├── home.tsx          ← dovrebbe avere la tab bar
  └── profile.tsx       ← dovrebbe avere la tab bar
```

Con un solo root layout non puoi dire "queste schermate hanno la tab bar, queste no" — il layout è uno solo e si applica a tutto. 
Con più layout invece:
```css
root _layout.tsx  →  <Stack />
  ├── (auth)/
  │     _layout.tsx  →  schermata piena, niente tab bar, sfondo dedicato
  │     login.tsx
  │     register.tsx
  │
  └── (app)/
        _layout.tsx  →  <Tabs /> con tab bar in basso
        home.tsx
        profile.tsx
```

Ogni gruppo ha il suo navigatore, il suo stile, i suoi provider:

- **root layout** — ==configurazione globale: `StatusBar`, provider di tema, font==
- **layout intermedi** — ==configurazione specifica per un gruppo di schermate correlate==

####  Cosa può contenere un layout

Il layout è un **componente React normale** — ==il navigatore è solo una parte di quello che può contenere.== 
Puoi inserire logica prima del `return` e altri componenti nel TSX.

**Logica prima del return — es. controllo autenticazione:**
```tsx
import { Slot, Redirect } from 'expo-router';
import { useAuth } from '@/hooks/useAuth';

const Layout = () => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Redirect href="/login" />;  // ← redirect prima ancora di renderizzare
  }

  return <Slot />;
}
```

**Provider che wrappano il navigatore:**
```tsx
import { Stack } from 'expo-router';
import { CartProvider } from '@/context/CartContext';

const Layout = () => {
  return (
    <CartProvider>        {/* ← provider specifico del gruppo */}
      <Stack />           {/* ← navigatore */}
    </CartProvider>
  );
}
```


Componenti aggiuntivi insieme al navigatore — es. banner, header custom:
```tsx
import { Slot } from 'expo-router';
import { View, Text } from 'react-native';

const Layout = () => {
  return (
    <View style={{ flex: 1 }}>
      <View style={{ backgroundColor: 'red', padding: 10 }}>
        <Text>Banner promozionale</Text>   {/* ← componente aggiuntivo */}
      </View>
      <Slot />                             {/* ← navigatore */}
    </View>
  );
}
```

> [!ticket] **L'unica regola** 
> Puoi mettere quello che vuoi, ma il navigatore ([[#^752b8b|`<Stack />`]], [[#^8085ac|`<Tabs />`]], [[#^a43585|`<Slot />`]]) **deve esserci sempre** — ==altrimenti le schermate figlie non vengono renderizzate, come abbiamo visto nella sezione sull'[[#Ordine di esecuzione dei file di `_layout`|ordine di esecuzione]].== 

> [!tip] Pattern più comune nella pratica
> 
> - **root `_layout.tsx`** — ==provider globali + navigatore==
> - **layout intermedi** — ==logica condizionale (autenticazione, permessi) + navigatore specifico per quel gruppo==
> 
> È la struttura che troverai nella maggior parte dei progetti Expo Router reali

> [!link] **Collegamento con le cartelle di raggruppamento** 
> Le [[#Cartelle di raggruppamento|cartelle di raggruppamento]] e i layout intermedi lavorano sempre insieme — le cartelle raggruppano schermate correlate, il layout definisce come quelle schermate si comportano e si presentano, senza introdurre livelli di navigazione in più nel path.
### Ordine di esecuzione dei file di `_layout`
C'è un concetto fondamentale che vale la pena chiarire subito: 
- ==**i file di layout vengono eseguiti dall'esterno verso l'interno**.==

Significa che quando Expo Router deve renderizzare una schermata profondamente annidata, non parte dal layout più vicino — parte dal layout più lontano, cioè dal root, e scende verso il basso fino ad arrivare alla schermata.

Per vederlo in pratica, aggiungiamo un `_layout.tsx` anche nella cartella `fifth/`, inizialmente con solo uno `<Slot />`:
```tsx
import { Slot } from 'expo-router';

const Layout = () => {
  return <Slot />;
}

export default Layout;
```

Come previsto, nessun cambiamento visivo — `<Slot />` è trasparente.

Ora sostituiamo lo `<Slot />` con una `<View>` senza navigatore, con sfondo blu per renderlo evidente:
```tsx
import { StyleSheet, Text, View } from 'react-native';

const Layout = () => {
  return (
    <View style={styles.container}>
      <Text>Intermediate Layout</Text>
    </View>
  );
}

export default Layout;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0e23c4f6',
  },
});
```

Premendo "Push to the Nasty Deep" veniamo bloccati sul layout intermedio — non arriviamo mai a `DeeplyNestedScreen`. 
Questo dimostra l'ordine di esecuzione:
```css
root _layout.tsx          ← 1° eseguito (Stack)
  └── fifth/_layout.tsx   ← 2° eseguito (View senza navigatore) ← bloccati qui ❌
        └── sixth/_layout.tsx   ← mai raggiunto
              └── DeeplyNestedScreen   ← mai raggiunta
```

> [!faq] **Perché ci blocchiamo in `fifth/` e non in `sixth/`?** 
> ==Perché l'esecuzione va dall'esterno verso l'interno== — **`fifth/_layout.tsx` viene eseguito prima di `sixth/_layout.tsx`.** 
> ==Non restituendo un navigatore, non cede mai il controllo al livello successivo, quindi tutto ciò che sta sotto non viene mai raggiunto.==

> [!warning] **Conseguenza pratica** 
> Un layout intermedio senza navigatore non blocca solo le schermate nella sua cartella: 
> - ==blocca **tutto il sottoalbero** sotto di lui, inclusi tutti i layout e le schermate annidate più in profondità.==
> 
> > [!remember] Tienilo sempre a mente quando la tua schermata non viene visualizzata: ==controlla i layout dal root verso il basso, non solo quello più vicino alla schermata.==

#### Ricapitolando

Non importa quale navigatore — `<Stack />`, `<Tabs />`, `<Slot />` — l'importante è ==che **un qualcosa** che sappia dove renderizzare le schermate figlie venga restituito==. 
Se manca, lo stack si blocca lì.
```css
root _layout.tsx         →  <Stack />  ✅ cede il controllo verso il basso
  └── fifth/_layout.tsx  →  <View />   ❌ non cede il controllo → tutto bloccato
        └── sixth/_layout.tsx          ← mai raggiunto
              └── DeeplyNestedScreen   ← mai raggiunta
```

Ogni layout è come una **porta** nel percorso verso la schermata:
- Se una porta non ha un navigatore è come se fosse **murata** — ==non esiste un passaggio verso il livello successivo, indipendentemente da quante porte aperte ci siano dopo di essa.==

> [!warning] **Regola fondamentale** Se anche un solo layout nel percorso dalla root alla schermata non restituisce un navigatore, **tutto il sottoalbero sotto di lui viene bloccato** — non solo la schermata immediata, ma tutti i layout e le schermate annidate più in profondità.
> 
> > [!tip] Quando una schermata non viene visualizzata, controlla i layout **dal root verso il basso**, non solo quello più vicino alla schermata.


### Reindirizzamento da un layout

Un layout può anche restituire un [[#Redirect|`<Redirect />` ]] invece di un navigatore. 
Per vederlo in pratica, ripristiniamo prima il layout intermedio in `fifth/` con uno `<Slot />`:
```tsx
import { Slot } from 'expo-router';

const Layout = () => {
  return <Slot />;
}

export default Layout;
```


Ora modifichiamo il layout in `sixth/` — quello adiacente alla schermata — per restituire un redirect verso `/secondIndex`:
```tsx
import { Redirect } from 'expo-router';

const Layout = () => {
  return <Redirect href="/secondIndex" />;
}

export default Layout;
```
Premendo "Push to the Nasty Deep" non arriviamo più a `DeeplyNestedScreen` — veniamo reindirizzati direttamente a `secondIndex`. 
Vediamo esattamente cosa succede passo per passo:
```css
root _layout.tsx          →  <Stack />   ✅ navigatore, si va avanti
  └── fifth/_layout.tsx   →  <Slot />    ✅ navigatore, si va avanti
        └── sixth/_layout.tsx  →  <Redirect href="/secondIndex" />
                                  ← intercetta la navigazione
                                  ← reindirizza a /secondIndex ↩️
              └── DeeplyNestedScreen  ← mai raggiunta
```

**L'esecuzione procede sempre dall'esterno verso l'interno** — ==il redirect in `sixth/_layout.tsx` viene raggiunto solo perché tutti i layout sopra di lui hanno restituito un navigatore==. 
==Non appena viene eseguito, intercetta la navigazione e la dirige altrove.==

> [!tip] Caso d'uso reale: Il redirect da un layout è il pattern standard per la **protezione delle route**. 
> Se l'utente non è autenticato e prova ad accedere a una schermata protetta, il layout del gruppo intercetta la navigazione e lo rimanda al login:
>```tsx
> import { Slot, Redirect } from 'expo-router';
>import { useAuth } from '@/hooks/useAuth';
>
>const Layout = () => {
>  const { isAuthenticated } = useAuth();
>
>  if (!isAuthenticated) {
>    return <Redirect href="/login" />;
>  }
>
>  return <Slot />;
>}
>```

>[!remember] **Redirect nel root layout** 
>Come accennato nella sezione sui [[#Navigatori e reindirizzamenti|navigatori]], al momento non è possibile usare `<Redirect />` direttamente nel root `_layout.tsx`. 
>==Il redirect funziona correttamente solo nei layout intermedi.==


```tsx
import { Stack } from "expo-router";
import "../global.css";
import React from "react";
import { StatusBar } from "expo-status-bar";

export default function RootLayout() {

  return (

    <>

      <StatusBar style="auto" />

      <Stack />

    </>

  );

}
```

in questo file stiamo restituendo uno stack che è un navigatore, quindi siamo pronti per andare oltre

Nel file di layout successivo stiamo restituendo uno slot che è anche un navigatore, quindi siamo di nuovo pronti per andare oltre.
```tsx
const Layout = () => {

    return <Slot/>

}
```

E infine, nel file di layout adiacente alla schermata che vogliamo visualizzare, veniamo di fatto reindirizzati altrove
```tsx
import React from 'react'

import { Redirect, Slot } from 'expo-router'

import { StyleSheet, Text, View } from 'react-native'

  

const Layout = () => {

  return <Redirect href= '/secondIndex' />

}

  

export default Layout

const styles = StyleSheet.create({

container: {

        flex: 1,

        justifyContent: 'center',

        alignItems: 'center',

        backgroundColor: '#8e2a2ab8',

    },

    txt: {

      alignItems: 'center',

      fontWeight: 'bold'

  

    }

})
```

