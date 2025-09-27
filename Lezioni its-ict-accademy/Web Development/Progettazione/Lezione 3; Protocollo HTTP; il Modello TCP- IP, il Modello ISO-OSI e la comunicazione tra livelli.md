# Introduzione
Nella [[Lezione 2; Applicazioni Web, Caratteristiche di un’applicazione a servizi, Frontend vs. Backend, il ruolo del Browser e del Server Web, differenza tra siti Web Statici e Applicazioni Dinamiche|scorsa lezione]] abbiamo affrontato le caratteristiche di una applicazione web e i diversi ruoli tra il backend e il frontend.
In questa lezione affronteremo il protocollo HTTP.

# Il concetto di protocollo e TCP/IP
Un **protocollo** è un insieme di regole che stabilisce **come due sistemi devono dialogare** tra loro.  
Senza un protocollo condiviso, la comunicazione non sarebbe possibile, perché i due sistemi “parlerebbero lingue diverse”.
## Protocollo TCP/IP
Sul web, la comunicazione avviene tramite la **famiglia di protocolli [[Modello TCP-IP|TCP/IP]]**, che si basa su un principio fondamentale:

> [!ticket] **Il client invoca il server (mai il contrario).**  
> È sempre il client che invia una richiesta, a cui il server risponde.

TCP/IP non è un singolo protocollo, ma un insieme organizzato in **4 livelli**, ognuno con responsabilità precise e con i propri sotto-protocolli. La comunicazione funziona solo se **sia il mittente che il destinatario usano gli stessi protocolli corrispondenti a ciascun livello** (come due persone che parlano la stessa lingua).

### I [[Modello TCP-IP#Struttura del modello TCP/IP|4 livelli]] del modello TCP/IP  
![[I 4 livelli del protocollo TCP-IP.png]]

Come abbiamo gia visto nella lezione [[Modello TCP-IP]] in Sistemi digitali il modello TCP/IP presenta 4 livelli, partendo dal basso verso l'alto:

