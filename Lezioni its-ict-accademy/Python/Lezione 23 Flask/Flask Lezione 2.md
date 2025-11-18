
# Rest E Flask


## Che cos'è REST 

Rest è l'archittettura per costruire siti web, un modo che un client richiede risorse a un server. 
È uno dei modi per organizzare un archittettura client-server.
Cos'è una risorsa: 

Per comodità le applicazioni che usano l'archittettura Rest usano l'HTTP.
Le risorse sono identificate dagli URI, su internet diventano URL. 
mentre RESTful si integra con flask.
Oltre a Flask, che è la parte implementativa, rest sta per 
è uno standard che viene eseguito per far si che due applicazioni web possano comunicare tramite protocollo HTTP

### I principi fondamentali
Rest è uno standard per l'architettura [[Reti di computer#1. Modello Client/Server|Client-Server]]:
- Il [[Reti di computer#^81dc1c|client]] è rappresentato dal browser durante la navigazione web tramite il quale inviamo richieste al server, 
- mentre il [[Reti di computer#^b4e999|server]] è il server che eroga servizi e gestisce le richieste e i dati.
Per semplificare il codice il server è stateless: cioè non tiene traccia della richiesta del cliente quindi ogni richiesta è indipendente ed è un vantaggio perché fa in modo che il server non si sovraccarica.
Ogni volta che il client fa una richiesta la richiesta deve essere completa: deve contenere tutte le risorse e le informazioni che riguardano quella risorsa.
Utilizza il protocollo HTTP come protocollo di comunicazione. 
QUalsiasi cosa è considerato una risorse: pagine web, utienti, ecc. 
La risorsa è identificata dall'URI: simile all' URL ma serve a identificare le risorse.
Un URL è sempre un URI mentre URI è un concetto un po più ampio: l'URI identifica le risorse mentre gli URL localizza le risorse ma le identifica anche.
Esistono tanti URI che sono endpoint ma c'è ogni endpoint per ogni URI e non è vero il contrario. 
Ad esempio: 
i path di FLask sono URI man durante la navigazione web usiamo gli URL.
Utilizzando HTTP utilizza i metodi GET, Post, PUT, DELETE.
I dati vengono rappresetnati con JSON e XML, quindi lo scambio avviene in questi due formati.
Inoltre abbiamo una cache per salvare le rispote in modo temporaneo e vengono salvate nel client.
Ad esempio abbiamo la cache del browser che ogni tanto deve essere svuotata.

### REST: i vantaggi

Semplicita: utilizza standard HTTP esistenti 

Scalabilità: essedno stateless ogni richiesta è indipendente quindi il server non memorizza le richieste e quindi il server può gestire ed erogare più servizi contemporaneamente per più client. 

Flessibilità: supporta diversi fomranti per richieste e risposte; il formato più utilizzato è il JSON ma ciò non toglie che non se ne possono usare altri formati.

Interoperabilità: funziona con qualsiasi piattaforma e con qualsiasi linguaggio; l'importante è che si utilizzi l'HTTP. 

Seprarazione: client e server sono indipendenti; ognuno di queste due entità  funzionano in maneira indipendente

### Risorse e URI

QUalsiasi cosa è cosiderata una risorsa: è una entità di dominio per analogia sono gli oggetti in analisi concenttuale.
Tutto viene identificato da URI e chiamato risorsa: se nel nostro dominio

URI sono sotantivi e non verbi: URI identifica risorse e non azioni; l'azione è definita dai verbi HTTP quindi URI sono sostantivi.
Se dovessimo accedere a una collezzioni di Utenti se definisco un URI come accediUTenti è sbagliato, devo solo scrivere Utenti.
In sintesi gli URI sono oggetti.
BIsogna utilizzare il plurale per le correzzioni: 
	se si deve accedere a una collezzioni di utenti definiamo utenti, se dovessimo accedere a un singolo utente devo definire `Utenti/id_utente` : sto accedendo alla collezzioni utenti a quell'id specifico del singolo utente. 
Esempi: 

```plain
GET #rappresenta l'azione /libri # in questo modo si ottiene la collezzioni di libri

GET /libri/5 #Ottengo la collezioni libri e accedo alla singola risorsa identificato con ID 5 

POST #permette di creare una nuova risorsa /libri  #Creo una nuova risorsa di collezzioni libri 

PUT #Aggiorna interamente una risorsa /libri/5 #Accedi alla risorsa con ID 5 nella collezzioni libri e aggiornala 

DELETE   /libri/5 #Elimino la risorsa con ID 5 all'intenro della collezzioni libri 

```

Esempi scorretti: 
```plain
GET /ottientiLibri

POST /creaLibro

DELETE /cancellaLibro/5
```


### Metodi HTTP e operazioni CRUD(Create, Read, Update, Delete)



| Metodo HTTP | Operazione CRUD | Descrizione        | Idempotente |
| ----------- | --------------- | ------------------ | ----------- |
| GET         | Read            | Recupera Risorse   | Si          |
| POST        | Create          | Crea Nuove Risorse | No          |
|             |                 |                    |             |

GET corrisponde alla azione di leggere/recuperare risorse quindi quando il cient 

La get è idempotente: se si esegue più volte la stessa azione il risultato non cambia, la risorsa non viene modificata.
Get è cacheable: le rispote date più di frequente al client vengono messe in una cache 

POST; crea nuove risorse all'interno di una collezzione: se si ha una collezione e devo creare risorse uso Post, ma se uso POST per una collezione con risorse già esistente crea una collezione nuova e non sovrascrive quella già esistente.
Difatti non è idempotente. 
POST crea e popula una collezione 

La moaggior parte dei casi se ho una collezione e la devo populare uso POST

PUT: è idempotente serve per aggioranre la risorsa che gia esiste; Per populare una collezione uso POST ma per aggiornare tutti i campi della risorsa, ad esempio utente uso PUT.
Più richeste PUT uguali no ncambiano il risultato. 

Dove è più conveneinte usare PUT anziché POST: ad esempio su whatsapp che si usano emoji per rispondere alle reaction dei messaggi uso PUT, ad esempio quando si risponde con una faccina che ride si usa PUT che crea l'emoji e sfrttando l'idempotenza di PUT aggiorna la reaction senza che venga aggiunto un nuovo emoji alla reaction dello stesso messaggio.
Ma quando inviamo un messaggio usiamo POST perché se scrivo 100 volte "ciao" vengono creati 100 messaggi con contenuti "ciao"

PATCH: si usa per una modifica parziale di un solo campo; esempio se si deve aggiornare il campo PAssword di Utente ed non è idempotente; perché la patch essedno una modifica parziale due PATCH consecutive possono cambiare il risultato. 

Mettiamo di avere un URI `Libri/5` e mettiamo di avere un numero di pagine che volgio modificare e quindi come payload devo scrivere `pagine:"+10"` devo scrivere 

```
PATCH /libri/5
{
	'pagine': "+10"
}
```

QUesto non è idempotente perché ogni volta aggiunge +10 pagine, mentre con PUT devo scrivere 

```
PUT /libri/5
{
	'pagine': "110"
}
```
Questa richiesta eseguita più volte non cambia il risultato ma se scriverssi : 
```
PUT /libri/5
{
	'pagine': "130"
}
```
La risorsa viene aggiornata completamente. 

La patch permette di sostituire con valori calcolabili, PUT no. 

DELETE cancella una risorsa ed è idempotente: il risultato non cambia perché una volta cancellata la risorsa non c'è più. 
Con DELETE devo specificare la risorsa che voglio cancellare a meno che non si vuole cancleaare una collezione. 

### Codici di Stato HTTP
QUando il client effettua una richiesta al server ci sono codici di stato che sono contenuti nella risposta del server che spiegano al server come andata la richiesta.
Questi codici sono standardizzati e sono le risposte quando il client effettua una richiesta 

#### La famiglia 200: 2xx - Successo
SOno i messaggi di successo 
- 200: Richiesta soddifsatta/completata
- 201: la risorsa è stata creata (tipica del post)
- 204 (No content): La richiesta è risucita ma non c'è nulla da restituire(ad esempio il DELETE).

#### La famiglia 400: 4xx - Errori Client
Famiglia errori lato client
- 400 Bad Request: il server non riconosce la richiesta perchè, ad esempio. il client manda un JSON malformato (`ValueError` in Python )
- 401 Unathorized: quando il client effettua una richiesta al server ma non ha l'autorizzazione richiesta
- 403 Forbidden: il server ha capito che risorsa volevo ma si rifiuta di darla, ad esempio perché l'utente non ha i permessi o perché ad esempio l'utnete vuole fare qualcosa che non può fare.
- 404 Not Found: La risorsa non è stata trovata; il client tenta di accedere ad una risorsa che non esiste perché all'URI sbalgiato 
- 405 Method Not Allowed: 
- 409: conflitto di stato; se abbiamo la stessa risorsa aggiornatan simultaneamente e il server non sa quale aggiornamento ridare al client. 

#### LA famiglia dei 500: 5xx - Errori Server
Famiglia errori lato server 
- 500: Internal Server Error: l'errore più generico; dovito a bug intenri al server o problemi di manutenzione 


Possiamo pure creare i nostri codici ma è sbalgiato farlo perché non sono lo standard 
### JSON come Standard per REST 
Il JSON è lo standard per lo scambio dati tra server e client; è facilmente leggibile simile a un dizionario Python o un ogetto di programmazione.
Quindi guardandolo a colpo d'icchio si capisce cosa stiamo formattando.
È facilmente covertibile in  oggetto JS ma è supportato in tutti i linguaggi di programmazione.
Il parsign è efficiente: viene letto ed elaborato efficientemente dai calcolcatori ed è più leggero e meno ridonante del XML e ha una struttura gerarchica.
Esempio: 
```json
{
	'id': 1,
	"titolo": "1984",
	"autore": "George Orwell",
	"isbn": "978"
}
```

### API 
API sta per Apllication Programming Interface, sono un ponte che peremttono a due sofwatre di parle tra loro.
Un insieme di regole e strumenti che spiegano come un programma può comunicare con un altro programma. 
Le API sono l'insieme degli endpoint 
Con le API andiamo a definire le richieste di un client può fare a un server:
se si definisce la regola `GET /libri`
si sta definiendo che il cient puo leggere le risorse nella collezzione libri del server.
Abbiamo un HTTP: `https://api.biblioteca.it/v1`
```
GET /libri #lista dei libri

GET /libri?genere=fantasy #filtro per genere 

GET /libri/123 #Dettaglio per genere 

POST /libri #Aggiungi libro 

PUT /libri/123 #Aggiorna libro

DELETE /libri/123 #Elimina il libro 

GET /autori #Lista autori

GET /autori/456/Libri #libri di un autore  
```

L'insieme dei verbi HTTP e degli URI formano l'API.
LE API definiti con i principi REST sono definiti come API RESTful. 
DIfatti poco sopra abbiamo della API RESTful perché seguono i principi REST.
Quindi le API sono regole e strumenti che permettono la comunicazione tra due programmi; quindi definiamo cosa si può fare.

Per ogni verbo HTTP relativo a quella risorsa la mia API può eseguire quelle azioni specifiche per quella risorsa; quindi le API permettono di definire le azioni da compiere seguendo l'URL base. 

(Formato OPenAPI).

Quindi quando si va ad implmentare questo path `https://api.biblioteca.it/v1` devo anche implementare un metodo GET, POST, PUT, DELETE. 
QUesti metodi vanno scritte in una documentazione API che vengono indfine implementati a livello codice. 

### Richardson Maturity Model 
È un modello di 4 livelli che permettono di misurare quanto le API che abbiano definito rispettano i principi di REST. 
A seconda della aratteristiche della nostra API posso collocare le mie API

#### Livello 0 - The swamp of POX 

Le caratteristiche le api utilizzano un solo ENDPoint e utilizzano sempre  metodi POST, e l'azione da compiere non è contenuto nel metodo HTTP ma è contenuto nel JSON della risposta: 
```json
POST /api
Content-Type: application/json
{
	"action": "getBook",
	"bookid": 5
}
```

```json
Post /api
Content-Type: application/json
{
	"action": "createBook",
	"title": "Nuovo Libro",
	"athor": "Autore"
}
```

Io posso fare la mia applicazione definendo `/api` e tutte le impostazioni sono messe nel body della richiesta HTTP. 
QUesto metodo pero non sfrutta i verbi HTTP eccetto Post. 
Il web funziona bene e veloce per via della cache: se il client fa una richiesta per una applicazione quella richiesta viene memorizzata nella cache quindi quando si riaccede a quella richiesta la richiesta è stata momentaneamente memorizzata e accedere alla apllicazione diventa più veloce.
Cosi facendo pero non si accede alla cache. 


In questo livello non ripesttano i principi REST: 

#### Livello 1 : risorse multiple 
Anzichè avere un solo Endpoint abbiamo diversi enpoint per accedere alle diverse risorse (URI differenti).
Non andiamo nello stesso path, ma abbiamo un URI diverso per ogni risorsa ma abbiamo diversi path ma abbiamo solo post 
Un po meglio, ma chiaramente devo guardare dentro il JSON per capire se creare la collezione o modificarla 

#### Livello 2: HTTP + Codici di stato  
Vengono introdotti i verbi HTTP e i codici di stato 
In questo caso non abbiamo il solo POST ma abbiamo i diversi metodi HTTP. 
Questo livello cadono le diversi API moderne , qui abbiamo i metodi e i sostantivi URI per le risorse. 
QUindi vengono implementati anche i diversi errori che accandono quando le azioni non vanno a buon fine o viceversa. 
```
GET /libri/5
POST /libri
PUT /libri/5

```
#### Livello 3: HATEOAS

Dove abbiamo tutto cio che è alla base del livello 2 solo che il server guida il client nella risposta attreverso link detti ipermediari: 
si manda la richiesta dal client al server ma nella risposta del server prevedo tutti i possibili endopoint che guidano la risposta del server e guida il client nelle diverse azioni da eseguire.
Oltre a rispondere come livello 2 ma la richiesta contiene anche i link alle altre richieste che il client può fare. 


```json
HTTP/1.1 201 Created
Content-Type: application/json
{
	"id": 5,
	"titolo": "1984",
	"_links":{
		"self": {"href":"/libri/5"},
		"_edit": {"href":"/libri/5", "method":"PUT"},
		"delete": {"href":"/libri/5", "method":"DELETE"},
		"author": {"href":"/autori/42"},
		"reviews": {"href": "/libri/5/recensioni"}
	}
}
```