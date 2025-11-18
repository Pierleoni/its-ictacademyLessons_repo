# Comunicazioni delle reti di computer

Esistono principalmente **due modalità di comunicazione** nelle reti:
1. **Point-to point:**
	-    ==Si tratta di un collegamento **diretto** tra due dispositivi.==
	   
![[Point to point.png]]

- La rete è strutturata come una serie di **nodi** (PC, switch, router, ecc.) collegati tra loro.
    
- ==Ogni collegamento unisce due soli dispositivi alla volta==.
    

> [!abstract] Glossario
> - **Switch:** ==collega più dispositivi all’interno della stessa rete locale.==
>     
> - **Router:** ==collega reti differenti.==

In questo modello, i dati viaggiano da un dispositivo sorgente a un dispositivo destinatario, eventualmente passando attraverso nodi intermedi. 
==Solo il destinatario elabora il messaggio, mentre gli altri nodi lo inoltrano==.
2. **Broadcast:**
	 -   ==Si tratta di un collegamento **condiviso** tra più dispositivi.==
	   
In questo modello:
- ==Un messaggio inviato da un nodo viene trasmesso contemporaneamente a **tutti** i dispositivi collegati.==
    
- ==Ogni dispositivo riceve il messaggio, ma solo quello a cui è destinato lo elabora, mentre gli altri lo ignorano.==

![[Broadcast.png]]

### Point-to-point 
Una rete **point-to-point** è organizzata tramite una serie di **nodi** e **collegamenti**.

- Un **nodo:** ==è qualsiasi dispositivo; ad esempio un PC, uno switch o un router.==
    
- Lo **switch:** ==collega più dispositivi **all’interno della stessa rete locale (LAN)**.==
    
- Il **router:** ==mette in comunicazione **reti diverse** tra loro.==
    


![[Point-to-Point2.png]]

Il trasferimento dei dati avviene sotto forma di **pacchetti:** ==essi partono da un **nodo sorgente** e arrivano a un **nodo destinazione**.== 
Durante il percorso, i pacchetti possono attraversare diversi nodi intermedi.  

> [!NOTE]
> Solo il nodo destinatario elabora effettivamente il messaggio; gli altri nodi si limitano a inoltrarlo.

#### Esempio di una rete point-to-point
Immaginiamo una rete composta da **5 PC**.

![[Point-to-Point_esempio.png]]


- **PC1** vuole inviare un messaggio a **PC5**.
    
- Esistono più percorsi possibili: ad esempio `(1 → 4 → 5)` oppure `(1 → 2 → 5)`.
    
- La scelta del **percorso migliore** (detta **instradamento** o _routing_) può basarsi su diversi criteri:
    
    - **Length-based (basato sulla lunghezza):** ==si sceglie il percorso più corto.==
        
    - **Traffic-based (basato sul traffico):** ==si sceglie il percorso meno congestionato.==
        

Supponiamo che il percorso migliore sia `(1 → 3 → 5)` ([[Point-to-Point_esempio.png|indicato come “percorso verde”]]).

Quindi: 
- ==PC1 invia il messaggio a **PC3**, che lo inoltra a **PC5**==.
    
 Ma cosa succede se **PC3 è offline**?

- In questo caso viene selezionato un **percorso alternativo** tra quelli disponibili (es: `1 → 4 → 5`).

### Broadcast 

==In una rete di tipo **broadcast**, tutti i computer collegati condividono lo **stesso canale di comunicazione**.==  
Questo significa che, quando un computer invia un messaggio, il segnale si diffonde (cioè viene _trasmesso in broadcast_) a **tutti i dispositivi connessi**.
![[broadcast2.png]]
A seconda di come viene gestita la consegna del messaggio, possiamo distinguere diverse modalità di comunicazione:

1. **Broadcast:** 
	-  ==Il messaggio viene inviato a **tutti** i computer della rete.==
    
	- ==Ogni dispositivo riceve la trasmissione, ma può decidere se elaborarla o ignorarla.==

