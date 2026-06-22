# Introduzione: Costruire un flusso Auth con Expo Router

Nelle lezioni precedenti abbiamo costruito una solida base di navigazione: lo [[Lezione 2 - Usare lo stack navigator con Expo Router#Navigazione in uno stack|Stack Navigator]] per la navigazione lineare, il [[Lezione 3 - Utilizzo di un Tab Navigator con Expo Router#Panoramica del Tab Navigator|Tab Navigator]] per le sezioni principali dell'app, le [[Lezione 4 - Le modals#Quando usare una Modal|modals]] per le schermate temporanee sovrapposte, e i [[Lezione 2 - Usare lo stack navigator con Expo Router#Percorsi dinamici|percorsi dinamici]] per le rotte parametriche. Abbiamo anche visto come usare [[Lezione 4 - Le modals#`unstable_settings`|`unstable_settings`]] per gestire il [[Lezione 4 - Le modals#Deep Linking in una finestra modale|deep linking]] e come il [[Lezione 3 - Utilizzo di un Tab Navigator con Expo Router#2. Redirect in `index.tsx`|`Redirect`]] permetta di smistare l'utente verso destinazioni diverse in base allo stato dell'app.

È proprio quest'ultimo concetto che diventa il protagonista di questa lezione. 
In quasi ogni app reale esiste una distinzione fondamentale tra due stati dell'utente: 
**autenticato** e non autenticato. 
==Queste due condizioni corrispondono a due aree completamente separate dell'app — l'area pubblica, accessibile a chiunque (login, registrazione, onboarding), e l'area privata, accessibile solo dopo aver effettuato l'accesso (home, profilo, impostazioni).==

Gestire questa separazione in modo corretto non è banale: 
- ==Non basta nascondere alcuni pulsanti o mostrare schermate diverse — bisogna assicurarsi che un utente non autenticato non possa mai raggiungere le schermate protette, neanche tramite deep link o navigazione diretta.== 
- ==E allo stesso tempo, un utente già autenticato non dovrebbe mai vedere la schermata di login.==

In questa lezione vedremo come costruire questo flusso in Expo Router, affrontando progressivamente tutti gli aspetti del problema:

- come strutturare le rotte per separare area pubblica e area privata
- come aggiungere i redirect di autenticazione
- come memorizzare e mantenere lo stato di autenticazione
- come gestire il caso in cui lo stato di autenticazione non è ancora noto — il cosiddetto stato **indeciso** — evitando flash indesiderati di contenuto durante il caricamento iniziale

## Il flusso di autenticazione 

Il flusso di autenticazione in Expo Router segue una logica semplice:
```css
Tentativo di navigazione verso /
        ↓
Hai effettuato l'accesso?
    ↓           ↓
   sì           no
    ↓           ↓
apri /    reindirizza a /login
```

Prima di renderizzare qualsiasi schermata, si verifica se l'utente è autenticato. Se non lo è, viene reindirizzato alla schermata di login. L'elemento chiave di questo meccanismo è il componente [[Lezione 3 - Utilizzo di un Tab Navigator con Expo Router#2. Redirect in `index.tsx`|`<Redirect>`]] che abbiamo già incontrato:
```tsx
<Redirect href='/login' />
```

##### Dove inserire la logica di autenticazione

L'app che vogliamo proteggere ha questa struttura:
```tsx
app/
├── (tabs)/
├── modal.tsx
└── _layout.tsx
```

Tutto ciò che si trova dentro `(tabs)` e le [[Lezione 4 - Le modals#Quando usare una Modal|modals]] deve essere accessibile solo agli utenti autenticati — incluso il deep linking diretto verso queste schermate.

Il posto più naturale dove inserire questa logica sarebbe il `_layout.tsx` radice: 
==si trova sopra a tutte le altre schermate, quindi il suo codice viene eseguito prima che qualsiasi schermata venga visualizzata.==
Tuttavia c'è un limite importante: 
- ==**al momento non è possibile usare `<Redirect>` nel file di layout radice**.==

La soluzione, come vedremo nella sezione successiva, passa ancora una volta per le [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Cartelle di raggruppamento|cartelle di raggruppamento]] — ==che ci permettono di introdurre un livello di layout intermedio dove inserire la logica di autenticazione.==

> [!hint] Questa limitazione del layout radice è temporanea — il supporto ai redirect nel file di layout radice è previsto in future versioni di Expo Router.


#### Strutturare le rotte protette

La soluzione è avvolgere tutte le schermate protette in una [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Cartelle di raggruppamento|cartella di raggruppamento]] `(protected)`, e spostare il layout radice un livello più in alto:
```css
app/
├── (protected)/
│   ├── (tabs)/
│   ├── modal.tsx
│   └── _layout.tsx   ← qui possiamo usare <Redirect>
├── login.tsx
└── _layout.tsx       ← layout radice (Stack Navigator)
```

Questo approccio risolve il problema in modo elegante: 
- ==il `_layout.tsx` dentro `(protected)` non è il layout radice, quindi è libero di usare `<Redirect>`.== 
Essendo il layout padre di tutte le schermate protette, il suo codice viene eseguito prima che qualsiasi schermata protetta venga visualizzata — incluse quelle raggiunte tramite deep link.

Allo stesso tempo, ==`login.tsx` si trova fuori da `(protected)`, quindi è accessibile senza autenticazione.== 
Aggiungere altre schermate pubbliche — registrazione, onboarding, recupero password — è semplice quanto aggiungere altri file allo stesso livello di `login.tsx`.

La struttura finale è:
```css
app/
├── (protected)/       ← solo utenti autenticati
│   ├── (tabs)/
│   ├── modal.tsx
│   └── _layout.tsx   ← controlla l'autenticazione e reindirizza
├── login.tsx          ← area pubblica
└── _layout.tsx        ← layout radice, gestisce solo lo Stack
```


>[!remember] **La cartella di raggruppamento `(protected)` non aggiunge nessun segmento al percorso URL:**
>==`(protected)/(tabs)` risponde esattamente agli stessi percorsi di prima.== 
>==La riorganizzazione è puramente strutturale e non impatta i percorsi esistenti né i deep link.==


### Aggiungere il reindirizzamento di autenticazione
#### Implementazione

Si crea la cartella `(protected)/` e si sposta tutto il contenuto esistente di `app/` al suo interno. La struttura risultante è:
```css
app/
├── (protected)/
│   ├── (tabs)/
│   │   ├── (home)/
│   │   ├── second/
│   │   ├── third.tsx
│   │   ├── fourth.tsx
│   │   └── _layout.tsx
│   ├── modal.tsx
│   ├── modal-with-stack/
│   └── _layout.tsx        ← vecchio layout radice, ora restituisce solo <Stack>
├── login.tsx
└── _layout.tsx            ← nuovo layout radice
```

Il nuovo root `_layout.tsx`  prende `StatusBar` e Tailwind dal vecchio layout e restituisce uno Stack Navigator:
```tsx
const RootLayout = () => {

    return (

        <>

            <StatusBar style='auto' />

            <Stack />

        </>

    );

};
```

Il vecchio `_layout.tsx` dentro `(protected)/` viene ripulito e restituisce semplicemente uno Stack:
```tsx
// app/(protected)/_layout.tsx
import { Stack } from 'expo-router';
import React from 'react';

export const unstable_settings = {
    initialRouteName: '(tabs)'
};

const ProtectedLayout = () => {
    return (
        <Stack>
            <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
            <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
            <Stack.Screen name='model-with-stack' options={{ presentation: 'modal', headerShown: false }} />
        </Stack>
    );
};

export default ProtectedLayout;
```

#### Creare la schermata di login

Si crea `login.tsx` direttamente dentro `app/` — fuori da `(protected)` — ==in modo che sia accessibile senza autenticazione==:
```tsx
// app/login.tsx
import { View, Text, StyleSheet } from 'react-native';
import React from 'react';

const Login = () => {
    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Login</Text>
        </View>
    );
};

export default Login;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    heading: {
        fontSize: 24,
        fontWeight: 'bold',
    }
});
```

Per ora è una schermata vuota — ==il contenuto reale (form, pulsanti, validazione) verrà aggiunto quando implementeremo la logica di autenticazione.== 
L'importante è che la rotta `/login` esista e sia raggiungibile.

> [!warning] **Dopo aver modificato la struttura del layout radice è consigliabile riavviare il bundler con `npx expo start --reset-cache` invece del semplice `npx expo start`** 
> il flag `--reset-cache` ==forza Metro a ricaricare completamente la struttura del filesystem, evitando comportamenti inattesi dovuti alla cache.==


> [!faq] `--reset-cache` vs `--clear`
> ono due flag simili ma con scope diverso:
>
>- `npx expo start --clear` — ==cancella solo la **cache di Metro** (il bundler JavaScript).== 
>>[!hint] ==È sufficiente nella maggior parte dei casi==, 
>>ad esempio dopo aver spostato file o modificato la struttura delle cartelle.
>
>- `npx expo start --reset-cache` — ==cancella la cache di Metro **e** quella di **Expo Go** e del progetto.==
>>[!fail] ==È più aggressivo e va usato quando `--clear` non risolve il problema,== 
>>ad esempio dopo modifiche al layout radice, aggiornamenti di dipendenze native, o comportamenti inspiegabili dell'app.
>
>>[!ticket] In generale: ==prova prima `--clear`, e se il problema persiste usa `--reset-cache`.==

Nel layout radice si aggiunge `(protected)` come `Stack.Screen` con `headerShown: false` per nascondere il titolo indesiderato:

```tsx
const RootLayout = () => {

    return (

        <>

            <StatusBar style='auto' />

            <Stack>

                <Stack.Screen name='(protected)' options={{ headerShown: false }} />

            </Stack>

        </>

    );

};
```

È lo stesso pattern già visto con [[Lezione 4 - Le modals#Expo Router Modal|(tabs)]] — ==ogni volta che una cartella di raggruppamento viene aggiunta a uno Stack Navigator, genera automaticamente un header con il suo nome.== 
==Nasconderlo è sempre necessario.==

#### Come si determina il percorso di una rotta

È utile capire come Expo Router converte la struttura del filesystem in percorsi URL, perché diventa sempre più importante man mano che la struttura dell'app cresce.

Partendo dal percorso assoluto del file, si applica questo processo in sequenza:

**1. Si elimina tutto ciò che precede `app/`**
```txt
src/app/(protected)/(tabs)/(home)/index.tsx
→ (protected)/(tabs)/(home)/index.tsx
```

**2. Si eliminano le cartelle di raggruppamento** — ==tutto ciò che è racchiuso tra parentesi non contribuisce al percorso:==
```txt
(protected)/(tabs)/(home)/index.tsx
→ index.tsx
```

**3. Si elimina `index`** — ==quando un file si chiama `index`, rappresenta la rotta radice di quella cartella. Non si può avere un file con nome vuoto, quindi `index` è la convenzione per indicare `/`==:
```txt
index.tsx
→ /
```

Il percorso finale è quindi `/` — ==la rotta radice dell'app, che corrisponde alla scheda Home del Tab Navigator.==

Applicando lo stesso ragionamento a un file più annidato:
```txt
src/app/(protected)/(tabs)/second/nested.tsx
→ second/nested.tsx   (rimosso il prefisso e i gruppi)
→ /second/nested      (percorso finale)
```

>[!hint] Ogni volta che non capisci quale percorso corrisponde a un file, applica queste tre regole in sequenza: 
>1. ==rimuovi il prefisso fino ad `app/`,== 
>2. ==rimuovi le cartelle tra parentesi,== 
>3. ==rimuovi `index`.== 
>Il risultato è sempre il percorso URL corrispondente.

#### Perché il layout radice non supporta i redirect

Quando l'app si avvia e tenta di caricare la rotta `/`, ==l'ordine di caricamento dei file segue la gerarchia del filesystem dall'alto verso il basso==:
```txt
app/_layout.tsx                        ← 1. layout radice
app/(protected)/_layout.tsx            ← 2. layout protetto
app/(protected)/(tabs)/_layout.tsx     ← 3. layout schede
app/(protected)/(tabs)/(home)/_layout.tsx  ← 4. layout home
app/(protected)/(tabs)/(home)/index.tsx    ← 5. schermata
```

**Il layout radice viene sempre renderizzato per primo e deve restituire un navigatore** — ==è lui che inizializza l'albero di navigazione dell'intera app.== 
Se invece restituisse un `<Redirect>`, ==l'albero di navigazione non verrebbe mai creato e l'app non avrebbe nessuna struttura su cui operare.==
```tsx
// ❌ non funziona nel layout radice
const RootLayout = () => {
    return <Redirect href='/login' />;  // l'albero di navigazione non esiste ancora
};

// ✅ corretto
const RootLayout = () => {
    return <Stack />;  // inizializza l'albero di navigazione
};
```


È per questo che la logica di autenticazione va inserita in `(protected)/_layout.tsx` e non nel layout radice — ==a quel punto l'albero di navigazione esiste già, il redirect ha un contesto in cui operare e può spostare l'utente verso `/login` senza problemi.==

> [!hint] Un modo semplice per ricordare questa regola: il layout radice **costruisce** l'albero di navigazione, tutti gli altri layout **operano** su di esso. Solo chi opera su un albero già esistente può usare i redirect.

Seguendo la catena di caricamento, ogni file di layout deve restituire un navigatore per permettere al livello successivo di essere visualizzato:
```scss
app/_layout.tsx              → <Stack>      ← inizializza l'albero
app/(protected)/_layout.tsx  → <Stack>      ← qui va la logica auth
app/(tabs)/_layout.tsx       → <Tabs>       ← schede in basso
app/(home)/_layout.tsx       → <Stack>      ← stack della scheda home
app/(home)/index.tsx         → schermata    ← finalmente visualizzata
```

Se uno qualsiasi di questi layout non restituisse un navigatore, la catena si interromperebbe e le schermate sotto di esso non verrebbero mai visualizzate.

Questo è esattamente il motivo per cui `(protected)/_layout.tsx` è **il posto giusto** per la logica di autenticazione: 
- ==sappiamo con certezza che il suo codice viene eseguito prima di qualsiasi schermata protetta, il layout radice ha già inizializzato l'albero di navigazione quindi i `redirect` funzionano, e tutte le schermate che vogliamo proteggere si trovano sotto di esso nella gerarchia.==

> [!example] **Pensa alla catena di layout come a una serie di cancelli:** 
> ==ogni cancello deve aprirsi — restituendo un navigatore — per permettere all'utente di passare al cancello successivo.== 
> Il cancello di `(protected)` è quello dove controlliamo il biglietto di autenticazione prima di far proseguire l'utente.


#### Aggiungere il redirect di autenticazione

Ora che sappiamo dove inserire la logica di autenticazione, implementiamo il `<Redirect/>` in `(protected)/_layout.tsx`. 
Per ora usiamo un valore statico per simulare lo stato di autenticazione:
```tsx
// app/(protected)/_layout.tsx
import { Redirect, Stack } from 'expo-router';
import React from 'react';

export const unstable_settings = {
    initialRouteName: '(tabs)'
};

const isLoggedIn: boolean = false;

const ProtectedLayout = () => {
    if (!isLoggedIn) {
        return <Redirect href='/login' />;
    }

    return (
        <Stack>
            <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
            <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
            <Stack.Screen name='model-with-stack' options={{ presentation: 'modal', headerShown: false }} />
        </Stack>
    );
};

export default ProtectedLayout;
```

La logica è un [[Lezione 2 - Usare lo stack navigator con Expo Router#Percorsi dinamici|early return]] — esattamente come il pattern già visto con `if (!proverb)` nella schermata dei proverbi: 
- ==se l'utente non è autenticato il componente restituisce subito il `<Redirect/>` e si ferma lì, senza mai renderizzare lo [[Lezione 2 - Usare lo stack navigator con Expo Router#Navigazione in uno stack|Stack Navigator]] e quindi senza mai dare accesso alle schermate protette.==

- `isLoggedIn = false` → ==redirect verso `/login`==
- `isLoggedIn = true` → ==Stack Navigator renderizzato, accesso alle schermate protette==

> [!hint] Notare che il redirect avviene **prima** che qualsiasi schermata protetta venga renderizzata — non si tratta di nascondere elementi UI, ma di bloccare completamente l'accesso alla rotta. Anche un deep link diretto verso una schermata protetta passerà per questo controllo e verrà reindirizzato a `/login`.


### Memorizzare lo stato di autenticazione 

Per rendere lo stato di autenticazione accessibile sia da `(protected)/_layout.tsx` che dalla schermata di login, abbiamo bisogno di un sistema di gestione dello stato condiviso. In questo caso usiamo **React Context**, che mantiene l'esempio indipendente da librerie esterne.

>[!tip] **State Management in React Native**  
React Context è la soluzione nativa di React per condividere dati tra componenti senza doverli passare manualmente attraverso le props. È perfetta per stati globali come l'autenticazione, il tema o le preferenze dell'utente.

Si crea il file `src/utils/authContext.tsx`:
```tsx
// src/utils/authContext.tsx
import { createContext, PropsWithChildren, useState } from "react";

// definisco la forma dello stato di autenticazione
type AuthState = {
    isLoggedIn: boolean;
    logIn: () => void;
    logOut: () => void;
};

// creo il context con i valori iniziali
// tutte le proprietà sono obbligatorie quindi devo passare un valore iniziale completo
export const AuthContext = createContext<AuthState>({
    isLoggedIn: false,
    logIn: () => {},
    logOut: () => {}
});

// esporto il provider che avvolgerà il layout radice
// PropsWithChildren tipizza automaticamente { children: React.ReactNode }
export function AuthProvider({ children }: PropsWithChildren) {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);

    const logIn = () => setIsLoggedIn(true);
    const logOut = () => setIsLoggedIn(false);

    return (
        <AuthContext.Provider value={{ isLoggedIn, logIn, logOut }}>
            {children}
        </AuthContext.Provider>
    );
}
```

Il context espone tre valori:
1. `isLoggedIn` per leggere lo stato, 
2. `logIn` e 
3. `logOut` per modificarlo. 
Qualsiasi componente avvolto nel provider può accedere a questi valori tramite `useContext(AuthContext)`.

> [!deep] `PropsWithChildren` è un tipo di React che aggiunge automaticamente `children: React.ReactNode` alle props del componente — 
> ==evita di doverlo dichiarare manualmente ogni volta che un componente deve accettare elementi figli.==


#### Connettere il Context all'app

Ora che il context è definito, dobbiamo collegarlo all'app in tre punti: il layout radice che avvolge tutto con il provider, il layout protetto che legge lo stato e gestisce il redirect, e la schermata di login che permette all'utente di autenticarsi.

##### Avvolgere l'app con `AuthProvider`

Il provider va inserito nel layout radice — il punto più alto della gerarchia — in modo che il context sia accessibile da qualsiasi componente dell'app:
```tsx
// app/_layout.tsx
const RootLayout = () => {
    return (
        <AuthProvider>
            <StatusBar style='auto' />
            <Stack>
                <Stack.Screen name='(protected)' options={{ headerShown: false }} />
                <Stack.Screen name='login' options={{ title: 'Login' }} />
            </Stack>
        </AuthProvider>
    );
};
```

#### Leggere il context in `(protected)/_layout.tsx`

Si sostituisce il valore statico `isLoggedIn` con il valore dinamico letto dal context tramite `useContext`. Il comportamento è identico a prima, ma ora il valore è reattivo — se cambia, il componente si ri-renderizza automaticamente:
```tsx
// app/(protected)/_layout.tsx
const ProtectedLayout = () => {
    const authState = useContext(AuthContext);

    if (!authState.isLoggedIn) {
        return <Redirect href='/login' />;
    }

    return (
        <Stack>
            <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
            <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
            <Stack.Screen name='model-with-stack' options={{ presentation: 'modal', headerShown: false }} />
        </Stack>
    );
};
```

##### Schermata di login

Nella schermata di login si legge il context e si collega il pulsante direttamente alla funzione `logIn` esposta dal provider:
```tsx
// app/login.tsx
const LoginScreen = () => {
    const authContext = useContext(AuthContext);

    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Login</Text>
            <Pressable style={styles.btn} onPress={authContext.logIn}>
                <Text style={styles.txtBtn}>Accedi!</Text>
            </Pressable>
        </View>
    );
};
```
##### Navigare dopo il login

C'è però un problema: 
==impostare `isLoggedIn` su `true` aggiorna il context ma non sposta automaticamente l'utente verso l'area protetta.== 
Bisogna navigare esplicitamente. 
==La soluzione è aggiungere [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`useRouter()`|`useRouter`]] direttamente dentro `AuthProvider`, in modo che la navigazione avvenga subito dopo l'aggiornamento dello stato==:
```tsx
// src/utils/authContext.tsx
export const AuthProvider = ({ children }: PropsWithChildren): ReactElement => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
    const router = useRouter();

    const logIn = () => {
        setIsLoggedIn(true);
        // replace invece di push: l'utente non può tornare alla schermata di login con Back
        router.replace('/');
    };

    const logOut = () => {
        setIsLoggedIn(false);
    };

    return (
        <AuthContext.Provider value={{ isLoggedIn, logIn, logOut }}>
            {children}
        </AuthContext.Provider>
    );
};
```

Si usa `router.replace('/')` invece di `router.push('/')` per lo stesso motivo già visto nella sezione [[Lezione 2 - Usare lo stack navigator con Expo Router#Sostituzione della schermata corrente|`replace`]]: ==dopo il login non vogliamo che l'utente possa tornare alla schermata di accesso tramite il gesto Back — la schermata di login deve sparire dallo stack.== 

#### Completare il flusso di autenticazione

##### Pulsante di logout

Si aggiunge un pulsante di logout nella schermata `fourth.tsx`, collegandolo alla funzione `logOut` esposta dal context:
```tsx
// app/(protected)/(tabs)/fourth.tsx
export default function FourthScreen() {
    const authState = useContext(AuthContext);
    const router = useRouter();

    return (
        <View style={styles.container}>
            <Text style={styles.heading}>Fourth Screen</Text>
            <Pressable style={styles.btnBack} onPress={() => router.back()}>
                <Text>Back</Text>
            </Pressable>
            <Pressable style={styles.btnLogOut} onPress={authState.logOut}>
                <Text style={styles.textBtn}>Log Out</Text>
            </Pressable>
        </View>
    );
}
```

##### Navigare verso il login dopo il logout

Analogamente a `logIn`, anche `logOut` deve navigare esplicitamente verso la schermata di login dopo aver aggiornato lo stato. Si aggiorna `authContext.tsx`:
```tsx
// src/utils/authContext.tsx
const logOut = () => {
    setIsLoggedIn(false);
    router.replace('/login');
};
```

In realtà questa navigazione avverrebbe automaticamente anche senza il `router.replace` — ==non appena `isLoggedIn` diventa `false`, `(protected)/_layout.tsx` si ri-renderizza e il redirect verso `/login` viene eseguito.== 
>[!ticket] Tuttavia è buona pratica essere espliciti, perché rende il flusso più chiaro e prevedibile.

##### Rimuovere le animazioni di transizione

L'animazione di scorrimento predefinita dello Stack Navigator non è naturale per i flussi di autenticazione — passare da login a home o viceversa con uno slide laterale appare strano. Si imposta `animation: 'none'` su entrambe le schermate nel layout radice:
```tsx
// app/_layout.tsx
const RootLayout = () => {
    return (
        <AuthProvider>
            <StatusBar style='auto' />
            <Stack>
                <Stack.Screen name='login' options={{ headerShown: false, animation: 'none' }} />
                <Stack.Screen name='(protected)' options={{ headerShown: false, animation: 'none' }} />
            </Stack>
        </AuthProvider>
    );
};
```

Il flusso completo ora funziona così:
```txt
App avviata
    ↓
(protected)/_layout.tsx controlla isLoggedIn
    ↓                        ↓
isLoggedIn = true      isLoggedIn = false
    ↓                        ↓
mostra le schede       redirect a /login
    ↓                        ↓
logout da fourth    pulsante login → logIn()
    ↓                        ↓
logOut() →           setIsLoggedIn(true)
setIsLoggedIn(false)  router.replace('/')
router.replace('/login')
```

>[!hint] **Usare `animation: 'none'` sulle transizioni di autenticazione è una convenzione consolidata nelle app mobile**
> ==Questo perché l'utente percepisce il login e il logout come un cambio di stato globale, non come una navigazione tra schermate.== 
> L'assenza di animazione rinforza questa percezione.



> [!deep] ##### Deep Dive: come funziona React context
> **Il problema del prop drilling**
> Per capire perché abbiamo bisogno di Context, vediamo cosa succederebbe se usassimo solo [[Lezione 3 - Hooks#Lo `useState()`|`useState`]]. 
> Dovremmo **passare lo stato manualmente attraverso ogni componente** (prop drilling):
>```tsx
> // ❌ ESEMPIO CON PROP DRILLING (da evitare)
>const App = () => {
>  const [isLoggedIn, setIsLoggedIn] = useState(false);
>  
>  return (
>    <ProtectedLayout 
>      isLoggedIn={isLoggedIn} 
>      setIsLoggedIn={setIsLoggedIn} 
>    />
>  );
>};
>
>const ProtectedLayout = ({ isLoggedIn, setIsLoggedIn }) => {
>  return (
>    <TabsNavigator 
>      isLoggedIn={isLoggedIn} 
>      setIsLoggedIn={setIsLoggedIn} 
>    />
>  );
>};
>
>const TabsNavigator = ({ isLoggedIn, setIsLoggedIn }) => {
>  return (
>    <>
>      <HomeScreen />
>      <FourthScreen 
>        isLoggedIn={isLoggedIn} 
>        setIsLoggedIn={setIsLoggedIn} 
>      />
>    </>
>  );
>};
>
>const FourthScreen = ({ isLoggedIn, setIsLoggedIn }) => {
>  // Finalmente posso usare lo stato!
>  const handleLogout = () => setIsLoggedIn(false);
>};
>```
>
>>[!failure] **Questo approccio è:**
>>
>>- **Ripetitivo**: ==devi passare le [[Lezione 2 - Il Props Object#Il Props Object|props]] attraverso ogni componente intermedio==
 >>   
>>- **Fragile**: ==se cambi la struttura, devi aggiornare tutte le [[Lezione 2 - Il Props Object#Il Props Object|props]]==
>>    
>>- **Difficile da manutenere**: ==difficile tracciare dove viene usato lo stato==
>
> Come React Context risolve il problema
>
>Con `useContext`, ==crei un **canale di comunicazione diretto** che bypassa la gerarchia dei componenti:==
>```tsx
>// ✅ CON CONTEXT
>const AuthContext = createContext<AuthState>(/* ... */);
>
>// Il provider si mette in alto
>const App = () => {
>  return (
>    <AuthProvider>  {/* ← Qui vive lo stato */}
>      <ProtectedLayout />  {/* Non riceve props! */}
>    </AuthProvider>
>  );
>};
>
>// Qualsiasi componente sotto il provider può "pescare" lo stato direttamente
>const FourthScreen = () => {
>  const authState = useContext(AuthContext);  // ← Pesca direttamente!
>  const handleLogout = () => authState.logOut();
>};
>```
>
>>[!faq] **Come funziona internamente**
>>1. **Il Provider** (`AuthProvider`) ==contiene lo stato (`useState`) e lo espone tramite la prop `value` del Context==
  >>  
>>2. **Il Consumer** (`useContext(AuthContext)`) ==si "abbona" al context e riceve il valore corrente==
  >>  
>>3. **Quando lo stato cambia** nel Provider, ==tutti i Consumer si ri-renderizzano automaticamente con il nuovo valore==
>
>>[!help] **Perché non possiamo usare solo useState nel layout radice**
>>
>>Potresti chiederti: "Perché non mettere `useState` in `_layout.tsx` e passarlo come props?"
>>```tsx
>>// ❌ Non funzionerebbe perché _layout.tsx è speciale
>>const RootLayout = () => {
>>    const [isLoggedIn, setIsLoggedIn] = useState(false);
>>    // Come passo queste props agli screen? 
>>    // <Stack.Screen /> non accetta props personalizzate!
>>};
>>```
>>
>>==I componenti dello Stack Navigator **non possono ricevere props direttamente** - è qui che `useContext` diventa essenziale.==
>>
##### Quando usare useContext vs altre soluzioni

| Scenario                                                                | Soluzione consigliata                  |
| ----------------------------------------------------------------------- | -------------------------------------- |
| **Stato condiviso tra molti componenti** (autenticazione, tema, lingua) | ✅ `useContext`                         |
| **Stato locale di un singolo componente** (input form, toggle)          | ✅ `useState`                           |
| **Stato che deve persistere tra schermate**                             | ✅ `useContext` (o Redux/Zustand)       |
| **Stato che cambia frequentemente** (animazioni)                        | ⚠️ `useState` (meglio per performance) |
| **Stato con logica complessa** (carrello, filtri)                       | ⚠️ `useReducer` o librerie esterne     |

### Mantenere lo stato di autenticazione nell'interazione nell'intera app 

Ora abbiamo memorizzato il nostro stato di accesso in questa variabile `useState`,
```tsx
const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
```
il che significa che si tratta di memoria temporanea; quindi, quando aggiorniamo l'app, il valore viene reimpostato a quello iniziale. Non è l'esperienza utente ideale per un'applicazione reale; vorremmo invece rendere persistente questo valore, ovvero salvarlo nella memoria del dispositivo.
Useremo un async storage 
```shell
npx expo install @react-native-async-storage/ async-storage
```
, supportato sia nelle build Expo che in quelle di sviluppo. Se state utilizzando una libreria di gestione dello stato come Relux Toolkit, YTI, Zustan o Legend State, tutte quelle moderne dispongono di adattatori per rendere persistente lo stato nella memoria del dispositivo.
Ora installiamo l'async storage e riavviamo il bundler; d'ora in poi, ogni volta che lo stato "all" viene aggiornato al momento dell'accesso o dell'uscita, vogliamo che venga salvato anche nell'async storage. Il mio stato "all" conterrà semplicemente un valore booleano che indica se siamo connessi o meno, poiché in realtà non mi sto collegando al back-end; tuttavia, nella realtà potresti memorizzare qui la data di scadenza del token "all", la data di aggiornamento o altri metadati.
```tsx
const storeAuthState = async (newState:{isLogged:boolean}) =>{

    }
```

Definiamo una chiave per il nostro storage: questa sarà la chiave con cui verrà memorizzato il nostro stato: 
```tsx
const authStorageKey: string = "auth-key";
```

È sempre consigliabile utilizzare un try-catch quando si interagisce con l’archiviazione asincrona. Ora dovremo convertire il nostro oggetto di stato di autenticazione in una stringa, poiché l’archiviazione asincrona accetta solo coppie chiave-valore di stringhe. Importeremo l’archiviazione asincrona e chiameremo `asyncStorage.setItem` con la chiave di archiviazione e il valore che vogliamo impostare.
```tsx
export const AuthProvider = ({ children }: PropsWithChildren): ReactElement => {

    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);

    const router = useRouter()

    const storeAuthState = async (newState: { isLogged: boolean }) => {

        try {

            const jsonValue = JSON.stringify(newState);

            await AsyncStorage.setItem(authStorageKey, jsonValue);

        } catch (error) {

            console.log(`Error saving: ${error}`);

        }

    }
```

Ora rendiamo asincrono l'archiviazione permanente dello stato di autenticazione ogni volta che si effettua l'accesso o l'uscita
```tsx
const logIn = () => {

        setIsLoggedIn(true);

        console.log(isLoggedIn)

        storeAuthState({ isLogged: true })

        router.replace("/")

    };

    const logOut = () => {

        setIsLoggedIn(false)

        console.log(isLoggedIn)

        storeAuthState({ isLogged: false })

        router.replace("/login")

    }
```

Ora dobbiamo anche recuperare correttamente questo valore iniziale al primo avvio dell'app; per farlo useremo un [[Lezione 4 - useEffect#Lo `useEffect`|`useEffect`]] di React con [[Lezione 4 - useEffect#Il dependency array|un array di dipendenze vuoto]] per recuperare gli elementi dall'archiviazione asincrona in modo asincrono, ma la funzione passata a `useEffect` è sincrona, quindi il modo per aggirare il problema è definire una funzione costante asincrona `getAll` dall’archivio e chiamarla in `useEffect` senza attendere il completamento.
Ora rendiamo asincrono l'accesso all'archivio persistente per lo stato di autenticazione ogni volta che si effettua l'accesso o l'uscita dall'app. Ora dobbiamo anche recuperare correttamente questo valore iniziale al primo avvio dell’app; per farlo useremo un `useEffect` di React con un array di dipendenze vuoto, che recupera gli elementi dall’archivio asincrono in modo asincrono, ma la funzione passata a `useEffect` è sincrona, quindi il modo per aggirare il problema è definire una funzione costante asincrona `getAll` dall’archivio e chiamarla in `useEffect` senza attendere il completamento. aggiungiamo un try-catch: è una buona pratica quando si lavora con l’archivio asincrono; chiameremo la funzione asincrona "getItem" dell’archivio e otterremo il valore memorizzato in corrispondenza della chiave che abbiamo impostato. Questo valore sarà `null` al primo avvio, ma in caso contrario ci aspettiamo che sia l’oggetto convertito in stringa che abbiamo salvato, quindi applicheremo il parsing JSON su di esso.
```tsx
useEffect(() => {

        const getAuthFromStorage = async () => {

            try {

                const value = await AsyncStorage.getItem(authStorageKey);

                if (value !==null){

                    const auth = JSON.parse

                }

            } catch (error) {

                console.log(`Error fetching from storage ${error}`)

            }

        };

        getAuthFromStorage();

    }, [])
```