1. **[[Modello TCP-IP#^applicationLayer|Livello Fisico]]**
    
    - Si occupa della trasmissione fisica dei dati (cavi, Wi-Fi, segnali). 
        
    - Utilizza protocolli **nativi** delle tecnologie di rete (es. Ethernet, Wi-Fi).
        
2. **[[Modello TCP-IP#^InternetLayer|Livello Rete]]**
    
    - Identifica gli indirizzi dei dispositivi nella rete.
        
    - Protocollo principale: **IP (Internet Protocol)**.
        
    - Esempio: sapere a quale indirizzo inviare il “pacchetto”.
        
3. **[[Modello TCP-IP#^0f712f|Livello Trasporto]]** 
    
    - Garantisce il trasferimento corretto dei dati da un’applicazione all’altra.
        
    - Protocolli principali:
        
        - **TCP (Transmission Control Protocol):** affidabile, garantisce che i pacchetti arrivino nell’ordine corretto.
            
        - **UDP (User Datagram Protocol):** più veloce, ma non garantisce l’ordine (usato per streaming, chiamate audio/video).
            
4. **[[Modello TCP-IP#^applicationLayer|Livello Applicazione]]**
    
    - È quello più vicino all’utente finale.
        
    - Qui troviamo i protocolli che servono per **esigenze specifiche di applicazioni**:
        
        - **HTTP** → per trasferire pagine e contenuti web.
            
        - **FTP** → per trasferire file di grandi dimensioni.
            
        - **SMTP** → per inviare e ricevere e-mail.
            
        - …e molti altri.


Ora approfondiamo meglio ognuno di questi livelli partendo dal livello più alto (livello di applicazione) arrivando al più basso (livello fisico)
### Livello di applicazione (Application Layer)

Il **[[Modello TCP-IP#Application layer|livello di applicazione]]** è: 
- quello più vicino all’utente finale ed è responsabile di fornire i **servizi di rete direttamente alle applicazioni software**, come ad esempio browser web, client di posta elettronica o programmi per il trasferimento di file.

In altre parole, è il livello che: 
- mette in comunicazione le applicazioni con la rete, occupandosi non solo della trasmissione dei dati, ma anche di come questi vengono rappresentati e interpretati.

#### Funzioni principali

- **Interfaccia con l’utente**  
    Fornisce i protocolli che permettono alle applicazioni di scambiarsi dati in rete. È grazie a questo livello che un browser può richiedere una pagina web o un client di posta inviare un’e-mail.
    
- **Gestione della sessione e della presentazione**  
    A differenza del modello OSI, nel TCP/IP queste funzioni sono incluse nello stesso livello:
    
    - _Gestione della sessione:_ apertura, mantenimento e chiusura della connessione tra due host.
        
    - _Presentazione dei dati:_ formattazione, traduzione e, se necessario, crittografia o compressione dei dati trasmessi.



> [!link] **Protocolli comuni del livello di applicazione**
> - **HTTP (HyperText Transfer Protocol):** protocollo fondamentale per la navigazione web.
  >  
>- **HTTPS (HTTP Secure):** versione sicura di HTTP, che utilizza la crittografia SSL/TLS.
  >  
>- **FTP (File Transfer Protocol):** usato per il trasferimento di file.
   > 
>- **SMTP (Simple Mail Transfer Protocol):** per l’invio di posta elettronica.
  >  
>- **POP3 (Post Office Protocol 3) e IMAP (Internet Message Access Protocol):** per la ricezione della posta elettronica.
  >  
>- **DNS (Domain Name System):** sistema che traduce i nomi di dominio (es. `www.google.com`) nei corrispondenti indirizzi IP numerici.


> [!example] **In sintesi:**
> Il livello di applicazione è ciò che rende **utilizzabile Internet dall’utente finale**. Senza di esso, non avremmo protocolli standardizzati per navigare, scambiare file o comunicare via e-mail. È quindi il punto in cui le esigenze pratiche delle persone (consultare un sito, inviare una mail, scaricare un documento) vengono tradotte in regole comprensibili e utilizzabili dai computer.

### Livello di trasporto (Transport Layer)
Il **[[Modello TCP-IP#TransportLayer Transport Layer|livello di trasporto]]** ha il compito di:
- gestire la comunicazione **tra due processi** (cioè applicazioni) che si trovano su host diversi.  
In altre parole: 
- fornisce un **canale logico di comunicazione** che permette ai dati di fluire in modo ordinato, affidabile e coerente tra mittente e destinatario.

Se il livello di rete si occupa di consegnare i pacchetti “da computer a computer”, il livello di trasporto si assicura che questi pacchetti arrivino **dal programma corretto del mittente al programma corretto del destinatario**, garantendo quindi un dialogo completo tra applicazioni.


#### Funzioni principali 

- **Segmentazione dei dati**  
    I dati provenienti dal livello di applicazione vengono suddivisi in segmenti più piccoli e gestibili, per poter essere trasmessi in rete in modo efficiente.
    
- **Controllo di flusso**  
    Regola la velocità di invio dei dati, così da non sovraccaricare il destinatario in caso di capacità di elaborazione inferiore.
    
- **Controllo di errore e affidabilità**  
    Si occupa di verificare che i segmenti arrivino a destinazione **senza errori**, **in ordine** e **senza duplicati**.


> [!link] **Protocolli Principali**
> - **[[Modello TCP-IP#TCP (Transmission Control Protocol)|TCP (Transmission Control Protocol)]]**
 >   
 >   - Protocollo **orientato alla connessione** e **affidabile**.
 >       
 >   - Prima di inviare i dati, stabilisce una connessione tramite il processo di **“three-way handshake”**.
  >      
  >  - Garantisce che ogni pacchetto venga ricevuto correttamente, richiedendo la ritrasmissione in caso di perdita.
 >       
 >   - Utilizzato dalla maggior parte delle applicazioni comuni, come la **navigazione web** (HTTP/HTTPS) e la **posta elettronica**.
 >       
>- **[[Modello TCP-IP#UDP (User Datagram Protocol)|UDP (User Datagram Protocol)]]**
 >   
 >   - Protocollo **senza connessione (connectionless)** e **non affidabile**.
 >       
 >   - Invia i dati (detti datagrammi) senza verificare che arrivino a destinazione.
 >       
  >  - È molto più veloce del TCP, ma non garantisce la consegna né l’ordine.
  >      
  >  - Usato in applicazioni dove conta la **velocità** e qualche perdita di pacchetto è accettabile, come **streaming video**, **giochi online** e **chiamate VoIP**.



> [!example] **In sintesi:**
> Il livello di trasporto rappresenta un **ponte affidabile (TCP)** o veloce ma “leggero” (UDP) tra le applicazioni distribuite su computer diversi. 
> Senza questo livello, i dati arriverebbero sì al computer giusto, ma non necessariamente al programma corretto, né nell’ordine giusto


### Livello di Rete o Internet (Network/Internet Layer)
Il **[[Modello TCP-IP#Internet Layer|livello di rete]]** è considerato il **cuore del modello TCP/IP:** 
- si occupa di garantire che i dati possano essere instradati correttamente da un host di origine a un host di destinazione, anche attraverso più reti interconnesse.

La sua responsabilità principale è dunque l’**indirizzamento logico** dei dispositivi e la scelta del **percorso migliore (routing)** che i pacchetti devono seguire per arrivare a destinazione.

#### Funzioni principali

- **Indirizzamento logico**  
    Ogni dispositivo connesso a una rete riceve un **indirizzo IP univoco**, necessario per identificarlo e permettere la comunicazione con altri host.
    
- **Instradamento (Routing)**  
    Determina il percorso più efficiente che i pacchetti devono seguire per raggiungere la destinazione, anche passando attraverso router e reti intermedie.
    
- **Frammentazione e ri-assemblaggio dei pacchetti**  
    Se un pacchetto è troppo grande per essere gestito da una rete intermedia, viene suddiviso in **frammenti** più piccoli. Alla destinazione, i frammenti vengono ri-assemblati per ricostruire i dati originali.


> [!link] **Protocolli Principali:**
> - **[[Modello TCP-IP#1. IP(Internet Protocol - IPv4 e IPv6)|IP (Internet Protocol)]]**  
> 	-   È il protocollo centrale di questo livello. Incapsula i segmenti provenienti dal livello di trasporto in pacchetti (chiamati **datagrammi**) e aggiunge le informazioni di indirizzo (IP di origine e IP di destinazione).  
 >   Esistono due versioni principali:
>    
> 	 - **IPv4:** basato su indirizzi a 32 bit (es. `192.168.1.1`).
>        
> 	 - **IPv6:** basato su indirizzi a 128 bit, pensato per superare l’esaurimento degli indirizzi IPv4.
  >      
>- **[[Modello TCP-IP#2. ICMP (Internet Control Message Protocol)|ICMP (Internet Control Message Protocol)]]**  
> 	 -  Utilizzato per inviare messaggi di controllo ed errore. Ad esempio, viene impiegato dal comando **ping** per verificare la raggiungibilità di un host.
  >  
>- **[[Modello TCP-IP#3. Address Resolution Protocol ARP|ARP (Address Resolution Protocol)]]**  
> 	-  Serve a tradurre un indirizzo IP in un **[[Modello TCP-IP#ARP Cache|indirizzo fisico (MAC address]])** all’interno di una rete locale, così che i pacchetti possano essere effettivamente consegnati all’interfaccia corretta.



> [!example] **In Sintesi:**
> Il livello di rete permette ai dati di viaggiare non solo **da computer a computer**, ma anche **attraverso reti complesse**, garantendo che ogni pacchetto arrivi all’host giusto. È il livello che rende Internet una rete globale, collegando dispositivi molto diversi tra loro con un linguaggio comune: l’**indirizzo IP**.


### Il Livello di Accesso alla Rete (Network Access Layer) 

Il **[[Modello TCP-IP#Network Access Layer|livello di accesso alla rete]]** è il più basso del modello TCP/IP.  
- Si occupa di **tutti gli aspetti fisici e di collegamento** necessari per trasmettere i dati da un dispositivo a un altro all’interno della stessa rete locale.

> [!caution] **Importante**
> Nel **modello TCP/IP** questo livello **raggruppa due livelli del modello OSI**:
>
>- **[[ISO E OSI Model#livelloFisico Livello fisico|Livello Fisico]]** → trasmissione dei bit sul mezzo fisico (cavo, onde radio, fibra ottica…).
 >   
>- **[[ISO E OSI Model#dataLink-layer Livello data link|Livello Data Link (Collegamento Dati)]]** → gestione degli indirizzi MAC e dell’organizzazione in frame.


#### Funzioni principali

- **Interfacciamento con l’hardware**  
    Gestisce la comunicazione diretta con la **scheda di rete (NIC)** e con il mezzo fisico utilizzato (Ethernet via cavo, Wi-Fi, fibra, ecc.).
    
- **Indirizzamento fisico (MAC Address)**  
    Ogni scheda di rete possiede un **indirizzo univoco** chiamato MAC, che permette di identificare i dispositivi all’interno di una stessa rete locale.
    
- **Framing**  
    I dati ricevuti dai livelli superiori vengono impacchettati in **frame** (unità logiche di trasmissione) che includono indirizzo sorgente, indirizzo destinatario e informazioni di controllo.
    
- **Trasmissione fisica**  
    I frame vengono trasformati in **segnali elettrici, luminosi o radio** a seconda del mezzo di trasmissione e inviati sul canale di comunicazione.


> [!link] **Protocolli e standard comuni**
> - **Ethernet** → Lo standard più diffuso per le **LAN cablate**.
 >   
>- **Wi-Fi (IEEE 802.11)** → Standard per le **reti senza fili (WLAN)**.
 >   
>- **PPP (Point-to-Point Protocol)** → Usato per collegamenti diretti tra due nodi (oggi meno comune, ma importante storicamente).


> [!Example] **In sintesi:**
> Il **livello di accesso alla rete** è quello che traduce i dati in **segnali fisici reali** che viaggiano lungo i cavi o attraverso l’aria.  
Senza questo livello, i dati resterebbero solo concetti logici nei livelli superiori: qui diventano **bit in movimento**.
>
>In breve:  
>-  OSI → "Fisico" + "Data Link"  
>-  TCP/IP → li unisce nel **Network Access Layer**

---

## Il Modello ISO/OSI

Oltre al **modello TCP/IP**, che rappresenta il modello **operativo e pratico** su cui si basa Internet, esiste anche un altro importante schema concettuale per comprendere le reti: il **modello ISO/OSI**.

### Cos'è il modello ISO/OSI 
Il modello **[[ISO E OSI Model|OSI (Open Systems Interconnection)]]** è stato sviluppato dall’**ISO (International Organization for Standardization)** come **modello di riferimento teorico** per descrivere come avviene la comunicazione tra sistemi di rete.

A differenza del TCP/IP, che è nato da **esigenze pratiche** ed è diventato uno **standard de facto** per il funzionamento di Internet, il modello OSI aveva un obiettivo più ampio:

- creare uno **standard universale** per la progettazione dei protocolli di rete,
    
- garantire l’**interoperabilità** tra sistemi di produttori diversi,
    
- fornire un quadro concettuale chiaro per suddividere i compiti della comunicazione.
#### Caratteristica fondamentale 

Il modello OSI suddivide la comunicazione di rete in **[[ISO-OSI Reference Model.png|sette livelli (layer) astratti.]]** 

- Ogni livello ha un **compito specifico** ben definito.
    
- La comunicazione avviene solo con il **livello immediatamente superiore e inferiore**, creando così una struttura modulare e ordinata.


> [!example] **In sintesi**
> In breve:
>
>- **TCP/IP** → modello pratico e operativo, usato realmente per Internet.
  >  
>- **OSI** → modello concettuale e didattico, utile per capire la logica della comunicazione e per progettare protocolli interoperabili.

### I livelli del modello ISO/OSI
Il modello OSI è formato da **7 livelli numerati dal basso verso l’alto**.  

> [!remember] **Trucco Mnemonico in inglese per ricodare tutti e 7 i livelli**
> **“<mark style="background: #FFB8EBA6;">P</mark>lease <mark style="background: #ABF7F7A6;">D</mark>o <mark style="background: #ADCCFFA6;">N</mark>ot <mark style="background: #D2B3FFA6;">T</mark>hrow <mark style="background: #E5FF00A6;">S</mark>ausage <mark style="background: #FF0000A6;">P</mark>izza <mark style="background: #00FF02A6;">A</mark>way”**  
   (<mark style="background: #FFB8EBA6;">Presentation</mark>, <mark style="background: #ABF7F7A6;">Data Link</mark>, <mark style="background: #ADCCFFA6;">Network</mark>, <mark style="background: #D2B3FFA6;">Transport</mark>, <mark style="background: #E5FF00A6;">Session</mark>, <mark style="background: #FF0000A6;">Presentation</mark>, <mark style="background: #00FF02A6;">Application</mark>).

#### **7 – [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|Livello di Applicazione (Application Layer)]]** 

- **Scopo:** È il livello più alto e fornisce l’**interfaccia diretta tra le applicazioni e la rete**. È quello con cui l’utente finale interagisce in modo visibile.
    
- **Funzioni:** Gestisce i protocolli specifici dei servizi che usiamo ogni giorno, ad esempio:
    
    - **HTTP** → per la navigazione web.
        
    - **SMTP, POP3, IMAP** → per l’invio e la ricezione di email.
        
    - **FTP** → per il trasferimento di file.
        
    - **DNS** → per tradurre i nomi di dominio (es. `www.google.com`) in indirizzi IP.
        

> [!example] **In sintesi:**
> 👉 qui troviamo i protocolli che usiamo direttamente come utenti.



#### **6 – [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model presentationLayer Presentation Layer|Livello di Presentazione (Presentation Layer)]]**

- **Scopo:** Si assicura che i dati inviati da un sistema siano **comprensibili** per il livello Applicazione del sistema destinatario.
    
- **Funzioni principali:**
    
    - **Traduzione dei dati** → converte i dati in un formato standard, così che sistemi diversi possano capirsi (es. da ASCII a EBCDIC).
        
    - **Crittografia/Decrittografia** → applica o rimuove la cifratura dei dati per garantire sicurezza e privacy.
        
    - **Compressione** → riduce la quantità di bit da trasmettere, rendendo la comunicazione più veloce ed efficiente.
        

> [!example]  **In sintesi:**
> 👉 è il “traduttore” che prepara i dati perché possano essere letti correttamente.



#### **5 – Livello di Sessione (Session Layer)**

- **Scopo:** Gestisce la **comunicazione continua** (la “sessione”) tra due applicazioni in rete.
    
- **Funzioni principali:**
    
    - **Controllo del dialogo** → decide chi può trasmettere e per quanto tempo, regolando lo scambio.
        
    - **Sincronizzazione** → inserisce dei “checkpoint” nel flusso dei dati, così che in caso di errore la trasmissione possa riprendere dall’ultimo punto valido invece di ricominciare da zero.
        

> [!example] **In sintesi:**
> 👉 è come un “moderatore” che gestisce le conversazioni tra applicazioni.

#### **4 – [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model transportLayer Transport Layer|Livello di Trasporto (Transport Layer)]]**

- **Scopo:** Garantisce un **trasporto affidabile e trasparente** dei dati **end-to-end**, cioè da un processo (programma) su un computer a un processo su un altro computer.
    
- **Funzioni principali:**
    
    - **Segmentazione e riassemblaggio** dei dati in unità gestibili.
        
    - **Controllo di flusso** → regola la quantità di dati trasmessi per evitare congestioni.
        
    - **Controllo degli errori** → rileva e gestisce perdite o duplicazioni di dati.
        
- **Protocolli principali:**
    
    - **TCP (Transmission Control Protocol)** → affidabile, orientato alla connessione.
        
    - **UDP (User Datagram Protocol)** → veloce, non affidabile (senza connessione).
        

> [!example] **In sintesi:**
> 👉 è il livello che assicura che i dati arrivino corretti e nell’ordine giusto (con TCP), o semplicemente “il più veloce possibile” (con UDP).

#### **3 – [[Network, Transport, Session, Presentation, Application Layers#Network layer|Livello di Rete (Network Layer)]]**

- **Scopo:** Gestire l’**indirizzamento logico** dei dispositivi e scegliere il percorso migliore (**routing**) per i dati attraverso la rete.
    
- **Funzioni principali:**
    
    - **Indirizzamento logico** tramite **indirizzi IP**.
        
    - **Instradamento (routing)** dei pacchetti da una rete all’altra.
        
- **Protocollo principale:**
    
    - **IP (Internet Protocol)**.
        

> [!example] **In sintesi:**
> 👉  è il livello che decide **dove devono andare i pacchetti** e come ci arrivano.

#### **2 – [[ISO E OSI Model#dataLink-layer Livello data link|Livello di Collegamento Dati (Data Link Layer)]]**

- **Scopo:** Fornire un **trasporto affidabile** dei dati lungo un singolo collegamento fisico (rete locale).
    
- **Funzioni principali:**
    
    - **Framing** → organizza i bit in unità logiche chiamate _frame_.
        
    - **Indirizzamento fisico** → utilizza gli **indirizzi MAC** per identificare i dispositivi all’interno della rete locale.
        
    - **Controllo degli errori** → rileva (e a volte corregge) errori di trasmissione provenienti dal livello fisico.
        

> [!example] **In sintesi:**
> 👉 è il livello che gestisce la comunicazione tra due dispositivi **direttamente collegati** nella stessa rete.


#### **[[ISO E OSI Model#livelloFisico Livello fisico|1 – Livello Fisico (Physical Layer)]]**

- **Scopo:** Trasmettere e ricevere i **bit grezzi non strutturati** attraverso un mezzo fisico.
    
- **Funzioni principali:**
    
    - Definisce le **specifiche elettriche, meccaniche e funzionali**:
        
        - Cavi (rame, fibra ottica).
            
        - Segnali elettrici o ottici.
            
        - Frequenze radio (Wi-Fi).
            
        - Connettori e interfacce.
            

> [!example] **In sintesi:**
> 👉 è il livello più basso, responsabile della **trasmissione fisica** dei dati.


### Comunicazione tra livelli
Quando si parla del modello **ISO/OSI**, è importante capire non solo i singoli livelli, ma **come questi interagiscono** tra loro. Ci sono due concetti fondamentali:
#### 1. Comunicazione verticale (all’interno dello stesso computer)
Immaginiamo di dover inviare un file. 
L’applicazione (es. un browser) genera i dati e li passa al **livello di Applicazione.** 
Da qui, i dati scendono uno per volta attraverso i vari livelli: Presentazione, Sessione, Trasporto, Rete, Collegamento Dati e infine Fisico.

Ad ogni passaggio, il livello in questione **aggiunge informazioni proprie**.

- Il Trasporto aggiunge ad esempio un numero di porta.
    
- Il livello Rete aggiunge l’indirizzo IP.
    
- Il livello Collegamento Dati aggiunge l’indirizzo MAC.
    

Questo processo si chiama **incapsulamento**: 
- i dati vengono “impacchettati” con sempre più informazioni, un po’ come mettere un oggetto dentro a una serie di scatole sempre più grandi.

Sul computer destinatario il processo è opposto: 
- i dati risalgono dal [[ISO E OSI Model#^livelloFisico|livello Fisico]] fino all’[[ISO E OSI Model#^applicationLayer|Applicazione]]. 
- Ogni livello legge solo le informazioni che riguardano lui, le rimuove (de-capsulamento) e passa il resto al livello superiore.


####  2. Comunicazione orizzontale (tra due computer)

Un aspetto cruciale del modello OSI è che, anche se fisicamente i dati passano per **tutti i livelli**, **concettualmente** ogni livello “parla” solo con il suo corrispondente sull’altro computer.

Esempio:

- Il **livello Trasporto** sul PC mittente non “vede” cosa fanno gli altri livelli. Per lui la comunicazione avviene direttamente con il livello Trasporto del PC destinatario (es. TCP che invia segmenti a TCP).
    
- Lo stesso vale per il livello Rete (IP con IP), per il livello Collegamento Dati (MAC con MAC), ecc.
    

Questa comunicazione tra pari viene detta **peer-to-peer**.



> [!example] **In pratica:**
> - **Verticale** = ogni livello fornisce servizi al superiore e usa quelli dell’inferiore → è la catena interna al computer.
  >  
>- **Orizzontale** = ogni livello comunica con il suo equivalente sull’altro computer → è la logica della comunicazione tra due sistemi.

#### Analogia Filosofo, Traduttore e Segretaria
Riprendiamo l'analogia fatta nella lezione [[Internetwork-Protocols]]: 
![[Network communication.png|592x423]]

Questo è un chiaro esempio di comunicazione verticale: 
In **Location A** il messaggio del filosofo (“I like rabbits”) non passa direttamente al filosofo di Location B.  
Prima attraversa i suoi **livelli interni**:

- Filosofo (Livello 3) → genera il messaggio.
    
- Traduttore (Livello 2) → lo trasforma in olandese.
    
- Segretaria (Livello 1) → lo invia fisicamente via fax.
    

Allo stesso modo, in **Location B** il messaggio risale dal fax fino al filosofo:

- Segretaria (Livello 1) → riceve il fax.
    
- Traduttore (Livello 2) → lo trasforma in francese.
    
- Filosofo (Livello 3) → lo comprende.
    

Questa catena di passaggi **dal livello superiore a quello inferiore (e viceversa)** rappresenta la **comunicazione verticale**.

#### 2. Comunicazione orizzontale (tra sistemi diversi)
Se volessimo vedere queste esempio dal punto di vista della comunicazione orizzontale non sarebbe comunque sbagliato: 
- concettualmente, ogni livello “parla” solo con il suo pari sull’altro lato:

	- **Filosofo ↔ Filosofo** → il senso del messaggio (l’idea “I like rabbits” ↔ “J’aime bien les lapins”).
    
	- **Traduttore ↔ Traduttore** → la lingua del messaggio (inglese ↔ olandese ↔ francese).
    
	- **Segretaria ↔ Segretaria** → il canale fisico (fax).
    

Questa è la **comunicazione logica peer-to-peer (orizzontale)**.


> [!abstract]- **Comunicazione verticale vs. Comunicazione orizzontale**
> - **Comunicazione verticale** → è quella **pratica e reale**, cioè il flusso dei dati dentro un singolo sistema.  
>    Ogni livello passa i dati a quello immediatamente sotto (aggiungendo informazioni → incapsulamento) o sopra (rimuovendole → decapsulamento).  
>    Questo è ciò che avviene **fisicamente** durante una trasmissione.
 >   
>- **Comunicazione orizzontale** → è quella **concettuale e logica**, cioè l’idea che ogni livello di un sistema “parli” con il livello corrispondente sull’altro sistema.  
 >   In realtà i livelli non comunicano direttamente (es. il livello Trasporto di A non invia messaggi _diretti_ al Trasporto di B), ma possiamo pensarlo così per semplificare la comprensione del modello.
 >> [!example] **Quindi:**
 >> - **Verticale = interazione reale** tra livelli adiacenti nello stesso host.
 >>   
>>- **Orizzontale = interazione logica** tra livelli pari in host diversi.


---
## Comunicazione tra livelli
Quindi quando un messaggio viene inviato dal **mittente**, non passa direttamente al destinatario, ma attraversa tutti i livelli del modello, **dall’alto verso il basso**.  
Ad ogni livello i dati ricevono nuove informazioni di controllo, che servono a garantire che il messaggio arrivi correttamente e al destinatario giusto. Questo processo si chiama **incapsulamento**.

- **Livello 7 – Applicazione:** l’applicazione genera i dati (es. il testo di un’email).
    
- **Livello 6 – Presentazione:** i dati vengono tradotti, formattati, eventualmente compressi o crittografati.
    
- **Livello 5 – Sessione:** viene stabilita e gestita la sessione di comunicazione.
    
- **Livello 4 – Trasporto:** i dati vengono segmentati, numerati e corredati di informazioni per garantire affidabilità e controllo del flusso.
    
- **Livello 3 – Rete:** i segmenti vengono incapsulati in pacchetti con gli indirizzi logici (IP) necessari all’instradamento.
    
- **Livello 2 – Collegamento Dati:** i pacchetti diventano frame, con indirizzi fisici (MAC) e controlli di errore locali.
    
- **Livello 1 – Fisico:** i frame vengono tradotti in segnali elettrici, ottici o radio e trasmessi sul mezzo fisico.
    


Al **destinatario** avviene il processo opposto: 
- i dati risalgono la pila dei livelli **dal basso verso l’alto**. Ogni livello rimuove le informazioni di controllo aggiunte dal livello corrispondente del mittente. Questo processo è detto **decapsulamento**.  
Alla fine, l’applicazione riceve i dati originali, pronti per essere mostrati all’utente.


> [!example] Questa dinamica di **incapsulamento/decapsulamento** è fondamentale per capire il modello a strati: ogni livello aggiunge “la sua busta” al messaggio, e il destinatario deve aprirle una per una nell’ordine corretto.

### Comunicazione peer-to-peer

Anche se i dati **scendono verticalmente** attraverso i livelli di uno stack sul mittente e **risalgono verticalmente** sul destinatario, concettualmente ogni livello **dialoga con il suo pari sul sistema remoto**.

Questo significa che:

- Ogni livello del mittente **si comporta come se stesse comunicando direttamente** con il corrispondente livello del destinatario.
    
- Questa comunicazione logica è regolata dai **protocolli**, che definiscono **come i dati devono essere strutturati, interpretati e gestiti** tra due entità dello stesso livello.
    

**Esempi pratici:**

- **Livello di Rete (Network Layer):** comunica logicamente con il livello di rete del destinatario per instradare correttamente i pacchetti verso la destinazione.
    
- **Livello di Trasporto (Transport Layer):** dialoga con il livello di trasporto del destinatario per garantire affidabilità, controllo di sequenza e integrità dei dati.
    

> Questa separazione chiara di responsabilità per livello rende il modello OSI **molto utile** per progettare, comprendere e risolvere problemi nelle reti, perché ciascun livello ha compiti ben definiti e isolati dagli altri.


### Confronto tra il Modello OSI e il Modello TCP/IP

Anche se **Internet funziona principalmente sul modello TCP/IP**, il modello OSI rimane molto utile per comprendere la struttura e il funzionamento delle reti in modo più dettagliato.

### Livelli corrispondenti

- **Livello Applicazione (TCP/IP)**  
    Questo livello raggruppa le funzionalità dei **tre livelli superiori dell’OSI**:
    
    - **Livello 7 - Applicazione (OSI):** Fornisce interfaccia e servizi di rete per le applicazioni utente (es. browser, client email, HTTP, SMTP).
        
    - **Livello 6 - Presentazione (OSI):** Gestisce formattazione, crittografia e compressione dei dati.
        
    - **Livello 5 - Sessione (OSI):** Stabilisce, gestisce e termina il dialogo tra host.
        
- **Livello Trasporto (TCP/IP)**  
    Corrisponde al **Livello 4 - Trasporto (OSI)**: garantisce comunicazione end-to-end affidabile e controllo del flusso dei dati tramite protocolli come TCP e UDP.
    
- **Livello Internet (TCP/IP)**  
    Coincide con il **Livello 3 - Rete (OSI)**: gestisce l’indirizzamento logico (IP), l’instradamento e il percorso dei pacchetti attraverso le reti.
    
- **Livello di Accesso alla Rete (TCP/IP)**  
    Raggruppa le responsabilità dei due livelli inferiori dell’OSI:
    
    - **Livello 2 - Collegamento Dati (OSI):** gestione del framing e dell’indirizzamento fisico locale (MAC address).
        
    - **Livello 1 - Fisico (OSI):** trasmissione dei bit attraverso il mezzo fisico (cavi, Wi-Fi, ecc.).
        

#### Differenze principali

- **Modello teorico vs pratico:** OSI è un modello di riferimento concettuale, mentre TCP/IP è quello utilizzato realmente su Internet.
    
- **Numero di livelli:** OSI ha 7 livelli distinti, offrendo una separazione più netta delle funzionalità; TCP/IP ne ha 4 (o 5 se si distingue tra Collegamento Dati e Fisico), combinando alcune funzioni.
    

> Anche nel TCP/IP, come nell’OSI, ogni livello dialoga logicamente con il suo pari sul sistema remoto (peer-to-peer) mentre i dati viaggiano fisicamente **dal livello superiore a quello inferiore** sul mittente e **dal basso verso l’alto** sul destinatario, secondo lo schema di **incapsulamento e decapsulamento**.


### Comunicazione tra livelli nel modello TCP/IP

Il principio di **comunicazione a livelli** nel modello TCP/IP è molto simile a quello del modello OSI, anche se ci sono differenze nella suddivisione e nel numero dei livelli.

#### 1. Comunicazione verticale (tra livelli adiacenti)

- I dati **scendono dall’alto verso il basso** attraverso i livelli dello stack sul mittente.
    
- Ogni livello aggiunge **informazioni di controllo** (intestazioni, header) ai dati ricevuti dal livello superiore. Questo processo si chiama **incapsulamento**.
    
- Al destinatario, i dati **risalgono dal basso verso l’alto** e ogni livello rimuove le intestazioni aggiunte dal corrispondente livello del mittente. Questo processo si chiama **decapsulamento**.
    
- Ogni livello utilizza i servizi del livello inferiore e fornisce servizi al livello superiore.
    

#### 2. Comunicazione orizzontale (logica "peer-to-peer")

- Concettualmente, ogni livello comunica **con il corrispondente livello sul sistema remoto**.
    
- Questa comunicazione logica è regolata dai **protocolli specifici** di ciascun livello.
    
- **Esempi:**
    
    - **Livello di Trasporto (TCP/UDP):** gestisce affidabilità, controllo di sequenza e integrità tra i processi di trasporto dei due sistemi.
        
    - **Livello Rete (IP):** coordina l’instradamento dei pacchetti tra host remoti.
        

##### Differenze principali tra TCP/IP e OSI

- **Numero di livelli:**
    
    - TCP/IP: 4 o 5 livelli (Applicazione, Trasporto, Internet, Accesso alla Rete; oppure con separazione di Collegamento Dati e Fisico).
        
    - OSI: 7 livelli (Applicazione, Presentazione, Sessione, Trasporto, Rete, Collegamento Dati, Fisico).
        
- **Combinazione di livelli:**
    
    - Il **livello Applicazione** del TCP/IP include Applicazione, Presentazione e Sessione dell’OSI.
        
    - Il **livello di Accesso alla Rete** del TCP/IP include Collegamento Dati e Fisico dell’OSI.
        

> In sintesi, pur con differenze di nomi e numeri di livelli, il **principio fondamentale rimane lo stesso**: comunicazione verticale tra livelli adiacenti e comunicazione logica peer-to-peer tra livelli corrispondenti.