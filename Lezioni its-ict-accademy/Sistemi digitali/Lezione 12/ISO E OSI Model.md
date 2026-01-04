# ISO/OSI Model, Physical Layer, Data Link Layer
## Introduzione 

## Network Architecture
L'architettura di rete è:
- ==un framework che delinea la struttura e il funzionamento di una rete, composta da un insieme di livelli e protocolli che stabiliscono come i dati vengono trasmessi e ricevuti.== 
![[Network Architeture.png]] 
- Il modello **ISO/OSI** (International Organization for Standardization / Open Systems Interconnection) si inserisce all'interno di questo contesto: 
 ==è un'architettura di rete teorica suddivisa in **7 livelli**, utile per standardizzare la comunicazione tra dispositivi diversi.== 
Contrariamente Il modello **[[Modello TCP-IP|TCP/IP]]** è una versione pratica, effettivamente utilizzata nelle reti moderne, suddivisa **4 livelli principali**.
Prima di approfondire il modello **ISO/OSI** dobbiamo parlare di architetture di rete proprietarie e architetture di rete non proprietarie.
### Reti Proprietarie e Reti non proprietarie  
Le reti possono essere classificate in **proprietarie** e **non proprietarie** in base all'uso di protocolli aperti o chiusi.
1. **Reti Proprietarie:**
   ==Le reti proprietarie sono architetture di rete sviluppate da un produttore specifico, con protocolli e tecnologie esclusivi, progettate per garantire la comunicazione tra dispositivi all'interno dello stesso ecosistema, spesso con limitata interoperabilità con reti di altri produttori.==
   Quindi è lo stesso produttore che stabilisce i protocolli, standard e tecnologie utilizzate nella rete. 
   Difatti le scelte possono essere sono arbitrarie e non seguire standard aperti, rendendo così la rete incompatibile con dispositivi di altri produttori.
   
> [!example]+ Esempio di Reti Proprietarie 
> - **AppleTalk** 
> - **Token Ring di IBM**
> - **PROFINET**.


2. **Le Reti Non Proprietarie:**
   ==Le **reti non proprietarie** sono architetture di rete basate su standard aperti, che consentono l'interoperabilità tra dispositivi e sistemi di diversi produttori.==
 

> [!example]+ Esempio di reti non proprietarie
> -**Ethernet
> -TCP/IP
> -Wi-Fi 
> -Bluetooth**.

#### Standard de Facto e de Iure
Il concetto di reti proprietarie e non proprietarie si collega alla distinzione tra **standard de facto** e **standard de iure.**
**Standard de facto**: si dice **de facto** quando un'architettura di reti viene adottata su larga scala grazie alla diffusione e all'efficacia pratica, senza un'approvazione formale da enti normativi. 
Come ad esempio il protocollo **TCP/IP**, che è diventato il protocollo di riferimento per Internet.
**Standard de iure**: si dice **de iure** quando un'architettura viene definita da organismi internazionali e formalmente riconosciuti. 
Come ad esempio l'**ISO/OSI**, sviluppato dall’ISO per creare un modello teorico di riferimento per la comunicazione in rete.
Quindi in pratica, molte reti **non proprietarie** si basano su **standard de facto** come **TCP/IP**, mentre reti **proprietarie** spesso usano protocolli specifici, senza una standardizzazione riconosciuta. 
Tuttavia, alcuni standard de iure possono essere adottati in reti proprietarie o non proprietarie, garantendo maggiore interoperabilità.

## ISO/OSI model
Il modello OSI (Open System Interconnetcion) è stato fondato nel 1984 e il suo risultato di lavoro dell'ISO(International Organization for Standardization). 
Si tratta di un modello di uno standard de iure.
Lo scopo è:
- ==Fornire un **modello di riferimento** per confrontare le diverse architetture di rete.==
Il modello **ISO/OSI** è una descrizione astratta della comunicazione e della progettazione dei protocolli di rete basata su livelli. Esso suddivide l'architettura di rete in **sette livelli**.
Il modello ISO/OSI è stato progettato seguendo i seguenti principi:
- ==Ogni livello deve avere un **diverso livello di astrazione**==.
- ==Ogni livello deve avere una **funzione ben definita**==.

