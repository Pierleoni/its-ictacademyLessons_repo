# Introduzione 
Fino ad ora abbiamo visto gli [[Lezione 3 - Hooks#Cosa sono gli Hooks|hook]] come lo [[Lezione 3 - Hooks#Lo `useState()`|`useState`]] e lo [[Lezione 4 - useEffect#Lo `useEffect`|`useEffect`]] ora vediamo un altro hook particolarmente utile come lo `useContext`.   

Prima di capire cos'è lo `useContext` e perché è così importante, partiamo da un problema molto comune quando si costruiscono applicazioni React (o React Native) via via più complesse: **il prop drilling**.

### Il problema: il prop drilling

Immaginiamo di avere una struttura di componenti annidati come questa:

```css
App
 └── TabsLayout
      └── GruppiScreen
           └── GroupItem
```


Se `App` possiede [[Lezione 3 - Hooks#Lo `useState()`|uno stato]] (ad esempio una lista di gruppi) e il componente più profondo, `GroupItem`, ha bisogno di quei dati, **senza Context** dovremmo passarli come props attraverso ogni singolo livello intermedio, anche se quei livelli non li utilizzano direttamente:
```jsx
function App() {
  const [groups, setGroups] = useState([]);
  return <TabsLayout groups={groups} setGroups={setGroups} />;
}

function TabsLayout({ groups, setGroups }) {
  // Non uso "groups" qui, ma devo comunque riceverlo per passarlo giù
  return <GruppiScreen groups={groups} setGroups={setGroups} />;
}

function GruppiScreen({ groups, setGroups }) {
  // Non uso "setGroups" qui, ma devo comunque passarlo giù
  return <GroupItem groups={groups} setGroups={setGroups} />;
}

function GroupItem({ groups, setGroups }) {
  // Finalmente uso i dati!
  return <Text>{groups.length} gruppi</Text>;
}
```

Questo pattern si chiama **"prop drilling"**: ==passare dati attraverso componenti intermedi che non li usano, solo per farli arrivare al componente che ne ha realmente bisogno.==

> [!failure] **Problemi del prop drilling**
> 
> - Il codice diventa verboso e ripetitivo
> - I componenti intermedi diventano "consapevoli" di dati che non usano
> - Aggiungere o rimuovere un dato richiede di modificare **ogni componente** della catena
> - Rende il refactoring più complicato e soggetto ad errori



### Cos'è il Context

React mette a disposizione la **Context [[Lezione 6 - API#API (Application Programming Interface)|API]]** per risolvere esattamente questo problema. Il Context permette di: 
- ==**condividere dati tra componenti senza doverli passare manualmente livello per livello**.==

> [!abstract] **Definizione**  
> ==Il Context è un meccanismo che permette a un valore (stato, funzioni, dati) di essere "letto" da qualsiasi componente discendente, indipendentemente da quanto è annidato, senza passare quel valore tramite props.==

Con il Context, l'esempio di prima diventa:
```jsx
// 1. Creiamo il contenitore
const GroupContext = createContext();

// 2. Un Provider "in alto" fornisce i dati
function App() {
  const [groups, setGroups] = useState([]);
  return (
    <GroupContext.Provider value={{ groups, setGroups }}>
      <TabsLayout />
    </GroupContext.Provider>
  );
}

// 3. I componenti intermedi non devono sapere nulla di "groups"
function TabsLayout() {
  return <GruppiScreen />;
}

function GruppiScreen() {
  return <GroupItem />;
}

// 4. GroupItem legge direttamente dal Context, saltando tutti i livelli intermedi
function GroupItem() {
  const { groups } = useContext(GroupContext);
  return <Text>{groups.length} gruppi</Text>;
}
```

> [!info] ==Nota che `TabsLayout` e `GruppiScreen` **non sanno nemmeno che `groups` esiste** — eppure `GroupItem`, molto più in basso nell'albero, riesce ad accedervi direttamente.==
> 


### I 3 passaggi per usare il Context

L'utilizzo del Context in React richiede sempre **3 passaggi fondamentali**: 
1. [[#1. Creare il Context|creazione]], 
2. [[#2. Fornire il Context (Provider)|provisioning]] 
3. [[#3. Consumare il Context|consumo]].

#### 1. Creare il Context

Si usa la funzione `createContext()`, importata da React:
```jsx
import { createContext } from 'react';

const GroupContext = createContext(undefined);
```

>[!note] **Nota sul valore di default**  
>==L'argomento passato a `createContext()` è il valore di default==, ovvero quello che verrà restituito se un componente prova a leggere il context **senza** essere avvolto da un Provider.  
>Spesso si passa `undefined` o `null`, in modo da poter rilevare (e segnalare) l'errore di un uso scorretto del context (vedremo più avanti come).

#### 2. Fornire il Context (Provider)

Il componente `Context.Provider` ==avvolge la parte di albero dei componenti che deve avere accesso ai dati, e riceve un prop `value` che rappresenta il valore condiviso==:
```jsx
function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);

  return (
    <GroupContext.Provider value={{ groups, setGroups }}>
      {children}
    </GroupContext.Provider>
  );
}
```
>[!help] **Perché usare `children`?**  
>==Il pattern `{ children }` permette al `Provider` di avvolgere qualsiasi componente gli venga passato come figlio==, rendendolo riutilizzabile e componibile con altri Provider (vedremo più avanti come annidare più Context contemporaneamente).


#### 3. Consumare il Context

Per **leggere** i dati forniti dal Provider, un componente discendente usa l'hook `useContext`, passandogli il Context creato al [[#1. Creare il Context|punto 1]]:
```jsx
import { useContext } from 'react';

function GroupItem() {
  const { groups } = useContext(GroupContext);
  return <Text>{groups.length} gruppi</Text>;
}
```

==`useContext(GroupContext)` restituisce il valore più recente passato al `value` del `Provider` più vicino sopra di esso nell'albero dei componenti.==

### Il pattern del Custom Hook

Nella pratica, invece di chiamare `useContext(GroupContext)` direttamente in ogni componente, ==è **buona norma** creare un **hook personalizzato** che incapsula questa chiamata==:
```jsx
function useGroups() {
  const context = useContext(GroupContext);

  if (context === undefined) {
    throw new Error('useGroups must be used within a GroupProvider');
  }

  return context;
}
```

>[!done] **Vantaggi di questo pattern**
>
>- ==Evita di dover importare sia `useContext` che il `GroupContext` in ogni file che consuma il context==
>- ==Centralizza il controllo di errore: se un componente chiama `useGroups()` senza essere avvolto da `GroupProvider`, riceve subito un errore chiaro invece di un bug silenzioso più avanti==
>- ==Rende il codice più leggibile: `const { groups } = useGroups();` comunica immediatamente l'intento==

###### Perché il controllo `if (context === undefined)`

Quando creiamo il context con `createContext(undefined)`, ==se un componente prova a leggerlo **senza** essere discendente di un `Provider`, riceverà proprio `undefined` come valore==. 
Quindi Il controllo esplicito trasforma questo comportamento silenzioso in un **errore immediato e comprensibile**:
```jsx
function useGroups() {
  const context = useContext(GroupContext);
  if (context === undefined) {
    throw new Error('useGroups must be used within a GroupProvider');
  }
  return context;
}
```

Questo è particolarmente utile durante lo sviluppo: ==invece di scoprire un bug misterioso quando `groups` risulta `undefined` in un punto lontano del codice, l'errore viene sollevato immediatamente, con un messaggio che indica esattamente cosa è andato storto.==

##### Esempio completo: struttura di un Context in React Native (Expo Router)

Ecco come si presenta tipicamente un file `Context` completo in un progetto [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Introduzione|Expo Router]], che segue tutti e 3 i passaggi visti sopra:

```tsx
// context/GroupContext.tsx
import React, { createContext, useContext, useState, useCallback } from 'react';
import type { ReactNode } from 'react';

// Definizione del tipo di dato
export interface Group {
  id: number;
  name: string;
  members: number[];
}

// Definizione della "forma" del context (dati + funzioni)
interface GroupContextType {
  groups: Group[];
  addGroup: (group: Group) => void;
  deleteGroup: (groupId: number) => void;
}

// 1. Creazione del Context
const GroupContext = createContext<GroupContextType | undefined>(undefined);

// 2. Il Provider
export function GroupProvider({ children }: { children: ReactNode }) {
  const [groups, setGroups] = useState<Group[]>([]);

  const addGroup = useCallback((group: Group) => {
    setGroups((prev) => [...prev, group]);
  }, []);

  const deleteGroup = useCallback((groupId: number) => {
    setGroups((prev) => prev.filter((g) => g.id !== groupId));
  }, []);

  return (
    <GroupContext.Provider value={{ groups, addGroup, deleteGroup }}>
      {children}
    </GroupContext.Provider>
  );
}

// 3. Il custom hook per il consumo
export function useGroups() {
  const context = useContext(GroupContext);
  if (context === undefined) {
    throw new Error('useGroups must be used within a GroupProvider');
  }
  return context;
}
```


###### Come si "monta" il Provider nell'app

Il `Provider` va posizionato **in alto** nell'albero dei componenti, tipicamente nel [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`_layout.tsx`|`_layout.tsx`]] principale (in Expo Router), avvolgendo tutte le screen che devono avere accesso al context:
```tsx
// app/_layout.tsx
import { GroupProvider } from '@/context/GroupContext';
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <GroupProvider>
      <Stack>
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      </Stack>
    </GroupProvider>
  );
}
```

###### Come si consuma il Context in una screen

Da questo momento, **qualsiasi screen o componente figlio**, per quanto profondamente annidato, può accedere ai dati semplicemente chiamando l'[[#Il pattern del Custom Hook|hook custom]]:
```tsx
// app/(tabs)/gruppi.tsx
import { useGroups } from '@/context/GroupContext';

export default function GruppiScreen() {
  const { groups, addGroup, deleteGroup } = useGroups();

  return (
    // ... JSX che usa groups, addGroup, deleteGroup
  );
}
```

>[!example] **In sintesi**  
>Il flusso completo del Context in React è:
>
>1. **Creazione**: `createContext()` ==genera il "contenitore" dei dati==
>2. **Provisioning**: `<Context.Provider value={...}>` ==rende disponibili quei dati a tutti i discendenti==
>3. **Consumo**: `useContext(Context)` (o un hook custom come `useGroups()`) ==permette a qualsiasi componente discendente di leggere quei dati, saltando ogni livello intermedio==


### Annidare più Context

Un'applicazione reale spesso necessita di più Context indipendenti (ad esempio uno per il tema, uno per l'autenticazione, uno per i dati di dominio). 
È possibile **annidare più Provider** uno dentro l'altro:

```tsx
export default function RootLayout() {
  return (
    <AuthProvider>
      <ThemeProvider>
        <UserProvider>
          <GroupProvider>
            <Stack>
              <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
            </Stack>
          </GroupProvider>
        </UserProvider>
      </ThemeProvider>
    </AuthProvider>
  );
}
```

>[!faq] **Perché separare i Context invece di usarne uno unico?**  
>==Separare i Context in base al dominio dei dati (autenticazione, tema, utenti, gruppi, ecc.) permette che gli aggiornamenti di un context non causino re-render nei componenti che consumano **solo** gli altri context.==  
>Se, ad esempio, cambiasse solo il tema (`ThemeContext`), i componenti che leggono solamente `useGroups()` **non** verrebbero ri-renderizzati inutilmente — a patto di applicare correttamente anche l'ottimizzazione vista nella prossima sezione.

### Context e re-render: il problema delle performance

Prima di vedere il problema, ricordiamoci cosa abbiamo appena imparato: ==il `Provider` fornisce un `value` a tutti i suoi componenti discendenti, e ogni volta che quel `value` cambia, React deve avvisare tutti i consumer del context che qualcosa è cambiato, così possono ri-renderizzarsi con i dati aggiornati.==

Questo comportamento è corretto e voluto: è **esattamente** il motivo per cui usiamo il Context. Il problema nasce da un dettaglio più sottile: **come facciamo a scrivere quel `value`?**==

#### Un esperimento mentale

Immaginiamo di scrivere il nostro `Provider` così, come abbiamo fatto finora:
```tsx
function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);

  const addGroup = (group) => {
    setGroups((prev) => [...prev, group]);
  };

  return (
    <GroupContext.Provider value={{ groups, addGroup }}>
      {children}
    </GroupContext.Provider>
  );
}
```

Sembra tutto corretto, no? Eppure c'è un problema nascosto legato a **come JavaScript confronta gli oggetti**.

###### Come JavaScript confronta gli oggetti

In JavaScript, due oggetti sono considerati "uguali" (con l'operatore `===`) **solo se sono letteralmente lo stesso oggetto in memoria** — non basta che abbiano lo stesso contenuto:
```js
const a = { valore: 1 };
const b = { valore: 1 };

console.log(a === b); // false! Contenuto identico, ma sono due oggetti diversi
```

==Ogni volta che scriviamo `{ ... }` per creare un oggetto letterale, JavaScript alloca un **nuovo spazio in memoria**, anche se il contenuto è identico a un oggetto creato un istante prima.==

#### Dove si nasconde il problema

Ora torniamo al nostro `Provider`. ==Ogni componente React, quando viene ri-renderizzato, **riesegue interamente il corpo della funzione** — comprese tutte le righe di codice al suo interno.==

Questo significa che, ogni volta che `GroupProvider` si ri-renderizza (anche per un motivo che non c'entra nulla con `groups`), questa riga:
```jsx
<GroupContext.Provider value={{ groups, addGroup }}>
```

**ricrea un oggetto `{ groups, addGroup }` completamente nuovo**, con un nuovo indirizzo in memoria — anche se `groups` e `addGroup` contengono esattamente gli stessi dati di prima.

> [!warning] **Il punto chiave**  
> ==React, per capire se il `value` di un context è cambiato, confronta il nuovo oggetto con quello del render precedente usando `===` (stesso confronto per riferimento che abbiamo visto sopra).==  
> Dato che l'oggetto `{ groups, addGroup }` è sempre "nuovo" ad ogni render del Provider, React lo considera **sempre diverso**, anche quando i dati al suo interno non sono affatto cambiati.

Il risultato concreto: ==**tutti i componenti che consumano quel context vengono ri-renderizzati ad ogni render del Provider**, indipendentemente dal fatto che i dati che a loro interessano siano cambiati o no.==

#### Perché questo è un problema

Pensiamo a un caso concreto: se il tuo `_layout.tsx` ha più Context annidati…
```tsx
<AuthProvider>
  <ThemeProvider>
    <GroupProvider>
      <Stack>...</Stack>
    </GroupProvider>
  </ThemeProvider>
</AuthProvider>
```

…e l'utente cambia semplicemente il tema (dark/light) tramite `ThemeProvider`, questo causa un re-render che si propaga verso il basso nell'albero. 
==Se `GroupProvider` non è ottimizzato, **anche tutti i componenti che leggono `useGroups()` verranno ri-renderizzati inutilmente**, pur non avendo nulla a che fare con il cambio di tema.==

Con pochi componenti il costo è trascurabile. ==Ma in un'app reale, con decine di screen che consumano lo stesso context, questi re-render "a cascata" e non necessari possono accumularsi e rallentare l'interfaccia in modo percepibile.==
#### La soluzione: memorizzare il `value` con `useMemo`

Il problema, come abbiamo visto, è che l'oggetto `value` viene **ricreato ad ogni render**, anche quando non serve. La soluzione naturale è quindi: _"ricrea l'oggetto solo quando i dati al suo interno cambiano davvero"_.

Questo è esattamente ciò che fa `useMemo`: ==memorizza (in inglese, _"memoizes"_) il risultato di un calcolo, e lo ricalcola solo quando le sue dipendenze cambiano.==
```tsx
import { useMemo } from 'react';

function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);

  const addGroup = useCallback((group) => {
    setGroups((prev) => [...prev, group]);
  }, []);

  // ✅ Il valore viene ricreato SOLO se groups o addGroup cambiano davvero
  const value = useMemo(
    () => ({ groups, addGroup }),
    [groups, addGroup]
  );

  return (
    <GroupContext.Provider value={value}>
      {children}
    </GroupContext.Provider>
  );
}
```

###### Cosa cambia concretamente

Finché `groups` e `addGroup` restano invariati tra un render e l'altro, `useMemo` **restituisce lo stesso identico oggetto** (stesso riferimento in memoria) del render precedente, invece di crearne uno nuovo. React, confrontando i due riferimenti con `===`, li trova **uguali**, e quindi **non** ri-renderizza i componenti consumer.

> [!done] **In pratica**
> 
> - Senza `useMemo`: `value` è un oggetto nuovo ad ogni render del Provider → i consumer si ri-renderizzano sempre
> - Con `useMemo`: `value` mantiene lo stesso riferimento finché `groups` o `addGroup` non cambiano realmente → i consumer si ri-renderizzano solo quando serve davvero

##### Un dettaglio da non sottovalutare: anche le funzioni sono oggetti

C'è un'insidia in più da tenere a mente. Guarda di nuovo questa riga:
```jsx
const addGroup = (group) => {
  setGroups((prev) => [...prev, group]);
};
```

Anche `addGroup` è, a tutti gli effetti, un oggetto (una funzione, in JavaScript, è un tipo speciale di oggetto). ==Questo significa che **anche questa funzione viene ricreata ad ogni render**, esattamente come succedeva con l'oggetto `{ groups, addGroup }` di prima.==

Se mettiamo `addGroup` ==nell'array di dipendenze di `useMemo`, ma `addGroup` è sempre "nuova" ad ogni render, **`useMemo` penserà sempre che qualcosa sia cambiato** — vanificando completamente l'ottimizzazione.==

La soluzione è applicare **lo stesso principio di memorizzazione anche alle funzioni**, tramite [[Lezione 4 - useEffect#Lo `useEffect`|`useCallback`]] (l'equivalente di `useMemo`, ma pensato specificamente per le funzioni):

```tsx
const addGroup = useCallback((group) => {
  setGroups((prev) => [...prev, group]);
}, []);
```

>[!ticket] **Regola pratica per i Context**  
>Nel pattern Context, si applica quasi sempre questa combinazione:
>
>1. **`useCallback`** ==per ogni funzione che finisce nel `value` del context==
>2. **`useMemo`** ==per l'oggetto `value` finale, che raggruppa stato e funzioni==
>
>==Solo così ci assicuriamo che il `value` cambi riferimento **esclusivamente** quando i dati reali cambiano, e non ad ogni singolo render del Provider.==
### Come funziona `useMemo` nel dettaglio

Riprendiamo la firma di `useMemo`:
```jsx
const value = useMemo(() => calcolo(a, b), [a, b]);
```

`useMemo` accetta **due argomenti**:

1. **Una funzione di calcolo** (`() => calcolo(a, b)`) → ==è la funzione che React eseguirà per ottenere il valore da memorizzare==
2. **Un array di dipendenze** (`[a, b]`) → ==dice a React _quando_ deve rieseguire quella funzione==

#### Il meccanismo passo-passo

Proviamo a seguire cosa succede ad ogni render, con un esempio concreto:
```jsx
function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);
  const addGroup = useCallback((group) => {
    setGroups((prev) => [...prev, group]);
  }, []);

  const value = useMemo(
    () => ({ groups, addGroup }),
    [groups, addGroup]
  );

  return <GroupContext.Provider value={value}>{children}</GroupContext.Provider>;
}
```
###### Primo render del componente

Alla primissima esecuzione, React non ha nulla in memoria a cui confrontarsi. Quindi:

1. ==React esegue la funzione di calcolo: `() => ({ groups, addGroup })`==
2. ==Ottiene un oggetto, chiamiamolo **Oggetto A**==
3. ==**Salva in memoria** sia l'Oggetto A che i valori delle dipendenze usate per crearlo (`groups` e `addGroup` in quel momento)==
4. ==Restituisce l'Oggetto A come valore di `value`==

###### Secondo render del componente

==Immaginiamo che il componente si ri-renderizzi per un qualsiasi motivo (magari un componente genitore si è aggiornato), ma **`groups` e `addGroup` non sono cambiati**.== 
A questo punto, prima di eseguire di nuovo la funzione di calcolo, React fa un controllo:

> [!abstract] **Il controllo che fa React**  
> ==React confronta ogni elemento del nuovo array di dipendenze `[groups, addGroup]` con i valori che aveva salvato al render precedente, uno per uno, usando il confronto `===`.==

Se tutte le dipendenze risultano identiche (stesso riferimento, stesso valore primitivo), React **salta completamente l'esecuzione** della funzione di calcolo, e restituisce **esattamente lo stesso Oggetto A** che aveva già in memoria dal render precedente — non un oggetto "uguale nel contenuto", ma **letteralmente lo stesso oggetto, con lo stesso indirizzo in memoria**.

######  Terzo render: una dipendenza cambia

Ora immaginiamo che l'utente chiami `addGroup(nuovoGruppo)`. Questo aggiorna lo stato `groups` tramite `setGroups`, causando un nuovo render. Questa volta, quando React controlla le dipendenze:

1. Confronta il nuovo `groups` con quello salvato in memoria → **sono diversi** (l'array `groups` è cambiato, perché `setGroups` ha creato un nuovo array con lo spread `[...prev, group]`)
2. Poiché almeno una dipendenza è cambiata, React **rieseguirà** la funzione di calcolo
3. Ottiene un **nuovo** oggetto, l'**Oggetto B** (diverso in memoria dall'Oggetto A)
4. Salva l'Oggetto B e le nuove dipendenze, sostituendo quelle vecchie
5. Restituisce l'Oggetto B come valore di `value`

#### Perché questo risolve il problema dei re-render

Ricordiamo il problema di partenza: **React decide se ri-renderizzare i consumer di un context confrontando il vecchio `value` con il nuovo, usando `===`** (lo stesso confronto per riferimento visto prima).

Grazie a `useMemo`:

- **Se le dipendenze non cambiano** → `useMemo` restituisce lo **stesso identico oggetto** di prima (Oggetto A) → React vede `vecchioValue === nuovoValue` → **nessun re-render** dei consumer
- **Se le dipendenze cambiano** → `useMemo` restituisce un **oggetto nuovo** (Oggetto B) → React vede `vecchioValue !== nuovoValue` → **i consumer si ri-renderizzano correttamente**, perché i dati sono davvero cambiati

> [!done] **Il punto centrale da ricordare**  
> ==`useMemo` non evita che il componente si ri-renderizzi (quello è governato da React normalmente) — evita invece che, _durante_ quel render, venga ricreato un nuovo oggetto quando non è necessario.== È proprio questo "riciclo" dell'oggetto precedente che permette a React di riconoscere: _"il context in realtà non è cambiato, quindi non serve avvisare i consumer"_.

#### Un'analogia per fissare il concetto

Immagina di avere una scatola (l'oggetto `value`) con dentro alcuni oggetti (`groups`, `addGroup`). Ogni volta che il tuo componente si ri-renderizza:

- **Senza `useMemo`**: ==prendi tutti gli oggetti e li rimetti dentro una **scatola nuova di zecca**, anche se gli oggetti dentro sono gli stessi di prima. Chi riceve la scatola (i consumer) vede "una scatola diversa da quella di prima" e reagisce come se qualcosa fosse cambiato.==
- **Con `useMemo`**: prima di creare una scatola nuova, controlli se gli oggetti che ci andrebbero dentro sono gli stessi della scatola precedente. Se sì, **consegni di nuovo la stessa vecchia scatola**, senza nemmeno aprirla. Chi la riceve capisce subito "è la stessa scatola di prima, non c'è nulla di nuovo da controllare".
### Riepilogo: quando usare il Context

> [!ticket] **Quando conviene usare il Context**
> 
> - ==Quando più componenti, a diversi livelli di annidamento, hanno bisogno degli stessi dati==
> - ==Quando il [[#Il problema il prop drilling|prop drilling]] renderebbe il codice eccessivamente verboso o difficile da mantenere==
> - ==Per dati "globali" all'applicazione (tema, autenticazione, utente corrente, preferenze)==

> [!failure] **Quando evitare il Context**
> 
> - ==Per dati che servono solo a un componente e ai suoi diretti figli (in questo caso le props sono sufficienti e più semplici)==
> - ==Per stati che cambiano molto frequentemente e coinvolgono aggiornamenti granulari (in questi casi il Context può causare troppi re-render, anche con `useMemo`; potrebbe convenire una libreria di state management dedicata)==


### `useCallback`: spiegazione approfondita

Abbiamo già incontrato `useCallback` nell'esempio del `GroupContext`, ma vediamo ora di capirlo a fondo, partendo dalle basi.

#### Il problema di partenza: le funzioni sono oggetti

Come abbiamo accennato parlando di [[#Come funziona `useMemo` nel dettaglio|`useMemo`]], in JavaScript **le funzioni sono un tipo speciale di oggetto**. 
Questo ha una conseguenza che spesso sorprende:
```js
const a = () => console.log('ciao');
const b = () => console.log('ciao');

console.log(a === b); // false! Anche se fanno la stessa cosa, sono due funzioni diverse
```

Esattamente come per gli oggetti letterali `{}`, ==ogni volta che scriviamo una funzione (una arrow function, una function expression), JavaScript crea **un nuovo oggetto funzione**, con un nuovo indirizzo in memoria — anche se il codice al suo interno è identico a una funzione creata un istante prima.==


#### Dove si presenta il problema in React

Ogni volta che un componente si ri-renderizza, **il suo intero corpo viene rieseguito**. Questo significa che qualsiasi funzione dichiarata _dentro_ il componente viene **ricreata da zero ad ogni render**:
```jsx
function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);

  // ⚠️ Questa funzione viene ricreata ad ogni render di GroupProvider
  const addGroup = (group) => {
    setGroups((prev) => [...prev, group]);
  };

  return (
    <GroupContext.Provider value={{ groups, addGroup }}>
      {children}
    </GroupContext.Provider>
  );
}
```

Anche se `addGroup` fa **esattamente la stessa cosa** ad ogni render (stessa logica, stesso comportamento), è comunque una **funzione nuova**, diversa in memoria dalla precedente.

#### Perché questo è un problema concreto

Ricordiamo cosa abbiamo imparato su `useMemo` nel contesto del `value` del Provider:
```jsx
const value = useMemo(
  () => ({ groups, addGroup }),
  [groups, addGroup]  // ← addGroup qui dentro
);
```

==Se `addGroup` è sempre "nuova" ad ogni render, `useMemo` la vedrà sempre come una dipendenza _cambiata_ — anche quando in realtà `groups` non è cambiato affatto.== Questo significa che `useMemo` **rieseguirà sempre** la sua funzione di calcolo, ricreando un nuovo oggetto `value` ad ogni render — vanificando completamente l'ottimizzazione che avevamo introdotto.

> [!warning] **Il punto centrale**  
> ==`useMemo` da solo non basta a stabilizzare il `value` del Provider, se le funzioni al suo interno vengono ricreate ad ogni render. Serve uno strumento che memorizzi _anche le funzioni stesse_, non solo gli oggetti che le contengono.==

#### Cos'è `useCallback`

`useCallback` è, concettualmente, **l'equivalente di `useMemo`, ma specializzato per le funzioni**. La sua firma è molto simile:
```jsx
const memoizedFunction = useCallback(() => {
  // corpo della funzione
}, [dipendenze]);
```

==`useCallback` restituisce la **stessa istanza della funzione** (stesso riferimento in memoria) tra un render e l'altro, finché nessuna delle dipendenze nell'array cambia. Solo quando una dipendenza cambia, `useCallback` restituisce una nuova funzione.==

###### Confronto diretto: `useMemo` vs `useCallback`

> [!abstract] **La differenza in una frase**
> 
> - **`useMemo`** ==memorizza il **valore restituito** da una funzione di calcolo==
> - **`useCallback`** ==memorizza **la funzione stessa**, senza eseguirla==

La differenza pratica è che `useCallback(fn, deps)` è più diretto e leggibile quando l'obiettivo è specificamente memorizzare una funzione, senza dover scrivere una funzione-che-restituisce-una-funzione come richiederebbe `useMemo`.
#### Esempio pratico completo: `FontSizeContext`

ediamo ora un esempio pratico e completo che mette insieme tutti i concetti visti finora: creazione del context, provider, consumo tramite `useContext`, e integrazione in un progetto **Expo Router**.

L'obiettivo di questo esempio è semplice: creare un **font size condiviso** tra più schermate (`PageOne` e `PageTwo`), controllabile tramite due bottoni `+` e `-`.
##### 1. [[#1. Creare il Context|Creazione del Context]]: `FontSizeContext.tsx`
```tsx
// context/FontSizeContext.tsx
import React, { createContext } from 'react';

// Passiamo un valore di default di 24
const FontSizeContext = createContext(24);

// Ed esportiamo di default questo contesto
export default FontSizeContext;
```

###### Spiegazione

- `createContext(24)` crea il context con **valore di default 24**.
- ==Questo valore di default verrà usato solo se un componente prova a leggere il context **senza** essere avvolto da nessun Provider — in questo esempio non useremo mai questo caso, ma è comunque una buona pratica fornire un default sensato.==
- A differenza dell'esempio precedente con `GroupContext` (dove usavamo TypeScript con un'interfaccia complessa e `undefined` come default), qui il context contiene semplicemente **un numero**, quindi non serve creare un tipo dedicato.

> [!note] **Perché qui non serve il custom hook**  
> Nell'esempio di `GroupContext` avevamo creato un hook personalizzato (`useGroups`) con un controllo di errore (`if (context === undefined) throw new Error(...)`). Qui, invece, **esportiamo direttamente il context** (`export default FontSizeContext`) senza custom hook, perché:
> 
> - il valore di default (`24`) è già un numero valido, quindi non c'è un vero "stato di errore" da intercettare
> - è un esempio didattico volutamente semplificato

##### 2. [[#2. Fornire il Context (Provider)|Il Provider]]: `useContextHook.tsx`

Qui troviamo il cuore della logica: ==il componente che **crea lo stato** (`size`) e lo **fornisce** tramite il Provider==.

```tsx
// context/useContextHook.tsx
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import React, { useState } from 'react';
import PageOne from '@/app/PageOne';
import PageTwo from '@/app/PageTwo';
import FontSizeContext from './FontSizeContext';

const UseContextHook = () => {
    const [size, setSize] = useState<number>(16);

    return (
        <FontSizeContext.Provider value={size}>
            <View style={styles.container}>
                <PageOne />
                <PageTwo />
                <View style={{ flexDirection: 'row', marginTop: 50 }}>
                    <TouchableOpacity
                        style={{ alignItems: 'center' }}
                        disabled={size === 41}
                        onPress={() => setSize((prev) => prev + 5)}
                    >
                        <Text style={{ marginRight: 30, fontSize: 50 }}>+</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                        style={{ alignItems: 'center' }}
                        disabled={size === 41}
                        onPress={() => setSize((prev) => prev - 5)}
                    >
                        <Text style={{ fontSize: 50 }}>-</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </FontSizeContext.Provider>
    );
};

export default UseContextHook;
```

###### Spiegazione passo-passo

1. **Stato locale** — `const [size, setSize] = useState<number>(16)` inizializza `size` a `16`. ==Nota che questo valore **sovrascrive** il default di `24` impostato in `createContext(24)`==: ==il default del context viene usato solo in assenza di Provider, mentre qui il Provider è presente e passa esplicitamente `value={size}`.==
2. **Il Provider avvolge i figli** — `<FontSizeContext.Provider value={size}>` rende `size` disponibile a **tutto ciò che si trova al suo interno**, cioè `PageOne`, `PageTwo` e (teoricamente) anche i bottoni, anche se questi ultimi non lo consumano.
3. **Aggiornamento con functional update** — `setSize((prev) => prev + 5)` e `setSize((prev) => prev - 5)` usano la [[Lezione 3 - Hooks#Aggiornare lo stato precedente in React|forma funzionale del setter]] che abbiamo già visto: ==garantisce che l'aggiornamento parta sempre dal valore **attuale** dello stato, evitando problemi di stato _stale_ in caso di click ravvicinati==.
4. **Disabilitazione condizionale** — `disabled={size === 41}` ==blocca entrambi i bottoni quando `size` raggiunge `41`==. Questo è un piccolo dettaglio poco intuitivo del tutorial originale: s==ia il bottone `+` che quello `-` si disabilitano alla stessa condizione, il che in pratica significa che, una volta raggiunto `41`, **anche il bottone `-` risulta bloccato** — probabilmente un refuso del tutorial, dato che ci si aspetterebbe che solo il bottone `+` si disabiliti al raggiungimento del massimo.==

> [!warning] **Attenzione al nome del file**  
> Il file si chiama `useContextHook.tsx` e il componente `UseContextHook`, ma **questo non è un hook** nel senso tecnico del termine (non inizia con `use` seguito da logica di stato riutilizzabile e non rispetta le [[Lezione 3 - Hooks#Alcune regole fondamentali sugli Hooks|regole degli Hooks]]) — è un componente React a tutti gli effetti, che **renderizza JSX**. Il nome è fuorviante ed è probabilmente solo una convenzione stilistica del tutorial, non una regola di React.

#### 3. I componenti consumer: `PageOne.tsx` e `PageTwo.tsx`

```tsx
// app/PageOne.tsx
import { StyleSheet, Text, View } from 'react-native';
import React, { useContext } from 'react';
import FontSizeContext from '@/context/FontSizeContext';

const PageOne = () => {
  const size = useContext(FontSizeContext);
  return (
    <View style={styles.container}>
      <Text style={{ fontSize: size }}>First page content</Text>
    </View>
  );
};

export default PageOne;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
});
```

`PageTwo.tsx` segue **esattamente lo stesso pattern**, cambiando solo il testo mostrato.

###### Spiegazione

- `const size = useContext(FontSizeContext)` legge il valore corrente fornito dal `Provider` più vicino sopra questo componente nell'albero — in questo caso, `UseContextHook`.
- ==Da notare che `PageOne` e `PageTwo` **non ricevono `size` come prop**: lo leggono direttamente dal context, saltando completamente `UseContextHook` come intermediario esplicito (anche se, di fatto, è proprio `UseContextHook` a renderizzarli come figli diretti in questo esempio).==
- Ogni volta che l'utente preme `+` o `-`, `size` cambia nello stato di `UseContextHook`, il `Provider` fornisce il nuovo valore, e **sia `PageOne` che `PageTwo` si ri-renderizzano automaticamente** con la nuova dimensione del font — senza che nessuno debba passare manualmente il nuovo valore.
#### 4. L'integrazione in Expo Router: `_layout.tsx` e `index.tsx`

Qui arriviamo al punto più delicato per un progetto **Expo Router**, diverso da un progetto Expo classico con `App.js`.

```tsx
// app/_layout.tsx
import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="home-outline" size={size} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="PageOne"
        options={{
          title: 'Pagina Uno',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="document-outline" size={size} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name='PageTwo'
        options={{
          title: 'Pagina Due',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name='document-outline' size={size} color={color} />
          )
        }}
      />
    </Tabs>
  );
}
```

```tsx
// app/index.tsx
import UseContextHook from '@/context/useContextHook';
import { StyleSheet, Text, View } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={{ fontSize: 24, marginBottom: 20, textAlign: 'center' }}>
        useContext in React Native
      </Text>
      <UseContextHook />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
});
```

###### Il punto chiave: una particolarità di questo esempio

> [!warning] **`PageOne` e `PageTwo` compaiono sia come tab che come componenti annidati**  
> Osservando attentamente la struttura, notiamo una cosa interessante: `_layout.tsx` registra `PageOne` e `PageTwo` come **tab separate** (raggiungibili navigando dalla tab bar), ma allo stesso tempo `UseContextHook` (renderizzato dentro `index.tsx`) **le importa e le mostra anche come componenti annidati**, tutte insieme nella stessa schermata Home.
> 
> ==Questo significa che `PageOne` e `PageTwo` vengono renderizzate **due volte in punti diversi**: una volta come contenuto della tab Home (dentro `UseContextHook`), e potenzialmente un'altra volta se l'utente naviga direttamente sulla loro tab dedicata.==

Quando l'utente naviga sulla tab "Pagina Uno" **direttamente** (cliccando sulla tab bar, non passando da Home), il componente `PageOne` viene renderizzato **fuori** dal `FontSizeContext.Provider` — perché quel Provider esiste solo dentro `UseContextHook`, che a sua volta vive solo dentro `index.tsx`.

###### Cosa succede in questo caso

Dato che `FontSizeContext` è stato creato con un **valore di default esplicito** (`createContext(24)`), `PageOne`, se navigato direttamente dalla tab bar, **non genera un errore** — semplicemente userà il valore di default (`24`) invece del valore controllato dai bottoni `+`/`-`.

> [!faq] **È un problema questo comportamento?**  
> Dipende dall'obiettivo. Se l'idea è che il font size debba essere condiviso **ovunque nell'app**, la soluzione più corretta sarebbe spostare il `Provider` (cioè la logica di `UseContextHook`, senza il JSX di `PageOne`/`PageTwo` annidati) **nel `_layout.tsx`**, avvolgendo l'intero `<Tabs>`. In questo modo, indipendentemente da quale tab l'utente visita, tutte condividerebbero lo stesso `size` e gli stessi bottoni per modificarlo (magari posizionati in un punto fisso, come un header comune).
> 
> ==Questo esempio, così com'è strutturato, funziona correttamente **solo quando si passa dalla Home**, dato che è lì che vive sia il Provider che le istanze "condivise" di `PageOne`/`PageTwo`.== È un aspetto tipico da tenere a mente quando si integra un tutorial pensato per un progetto Expo "classico" (con `App.js` come unico entry point) in un progetto **Expo Router**, dove la navigazione stessa introduce più "punti di ingresso" verso lo stesso componente.

##### Applicare `useCallback` al nostro esempio

Riprendiamo il `GroupProvider` e applichiamo `useCallback` ad `addGroup`:
```tsx
import { useCallback, useMemo, useState } from 'react';

function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);

  // ✅ addGroup mantiene lo stesso riferimento tra i render
  const addGroup = useCallback((group) => {
    setGroups((prev) => [...prev, group]);
  }, []); // array vuoto: la funzione non dipende da nulla che cambia

  const value = useMemo(
    () => ({ groups, addGroup }),
    [groups, addGroup]
  );

  return (
    <GroupContext.Provider value={value}>
      {children}
    </GroupContext.Provider>
  );
}
```

###### Perché l'array di dipendenze è vuoto `[]`

Guardiamo bene il corpo di `addGroup`:
```tsx
const addGroup = useCallback((group) => {
  setGroups((prev) => [...prev, group]);
}, []);
```


==Questa funzione non fa mai riferimento diretto a `groups` — usa invece la [[Lezione 3 - Hooks#Aggiornare lo stato precedente in React|forma funzionale del setter]] (`prev => [...prev, group]`), che riceve automaticamente lo stato più aggiornato da React stesso, senza bisogno di "catturare" `groups` dall'esterno.==

Questo è un dettaglio molto importante: **se `addGroup` non dipende da nessuna variabile esterna che cambia**, allora non ha mai bisogno di essere ricreata — può rimanere sempre la stessa funzione, per tutta la vita del componente. Per questo l'array di dipendenze è vuoto.

> [!ticket] **Regola pratica**  
> ==Preferisci sempre la forma funzionale del setter (`setGroups(prev => ...)`) invece di quella diretta (`setGroups([...groups, newGroup])`) quando scrivi funzioni che finiranno dentro `useCallback`. Questo ti permette quasi sempre di lasciare l'array di dipendenze vuoto, rendendo la funzione stabile per l'intera vita del componente.==

##### Un esempio in cui servono davvero delle dipendenze

Non tutte le funzioni possono avere un array di dipendenze vuoto. Immaginiamo una funzione che filtra i gruppi in base a un testo di ricerca esterno:
```tsx
function GroupProvider({ children }) {
  const [groups, setGroups] = useState([]);
  const [searchText, setSearchText] = useState('');

  // Questa funzione USA searchText direttamente, non tramite un setter funzionale
  const getFilteredGroups = useCallback(() => {
    return groups.filter((g) => g.name.includes(searchText));
  }, [groups, searchText]); // ⚠️ deve rieseguirsi se groups O searchText cambiano

  // ...
}
```

Qui `getFilteredGroups` **legge direttamente** `groups` e `searchText` dal closure (dall'ambiente circostante), quindi **deve** essere ricreata ogni volta che uno di questi due valori cambia — altrimenti continuerebbe a filtrare usando dati "vecchi", intrappolati nella versione precedente della funzione (il problema dello _stale state_ che abbiamo visto parlando di `useState`).

> [!faq] **Come decido quali dipendenze mettere nell'array?**  
> ==La regola è semplice: ogni variabile (stato, prop, altra funzione memorizzata) che la funzione legge direttamente dal proprio "scope" esterno, e che può cambiare nel tempo, va inserita nell'array di dipendenze.== Se la funzione non legge nulla dall'esterno (o legge solo tramite `prev` nella forma funzionale del setter), l'array può restare vuoto.

##### Un dettaglio sottile: quando `useCallback` "non serve"

È importante essere onesti su un punto: **`useCallback` da solo non evita che la funzione venga ricreata al primo render**, né impedisce al componente di ri-renderizzarsi. Il suo unico scopo è: ==_"se la funzione non è cambiata rispetto all'ultimo render, restituisci quella vecchia invece di crearne una nuova"_==.

> [!failure] **Un errore comune: usare `useCallback` "ovunque"**  
> Avvolgere _ogni_ funzione in `useCallback` "per sicurezza" non è sempre una buona pratica. `useCallback` stesso ha un piccolo costo (deve confrontare le dipendenze ad ogni render). ==Ha senso usarlo quando la funzione:==
> 
> - ==viene passata come **dipendenza** ad un altro hook come `useMemo`, `useEffect` o un altro `useCallback`==
> - ==viene passata come **prop** a un componente figlio ottimizzato con `React.memo` (che salta il re-render se le props non cambiano)==
> 
> ==Se una funzione viene usata solo internamente al componente (es. dentro un `onPress`, senza essere passata altrove né inserita in un array di dipendenze), avvolgerla in `useCallback` spesso non porta alcun beneficio reale.==

#### Perché nel pattern Context lo usiamo quasi sempre

Nel caso specifico del pattern Context che abbiamo visto, **`useCallback` è quasi sempre giustificato**, perché le funzioni del Provider (`addGroup`, `deleteGroup`, ecc.) rientrano esattamente nel primo caso sopra: **vengono sempre inserite come dipendenza di `useMemo`** per costruire il `value` del Provider.
```tsx
const addGroup = useCallback((group) => {
  setGroups((prev) => [...prev, group]);
}, []);

const deleteGroup = useCallback((groupId) => {
  setGroups((prev) => prev.filter((g) => g.id !== groupId));
}, []);

// Entrambe le funzioni sopra sono dipendenze di questo useMemo:
const value = useMemo(
  () => ({ groups, addGroup, deleteGroup }),
  [groups, addGroup, deleteGroup]
);
```

Senza `useCallback` su `addGroup` e `deleteGroup`, l'intera catena di ottimizzazione con `useMemo` **si romperebbe**, perché quelle funzioni sarebbero comunque "nuove" ad ogni render, forzando `useMemo` a ricreare sempre un nuovo oggetto `value`.

>[!example] **In sintesi**
>
>- Le funzioni, come gli oggetti, vengono **ricreate ad ogni render** in JavaScript
>- `useCallback(fn, deps)` ==**memorizza una funzione**, restituendo la stessa istanza finché le dipendenze non cambiano== — è l'equivalente di `useMemo` applicato specificamente alle funzioni
>- Usare la **forma funzionale dei setter** (`setState(prev => ...)`) ==all'interno delle funzioni permette quasi sempre di lasciare l'array di dipendenze **vuoto**, rendendo la funzione stabile per tutta la vita del componente==
>- Nel pattern Context, `useCallback` è quasi sempre necessario **in combinazione con `useMemo`**: ==senza di esso, l'intera ottimizzazione contro i re-render superflui non funzionerebbe==
