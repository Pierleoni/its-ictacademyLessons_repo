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

##### Il problema della memoria temporanea

Lo `useState` che abbiamo usato finora è **memoria temporanea:** 
```tsx
const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
```

==ogni volta che l'app viene riavviata, `isLoggedIn` torna al suo valore iniziale `false`, costringendo l'utente a fare login ogni volta.== Non è l'esperienza utente ideale — in un'app reale ci si aspetta di rimanere autenticati finché non si effettua esplicitamente il logout.

Per risolvere questo problema bisogna rendere persistente il valore nella memoria del dispositivo. La soluzione è **AsyncStorage**, installabile tramite:
```shell
npx expo install @react-native-async-storage/ async-storage
```

>[!info] Se stai usando una libreria di gestione dello stato come Redux Toolkit, Zustand o Legend State, tutte le librerie moderne dispongono di adattatori nativi per la persistenza — in quel caso non hai bisogno di gestire AsyncStorage manualmente.


##### Salvare lo stato nell'AsyncStorage

`AsyncStorage` funziona come un dizionario persistente sul dispositivo: 
- ==salva e legge coppie chiave-valore, ma accetta **solo stringhe**.== 
==Questo significa che qualsiasi oggetto va serializzato con `JSON.stringify` prima di salvarlo, e deserializzato con `JSON.parse` quando lo si rilegge.== 

Definiamo una chiave univoca per identificare il nostro valore in storage e una funzione asincrona per il salvataggio:
```tsx
// src/utils/authContext.tsx
const authStorageKey: string = "auth-key";

const storeAuthState = async (newState: { isLogged: boolean }) => {
    try {
        const jsonValue = JSON.stringify(newState);
        await AsyncStorage.setItem(authStorageKey, jsonValue);
    } catch (error) {
        console.log(`Error saving: ${error}`);
    }
};
```


Si chiama `storeAuthState` ogni volta che lo stato cambia, sia dentro `logIn` che dentro `logOut`:
```tsx
const logIn = () => {
    setIsLoggedIn(true);
    storeAuthState({ isLogged: true });
    router.replace('/');
};

const logOut = () => {
    setIsLoggedIn(false);
    storeAuthState({ isLogged: false });
    router.replace('/login');
};
```

In questo modo ogni cambio di stato viene immediatamente scritto su disco e sopravvive al riavvio dell'app.
##### Recuperare lo stato al primo avvio

Salvare non è sufficiente — bisogna anche **leggere** il valore salvato quando l'app si avvia. Si usa un [[Lezione 4 - useEffect#Lo `useEffect`|`useEffect`]] con [[Lezione 4 - useEffect#Il dependency array|array di dipendenze vuoto]] — ==viene eseguito una sola volta al montaggio del componente==, esattamente quello che vogliamo per l'inizializzazione.

**`useEffect` accetta solo funzioni sincrone**, ==quindi si definisce una funzione asincrona interna e la si chiama immediatamente== — è il pattern standard per usare `async/await` dentro un `useEffect`:

```tsx
useEffect(() => {
    const getAuthFromStorage = async () => {
        try {
            const value = await AsyncStorage.getItem(authStorageKey);
            if (value !== null) {
                // JSON.parse riconverte la stringa nell'oggetto originale
                const auth = JSON.parse(value);
                setIsLoggedIn(auth.isLogged);
            }
        } catch (error) {
            console.log(`Error fetching from storage: ${error}`);
        }
        // indipendentemente dal risultato, lo stato è ora determinato
        setIsReady(true);
    };

    getAuthFromStorage();
}, []);
```

`setIsReady(true)` viene chiamato **fuori dal blocco `if`**, dopo il `try-catch` — questo garantisce che `isReady` diventi `true` indipendentemente da ciò che è successo: 
- ==sia che abbiamo trovato un valore salvato, sia che fosse il primo avvio, sia che ci sia stato un errore.==
##### Il problema dello stato indeciso

