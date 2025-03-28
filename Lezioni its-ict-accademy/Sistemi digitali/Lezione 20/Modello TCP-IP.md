# [[ISO E OSI Model|ISO/OSI]] Model vs TCP/IP Model

Il modello TCP/IP è un framework essenziale utilizzato per standardizzare e garantire una comunicazione dati affidabile attraverso reti interconnesse, inclusa Internet. È composto da quattro livelli, ciascuno responsabile di funzioni specifiche nel processo di trasmissione dei dati. 
![](https://i.imgur.com/5ZFJkru.png)

Come possiamo notare dall'immagine i quattro livelli del modello TCP/IP sono equiparabili ai 7 livelli del modello ISO/OSI. 
Il modello TCP/IP è lo standard de facto per la comunicazione su Internet e nelle reti, ampiamente adottato per la sua robustezza e flessibilità.
## Application layer
Equiparabile ai livelli [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|livello di applicazione]], [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model presentationLayer Presentation Layer|livello di presentazione]] e il [[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model sessionLayer Session Layer|livello di sessione]] del modello ISO/OSI. 
==Fornisce servizi di rete direttamente alle applicazioni utente.==  
Gestisce i protocolli a livello applicativo.
I protocolli di questo livello sono:
- [[#Domain Name System (DNS)|DNS]] : Domain name resolution
- HHTP/HTTPS: navigazione web
- FTP: Trasferimento file
- SMTP/POP3/IMAP: email
- DHCP: Gestione dell'assegnazione degli indirizzi IP

### Domain Name System (DNS)
È un sistema di nominazione decentralizzato e gerarchico che traduce nomi logici (ad esempio `www.cisco.com`) in indirizzi IP (ad esempio `198.133.219.25`). 
![](https://i.imgur.com/4ymJgVT.png)

In sostanza se voglio visitare il sito della CISCO devo solo ricordare l'URL e la macchina lo traduce in indirizzo IP (198.133.219.25). Quindi serve il nome di dominio e li traduce in indirizzo IP, questo perché il nome si compone di domini; ad esempio `.com` è un dominio top level main e `cisco` e un sotto dominio di `.com`.
#### Come lavora il DNS
Supponiamo di voler navigare su un sito web: apriamo il browser componiamo l'URL e premiamo invio:
Si crea un DNS Query: il processo di inizio quando l'utente digita un nome di dominio dentro un web browser
, in seguito si va ad azionare il Recursive Resolver: la query è mandata a un DNS resolver, 
dopodichè entra in gioco Il Root Server (necessario per evitare di fare ricerche non necessarie), in seguito si va al TLD Server(specifica il domino), dopodichè entra in gioco il Authoritative DNS Server e per ultimo il Response

Esistono diversi server pubblici come google, etc.

### HTTP
il protocollo utilizzato per la navigaxione web tra client(browser) e server(il sito dove è). Esistone la navigazione sicura che è il HTTPS che è un estensione dell'HTTP e aggiunge sicurezza e provedde a una comunicazione sicura che encripta i dati che vengono scambiati tra il cliente e il server. 

#### Come funziona la navigazione web
1. L'utente digita l'URL
2. DNS Resolution: si dice tramite a una query di tradurre l'URL in un indirizzo IP
3. Server Connection: il browser stabilisce una connessione per identificare il server
4. Sending a Request: usa l'HTTP o HTTPS, il browesr manda una richiesta di GET  al server, tipicamente ricihede il documento di default (es: index.html)
5. Receiving a Request: Il server risponde mandando il contenuto HTML della pagina web richiesta
   pagina web al browser
6. Rendering the page


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