La scelta dei livelli deve:

- ==**Minimizzare** il passaggio di informazioni tra i livelli.==
- ==**Evitare** di concentrare troppe funzioni in un unico livello.==
- ==**Evitare** un numero eccessivo di livelli.==
Come detto poco sopra, il modello **ISO/OSI** è strutturato in **sette livelli:** ==ordinati dal più basso (vicino all'hardware) al più alto (vicino all'utente==). 
Ogni livello svolge una funzione specifica e interagisce con il livello adiacente.
![[ISO-OSI Reference Model.png]]

1. **[[#livelloFisico Livello fisico|Livello Fisico(Physical)]]:** 
   ==Definisce le caratteristiche fisiche della rete, come cavi, segnali elettrici e trasmissione dei bit==.  ^livelloFisico
   
   
2. **[[#dataLink-layer Livello data link|Livello di Data Link(Collegamento tra dati)]]:** 
   ==Organizza i bit in **frame**, gestisce gli errori di trasmissione e controlla l'accesso al mezzo trasmissivo.==  ^dataLink-layer
   

3. **[[Network, Transport, Session, Presentation, Application Layers#Network layer|Livello di Rete (Network)]]**:
   ==Si occupa dell'instradamento dei pacchetti e dell'indirizzamento logico, utilizzando protocolli come **IP**==.  ^networkLayer
   
   
4. **[[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model transportLayer Transport Layer|Livello di Trasporto (Transport)]]**:
   ==Assicura la consegna affidabile dei dati tra i dispositivi, con protocolli come **TCP** e **UDP**==.  ^transportLayer
   
5. **[[Network, Transport, Session, Presentation, Application Layers#Session Layer|Livello di Sessione (Session)]]**:
   ==Gestisce l'avvio, il mantenimento e la chiusura delle sessioni di comunicazione tra applicazioni==.  ^sessionLayer
   
   
6. **[[Network, Transport, Session, Presentation, Application Layers#Presentation Layer|Livello di Presentazione (Presentation)]]**:
   ==Converte, comprime e cripta i dati per garantire compatibilità tra i diversi sistemi.==   ^presentationLayer
   
   
7. **[[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|Livello di Applicazione (Application)]]**:
   ==Fornisce servizi di rete agli utenti e alle applicazioni, come **HTTP, FTP e SMTP**==.  ^applicationLayer



> [!remember] **Trucco Mnemonico in inglese per ricodare tutti e 7 i livelli**
> **“<mark style="background: #FFB8EBA6;">P</mark>lease <mark style="background: #ABF7F7A6;">D</mark>o <mark style="background: #ADCCFFA6;">N</mark>ot <mark style="background: #D2B3FFA6;">T</mark>hrow <mark style="background: #E5FF00A6;">S</mark>ausage <mark style="background: #FF0000A6;">P</mark>izza <mark style="background: #00FF02A6;">A</mark>way”**  
   (<mark style="background: #FFB8EBA6;">Physical</mark>, <mark style="background: #ABF7F7A6;">Data Link</mark>, <mark style="background: #ADCCFFA6;">Network</mark>, <mark style="background: #D2B3FFA6;">Transport</mark>, <mark style="background: #E5FF00A6;">Session</mark>, <mark style="background: #FF0000A6;">Presentation</mark>, <mark style="background: #00FF02A6;">Application</mark>).


Nei primi tre livelli (Fisico, Data Link e Rete), il dato viene generalmente chiamato **bit, frame o pacchetto**, mentre nei livelli superiori può essere chiamato **segmento, messaggio o dato** a seconda del contesto.

I primi tre livelli sono spesso detti **"media layers"**, perché gestiscono il trasporto dei dati attraverso la rete e includono dispositivi come **router e [[#Network Switch|switch]]**. 
Mentre gli ultimi 4 livelli sono detti **"Host Layers"** perché si occupano della elaborazione dei dati e del loro utilizzo delle applicazioni e dell'utente; in parole povere si lavorano a livello software per garantire che i dati vengano **trasferiti, elaborati e presentati correttamente** all'utente.
I dispositivi finali, come **computer e smartphone**, operano su tutti e sette i livelli del modello.
## I primi 2 livelli del modello ISO/OSI
## [[#^livelloFisico|Livello fisico]] 
- Il **livello fisico** è responsabile della connessione fisica tra i dispositivi. 
- Si occupa della trasmissione e della ricezione di **flussi di bit grezzi** su un mezzo fisico.
 
**Principali mezzi fisici di trasmissione:**

- **Cavi in rame** (es. [[#Cavi coassiali ed Ethernet|Ethernet, cavo coassiale]]).  ^caviRame
  
- **Cavi in fibra ottica**;
- **Frequenze radio** (es. Wi-Fi, Bluetooth). 
### [[#^caviRame|Cavi coassiali ed Ethernet]] 

#### Cavi Ethernet
==I **cavi Ethernet** sono tra i più diffusi per la creazione delle **Local Area Network (LAN)**, in quanto permettono di connettere i dispositivi in rete in modo affidabile==. 
Sono composti da **coppie di fili di rame intrecciati** tra loro: 
==una tecnica che riduce le **interferenze elettromagnetiche** e migliora la qualità del segnale.==  
==Ogni filo di rame è rivestito da una **guaina isolante in plastica**, con colori diversi per distinguere i canali di trasmission==e. 
L'insieme delle coppie di fili è poi protetto da un'ulteriore **guaina esterna:** 
==serve a schermare il cavo e aumentarne la resistenza meccanica==.

![[cavo ethernet.png|369x166]]


#### Cavi Coassiali
Il **cavo coassiale** è un tipo di cavo elettrico costituito da un 
- ==**conduttore centrale in rame.**== 
- ==circondato da uno **strato isolante.**== 
- ==una **schermatura metallica.**== 
- ==e una **guaina esterna isolante.**== 
Questa struttura offre ==**ottima protezione contro le interferenze elettromagnetiche**, garantendo una trasmissione del segnale più stabile e di qualità superiore rispetto ai cavi Ethernet, soprattutto su **lunghe distanze**.== 
Inoltre, il cavo coassiale consente una **maggiore velocità di trasmissione dei dati**, motivo per cui viene utilizzato in applicazioni che richiedono **alta larghezza di banda**, come le connessioni via cavo per la TV e le reti a lunga distanza.

![[Cavo Coassiale.png|399x218]]
#### Cavo a fibra ottica
==Il cavo a fibra ottica è un tipo di cavo di rete che utilizza la luce per trasmettere dati ad alta velocità su lunghe distanze==. 
Quindi i dati viaggiano su questo cavo sotto forma di impulsi luminosi, il che consente di raggiungere tassi di trasmissione molto più elevati rispetto ai cavi tradizionali. Inoltre, ==il cavo a fibra ottica è immune alle interferenze elettromagnetiche==, garantendo una trasmissione dei dati pulita e affidabile.

##### Struttura del cavo a fibra ottica:

- **Nucleo (Core)**: ==La parte centrale della fibra, realizzata in vetro o plastica, attraverso la quale viaggiano i segnali luminosi.==
- **Rivestimento (Cladding)**: ==Circonda il nucleo e riflette la luce all'interno del nucleo stesso, minimizzando la perdita di segnale==.
- **Coating**: ==Protegge la fibra da danni e umidità==.
- **Guaina esterna (Outer Jacket)**: ==Fornisce ulteriore protezione contro i fattori ambientali.==
![[Cavo fibra ottica.png|484x222]]
### Connessioni wireless

==Il trasferimento dati tramite radiofrequenza (RF) implica la trasmissione di dati in modalità wireless attraverso onde elettromagnetiche==. 
Le tecnologie più diffuse che utilizzano RF per abilitare la comunicazione wireless tra dispositivi sono il Wi-Fi e il Bluetooth.

#### Wi-Fi

- **Bande di frequenza**: I==l Wi-Fi opera principalmente nelle bande di frequenza 2.4 GHz e 5 GHz, con i nuovi standard che utilizzano anche la banda 6 GHz. La banda a 2.4 GHz è particolarmente nota per la sua stabilità==.
- **Range**: ==Tipicamente copre una distanza fino a 100 metri all'interno degli edifici, a seconda dell'ambiente e degli ostacoli presenti==.
- **Tipo di rete**: ==Di solito fa parte di una [[Reti di computer#Reti e classificazione geografica|rete locale (LAN)]], dove più dispositivi si connettono a un router centrale o a un punto di accesso==.
- **Applicazioni**: ==Accesso a Internet, servizi di streaming, giochi online, connettività per smart home e networking aziendale==.

#### Bluetooth

- **Bande di frequenza**: ==Il Bluetooth opera nella banda ISM (Industriale, Scientifica e Medica) a 2.4 GHz==.
- **Range**: ==Tipicamente copre una distanza fino a 10 metri, con alcune versioni (come il Bluetooth 5) che possono estendersi fino a 100 metri==.
- **Tipo di rete**: ==Di solito forma una rete personale (PAN), dove i dispositivi si connettono direttamente tra loro o attraverso un dispositivo centrale in una topologia a stella==.
- **Applicazioni**: Connessione di periferiche (ad esempio, cuffie, tastiere), trasferimento di file tra dispositivi mobili, streaming audio wireless e controllo di dispositivi smart home.

#### Vantaggi del trasferimento dati RF

- ==Elimina la necessità di cavi fisici, offrendo maggiore mobilità e comodità.==
- ==Semplifica il processo di connessione e comunicazione tra i dispositivi==.

### Frequenza 
==La frequenza rappresenta il **numero di oscillazioni di un'onda in un dato intervallo di tempo**==. Si misura in Hertz(Hz) dove un 1Hz equivale a un ciclo al secondo 


> [!Example] Esempio di cicli al secondo partendo dagli Hertz
> - **50 Hz** = 50 cicli al secondo
> - **1000 Hz (1 kHz)** = 1000 cicli al secondo
> - **5 kHz** = 5000 cicli al secondo
> - **1 MHz** = 1.000.000 cicli al secondo

Quindi ogni Hertz rappresenta un'oscillazione completa dell'onda in un secondo. 
![[Frequency.png]]
In questa immagine possiamo vedere un'onda periodica, sull'asse delle ordinate (x) abbiamo il tempo o frequenza mentre sull'asse delle ascisse (y) abbiamo l'ampiezza del segnale (dB).
Il quadrato in rosso va a sottolineare il ciclo completo dell'onda  in un secondo.
### [[Bandwidth (Larghezza di banda)]]
==La **larghezza di banda** è l'intervallo di frequenze all'interno di una determinata banda occupata da un segnale==. 
==Si calcola come la differenza tra la frequenza più alta e quella più bassa== dell'intervallo ed è misurata in **Hertz (Hz)**.

La larghezza di banda effettivamente sperimentata dagli utenti può essere inferiore a causa di fattori come **congestione della rete, distanza dal router, interferenze e capacità dei dispositivi**.

### Larghezza di Banda

==La larghezza di banda definisce la quantità di dati che può essere trasmessa su una connessione di rete in un determinato periodo di tempo, generalmente misurata in **bit per secondo (bps)**==. 
Una larghezza di banda maggiore indica una maggiore capacità di trasporto dei dati, risultando in una trasmissione più veloce e in **prestazioni migliori nelle comunicazioni di rete.**

#### Bandwidth delay product
==Il **Bandwidth-Delay Product** definisce la quantità massima di dati (espressa in bit) che può essere in transito in un collegamento di rete in un dato momento==.

![[Bandwidth delay.png]]
Per spiegare meglio il concetto di Bandwidth Delay Product (BDP), partiamo da questa immagine:
- **La cross section: bandwidth:**
   ==la **larghezza di banda**, ossia la quantità di dati che possono fluire attraverso il collegamento per unità di tempo==. 

> [!ticket] Maggiore è la sezione, maggiore sarà la quantità di dati che possono attraversare la rete contemporaneamente.
>    

- **Length: Delay (Lunghezza: Ritardo)**  
==La lunghezza del tubo rappresenta il **ritardo (delay)**, ovvero il tempo necessario affinché i dati viaggino da un'estremità all'altra della connessione==. 
Un tubo più lungo implica un maggiore tempo di percorrenza.

- **Volume: Bandwidth × Delay (Volume: Larghezza di banda × Ritardo)**  
Il volume del tubo rappresenta il **Bandwidth-Delay Product:** 
==ossia la quantità totale di dati che possono essere "contenuti" nella rete in un dato momento==. 
Se il tubo è lungo (alto ritardo) o ha una grande sezione (alta larghezza di banda), la quantità di dati in transito sarà maggiore.

![[Bandwidth delay Product2.png]]
Questa immagine ci mostra un'applicazione pratica del **BDP**, dove c'è un 
- **Sender:**
	- colui che manda i pacchetti dati  
- **Receiver:** 
	- colui che riceve questi pacchetti dati.
#### Analisi dell'immagine

1. **Parametri del collegamento**
    
    - **Bandwidth (Larghezza di banda):** 5 bps (bit per secondo)
    - **Delay (Ritardo):** 5 s (secondi)
    - **Bandwidth-Delay Product:** 5 bps×5 s=25 bit  
        → ==Questo significa che **massimo 25 bit possono essere in transito contemporaneamente nella rete**==.
1. **Dinamica della trasmissione**
    
    - Il **mittente (Sender)** invia 5 bit ogni secondo.
    - Tuttavia, i bit devono attraversare un canale con **ritardo di 5 secondi**, quindi impiegheranno 5 secondi per raggiungere il **ricevitore (Receiver)**.
    - I primi 5 bit inviati al secondo 1 raggiungono il destinatario solo dopo 5 secondi.
    - Nel frattempo, il mittente continua a inviare nuovi bit ogni secondo, riempiendo progressivamente il canale di trasmissione.
    - Dopo 5 secondi, il collegamento è **pieno** di dati (25 bit in transito), e il ricevitore inizia a ricevere dati in modo continuo.



#### Interpretazione del Bandwidth-Delay Product (BDP)

- Nei primi secondi, il **canale viene riempito** di bit, ma il destinatario non riceve nulla finché non trascorre il tempo di ritardo.
- Dopo 5 secondi, il collegamento ha raggiunto il suo massimo **Bandwidth-Delay Product (25 bit)**: **non possono esserci più di 25 bit in transito contemporaneamente**.
- Una volta che il collegamento è completamente utilizzato, il destinatario inizia a ricevere dati regolarmente a 5 bps.
  
In conclusione l'immagine dimostra che in una connessione con una certa larghezza di banda e un certo ritardo, c'è un limite massimo ai dati che possono essere "in volo" tra il mittente e il destinatario. Questo concetto è fondamentale per ottimizzare le prestazioni di rete, specialmente nelle connessioni ad alta latenza, come quelle satellitari o transoceaniche.
#### Interpretazione pratica:
- ==Se la **larghezza di banda** è elevata ma il **ritardo** è basso (tubo corto), i dati arriveranno rapidamente con una capacità elevata==.
- ==Se il **ritardo** è alto (tubo lungo) ma la **larghezza di banda** è bassa (sezione piccola), i dati impiegheranno più tempo per attraversare la rete e il flusso sarà limitato==.
- In scenari come le reti satellitari, il **ritardo è elevato**, quindi è necessario un **alto Bandwidth-Delay Product** per mantenere buone prestazioni.

In sintesi, questa immagine aiuta a visualizzare come **larghezza di banda e ritardo influenzano la quantità di dati che possono essere in transito contemporaneamente**.

## [[#^dataLink-layer|Livello data link ]] 
Il livello di Data Link è il secondo strato del modello OSI e ==si occupa della connessione logica nodo a nodo, gestendo la trasmissione dei dati in forma di frame tra dispositivi all'interno di una rete==. 
==Questo livello è fondamentale per garantire che i dati vengano trasmessi in modo affidabile e ordinato tra i vari nodi della rete==, che possono includere router, switch e altri dispositivi.

#### Funzioni del Livello di Data Link

1. **Framing**:
    
    - ==I dati provenienti dal livello superiore (Network layer) vengono suddivisi in unità più piccole chiamate frame==. 
    - **Ogni frame contiene informazioni di controllo**:  
	      ==come indirizzi MAC e dati di errore, che facilitano la trasmissione e la ricezione==.
2. **Error Detection**:
    
    - ==Il livello di Data Link è responsabile della rilevazione degli errori nei frame trasmessi==. 
    - Utilizza tecniche come il **Controllo di Ridondanza Ciclomale (CRC)** ==per identificare eventuali errori nei dati ricevuti==. 
      ==Se viene rilevato un errore, il frame può essere ritrasmesso==.
3. **Flow Control**:
    
    - ==Gestisce il flusso di dati tra il mittente e il destinatario per evitare congestioni nella rete==. 
    - **Ciò è particolarmente importante in situazioni in cui il mittente può inviare dati più rapidamente di quanto il destinatario possa elaborare.**
4. **Addressing**:
    
    - ==Utilizza gli indirizzi **MAC (Media Access Control)** per identificare in modo univoco i dispositivi all'interno della rete==. 
    - **Gli indirizzi MAC sono assegnati a ciascun dispositivo di rete** e sono utilizzati: 
	      ==per indirizzare i frame ai destinatari corretti==.

#### Sottolivelli del [[#dataLink-layer Livello data link|Livello di Data Link]]

![[Sub-layers data link.png]]
^imgSublayers-Datalink

Il livello di Data Link è suddiviso in due sottolivelli principali:

1. **[[#LLC Framing|Logical Link Control (LLC)]]**:
    
    - ==Il sottolivello LLC gestisce la comunicazione tra il livello di Data Link e il[[Network, Transport, Session, Presentation, Application Layers#Network layer|livello di rete]]==. 
    - Si occupa di funzioni come: 
	    - ==il controllo degli errori== 
	    - ==il controllo del flusso, garantendo che i frame siano formattati correttamente e trasmessi in modo affidabile==.
	  
	^LLC-List
    
2. **[[#Media access control|Media Access Control (MAC)]]**:
    
    - ==Il sottolivello MAC controlla come i dispositivi accedono al mezzo fisico di trasmissione==. 
    - ==Determina le modalità di accesso alla rete per evitare collisioni==.
    - Utilizza protocolli come:
	    - **[[ISO E OSI Model#^csma-cd|CSMA/CD]]** (Carrier Sense Multiple Access with Collision Detection) per reti cablate 
	    - **[[ISO E OSI Model#^csma-ca|CSMA/CA]]** (Carrier Sense Multiple Access with Collision Avoidance) per reti wireless.
     ^MAC-List
### LLC Framing 
Il processo di framing nel sottolivello [[#^LLC-List|Logical Link Control (LLC)]]: 
- ==è fondamentale per la corretta trasmissione dei dati tra i dispositivi di rete==. 
- Ogni frame è composto da un header, dai dati e da un trailer, e include diverse informazioni chiave.

![[LLC Framing.png]]
^frame-img


[[#^frame-img|Riprendendo l'immagine]] analizziamo la struttura del frame:
#### Struttura del Frame

1. **Preamble (preambolo)**: 
    
    - ==Il preambolo è una serie di bit che prepara il dispositivo ricevente a comprendere i dati in arrivo==. 
    - ==Si trova all'inizio del frame e garantisce che il mittente e il ricevente siano sincronizzati prima dell'inizio del messaggio effettivo==.
2. **Header(intestazione)**:
    
    - **Destination MAC Address**: 
	    - ==L'indirizzo fisico del dispositivo destinatario sulla rete.== 
	    - ==Serve per indirizzare correttamente il frame.==
    - **Source MAC Address**: 
	    - ==L'indirizzo fisico del dispositivo mittente==. 
	    - ==Indica chi ha inviato il frame==.
    - **Length**: 
	    - ==La dimensione del payload di dati nel frame==.
	    - ==indica quanto spazio occupa il contenuto==.
3. **Data**:
    
    - ==Il campo che contiene il payload effettivo che viene trasmesso.== 
    - ==Può includere anche gli header dei livelli superiori==.
4. **Trailer**:
    
    - **CRC Checksum**: 
	    - ==Il trailer contiene un valore di checksum calcolato dai contenuti del frame==. 
	    - **Questo valore è utilizzato per rilevare errori nella trasmissione**; 
		    - ==Se il checksum calcolato al ricevimento non corrisponde a quello trasmesso, indica che il frame è stato corrotto==. 
	    - Il checksum è generato tramite una **funzione hash:**
			- ==produce un valore di dimensione fissa e unica per un dato input==. 
			- Questo valore è unidirezionale: ==il che significa che non è possibile risalire all'input originale a partire dal checksum==.

#### Meccanismi di Controllo del Flusso

Il controllo del flusso è essenziale per garantire che i dati vengano trasmessi in modo efficiente e senza congestioni nella rete. 
Due meccanismi principali utilizzati nel livello di Data Link sono:

1. **Stop-and-Wait**:
    
    - **Descrizione**: 
	    - ==Il mittente trasmette un frame e attende un riconoscimento (ACK) dal ricevente prima di inviare il frame successivo==. 
	     
		 -  ==Questo approccio assicura che ogni frame venga ricevuto e riconosciuto prima di procedere, prevenendo l'overflow dei dati e garantendo una consegna ordinata.==
    - **Vantaggi**: ==Semplice e facile da implementare==.
    - **Svantaggi**: ==Inefficiente per reti ad alta velocità a causa del tempo di attesa tra i frame==.
1. **Sliding Window**:
    
    - **Descrizione**: 
	     -  ==Questo meccanismo consente di inviare più frame prima di richiedere un riconoscimento.== 
	     -  Il mittente può trasmettere un numero specificato di frame, determinato dalla dimensione della "finestra". 
	     -  ==Dopo aver inviato questi frame, il mittente attende gli ACK. Man mano che gli ACK vengono ricevuti, la finestra si sposta in avanti, consentendo al mittente di inviare ulteriori frame.==
    - **Vantaggi**: ==Utilizzo più efficiente delle risorse di rete e migliori prestazioni nelle reti ad alta velocità.==
    - **Svantaggi**: ==Maggiore complessità di implementazione rispetto al metodo Stop-and-Wait.==

#### Media access control 
==Il sottolivello MAC controlla come i dati vengono posizionati e recuperati dal mezzo di rete==.

##### Funzioni: 
• **Indirizzamento**: 
	==Utilizza indirizzi MAC per identificare i dispositivi di invio e ricezione sulla rete.== 
• **Controllo dell'accesso**: 
	==Determina come i dispositivi condividono il mezzo di rete per evitare collisioni (quando due dispositivi tentano di inviare dati simultaneamente)==.

##### Metodi di esempio:

- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**:  ^csma-cd
	 -  ==Utilizzato nelle reti Ethernet per gestire la trasmissione dei dati e rilevare le collisioni.==  
	   
- **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)**:  ^csma-ca
	-   ==Utilizzato nelle reti Wi-Fi per evitare collisioni aspettando un canale libero prima di trasmettere==.  
	  
-  **Delimitazione dei frame**: 
	- ==Definisce l'inizio e la fine di un frame, garantendo che i dati siano interpretati correttamente.==


#### Network Switch
Gli switch di rete sono dispositivi fondamentali in una rete locale (LAN). ==Consentono la comunicazione tra diversi dispositivi all'interno della stessa rete.==

In sostanza Uno switch di rete è un dispositivo che: 
- ==riceve== 
- ==elabora== 
- ==e inoltra i dati a dispositivi specifici all'interno di una rete locale==. 
**Opera al livello di [[#dataLink-layer Livello data link|Data Link]] del modello ISO/OSI.** 

![[Network Switch.png]]

##### Funzionamento base di uno switch

- ==Riceve un frame di dati da un dispositivo connesso==.  
- ==Legge l'indirizzo MAC di destinazione del frame==.  
- ==Cerca l'indirizzo MAC nella sua tabella degli indirizzi MAC per determinare la porta di destinazione==.  
	- ==La tabella degli indirizzi MAC mappa gli indirizzi MAC ai numeri delle porte dello switch==.  
	- ==Viene costruita dinamicamente apprendendo gli indirizzi MAC dai frame che passano attraverso lo switch==.  
- ==Invia il frame alla porta corretta per raggiungere il dispositivo di destinazione==.


