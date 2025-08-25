Sta per Application Programming Interface, è l'interfaccia di programmazione che viene messa a disposizione dai programmatori per agire sull software stesso.
Prendiamo come esempio le promisises di JS: in quel caso abbiamo due modi per fare le promesis 
1. Fetch(). then
2. Async await 
Questi due modi mettono in comunicazioni il programmatore con un API di JS.
Quindi in sostanza le API sono anche un sistema di comunicazione per ricevere e mandare dati.
Di base però sono regole in che vengono date, entro le quali si può sviluppare codice.
Ad esempio su[ trello](https://www.atlassian.com/it/software/trello): ci danno degli endpoint(URL) a cui possiamo connetterci per mandare e riceve dati.
Per capire meglio:
Mettiamo di avere due sistemi;
Un sistema A scritto in PHP e un sisema B scritto in JAVA, questi due sistemi devono comunicare:
il sistema A invia Request e il sistema B manda delle response, questa comunicazione avviene sull HTTPS.
Quindi attraverso l'HTTPS possiamo fare delle chiamate dette GET o delle POST, PATCH, PUT, Delete (questi sono detti anche verbi HTTPS).
Quello che abbiamo fatto fino adesso abbiamo efettuato le chiamate a JSON Placeholder, queste chiamate si portano dietro dei verbi che però noi non abbiamo specificato.
Un altra app è [Postman](https://www.postman.com/), che permette di fare le chiamate ai diversi host su API (su Windows è possibile anche scaricare l'applicazione per testare chiamate in LocalHost).

### L'API come ponte tra programmi diversi
Questo è l'uso più comune del termine oggi e si riferisce alla comunicazione tra applicazioni sperate, che spesso  

Alcuni esempi di API: login di FB, login Google 
Si cihede l'autoriazzazione a google di iscirversi al sito tramite piattaforma e google genera automaticamente il token autorizzativo.

In java esistono le interfaccie: possono essere viste come contratti per creare la classe asosciata, e la classe deve avere la struttura che viene indicata dall'interfaccia.
Quindi le intrefaccie possono essere viste come contratti di progrmazzazione, stessa cosa per le API e per le UI.


Le api forniscono un livello di astrazione: non serve conoscere il complesso strutturata ad esempio di google per creare un sito web ma attraverso le regole delle API di google è possibile costruire siti web e codice da utilizzare sulla piattaforma di google.

IO posso sviluppare 10 interfaccie diverse per lo stesso server perchè utilizzo l'API, quindi uno dei vantaggi è lo sviluppo paralello: poiché le API fungono da "contratto" tra diverse parti di un sistema, i team possono laorare in parallello. Ad esempio, il team


API WEB 
API REST
API SOAP: quella più vecchia che lavora con l'XML, sia il client che il server devono sviluppare in contemporanea un file XML espondendo le request. 
API GraphQL

Un esempio pratico di API è la libreria di React s

API sicnrone e asincrone
ENDPOINt: e il punto di accesso specifico di un API(URL)
il Payload rappresetna i dati effettivi che vengono trasportati in una richiesta o in una risposta API. 


SISTEMI REST 
Sono API con ulteriori regole e sono un insieme di principi di design cche guidono la progettazione,
L'obiettivo è quello di regolomentare lo sviluppo di sistemi 
L'acronimo è Represetnation State Transfer.
Con le rest posso fare una chiamata JS a qualsisasi server, questo si chiama indipendenza 
L'interazione è basata sulle risorse 