###### Esempio broadcast 
![[esempio_broadcast.png]]

Il PC1 manda un messaggio che viene ricevuto da tutti i PC collegati allo stesso canale


2. **Multicast:**
	- ==Il messaggio è destinato a un **gruppo specifico** di computer all’interno della rete.==
    
	- Solo i computer che fanno parte di quel gruppo lo elaborano; gli altri lo ignorano.   

###### Esempio Multicast 
![[multicast_ex.png]]

PC1 invia un messaggio → solo **PC2 e PC5** lo ricevono, mentre gli altri no.


3. **Anycast:**
	- ==Il messaggio è inviato a un insieme di computer, ma viene effettivamente ricevuto solo da **uno di essi**: di solito quello **più vicino alla sorgente** (in termini di percorso o distanza di rete).==
###### Esempio Anycast
![[Anycast_ex.png]]

PC1 invia un messaggio a un gruppo composto da **PC2, PC4, PC5** → il messaggio arriva al **PC2** perché è quello più vicino.

4. **Unicast:**
	- ==Il messaggio è inviato a **un solo destinatario specifico**, identificato chiaramente dall’indirizzo.==
    
	- ==Gli altri dispositivi presenti nella rete ignorano il messaggio.==
###### Esempio Unicast
![[Unicast_ex.png]]

PC1 invia un messaggio diretto a **PC4** → solo PC4 lo riceve ed elabora.


> [!example] **In sintesi**
> - **Broadcast** = a tutti.
>   
 >- **Multicast** = a un gruppo.
>    
>- **Anycast** = a uno tra molti (di solito il più vicino).
  >  
>- **Unicast** = a un destinatario preciso.
> 



## Computer Network Topology
==La **topologia di rete** descrive il modo in cui sono organizzati e collegati tra loro i vari elementi di una rete informatica, cioè dispositivi come computer, router, switch e i cavi o collegamenti che li uniscono==.  
Può essere rappresentata in due modi:

- **Fisica** → ==mostra come i dispositivi e i cavi sono fisicamente disposti nello spazio;==
    
- **Logica** → ==mostra come i dati si muovono effettivamente all’interno della rete.==
    

Esistono 5 topologie principali:

