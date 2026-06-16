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


