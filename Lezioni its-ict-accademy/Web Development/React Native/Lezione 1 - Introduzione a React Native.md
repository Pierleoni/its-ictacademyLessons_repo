
# Introduzione: Cos'è React Native
Grazie a **[[Lezione 7; React#Cos'è React|React JS]]** e **[[#Cos’è React Native (logica dell’applicazione)|React Native]]** è possibile sviluppare applicazioni mobili **native** per **iOS** e **Android**, non semplici web app o siti ottimizzati per dispositivi mobili.  
==Le applicazioni create con React Native sono app reali, installabili sui dispositivi e distribuibili tramite gli store ufficiali, come **App Store** e **Google Play**,== esattamente come quelle sviluppate con tecnologie native.

L’aspetto più rilevante di React Native è che, pur consentendo lo sviluppo di app native, ==utilizza **[[Lezione 1 I fondamenti Javascript|JavaScript]]** come linguaggio principale, lo stesso impiegato nello sviluppo web.== 
Questo permette di riutilizzare gran parte delle logiche applicative e della sintassi di **React JS**, riducendo la curva di apprendimento per chi proviene dal mondo web.

React Native mette a disposizione componenti e **[[Lezione 6 - API#API (Application Programming Interface)|API]]** specifiche per l’interazione diretta con il **sistema operativo** del dispositivo, consentendo l’accesso a funzionalità hardware e di sistema come fotocamera, GPS, notifiche, vibrazione, memoria locale e molto altro.

In questo senso, React Native rappresenta una vera e propria **fusione tra sviluppo web e sviluppo nativo**:

- ==consente di scrivere **un’unica base di codice** in **JavaScript e JSX**;==
    
- ==traduce le interfacce in **componenti nativi reali**, garantendo prestazioni e comportamenti paragonabili a quelli di applicazioni sviluppate direttamente in **Swift** (iOS) o **Kotlin/[[Lezione 1 I fondamenti Javascript|Java]]** (Android).==

## React JS 

**React.js** è una libreria JavaScript progettata per la costruzione di **interfacce utente**. 
È utilizzata principalmente nello sviluppo web, ed è per questo motivo che, in questo contesto, viene affiancata da **[[Lezione 7; React#^ed66ba|React DOM]]**, la libreria che funge da collegamento tra React e il browser.

È importante sottolineare che **React, di per sé, è piattaforma-agnostico**: 
- ==non è legato a un ambiente specifico e non conosce direttamente né il [[DOM|DOM]] del browser né le [[Lezione 6 - API#API (Application Programming Interface)|API]] di un sistema operativo==. 
- Il suo compito si limita a:

	- ==gestire lo **[[Lezione 7; React#Il concetto di stato in React|stato]]** e il ciclo di vita dei componenti;==
    
	- ==costruire un **[[Lezione 7; React#^ed66ba|Virtual DOM]]**, ovvero una rappresentazione virtuale dell’interfaccia utente;==
    
	- ==calcolare in modo efficiente le **modifiche** da applicare all’interfaccia in seguito a un aggiornamento dello stato.==
    

Per trasformare questa rappresentazione astratta in elementi concreti e visibili all’utente è necessario un **livello di integrazione con la piattaforma di destinazione**, spesso definito come un “ponte” (_bridge_).

Nel contesto web, questo ruolo è svolto da **React DOM**, che traduce i componenti React in **elementi HTML reali**, inserendoli e aggiornandoli all’interno del DOM del browser.
```jsx
// Esempio con React DOM (sviluppo web)
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

```

Questa separazione tra **logica di rendering** (React) e **piattaforma di destinazione** (React DOM per il web, React Native per il mobile) è ciò che rende possibile riutilizzare gli stessi concetti, la stessa sintassi e gran parte delle stesse logiche applicative in ambienti differenti.
## React Native 
**React Native** estende il modello concettuale di React sostituendo **React DOM** con un diverso livello di integrazione verso la piattaforma di destinazione: 
- il **mondo mobile**.  
In questo caso, il “ponte” non è il browser, ma i **sistemi operativi mobili** (iOS e Android).

React Native fornisce un insieme di **[[Lezione 1- Componenti Funzionali in React React|componenti]] React specifici**, progettati per mappare direttamente i **controlli nativi** delle piattaforme mobili. 
==Questi componenti non generano HTML, ma vengono tradotti in elementi UI nativi reali.==

Inoltre, React Native espone **[[Lezione 6 - API#API (Application Programming Interface)|API]] di piattaforma** accessibili da JavaScript, che consentono di interagire con funzionalità del dispositivo come fotocamera, sensori, memoria locale, vibrazione e notifiche.
```jsx
// Esempio con React Native
import { Text, View } from 'react-native';
export default function App() {
	return (
		<View>
			<Text>Benvenuti in React Native!</Text>
		</View>
	);
}
```

In questo caso, `<View>` e `<Text>`: 
- ==non sono tag HTML ma componenti nativi che verranno tradotti rispettivamente in un UIView (su iOS) e in un TextView (su Android).==
In React Native, noi scriviamo il codice dell’app in JavaScript e JSX, esattamente come faremmo in React per il web. 
Tuttavia, anche se la sintassi è simile, il risultato finale è completamente diverso: 
- ==non viene generato HTML, ma un’app nativa per Android e iOS.==
Il codice che scriviamo può apparire così:
```JSX
const App = (props) => {
	return (
		<View>
			<Text>Hello there!</Text>
		</View>
	);
};
```

==In questo esempio, `<View>` e `<Text>` **non sono elementi HTML**, ma componenti forniti da React Native.== 
Essi vengono tradotti, a runtime, nei corrispettivi componenti nativi della piattaforma:

- su **iOS**, `<View>` diventa un `UIView` e `<Text>` un controllo testuale nativo;
    
- su **Android**, `<View>` diventa un `android.view.View` e `<Text>` un `TextView`.
    

Dal punto di vista dello sviluppatore, il codice viene scritto in **JavaScript e JSX**, esattamente come in React per il web. 
Tuttavia, il risultato finale è completamente diverso:

- ==**non viene generato HTML**;==
    
- ==viene invece prodotta un’**applicazione nativa** per iOS e Android.==
    

Un componente React Native può essere definito, ad esempio, come segue:

```jsx
const App = (props) => {
  return (
    <View>
      <Text>Hello there!</Text>
    </View>
  );
};

```

Qui viene definito un **componente funzionale** che restituisce JSX.  
Sebbene `<View>` e `<Text>` ricordino visivamente i tag HTML, il loro significato è diverso: 
- ==sono **astrazioni** che React Native utilizza per creare le corrispondenti viste native della piattaforma.==

#### Separazione tra UI e logica

In un’applicazione React Native è fondamentale distinguere due livelli che coesistono:

1. **Interfaccia utente (UI Elements)**  
    - ==I componenti JSX (`<View>`, `<Text>`, `<TextInput>`, ecc.) rappresentano la parte visiva dell’app.==  
    - ==Questi componenti vengono **tradotti in controlli nativi** specifici per iOS e Android.==
    
2. **Logica applicativa (Logic)**  
    - ==Tutto il codice JavaScript che gestisce stato, condizioni, funzioni, eventi e hook (come [[Lezione 3 - Hooks#Lo `useState()`|`useState`]] e [[Lezione 4 - useEffect#Lo `useEffect`|`useEffect`]]) **non viene compilato in codice nativo**, ma viene eseguito come JavaScript, in un thread dedicato gestito da React Native.==
    

In altre parole:

- ==il **JSX** viene trasformato in **viste native**;==
    
- ==la **logica** rimane JavaScript ed è semplicemente eseguita.==
####  Corrispondenza tra web e mobile

Nel web, con React, si utilizzano elementi HTML come `<div>` e `<input>`.  
Nel mondo mobile, tali elementi non esistono: ogni piattaforma possiede i propri componenti nativi.

React Native fornisce quindi **componenti astratti** che fungono da equivalenti multipiattaforma:

- `<div>` → `<View>`
    
- `<input>` → `<TextInput>`
    

React Native si occupa automaticamente di tradurre questi componenti:

- `<View>` → `UIView` (iOS) / `android.view.View` (Android)
    
- `<TextInput>` → `UITextField` (iOS) / `EditText` (Android)
    

Grazie a questo meccanismo, è possibile scrivere **un’unica base di codice**, utilizzando un solo linguaggio e un solo set di componenti, ottenendo interfacce **completamente native**, con prestazioni e comportamento paragonabili a quelli di applicazioni sviluppate direttamente in **Swift** o **Kotlin**.

##### Schema concettuale

```text
UI Elements (JSX)
↓
Componenti esposti da React Native
↓
Traduzione in viste native (iOS / Android)

```


### Cos’è React Native (logica dell’applicazione)

Accanto alla parte visiva dell’applicazione, in React Native è presente la **logica applicativa:** 
- ==che comprende la gestione dello stato, le funzioni, le condizioni, gli eventi e le operazioni di accesso ai dati.==  
Questa logica viene **scritta interamente in JavaScript** e ==**non viene compilata in codice nativo**.==

Il codice JavaScript viene eseguito all’interno di un **thread JavaScript dedicato**, gestito direttamente da React Native e incluso come parte integrante dell’applicazione nativa finale.
```text
Logic
↓
Scritta dallo sviluppatore in JavaScript
↓
Eseguita in un JavaScript thread dell’app React Native
↓
Non compilata in codice nativo
```
Durante la fase di build, React Native configura un ambiente di esecuzione che include un **motore JavaScript** (come **Hermes** o **JavaScriptCore**).  
Questo motore ha il compito di: 
- ==interpretare ed eseguire la logica dell’applicazione, mantenendo separata l’esecuzione del codice dalla gestione diretta dell’interfaccia nativa.==

La comunicazione tra la **logica JavaScript** e la **parte nativa** avviene tramite un meccanismo chiamato **bridge:** 
- ==Il bridge rappresenta un canale di comunicazione che consente al codice JavaScript di inviare istruzioni alla piattaforma nativa e di ricevere risposte in modo controllato.==

Attraverso il bridge, la logica JavaScript può, ad esempio:

- ==richiedere la creazione di una nuova `<View>`;==
    
- ==aggiornare il contenuto di un `<Text>`;==
    
- ==accedere a una API nativa, come la fotocamera o la memoria del dispositivo.==
    

React Native si occupa quindi di **tradurre queste istruzioni astratte** in operazioni concrete sul sistema operativo, convertendole nei corrispondenti comandi nativi per iOS o Android.

In sintesi, React Native mantiene una netta separazione tra:

- ==**UI**, che viene tradotta in viste native;==
    
- ==**logica**, che rimane JavaScript ed è eseguita da un motore dedicato.==
    

Questa architettura consente di combinare la flessibilità dello sviluppo in JavaScript con le prestazioni e il comportamento di un’applicazione nativa

### Creazione del progetto con Expo
Dopo aver chiarito come React Native separi **interfaccia nativa** e **logica JavaScript**, è possibile passare alla fase operativa, ovvero alla **creazione di un nuovo progetto** e alla scelta dell’ambiente di sviluppo.

La documentazione ufficiale di React Native propone due modalità principali per avviare un’applicazione:

- **Expo CLI**
    
- **React Native CLI**
    

Entrambi sono strumenti da riga di comando (_Command Line Interface_): 
- ==utilizzati per creare, avviare e gestire progetti React Native, ma adottano approcci differenti in termini di configurazione e controllo sul codice nativo.==

#### 1. Creazione del progetto con Expo

**Expo** è: 
- ==una piattaforma gratuita che fornisce un ambiente di sviluppo **gestito** (_managed workflow_), pensato per semplificare l’avvio di un progetto React Native.==  
Si occupa automaticamente della configurazione dell’ambiente nativo, consentendo allo sviluppatore di concentrarsi principalmente sul codice JavaScript e sull’interfaccia dell’app.

Per creare un nuovo progetto con Expo si utilizzano i seguenti comandi:
```shell
npx create-expo-app NomeProgetto --template blank
cd NomeProgetto
npx expo start
```

1.   `npx create-expo-app NomeProgetto --template blank` : 
	- ==crea la struttura di base del progetto.==
    
2. `cd NomeProgetto`: 
	-  ==sposta la shell all’interno della cartella del progetto.==
    
3. `npx expo start`: 
	- ==avvia il **server di sviluppo**, permettendo di eseguire e testare l’app in tempo reale tramite un emulatore o un dispositivo fisico usando l’app **Expo Go**.==
Grazie a questo approccio, l’ambiente JavaScript, il bridge e l’accesso alle API native vengono configurati automaticamente, senza richiedere interventi manuali sul codice nativo.

> [!faq] Perché scegliere Expo
> Expo è particolarmente indicato nelle fasi iniziali dello sviluppo perché riduce drasticamente la complessità del setup.  
Offre un ambiente di sviluppo gestito in cui molte dipendenze native sono già pronte all’uso.
>
>In particolare:
>
>- è gratuito e non richiede registrazione;
  >  
>- evita la configurazione manuale di Android Studio e Xcode;
  >  
>- fornisce API native preconfigurate (fotocamera, sensori, notifiche, storage);
  >  
>- include strumenti integrati come **Expo Go** e i servizi di build;
  >  
>- accelera la fase di prototipazione.
  >  
>
>Qualora fosse necessario un controllo maggiore, è sempre possibile uscire dall’ambiente Expo tramite il processo di **eject**, mantenendo il codice React Native già scritto.

##### 2. L'alternativa: React Native CLI
L’altra opzione è **React Native CLI**, ==lo strumento ufficiale mantenuto dal team di React Native.==  
A differenza di Expo, questo approccio prevede un **setup manuale** dell’ambiente di sviluppo, che include la configurazione di:

- Android Studio,
    
- Xcode,
    
- variabili d’ambiente e dipendenze native.
    

React Native CLI offre un ambiente più **essenziale e flessibile**, ==pensato per chi necessita di un controllo completo sull’applicazione nativa o deve integrare codice scritto direttamente in **Swift**, **Objective-C**, **Kotlin** o **Java**.==

È importante sottolineare che **Expo e React Native CLI non sono approcci mutuamente esclusivi**.  
==È possibile iniziare lo sviluppo con Expo per sfruttarne la semplicità iniziale e, quando il progetto cresce o richiede funzionalità native avanzate, migrare verso un workflow completamente nativo.==  
Questo processo prende il nome di **ejecting** ed è reversibile in qualsiasi momento del ciclo di sviluppo.


> [!faq] Quando usare uno o l’altro
> - **Expo CLI** :
> 	- ==è consigliato per partire rapidamente, sviluppare prototipi e realizzare applicazioni standard che sfruttano API native comuni.==
>    
>- **React Native CLI:**
>	- ==è più adatto quando servono integrazioni native personalizzate o un controllo diretto e approfondito sulla piattaforma.==
  >  
>
>In sintesi, Expo rappresenta il punto di partenza ideale per sviluppare applicazioni React Native in modo rapido e senza frizioni, mentre React Native CLI costituisce la soluzione più avanzata per scenari complessi e altamente personalizzati.






