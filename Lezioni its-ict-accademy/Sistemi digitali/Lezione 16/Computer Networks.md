# Network, Transport, Session, Presentation, Application Layers

Riprendiamo dal modello [[ISO E OSI Model|ISO/OSI]] adesso riprendiamo dall'ultimo livello di questo modello e introduciamo gli altri
## Network layer
[[ISO E OSI Model#^networkLayer|Il livello di rete]] è il terzo livello nel modello ISO/OSI.
![[Network Layer.png]] 
Definisce come i dati vengono inviati ai dispositivi riceventi attraverso più reti. 
Nello specifico è responsabile delle funzioni di 
1. **[[#routingProc Routing Process|Routing]]:** 
   Definisce il percorso ottimale per i dati per viaggiare dalla sorgente alla destinazione.   ^routingProc
   
 2. **Forwarding(instradamento):**
    Muove i pacchetti dall'input del router all'output appropriato.
    
 3. **Logical Addressing(indirizzamento):** 
    in questo livello viene scelto il percorso per inviare i pacchetti, l'azione di inviarli (forward) è gestita utilizzando l'indirizzo IP, che identifica in modo univoco i dispositivi sulla rete.
    
 4. **Frammentazione e Riassemblaggio:**  
    Scompone i pacchetti di grandi dimensioni in frammenti più piccoli e li riassembla alla destinazione.
### Struttura del pacchetto del Header 
Anche in questo livello abbiamo l'header del pachetto.

![[Packet Header Structure.png|600*400]] 

> [!info]  Il Time to live (TTL) decide se distruggere il pacchetto o meno, nel caso in cui viene considerato perso. 


### [[#^routingProc|Routing Process]]
Il processo di questo livello viene chiamato in processo di routing ed è diviso in 3 step:
1. Determinazione del percorso: determina il percorso
2. Packet switcging: inoltro da un route al all altro in base alla tabella che si trova nella determinazione del percorso
3. Next -Hop Forwarding: salto del pachetto da un router all'altro. 
![[Routing Process.png]]

### Path determination
Di come avviene la determinazione del percorso migliore dalla sorgente alla destinazione.
Le tabelle di routing: sono tabelle che sono nei vari routing
il routing puo essere statico, cioè il costruttore determina i percorsi, dinamico, cioè il percroso è scelto automaticamente 
Gli algoritmi di ruoting per scegliere il percroso meigliore possono basarsi sul concetto del percorso più breve (detemrinato da una somma: supponiamo di avere la topologia di rete dell'immagine sopra; il percorso più breve è detemrianto sommando i vari pesi sulle conessioni, quella che restituisce il valore più basso è il percorso più breve) o sul vettore della distanza: si basa sul numero di OOP che servono per raggiungere la sorgente e la destinazione e posso scegliere quello che ha meno OOP.
La prima metodologia che sfrutta la funzione culumativa è quella più usata per reti di grandi diemsnioni perché non serve conoscere l'intera topologie di rete. 
L'altra basata sugli OOP è più facile da implementare ed è molto usata per reti piccole, ovviamente in questo caso è necessario della tipologia della rete perché senno il router continua ad aumentare il numero di OOP all'infinito (count ot infinity)
### Packet switching
è il processo di mouvere i pachetti dalla porta di input alla porta di output basandosi sulle tabelle di routing accenate prima. 
Come vinee spostato all pachetto in 2 modi 
1. Store and forward: il router prima di mandarlo in output aspeta di aver ricevuto l'intero pachhetto, una volta che l'ha avuto legge l'indirizzo IP del desitinatario e lo invia e in base alla tabella di routing sa su quale porta fallo uscire
2. Il cut trough: il router non apsetta di aer ricevuto l'intero pachetto ma legge già l'indirizzo IP di destinazione già lo invia.
(la scelta cambia in base alla modalita della rete, per il primo i router sono dotati di una piccola memoria anche buffer e se quella porta è occupata i pacchetti vengono temporaneamente bloccati, ovviamente ha lo scopo di non perderli. Il buffering viene utilizzato nei entrambi casi)
Forwarding decision: il router decide su quale router mandare il pacchetto 

### Store and 
è il metodo più affidabile, il router ricevere l'intero pacchetto e controlla se i dati sono integri, tutto ciò avviene prima dell'invio. Se il pachhetto è valido viene mandato in uscita viceversa viene distrutto. 
I vantaggi sono 
affidabilità 
Inoltre permette di impostare le proprietà dei pachetti, ovviamente c'è una maggiore latenza per via dei vari controlli ma anche perché deve attendre l'invio dell'intero pacchetto. 
### Cut Torugh 
il pachetto viene inviato non pappena l'indirizzo di destinazione viene letto. 
Il pacchetto arriva sulla porta di input del router e non apppena quest'ultimo riesce a leggere l'indirizzo IP, che a sua volta viene tradotto in indirizzo MAC perché serve affinche il pacchetto venga inviatao a quel determinato router, del destinatario invia il data packet. 
IMetodo utilizzato quando sono necessarie alte prestazioni in velocità, ma lo svantaggio è che i pacchetti corrotti vengono inoltrati.
### Next Hop Forwaridn 
è il salto del pacchetto da un orute all'altro o quando raggiunge la destinazione finale. L'indirzzo IP detemrina su quale router deve essere inviato il pacchetto 
L'ARP è un potocollo traduce l'IP in indirizzo MAC per identificare il prossimo router al livello fisico.
Il router lavoro al livello network e lo switch data link, a livello network quando il pacchetto arriva al router. 
Questo è un esempio di tabella di routing su ogni router e viene cotruita con gli algoritmi di routing: 
![[Routing Process2.png]]

Deault trouter : è la regola che viene seguita quando non ci sono altre corrsipondeze nella tabella, quando arriva un data packet che non segue una regola e di conseguneza lo mando sulla defualt route nella speranza cge seuendo questo percorso arriva su un riouter che ha una regola per quel data packet.

### Logical Addressing 

abbiamo 2 versioni di indirizzo IP:
versione 4 a 32 bit
versione 6 a 128 bit 

La versione 4 nata prima ma sta esaurrendo gli spazi di indirizzi e per questo hanno invetato la versione 6. Stiamo a livello network 

### La versione 4 dell'IP
sono 4 numeri di tre cifre, partono da 0 arrivano a 255.
Esistono diversi clssi che detemrinano lo scopo della rete e il suo dimensionamento. 


### La maschere di rete (subnet mask sctructure)
è un numero di 32 bit che seve a suddividere la rete tra l'Host e la rete a cui eè connesso. 
In binario anche essa è formato da 4 gruppi di otteti (gruppi di otto bit), dove gli `1` identificano la rete, e gli `0` identificano l'Host. 

#### Combingi IP adress and subnet mask 

### IPv4 Class A e Class B 
la classe A ha un range da 0 a 255
il rannge rappresenta la rete e tutti gli altri gruppu sono usati per rappresentare l'Host, di conseguenza questa classe ci lavorano gli internet service provider (vodafone, Tim, etc.)
lasse B: 
il range da 128 a 191.255.255
in questo caso la subnet mask è 255.255.0.0. 
Questa è la classe dove rientrano le reti di medie dimensioni come la univerità o le grandi aziende

Classe C 
il range va da 192.0.0 a 255.255.255
la subnet mask è 255.255.255.0 
In questa classe lavorano le reti domestiche   

Classe D: 
parte da 244.0.0.0 a 239.255.255.255
la subnet mask è di 255.255.255.255
è una classe dedicata alle reti broadcast 

Classe E 
dedicata per scopo sperimentale 

### Private and Public IP
L'indirizzo IP pubblico è utilizzato per navigare su internet ed è fornito dall'internet provider, quindi il server viene collegato ad un indirizzo IP pubblico
Indirizzo IP privato è associato al nostro device all'interno della LAN, perciò un dispositivo ha due indirizzo IP: 
uno privato associato al dispositivo e uno pubblico dato dall'internet provider: entrambi sono dinamici perché all'interno della LAN te lo assegna il router e quello pubblico è fornito dal internet service provider. 
Tecnologie di rete che permette la connessione tra IP privati e pubblici avviene attraverso il NAT: traduce indirizzi privati a indirizzi pubblici e viceversa. 
Il NAT permette di collegare diversi indirizzi privati a un unico indirizzo pubblico. 

## Transport Layer
Si occupa della comunicazione end-to-end: cioè dalla sorgente alla destinazione, esempio in whatsapp il messaggio parte dalla sorgente e viene decifrato solo alla destinazione e non in mezzo al percorso, quindi non sugli altri dispositivi. 
Un analogia che puossiamo usare è: supponiamo di avere una east coast e una west coast dove vivono dei cugini, i cugini di una west coeast vogliono comunicare con i cugini della east coast, i folks della costa ovest consegnano la lettere alla zio Bill (Transposrt LAyer), allo zio Bill non interessa cosa succede in mezzo e dopo che la lettera arriva la prenderà lo zio Sam e la consegnera ai cugini della east coast.

### Funzioni
Error detction and correction: non sempre non viene previsto solo nei casi delle connessioni TCP/IP.  La correzzione di errore nei data link avviene su ogno nodo mentre nei meccanismi end to end la correzzione avviene solo nella destinazione. 
Flow control: possiamo definoire se la consessione e conection oriented  o connectionless.

Una volta ricevuti dei dati e una volta riscorstuti bisogna capire a quale applicazioni assegnarli.
Per fare cio si utilizzano le socket 

### Sockets 
Le applicazioni che comunicano tramite sockets(porte/interfaccie) la sockets viene ancorata all'indirizzo IP dopo i due punti: quindi ho l'indirizzo IP che mi rileva la rete e l'Host dopo ho la socket mi identifica l'applicazione a cui devo accedere. 
È una porta statica ma è associato alla applicazione. 

### Header del segmento 
Ogni livello aggiunge un header, oltre ai dati gli altri paramenti sono la porta sorgente e la porta di destinazione. Ongi volta che ci aaviciniamo al livello applicativo l'header inizia a contenere meno informazioni iniziamo ad avere. 

## Session Layer 
Gestisce e controlla le connessioni e la comunicazioe tra applicazioni, quindi controlla la conessione logica tra le applicazioni: due applicazioni devono comunicare e avvia la sessione di comunicazioni. Nel session iniziamo a parlare di connessioni tra applicazioni. 
Qui avvia la sessione tra apllicazioni e definisce se questo dialofgo deve essere
half duplex: la comunicazione deve andare in entrmabe le direzione ma non è simultanea 
full-duplex: la comunicazione avviene in entrambe le direzione ed è simultanea. 


## Presentation Layer 
I dati che arrivano dalla applicazione vengono convertiti in formati che sono leggibili per il dispositivi che riceve, questo livello rende compatibile la presentazione tra due dispositivi diversi. 
Quindi traduce, encripta/decripta: 
e comprime
Application Layer
Qui abbiamo l'interfaccia utente che permettono di comunicare e interagire attraverso la rete, e qui vengono eseguiti i programmi.










