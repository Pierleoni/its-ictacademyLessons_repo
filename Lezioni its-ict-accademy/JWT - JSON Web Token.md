
## JSON Web Token

Abbiamo già visto cos'è [un file JSON](Lezione 5 - Il Formato JSON#Cos'è il JSON e perché viene utilizzato) e com'è [strutturato un file JSON](Lezione 5 - Il Formato JSON#**Struttura di un documento JSON**), ora vedremo cos'è un **JWT (JSON Web Token)** e a cosa serve.

### Cosa sono i JWT

Per comprendere meglio cosa sono i JWT partiamo da un'analogia: immaginiamo di dover accedere al nostro conto bancario per controllare il saldo o effettuare un bonifico. In questo scenario entrano in gioco due concetti fondamentali che lavorano in sequenza:

1. **Autenticazione**
2. **Autorizzazione**

> [!info] È importante non confonderli: l'autenticazione viene **prima** e risponde alla domanda _"Chi sei?"_, mentre l'autorizzazione viene **dopo** e risponde a _"Cosa puoi fare?"_

### Autenticazione

==È il processo di identificazione di un utente attraverso le sue credenziali== — esattamente come quando si fa il login in una web app, un'app desktop o un'app mobile.

Nel momento in cui i campi del form vengono compilati correttamente, l'utente è **autenticato** e può accedere al suo profilo. 
In questo preciso momento il server rilascia all'utente due token:

1. **Refresh Token** — ==ha una lunga durata e serve a richiedere un nuovo Access Token quando questo scade, senza dover fare di nuovo il login==
2. **Access Token** — ==è il **JWT** vero e proprio, ha una durata breve e viene utilizzato per l'autorizzazione ad ogni richiesta successiva== ^f35758

### Autorizzazione

==È il processo di verifica dei permessi per assicurarsi che l'utente abbia accesso alle azioni, alle risorse o ai servizi a cui sta tentando di accedere.==

> [!example] **Tornando all'analogia bancaria:**
>  una volta autenticato, l'autorizzazione stabilisce **cosa** quell'utente può fare — visualizzare il proprio conto, effettuare un bonifico, o accedere solo alle sue risorse e non a quelle di altri utenti. 
>  Ad ogni richiesta verso il server, il client invia il JWT nell'[[Lezione 7 - Sistemi REST#Gli header HTTP informazioni aggiuntive|header]] della chiamata HTTP, e il server lo verifica per decidere se concedere o negare l'accesso.


### Anatomia di un JSON Web Token
Un JWT è composto da tre parti, separate da un punto (`.`) e codificate in Base64URL:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTYiLCJuYW1lIjoiTHVjYSBSb3NzaSIsImV4cCI6MTcxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Queste tre parti corrispondono a 
```
HEADER . PAYLOAD . SIGNATURE
```

