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

^20317e

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
Nella barra delle schede ogni tab ha un'etichetta testuale sotto l'icona. Per impostazione predefinita corrisponde al `name` della schermata, quindi una schermata chiamata `index` avrà l'etichetta "index".

Ci sono tre modi per configurarla, in ordine di precedenza crescente:
1. **`title`** — ==se impostato, viene usato sia come titolo dell'header che come etichetta della tab bar==:

```tsx
<Tabs.Screen name="index"
    options={{
        title: 'Home',
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-1-outline" size={size} color={color} />
        )
    }}
/>
```

In questo caso la Label si chiamerà "Index".

Mentre se assegniamo un titolo alla schermata, per impostazione predefinita tale titolo verrà utilizzato anche come etichetta:  
```tsx
<Tabs.Screen name="index"

          options={{

            title: 'Home',

            tabBarIcon: ({ color, size }) => (

              <MaterialCommunityIcons name="dice-1-outline" size={size} color={color} />

            )

          }}
```

In questo caso sia l'header che l'etichetta mostreranno "Home".


**2. `tabBarLabel`** — proprietà **specifica** della tab bar: 
- ==sovrascrive solo l'etichetta sotto l'icona, lasciando il titolo dell'header invariato. ==
- ==Non appena viene impostato, `title` e `tabBarLabel` diventano completamente indipendenti:==
```tsx
<Tabs.Screen name="index"
    options={{
        title: 'Home',         // header → "Home"
        tabBarLabel: 'Index',  // etichetta tab bar → "Index"
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-1-outline" size={size} color={color} />
        )
    }}
/>
```

Ora la seconda schermata della tab-bar si chiamerà "`Map`"


> [!NOTE] Nel primo tab screen la proprietà `tabBarLabel` sovrascrive la proprietà `name`

**3. Nascondere le etichette** —   ==tramite `tabBarShowLabel: false` in `screenOptions` si nascondono le etichette su tutte le schede==:
```tsx
<Tabs screenOptions={{ tabBarActiveTintColor: 'blue', tabBarShowLabel: false }}>
```


| Proprietà     | Effetto                                                   |
| ------------- | --------------------------------------------------------- |
| `name`        | etichetta di default se non è impostato nient'altro       |
| `title`       | sovrascrive sia header che etichetta                      |
| `tabBarLabel` | sovrascrive solo l'etichetta, ha la precedenza su `title` |
>[!hint] Come sempre, per esplorare tutte le opzioni disponibili usa `CTRL + Spazio` dentro `options={{}}` per vedere i tipi TypeScript completi.

### Nascondere una schermata dalla barra delle schede

