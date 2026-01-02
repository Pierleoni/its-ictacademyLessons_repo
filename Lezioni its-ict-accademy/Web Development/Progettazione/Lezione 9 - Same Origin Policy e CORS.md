
# Introduzione : dal metodo OPTIONS alla sicurezza del browser

Nella lezione precedente abbiamo visto come, utilizzando strumenti come **[[Lezione 8 - Chiamate Curl#Cosa sono le chiamate cURL|cURL]]**, sia possibile inviare direttamente richieste HTTP a un server e osservare in modo esplicito metodi, header e risposte.

Abbiamo anche introdotto il metodo **[[Lezione 8 - Chiamate Curl#Il metodo OPTIONS|OPTIONS]]**, ==chiarendo che spesso **non è l’utente a inviarlo**, ma è il **browser** a farlo automaticamente come parte dei meccanismi di sicurezza del Web moderno.==

Per comprendere **perché il browser si comporta in questo modo**, è necessario introdurre due concetti fondamentali:
- la **Same-Origin Policy**;
    
- il meccanismo **CORS (Cross-Origin Resource Sharing)**.
Questi concetti spiegano **perché alcune richieste funzionano con cURL ma non dal browser**, e perché il metodo OPTIONS è così strettamente legato alla sicurezza delle applicazioni web.

## La Same-Origin Policy

==La **Same-Origin Policy (SOP)** è una **politica di sicurezza implementata dai browser** che limita le interazioni tra risorse provenienti da origini diverse.==

In termini semplici:

> ==**una pagina web può effettuare richieste solo verso la stessa origine da cui è stata caricata**, salvo esplicite autorizzazioni.==

###  Quando due URL hanno la stessa origine

Due URL sono considerati della **stessa origine** solo se **tutti e tre** questi elementi coincidono:

- **protocollo** (`http` / `https`);
    
- **dominio**;
    
- **porta**.
    

#### Esempi

✅ **Stessa origine**
```arduino
https://example.com/page1
https://example.com/page2
```

**Origini diverse**

- `https://example.com` → `http://example.com`  
    _(protocollo diverso)_
    
- `https://example.com` → `https://api.example.com`  
    _(sottodominio diverso)_
    
- `https://example.com` → `https://example.com:8080`  
    _(porta diversa)_

###  Perché esiste la Same-Origin Policy

La Same-Origin Policy è uno dei **pilastri della sicurezza del Web**.  
Il suo obiettivo è **proteggere l’utente** da comportamenti malevoli.

Senza questa politica, un sito potrebbe:

- ==leggere dati sensibili di altri siti aperti nel browser;==
    
- ==inviare richieste non autorizzate a nome dell’utente (ad esempio usando cookie o token);==
    
- ==accedere a risorse private o riservate.==
    

In altre parole, la SOP impedisce che una pagina web possa **“spiare” o manipolare** risorse appartenenti ad altre origini.

## Cos’è CORS (Cross-Origin Resource Sharing)

**CORS** è un meccanismo che permette di **rilassare in modo controllato** la Same-Origin Policy.

Non è il browser a decidere liberamente:  
- ==è **il server** che dichiara **quali origini sono autorizzate** ad accedere alle sue risorse.==

Con CORS, il server può specificare:

- ==da quali domini accetta richieste;==
    
- ==quali metodi HTTP sono consentiti;==
    
- ==quali header possono essere inviati;==
    
- ==se le credenziali sono ammesse.==
    

Queste informazioni vengono comunicate tramite **header HTTP di risposta**, come:

- `Access-Control-Allow-Origin`
    
- `Access-Control-Allow-Methods`
    
- `Access-Control-Allow-Headers`

### CORS: un’eccezione controllata alla Same-Origin Policy
Quindi **CORS (Cross-Origin Resource Sharing):** 
- ==è il meccanismo che consente a un **server di dichiarare esplicitamente** quali origini sono autorizzate ad accedere alle sue risorse.==

In altre parole:

> **la Same-Origin Policy non viene eliminata**, ma può essere **rilassata in modo controllato** su decisione del server.

Il browser si limita a **far rispettare** queste regole, senza mai decidere autonomamente.


###  Simple Requests (Richieste Semplici)

Non tutte le richieste cross-origin sono considerate rischiose.  
==Alcune vengono classificate come **Simple Requests** e vengono inviate **direttamente**, senza alcun controllo preliminare.==

###### Esempio di Simple Request
```js
fetch('http://localhost:3001/users', { method: 'GET' });
```

#### Criteri per una Simple Request

Una richiesta è considerata _simple_ se soddisfa **tutti** questi requisiti:

1. **Metodo HTTP**:
    
    - `GET`
        
    - `HEAD`
    
	- `POST` 
        
2. **Headers consentiti**:
    
    - `Content-Type: text/plain`
        
    - `application/x-www-form-urlencoded`
        
    - `multipart/form-data`

Esempio: 
```js
fetch('/api/login', {
  method: 'POST',
  body: 'username=marco&password=123',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
});
```

Questa **è una Simple Request**, anche se modifica lo stato del server.
Chiariamo subito questo punto: 
>==**non è la modifica dello stato del server in sé a far scattare il preflight**.==

Se la richiesta rientra in questi criteri, il browser **non invia alcuna preflight request**.


> [!faq] **Perche `POST` non viene considerato un metodo pericoloso**
> La risposta sta nel fatto che, **per il browser**, la distinzione non è basata sulla semantica REST, ma su **criteri storici e di sicurezza pratica**.
> 1. **“Pericoloso” per REST ≠ “pericoloso” per il browser**
> Dal punto di vista REST: 
> - `GET` → sicuro (_safe_, read-only)
  >  
>- `POST` → **modifica lo stato**
  >  
>- `PUT` → modifica lo stato
  >  
>- `PATCH` → modifica lo stato
  >  
>- `DELETE` → modifica lo stato
> Quindi potremmo pensare che `POST` modifica lo stato quanto `PUT` e `DELETE`, tuttavia ciò che fa scattare il preflight request non è la modifica dello stato in sé. 
> Difatti la ragione di questo comportamento lo si deve guardare non dal lato server ma da lato client, più specificatamente dal lato del browser il quale non ragiona in termini REST.
> 2. **Il criterio del browser è storico (HTML)**
> Il concetto di _Simple Request_ nasce **prima delle API REST**, ed è legato a ciò che **HTML è sempre stato in grado di fare senza JavaScript**.
> Storicamente, una pagina HTML poteva: 
>```html
> <form method="GET" action="/search">
><form method="POST" action="/login">
>```
>
>**GET e POST sono sempre stati permessi**  
> **PUT, PATCH, DELETE non sono mai stati supportati dai form HTML**
> 
> Questo significa che: 
> - milioni di siti hanno sempre inviato `POST` cross-origin
>   
>- bloccarli avrebbe **rotto il Web.**
>  
> Ovviamente anche `POST` è "sicuro" fin tanto che rispetta tutti i criteri delle Simple Requests 
>
>>[!example] **Esempio in cui scatta la preflight request con `Post`**
>>```js
>>fetch('/api/users', {
  >>	method: 'POST',
  >>	headers: {
  >> 		 'Content-Type': 'application/json' //Header che non rispetta i criteri delle Simple Requests
  >>},
  >>	body: JSON.stringify({ name: 'Mario' })
>>});
>>
>>```
>
>


### Richieste non semplici e Preflight Request
Quando una richiesta **esce dai criteri delle Simple Requests**, il browser la considera **potenzialmente pericolosa**.

In questi casi entra in gioco il meccanismo delle **Preflight Requests**.

###### Esempio di richiesta che genera preflight 
```js
fetch('http://localhost:3001/users', {
  method: 'DELETE',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  }
});
```
Motivi del preflight:

1.  metodo non "semplice" ;
	-  `PUT`
    
	- `PATCH`
    
	- `DELETE` 
    
2.  header personalizzati: 
	-  `Authorization`
    
	- `X-Custom-Header`
    
	- `Content-Type: application/json`
    
	- `Content-Type: application/json`.
3. Oppure entrambi: 
	- Esempio tipico: 
```js
fetch('/api/users/1', {
  method: 'DELETE',
  headers: {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
  }
});
```

Qui **Preflight obbligatoria**, perché:

- il metodo è “pericoloso”;
    
- l’header `Authorization` può esporre dati sensibili.

#### Cos’è una Preflight Request

Una **Preflight Request** è una richiesta HTTP **[[Lezione 8 - Chiamate Curl#Il metodo OPTIONS|OPTIONS]]** che il browser invia **automaticamente prima della richiesta reale**.

Il suo scopo è semplice:

> ==**chiedere al server se la richiesta che il client vuole inviare è consentita**.==

L’utente o lo sviluppatore **non la scrive manualmente**: è il browser a gestire tutto il processo.

##### Flusso completo di una Preflight Request

**Scenario:**
Immaginiamo di avere una chiamata di questo tipo 
```js
fetch('http://localhost:3001/users/1', {
  method: 'DELETE',
  headers: { 'Authorization': 'Bearer abc123' }
});
```

###### Cosa accade “dietro le quinte”

**STEP 1 – Preflight automatico del browser**
```http
OPTIONS /users/1 HTTP/1.1
Host: localhost:3001
Origin: http://localhost:3000
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: Authorization
```

Il browser chiede:

- “Posso usare DELETE?”
    
- “Posso inviare l’header Authorization?”
    
- “Da questa origine?”

**STEP 2 – Risposta del server**
```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
```

Il server autorizza esplicitamente l’operazione.

**STEP 3 – Invio della richiesta reale**
Solo dopo una risposta positiva al preflight, il browser invia la richiesta effettiva:
```http
DELETE /users/1 HTTP/1.1
Host: localhost:3001
Origin: http://localhost:3000
Authorization: Bearer abc123
```

#### Header CORS principali

Durante questo scambio, entrano in gioco alcuni header fondamentali:

##### Header inviati dal browser (preflight)

- `Origin`
    
- `Access-Control-Request-Method`
    
- `Access-Control-Request-Headers`
    

##### Header restituiti dal server

- `Access-Control-Allow-Origin`
    
- `Access-Control-Allow-Methods`
    
- `Access-Control-Allow-Headers`
    
- `Access-Control-Allow-Credentials`
    
- `Access-Control-Max-Age`
    

Questi header **determinano se la richiesta verrà eseguita o bloccata**.


> [!example] **In sintesi:**
> Le **Simple Requests** (come la maggior parte delle `GET`): vengono inviate direttamente dal browser perché utilizzano metodi e header considerati **a basso rischio**.
>
>Le richieste che usano **metodi non sicuri** (`PUT`, `PATCH`, `DELETE`) o **header non standard** fanno invece scattare una **Preflight Request (OPTIONS)**.
>
>In questi casi, il browser **chiede preventivamente al server se l’operazione è consentita**, prima di inviare la richiesta reale.