#### 1. Header: 
Contiene i metadati del token (es: il tipo di token, l'algoritmo usato per creare la firma  ), in particolare il tipo di token e l'algoritmo usato per generare la firma.
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

#### 2. Payload: 
**È la parte principale del token:** 
- ==contiene le informazioni sull'utente e sulla sessione.==
- ==I campi al suo interno si chiamano **claim**.== 
Lo standard JWT definisce alcuni claim consigliati che si trovano quasi sempre:

| Campo   | Nome esteso | Significato                                                                        |
| ------- | ----------- | ---------------------------------------------------------------------------------- |
| `"iss"` | Issuer      | ==Chi ha emesso il token (es. un servizio di autenticazione o un provider OAuth)== |
| `"sub"` | Subject     | Il soggetto del token, tipicamente l'ID utente                                     |
| `"exp"` | Expiration  | Timestamp Unix di scadenza del token                                               |
| `"iat"` | Issued At   | Timestamp Unix di emissione del token                                              |
Oltre a questi, il payload può contenere claim personalizzati per l'applicazione — nome utente, email, ruolo (`"admin"`, `"visitor"`, ecc.):
```json
{
  "iss": "auth.miabanca.it",
  "sub": "user_123456",
  "exp": 1716239022,
  "iat": 1716235422,
  "name": "Luca Rossi",
  "email": "luca@example.com",
  "role": "admin"
}
```

>[!warning] Il payload **non è cifrato**, solo codificato in Base64URL. 
>Chiunque intercetti il token può leggerne il contenuto — non inserire mai dati sensibili come password o numeri di carta di credito.

#### 3. Signature (firma): 
Quando il server di autenticazione emette un JWT, lo **firma**: 
- ==è il modo in cui dichiara di essere l'autorità che ha emesso quel token.==

La firma viene generata così:
```
HMACSHA256(
  base64url(header) + "." + base64url(payload),
  secret
)
```

==Il server prende [[#1. Header|header]] e [[#2. Payload|payload]], li fa passare attraverso una funzione di hashing insieme a un **valore segreto** (una stringa privata che solo il server conosce), e produce un hash univoco.== 
Questo hash è la firma, ed è inclusa nel token stesso.

#### Come funzionano le firme 
Ora che sappiamo cosa contiene un JWT, vediamo come il server garantisce che nessuno lo abbia manomesso.

Quando emette il token, il server prende l'header e il payload e li fa passare attraverso una funzione di hashing insieme a un **valore segreto** — una stringa privata che solo il server conosce (es. `"mio_segreto_super_sicuro"`). 
Il risultato di questa operazione è la firma, che viene inclusa nel token stesso come terza parte.
```
firma = HMACSHA256(base64url(header) + "." + base64url(payload), secret)
```

In altre parole, la firma è una "impronta digitale" del token: cambia se cambia anche solo un carattere nell'header o nel payload.

#### Come funziona la verifica

Quando il client invia il JWT al server in una richiesta protetta, il server non si fida ciecamente del token — lo **verifica**:

1. ==Prende l'header e il payload ricevuti==
2. ==Ricalcola la firma con lo stesso algoritmo e lo stesso segreto==
3. ==Confronta la firma appena calcolata con quella presente nel token==

> [!done] **Se le due firme corrispondono → il token è legittimo, non è stato alterato durante il trasporto e l'utente viene autorizzato.**
> 
> 

> [!failure] **Se le due firme non corrispondono → il token è stato manomesso (o è stato firmato con un segreto diverso) e il server risponde con un `401 Unauthorized`.**
> 

> [!info] Questo meccanismo è efficiente proprio perché il server non deve fare nessuna query al database per verificare l'identità dell'utente — gli basta ricalcolare l'hash. È uno dei motivi per cui i JWT sono così diffusi nelle architetture a microservizi.


### La decodifica dei JWT
C'è una cosa fondamentale da capire sui JWT: 
- ==**non sono crittografati, sono codificati**.== 
Non è la stessa cosa.

La codifica Base64URL non è una forma di protezione — ==è semplicemente un formato di trasporto.== 
Chiunque può prendere un JWT, incollarlo su [jwt.io](https://jwt.io/) e leggere immediatamente tutti i claim in chiaro. È proprio per questo che, come abbiamo già detto, **non si devono mai inserire informazioni sensibili nel payload**.

Ma c'è di più: non solo è possibile _leggere_ il contenuto di un JWT, ma è anche possibile _modificarlo_. Immaginiamo di intercettare questo token:
```json
{
  "iss": "auth.miabanca.it",
  "sub": "user_123456",
  "exp": 1716239022,
  "iat": 1716235422,
  "name": "Luca Rossi",
  "email": "luca@example.com",
  "role": "user"
}
```

Un attaccante potrebbe provare a cambiare `"role": "user"` in `"role": "admin"` per ottenere privilegi elevati. In teoria sembra un attacco semplicissimo — in pratica **non funziona**, perché modificando il payload la firma non corrisponde più. Il server ricalcola l'hash, lo confronta con quello nel token e rileva immediatamente la manomissione, restituendo un `401 Unauthorized`.
>[!info] **La firma non impedisce a nessuno di _leggere_ o _modificare_ il token — impedisce che una versione modificata venga accettata dal server.** 
>==La sicurezza non sta nella segretezza del contenuto, ma nell'integrità garantita dalla firma.==

### Lo statelessness dei JWT

I JWT sono [[Lezione 7 - Sistemi REST#**Vincolo “Stateless” (Senza Stato)** e Risorse|stateless]], esattamente come le API REST — e non è una coincidenza, sono due concetti che lavorano molto bene insieme.

Per capire perché questo è importante, immaginiamo una piattaforma come Netflix: un'azienda con migliaia di microservizi indipendenti (streaming video, catalogo, fatturazione, raccomandazioni, ecc.) che devono tutti essere in grado di riconoscere e servire l'utente.

Senza i JWT, ogni servizio dovrebbe contattare un database centrale per verificare chi è l'utente e cosa può fare — migliaia di richieste al secondo, tutte che attendono una risposta dal database. Un collo di bottiglia enorme.

Con i JWT invece ogni token **porta con sé tutte le informazioni necessarie**: 
- chi è l'utente, 
- il suo ruolo, 
- quando il token scade. 
Quando l'utente sta facendo lo streaming di un video, il client invia decine di richieste al secondo per recuperare i pacchetti video — il servizio di streaming non ha bisogno di validare ogni singola richiesta contro un database. 
Gli basta verificare la firma del JWT localmente, in memoria, in pochi millisecondi.

> [!info] **Questo è il vantaggio principale dello statelessness:** 
> ==il server non deve ricordare nulla tra una richiesta e l'altra.== 
> ==Ogni richiesta è autonoma e porta con sé tutto il contesto necessario per essere elaborata.==


### Refresh Token

Ora che abbiamo capito come funzionano i JWT, potremmo essere tentati di generare un token per ogni utente con una scadenza molto lunga — magari un anno — e non pensarci più. 
In realtà ci troveremmo subito di fronte a due problemi seri.
#### **Primo problema: il furto del token:** 
- I JWT sono come i passaporti: ==se qualcuno riesce a intercettare il token di un utente e a includerlo nell'header `Authorization`, può accedere al suo profilo indisturbato — né il sistema né l'utente se ne accorgerebbero==.

#### **Secondo problema: le informazioni nel token diventano obsolete.** 
Supponiamo che il ruolo di un utente venga retrocesso da `"admin"` a `"user"`. 
==Se il token scade tra un anno, quell'utente continuerà ad accedere come amministratore fino alla scadenza.== 
Questo è un effetto diretto dello statelessness che abbiamo visto prima: 
- ==i servizi si fidano ciecamente di quello che c'è scritto nel token, e a differenza delle sessioni tradizionali lato server, **un JWT non può essere invalidato dal server stesso**.==

Per ovviare a entrambi i problemi, i JWT hanno un **ciclo di vita breve** — **in genere nell'ordine dei minuti.** 
Quando il token scade, il client non costringe l'utente a fare di nuovo il login: 
- ==invia invece il **Refresh Token:** (che avevamo visto essere rilasciato insieme all'Access Token al momento del login) per richiederne uno nuovo.== 
**Il Refresh Token ha una durata molto più lunga:** 
- ==viene salvato nel database e può essere associato all'ID utente, a una sessione specifica o persino a un determinato dispositivo==.

> [!done] **Questo meccanismo mitiga entrambi i rischi:**
> 
> 
> 1. **Furto del token** — ==anche se qualcuno intercetta un Access Token, questo diventa inutilizzabile in pochi minuti quando viene sostituito dal refresh.==
> 2. **Token non aggiornati** — ==ad ogni refresh il server può emettere un nuovo token con le informazioni più recenti, ad esempio il ruolo aggiornato dell'utente==.

> [!info] Il Refresh Token è l'unico elemento di questa architettura che richiede una verifica contro il database. L'Access Token invece viene validato localmente dal server tramite la firma — è esattamente questa separazione che rende il sistema scalabile.
#### Refresh Token Rotation

Anche i Refresh Token però possono essere rubati — e dato che hanno una durata molto più lunga degli Access Token, il rischio è maggiore. 
Per mitigare questo problema si usa una tecnica chiamata **Refresh Token Rotation**: 
- ==ogni volta che un Refresh Token viene utilizzato, viene immediatamente invalidato e sostituito con uno nuovo.==

Il flusso funziona così:

1. ==L'Access Token dell'utente scade==
2. ==Il client invia il Refresh Token al server per richiederne uno nuovo==
3. ==Il server verifica il Refresh Token, elimina quello vecchio dal database e rilascia contemporaneamente un nuovo Access Token **e** un nuovo Refresh Token==
4. ==Il client salva il nuovo Refresh Token per il prossimo ciclo==

In questo modo, anche se un attaccante riuscisse a rubare il Refresh Token, avrebbe una finestra di utilizzo brevissima: 
- ==al primo refresh legittimo dell'utente, quel token viene invalidato e l'attaccante si ritrova con un token inutilizzabile==.

> [!warning] Se il server riceve una richiesta con un Refresh Token già utilizzato in precedenza, questo è un segnale di allarme — significa che qualcuno potrebbe averlo rubato. In questo caso la best practice è invalidare **tutta la sessione** dell'utente e costringerlo a fare di nuovo il login.
