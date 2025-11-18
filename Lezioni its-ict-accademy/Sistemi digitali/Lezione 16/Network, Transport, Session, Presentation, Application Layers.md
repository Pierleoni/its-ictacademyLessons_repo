# Network, Transport, Session, Presentation, Application Layers

Riprendiamo dal modello [[ISO E OSI Model|ISO/OSI]] adesso riprendiamo dall'ultimo livello di questo modello e introduciamo gli altri
## Network layer
[[ISO E OSI Model#^networkLayer|Il livello di rete]] è il terzo livello nel modello ISO/OSI.
![[Network Layer.png]] 
==Definisce come i dati vengono inviati ai dispositivi riceventi attraverso più reti.== 
Nello specifico è responsabile delle funzioni di 
1. **[[#routingProc Routing Process|Routing]]:** 
	- ==Definisce il percorso ottimale per i dati per viaggiare dalla sorgente alla destinazione==.   ^routingProc
   
 2. **Forwarding (instradamento):**
    - ==Muove i pacchetti dall'input del router all'output appropriato==.
    
 3. **[[#Logical Addressing - IP Address|Logical Addressing(indirizzamento):]]** 
    - ==in questo livello viene scelto il percorso per inviare i pacchetti, l'azione di inviarli (forward) è gestita utilizzando l'indirizzo IP, che identifica in modo univoco i dispositivi sulla rete==.
    
 4. **Frammentazione e Riassemblaggio:**  
    - ==Scompone i pacchetti di grandi dimensioni in frammenti più piccoli e li riassembla alla destinazione.==
### Struttura del pacchetto del Header 
Anche in questo livello abbiamo l'header del pachetto.

![[Packet Header Structure.png|600*400|634x418]] 

> [!info]  ==Il [[Internetwork-Protocols#^timetoLive2|Time to live (TTL)]] decide se distruggere il pacchetto o meno, nel caso in cui viene considerato perso==.   ^timeToLive


### [[#^routingProc|Routing Process]]
Il processo di questo livello viene chiamato in processo di routing ed è diviso in 3 step:
1. [[Network, Transport, Session, Presentation, Application Layers#Path determination|Determinazione del percorso]]: 
   determina il percorso dei dati. 
   ==I routers usano delle [[#^tableRouting|tabelle di routing]] e [[#Algoritmi di routing|algoritmi]] al loro interno per decidere il percorso migliore per i data packets.==  ^pathDet

2. [[#Packet Switching|Packet switching]]: 
   ==inoltra i pacchetti dati da un router all'altro basandosi sulle tabelle di routing che si trovano nella **[[#^pathDet|determinazione del percorso]].**== 
	^packetSwitching
   
3. **[[#next-hopForwarding Next Hop Forwarding|Next -Hop Forwarding]]:** 
   ==ogni router inoltra il pacchetto al router successivo finché non raggiunge la destinazione.== ^next-hopForwarding


![[Routing Process.png]]
^img-pathRouting

> [!remember] **Tabelle di Routing** 
> ==Queste tabelle contengono informazioni sui percorsi disponibili per raggiungere diverse reti e sono utilizzate dai router per determinare il miglior percorso per inoltrare i pacchetti di dati.== 
> Le tabelle di routing possono includere informazioni come: 
> - ==indirizzi di rete==.
> - ==metriche di costo== .
> - ==interfacce di uscita.==
> - ==topologia di rete==.
> - ==percorsi disponibili==.
> Vengono aggiornate dinamicamente attraverso protocolli di routing per riflettere i cambiamenti nella topologia della rete.  ^tableRouting
 
### [[#^pathDet|Path determination]] 
==La determinazione del percorso è il processo attraverso cui i router decidono il miglior percorso affinché i pacchetti dati viaggino dalla sorgente alla destinazione.==
Questa decisione avviene grazie alle [[#^tableRouting|tabelle di routing]]. 
Inoltre queste tabelle vengono utilizzate nei 2 tipi di routing:
1. **Static Routing:** 
	==i percorsi vengono configurate manualmente dagli amministratori di rete e le informazioni vengono inserite nelle tabelle di routing, che rimangono fisse a meno che non subiscano modifiche manuali==.
 
> [!remember]
> Le tabelle di routing statiche vengono implementate in reti semplici o in situazioni in cui i percorsi non cambiano frequentemente.

1. **Dynamic Routing:** 
   ==i percorsi vengono appressi automaticamente e aggiornati utilizzando protocolli di routing, in questo caso le tabelle di routing vengono aggiornate dinamicamente in base alle informazioni ricevute, riflettendo i cambiamenti nella topologia della rete.== 

[[#^pathDet|Come accenato prima]], i routers oltre ha usare le tabelle di routing  usano anche algoritmi di routing. 
#### Algoritmi di routing 
Gli algoritmi di routing per sceglier percorso migliore si basano su due algoritmi: 
1. **Shortest Path First (SPF):**
	   ==Calcola il percorso più breve, dalla sorgente alla destinazione, basandosi su metriche di costo cumulative==.  
2. **Distance Vector:**
	   ==Determina il percorso migliore in base a metriche di distanza e aggiornamenti dai router vicini.==  

##### Shortest Path First
Andiamo a vedere nel dettaglio questi due algoritmi:
Abbiamo detto che la metodologia SPF, che sfrutta la funzione cumulativa:
	  ==determina una somma per calcolare il percorso più breve==. 
  Supponiamo di avere la [[Network, Transport, Session, Presentation, Application Layers#^img-pathRouting|topologia di rete dell'immagine sopra]]; ==in questo caso l'algoritmo somma i pesi delle connessioni nella rete e identica il percorso più breve.== 
  Quindi in parole povere, ==il percorso più breve è determinato sommando i vari pesi sulle connessioni, quella che restituisce il valore più basso è il percorso più breve.==
  
> [!done] Casi d'uso
> È particolarmente utilizzata in reti di grande dimensioni, poiché non è necessario conoscere l'intera topologia della rete 

##### Distance Vector
Mentre il Distance Vector si basa ==sul numero di **"hop"(salti)** necessari per raggiungere la sorgente e la destinazione, scegliendo il percorso con il minor numero di hop.== 

> [!done] Casi d'uso
> È più facile da implementare ed è molto usata per reti piccole.
> Ovviamente in questo caso è necessario avere una buona conoscenza della tipologia della rete perché senno il router potrebbe continuare ad aumentare il numero di hop all'infinito, questo è un fenomeno noto come "count to infinity"


### [[#^packetSwitching|Packet Switching]] 
==È il processo di muovere i pacchetti di dati dalla porta di input di un router alla porta di output appropriata, basandosi sulle [[#^tableRouting|tabelle di routing]]==. 
I pacchetti vengono spostati dalla porta di input alla porta di output sfruttando la **Switching Fabric:**
	==è l'architettura interna di un router che connette le porte di input alle porte di output.==

I pacchetti vengono spostati tramite due metodi di commutazione (switching):

1. **[[#storeNforward Store and Forward Switching|Store and Forward]]**: 
	   ==Il router, prima di mandare il pacchetto in output, aspetta di aver ricevuto l'intero pacchetto==. 
	  ==Una volta ricevuto, legge l'indirizzo IP del destinatario e lo invia, utilizzando la [[#^tableRouting|tabella di routing]] per determinare su quale porta farlo uscire==.   ^storeNforward

3. **[[#cut-trough Cut Through Switching|Cut -Through]]**: 
   ==Il router non aspetta di aver ricevuto l'intero pacchetto, ma appena riceve l'informazione che riporta l'indirizzo IP, lo legge e invia il pacchetto in output verso la destinazione==. ^cut-trough


La scelta del metodo di commutazione (Store-and-Forward o Cut-Through) dipende dalla modalità della rete e dalla gestione del buffering. 
Nel caso dello **Store-and-Forward:**
i ==router utilizzano un buffer per memorizzare temporaneamente i pacchetti in arrivo se la porta di output è occupata, prevenendo così la perdita di pacchetti.== 
==Questo metodo richiede che l'intero pacchetto venga ricevuto prima di essere inoltrato==. 
D'altra parte, nel **Cut-Through:** 
il pacchetto viene inoltrato non appena l'indirizzo di destinazione è stato letto, riducendo la latenza, ma non consente il buffering nel caso in cui la porta di output sia occupata.
Per **buffering** si intende: 
==la memorizzazione temporanea dei pacchetti in memoria se la porta di output è occupata, prevenendo la perdita di pacchetti.== 
**Forwarding decision(Decisione di inoltro ):** 
==Basandosi sull'indirizzo IP di destinazione e sulla tabella di routing, il router decide il prossimo salto per il pacchetto.== 
In altre parole, il router determina a quale router inviare il pacchetto.

#### [[#^storeNforward|Store and Forward Switching]] 
è il metodo più affidabile, ==il router ricevere l'intero pacchetto e controlla se i dati sono integri, tutto ciò avviene prima dell'invio.== 
**Processo:**
1. ==Il router riceve l'intero pacchetto di dati.==
2. ==Il pacchetto viene memorizzato temporaneamente in memoria==.
3. ==Viene eseguito un controllo degli errori (come il CRC) per garantire l'integrità dei dati==.
4. ==Se il pacchetto è valido, viene mandato in uscita; viceversa, se il pacchetto non è valido, viene distrutto==.


> [!done] Vantaggi
> - **Affidabilità:** ==garantisce una trasmissione priva di errori controllando l'intero pacchetto prima dell'inoltro==.
>- ==Permette di impostare le proprietà dei pacchetti==.
>- ==È adatto per reti in cui l'integrità dei dati è cruciale==.

> [!fail] Svantaggi
> - Maggiore latenza: ==dovuta al tempo necessario per ricevere e processare l'intero pacchetto.==
>- ==Richiede più memoria per memorizzare i pacchetti==.

#### [[#^cut-trough|Cut Through Switching]] 
==Il pacchetto viene inviato non appena l'indirizzo di destinazione viene letto==. Quando il pacchetto arriva sulla porta di input del router:, 
1) quest'ultimo legge l'indirizzo IP, 
2) che viene poi tradotto in un indirizzo MAC. 
==Questo passaggio è necessario affinché il pacchetto venga inviato al router corretto del destinatario==.
**Processo:**

3. ==Il router inizia a inoltrare il pacchetto non appena legge l'indirizzo MAC di destinazione dall'intestazione del pacchetto==.
4. ==Il resto del pacchetto continua a essere inoltrato mentre viene ricevuto.==

> [!done] **Vantaggi:**
> - **Maggiore velocità:** ==il forwarding inizia quasi immediatamente dopo la lettura dell'indirizzo di destinazione, riducendo la latenza==.
> - ==Trasferimento dati più veloce, adatto per reti ad alte prestazioni==.

> [!fail] **Svantaggi:**
> - ==Non viene effettuato alcun controllo degli errori nel pacchetto, il che significa che i pacchetti corrotti potrebbero essere inoltrati==.
> - ==Questo può portare a problemi potenziali se il pacchetto è danneggiato durante la trasmissione==.

### [[#^next-hopForwarding|Next Hop Forwarding]]  
 ==È il salto del pacchetto da un router all'altro o quando raggiunge la destinazione finale. 
 L'indirizzo IP determina a quale router deve essere inviato il pacchetto.== 
**Processo**:
- **Hop-by-Hop Routing**: 
  ==Ogni router lungo il percorso prende una decisione di inoltro indipendente, basata sulla propria tabella di routing==.

- **Next-Hop Address**: 
  ==L'indirizzo IP del prossimo router a cui il pacchetto deve essere inviato.==

- **Address Resolution Protocol (ARP)**: 
  ==È un protocollo che traduce gli indirizzi IP in indirizzi MAC per identificare il prossimo router a [[ISO E OSI Model#livelloFisico Livello fisico|livello fisico]] e per il forwarding dei pacchetti a livello di collegamento dati ([[ISO E OSI Model#dataLink-layer Livello data link|Data Link Layer]])==.

**Livelli di Operazione**:
- Il router opera a livello di rete (Network Layer), mentre lo switch opera a livello di collegamento dati (Data Link Layer). Quando il pacchetto arriva al router, quest'ultimo lavora a livello di rete.
Questo è un esempio di tabella di routing su ogni router e viene cotruita con gli algoritmi di routing: 
![[Routing Process2.png]]

> [!info] **Default Router** 
> ==È la regola che viene seguita quando non ci sono altre corrispondenze nella tabella di routing==. 
> 
> ==Quando arriva un pacchetto di dati che non segue una regola specifica, viene inviato sulla **default route** nella speranza che, seguendo questo percorso, arrivi a un router che ha una regola per quel pacchetto di dati.==

## Logical Addressing - IP Address
Un **indirizzo IP** ==è un numero che identifica in maniera univoca un’interfaccia di rete su una rete basata sul protocollo Internet (IP)==.

- ==Ha una **parte di rete** (network) che identifica la rete di appartenenza==.  
     ^83bcda
     
- ==Ha una **parte host** che identifica il singolo dispositivo all’interno di quella rete==.   
  
     ^bd5cc1
- Può essere di due tipi:
	1. **IPv4** (32 bit, notazione decimale puntata) 
	2. **IPv6** (128 bit, notazione esadecimale).

- **Versione 4 (IPv4)**: 
	- ==Indirizzi a 32 bit== 
	- Esempio: `192.168.1.1`. 
- Questa versione è stata introdotta per prima, ma sta esaurendo gli spazi di indirizzi disponibili, motivo per cui è stata sviluppata la versione 6.

- **Versione 6 (IPv6)**: 
	 -  ==Indirizzi a 128 bit.==
	 - **Esempio:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`. 
- Questa versione offre un numero significativamente maggiore di indirizzi disponibili.


> [!info] Entrambe le versioni operano a livello di rete ([[#Network layer|Network Layer nel modello ISO/OSI]] e [[Modello TCP-IP#Internet Layer|Internet Layer nel modello TCP/IP]]).
> 

### La Versione 4 dell'IP

==Gli indirizzi IPv4 sono composti da quattro numeri, ciascuno formato da tre cifre, che vanno da `0` a `255`.== 
Esistono diversi classi di indirizzi che determinano lo scopo della rete e il suo dimensionamento.

##### **Classi di indirizzi IP (per definire dimensione e scopo della rete)**

- **[[#Classe A|Classe A]]**: da `0.0.0.0` a `127.255.255.255`
    
- **[[#Classe B|Classe B]]**: da **128.0.0.0** a **191.255.255.255**
     
- **[[#Classe C|Classe C]]**: da **192.0.0.0** a **223.255.255.255**
    
- **[[#Classe D|Classe D]]**: da **224.0.0.0** a **239.255.255.255** (_Multicast_)
    
- **[[#Classe E|Classe E]]**: da **240.0.0.0** a **255.255.255.255** (_Riservata_)
## La Maschera di Rete (Subnet Mask Structure)

La **subnet mask** ==è un numero di 32 bit che serve a suddividere un indirizzo IP in due parti==:

1. **Parte di rete** → ==identifica la rete di appartenenza==.
    
2. **Parte di host** → ==identifica i dispositivi all’interno di quella rete.==

### Funzione

==Determina quale sezione dell’indirizzo IP rappresenta la rete e quale rappresenta l’host.==
### Formato:
- ==Notazione decimale puntata== (ad esempio, `255.255.255.0`).
### Rappresentazione Binaria:
La subnet mask si applica all'indirizzo IP:
- ==i bit a `1` corrispondono alla parte di rete,==
    
- ==i bit a `0` corrispondono alla parte di host.==
Ad esempio:
 `255.255.255.0` in binario è rappresentato come `11111111.11111111.11111111.00000000`.

> [!ticket] ==In binario, la maschera è composta da 4 ottetti (32 bit).==  
>==I bit `1` identificano la rete, mentre i bit `0` identificano l’host.==.
> 

### Combinazione di Indirizzo IP e Subnet Mask

#### Indirizzo di Rete:

==È la parte dell'indirizzo IP identificata dagli `1` della subnet mask==.

> [!info] **Info**
> ==si ottiene applicando un’operazione **AND logica** tra indirizzo IP e subnet mask.==
>>[!example]- **Esempio**
>>1. **[[Le architetture di un Computer#Conversione decimale in Binario|Converti in binario:]]**
>> 	  - IP: `192.168.1.10` → `11000000.10101000.00000001.00001010`
>> 	  - SM: `255.255.255.0` → `11111111.11111111.11111111.00000000`
>>2. Esegui l'[[Le architetture di un Computer#Operatore **AND** (E logico)|AND]] logico: 
>>```
>> 11000000.10101000.00000001.00001010 (IP)
>>AND
>>11111111.11111111.11111111.00000000 (Subnet Mask)
>>------------------------------------
>>11000000.10101000.00000001.00000000
>>```
>>
>>3. **[[Le architetture di un Computer#Conversione Binario in decimale|Converti il risultato in decimale]]:**
>>- `11000000` → 192
>>  
>>- `10101000` → 168
>>  
>>- `00000001` → 1
>>  
>>- `00000000` → 0
>>  
>>- **Network Address:** `192.168.1.0`
>>
>>1. **Trova l'Host:**
>>   L'host è la parte "libera" rimasta dopo l'AND. In questo caso, è l'ultimo ottetto: `.10`.


#### Indirizzo Host:

==è la parte rimanente dell’indirizzo IP, corrispondente ai bit a `0` della subnet mask, che identifica i singoli dispositivi==.

> [!example] Esempio
> - **Indirizzo IP**: `192.168.1.10`
> - **Subnet Mask**: `255.255.255.0`
> - **Indirizzo di Rete**: `192.168.1.0`
> - **Indirizzo Host**: `10`

In questo esempio, i primi tre ottetti (`192.168.1`) rappresentano la rete, mentre l’ultimo ottetto (`10`) rappresenta l’host.


### Classi di IPv4

#### Classe A

- **Range**: `0.0.0.0` a `127.255.255.255`.
- **Primo Ottetto**: da `0` a `127`
- **Subnet Mask Predefinita**: `255.0.0.0`
- **Numero di Reti**: 128 ($2^7$)
- **Host per Rete**: Oltre 16 milioni (2^24 - 2)
- **Utilizzo**: ==Progettata per reti molto grandi con molti dispositivi, come grandi aziende o provider di servizi Internet (ISP)== (es. Vodafone, Tim, ecc.).
- **Esempio**: `10.0.0.1`

#### Classe B

- **Range**: `128.0.0.0` a `191.255.255.255`
- **Primo Ottetto**: da 128 a 191
- **Subnet Mask Predefinita**: `255.255.0.0`
- **Numero di Reti**: 16.384 ($2^{14}$)
- **Host per Rete**: Oltre 65.000 ($2^{16} - 2$)
- **Utilizzo**: ==Adatta per reti di medie dimensioni, come università o grandi aziende==.
- **Esempio**: `172.16.0.1`

#### Classe C

- **Range**: `192.0.0.0` a `223.255.255.255`.
- **Primo Ottetto**: da 192 a 223
- **Subnet Mask Predefinita**: `255.255.255.0`
- **Numero di Reti**: Oltre 2 milioni (2^21)
- **Host per Rete**: 254 (2^8 - 2)
- **Utilizzo**: ==Ideale per reti piccole, come piccole aziende o reti domestiche==.
- **Esempio**: `192.168.1.1`

#### Classe D

- **Range**: `224.0.0.0` a `239.255.255.255`
- **Primo Ottetto**: da 224 a 239
- **Subnet Mask Predefinita**: `255.255.255.255`
- **Utilizzo**: ==Riservata per gruppi multicast, consente l'invio di un singolo pacchetto a più destinazioni==.
- **Esempio**: `224.0.0.1`

#### Classe E

- **Range**: `240.0.0.0` a `255.255.255.255`.
- **Primo Ottetto**: da 240 a 255
- **Utilizzo**: ==Riservata per scopi sperimentali e uso futuro. Non utilizzata per il networking generale==.

### Indirizzi IP Privati e Pubblici

**Indirizzo IP Pubblico**:
- ==Utilizzato per navigare su Internet ed è fornito dall'Internet Service Provider (ISP).==
- ==È l'indirizzo a cui il server è collegato e che è routabile su Internet==.

> [!example] **Esempi**:
> 
> - Indirizzo di un sito web: 93.184.216.34
> - Server aziendale: 203.0.113.10

**Indirizzo IP Privato**:
- ==Associato ai dispositivi all'interno di una rete locale (LAN) e non è routabile su Internet.==
- Ogni dispositivo ha due indirizzi IP: 
	1. ==uno privato, associato al dispositivo stesso==.
	2. ==uno pubblico, fornito dall'ISP==.

> [!example] **Esempi**
> 
> - Rete domestica: `192.168.1.1`
> - Rete aziendale: `10.0.0.1`
> 

Entrambi gli indirizzi IP (privato e pubblico) sono generalmente dinamici: 
1. ==l'indirizzo privato è assegnato dal router all'interno della LAN==, 
2. ==mentre l'indirizzo pubblico è fornito dall'ISP==.

> [!NOTE] **Nota**
> ==Ogni dispositivo nella LAN ha un indirizzo privato==. 
> ==L’accesso a Internet avviene tramite il router, che possiede sia un indirizzo privato (verso la LAN) sia un indirizzo pubblico (verso l’ISP)==. Questo meccanismo consente ai dispositivi della rete locale di comunicare su Internet attraverso un unico indirizzo pubblico.

#### **Tecnologia NAT (Network Address Translation)**:

- **Scopo:**
	-   ==Permette la connessione tra indirizzi IP privati e pubblici==.
- **Funzione:**
	- ==Traduce gli indirizzi privati in indirizzi pubblici e viceversa==.
	- ==Consente a più indirizzi IP privati di condividere un unico indirizzo IP pubblico per l'accesso a Internet==.

> [!example] **Esempio**
>  Un router domestico utilizza il NAT per consentire a tutti i dispositivi in una rete domestica (con indirizzi IP privati) di accedere a Internet utilizzando l'indirizzo IP pubblico del router.

## [[ISO E OSI Model#^transportLayer|Transport Layer]] 
Il **Transport Layer** si occupa della comunicazione **end-to-end**: 
ovvero dalla sorgente alla destinazione. 
Ad esempio, in un'app come WhatsApp, ==il messaggio parte dalla sorgente e viene decifrato solo alla destinazione, senza essere accessibile o modificabile durante il percorso da altri dispositivi.==

### Analogia:

![[Analogia.png]]

Immaginiamo di avere una costa est e una costa ovest, dove vivono dei cugini. I cugini della costa ovest vogliono comunicare con i cugini della costa est. I cugini della costa ovest consegnano la lettera allo zio Bill (che rappresenta il Transport Layer). A zio Bill non interessa cosa succede nel mezzo; il suo compito è semplicemente quello di garantire che la lettera venga consegnata. 
Lo zio Bill consegna la lettera al postino a cui non interessa di sapere quale sia il contenuto della lettera ma ha il solo compito di consegnarla allo zio Sam della costa est.
Una volta che la lettera arriva, sarà presa dallo zio Sam e consegnata ai cugini della costa est che leggeranno il contenuto della lettera.

### Funzioni del Transport Layer

- **End-to-End Communication**: ==Gestisce il trasferimento dei dati tra i dispositivi, garantendo che le informazioni vengano inviate e ricevute correttamente==.
    
- **Segmentation and Reassembly**: ==Suddivide i grandi flussi di dati in segmenti più piccoli e li ricompone alla destinazione, facilitando una trasmissione più efficiente.==
    
- **Error Detection and Correction**: 
	  ==Assicura l'integrità e l'affidabilità dei dati.==
	   La correzione degli errori non è sempre prevista, ma è fondamentale nelle connessioni [[Modello TCP-IP|TCP/IP]]. 
	   Nei meccanismi di [[ISO E OSI Model#dataLink-layer Livello data link|livello Data Link]], la correzione degli errori avviene su ogni nodo, mentre nei meccanismi end-to-end, la correzione avviene solo alla destinazione.
    
- **Flow Control**: 
	  ==Gestisce la velocità di trasmissione dei dati tra i dispositivi==. Possiamo definire se la connessione è **[[Internetwork-Protocols#Connection Oriented services|connection-oriented]]** (orientata alla connessione) o **[[Internetwork-Protocols#Servizi non orientati alla connessione(connectionless)|connectionless]]** (senza connessione).
    
- **Connection Management**: 
	  ==Stabilisce, mantiene e termina le connessioni, garantendo che i dispositivi possano comunicare in modo efficace==.

Una volta ricevuti dei dati e una volta ricostruiti bisogna capire a quale applicazioni assegnarli.
Per fare cio si utilizzano le socket. 

### Sockets 
Le **sockets** sono fondamentali per abilitare la comunicazione tra dispositivi su una rete. 
==Agiscono come interfacce attraverso le quali i processi (applicazioni) comunicano all'interno di una rete informatica==.

==Una socket viene ancorata all'indirizzo IP, seguito da due punti e dal numero di porta==. 
==Questo significa che l'indirizzo IP identifica la rete e l'host, mentre il numero di porta identifica l'applicazione specifica a cui si desidera accedere==.

> [!example] Esempio
> `192.168.1.1:80, dove 192.168.1.1` 
> è l'indirizzo IP e `80` è il numero di porta associato all'applicazione (ad esempio, un server web).

==Le porte sono statiche e sono associate a specifiche applicazioni, consentendo così una comunicazione chiara e organizzata tra i vari processi.==
![[Sockets.png]]
### Header del segmento 
Ogni livello aggiunge un header, oltre ai dati gli altri paramenti sono la porta sorgente e la porta di destinazione. Ogni volta che ci avviciniamo al livello applicativo l'header inizia a contenere meno informazioni. 
![[Header del segmento.png|center]]

Come possiamo vedere da questa immagine: 
Le dimensioni totali del header occupano 32 bit, le componenti principali sono:
1. **Source Port # (Porta d'origine):**
	- ==Presente nei primi 16 bit (2 byte)==.
	- ==Specifica il numero di porta del mittente, permettendo ai dispositivi di identificare quale applicazione sta inviando il segmento==.
2. **Destination Port # (Porta di Destinazione)**:
    - ==Anch'essa presente nei successivi 16 bit (2 byte)==.
    - ==Indica il numero di porta del destinatario, determinando quale applicazione deve ricevere il segmento==.
3. **Other Header Fields (Altri Campi dell'Header)**:
	- ==Includono informazioni aggiuntive necessarie per il corretto instradamento e gestione del segmento==.
	- ==Questi campi possono includere numeri di sequenza, numeri di [[Internetwork-Protocols#Il servizio ACK (Acknowledgment)|ack]], flags di controllo, e informazioni sulla dimensione dell'header stesso==.
	- Dipendono dai protocolli  [[Modello TCP-IP#TCP (Transmission Control Protocol)|TCP]] o [[Modello TCP-IP#UDP (User Datagram Protocol)|UDP]] 
## [[ISO E OSI Model#^sessionLayer|Session Layer]] 
==Gestisce e controlla le connessioni e la comunicazione tra applicazioni, quindi controlla la connessione logica tra le applicazioni: due applicazioni devono comunicare e avvia la sessione di comunicazioni==. 
**Nel session iniziamo a parlare di connessioni tra applicazioni.** 
Qui avvia la sessione tra applicazioni e definisce se questo dialogo deve essere:

1. **Half Duplex Mode**: 
   ==la comunicazione deve andare in entrambe le direzione ma non è simultanea==.

> [!example] Esempio
> ==Un stampante di rete e un computer comunicano in modalità half-duplex, dove il computer invia un lavoro di stampa e la stampante restituisce una conferma, ma non inviano dati contemporaneament==e.

![[Half-duplex.png]]
2. **Full-Duplex Mode**: 
   ==la comunicazione avviene in entrambe le direzione ed è simultanea==. 

> [!example] Esempio
> ==Un'applicazione di videoconferenza in cui entrambi i partecipanti possono parlare e ascoltare contemporaneamente, garantendo una comunicazione bidirezionale fluida==.

![[Full-duplex Mode.png]]
## [[ISO E OSI Model#^presentationLayer|Presentation Layer ]] 
==I dati che arrivano dalla applicazione vengono convertiti in formati che sono leggibili per il dispositivi che riceve, questo livello rende compatibile la presentazione tra due dispositivi diversi==. 
Quindi 
- **Traduce:**
  ==Converte i formati dei dati da formati specifici dell'applicazione a formati di rete e viceversa==.
- **Encripta/decripta**: 
  ==Garantisce la sicurezza dei dati crittografandoli prima della trasmissione e de-crittografandoli al momento della ricezione==.
- **Comprime:**
  ==Riduce la dimensione dei dati da trasmettere per ottimizzare l'uso delle risorse di rete==.


## [[ISO E OSI Model#^applicationLayer|Application Layer]] 
==Qui abbiamo l'interfaccia utente che permettono di comunicare e interagire attraverso la rete, e qui che vengono eseguiti i programmi==.

- **Funzioni:** 
Servizi di Rete: ==Abilita le applicazioni utente a interagire con la rete (ad esempio, trasferimenti di file, email, accesso remoto)==.

-  **Condivisione delle Risorse:** 
==Facilita l'accesso alle risorse di rete==.

- Interfaccia Utente: 
==Fornisce un'interfaccia per l'utente per interagire con la rete<==.












