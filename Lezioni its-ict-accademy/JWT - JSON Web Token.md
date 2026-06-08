
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
Quando il server di autenticazione emette un JWT, lo **firma**: è il modo in cui dichiara di essere l'autorità che ha emesso quel token.

La firma viene generata così:
```
HMACSHA256(
  base64url(header) + "." + base64url(payload),
  secret
)
```

Il server prende header e payload, li fa passare attraverso una funzione di hashing insieme a un **valore segreto** (una stringa privata che solo il server conosce), e produce un hash univoco. 
Questo hash è la firma, ed è inclusa nel token stesso.

#### Come funzionano le firme 
Ora che sappiamo cosa contiene un JWT, vediamo come il server garantisce che nessuno lo abbia manomesso.

Quando emette il token, il server prende l'header e il payload e li fa passare attraverso una funzione di hashing insieme a un **valore segreto** — una stringa privata che solo il server conosce (es. `"mio_segreto_super_sicuro"`). Il risultato di questa operazione è la firma, che viene inclusa nel token stesso come terza parte.
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
La parte più importante da comprendere dei JWT è che non sono realmente crittografati e decrittografati, ma sono in in realtà codificati. 
Chiunque può visualizzare e modificare i JWT. 
Come abbiamo già detto sono codificati utilizzando Base64, difatti è possibile prendere qualsiasi JWT copiarli e incollarli su [jwt.io](https://www.jwt.io/) e vedere tutti i claims. 
Ed è proprio per questo che non si deve mai memorizzare informazioni sensibili nei JWT, anche perché non solo è possibile visualizzare il contenuto di questi JWT ma possiamo alterare i valori delle chiavi. 
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

Ad esempio in questo caso abbiamo cambiato il ruolo dell'utente da `"admin"` in `"user"`, in questo modo possiamo pensare di hackerare il sistema riscrivendo semplicemente il valore a nostro piacimento anche se in realtà questo non accadrebbe perché le firme non corrisponderebbero più.

### Lo statelessness dei JWT 
I JWT sono [[Lezione 7 - Sistemi REST#**Vincolo “Stateless” (Senza Stato)** e Risorse|stateless]], esattamente come le API REST. 
Per comprendere meglio partiamo da uno scenario: 
Immaginiamo una piattaforma tipo Netflix; un azienda enorme con migliaia di servizi (fatturazione, streaming video, catalogo, etc.), l'utente deve ovviamente poter interagire con questi diversi servizi. 
Ed è proprio qui che la stateless entra in gioco: 
- Un JWT contiene tutte le informazioni di cui hanno bisogno questi servizi per elaborare la loro richiesta.
Quindi quando l'utente sta recuperando (fetching) un video da Netflix sta anche inviando molte richieste per recuperare questi pacchetti. 
Ad esempio il servizio di streaming non ha bisogno di prendere ogni singola richiesta dal client e convalidarla rispetto a qualche database. 

### Refresh Token 
Ora che abbiamo capito come funzionano e cosa sono i JWTs potremo erroneamente pensare di costruire la nostra app, generare i JWT per i nostri utenti con una sola scadenza e basterà che li usino e andrà tutto bene . 
In realtà ci troveremmo di fronte a due problemi: 
1. I JWTS sono come i passaporti: se qualcuno riesce a rubare il JWT di qualcun altro e a fornirlo nell'intestazione di autorizzazione può accedere al profilo di quel utente senza che il sistema (e anche l'utente) se ne accorga.
2. Le informazioni contenute nel token potrebbero cambiare: 
	- supponiamo che il livello di accesso di un utente cambi da amministratore ad utente, e se il token scade tra un anno quell'utente potrebbe accedere ancora al servizio come amministratore fino alla scadenza del token.
Questo perché come abbiamo detto i token JWT sono stateless, in questo caso contendo il ruolo, i servizi prenderanno quel ruolo come legittimo e a differenza delle normali e tradizionali  sessioni dei server:
- I JWTs non possono essere essere invalidati dal server stesso. 
Per ovviare a questo problema I JWTs hanno un ciclo di vita breve (in genere nell'ordine dei minuti).
Ogni volta che il token scade, l'utente invierà una richiesta per aggiornare (refresh) quel token,  e se il nuovo token viene autenticato, viene salvato nel database e associato all'ID utente o a una determinata sessione o magari a un determinato dispositivo.
Quindi l'utente ogni volta che il token web JSON di accesso scade può fornire il proprio token di aggiornamento.

Quindi fare il refresh mitiga due rischi: 
1. Che qualcuno rubi i token utenti specifici, e se pure ci riuscisse il token viene aggiornato molto velocemente quindi diventerebbe inutilizzabile ben presto 
2. I token non rappresentano lo stato reale delle cose: 

#### Refresh token rotation 
In ogni caso per evitare che i token vengano comunque rubati, si usa ruotare i token di aggiornamento (refresh) ogni volta che il token viene utilizzato. 
Quindi ad esempio, il token di accesso di un utente è scaduto e il client manda una richiesta di aggiornamento al server dicendogli che ha bisogno di un nuvo token di accesso fornendogli il proprio token di aggiornamento, e solo quando l'operazione ha successo il server elimina il vecchio refresh e ne rilascia uno nuovo.
Quindi ogni volta che aggiornerò il token, ne riceverò uno nuovo, questo significa che se un hacker riuscisse ad accedere al mio refresh token al primo refresh quel token non varrà più nulla. 