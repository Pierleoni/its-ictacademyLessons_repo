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
Questi "vincoli" non sono regole arbitrarie, ma principi di progettazione che, se seguiti, garantiscono che un'architettura sia scalabile,
semplice e affidabile, proprio come il web stesso
Uno dei vincoli più importanti di REST è la **statelessness**.
#### Vincolo Statelessness 
- **Significato**: 
	- ==Ogni richiesta inviata dal client al server deve contenere tutte le informazioni necessarie per essere compresa ed elaborata.==
    
- **Nessuna sessione sul server**: 
	- ==Il server non memorizza dati tra le richieste. Se il client ha bisogno di autenticazione, deve inviare le credenziali in ogni richiesta.==
    

> [!done]
> ###### **Perché è fondamentale?**
> 
> - **Scalabilità**: 
> 	- ==Qualsiasi server può gestire qualsiasi richiesta, facilitando la distribuzione del carico.==
>     
> - **Affidabilità**: 
> 	- ==In caso di errore, la richiesta può essere reinviata a un altro server senza problemi.==
>     
> - **Semplicità**: 
> 	- ==La logica del server è più semplice, perché non deve gestire sessioni.==
>     

> [!example] **Analogia della pizzeria**: 
>  
> Immagina una pizzeria dove ogni cameriere può servire qualunque tavolo perché lo stato dell’ordine è centralizzato nel sistema. 
>> [!done] Vantaggio: facilità di distribuzione del lavoro. 
>> 
>
>
>>[!failure] Svantaggio: nessun cameriere conosce le preferenze dei clienti; ogni interazione è autonoma.


#### Interazione basata su Risorse 
REST ruota attorno al concetto di **risorsa**, identificata da un URL unico. Ogni operazione viene effettuata tramite i verbi HTTP standard:

- `GET /utenti/123` → Recupera la risorsa “utente 123”
    
- `POST /utenti` → Crea una nuova risorsa “utente”
    
- `PUT /utenti/123` → Aggiorna completamente la risorsa “utente 123”
    
- `DELETE /utenti/123` → Elimina la risorsa “utente 123”
    

L’interfaccia diventa prevedibile e coerente, basandosi sulla manipolazione di **oggetti e risorse** tramite operazioni standard.

### **Architettura Stateful (Con Stato)**

In un’architettura **stateful**: 
- ==il server crea e mantiene una **sessione dedicata per ciascun client**.== 
- ==Questo significa che il server “ricorda” chi è il client e tiene traccia di tutte le sue interazioni precedenti.==

> [!example] **Analogia:**
>  immagina una pizzeria di lusso dove ogni cliente ha **un cameriere personale** per tutta la durata della cena.
> 
>> [!done]  **Vantaggio**: 
>> il cameriere conosce le preferenze del cliente (“il solito?”) e lo stato preciso del suo ordine, offrendo un servizio più personalizzato e immediato.
>   
>  
>>[!failure]  **Svantaggio**: 
>>modificare l’ordine può essere più complicato se non si passa dal cameriere assegnato. 
>>Se arrivano molti clienti contemporaneamente, il carico di lavoro non si distribuisce facilmente, perché ogni cameriere è legato ai propri tavoli.

    

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
>  ogni cliente ha un cameriere personale. 
>> [!done]  Vantaggi: servizio più personalizzato. 
>> 
>
>
>> [!failure] Svantaggi: difficoltà nel gestire grandi numeri di clienti e carichi variabili.
