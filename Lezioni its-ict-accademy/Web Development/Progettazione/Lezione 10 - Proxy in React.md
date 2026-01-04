### Introduzione

Come visto nelle sezioni precedenti, i browser applicano la **[[Lezione 9 - Same Origin Policy e CORS#La Same-Origin Policy|Same Origin Policy]]:**
- ==una regola di sicurezza fondamentale che limita le richieste HTTP tra risorse appartenenti a **origini diverse** (protocollo, dominio o porta).==  
Per consentire comunicazioni controllate tra applicazioni web e server remoti, il web moderno introduce il meccanismo **[[Lezione 9 - Same Origin Policy e CORS#Cos’è CORS (Cross-Origin Resource Sharing)|CORS (Cross-Origin Resource Sharing)]]:** 
- ==che permette al server di dichiarare esplicitamente **quali origini, metodi e header sono autorizzati**.==

Tuttavia, durante lo **sviluppo locale**, è molto comune che il client e il server girino su **porte diverse** (ad esempio `localhost:3000` per [[Lezione 7; React|React]] e `localhost:3001` per l’API), causando richieste cross-origin, [[Lezione 9 - Same Origin Policy e CORS#Cos’è una Preflight Request|preflight request]] e potenziali blocchi da parte del browser.  
Per semplificare questo scenario e rendere più fluido il flusso di sviluppo, React mette a disposizione il concetto di **proxy:**
- ==uno strumento che consente di **simulare una comunicazione same-origin** inoltrando le richieste dal server di sviluppo React al backend API.==

L’uso del proxy
- ==non sostituisce CORS== 
- ==né lo disabilita,== 
- ==ma rappresenta una **soluzione tecnica limitata all’ambiente di sviluppo**, utile per concentrarsi sul comportamento dell’applicazione senza dover configurare fin da subito le policy di sicurezza lato server.==  
Nei paragrafi successivi vedremo **come configurare un proxy in React**, analizzando le diverse modalità disponibili e il loro impatto sulla comunicazione client–server.


##  Uso del Proxy in React (Ambiente di Sviluppo)

Durante lo sviluppo di un’applicazione **React**, è molto frequente imbattersi in problematiche legate a **[[Lezione 9 - Same Origin Policy e CORS#CORS un’eccezione controllata alla Same-Origin Policy|CORS]]**.  
Questo accade soprattutto quando **client e server non condividono la stessa origine**, una situazione tipica negli ambienti di sviluppo locali.

Un caso estremamente comune è il seguente:

- il **client React** è eseguito su `http://localhost:3000`;
    
- il **server delle API** è in ascolto su `http://localhost:3001` (oppure su un dominio differente).

Dal punto di vista del browser, queste due URL rappresentano **origini diverse** (porta differente), e quindi **ogni richiesta HTTP** inviata dal client al server API è soggetta alle **regole della Same Origin Policy**.  
Di conseguenza, il browser applica le politiche **CORS**, con la possibile generazione di **preflight request** (`OPTIONS`) o, nei casi più restrittivi, con il blocco completo della richiesta.

Per **semplificare il flusso di sviluppo** ed evitare di configurare immediatamente le policy CORS lato server, React mette a disposizione il concetto di **proxy**.

L’utilizzo del proxy consente di:

- ==evitare i problemi di CORS **durante la fase di sviluppo**==;
    
- ==far apparire tutte le richieste come **same-origin** dal punto di vista del browser==;
    
- ==mantenere il codice client più pulito e leggibile, senza logiche condizionali legate all’ambiente==.
    

> [!warning] **Nota importante**  
> Il proxy di React è una **soluzione esclusivamente pensata per l’ambiente di sviluppo**.  
> In **produzione**, la gestione delle politiche di sicurezza e del CORS deve essere effettuata **sempre lato server**.
## Come funziona il Proxy in React

Il funzionamento del proxy React si basa su un meccanismo di **inoltro trasparente delle richieste**.

In pratica:

- il **browser** invia tutte le richieste HTTP **solo al server di sviluppo React** (`localhost:3000`);
    
- il server React intercetta le richieste destinate alle API;
    
- tali richieste vengono **inoltrate internamente** al server backend (`localhost:3001`);
    
- dal punto di vista del browser, la comunicazione avviene **con una singola origine**.
    

Poiché il browser vede la richiesta come **same-origin**,  
==le regole CORS e le preflight request non vengono attivate==.

Questo approccio permette allo sviluppatore di concentrarsi sul **comportamento dell’applicazione** e sulla **logica di comunicazione client–server**, rimandando la configurazione delle policy CORS a una fase successiva, tipicamente quella di **deploy in produzione**.

### Metodo 1 – Proxy tramite `package.json`

Il **metodo più semplice e immediato** per utilizzare un proxy in un progetto React consiste nell’aggiungere la proprietà `proxy` all’interno del file `package.json`.
```json
{
  "proxy": "http://localhost:3001"
}
```

Con questa configurazione, React è in grado di **inoltrare automaticamente** le richieste HTTP verso il server backend durante l’esecuzione dell’ambiente di sviluppo.

#### Prima (senza proxy)

In assenza di proxy, il client React effettua chiamate dirette al server API:

```js
fetch('http://localhost:3001/users')
```
In questo scenario:

- il browser rileva che la richiesta è **cross-origin** (`localhost:3000` → `localhost:3001`);
    
- entra in gioco il meccanismo **CORS**, con possibile **preflight request**;
    
- il server deve essere configurato per accettare esplicitamente l’origine `http://localhost:3000`.
    

Questo comporta una **maggiore complessità**, soprattutto in fase di sviluppo.
#### Dopo (con proxy)
Con il proxy configurato, il client React può effettuare richieste in modo più semplice:

```js
fetch('/users')
```

A questo punto:

- React intercetta la richiesta;
    
- la inoltra internamente a:

```shell
http://localhost:3001/users
```

- dal punto di vista del browser:
    
    - la richiesta è diretta a `localhost:3000`;
        
    - **non è cross-origin**;
        
    - **CORS non viene applicato**.
        

> [!done] **Vantaggi**
> 
> - configurazione rapida e immediata;
>     
> - nessuna dipendenza aggiuntiva;
>     
> - ideale per progetti semplici con un solo backend.
>     

> [!failure] **Limiti**
> 
> - supporta **un solo server di destinazione**;
>     
> - non consente regole avanzate (rewrite, header, più path);
>     
> - flessibilità limitata.
>

###  Metodo 2 – Proxy JavaScript con `http-proxy-middleware`

Per applicazioni più articolate — ad esempio con **più backend**, **path differenti** o **regole di inoltro personalizzate** — React consente di definire il proxy tramite codice JavaScript.

Questo approccio offre **maggiore controllo** sul comportamento delle richieste.

**Installazione della dipendenza**
```shell
npm install http-proxy-middleware --save-dev
```


 **Creazione del file di configurazione:**

Crea il file:

```shell
src/setupProxy.js
```

Esempio di configurazione:
```js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:3001',
      changeOrigin: true
    })
  );
};
```

#### Come funziona

Con questa configurazione:

- tutte le richieste verso:
    
    - `/api/*`
        
- vengono inoltrate a:
    
    - `http://localhost:3001/api/*`
        

Dal punto di vista del browser:

- le richieste risultano dirette **solo verso `localhost:3000`**;
    
- non vengono applicate le regole CORS;
    
- la comunicazione appare **same-origin**.
    

> [!done] **Vantaggi**
> 
> - maggiore flessibilità e controllo;
>     
> - possibilità di gestire **più backend**;
>     
> - supporto a configurazioni avanzate (rewrite dei path, logging, sicurezza).
>     



### Considerazione finale

È importante sottolineare che il proxy **non disabilita CORS**:  
==lo aggira esclusivamente in ambiente di sviluppo==, facendo apparire le richieste come **same-origin** dal punto di vista del browser.

In **produzione**, le politiche CORS devono essere **sempre gestite correttamente lato server**.

> [!example] **In sintesi**
> 
> |Metodo|Quando usarlo|
> |---|---|
> |`proxy` in `package.json`|Progetti semplici con un solo backend|
> |`http-proxy-middleware`|Progetti complessi, più API o regole avanzate|