# Introduzione: dal setup allo sviluppo dell’interfaccia

Dopo aver chiarito **[[Lezione 1 - Introduzione a React Native#Introduzione Cos'è React Native|cos’è React Native]]** e aver visto **[[Lezione 1 - Introduzione a React Native#Creazione del progetto con Expo|come creare un progetto tramite Expo]]**, entriamo finalmente nella fase centrale dello sviluppo di un’applicazione mobile: la costruzione dell’interfaccia e la gestione delle interazioni.

React Native ci permette di sviluppare applicazioni **iOS e Android** utilizzando **JavaScript e React**, ma con una differenza fondamentale rispetto al web:  
non lavoriamo con HTML e CSS, bensì con **componenti nativi** e **stili JavaScript**.

In questa fase iniziale ci concentreremo sulle **basi pratiche**, indispensabili per comprendere come:

- si costruisce una UI mobile;
    
- si gestisce lo stato dell’applicazione;
    
- si rende l’interfaccia dinamica e interattiva.
    

Questi concetti verranno applicati immediatamente nello sviluppo di una prima app di esempio.

## I tre pilastri dello sviluppo in React Native

### 1. Componenti di React Native e costruzione dell’interfaccia (UI)

Il primo passo nello sviluppo di un’app React Native è l’utilizzo dei **componenti fondamentali** messi a disposizione dal framework.

Tra i principali:

- **View** → ==contenitore base, equivalente concettuale di un `<div>` nel web;==
    
- **Text** → ==utilizzato per visualizzare testo (qualsiasi stringa deve essere contenuta in un `Text`);==
    
- **Button** → ==componente base per le azioni dell’utente;==
    
- **TextInput** → ==campo di input per l’inserimento di testo.==
    

Questi componenti:

- ==**non sono tag HTML**;==
    
- ==vengono tradotti internamente in **componenti nativi iOS e Android**;==
    
- ==garantiscono prestazioni e comportamento coerenti con la piattaforma==.
    

Attraverso la composizione di questi elementi si costruisce la struttura di base dell’interfaccia dell’app.

### 2. Stile delle app in React Native

In React Native lo styling **non avviene tramite CSS**, ma attraverso oggetti JavaScript definiti con `StyleSheet`.

Caratteristiche principali:

- ==gli stili sono definiti in **oggetti JS**;==
    
- ==le proprietà sono simili al CSS, ma scritte in **camelCase** (`backgroundColor`, `marginTop`, ecc.);==
    
- ==non esistono classi CSS né fogli di stile esterni.==
    

Per la disposizione degli elementi viene utilizzato **Flexbox** come sistema di layout predefinito, che consente di:

- ==organizzare componenti in righe e colonne;==
    
- ==gestire allineamenti e spaziature;==
    
- ==creare layout responsive e adattabili a schermi diversi.==
    

Impareremo quindi a:

- strutturare correttamente il layout;
    
- gestire margini, padding e colori;
    
- ottenere interfacce moderne e coerenti.
### 3. Interattività e gestione dello stato

Un’app non è utile se non reagisce alle azioni dell’utente.  
Per questo è fondamentale introdurre il concetto di **stato**.

In React Native:

- ==lo stato rappresenta i **dati dinamici** di un componente;==
    
- ==quando lo stato cambia, la UI viene **aggiornata automaticamente**.==
    

Vedremo come:

- collegare un `Button` a una funzione;
    
- leggere l’input inserito dall’utente tramite `TextInput`;
    
- aggiornare la UI in risposta alle interazioni;
    
- utilizzare l’hook **[[Lezione 3 - Hooks#Lo `useState()`|`useState`]]** per gestire lo stato locale dei componenti.
    

Questo è il cuore del modello reattivo di React.

> [!deep] **Estensione ES7+ React/Redux/React-Native snippets**
> Come per React JS anche in React native esiste un'estensione che digitando un delle hotkey crea uno scheletro di un core component (simile alla hotkey `rafce` in React JS).
> L'estensione è la stessa di React JS che è valida anche per React Native: 
> -  **ES7+ React/Redux/React-Native snippets** (sviluppata da *dsznajder* )
> È l'estensione più popolare è diffusa nel panorama React / React Native. 
> È stata lo standard de facto per snippet come `rafce`, `rafc`, etc.
> Ed è compatibile con JavaScript e TypeScript per progetti React e React Native. 
>> [!success] **Vantaggi**
>> - Molto usata, con **molte segnalazioni di compatibilità** con snippet React + React Native (compresi componenti, hook, import ecc.).
 >>   
>>- Funziona nella maggior parte dei casi per React Native ed è conosciuta nella community.
  >>  
>>- Funzioni come ricerca dei snippet e comandi per inserire blocchi di codice.
>
>
>> [!failure] **Svantaggi/note:**
>> - A volte può **lasciar andare snippet React “web only”** oppure richiede file con estensione corretta (es. `.tsx`) per comparire.
>>    
>>- Non ha ricevuto aggiornamenti recenti (ultimo update nel 2022), ma è stabile e ampiamente usata.
>
>Come sappiamo le hotkey `rafc` e `rafce` in React creano uno scheletro del componente ma con due differenze: 
>1. `rafc`: crea lo scheletro del componente senza un export defualt.
>2. `rafce`: crea lo scheletro del componente con un export defualt.
>   
>Anche per React Native, con questa estensione, esistono diverse hotkeys le quali creano tutte uno scheletro del core component con delle differenze che vale la pena di conoscere: 
>
>1. `rnf`: funzione componente base 
>```js
>import { View, Text } from 'react-native'
>
>import React from 'react'
>
>  
>
export default function CoreComponent() {
>
> return (
>
>    <View>
>
>      <Text>CoreComponent</Text>
>
>    </View>
>
>  )
>
>}
>```
>2. `rnfs`: Funzione componente(+ `export default`) + StyleSheet vuoto
>```js
>import { StyleSheet, Text, View } from 'react-native'
>import React from 'react'
>
>export default function CoreComponent() {
>
  return (
>
>    <View>
>
>      <Text>CoreComponent</Text>
>
>    </View>
>  )
>
>}
>const styles = StyleSheet.create({})
>```
>
>3. `rnfe`: Funzione componente con export( simile a `rafce`)
>   
>```js
> import { View, Text } from 'react-native'
>import React from 'react'
>const CoreComponent = () => {
>  return (
>    <View>
>      <Text>CoreComponent</Text>
>    </View>
>  )
>}
>export default CoreComponent
>```
>
>4. `rncs`: Class component con StyleSheet
>   
>```js
> import { Text, StyleSheet, View } from 'react-native'
>import React, { Component } from 'react'
>
>export default class CoreComponent extends Component {
>  render() {
>    return (
>      <View>
>        <Text>CoreComponent</Text>
>      </View>
>    )
>  }
>}
>
>const styles = StyleSheet.create({})
>```
>
>5. `imrn`: import da `react-native`
>   
>```js
>import { first } from 'react-native'
>```



## L’app di esempio: Goal Tracker

Per applicare immediatamente i concetti introdotti, realizzeremo una semplice applicazione chiamata **Goal Tracker**.

### Funzionalità principali

L’app permetterà di:

- aggiungere nuovi obiettivi tramite una **finestra modale**;
    
- visualizzare l’elenco degli obiettivi inseriti;
    
- rimuovere un obiettivo semplicemente toccandolo nella lista.
    

### Obiettivi didattici

Nonostante la semplicità, questa app è sufficiente per comprendere:

- come strutturare un’app React Native;
    
- come gestire lo stato e le interazioni di base;
    
- come applicare stili e layout;
    
- come usare la **visualizzazione condizionale** dei componenti.
    

Questa applicazione rappresenta quindi il **punto di partenza pratico** per lo sviluppo di app mobile con React Native.


## Lavorare con i Core Components in React Native

I **Core Components** sono gli elementi fondamentali messi a disposizione da React Native per costruire l’interfaccia utente.  
==A differenza del web, **non utilizziamo HTML**, ma componenti specifici come `View`, `Text`, `Button`, `Image`, ecc., che vengono tradotti in **widget nativi** iOS e Android.==

Questi componenti:

- ==non sono HTML;==
    
- vengono tradotti internamente in **widget nativi**:
    
    - **Swift / Objective-C** su iOS;
        
    - **Java / Kotlin** su Android;
        
- ==garantiscono comportamento e prestazioni coerenti con la piattaforma.==


Comprendere il ruolo e le responsabilità di ciascun componente è essenziale per evitare errori comuni e strutturare correttamente l’app.

### 1. `<View />`

==`View` è il **contenitore fondamentale** in React Native ed è concettualmente equivalente al `<div>` nel web.==

#### Ruolo principale

- ==Layout e raggruppamento di altri componenti==
    
- ==Base per costruire qualsiasi struttura dell’interfaccia==
    

#### Sistema di layout

- Utilizza **Flexbox** per il posizionamento dei figli
    

### Differenze chiave rispetto al web

- **Nessuno scrolling automatico**  
    ==Se il contenuto eccede lo spazio disponibile, viene **tagliato**==  
    ==→ per lo scrolling è necessario usare `<ScrollView />`==
    
- ==**`flexDirection` di default è `column`**==  
    ==(verticale), mentre nel web è `row`==
    

### Props importanti

- **`style`**  
    Permette di definire:
    
    - ==margini e padding==
        
    - ==bordi==
        
    - ==regole Flexbox==
        
- **`onLayout`**  
    Evento chiamato dopo il rendering che restituisce:
    
    - ==coordinate (`x`, `y`)==
        
    - dimensioni (`width`, `height`)  
        ==Utile per layout dinamici e calcoli responsive==


### 2. `<Text />`

==`Text` è **l’unico componente** in grado di renderizzare stringhe di testo.==

==React Native **non consente testo libero dentro una `View`**,== a differenza di quanto avviene con un `<div>` nel web.

#### Ruolo principale

- Visualizzazione del contenuto testuale
    

#### Eredità degli stili

- ==Gli stili **non sono ereditati a cascata** come nel CSS==
    
    - ad esempio: un `fontFamily` applicato a una `View` **non** viene ereditato dai `Text`
        
- **Eccezione importante**  
    ==Un `<Text>` annidato dentro un altro `<Text>` **eredita lo stile del padre**==
    

#### Props importanti

- **`numberOfLines`**  
    ==Tronca il testo dopo un certo numero di righe aggiungendo `...`==
    
- **`ellipsizeMode`**  
    ==Decide dove troncare il testo:==
    
    - `head`
        
    - `middle`
        
    - `tail`
        
- **`selectable`**  
    ==Permette all’utente di selezionare e copiare il testo==  
    ==(default: `false`)==


### 3. `<Button />`

==`Button` è un componente base **pre-stilizzato** che si adatta automaticamente alla piattaforma.==

### Comportamento per piattaforma

- **iOS** → testo cliccabile (blu di default)
    
- **Android** → bottone rettangolare pieno (Material Design)
    

#### Limitazioni

- ==Estremamente **rigido dal punto di vista dello stile**==
    
- Non è possibile:
    
    - ==aggiungere padding personalizzato==
        
    - ==modificare bordi o forme==
        
    - ==inserire icone o layout complessi==
        

#### Quando usarlo

- Prototipi rapidi
    
- Azioni semplici dove il design non è rilevante
    

#### Alternative professionali

Per bottoni personalizzati si utilizzano quasi sempre:

- `<Pressable />`
    
- `<TouchableOpacity />`
    

combinati con:

- `<Text />`
    
- icone o altri componenti



### 4. `<TextInput />`

==`TextInput` consente all’utente di inserire testo tramite tastiera.==

#### Gestione dello stato

È quasi sempre un **Controlled Component**, ovvero:

- ==il valore visualizzato è legato allo **stato** dell’app==
    
- ==ogni modifica aggiorna lo stato tramite `useState`==
    

#### Controllo della tastiera

==È possibile decidere **che tipo di tastiera** mostrare all’utente.==

#### Props importanti

- **`value`**  
    ==Valore corrente del campo==
    
- **`onChangeText`**  
    **Funzione chiamata a ogni digitazione**  
    → ==riceve direttamente la stringa (non un evento come nel web)==
    
- **`keyboardType`**
    
    - `default`
        
    - `numeric`
        
    - `email-address`
        
    - `phone-pad`
        
- **`secureTextEntry`**  
    `{true}` ==per campi password (nasconde i caratteri)==
    
- **`multiline`**  
    `{true}` ==per consentire l’andata a capo (textarea)==

**Esempio Tipico**
```jsx
const [text, setText] = useState('');

<TextInput
  style={{ height: 40, borderColor: 'gray', borderWidth: 1, padding: 10 }}
  value={text}
  onChangeText={newText => setText(newText)}
  placeholder="Scrivi qui..."
  keyboardType="email-address"
/>
```


### 5. `<Image />`

==`Image` consente di visualizzare immagini **locali** o **remote**.==

### Tipologie di sorgenti

#### Immagini locali

```js
source={require('./path/to/image.png')}
```

- ==React Native rileva automaticamente le dimensioni==
    

#### Immagini remote

```js
source={{ uri: 'https://...' }}
```

> [!NOTE]  **Nota fondamentale**  
> 
> Per le immagini remote è **obbligatorio** specificare:
> 
> - `width`
>     
> - `height`
>     
> 
> altrimenti l’immagine **non viene visualizzata**.

#### Props importanti: `resizeMode`

- **`cover`**  
    ==Riempie il contenitore mantenendo l’aspect ratio (può tagliare i bordi)==
    
- **`contain`**  
    ==Mostra tutta l’immagine (può lasciare spazi vuoti)==
    
- **`stretch`**  
    ==Stira l’immagine (distorce)==


### Costruire componenti personalizzati

In React Native, così come in React per il web, l’interfaccia non viene costruita scrivendo tutto in un unico file, ma **componendo piccoli componenti riutilizzabili**.

I **Core Components** (`View`, `Text`, `Button`, ecc.) rappresentano i **mattoni di base**: combinandoli possiamo creare **componenti personalizzati**, più espressivi e facilmente riutilizzabili.

**Esempio: componente personalizzato**
```jsx
const MyTitle = (props) => {
  return (
    <View>
      <Text>{props.title}</Text>
    </View>
  );
};
```

In questo esempio:

- `MyTitle` è un **componente React Native personalizzato**;
    
- utilizza due Core Components:
    
    - `View` ==come **contenitore**;==
        
    - `Text` ==per **visualizzare il testo**;==
        
- il contenuto viene passato dall’esterno tramite le **props** (`props.title`).
    

👉 Questo approccio è alla base dello sviluppo in React Native:  
==**interfacce complesse nascono dalla composizione di componenti semplici**.==


### ## La struttura di un progetto Expo

Un progetto creato con Expo presenta una struttura standard, pensata per essere semplice e immediata:
```text
MYPROJECT/
├─ .expo/
├─ assets/
├─ node_modules/
├─ App.js
├─ app.json
├─ package.json
```

##### File e cartelle principali

- **`App.js`**  
    - ==È il file principale dell’applicazione.==  
    - ==Contiene il **root component**, ovvero il punto di ingresso dell’intera app.==
    
- **`assets/`**  
    - ==Contiene risorse statiche come immagini, icone e font.==
    
- **`package.json`**  
    - ==Definisce dipendenze, script e configurazione del progetto.==
    

👉 Tutta l’app React Native parte da `App.js`, che a sua volta può importare e usare altri componenti.


### Il primo componente React Native: `App.js`

Nel file `App.js` iniziamo importando i Core Components fondamentali:
```jsx
import { View, Text, StyleSheet } from 'react-native';
```
#### Ruolo dei componenti importati

- **`View`**  
    - ==Funziona come un **contenitore/layout**  (concettualmente simile a un `<div>` nel web)==
    
- **`Text`**  
    - ==Serve per **mostrare testo** sullo schermo==
    
- **`StyleSheet.create()`**  
    - Permette di definire gli stili in **JavaScript**, perché in React Native:
    
	    - non esiste il CSS;
        
	    - gli stili sono oggetti JS.
        

#### Styling in React Native

Le proprietà di stile:

- sono simili al CSS (`backgroundColor`, `alignItems`, `justifyContent`, `flex`, ecc.);
    
- vengono passate come **oggetti JavaScript**;
    
- usano la **camelCase** invece dei trattini.


### Un errore fondamentale: il testo deve stare dentro `<Text>`

Uno degli errori più frequenti per chi proviene da React Web è il seguente:

> **Text strings must be rendered within a `<Text>` component**

**Esempio di codice errato**
```jsx
<View>Hello World!</View>
```

Questo codice genera un errore perché:

- `View` **non è progettata per mostrare testo**
    
- `View` è un **contenitore/layout**, non un componente di contenuto

**Codice corretto**
```jsx
<View>
  <Text>Hello World!</Text>
</View>
```

### Concetto chiave da ricordare

- **`<View>`** → contenitore, struttura, layout
    
- **`<Text>`** → contenuto testuale
    

> **Qualsiasi stringa visibile deve essere sempre racchiusa in un `<Text>`**, anche se è solo una parola o un numero.

Questa distinzione è fondamentale per lavorare correttamente con React Native.


#### Visualizzazione dell’app sugli emulatori

Quando avviamo il progetto con:

```shell
npm start
```

Expo apre il **Metro Bundler**.  
Da qui possiamo:

- premere **`a`** :
	- ==per avviare l’app su **Android Emulator**==
    
- premere **`i`**: 
	- ==per avviare l’app su **iOS Simulator** (solo su macOS)==
    

### Hot Reload

Ogni volta che salviamo un file:

- ==l’app viene aggiornata **automaticamente**==
    
- ==non è necessario riavviare il progetto==
    

Questo meccanismo si chiama **Hot Reload** ed è uno dei grandi vantaggi di React Native durante lo sviluppo.

### Nidificazione di componenti: più View, Text e Button

I Core Components possono essere **nidificati** tra loro per creare interfacce complesse.

Esempio concettuale:

- una `View` come contenitore principale
    
- più `Text` al suo interno
    
- uno o più `Button` per l’interazione
    

Questa composizione è alla base della costruzione della UI in React Native.


## Il componente `Button`

Il `Button` è un altro Core Component fondamentale.

Caratteristica importante:

- ==**richiede sempre la prop `title`**==

**Esempio corretto**
```jsx
<Button title="Tap me!" />
```

> [!link]  **Differenza rispetto al web**
>
>Nel web potremmo scrivere:
>```html
> <button>Cliccami</button>
>
>```
>In React Native **non esiste contenuto testuale interno al Button**:  
>- ==il testo viene sempre passato tramite la prop `title`.==



> [!warning] **Differenze principali rispetto a React per il Web**
> React Native si basa sugli stessi concetti di React, ma con differenze strutturali importanti:
>
>- ❌ Non usiamo HTML  
 >   ✔️ Usiamo Core Components (`View`, `Text`, `Button`, `Image`, ecc.)
 >   
>- ❌ Non usiamo CSS  
>    ✔️ Gli stili sono definiti in **JavaScript**
 >   
>- ✔️ Ogni componente React Native viene tradotto in un **componente nativo**
>    
>- ✔️ I Core Components devono essere **importati esplicitamente** prima dell’uso

### Styling in React Native: niente CSS, solo JavaScript

React Native **non utilizza file `.css`** né selettori come `.container` o `#title`.

Tutto lo stile viene definito **direttamente nel codice JavaScript**, utilizzando oggetti.

### Due modi principali per applicare gli stili

1. **Inline Styles**
    
2. **StyleSheet Objects** (approccio consigliato)
    

Entrambi utilizzano oggetti JavaScript ispirati al CSS, ma con differenze importanti.

####  Inline Styling

Come in React JS gli stili possono essere definiti direttamente nella prop `style`.

**Esempio:**
```jsx
<Text
  style={{
    margin: 16,
    borderWidth: 2,
    borderColor: 'red',
    padding: 16,
  }}
>
  Testo di esempio
</Text>
```

**Spiegazione delle proprietà**

- `margin: 16`  
    → ==margine esterno di 16 unità (punti logici)==
    
- `borderWidth: 2` + `borderColor: 'red'`  
    → ==bordo rosso spesso 2 unità==
    
- `padding: 16`  
    → ==spazio interno tra bordo e contenuto==


> [!fail] **Attenzione**
> Non possiamo scrivere:
>```css
> border: 1px solid red;
>
>```
>In React Native:
>
>- `border` **non esiste**
  >  
>- dobbiamo scomporre la proprietà in:
 >   
  >  - `borderWidth`
  >      
 >   - `borderColor`
  >      
  >  - `borderStyle` (se necessario)
##### Differenze rispetto al CSS tradizionale

Anche se la logica è simile al CSS, esistono differenze importanti:

- ==Le **unità di misura sono numeriche**, non `px`, `em`, `%`==
    
    - `margin: 16` ==significa **16 punti logici**==
        
- Le proprietà usano la **camelCase**
    
    - ==`backgroundColor` invece di `background-color`==
        
- Alcune proprietà CSS **non esistono**
    
    - `float`
        
    - `box-shadow`
        
    - `border-collapse`
        
    - e molte altre
        
- ❌ Nessun selettore
    
- ❌ Nessuno stile globale
    
- ✔️ ==Ogni stile è applicato **direttamente al componente**==

#### Usare gli StyleSheet Objects (approccio consigliato)

Scrivere stili inline è utile per esempi o test rapidi, ma **non è consigliato nei progetti reali**.

La soluzione corretta è utilizzare `StyleSheet`.

### Vantaggi principali

- separazione tra JSX e stili
    
- maggiore leggibilità
    
- riutilizzo degli stili
    
- codice più scalabile
**Esempio concettuale**
```jsx
const styles = StyleSheet.create({
  dummyText: {
    margin: 16,
    borderWidth: 2,
    borderColor: 'red',
    padding: 16,
  },
});
```

**Applicazione:**
```jsx
<Text style={styles.dummyText}>Testo</Text>
```


> [!faq] **Perché usare `StyleSheet.create()`**
>
>L’uso di `StyleSheet.create()`:
>
>- ==fornisce **autocompletamento** negli editor (VS Code);==
   > 
>- ==aiuta React Native a **ottimizzare internamente** gli stili;==
  >  
>- ==mantiene il codice più **ordinato e manutenibile**.==
   > 
>
>Inoltre:
>
>- modificando una sola volta lo stile (`dummyText`)
   > 
>- tutte le componenti che lo utilizzano si aggiornano automaticamente



> [!NOTE] Title
> Contents
