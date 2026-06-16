# Introduzione 
Nelle lezioni precedenti abbiamo esplorato i due navigatori fondamentali di Expo Router: 
1. lo [[Lezione 2 - Usare lo stack navigator con Expo Router|Stack Navigator]], ==che organizza la navigazione come una pila lineare di schermate,==  
2. il [[Lezione 3 - Utilizzo di un Tab Navigator con Expo Router|Tab Navigator]], ==che permette di passare tra sezioni principali dell'app tramite una barra delle schede.==
Abbiamo anche visto come i due si combinino in strutture ad albero, con stack annidati dentro le schede.

Esiste però un terzo pattern di navigazione che non si inserisce né in una pila né in una scheda: la **modal**. 
**Una modal è una schermata che si sovrappone al contenuto esistente senza sostituirlo** — ==l'utente la percepisce come un livello separato, temporaneo, che interrompe il flusso principale per richiedere un'azione o mostrare un'informazione.==

È il pattern che riconosci in moltissime app: ==il foglio che sale dal basso quando vuoi condividere un contenuto, il popup di conferma prima di eliminare qualcosa, il form di creazione rapida che si apre senza abbandonare la schermata corrente.==

Dal punto di vista tecnico, in Expo Router le modals sono schermate come tutte le altre — vivono nel filesystem sotto `app/` e si raggiungono tramite navigazione — ma vengono configurate con opzioni specifiche che ne modificano l'animazione e il comportamento di dismissione. La differenza non è strutturale ma di presentazione.

In questa lezione vedremo come creare e configurare modals, come gestirne la dismissione, e come integrarle correttamente con lo Stack Navigator e il Tab Navigator già visti.

##  Quando usare una Modal

Prima di implementare una modal tramite Expo Router, è utile valutare quale strumento si adatta meglio al caso d'uso. Expo Router non è l'unico modo per mostrare contenuto sovrapposto — esistono due alternative native che in molti casi sono più semplici e appropriate:
1. **`Alert`** — per conferme rapide e messaggi di sistema:
```tsx
import { Alert } from 'react-native';

Alert.alert(
    'Conferma eliminazione',
    'Sei sicuro di voler eliminare questo elemento?',
    [
        { text: 'Annulla', style: 'cancel' },
        { text: 'Elimina', style: 'destructive', onPress: () => deleteItem() }
    ]
);
```

È la scelta giusta quando hai bisogno di una risposta semplice dall'utente — sì/no, conferma/annulla — senza necessità di UI personalizzata.

**`Modal` di React Native** — per contenuto sovrapposto con stile custom:
```tsx
import { Modal } from 'react-native';

<Modal visible={isVisible} animationType="slide" transparent>
    <View style={styles.overlay}>
        <Text>Contenuto personalizzato</Text>
        <Button title="Chiudi" onPress={() => setIsVisible(false)} />
    </View>
</Modal>
```

==È la scelta giusta quando hai bisogno di un layout personalizzato ma vuoi gestire tutto localmente dentro il componente, senza coinvolgere il router.==

Entrambe queste opzioni possono essere attivate da qualsiasi schermata dell'app senza toccare la struttura di navigazione. 

> [!done] **La modal di Expo Router ha senso quando la schermata modale ha una propria rotta, deve essere raggiungibile tramite deep link, o deve contenere navigazione interna.**



| Strumento               | Quando usarlo                                                         |
| ----------------------- | --------------------------------------------------------------------- |
| `Alert`                 | conferme rapide, messaggi di sistema                                  |
| `Modal` di React Native | UI custom gestita localmente nel componente                           |
| Modal di Expo Router    | schermata modale con rotta propria, deep linking, navigazione interna |

