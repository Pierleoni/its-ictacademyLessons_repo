# Introduzione 
Nelle lezioni precedenti abbiamo analizzato i meccanismi fondamentali alla base della comunicazione tra client e server: il funzionamento del [[Lezione 3; Protocollo HTTP; il Modello TCP- IP, il Modello ISO-OSI e la comunicazione tra livelli|protocollo HTTP]], la struttura delle richieste e delle risposte, il ruolo degli [[Lezione 4 - Protocollo HTTP 2 parte#^header|header]] e del [[Lezione 4 - Protocollo HTTP 2 parte#^body|body]], fino ad arrivare al [[Lezione 5 - Il Formato JSON|formato JSON]] come standard moderno per lo scambio dei dati. 
Abbiamo inoltre introdotto il concetto di [[Lezione 6 - API|API]] e visto come queste espongano risorse accessibili tramite [[Lezione 6 - API#Endpoint|endpoint]] ben definiti, utilizzando [[Lezione 6 - API#Payload|payload]] strutturati per trasmettere informazioni in modo chiaro e interoperabile.

Il passo successivo consiste nel comprendere **come organizzare** questi elementi in un vero e proprio modello architetturale. In altre parole: quando progettiamo un sistema basato su API, quali regole seguiamo per rendere la comunicazione semplice, prevedibile e scalabile?

A questa esigenza risponde **REST (REpresentational State Transfer)**:
uno stile architetturale che si è affermato come lo standard de facto per la realizzazione delle API web moderne. 
REST fornisce un insieme di principi e convenzioni che guidano la progettazione di servizi web facilmente utilizzabili, interoperabili e aderenti ai meccanismi naturali del protocollo HTTP.

## Sistemi REST 
==REST (_REpresentational State Transfer_) è uno **stile architetturale** basato su un insieme di vincoli, linee guida e buone pratiche pensate per progettare sistemi distribuiti semplici da usare, scalabili e coerenti.== 
È importante chiarire sin da subito che ==**REST non è un’architettura completa**, né una tecnologia specifica.==  
Non è un protocollo, non è un framework, non è una libreria:  
- ==è un **modello di progettazione** che definisce come strutturare un sistema affinché sia prevedibile, chiaro e soprattutto interoperabile.==

L’obiettivo principale di REST è offrire un riferimento comune per evitare che ogni sviluppatore implementi API a modo proprio, generando sistemi incoerenti, difficili da integrare e complicati da mantenere nel tempo. 
Quando un servizio rispetta i vincoli e i principi di questo modello, si dice che è un sistema **RESTful**.


> [!NOTE] 
> #### Origini e contesto storico
> L’idea di REST nasce nel 2000 all’interno della tesi di dottorato di **Roy Fielding**, intitolata _Architectural Styles and the Design of Network-based Software Architectures_. Quell’anno rappresentava un momento cruciale per l’evoluzione del web:
>
>- Internet cresceva rapidamente a livello globale
  >  
>- Le applicazioni distribuite diventavano sempre più complesse
 >   
>- Le tecnologie disponibili erano spesso pesanti, rigide e poco intuitive
  >  
>- Il web stesso dimostrava che semplicità e standardizzazione potevano ottenere risultati enormi
  >  
>
>In questo scenario, Fielding analizzò i punti di forza del web e cercò di formalizzarli in un modello chiaro e generale, capace di guidare la progettazione dei futuri sistemi distribuiti. Così nacque REST.
>
>#### Chi era Roy Fielding 
> Fielding non era soltanto uno studioso, ma uno dei principali protagonisti dell’evoluzione del web. Tra i suoi contributi più importanti:
>
>- co-fondatore del progetto **Apache HTTP Server**, che per anni è stato il web server più utilizzato al mondo
 >   
>- autore principale delle specifiche **HTTP/1.0** e **HTTP/1.1**
 >   
>- co-fondatore della **Apache Software Foundation**
  >  
>- membro attivo del **W3C**, il consorzio che definisce gli standard del web
 >   
>
>Questa posizione privilegiata gli permise di osservare contemporaneamente sia le difficoltà reali degli sviluppatori sia i limiti teorici dei modelli distribuiti dell’epoca.
>
>#### Prima di REST:  un panorama frammentato e complesso
>Prima del 2000, la realizzazione di sistemi distribuiti era spesso un percorso tortuoso. Tra le tecnologie più utilizzate:
>
>- **CORBA**: molto potente, ma estremamente complessa e difficile da manutenere
  >  
>- **RPC (Remote Procedure Call)**: cercava di nascondere la natura distribuita, provocando problemi di affidabilità
  >  
>- **SOAP**: formalmente rigoroso, ma eccessivamente verboso e basato su messaggi XML pesanti
  >  
>- Tecnologie proprietarie: ogni azienda implementava protocolli personalizzati, incompatibili tra loro
 >   
>
>Il risultato era un ecosistema caotico:  
>- servizi poco interoperabili, scarsa scalabilità, implementazioni difficili da integrare e sistemi in cui client e server erano troppo strettamente legati.
> #### I problemi che REST voleva risolvere
>REST nacque quindi con l’obiettivo di affrontare alcune criticità ricorrenti nei sistemi distribuiti:
>
>- **eccessiva complessità** delle tecnologie dell’epoca
  >  
>- **accoppiamento troppo stretto** tra client e server
  >  
>- **scarsa scalabilità**, soprattutto sotto carichi elevati
  >  
>- **difficoltà di interoperabilità** tra sistemi diversi
  >  
>- **mancanza di un modello condiviso** per la progettazione delle API
  >  
>
>Analizzando ciò che aveva reso il web così efficace, Fielding estrasse una serie di principi che – se applicati correttamente – avrebbero permesso di creare sistemi semplici, prevedibili e facili da integrare.  
>Da qui nasce REST, lo stile architetturale che oggi costituisce la base della maggior parte delle API web moderne.  

### Le motivazione fondamentali di REST 
Alla luce di ciò le motivazioni fondamentali delle REST sono: 

##### 1. Semplicità

==Il principio guida di REST è eliminare la complessità superflua.==  
Invece di inventare un nuovo protocollo di comunicazione, REST utilizza l’**HTTP**, che già governa il web, con vantaggi significativi:

> [!done] La semplicità di REST
> 
> - **Curva di apprendimento ridotta**: 
> 	- ==Gli sviluppatori conoscono già i verbi HTTP (GET, POST, PUT, DELETE, ecc.) e i codici di stato (200, 404, 500, ecc.), senza dover apprendere nuovi standard complessi.==
>     
> - **Niente “buste” complicate**: 
> 	- ==A differenza di protocolli come SOAP, che avvolgono ogni messaggio in strutture XML complesse, le richieste REST sono dirette e leggibili.==
>     
> - **Debugging facilitato**: 
> 	- ==Le richieste REST sono semplici messaggi di testo che possono essere facilmente ispezionati con strumenti di sviluppo di qualsiasi browser.==
>     

_Esempio_: Una richiesta REST GET a `/utenti/123` è immediatamente comprensibile, mentre in SOAP sarebbe necessario costruire un intero documento XML.

##### 2. Scalabilità

==REST è progettato per gestire sistemi con **alto numero di utenti e richieste simultanee**.== 
Alcuni principi chiave che permettono questa scalabilità sono:

> [!done] Principi chiave
> 
> - **Stateless (senza stato)**: 
> 	- ==Ogni richiesta contiene tutte le informazioni necessarie per essere elaborata. Il server non mantiene alcuna memoria dello stato del client tra una richiesta e l’altra. Questo permette di distribuire il carico su più server senza problemi.==
>     
> - **Caching**: 
> 	- ==Le risposte possono essere memorizzate temporaneamente (client o nodi intermedi) riducendo il numero di richieste al server e migliorando le prestazioni.==
>     
> - **Sistema a livelli (Layered System)**: 
> 	- ==Tra client e server possono esserci più livelli intermedi, come proxy o bilanciatori di carico, senza che client o server debbano modificarne il comportamento.==
>     

##### 3. Indipendenza

==REST favorisce **disaccoppiamento e interoperabilità** tra client e server==:

> [!done] Caratteristiche
> - **Indipendenza di piattaforma e linguaggio**: 
> 	- Un client JavaScript può comunicare con un server Python, Java o qualsiasi altra tecnologia senza problemi.
>     
> - **Evoluzione indipendente**: 
> 	- Client e server possono essere aggiornati separatamente, purché il contratto dell’API non venga rotto.
>     
> 

Questi vincoli garantiscono che un’architettura RESTful sia **scalabile, semplice e affidabile**, proprio come il web stesso.


### **Vincolo “Stateless” (Senza Stato)** e Risorse
I sistemi REST si basano su un insieme di vincoli pensati per garantire:
- **scalabilità**, 
- **semplicità** 
- **affidabilità**, 
seguendo gli stessi principi che hanno reso il web un sistema robusto. 
Tra questi vincoli, uno dei più importanti è quello della **statelessness**.
#### 1. Vincolo Statelessness 
- **Significato**: 
	- ==Un servizio è stateless quando ogni richiesta inviata al server contiene già tutte le informazioni necessarie per essere capita ed elaborata, senza che il server debba ricordare nulla di quanto avvenuto in precedenza.==
    
- Di conseguenza non vi è **nessuna sessione sul server**: 
	- ==Il server **non mantiene sessioni** né stato tra una richiesta e la successiva. == 
	- ==Se il client deve dimostrare la propria identità o passare parametri, deve farlo **ogni volta**, includendo le informazioni nella richiesta.==
    

> [!done]
> ###### **Perché è fondamentale?**
> 
> - **Scalabilità**: 
> 	- ==Qualsiasi server dell’infrastruttura può gestire qualsiasi richiesta, favorendo il bilanciamento del carico e semplificando l’aggiunta di nuovi nodi.==
>     
> - **Affidabilità**: 
> 	- ==Se un server ha un problema, la richiesta può essere ripetuta verso un altro server, senza perdere informazioni sul contesto.==
>     
> - **Semplicità**: 
> 	- ==Il server non deve gestire sessioni o memorie temporanee, riducendo complessità e possibilità di errore.==
>     

> [!example] **Analogia della pizzeria**: 
>  
> Immagina una pizzeria in cui **non esiste un cameriere dedicato a un determinato tavolo**.  
>Tutti i camerieri possono servire chiunque, perché ogni ordine contiene già tutto ciò che serve per essere preparato.
>> [!done] Vantaggio: il lavoro si distribuisce facilmente.
>> 
>
>
>>[!failure] Svantaggio: nessun cameriere conosce preferenze o storicità del cliente; ogni ordine è indipendente.
^analogiaPizzeriaStateless

#### 2. Interazione basata su Risorse 
REST organizza il sistema attorno al concetto di **risorsa:** 
- ==ciascuna identificata da un URL unico.== ^risorsa

Le operazioni sulle risorse seguono i verbi standard di HTTP, che conferiscono coerenza e prevedibilità all’interfaccia.

- `GET /utenti/123` → Recupera la risorsa “utente 123”
    
- `POST /utenti` → Crea una nuova risorsa
    
- `PUT /utenti/123` → Sostituisce completamente la risorsa esistente
    
- `DELETE /utenti/123` → Elimina la risorsa
    

Questa combinazione di **URL + verbi HTTP** rende l’interazione semplice, intuitiva e altamente standardizzata.

### **Architettura Stateful (Con Stato)**
Per comprendere meglio il vantaggio del modello [[#1. Vincolo Statelessness|stateless]], è utile confrontarlo con l’approccio tradizionale **stateful**, dove il server mantiene un **contesto** per ogni client.

In un’architettura **stateful**: 
- ==il server crea e mantiene una **sessione dedicata per ciascun client**.== 
- ==Questo significa che il server “ricorda” chi è il client e tiene traccia di tutte le sue interazioni precedenti.==

> [!example] **Analogia: la pizzeria con cameriere personale**
>  immagina una pizzeria di lusso dove ogni cliente ha **un cameriere personale** per tutta la durata della cena.
> 
>> [!done]  **Vantaggio**: 
>> il cameriere conosce le preferenze del cliente (“il solito?”) e lo stato preciso del suo ordine, offrendo un servizio più personalizzato e immediato.
>   
>  
>>[!failure]  **Svantaggio**: 
>>modificare l’ordine può essere più complicato se non si passa dal cameriere assegnato. 
>>Se arrivano molti clienti contemporaneamente, il carico di lavoro non si distribuisce facilmente, perché ogni cameriere è legato ai propri tavoli.
>>Inoltre, se il cameriere assegnato si assenta, la continuità del servizio si interrompe.
^analogiaPizzeriaStateful

    

**Vantaggi principali:**

- **Performance**: 
	- ==le richieste possono essere più leggere, poiché il server conosce già il contesto e lo stato del client.==
    
- **Esperienza utente**: 
	- ==l’interazione risulta più fluida e contestualizzata, simile a una conversazione continua.==
    

**Svantaggi principali:**

- **Scalabilità limitata**: 
	- ==è più difficile distribuire il carico su più server, perché ciascun client è legato a un server specifico.== 
	- ==Reindirizzare la richiesta a un altro server può causare problemi, in quanto quest’ultimo non conosce lo stato della sessione.==
    
- **Maggiore complessità e costi**: 
	- ==gestire sessioni dedicate aumenta la complessità del server e rendere scalabile l’infrastruttura richiede più risorse.==
    
- **Fragilità**: 
	- ==se il server che mantiene la sessione si guasta, tutte le informazioni sullo stato dei client vanno perse, costringendo l’utente a ricominciare da capo==
### **Architettura Stateless vs Stateful**

- **Stateless (senza stato)**:
    
    - ==Il server non mantiene informazioni sul client tra le richieste.==
        
    - Vantaggi: 
	    - ==scalabilità,== 
	    - ==affidabilità,== 
	    - ==facilità di monitoraggio==.
        
    - Svantaggi: 
	    - ==il client deve inviare dati aggiuntivi (es. token) ad ogni richiesta.==
        
- **Stateful (con stato)**:
    
    - ==Il server mantiene una sessione per ogni client.==
        
    - Vantaggi: 
	    - ==migliore performance==  
	    - ==esperienza utente personalizzata==.
        
    - Svantaggi: 
	    - ==scalabilità limitata,== 
	    - ==complessità maggiore== 
	    - ==fragilità in caso di guasti==.
        

> [!example] **Analogia della pizzeria con camerieri dedicati**:
>  Quindi ritornando [[#^analogiaPizzeriaStateless|all'analogia della pizzeria in un sistema stateless]]: 
>Ogni cliente   non ha un cameriere personale.
 > [[#^analogiaPizzeriaStateful|Mentre in un sistema stateful]]: 
 >  ogni cliente ha un cameriere personale. 
>> [!done]  Vantaggi: servizio più personalizzato. 
>> 
>
>
>> [!failure] Svantaggi: difficoltà nel gestire grandi numeri di clienti e carichi variabili.



> [!faq] 
> #### Perché i Servizi Stateless Sono Più Convenienti ed Efficienti
> Uno dei motivi principali per cui i sistemi REST hanno avuto così grande successo è il **vantaggio economico** associato al modello **stateless**.
>
>Nei sistemi **[[#**Architettura Stateful (Con Stato)**|stateful]]**, ogni volta che un client interagisce con un server:
>==quest’ultimo deve mantenere una **sessione attiva**, cioè uno spazio di memoria dedicato in cui conservare informazioni sullo stato della conversazione (dati parziali, preferenze, step già completati, ecc.).==  
>Questa gestione dello stato, però, ha un costo molto elevato:
>
>- ==ogni sessione occupa memoria sul server,==
 >   
>- ==più client si collegano, più sessioni devono essere gestite,==
 >   
>- ==per scalare è necessario aggiungere server più potenti o nuovi nodi, con costi crescenti.==
 >   
>
>Con l’arrivo dei sistemi REST la logica cambia completamente: 
>- **la sessione lato server non è più necessaria**.  
>Il servizio diventa **[[#Vincolo Statelessness|stateless]]:**  ==cioè ogni richiesta contiene già tutte le informazioni necessarie per essere processata, senza dover dipendere da una memoria condivisa precedente.==
>Questo approccio porta a due conseguenze fondamentali:
>
>1. Riduzione dei costi e aumento della scalabilità:
>
>	Poiché il server non deve più mantenere sessioni dedicate:
>
>	- ==si riduce l’uso di memoria e risorse.==
>    
>	- ==diventa molto più semplice distribuire il carico tra più server.==
>    
>	- ==ogni richiesta può essere gestita da qualsiasi nodo dell’infrastruttura.==
>    
>
>Il risultato è una scalabilità **più economica, lineare e affidabile**.
>
>2. Disaccoppiamento totale tra Client e Server
>
>	Nei servizi stateless, la gestione della “conversazione” viene spostata sul **client**, che è un programma eseguito su una macchina indipendente.
>
>	Questo significa che:
>
>	- ==le operazioni su più step (wizard, procedure multistep, form complessi, ecc.) vengono gestite temporaneamente dal client.==
  >  
>	- ==solo al termine di tutto il processo il client invia una chiamata completa al server, che la elabora senza dover conoscere gli step precedenti.==
 >   
>
>In questo modo, chi sviluppa il servizio lato server non deve preoccuparsi di come il client gestisce la sua interazione interna: può concentrarsi solo sulla logica della singola richiesta.


---

## La Scala di Maturità REST (Richardson Maturity Model)

Roy Fielding, nel definire i principi architetturali dello stile REST, ha anche ispirato l’elaborazione di un modello che permette di classificare il grado di aderenza di un sistema a tali principi. 
Questo modello è conosciuto come **Scala di Maturità di Richardson** (Richardson Maturity Model):
- suddivide le API in diversi livelli, dal più rudimentale al pienamente RESTful.

È importante sottolineare che non si tratta di una norma o di una legge formale: 
- ==è semplicemente uno strumento utile per comprendere **quanto profondamente un’API rispetti lo stile REST** e per valutare in quale direzione evolvere un sistema esistente.==
### Livello 0 – Il “Far West”

==Al livello zero troviamo i sistemi con il più basso grado di maturità.==  
In questa categoria rientrano le API che trattano l'interfaccia remota come un unico punto di accesso:
- spesso utilizzando un solo endpoint generico (ad esempio `POST /api`) per eseguire qualunque operazione.  
In questi sistemi **non esistono vere e proprie risorse**, né una differenziazione tra operazioni basate sui metodi HTTP. 
I vincoli REST sono completamente assenti e coesistono stili architetturali molto diversi, da qui il nome “Far West”.

### Livello 1 – Risorse

Il primo passo verso REST consiste nell'introduzione del concetto di **[[#^risorsa|risorsa]]:**
- ==rappresentata tramite URI specifici.==  

A questo livello l’API dispone di endpoint distinti per gli elementi del dominio (ad esempio `/clienti`, `/ordini`, `/prodotti`).  
Tuttavia, pur iniziando a separare le entità, **le operazioni sono ancora accentrate**: 
- ==spesso tutte le interazioni avvengono tramite un unico metodo HTTP (di solito `POST`).==  
Il sistema migliora in organizzazione, ma non sfrutta ancora la semantica del protocollo HTTP.

### Livello 2 – Verbi HTTP e Codici di Stato

Il livello 2 introduce un elemento fondamentale dello stile REST: 
- la **[[Lezione 4 - Protocollo HTTP 2 parte#^verbiHTTP|semantica dei metodi HTTP]]**.  
Ogni operazione viene espressa tramite il verbo più appropriato:

- [[Lezione 4 - Protocollo HTTP 2 parte#^04d1a5|`GET`]] per recuperare risorse
    
- [[Lezione 4 - Protocollo HTTP 2 parte#^9ffd01|`POST`]] per crearle
    
- [[Lezione 4 - Protocollo HTTP 2 parte#^523224|`PUT`]] o [[Lezione 4 - Protocollo HTTP 2 parte#^6cfc05|`PATCH`]] per aggiornarle
    
- [[Lezione 4 - Protocollo HTTP 2 parte#^595c2b|`DELETE`]] per eliminarle
    

Inoltre, il sistema utilizza i **[[Lezione 4 - Protocollo HTTP 2 parte#Status Code HTTP|codici di stato HTTP]]** per comunicare l’esito delle operazioni (ad esempio `200 OK`, `404 Not Found`, `201 Created`).  
Questo livello rappresenta nella pratica il traguardo raggiunto dalla maggior parte delle API moderne ed è già sufficiente per ottenere un'interfaccia ben progettata, chiara e comprensibile.

### Livello 3 – HATEOAS (Hypermedia as the Engine of Application State)

Il livello più alto della scala introduce il vincolo dell’**hypermedia**.  
In un sistema di livello 3: 
- ==ogni risorsa non contiene soltanto dati, ma anche **link che guidano il client** attraverso le possibili azioni successive.==  

In altre parole, lo stato dell’applicazione è determinato anche dai collegamenti ipermediali forniti dal server: 
- ==l’interazione diventa auto-documentata e dinamica.==

Si tratta del livello che più si avvicina all’architettura REST completa teorizzata da Fielding. 
Tuttavia, non sempre è necessario o conveniente implementarlo integralmente: ==molte API si fermano al livello 2 pur essendo progettate in modo efficace.==

Approfondiamo ogni livello 

#### Livello 0 – La “Palude” del POX (The Swamp of POX)
Il Livello 0 rappresenta il punto di partenza della Scala di Maturità REST: 
- ==è il gradino più basso, quello in cui un sistema utilizza il [[Lezione 3; Protocollo HTTP; il Modello TCP- IP, il Modello ISO-OSI e la comunicazione tra livelli|protocollo HTTP]] nel modo più semplice (e più limitato) possibile.== 
- L’acronimo **POX** significa **_Plain Old XML_** – anche se oggi potremmo parlare indifferentemente di _Plain Old JSON_ – e descrive un approccio in cui il server e il client si scambiano semplici messaggi strutturati senza alcuna attenzione ai principi del web.

##### **Come funziona un sistema POX**

A questo livello, l’HTTP non viene sfruttato come protocollo applicativo dotato di semantica propria, ma viene trattato come un semplice “tunnel” per invocare funzioni remote, in stile RPC (Remote Procedure Call).  
Le caratteristiche fondamentali sono:

- **Un unico endpoint**: 
	- ==esiste un solo URL che riceve tutte le richieste, indipendentemente dall’operazione da eseguire.==
    
- **Uso quasi esclusivo del metodo POST**: 
	- ==che si tratti di leggere, creare o eliminare dati, le richieste vengono inviate sempre allo stesso modo.==
    
- **Assenza del concetto di risorsa**: 
	- ==il sistema non espone elementi del dominio tramite URI significativi; lavora invece su “funzioni” o “comandi”.==
    
- **Messaggi sincroni**: 
	- ==client e server comunicano tramite scambio immediato di dati via HTTP, senza alcun meccanismo di navigazione tra stati.==
    

Il risultato è un’API che “parla” con il server, ma che non utilizza nessuno dei vincoli dello stile REST né la struttura naturale del web.

> [!faq] **Perché si parla di “palude”**
> 
> La metafora della palude (_swamp_) vuole evidenziare che questo approccio tende a diventare presto poco chiaro, confuso e difficile da scalare.  
> L’assenza di risorse, l’uso indistinto dei metodi HTTP e la concentrazione di tutte le operazioni in un unico endpoint portano a un codice meno leggibile, meno standard e più fragile.
> 
> In pratica, l’API funziona… ma senza alcun ordine architetturale.
> 
>
>> [!example] **Esempio pratico**
>>
> >Immaginiamo un sistema che deve gestire utenti.  
>> Una tipica API di Livello 0 espone un solo endpoint:
>>```
>> https://api.example.com/userService
>>
>>```
>
>
>A questo URL arrivano tutte le richieste, indipendentemente dall’azione da eseguire.
>
>1. **Richiedere i dati di un utente**  
 >   Anche per una semplice operazione di lettura, il client invia un POST.  
 >   L’intenzione (“getUser”) è indicata nel payload.
  >  
>2. **Creare un nuovo utente**  
 >   La richiesta è identica nella forma: sempre un POST allo stesso URL.  
 >   Cambia solo l’azione dichiarata nel corpo (ad esempio “createUser”).
 >   
>3. **Eliminare un utente**  
 >   Di nuovo un POST allo stesso endpoint, con un payload che indica “deleteUser”.
>    
>
>Il server interpreta il contenuto del messaggio e decide quale operazione svolgere.  
>In altre parole, **la logica dell’API non è espressa nell’URI o nei metodi HTTP, ma nascosta nel corpo della richiesta**.


#### **Caratteristiche principali dei sistemi POX**

I sistemi che rientrano nel Livello 0 condividono alcune caratteristiche strutturali molto semplici, che mostrano chiaramente come non sfruttino le potenzialità del web:

- **Comunicazione sincrona tramite HTTP:** il protocollo viene usato solo come mezzo di trasporto per scambiare messaggi. Nessuna delle sue funzionalità applicative viene realmente valorizzata.
    
- **Assenza del concetto di risorsa:** invece di esporre elementi del dominio tramite URL significativi, il sistema lavora con “funzioni” o “operazioni” remote, come in un classico modello RPC.
    
- **Uso minimo dei verbi HTTP:** tipicamente l’interazione si riduce a GET e soprattutto POST, utilizzati indistintamente per qualsiasi tipo di operazione (lettura, creazione, cancellazione).
    

Questi aspetti rendono il sistema funzionante, ma poco chiaro e scarsamente strutturato.



##### **Esempio pratico del Livello 0**

Per capire come si comporta un’API POX, immaginiamo un sistema che gestisce utenti.  
Un’API di Livello 0 espone **un unico endpoint**, responsabile di tutte le operazioni:
```plain
https://api.example.com/userService
```

Il client invia sempre lo stesso tipo di richiesta e indica l’azione da eseguire all’interno del payload.

1. **Richiedere i dati di un utente**  
    Anche se è un’operazione di sola lettura, si utilizza comunque il metodo **POST**.  
    Nel corpo della richiesta viene indicata l’azione, ad esempio `"getUser"`.
```json
POST /useService
Host: api.example.com
Content-Type: application/json
{
	"action": "getUser",
	"userId": 123
}
```
2. **Creare un nuovo utente**  
    La struttura della richiesta non cambia: sempre un POST allo stesso URL.  
    Nel payload compare l’istruzione `"createUser"` e i dati necessari alla creazione.
```json
POST /useService
Host: api.example.com
Content-Type: application/json
{
	"action": "createUser",
	"userData": {
		"name": "Mario Rossi",
		"email": "mario.rossi@example.com"
	}
}
```
    
3. **Eliminare un utente**  
    Ancora un POST verso lo stesso endpoint, con `"deleteUser"` specificato nel corpo.
    
```

```
In tutti i casi, il server deve leggere il payload e decidere quale funzione eseguire.  
L’URL non esprime alcun significato, e i verbi HTTP non aiutano a comprendere l’intenzione dell’operazione.  
Tutto è concentrato nel corpo del messaggio, rendendo l’API poco leggibile e meno standard.