C'è però un problema sottile: ==la lettura da AsyncStorage è asincrona==. 
Al primo render, `isLoggedIn` è `false` e `(protected)/_layout.tsx` eseguirebbe immediatamente il [[Lezione 3 - Utilizzo di un Tab Navigator con Expo Router#2. Redirect in `index.tsx`|redirect]] verso `/login` — prima ancora che AsyncStorage abbia restituito il valore reale. 
Un utente già autenticato verrebbe rimandato al login ad ogni avvio.

La soluzione è aggiungere una variabile `isReady` che segnala se lo stato di autenticazione è stato determinato o è ancora in corso di lettura:
```tsx
// src/utils/authContext.tsx
type AuthState = {
    isLoggedIn: boolean;
    isReady: boolean;      // true solo dopo aver letto AsyncStorage
    logIn: () => void;
    logOut: () => void;
};

export const AuthContext = createContext<AuthState>({
    isLoggedIn: false,
    isReady: false,
    logIn: () => {},
    logOut: () => {}
});

export const AuthProvider = ({ children }: PropsWithChildren): ReactElement => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
    const [isReady, setIsReady] = useState<boolean>(false);
    const router = useRouter();

    // ...

    return (
        <AuthContext.Provider value={{ isLoggedIn, isReady, logIn, logOut }}>
            {children}
        </AuthContext.Provider>
    );
};
```

In `(protected)/_layout.tsx` si aggiunge un controllo su `isReady` **prima** del redirect — ==se lo stato non è ancora determinato, si restituisce `null` per non renderizzare nulla e attendere==:
```tsx
// app/(protected)/_layout.tsx
const ProtectedLayout = () => {
    const authState = useContext(AuthContext);

    // stato ancora indeciso → non renderizzare nulla e aspettare
    if (!authState.isReady) {
        return null;
    }

    // stato determinato → controlla autenticazione
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

Il flusso al primo avvio diventa:
```css
App avviata
    ↓
isReady = false → return null (nessun redirect prematuro)
    ↓
AsyncStorage legge il valore salvato
    ↓
setIsLoggedIn(valore salvato) + setIsReady(true)
    ↓
re-render di ProtectedLayout
    ↓                        ↓
isLoggedIn = true      isLoggedIn = false
    ↓                        ↓
mostra le schede       redirect a /login
```



Per capire meglio la sequenza di render, aggiungendo dei `console.log` si vede chiaramente cosa succede:
```tsx
console.log(`isReady ${authState.isReady}`)
console.log(`isReady ${authState.isReady}`)
```

```shell
LOG  isReady: false   ← primo render, AsyncStorage non ha ancora risposto
LOG  isLoggedIn: false
LOG  isReady: true    ← secondo render, AsyncStorage ha risposto
LOG  isLoggedIn: true ← ora il valore reale è disponibile
```

Senza `isReady`, al primo render il redirect verso `/login` verrebbe eseguito immediatamente e `ProtectedLayout` non verrebbe mai ri-renderizzato con il valore corretto. 
Con `isReady`, invece, il layout aspetta che AsyncStorage abbia risposto prima di prendere qualsiasi decisione di navigazione.

> [!hint] Restituire `null` da un componente React è perfettamente valido —  
> ==dice a React di non renderizzare nulla per quel componente.==  
> ==È la soluzione più pulita per gestire gli stati di caricamento iniziale senza mostrare flash di contenuto indesiderato.== In un'app reale, al posto di `null` si potrebbe restituire uno splash screen o un indicatore di caricamento.


### Mostrare la schermata iniziale mentre l'autenticazione è indecisa

##### Il problema

Restituire `null` mentre `isReady` è `false` funziona correttamente — nessun redirect prematuro — ma produce un'esperienza visiva non ideale: 
- ==l'utente vede una **schermata vuota** per il tempo necessario a determinare lo stato di autenticazione.==

In uno scenario reale questo tempo potrebbe non essere trascurabile — ad esempio se bisogna effettuare una chiamata [[Lezione 6 - API#API (Application Programming Interface)|API]] per verificare o aggiornare un [[JWT - JSON Web Token#Cosa sono i JWT|token JWT]]. 
Per simulare questo caso aggiungiamo un ritardo artificiale di 1 secondo nel `useEffect`: 

```tsx
useEffect(() => {
    const getAuthFromStorage = async () => {
        // simulo un'operazione lenta (es. chiamata API per refresh token)
        await new Promise((res) => setTimeout(() => res(null), 1000));

        try {
            const value = await AsyncStorage.getItem(authStorageKey);
            if (value !== null) {
                const auth = JSON.parse(value);
                setIsLoggedIn(auth.isLogged);
            }
        } catch (error) {
            console.log(`Error fetching from storage: ${error}`);
        }

        setIsReady(true);
    };

    getAuthFromStorage();
}, []);
```

Con questo ritardo, al riavvio dell'app si vede chiaramente il problema: 
- ==la splash screen scompare, appare una schermata nera vuota per un secondo, e solo dopo compare l'app.== 
Non è un'esperienza accettabile.

##### La soluzione: mantenere la splash screen visibile

Il pattern consolidato per gestire questa situazione è: 
- ==**mantenere la splash screen visibile** finché lo stato di autenticazione non è determinato, nascondendola solo quando `isReady` diventa `true`.== 
Expo mette a disposizione `SplashScreen` proprio per questo scopo.

In cima ad `authContext.tsx` si chiama `SplashScreen.preventAutoHideAsync()` — questa istruzione va eseguita il prima possibile, fuori da qualsiasi componente, in modo che la splash screen rimanga visibile fin dall'avvio:
Ora, nella parte superiore del contesto di autenticazione (`src/utils/authContext.tsx`), chiamiamo `SplashScreen.preventAutoHideAsync`: 
```tsx
// src/utils/authContext.tsx
import * as SplashScreen from 'expo-splash-screen';

// impedisce alla splash screen di nascondersi automaticamente
SplashScreen.preventAutoHideAsync();
```
Poi si aggiunge un secondo `useEffect` con `isReady` nell'array delle dipendenze — ==viene eseguito ogni volta che `isReady` cambia, e nasconde la splash screen non appena lo stato è determinato==:
```tsx
useEffect(() => {
    if (isReady) {
        SplashScreen.hideAsync();
    }
}, [isReady]);
```

> [!FAQ] **Perché due `useEffect` separati?**
>  
> 
> Si potrebbe pensare di chiamare `SplashScreen.hideAsync()` direttamente dentro `getAuthFromStorage`, subito dopo `setIsReady(true)`. Funzionerebbe, ma separare le responsabilità è una pratica migliore:
> 
> - il primo `useEffect` si occupa esclusivamente di **leggere lo stato da AsyncStorage**
> - il secondo `useEffect` si occupa esclusivamente di **gestire la splash screen** in risposta al cambiamento di `isReady`
> 
> Questo rende il codice più leggibile e più facile da modificare in futuro — se in futuro `isReady` dipendesse da più condizioni, la logica della splash screen non andrebbe toccata.

Il flusso completo al primo avvio diventa:
```text
App avviata
    ↓
SplashScreen.preventAutoHideAsync() → splash screen bloccata
    ↓
isReady = false → ProtectedLayout restituisce null
    ↓
AsyncStorage legge il valore (o attende la chiamata API)
    ↓
setIsLoggedIn(valore) + setIsReady(true)
    ↓
useEffect([isReady]) → SplashScreen.hideAsync()
    ↓
re-render di ProtectedLayout
    ↓                        ↓
isLoggedIn = true      isLoggedIn = false
    ↓                        ↓
mostra le schede       redirect a /login
```

>[!hint] `SplashScreen.preventAutoHideAsync()` va chiamato il prima possibile nel ciclo di vita dell'app — ==idealmente al livello più alto del modulo, fuori da qualsiasi componente o hook.== 
>Se viene chiamato troppo tardi, la splash screen potrebbe già essersi nascosta automaticamente prima che l'istruzione venga eseguita.