# Introduzione : Tab Navigator 
Fino ad ora abbiamo lavorato con lo [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^752b8b|Stack Navigator]], che organizza la navigazione come una pila di schermate: 
- ==ogni nuova schermata si aggiunge sopra la precedente e si torna indietro tramite il pulsante Back.== 
- ==È un modello lineare, adatto per flussi come login → home, o lista → dettaglio.==

Il **Tab Navigator** introduce un modello di navigazione completamente diverso: 
- ==invece di una pila, abbiamo una **barra di schede** — solitamente in basso — che permette di passare da una sezione all'altra dell'app in modo diretto, senza dover seguire un percorso sequenziale.== 

> [!note] **È il pattern che vedi in app come Instagram, Spotify o TikTok, dove le sezioni principali sono sempre accessibili con un tap.**
> 

I due navigator non si escludono a vicenda: 
- ==nella maggior parte delle app reali vengono **usati insieme**.== 
- ==Una struttura tipica è avere il Tab Navigator come radice, con ogni scheda che contiene al suo interno uno Stack Navigator per gestire la navigazione interna a quella sezione.== 
Vedremo esattamente questo pattern durante la lezione.

Gli argomenti che affronteremo sono:

- creare il layout per le schede in basso
- aggiungere icone e etichette alla barra
- nascondere schermate dalla barra
- usare i badge sulle icone
- annidare uno Stack Navigator dentro una scheda
- gestire titoli duplicati
- configurare il comportamento della scheda al ritorno e alla perdita del focus


## Panoramica del Tab Navigator

Per visualizzare le schermate come schede in basso, il file `_layout.tsx` della sezione deve restituire un **Tab Navigator** invece di uno Stack Navigator — esattamente come abbiamo fatto con lo [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^752b8b|Stack Navigator]], ma con un componente diverso.

Ogni scheda può essere:

- una **singola schermata** — il caso più semplice
- un **navigatore a sé stante** — ad esempio uno Stack Navigator annidato dentro una scheda

Questo secondo caso è estremamente comune nelle app mobile reali: 
- ==una scheda contiene il suo stack interno, permettendo di navigare in profondità all'interno di quella sezione senza abbandonare la scheda corrente.==

##### La struttura ad albero

Quando si annidano navigatori, la cronologia di navigazione smette di essere una lista lineare e diventa una **struttura ad albero**:
```
Tab Navigator
├── Scheda 1 (singola schermata)
└── Scheda 2 (Stack Navigator)
    ├── Screen A
    └── Screen B
```

Navigando verso Screen B dentro la Scheda 2, ci si trova contemporaneamente dentro uno stack e dentro una scheda. Questo è il motivo per cui la gestione della navigazione mobile è più complessa rispetto al web — non c'è un unico storico lineare, ma rami indipendenti che coesistono.

### Creare un layout per le schede in basso 

Il punto di partenza è un `_layout.tsx` che restituisce uno [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^752b8b|Stack Navigator]] e quattro schermate: 

1. `index.tsx`, 
2. `second.tsx`, 
3. `third.tsx` 
4. e `fourth.tsx`. 
Con lo Stack, le schermate non sono accessibili direttamente — bisogna aggiungere pulsanti per navigare tra loro.

Per passare al Tab Navigator basta **sostituire `<Stack />` con `<Tabs />`** nel layout:
```tsx
import { Tabs } from "expo-router";

export default function RootLayout() {
  return (
    <>
      <StatusBar style="auto" />
      <Tabs />
    </>
  );
}
```

Expo Router rileva automaticamente tutti i file nella cartella `app/` e li mostra come schede — esattamente come faceva con lo Stack, senza bisogno di dichiararle esplicitamente.


##### Dichiarare le schede esplicitamente

Anche se non è obbligatorio, è consigliabile elencare le schermate dentro `<Tabs>` tramite `<Tabs.Screen>` per due motivi: controllare l'**ordine** in cui appaiono nella barra e configurare le **opzioni di visualizzazione** di ciascuna.