### Alert 
Per conferme rapide si usa il componente [`Alert` di React Native](https://reactnative.dev/docs/alert), richiamabile da qualsiasi schermata senza toccare la struttura di navigazione.

La forma più semplice mostra solo un messaggio:
```tsx
const handleOpenAlert = () => {
    Alert.alert('Hello, World!');
};
```

`Alert.alert()` accetta fino a quattro argomenti:
```tsx
Alert.alert(title, message, buttons, options)
```
1. `title` — titolo del dialog, in grassetto
2. `message` — testo descrittivo sotto il titolo
3. `buttons` — array di oggetti che definiscono i pulsanti
4. `options` — opzioni aggiuntive specifiche per piattaforma

La forma completa:
```tsx
const handleOpenAlert = () => {
    Alert.alert('Warning!', 'Are you sure you want to proceed?', [
        {
            text: 'Cancel',
            style: 'cancel'
        },
        {
            text: 'Confirm',
            style: 'destructive',
            onPress: () => console.log("Let's go!")
        }
    ]);
};
```

##### Il terzo argomento: `buttons`

È un array di oggetti, ognuno dei quali rappresenta un pulsante con queste proprietà: 

| Proprietà     | Tipo                                         | Descrizione                                              |
| ------------- | -------------------------------------------- | -------------------------------------------------------- |
| `text`        | `string`                                     | testo del pulsante                                       |
| `style`       | `'default'` \| `'cancel'` \| `'destructive'` | stile visivo del pulsante                                |
| `onPress`     | ``() => void``                               | callback eseguita alla pressione                         |
| `isPreferred` | `boolean`                                    | evidenzia il pulsante come scelta consigliata (solo iOS) |

##### `style`
```tsx
{ text: 'Ok', style: 'default' }      // testo normale, colore di sistema
{ text: 'Annulla', style: 'cancel' }  // testo in grassetto, indica annullamento
{ text: 'Elimina', style: 'destructive' } // testo rosso, azione irreversibile
```

Su Android `style` ha meno impatto visivo rispetto a iOS — i pulsanti appaiono tutti simili indipendentemente dallo stile.


##### Numero di pulsanti
```tsx
// un solo pulsante → "Ok" di conferma
Alert.alert('Titolo', 'Messaggio', [
    { text: 'Ok' }
]);

// due pulsanti → layout affiancato, sinistra annulla destra conferma
Alert.alert('Titolo', 'Messaggio', [
    { text: 'Annulla', style: 'cancel' },
    { text: 'Conferma', style: 'destructive', onPress: () => deleteItem() }
]);

// tre pulsanti → layout verticale su iOS
Alert.alert('Titolo', 'Messaggio', [
    { text: 'Opzione A', onPress: () => console.log('A') },
    { text: 'Opzione B', onPress: () => console.log('B') },
    { text: 'Annulla', style: 'cancel' }
]);
```

>[!remember] Su Android il numero massimo di pulsanti è **tre** — oltre non vengono renderizzati.

###### `onPress` e pulsante senza callback

Se un pulsante non ha `onPress`, premendolo chiude semplicemente il dialog senza fare nulla:
```tsx
Alert.alert('Operazione completata', 'Il file è stato salvato.', [
    { text: 'Ok' } // nessun onPress → chiude e basta
]);
```


##### Il quarto argomento: `options`
```tsx
Alert.alert('Titolo', 'Messaggio', buttons, {
    cancelable: true,   // Android: chiude il dialog premendo fuori o il tasto Back
    onDismiss: () => {} // Android: callback eseguita quando il dialog viene chiuso senza premere nessun pulsante
});
```

Lo `style` del pulsante accetta tre valori: `default`, `cancel` e `destructive`. Quest'ultimo colora il pulsante di rosso su iOS per segnalare un'azione irreversibile.

>[!caution] **`cancelable` e `onDismiss` sono solo Android — su iOS il dialog può essere chiuso solo tramite uno dei pulsanti definiti nell'array.**
>
>`Alert` e il suo comportamento visivo sono **specifici per piattaforma** — ==su iOS appare come un popup centrato, su Android come un dialog nativo==. Non è possibile applicare stili personalizzati: 
>- ==se hai bisogno di un layout custom, la scelta giusta è la `Modal` di React Native o una modal di Expo Router.==

### React Native Modal 
Il componente `Modal` di React Native permette di: 
- ==creare finestre modali completamente personalizzabili.== 
[[#Alert|A differenza di `Alert`]], qui si ha pieno controllo sul layout e sullo stile.
La visibilità della modal viene gestita tramite uno [[Lezione 3 - Hooks#Lo `useState()`|`useState]]`: 
```tsx
const [modalVisible, setModalVisible] = useState<boolean>(false);
```

Il componente `Modal` si posiziona in fondo al JSX e riceve `visible` per controllarne la visibilità e `onRequestClose` come callback per chiuderla — quest'ultima viene chiamata quando l'utente preme il pulsante Back di Android o usa i gesti di dismissione:
```tsx
<Pressable style={styles.button} onPress={() => setModalVisible(true)}>
    <Text>Apri modale</Text>
</Pressable>

<Modal
    visible={modalVisible}
    onRequestClose={() => setModalVisible(false)}
>
    <View style={styles.modalOuter}>
        <View style={styles.modalInner}>
            <Text>A custom styled modal!</Text>
            <Pressable style={styles.button} onPress={() => setModalVisible(false)}>
                <Text>Chiudi</Text>
            </Pressable>
        </View>
    </View>
</Modal>
```

La struttura con **vista esterna e vista interna** è il pattern più comune: 
- ==la vista esterna centra il contenuto nello schermo, quella interna contiene il layout della modal con margini e sfondo.==
##### Opzioni di animazione e presentazione

Il comportamento visivo si controlla tramite tre prop principali:

**`animationType`** — definisce l'animazione di entrata:
```tsx
animationType="none"   // nessuna animazione (default)
animationType="fade"   // dissolvenza
animationType="slide"  // scivola dal basso
```

**`transparent`** — se `true`, ==lo sfondo della modal è trasparente e il contenuto sottostante rimane visibile==:

```tsx
<Modal
    visible={modalVisible}
    animationType="slide"
    transparent={true}
    onRequestClose={() => setModalVisible(false)}
>
```

**`presentationStyle`** — ==controlla lo stile di presentazione, con valori che replicano i pattern nativi di iOS==:
```tsx
presentationStyle="fullScreen"  // occupa tutto lo schermo
presentationStyle="pageSheet"   // foglio che sale dal basso, scorri verso il basso per chiudere
presentationStyle="formSheet"   // simile a pageSheet ma più stretto
```

> [!warning] `presentationStyle="pageSheet"` non funziona sul simulatore Android: 
> - ==è una funzionalità prevalentemente iOS.== 
> Il componente `Modal` funziona su entrambe le piattaforme, ma alcune opzioni di presentazione hanno comportamenti diversi o non supportati su Android.

> [!remember] `transparent={true}` e `presentationStyle` non vanno usati insieme  ==`presentationStyle` sovrascrive il comportamento di `transparent`.== 
> ==Se vuoi la modal trasparente con il contenuto sullo sfondo visibile, usa `transparent` senza `presentationStyle`.==


> [!deep] `onRequestClose` vs `onPress`
> Nell esempio abbiamo usato sia la prop `onRequestClose` di `<Modal>` che la prop `onPress` di `<Pressable>`, benché sembrano essere ridondanti, ed effettivamente lo sono, la loro applicazione dipende dalla piattaforma usata(Android o iOS). 
> 
> - `onRequestClose`:  ==viene chiamato quando l'utente preme il tasto fisico **Back** del dispositivo.== 
> 	- ==Su Android è **obbligatorio** (React Native mostra un warning se manca), anche se tecnicamente il modal non si chiude da solo senza che tu chiami `setModalVisible(false)` dentro.==
> 
>- `onPress` sul bottone: 
>	- Funziona su **tutte le piattaforme** (Android, iOS, Web)
>>[!example] Quindi:
>>
>>- Su **iOS** → ==puoi fare a meno di `onRequestClose` perché non esiste il tasto Back fisico==
>>- Su **Android** → ==è **consigliato tenerlo**, altrimenti il tasto Back hardware non fa nulla (o genera un warning) e l'utente rimane bloccato nel modal==
>>- Su **Web** → ==non ha effetto==

### Expo Router Modal 
Quando la modal deve essere una **rotta effettiva** dell'app — raggiungibile tramite navigazione, con un proprio percorso e potenzialmente con navigazione interna — né `Alert` né il componente `Modal` di React Native sono la scelta giusta.
In questo caso si usa Expo Router per definire la modal come schermata vera e propria.
##### Riorganizzare la struttura

Per far coesistere le schede in basso e la modal sotto lo stesso navigator, bisogna prima riorganizzare il filesystem. 
Le schede vengono raggruppate dentro una [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Cartelle di raggruppamento|cartella di raggruppamento]] `(tabs)`, e si aggiunge un nuovo layout radice che gestisce sia le schede che la modal:

```scss
app/
├── (tabs)/
│   ├── (home)/
│   ├── second/
│   ├── third.tsx
│   ├── fourth.tsx
│   └── _layout.tsx   ← restituisce <Tabs>
├── modal.tsx
└── _layout.tsx       ← restituisce <Stack> (nuovo layout radice)
```

Il nuovo `_layout.tsx` radice restituisce uno Stack Navigator e si occupa anche di `StatusBar` e Tailwind, che vengono spostati qui dal layout delle schede:
```tsx
// app/_layout.tsx
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import "../global.css";

const RootLayout = () => {
    return (
        <>
            <StatusBar style='auto' />
            <Stack>
                {/* nasconde l'header duplicato delle schede */}
                <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
                {/* definisce la modal come schermata con presentazione modale */}
                <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
            </Stack>
        </>
    );
};

export default RootLayout;
```

##### Creare e aprire la modal

`modal.tsx` è un componente normale:
```tsx
// app/modal.tsx
const Modal = () => {
    return (
        <View style={styles.container}>
            <Text>Modal</Text>
        </View>
    );
};
```

Si naviga verso di essa esattamente come verso qualsiasi altra schermata:
```tsx
// app/(tabs)/(home)/index.tsx
<Link href='/modal' push asChild>
    <Button title='Open router Modal' />
</Link>
```

La differenza rispetto a una schermata normale è tutta nell'opzione `presentation: 'modal'` definita nel layout radice — ==quella singola proprietà trasforma la transizione in un'animazione modale nativa con supporto al gesto di scorrimento verso il basso per chiuderla.==
```tsx
const RootLayout = () => {

    return (

        <>

            <StatusBar style='auto' />

            <Stack>

                <Stack.Screen name='(tabs)' options={{ headerShown: false }} />

                <Stack.Screen name='modal' options={{

                    presentation: 'modal'

                }} />

            </Stack>

        </>

    )

  

}
```

> [!hint] `presentation: 'modal'` 
> - ==su iOS produce l'animazione nativa a foglio che sale dal basso con il gesto di dismissione.== 
> - ==Su Android l'animazione è diversa ma comunque appropriata alla piattaform==a — Expo Router gestisce automaticamente le differenze.

> [!warning] Dopo aver riorganizzato il filesystem è necessario riavviare il bundler con `npx expo start` — le modifiche alla struttura delle cartelle non vengono rilevate automaticamente.

### Più schermate in una finestra modale 
ome abbiamo visto con le schede, anche una modal può contenere al suo interno uno Stack Navigator — permettendo di navigare in profondità senza uscire dalla modal stessa.

##### Struttura del filesystem

Si crea una cartella `modal-with-stack/` dentro `app/` con tre file:
```scss
app/
├── modal-with-stack/
│   ├── _layout.tsx   ← Stack Navigator interno alla modal
│   ├── index.tsx     ← schermata principale della modal
│   └── nested.tsx    ← schermata annidata
```

Il `_layout.tsx` restituisce semplicemente uno Stack Navigator:
```tsx
// app/modal-with-stack/_layout.tsx
import { Stack } from 'expo-router';

const Layout = () => {
    return <Stack />;
};

export default Layout;
```


Aggiungeremo anche un'altra schermata chiamata `nested.tsx`: 

```tsx
const NestedScreen = () => {

  return (

    <View style={styles.container}>

      <Text>Nested Screen</Text>

    </View>

  );

};
```

##### Configurare la modal nel layout radice

Nel `_layout.tsx` radice si aggiunge la nuova schermata con `presentation: 'modal'`, esattamente come per la modal semplice:
```tsx
// app/_layout.tsx
const RootLayout = () => {
    return (
        <>
            <StatusBar style='auto' />
            <Stack>
                <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
                <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
                <Stack.Screen name='modal-with-stack' options={{ presentation: 'modal' }} />
            </Stack>
        </>
    );
};
```


##### Navigazione interna alla modal

`modal-with-stack/index.tsx` naviga verso la schermata annidata tramite il suo percorso assoluto:
```tsx
// app/modal-with-stack/index.tsx
const ModalWithStack = () => {
    return (
        <View>
            <Text>ModalWithStack</Text>
            <Link href='/modal-with-stack/nested' push asChild>
                <Button title='Push to nested' />
            </Link>
        </View>
    );
};
```

##### Aprire la modal dalla homepage

Dalla schermata `(home)/index.tsx` si aggiunge un link verso la nuova modal, esattamente come per qualsiasi altra schermata:
```tsx
import { Stack } from 'expo-router'
<Link href='/modal-with-stack' push asChild>
    <Button title="Apri la Router Modal con Stack" />
</Link>
```

Il risultato è una modal che si apre con l'animazione nativa e al suo interno permette di navigare tra `index` e `nested` tramite il proprio Stack Navigator — il tutto senza abbandonare il contesto modale.

> [!hint] Il pattern "modal con stack interno" è comune nelle app reali quando la modal rappresenta un flusso multi-step
>  ==ad esempio un processo di checkout, un wizard di configurazione, o un form a più pagine.== 
>  **L'utente percepisce l'intera sequenza come un'esperienza temporanea sovrapposta all'app principale.**

### Deep Linking in una finestra modale 


Aprendo la modal tramite deep link — cioè navigando direttamente verso `/modal` senza passare prima dalle schede — si nota un problema: 
- ==la modal si apre correttamente, ma **le schede in background non vengono caricate**.== 
Chiudendo la modal non c'è nulla a cui tornare.

Il motivo è che il layout radice è uno Stack Navigator, e quando si accede direttamente a una schermata dello stack tramite deep link, quella schermata diventa la prima — e unica — nello stack. Le schede non vengono mai inizializzate perché non ci si è passati prima.

##### `unstable_settings`

La soluzione è esportare una costante speciale chiamata `unstable_settings` nel file del layout radice, impostando `initialRouteName` su `(tabs)`:
```tsx
// app/_layout.tsx
export const unstable_settings = {
    initialRouteName: '(tabs)'
};

const RootLayout = () => {
    return (
        <>
            <StatusBar style='auto' />
            <Stack>
                <Stack.Screen name='(tabs)' options={{ headerShown: false }} />
                <Stack.Screen name='modal' options={{ presentation: 'modal' }} />
                <Stack.Screen name='modal-with-stack' options={{ presentation: 'modal', headerShown: false }} />
            </Stack>
        </>
    );
};
```



Questo dice allo Stack Navigator che:
- ==`(tabs)` è sempre la schermata di base==
- ==anche quando si accede direttamente a una schermata diversa tramite deep link.== 
- ==Il navigator caricherà prima le schede in background e poi aprirà la modal sopra di esse. Chiudendo la modal, le schede sono già pronte.==

> [!warning] Il nome `unstable_settings` può sembrare allarmante ma è perfettamente utilizzabile in produzione. 
> ==Il prefisso `"unstable"` indica solo che il nome della proprietà potrebbe cambiare in future versioni di Expo Router — è già prevista la rinomina in `anchors`.== 
> Il comportamento in sé è stabile e affidabile.

> [!hint] `initialRouteName` non cambia la schermata che viene mostrata per prima all'utente — cambia solo quale schermata viene caricata come **base dello stack** quando si accede tramite deep link. L'utente vedrà comunque la modal aprirsi, ma con le schede già pronte in background

