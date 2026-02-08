In questa lezione dobbiamo collegare l'app al servizio di Firebase, chiamato Firestore.
Questo servizio è detto backendless: 
- **significa che non è necessario sviluppare e mantenere un backend personalizzato**, poiché Firebase (e in particolare Firestore) fornisce direttamente i servizi di backend come **persistenza dei dati, autenticazione, gestione delle richieste e sicurezza**, accessibili dal client tramite SDK e API già pronte.
Successivamente, per poter utilizzare Firebase all’interno del progetto, è necessario **installare le relative dipendenze**.  
A tal fine, eseguire il seguente comando **dalla directory root del progetto**:
```shell
npx create-expo-app userCrudNative --template blank
```

Questo comando aggiunge al progetto il pacchetto Firebase, rendendo disponibili gli SDK necessari per inizializzare l’applicazione e interagire con servizi come Firestore, autenticazione e storage.
Successivamente, creiamo un file denominato **`firebaseConfig.js`** e al suo interno incolliamo lo **script di configurazione fornito da Firebase**, necessario per inizializzare l’applicazione e collegarla al progetto Firebase creato in precedenza:
```jsx
// Import delle funzioni necessarie dagli SDK Firebase
import { initializeApp } from "firebase/app";

// Configurazione dell'applicazione Firebase
const firebaseConfig = {
  apiKey: "AIzaSyAeCCTrBqMs4yuhw2T_szWRtBT1VWgePPA",
  authDomain: "user-crud-990e6.firebaseapp.com",
  projectId: "user-crud-990e6",
  storageBucket: "user-crud-990e6.firebasestorage.app",
  messagingSenderId: "304392754507",
  appId: "1:304392754507:web:0850385db247052bb9c4ce"
};

// Inizializzazione dell'app Firebase
const app = initializeApp(firebaseConfig);

```
A questo punto, per poter utilizzare Firebase all’interno del progetto, è necessario **installare le dipendenze richieste**.  
Dalla **directory root del progetto**, eseguire il seguente comando:
```shell
npm install firebase
```


Questo passaggio consente di rendere disponibili gli SDK Firebase necessari per interagire con i servizi offerti, come Firestore, autenticazione e storage.

Dopodiche scrivere in questo file 
```js
// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";

import {getFireStore} from "firebase/firestore";

import {getAuth} from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use

// https://firebase.google.com/docs/web/setup#available-libraries

  

// Your web app's Firebase configuration

const firebaseConfig = {

    apiKey: "AIzaSyAeCCTrBqMs4yuhw2T_szWRtBT1VWgePPA",

    authDomain: "user-crud-990e6.firebaseapp.com",

    projectId: "user-crud-990e6",

    storageBucket: "user-crud-990e6.firebasestorage.app",

    messagingSenderId: "304392754507",

    appId: "1:304392754507:web:0850385db247052bb9c4ce"

};

  

// Initialize Firebase

const app = initializeApp(firebaseConfig);

  

const db = getFireStore(app);

const auth = getAuth(app);

  
  
  

export {app, db, auth};
```

Poi installare altre dipendenze con i commandi : 
```shell
npm install @react-navigation/native-stack
```

```shell
npm install @react-navigation/native
```

```shell
npx expo install react-native-screens react-native-safe-area-context
```