e una singola schermata (`index.tsx`). 
```tsx
<Tabs>
    <Tabs.Screen name="index" />
    <Tabs.Screen name="second" />
    <Tabs.Screen name="third" />
    <Tabs.Screen name="fourth" />
</Tabs>
```
Il prop `name` segue la stessa convenzione già vista con [[Lezione 2 - Usare lo stack navigator con Expo Router#Il prop `name`|`Stack.Screen`]]: percorso del file relativo alla cartella `app/`, senza barra iniziale e senza estensione.


> [!deep] ##### Nascondere una schermata dalla barra
>
>È possibile che una schermata esista nel filesystem — e quindi sia raggiungibile tramite navigazione — ma non debba apparire come scheda nella barra in basso. Si ottiene passando `href: null` nelle opzioni:
>
>```tsx
><Tabs.Screen
>    name="(stackNavigator)"
>    options={{
>        href: null,       // non appare nella barra in basso
>        headerShown: false // nasconde anche l'header
>    }}
>/>
>```
>
>>[!hint] `href: null` è ==utile per schermate di supporto come modali, dettagli, o navigatori annidati che non devono essere accessibili direttamente dalla barra delle schede, ma solo tramite navigazione programmatica.==

### Aggiungere icone alla barra delle schede
Le icone placeholder generate automaticamente da Expo Router possono essere sostituite tramite le opzioni di `<Tabs.Screen>`. Possono essere qualsiasi componente React Native, ma la scelta più comune è usare le icone vettoriali di Expo( [icons]([https://docs.expo.dev/guides/icons/](https://icons.expo.fyi/Index)), installabili tramite:
```shell
npx expo install @expo/vector-icons
```
Una volta installate, si importa il set desiderato — in questo caso `MaterialCommunityIcons`:
```tsx
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
```

L'icona si passa tramite la proprietà `tabBarIcon` dentro `options`, che accetta una **funzione** che restituisce un componente:
```tsx
<Tabs.Screen name="index"
    options={{
        tabBarIcon: () => (
            <MaterialCommunityIcons name="dice-1-outline" size={24} color="black" />
        )
    }}
/>
```


#### Colore e dimensione dinamici

Con questa implementazione le icone appaiono correttamente, ma non cambiano colore quando si passa da una scheda all'altra. Il Tab Navigator passa automaticamente alla funzione `tabBarIcon` alcuni parametri tra cui `color` e `size`, che riflettono lo stato attivo o inattivo della scheda. Basta destrutturarli e passarli all'icona:
```tsx
<Tabs.Screen name="second"
    options={{
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-2-outline" size={size} color={color} />
        )
    }}
/>
```

In questo modo il Tab Navigator gestisce automaticamente il colore dell'icona — grigio quando la scheda è inattiva, colorato quando è attiva.

##### `tabBarIcon`

`tabBarIcon` è: 
- una [[Lezione 2 - Il Props Object#Il Props Object|proprietà]] di `options` che ==accetta una **funzione** che restituisce un componente React Native da usare come icona nella barra delle schede.== 

> [!hint] **È importante che sia una funzione e non direttamente un componente**
>   ==perché il Tab Navigator ha bisogno di chiamarla passandole i parametri dello stato corrente della scheda.==

###### Uso statico

Nella forma statica la funzione ignora i parametri e restituisce sempre la stessa icona con valori fissi:
```tsx
tabBarIcon: () => (
    <MaterialCommunityIcons name="dice-1-outline" size={24} color="black" />
)
```

Il problema è che `color` e `size` sono hardcoded — l'icona avrà sempre lo stesso aspetto indipendentemente dal fatto che la scheda sia attiva o meno.

###### Uso dinamico

Il Tab Navigator chiama `tabBarIcon` passandole un oggetto con diversi parametri. I più utili sono:

| Parametro | Tipo      | Descrizione                                                       |
| --------- | --------- | ----------------------------------------------------------------- |
| `color`   | `string`  | colore calcolato dal navigator in base allo stato attivo/inattivo |
| `size`    | `number`  | dimensione consigliata per l'icona                                |
| `focused` | `boolean` | `true` se la scheda è quella attualmente selezionata              |
Destrutturandoli si ottiene un'icona che reagisce allo stato della scheda:
```tsx
tabBarIcon: ({ color, size }) => (
    <MaterialCommunityIcons name="dice-2-outline" size={size} color={color} />
)
```

==`color` viene calcolato automaticamente dal navigator in base a `tabBarActiveTintColor` e `tabBarInactiveTintColor`== — **non devi gestire tu la logica attivo/inattivo, ci pensa il Tab Navigator.**

`focused` invece è ==utile quando vuoi cambiare l'icona stessa in base allo stato, non solo il colore==:
```tsx
tabBarIcon: ({ color, size, focused }) => (
    <MaterialCommunityIcons
        name={focused ? "dice-1" : "dice-1-outline"}
        size={size}
        color={color}
    />
)
```

In questo caso quando la scheda è attiva l'icona è piena, quando è inattiva è solo il contorno.



#### Colore globale delle schede attive

Invece di definire il colore scheda per scheda, si può impostare il colore delle schede attive a livello globale tramite `screenOptions` sul componente `<Tabs>`:
```tsx
<Tabs screenOptions={{ tabBarActiveTintColor: 'blue' }}>
```

`screenOptions` funziona come un `options` di default applicato a tutte le schede — ogni `<Tabs.Screen>` può comunque sovrascriverlo localmente per casi specifici, seguendo la stessa [[Lezione 2 - Usare lo stack navigator con Expo Router#Precedenza delle opzioni|logica di precedenza]] già vista con lo Stack Navigator.


###### `screenOptions`

`screenOptions` è un [[Lezione 2 - Il Props Object#Il Props Object|prop]] del componente `<Tabs>` che ==permette di definire opzioni di default per **tutte le schede contemporaneamente**==. 
==Evita di ripetere le stesse opzioni su ogni `<Tabs.Screen>`.==

Accetta le stesse proprietà di `options`, più alcune specifiche del Tab Navigator:

| Proprietà                 | Descrizione                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `tabBarActiveTintColor`   | colore di icona ed etichetta della scheda attiva             |
| `tabBarInactiveTintColor` | colore di icona ed etichetta delle schede inattive           |
| `tabBarStyle`             | stile della barra in basso (altezza, colore di sfondo, ecc.) |
| `tabBarShowLabel`         | mostra o nasconde l'etichetta testuale sotto l'icona         |
| `tabBarLabelStyle`        | stile del testo dell'etichetta                               |
| `headerShown`             | mostra o nasconde l'header su tutte le schermate             |
**Un esempio completo:**
```tsx
<Tabs
    screenOptions={{
        tabBarActiveTintColor: 'blue',
        tabBarInactiveTintColor: 'gray',
        tabBarStyle: { backgroundColor: '#f5f5f5' },
        tabBarShowLabel: true,
        headerShown: false
    }}
>
```

Come già visto con lo [[Lezione 2 - Usare lo stack navigator con Expo Router#Precedenza delle opzioni|Stack Navigator]], le opzioni definite in `screenOptions` ==sono il default globale== — ogni `<Tabs.Screen>` può sovrascriverle localmente per casi specifici.


### Etichette e titoli 
%% Continuare da qui %%