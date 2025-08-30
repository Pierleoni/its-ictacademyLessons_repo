# [[ISO E OSI Model|ISO/OSI]] Model vs TCP/IP Model

Il modello TCP/IP è un framework essenziale utilizzato per standardizzare e garantire una comunicazione dati affidabile attraverso reti interconnesse moderne, incluso Internet. 
Difatti è progettato per garantire uno scambio dati **standardizzato, affidabile e scalabile** tra sistemi eterogenei.


### Struttura del modello TCP/IP
È composto da **4 livelli**, ciascuno responsabile di funzioni specifiche nel processo di trasmissione dei dati. 


![](https://i.imgur.com/5ZFJkru.png)
^iso-osiANDtcp-ip


1. **[[#Application layer|Application Layer]]** – ==fornisce i protocolli per applicazioni e servizi di rete (HTTP, FTP, SMTP, DNS, ecc.)==.   ^applicationLayer
    
2. **[[#Transport Layer|Transport Layer]]** – ==gestisce la comunicazione tra processi con protocolli come **TCP** (affidabile, orientato alla connessione) e **UDP** (veloce, non affidabile)==.   ^TransportLayer
    
3. **[[#Livello Interent|Internet Layer]]** – ==si occupa dell’indirizzamento e dell’instradamento dei pacchetti tramite l’**IP**==.   ^InternetLayer
    
4. **[[#Network Access|Network Access (Link) Layer]]** – ==definisce come i dati vengono trasmessi fisicamente sulla rete== (Ethernet, Wi-Fi, ARP).   ^NetworkLayer

#### Confronto con il modello ISO/OSI
[[#^iso-osiANDtcp-ip|Guardando l'immagine soprastante]] possiamo notare come i 4 livelli del TCP/IP coprono le stesse funzionalità dei 7 livelli del modello ISO/OSI. 

> [!NOTE] **Nota:**
> Il modello ISO/OSI è teorico e quindi il modello TCP/IP pur essendo più semplice (solo 4 livelli) copre le stesse funzionalità in modo più pratico e integrato
- **[[#^applicationLayer|Application (TCP/IP)]]** ≈ Livelli 5-6-7 ([[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|Application]], [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model presentationLayer Presentation Layer|Presentation]], [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model sessionLayer Session Layer|Session]]) di ISO/OSI.
    
- **[[#^TransportLayer|Transport (TCP/IP)]]** ≈ [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model transportLayer Transport Layer|Transport]] (ISO/OSI).
    
- **[[#^InternetLayer|Internet (TCP/IP)]]** ≈ [[Network, Transport, Session, Presentation, Application Layers#Network layer|Network]] (ISO/OSI).
    
- **[[#^NetworkLayer|Network Access (TCP/IP)]]** ≈ [[ISO E OSI Model#dataLink-layer Livello data link|Data Link]] + [[ISO E OSI Model#livelloFisico Livello fisico|Physical]] (ISO/OSI).


> [!link] Caratteristiche dei due modelli
> - **TCP/IP:** ==è lo **standard de facto** nelle reti moderne, scelto per la sua **robustezza, flessibilità e diffusione**.==
 >   
>- **ISO/OSI:** ==rimane utile come modello **concettuale** e didattico, in quanto più dettagliato e modulare.==

## Application layer
Come anticipato, corrisponde ai livelli [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|Application]], [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model presentationLayer Presentation Layer|Presentation]] e il [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model sessionLayer Session Layer|Session]] del modello [[ISO E OSI Model|ISO/OSI]]. 
Questo livello è il più vicino all’utente ed è responsabile della gestione dei protocolli che permettono alle applicazioni di comunicare in rete.
#### Caratteristiche 
- ==Fornisce servizi di rete direttamente alle applicazioni utente.==  
- ==Gestisce i protocolli a livello applicativo.==

#### Protocolli principali
 ![[Application Layer.png]]

- **[[#Domain Name System (DNS)|DNS (Domain Name System)]]:**
	-  ==risoluzione dei nomi di dominio==.   ^DNS
    
- **HTTP/HTTPS (HyperText Transfer Protocol):**
	-  ==navigazione web==.    ^Http-https
    
- **FTP (File Transfer Protocol):** 
	- ==trasferimento di file==.   ^ftp
    
- **SMTP/POP3/IMAP:** 
	- ==protocolli per l’invio e la ricezione di e-mail==.   ^smtp-pop3-imap
    
- **DHCP (Dynamic Host Configuration Protocol):** 
	- ==gestione e assegnazione dinamica degli indirizzi IP.==    ^dhcp

### [[#^DNS|Domain Name System (DNS)]]
Il **Domain Name System (DNS)** è un sistema di denominazione **gerarchico** e **decentralizzato** che traduce i **nomi di dominio leggibili dall’uomo** (es. `www.cisco.com`) in **indirizzi IP leggibili dalle macchine** (es. `198.133.219.25`).



In pratica, quando vogliamo visitare un sito web ci basta ricordare il nome di dominio, mentre il DNS si occupa di tradurlo nell’indirizzo IP corrispondente, necessario per stabilire la connessione.


> [!example] **Esempio**
> `www.cisco.com` → `198.133.219.25`


Seguendo l'esempio fornito:  all'utente serve il nome di dominio (`www.cisco.com`) Il DSN lo traduce in indirizzo IP corrispondente, necessario per stabilire la connessione.
Questo perché il nome si compone di domini: 
- `.com` è il **Top-Level Domain (TLD)**
    
- `cisco` è il **Second-Level Domain**, cioè un sotto-dominio del TLD `.com`.

![](https://i.imgur.com/4ymJgVT.png)
#### Come funziona il DNS (passaggi principali)
Il DNS è un **componente critico di Internet**: senza di esso gli utenti sarebbero costretti a ricordare solo gli indirizzi IP.
Supponiamo di voler navigare su un sito web: apriamo il browser → componiamo l'URL→ premiamo invio:
Il flusso prevede **6 passaggi** che sono i seguenti: 
1. **DNS Query:** 
	- ==l’utente inserisce un nome di dominio nel browser==.
    
2. **Recursive Resolver:** 
	- ==la query viene inviata a un DNS resolver, che avvia il processo di risoluzione.==
    
3. **Root Server:** 
	- ==il resolver interroga un root server per ottenere l’indicazione del server TLD corretto (es. `.com`, `.org`)==.
    
4. **TLD Server:** 
	- ==il resolver interroga il server TLD per sapere quale sia il server DNS autorevole del dominio richiesto==.
    
5. **Authoritative DNS Server:** 
	- ==restituisce l’indirizzo IP associato al dominio==.
    
6. **Response:** 
	- ==il resolver invia l’IP al browser, che stabilisce la connessione con il web server.==

> [!info]
> Esistono server DNS pubblici, ad esempio quelli di **Google (8.8.8.8, 8.8.4.4)** o **Cloudflare (1.1.1.1)**.

### HyperText Transfer Protocol (HTTP)
È il protocollo utilizzato per la navigazione web: 
-  ==permette lo scambio di dati tra un **client** (il browser) e un **server** (il sito web)==.  
- 
Esiste anche la variante sicura - **HTTPS (HyperText Transfer Protocol Secure):** 
-  **è un’estensione di HTTP**. 
- ==Essa aggiunge un livello di sicurezza grazie alla crittografia, proteggendo i dati scambiati tra client e server==.

#### Come funziona la navigazione web
La navigazione web avviene tramite **6 passaggi:** 

![[HTTP - Web Browsing Process.png]]

1. **Digitazione dell’URL**: 
	- ==l’utente inserisce l’indirizzo di un sito nella barra del browser.==
    
2. **DNS Resolution**: 
	- ==il browser invia una query DNS per tradurre l’URL in un indirizzo IP.==
    
3. **Connessione al server**: 
	- ==il browser stabilisce una connessione con il server corrispondente.==
    
4. **Invio della richiesta**: 
	- ==tramite HTTP o HTTPS, il browser invia una richiesta (in genere di tipo `GET`) al server, solitamente per ottenere il documento predefinito (ad esempio `index.html`).== 
    
5. **Ricezione della risposta**: 
	- ==il server invia al browser il contenuto HTML della pagina richiesta.==
    
6. **Rendering della pagina**: 
	- ==il browser interpreta il codice HTML (insieme a eventuali CSS e JavaScript) e visualizza la pagina formattata.==


### FTP
Utilizzato per il trasferiento di file affidabile da un Host a un server (connection oriented) e  utilizza le connessioni TC, come ad esempio Internet. Facilita il trasferimento dei file tra un client e un server. 
3 step:
Stabilimento della conessione:
Controlo COnnection
Data Connection

Autenticazione:


Trasferimento del file: 
sfrutta entrambi le connessioni e usa il data transfer


### STMP/POP3/IMAP
Sono 3 protocolli, di invio STMP e gli altri di ricezioni

Il POP3 recupera le email scaricandole in locale e cancellandole dal server
ùIMPa: recupra le email per l'utente, le scarica ma lascia le email sul server rendendole accessibili da qualsiasi dispositivi

### DHCP (Dynamic Host Configuration Protocol)

DHCP è un protocollo utilizzato quando un nuovo device si collega a una rete per assegnare l'indirizzo IP 
Non sa qual'è il router invia in boradcast un messaggio in rete per scorprire chi è il DCHP server (il router) e quando il router risponde invia tutti i dati offrendo indirizzo IP dispponibile  e e le altre configuarzioni di rete. 
Il client risponde con un DHCP Request indicando che accetta le condizioni



## Transport Layer
Il Tcp usta per le connsessioni connection-oriented

### TCP
Fornisce l'affidabilità, stabilsce la connessione, la mantiene fin tanto che ci sono dati da trasferire e dopo che il trasferiemnto di dati non c'è più stacca la connessione.
L'host B risponde con due messaggi (l'ACK e il messaggio flag Fin questo serve nel caso in cui l'Host A abbia finito di mandare i dati ma l'host B no).

#### TCP Header Structure
nel caso del TCP oltre a porte sorgente e porte di destinazioni abbiamo anche altri campi chiave come 
L'acknowlegment number: confemra il riceviemtno di dati 
Checksum
FLags:
SYN
ACK
FIN


### UDP 
Per connessioni connectionless, è stato inserito il meccanismo di controllo di errori per evitare usi impropri di questo protocolli, a differenza delle connessioni connectionless del protocollo ISO/OSI
#### UDP Header Structure
Source e destination port
Length
Checksum


## Livello Interent
Il protoccolo IP 
ICMP
ARP 
### ICMP 
è un protocollo che viene utilizzato per creare il report riguarod una connessione, quindi utilizzato dai tool di diagnostica, e in grado di creare un report.
su windows `ping google.com` per vedere se il server di google è disponibile 
un altro commando è `tracert google.com`: permette di vedere il percorso di tutti i pacchetti trasporti per raggiungere la destinazione (dall'host al server).

### ARP 
si occuppa di tradurre gli indirizzi IP in indirizzi MAC all'intenro della LAN.
Come funziona:
Di fare questa traduzione se ne occupa il router che ha un tabella al suo intenro dove tutti gli indirizzi IP sono associati gli indirizzi MAC, se la tabella non è aggiornata il dispositivo che vuole comunicare manda in broadcast un 
ARP Request
il dispoistivo dall'altro capo risponde con un ARP Reply
 e infine c'è il ARP Cache.


## Network Access
Protocolli Ethernet e wi-fi