1.  **[[#1. Bus Topology|Bus]]**
    
 2. **[[#2. Ring Topology (anello)|Ring (Anello)]]**
    
 3. **[[#3. Star Topology (Stella)|Star (Stella)]]**
    
 4. **[[#4. Mesh Topology (Maglia)|Mesh (Maglia)]]**
    
 5. **[[#5. Tree Topology (Albero)|Tree (Albero)]]**

### 1.  Bus Topology
==In questa topologia tutti i dispositivi condividono **un unico cavo di comunicazione** (chiamato bus principale).==  
==Quando un computer invia un segnale, questo viaggia in entrambe le direzioni lungo il cavo fino a raggiungere il destinatario corretto==.

![[bus topology.png|423x187]]


> [!done] **Vantaggi:**
> 
> - **Economica:** ==richiede meno cavi rispetto ad altre topologie==.
>     
> - **Adatta a piccole reti:** ==ideale quando ci sono pochi dispositivi.==
>     
> - **Semplice da comprendere e implementare.**
>     
> - **Espandibile facilmente:** ==basta collegare altri dispositivi al cavo.==
>     

> [!fail]  **Svantaggi:**
>
> 
> - **Punto critico unico:** ==se il cavo principale si rompe, l’intera rete smette di funzionare.==
>     
> - **Prestazioni ridotte:** ==con più dispositivi o molto traffico, la rete diventa lenta.==
>     
> - **Lunghezza limitata:** l==a distanza massima è vincolata alla lunghezza del cavo.==


### 2. Ring Topology (anello)
==I dispositivi sono collegati **in cerchio**, ognuno connesso a due vicini==.  
==I dati viaggiano in una sola direzione lungo l’anello.==  
Per trasmettere, un computer deve attendere il **token:** 
	==un segnale speciale che dà il permesso di inviare i dati.==

![[Ring Topology.png|331x208]]

> [!done] **Vantaggi**
> 
> - **Prestazioni costanti:** ==anche con molti dispositivi, la rete resta efficiente perché solo chi possiede il token trasmette.==
>     
> - **Basso costo di realizzazione ed espansione.**
>     
> 

> [!fail] **Svantaggi:**
> - **Difficile da gestire:** ==la diagnosi dei guasti è complessa.==
>     
> - **Interruzioni:** ==aggiungere o rimuovere un dispositivo ferma temporaneamente la rete.==
>     
> - **Fragilità:** ==il guasto di un singolo dispositivo può compromettere l’intero anello.==


### 3. Star Topology (Stella)
==Tutti i dispositivi sono collegati a un **nodo centrale** (hub o switch)==.  
I dati passano sempre attraverso il nodo centrale prima di arrivare a destinazione.  
==Il nodo centrale funziona anche da **ripetitore di segnale**==.

![[Star Topolgy.png|361x232]]


> [!done] **Vantaggi:**
> 
> - **Facile da espandere:** ==basta collegare un nuovo dispositivo al nodo centrale.==
>     
> - **Diagnosi semplice:** ==i guasti si individuano rapidamente.==
>     
> - **Resilienza parziale:** ==se un dispositivo periferico si rompe, la rete continua a funzionare.==
>     

> [!fail] **Svantaggi:**
> 
> 
> - **Vulnerabilità del nodo centrale:** ==se l’hub/switch si rompe, l’intera rete si blocca.==
>     
> - **Carico elevato sul nodo centrale:** ==tutto il traffico passa da lì, creando possibili rallentamenti.==
>     
> 



### 4. Mesh Topology (Maglia)

==Ogni dispositivo è collegato con molti altri dispositivi tramite **connessioni ridondanti**.==

- **Full mesh:** t==utti sono collegati direttamente con tutti.==
    
- **Partial mesh:** ==alcuni dispositivi sono collegati direttamente, altri passano attraverso nodi intermedi.==

![[mesh topology.png|409x149]]

> [!done] **Vantaggi:**
> 
> 
> - **Indipendenza:** ==ogni collegamento gestisce il proprio traffico dati.==
>     
> - **Alta tolleranza ai guasti:** ==anche se un collegamento si rompe, la rete continua a funzionare.==
>     
> - **Diagnosi rapida:** ==i problemi si individuano facilmente.==
>     

> [!fail] **Svantaggi:**
> 
> - **Difficile da configurare:** ==l’installazione è complessa.==
>     
> - **Costosa:** ==richiede molti cavi, quindi i costi sono elevati==.
>     
> - **Molto cablaggio necessario:** ==la quantità di fili aumenta con il numero di dispositivi.==


### 5. Tree Topology (Albero)
È una combinazione delle topologie **[[#3. Star Topology (Stella)|stella]]** e **[[#1. Bus Topology|bus]]**.  
==Si parte da un **nodo principale (root)** che funge da tronco, e da esso si diramano altre strutture a stella==.

![[Tree Topology.png|341x183]]

> [!done] **Vantaggi:**
> 
> 
> - **Struttura ibrida:** ==unisce i punti forti di bus e stella.==
>     
> - **Scalabile:** ==aggiungere nuovi nodi è semplice==.
>     
> - **Gestione agevole:** ==facile da monitorare e mantenere.==
>     
> - **Rilevazione errori:** ==i problemi si individuano velocemente.==
>     
> 

> [!fail] **Svantaggi:**
> - **Molto cablaggio richiesto.**
>     
> - **Costosa da realizzare e mantenere.**
>     
> - **Dipendenza dal nodo principale:** ==se il root node si rompe, l’intera rete può fermarsi.==
>     
> - **Manutenzione complessa:** ==più nodi ci sono, più difficile diventa la gestione.==



## Architetture di reti 
Un’**architettura di rete** definisce il modo in cui i dispositivi comunicano e collaborano tra loro, stabilendo ruoli e modalità di condivisione delle risorse. 
**Le 2 principali architetture sono**:
### 1. Modello Client/Server

==È un’architettura centralizzata in cui più dispositivi, chiamati **client**, richiedono servizi o risorse a un **server**, che ha il compito di gestire processi, dati e sicurezza==.

- **Client**: ^81dc1c
    
    - ==Richiede servizi o risorse.==
        
    - ==Invia le richieste al server.==
        
- **Server**: ^b4e999
    
    - ==Fornisce risorse e servizi==.
        
    - ==Gestisce l’elaborazione dei dati e lo storage.== → [[Lezione 2; Applicazioni Web, Caratteristiche di un’applicazione a servizi, Frontend vs. Backend, il ruolo del Browser e del Server Web, differenza tra siti Web Statici e Applicazioni Dinamiche#Interoperabilità del sistema Reti di computer 1. Modello Client/Server Client-Server|Interoperabilità del sistema Client-Server (SOAP e REST)]] 
        
    - ==Restituisce i risultati al client.==
        

![[Client-Server.png|527x263]]

> [!Info] 
> Questo modello si integra tipicamente con **topologie come la stella ([[#3. Star Topology (Stella)|star]])**, dove il server rappresenta il nodo centrale, oppure con la **topologia ad albero ([[#5. Tree Topology (Albero)|tree]])**, in cui più server possono essere collegati in modo gerarchico.  
> È molto diffuso in **LAN aziendali, sistemi web e database centralizzati**, perché offre **efficienza, scalabilità e controllo**.


### 2. Modello Peer-to-Peer(P2P)
È un’architettura decentralizzata in cui ogni dispositivo, o **peer**, ha lo stesso livello di responsabilità: ==può agire sia come client che come server==. 
In questo modello:

- Ogni peer può:
    
    - ==Richiedere risorse o servizi==.
        
    - ==Fornire risorse e servizi==.
        
    - ==Gestire processi e dati localmente==.
        
    - ==Condividere informazioni con gli altri==.
        


![[Peer-to-Peer (P2P).png]]

> [!info]
> ==Il P2P si integra bene con **[[#4. Mesh Topology (Maglia)|topologie mesh]]** (complete o parziali), dove i dispositivi sono interconnessi senza un unico punto centrale, garantendo **ridondanza e resilienza**==.  
> È utilizzato in **applicazioni di file sharing, comunicazioni distribuite e sistemi collaborativi**.


### Reti e classificazione geografica


Oltre all’architettura e alla topologia, le reti possono essere classificate in base alla loro **estensione geografica**:

1. **PAN (Personal Area Network)** :
	-   ==connessioni molto locali (pochi metri, es. Bluetooth)==.
    
2. **LAN (Local Area Network)** :
	-   ==reti locali in ambienti limitati (uffici, case, scuole)==.
    
3. **MAN (Metropolitan Area Network)** :
	-   ==reti cittadine che coprono aree urbane==.
    
4. **WAN (Wide Area Network)** :
	-   ==reti su vasta scala geografica (tra città o nazioni)==.
    
5. **[[Internetwork-Protocols|Internet]]** :
	-   ==la più grande rete globale, che interconnette milioni di dispositivi in architetture e topologie differenti.==
    
![[Tipi di connessione.png|513x309]]

> [!abstract]- **Point-to-Point e Broadcast: due modalità di comunicazione di base**
> Quando parliamo di **reti**, oltre a _come_ sono organizzate (topologia), _che ruoli hanno i nodi_ (architettura), e _quanto sono estese_ (tipologie come LAN/WAN), dobbiamo anche considerare **come viaggiano i dati**:
>
>- **[[#Point-to-point|Point-to-Point:]]**  
> 	 ==comunicazione diretta tra due dispositivi/nodi==.  
  > 	 Es.: un cavo seriale tra due PC, una connessione VPN tra due server, una connessione TCP tra client e server.
>    
>- **[[#Broadcast|Broadcast:]]** 
> 	 ==un dispositivo invia un messaggio che viene ricevuto da **tutti** i nodi della rete (o del dominio di broadcast).==  
> 	   Es.: LAN Ethernet (messaggio ARP), Wi-Fi su canale condiviso.
>
>**Collegamento con le Topologie**
>- **[[#3. Star Topology (Stella)|Topologia a stella]] (Client/Server tipico)** : 
>  ==usa connessioni **point-to-point** tra ogni client e il server centrale==.
 >   
>- **[[#1. Bus Topology|Topologia bus]]** : 
>  ==usa il **broadcast**: ogni pacchetto inviato sul cavo è ricevuto da tutt==i.
 >   
>- **[[#4. Mesh Topology (Maglia)|Topologia mesh]]** : 
>  ==prevalentemente **point-to-point**, perché ogni nodo ha link diretti con altri nodi specifici==.
 >   
>- **[[#2. Ring Topology (anello)|Topologia ad anello]]** : 
>  ==è sequenziale, ma il passaggio del token è simile a una forma controllata di broadcast==.
>  
> **Collegamento con le architetture**
> - **Client/Server:**  
> 	  ==si appoggia soprattutto a **[[#Point-to-point|point-to-point]]** (es. un client stabilisce una connessione TCP verso il server)==.
>    
>- **Peer-to-Peer (P2P):**  può usare entrambi:
 >   
 >   - ==**[[#Point-to-point|Point-to-point]]** per connessioni dirette tra due peer.==
>        
>    - ==**[[#Broadcast|Broadcast]]** per scoprire chi è disponibile nella rete locale (es. protocolli come BitTorrent o discovery via UDP)==.
>
>
>**Collegamento con le Tipologie di rete (PAN, LAN, MAN, WAN)**
>- **PAN** → tipicamente **point-to-point** (Bluetooth pairing) ma anche broadcast (Bluetooth discovery).
>    
>- **LAN** → entrambe:
  >  
 >   - **Broadcast** (es. ARP, DHCP).
 >       
>    - **Point-to-point** (connessioni TCP tra dispositivi).
  >      
>- **MAN/WAN** → principalmente **point-to-point** (collegamenti tra router e provider). Il broadcast qui non è scalabile, quindi viene confinato alle LAN locali.
>    
>- **Internet** → è essenzialmente **point-to-point**: ogni pacchetto viaggia da un router a un altro fino a destinazione. Il broadcast non esiste su scala globale.
>  
>  
>  
>  
>> [!example] **In sintesi**
>> - **Broadcast** è tipico delle **LAN e delle topologie bus/anello**, utile per scoprire dispositivi o inviare messaggi a tutti.
>>    
>>- **Point-to-point** è la modalità dominante in **WAN, Internet e nelle connessioni Client/Server**, perché è più scalabile e sicuro.
 >>   
>>- Le **architetture** (Client/Server o P2P) scelgono l’una o l’altra modalità a seconda del contesto: discovery in broadcast, comunicazione in point-to-point.

> [!example] **In sintesi:**
> - **Comunicazione di reti:** ==definisce come viaggiano i dati.== 
> 
> - **Architettura** : ==definisce i ruoli dei dispositivi (Client/Server o P2P)==.
>     
> - **Topologia** : ==definisce come i dispositivi sono fisicamente o logicamente collegati.==
>     
> - **Tipologia di rete (PAN, LAN, WAN, …)** : ==definisce l’estensione geografica della rete.==