[[#^20317e|Come abbiamo visto prima]] per nascondere una schermata dalla barra delle schede senza rimuoverla dal filesystem si passa `href: null` nelle opzioni:
```tsx
{/* questa rotta esiste ed è raggiungibile tramite navigazione, ma NON appare nella barra in basso */}
<Tabs.Screen
    name="(stackNavigator)"
    options={{
        href: null,        // rimuove la scheda dalla barra in basso
        headerShown: false // nasconde anche l'header
    }}
/>
```

`href: null` dice al Tab Navigator: 
- ==di non generare nessun link verso questa schermata nella barra==
- ==la schermata continua ad esistere nel filesystem e ci si può navigare programmaticamente tramite `router.push()`, ma l'utente non la vedrà mai come scheda selezionabile.==

>[!remember] **Questo pattern è utile per schermate di supporto come modali, dettagli, o navigatori annidati che devono essere accessibili solo tramite navigazione programmatica e non direttamente dalla barra delle schede.**


### Badges

I badge sono: 
- ==indicatori visivi che appaiono sull'icona della scheda in alto a destra, comunemente usati per notifiche o contatori.== 
Si aggiungono tramite la proprietà `tabBarBadge`:

```tsx
<Tabs.Screen name="fourth"
    options={{
        title: "fourth",
        tabBarBadge: 2,
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-4-outline" size={size} color={color} />
        )
    }}
/>
```

`tabBarBadge` accetta sia un numero che una stringa — in un caso reale il valore sarebbe dinamico, ad esempio il numero di notifiche non lette preso dallo stato dell'applicazione.


##### Personalizzare lo stile del badge

Lo stile del badge si personalizza tramite `tabBarBadgeStyle`:
```tsx
<Tabs.Screen name="fourth"
    options={{
        title: "fourth",
        tabBarBadge: 2,
        tabBarBadgeStyle: {
            backgroundColor: 'tomato',
            color: 'white'
        },
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-4-outline" size={size} color={color} />
        )
    }}
/>
```

>[!hint] In un'app reale `tabBarBadge` viene quasi sempre collegato allo stato globale dell'applicazione — ad esempio un context o uno store Redux — in modo che il contatore si aggiorni automaticamente al variare dei dati.

#### Esempio reale 
Per capire come i badge vengono aggiornati automaticamente prendiamo ad esempio una scheda "Notifica" il cui badge mostra il numero di notifiche non lette.
```tsx
// context/NotificationContext.tsx
import React, { createContext, useContext, useState } from 'react';

type NotificationContextType = {
    unreadCount: number;
    addNotification: () => void;
    markAllAsRead: () => void;
};

const NotificationContext = createContext<NotificationContextType | null>(null);

export const NotificationProvider = ({ children }: { children: React.ReactNode }) => {
    const [unreadCount, setUnreadCount] = useState(0);

    const addNotification = () => setUnreadCount(prev => prev + 1);
    const markAllAsRead = () => setUnreadCount(0);

    return (
        <NotificationContext.Provider value={{ unreadCount, addNotification, markAllAsRead }}>
            {children}
        </NotificationContext.Provider>
    );
};

export const useNotifications = () => useContext(NotificationContext)!;
```

Nel layout avvolgi tutto nel provider e leggi `unreadCount` per passarlo al badge:
```tsx
// _layout.tsx
import { useNotifications, NotificationProvider } from '../context/NotificationContext';

function Layout() {
    const { unreadCount } = useNotifications();

    return (
        <Tabs screenOptions={{ tabBarActiveTintColor: 'blue' }}>
            <Tabs.Screen name="index"
                options={{
                    title: 'Home',
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="home" size={size} color={color} />
                    )
                }}
            />
            <Tabs.Screen name="notifications"
                options={{
                    title: 'Notifiche',
                    // se unreadCount è 0 non mostra il badge, altrimenti mostra il numero
                    tabBarBadge: unreadCount > 0 ? unreadCount : undefined,
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="bell-outline" size={size} color={color} />
                    )
                }}
            />
        </Tabs>
    );
}

// il provider deve stare fuori da Layout per rendere il context disponibile
export default function RootLayout() {
    return (
        <NotificationProvider>
            <Layout />
        </NotificationProvider>
    );
}
```


Nella schermata delle notifiche puoi simulare l'arrivo di nuove notifiche e azzerarle:
```tsx
// app/notifications.tsx
import { useNotifications } from '../context/NotificationContext';

export default function NotificationsScreen() {
    const { unreadCount, addNotification, markAllAsRead } = useNotifications();

    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', gap: 16 }}>
            <Text>Notifiche non lette: {unreadCount}</Text>
            <Button title="Simula nuova notifica" onPress={addNotification} />
            <Button title="Segna tutte come lette" onPress={markAllAsRead} />
        </View>
    );
}
```

> [!todo] **Il flusso è:**
>  `addNotification()` aggiorna `unreadCount` nel context → il layout rileva il cambiamento e aggiorna `tabBarBadge` → il badge si aggiorna automaticamente su tutte le istanze del navigator. Premendo "Segna tutte come lette" `unreadCount` torna a `0` e il badge sparisce perché `undefined` non viene renderizzato.ù

### Utilizzare un navigatore di stack in una scheda 
Fino ad ora ogni scheda corrisponde a una singola schermata. 
==È però possibile trasformare una scheda in un **navigatore a pila**, permettendo di navigare in profondità all'interno di quella scheda senza abbandonarla==.

L'obiettivo è trasformare la scheda `second` in uno Stack Navigator con tre schermate interne:
```
app/
├── index.tsx
├── second/
│   ├── index.tsx        → schermata principale della scheda
│   ├── nested.tsx       → prima schermata annidata
│   └── also-nested.tsx  → seconda schermata annidata
├── third.tsx
└── fourth.tsx
```

La struttura dei percorsi risultante sarà:
```
/index
/second          ← Stack Navigator
    /second/index
    /second/nested
    /second/also-nested
/third
/fourth
```

Dalla prospettiva dell'utente, la scheda `second` si comporta come le altre — è sempre visibile nella barra in basso — ma ==al suo interno ha uno stack indipendente che permette di navigare tra `index`, `nested` e `also-nested` senza uscire dalla scheda.==

> [!hint] Questa è la struttura più comune nelle app mobile reali: 
> - ==il Tab Navigator gestisce le sezioni principali dell'app, mentre ogni sezione ha il suo Stack Navigator interno per gestire la navigazione in profondità.==


#### Perché serve un `_layout.tsx`?

Senza un file di layout dentro `second/`, Expo Router risale la gerarchia fino al layout radice, che restituisce un `<Tabs>`. Il risultato è che `nested.tsx` e `also-nested.tsx` vengono aggiunte come schede nella barra in basso — non è quello che vogliamo.

Per risolvere si crea un `_layout.tsx` dentro `second/` che restituisce uno Stack Navigator:
```tsx
// app/second/_layout.tsx
export default function StackLayout() {
    return <Stack />;
}
```
Da questo momento Expo Router usa questo layout per tutte le schermate dentro `second/`, che vengono gestite come una pila indipendente invece che come schede.




##### Navigazione tra le schermate annidate

`second/index.tsx` naviga verso `nested`:
```tsx

export default function SecondScreen() {
    const router = useRouter();
    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Second Index Screen</Text>
            <Pressable onPress={() => router.push('/second/nested')}>
                <Text>Push to the nested screen</Text>
            </Pressable>
        </View>
    );
}
```


`second/nested.tsx` naviga verso `also-nested`:

```tsx
export default function NestedScreen() {
    const router = useRouter();
    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Nested Screen</Text>
            <Pressable onPress={() => router.push('/second/also-nested')}>
                <Text>Push to the also nested screen</Text>
            </Pressable>
        </View>
    );
}
```

`second/also-nested.tsx` usa `dismissAll()` per tornare direttamente alla radice dello stack:

```tsx
export default function AlsoNestedScreen() {
    const router = useRouter();
    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Also Nested Screen</Text>
            {/* dismissAll chiude tutte le schermate nello stack e torna a second/index */}
            <Pressable onPress={() => router.dismissAll()}>
                <Text>Return to the second tab</Text>
            </Pressable>
        </View>
    );
}
```

> [!NOTE] **`dismissAll()` è diverso da `back()`:**
> -  `back()` ==torna di un solo livello,== 
> - `dismissAll()` ==chiude **tutto lo stack** e riporta direttamente alla prima schermata — in questo caso `second/index`.==

#### Rimuovere i titoli duplicati

Quando si annida uno Stack Navigator dentro una scheda del Tab Navigator, si ottengono **due header sovrapposti**: 
- ==quello del Tab Navigator in alto e quello dello Stack Navigator appena sotto.== 
- ==Non è un comportamento desiderato.==

La soluzione più comune è: 
- ==nascondere l'header del Tab Navigator, lasciando quello dello Stack Navigator:==
	-  ==in questo modo i titoli possono cambiare dinamicamente durante la navigazione all'interno dello stack.==

Si imposta `headerShown: false` nelle opzioni della scheda `second` nel layout radice: 
```tsx
 // app/_layout.tsx
<Tabs.Screen name="second"
    options={{
        title: 'second',
        headerShown: false,  // nasconde l'header del Tab Navigator
        tabBarLabel: 'Map',
        tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="dice-2-outline" size={size} color={color} />
        )
    }}
/>
```

A questo punto l'unico header visibile è quello dello Stack Navigator interno, che si configura nel `_layout.tsx` dentro `second/`:

```tsx
// app/second/_layout.tsx
export default function StackLayout() {
    return (
        <Stack>
            <Stack.Screen name="index" options={{ title: 'index' }} />
            <Stack.Screen name="nested" options={{ title: 'nested' }} />
            <Stack.Screen name="also-nested" options={{ title: 'also-nested' }} />
        </Stack>
    );
}
```

>[!warning] **I valori di `name` qui sono relativi al file di layout corrente, non al percorso assoluto. Quindi si scrive `nested` e non `second/nested`.**


### Aggiungere un navigatore di stack al percorso dell'indice 
E se volessimo aggiungere anche un navigatore a pila nella scheda Home? Beh, la nostra scheda Home visualizza la route index, che è una route speciale. Quando si esegue la mappa del sito (`npx-expo-router-sitemap`), la route index è proprio questa (/). Ed è la schermata che si apre per prima all'avvio dell'app. Quindi il problema che abbiamo è che se creiamo una cartella in cui inserire la nostra schermata index, anche se la colleghiamo correttamente nel layout delle nostre schede, quando aggiorniamo l'app, otterremo questa pagina "non trovata": questo perché al primo avvio, il router sta cercando di visualizzare questa route index e in effetti non ce n'è una.

Puoi verificarlo facilmente anche con il comando CLI, ma è qui che entrano in gioco le cartelle di raggruppamento, quindi quando aggiungi le parentesi intorno alla cartella home e, in questo caso, ho dovuto anche riavviare il bundler e aggiornare l'app. La nostra pagina indice viene nuovamente visualizzata

Possiamo vederla anche qui nella mappa del sito. Ora non ci resta che duplicare questa schermata indice in un'altra schermata per lo stack
Aggiungi un pulsante dalla schermata dell'indice alla schermata annidata.

```tsx
export default function IndexScreen() {

  const routerToNestedHome = useRouter()

  
  

  return (

    <View style={styles.container}>

      <Text style={styles.heading}>Index Screen</Text>

      <Pressable style={styles.button} onPress={() => routerToNestedHome.push('/home-nested')}>

        <Text>Push to the nested home </Text>

      </Pressable>

    </View >

  );

}
```


Aggiungere un layout alla cartella (home) che restituisca uno stack Navigator e nel 
```
import { View, Text } from 'react-native'

import React from 'react'

import { Stack } from 'expo-router'

  

const LayoutScreenHome = () => {

    return (

        <Stack />

    )

}

  

export default LayoutScreenHome
```
layout radice assicurarsi di puntare alla cartella home
```tsx
 <Tabs.Screen

          name="(home)"

          options={{

            title: 'Home',

            tabBarLabel: 'Home',

            headerShown: false,

            tabBarIcon: ({ color, size }) => (

              <MaterialCommunityIcons name="home-outline" size={size} color={color} />

            )

          }}

        />
```

E ora, quando aggiorniamo l'app, il nostro indice ha annidato un navigatore
Come per la seconda schermata, è possibile nascondere questa intestazione con `headerShown: false`.

### Prima schermata ad aprirsi
