
# Internetwork
==Internetwork o Internet è una una raccolta di diverse reti collegate tramite un gateway==. 
Ogni rete utilizza hardware diverso e, cosa ancora più importante, protocolli diversi per gestire la comunicazione interna.
![[Internetwork.png]]

## Protocolli
La comunicazione tra varie entità all'interno delle reti è gestita da protocolli. 
==Un protocollo di rete è un insieme formale e predefinito di regole che governano le interazioni tra due o più dispositivi elettronici connessi per facilitare la comunicazione.== 
Queste regole riguardano principalmente i componenti software dei dispositivi.

Le prime reti di computer si concentravano principalmente sull'hardware, considerando il software semplicemente come un complemento. Questo approccio è obsoleto. Nei contesti moderni, il software di rete è strutturato in modo complesso e gioca un ruolo centrale nella funzionalità della rete.

### Il ruolo centrale di un software di rete

Il software di rete gioca un ruolo centrale nelle moderne infrastrutture di rete, poiché ==è responsabile della gestione delle funzionalità, della compatibilità e della comunicazione tra diversi componenti hardware.== 
La sua importanza è evidente in vari aspetti:

**Complessità delle Funzionalità**:  
Le reti moderne devono supportare un'ampia gamma di servizi e applicazioni, ==dalla semplice trasmissione dei dati a operazioni di sicurezza complesse, gestione del traffico, ottimizzazione delle prestazioni e integrazione con il cloud.== 
==Queste funzioni richiedono software sofisticato in grado di gestire dinamicamente varie esigenze e configurazioni==.

**Adattabilità e Scalabilità**:  
Le reti odierne devono essere altamente adattabili e scalabili per rispondere rapidamente alle mutevoli esigenze aziendali o dei consumatori. 
==Il software di rete consente questa flessibilità, permettendo aggiornamenti e modifiche da implementare molto più rapidamente e a costi inferiori rispetto ai cambiamenti hardware.== 

**Sicurezza**:  
La sicurezza delle reti moderne si basa fortemente su software avanzato per implementare firewall, sistemi di rilevamento delle intrusioni, crittografia e altre misure di sicurezza essenziali per proteggere i dati e mantenere la rete sicura contro minacce sempre più sofisticate.

==Quindi il software di rete è cruciale non solo per gestire la funzionalità, ma anche per garantire compatibilità e comunicazione tra diversi componenti hardware. Agendo come intermediario, consente a dispositivi diversi, potenzialmente di vari produttori, di lavorare insieme senza problemi.== 
Questa interoperabilità è fondamentale per costruire sistemi di rete flessibili ed efficienti che possano adattarsi a nuove tecnologie e requisiti.

### Gli strati dei livelli
Per semplificare il design, le reti sono strutturate in strati che si basano l'uno sull'altro. 
Le differenze tra le reti possono includere: 
• ==Il numero di strati.== 
==• I nomi degli strati.==
==• Il contenuto di ciascun strato.==
==• La funzionalità di ciascun strato.==
![[Stack of Layers.png|right]] ==Ogni strato serve a fornire servizi specifici agli strati superiori, mentre astrae i dettagli su come tali servizi sono implementati.==









### Layer Protocol
==Il concetto di Layer Protocol è organizzato su livelli diversi, dove ogni livello offre servizi esclusivamente al livello immediatamente superiore.== 
Questi livelli possono variare sia per numero che per funzionalità, ma la loro interazione è fondamentale per garantire una comunicazione efficace tra dispositivi. 
I protocolli governano la comunicazione tra le diverse macchine, stabilendo regole e convenzioni che guidano questo processo. Quando il livello `n` di una macchina comunica con il livello `n` di un'altra macchina, le norme che regolano questa interazione sono conosciute collettivamente come protocollo del livello `n`. In sostanza, un protocollo è un accordo che definisce le procedure di comunicazione tra le parti coinvolte, assicurando che le informazioni vengano scambiate in modo chiaro e coerente.
![[Layer Protcol.png|center|490]]
Osservando l'immagine, si nota che ogni livello comunica direttamente con il livello corrispondente sull'altra macchina (es: livello 5 con livello 5, livello 4 con livello 4, e così via). 
[[#^logicComm|Questa comunicazione tra livelli uguali è logica]]: 
nel senso che ogni livello utilizza un protocollo specifico per scambiarsi dati con il suo equivalente sull'altra macchina. 
Tuttavia, nella pratica, i dati non vengono trasmessi direttamente tra livelli uguali, ma devono passare attraverso tutti i livelli sottostanti: il livello più alto affida i dati a quello inferiore, fino ad arrivare al livello più basso, che si occupa della trasmissione vera e propria. Una volta ricevuti dall'altra macchina, i dati risalgono attraverso i vari livelli fino a raggiungere quello di destinazione. Questo approccio a strati garantisce una comunicazione organizzata e modulare, in cui ogni livello ha un ruolo preciso e si basa sui servizi di quello sottostante


> [!faq] Cosa si intende per "comunicazione logica"?
> Per comunicazione logica si intende un'astrazione: 
> ogni livello "sembra" comunicare direttamente con il suo corrispondente sull'altra macchina, ma in realtà i dati devono attraversare tutti i livelli sottostanti prima di essere trasmessi fisicamente.  ^logicComm
>> [!deep] Distinzione tra comunicazione **logica** e **fisica** 
> > Questa distinzione è un concetto fondamentale nei modelli di rete, come il modello [[ISO E OSI Model#ISO/OSI model|OSI]] o TCP/IP.
> > - **Comunicazione logica (astratta):**
> > ==rappresenta il modo in cui immaginiamo che i dati vengano scambiati tra 2 entità equivalent==i (es: livello 4 con il livello 4). 
> > È definita dai protocolli e dalle regole di comunicazione tra i livelli corrispondenti, ma ==non avviene direttamente.== 
> > - **Comunicazione fisica (concreta/reale):**
> > ==È il trasferimento effettivo dei dati attraverso i mezzi fisici== (cavi, onde radio, fibra ottica, etc).
> > Qui entrano in gioco le schede di rete, i router e altri dispositivi hardware. 
>>> [!example]- In sintesi
>>> Quindi nel modello a strati (es: [[ISO E OSI Model|OSI]]) la comunicazione **logica** avviene tra livelli corrispondenti su macchine diverse, ==ma per raggiungere il livello corrispondente, i dati devono essere incapsulati e trasmessi attraverso i livelli inferiori fino al livello fisico, che si occupa della trasmissione vera e propria.== 
>>> Ergo:
>>> - la comunicazione **fisica:** ==è quella che avviene a livello hardware== 
>>> - la comunicazione **logica:** ==è un'astrazione utile per comprendere e progettare i protocolli di rete.== 




## Comunicazione di rete 
Per spiegare meglio il funzionamento della comunicazione in rete, andiamo ad analizzare questa immagine:
![[Network communication.png|right]]

L'immagine rappresenta un processo di comunicazione tra **Location A** e **Location B**, in cui un messaggio viene elaborato e trasmesso attraverso diversi livelli prima di arrivare al destinatario finale.

- In **Location A**, il mittente (un filosofo) formula il messaggio originale: _"I like rabbits"_.
- Questo messaggio non viene inviato direttamente, ma passa attraverso vari livelli:
    1. **Livello 2:** Un traduttore lo converte in olandese (_"Ik vind konijnen leuk"_).
    2. **Livello 1:** Una segretaria prende il messaggio tradotto e lo invia via fax alla Location B.
- In **Location B**, il messaggio viene ricevuto e il processo si svolge al contrario:
    1. **Livello 1:** La segretaria riceve il fax con il messaggio in olandese.
    2. **Livello 2:** Il traduttore converte il messaggio in francese (_"J'aime bien les lapins"_).
    3. **Livello 3:** Il filosofo di Location B riceve il messaggio finale.

#### Collegamento con il [[ISO E OSI Model#ISO/OSI model|modello OSI]] 

L'immagine può essere interpretata come un'analogia con il **modello OSI** delle reti di comunicazione:

- **Livello 4 ([[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model applicationLayer Application Layer|Applicazione]]):** 
  Il **filosofo** rappresenta l'utente finale che genera e interpreta il messaggio.
- **Livello 3 ([[Network, Transport, Session, Presentation, Application Layers#ISO E OSI Model presentationLayer Presentation Layer|Presentazione]]):** 
  Il **traduttore** si occupa della conversione del messaggio in un formato comprensibile per il destinatario, proprio come il livello di presentazione traduce dati in formati compatibili tra sistemi diversi.
- **Livello 2 ([[ISO E OSI Model#dataLink-layer Livello data link|Data Link]]):**  
La **segretaria** rappresenta il livello di collegamento dati (Data Link), ==perché si occupa di preparare il messaggio per la trasmissione, verificare che sia inviato correttamente e gestire eventuali problemi di trasmissione==. Questo livello garantisce che i dati vengano consegnati in modo affidabile tra due nodi collegati direttamente.
- **Livello 1 ([[ISO E OSI Model#livelloFisico Livello fisico|Fisico]]):** 
 Il **fax** rappresenta il livello fisico, ==poiché si occupa esclusivamente della trasmissione del messaggio tra Location A e Location B senza interpretarne il contenuto.== 
 Questo è analogo alla trasmissione di bit tramite cavi, onde radio o fibre ottiche nelle reti di comunicazione.

#### Collegamento con i concetti di [[#^logicComm|comunicazione logica]] 
Questa immagine rappresenta bene la distinzione tra **comunicazione logica** e **comunicazione fisica**:

- **Comunicazione logica:** 
  ==A livello teorico, il filosofo di Location A parla direttamente con il filosofo di Location B, senza preoccuparsi di come il messaggio venga trasmesso.== 
- **Comunicazione fisica:** 
  ==In realtà, il messaggio deve passare attraverso più livelli, proprio come avviene nelle reti di computer, dove i dati vengono incapsulati, trasmessi e decodificati a ogni livello.==
Quindi la comunicazione è verticale a livello fisico, ma a livello astratto e teorico è parallela. 
Per maggiore chiarezza: 
**Location A:**
- il filosofo della location A, cioè colui che invia il messaggio, non si cura di come il messaggio venga mandato.
- Il traduttore (cioè colui che si trova al livello sottostante al filosofo) una volta che è arrivato il messaggio lo traduce in olandese e lo invia alla segreteria ma non si curerà di come la segreteria preparà o inviarà il messaggio. 
- La segretaria una volta preparato il messaggio l'ho inoltra via fax ma non si preoccupa di come il fax trasmette le informazioni all'altro fax.

**Location B:**
- la segreteria di questa location una volta che gli è arrivato il messaggio, non si cura di come il fax gliel'ha fatto arrivare, lo prepara e lo manda al livello superiore 
- Il traduttore di questa location non si cura di come gli è arrivato il messaggio ma si preoccupa solo di tradurlo nella lingua che il filosofo della sua location comprende
- Il filosofo di questa location una volta che gli è arrivato il messaggio tradotto in francese, non si cura di come il messaggio sia arrivato ma lo legge e lo comprende. 
In conclusione questa immagine riassume efficaciamente il funzionamento della comunicazione in rete:
ogni livello svolge un compito specifico e il messaggio viene elaborato progressivamente prima di arrivare al destinatario. 
**Il filosofo mittente non si preoccupa di come il messaggio viene trasmesso**, esattemante come un'applicazione di rete non si preoccupa del percorso fisico dei dati.
### Network communication
L'interfaccia è quel punto in cui due livelli del protocollo si incontrano, e il livello sottostante può offrire servizi al livello superiore. 
È importante notare che i dati non vengono trasferiti direttamente dal livello `n` di una macchina al livello `n` di un'altra macchina. Invece, il processo di comunicazione avviene in due direzioni:![[Network Communication2.png|center]]
Come possiamo notare da questa immagine la comunicazione varia:
- **Fonte (top-down)**: 
  ==ogni livello passa i dati e le informazioni di controllo al livello immediatamente inferiore, continuando fino a raggiungere il livello più basso.== 
- **Destinazione (bottom-up)**: 
  ==ogni livello riceve i dati e le informazioni di controllo dal livello immediatamente inferiore e li passa al livello superiore, continuando fino a raggiungere il livello più alto.== 

Il modello TCP/IP, sebbene non sia uno standard ufficiale, è diventato uno standard de facto nel campo delle comunicazioni di rete. 
Se produco un dispositivo che non è conforme ai modelli TCP/IP, esso non sarà in grado di comunicare con altri dispositivi collegati sulla rete. 
La conformità a questo modello è essenziale per garantire l'interoperabilità tra diversi sistemi e dispositivi, permettendo loro di scambiare informazioni in modo efficace.

Inoltre, al di sotto del livello 1, il mezzo fisico facilita il trasferimento dei dati dall'**host 1** all'**host 2**. 
Questa architettura a livelli, con interfacce ben definite, è fondamentale per garantire che ogni livello possa svolgere le proprie funzioni specifiche e interagire correttamente con i livelli adiacenti. 
In sintesi, la comunicazione di rete si basa su un sistema strutturato che assicura un funzionamento armonioso e coerente delle reti moderne.
#### Esempio tecnico e pratico 
Se vogliamo fornire un esempio pratico di come questa communicazione tra livelli e tra due differenti host funzioni, dobbiamo guardare questa immagine: ![[Network Communication Technical.png|center]]
In questo caso l'applicazione deve inviare il messaggio **M** alla sua **entità peer** (cioè, lo stesso programma applicativo su un'altra macchina).

1. **Il livello 5:** 
   consegna il messaggio **M** al livello 4.
2. **Il livello 4:** 
   aggiunge un'intestazione **H4** al messaggio. Le intestazioni contengono informazioni di controllo come numero di sequenza, offset dei dati, numero di riconoscimento, dimensione, ecc. Il livello 4 consegna il messaggio **M** al livello 3.
3. **Il livello 3:** 
   divide i dati in unità più piccole (pacchetti) e aggiunge un'intestazione **H3** a ciascun pacchetto. Le intestazioni contengono indirizzi IP di sorgente e destinazione, lunghezza totale, un identificatore unico per il pacchetto, lunghezza dell'intestazione, TTL, ecc. Il livello 3 consegna i pacchetti al livello 2.
4. **Il livello 2:** 
   aggiunge un'intestazione **H2** e un trailer **T2** a ciascun pacchetto ricevuto, chiamato frame. Le intestazioni contengono indirizzi MAC di sorgente e destinazione, lunghezza del payload, ecc. Il trailer è usato per il controllo degli errori di trasmissione. Il livello 2 consegna i pacchetti al livello 1.
5. **Il livello 1:** 
   il livello fisico, trasferisce i dati alla macchina di destinazione.
6. Nella macchina di destinazione, il messaggio risale attraverso ciascun livello, rimuovendo intestazioni e trailer ad ogni passaggio. Il messaggio viene completamente ricostruito e diventa leggibile una volta che raggiunge il livello 5.

### Tipologie di rete offerti 
Connectio Oriented services:
Usiamo come analogia la linea telefonica; fanno la stessa cosa inizialnillazon la conessione che viene mantoeuta fino a che i due dispoitivi semttono di comunicare. 
Questo tipo di servizi sono utilizzati quando l'affidabilita rispetto alla velocità, questi connessioni hanno meccanismi di controllo nell trasferiemto dell'informazione ma ciò li porta ad essere servizi più lenti.
Quijdi qui garantisce l'ordine di invio: il primo pacchetto che parte è il primo ad essere inviato e l'ultimo pacchetto e l'ultima ad arrrviare anche perché quando invio un pacchetto devo riceve confemra, ciò avviene purequando ricevo un pacchetto (Questo tipo di servizio è molto utilizzato dalle banche). 
Ciò che rallenta questi servizi è lo handshaking: cioè è un processo che va a rallentare la connessione perché l'apre la connessione in più bisonga tenere conto dell'invio. 
L'handshaking serve per inizializzare la connessione tra un device A e un device B:
A dice a B che deve inviargli i dati e li invia solo quando B gli invia il messaggio di OK,
L'affidabilità è anche garantita con meccANISMI di controllo dell'erroe come gli ACK: 
un esempio è quello di mandare un pachetto e aspetto la confemra di arrivo, se questo ACK non arrIVA per un toto di tempo devo presumere che quel pachhetto sia perso e devo considerare di inviarlo di nuovo.
Il time to leave:

### Servizi non orientati alla connessione:
QUesti sefvizi non è richiesta una conessione permanente tra idevice che comunicano, imessaggi vengono mandati in rete e prendono un altro percorso, questo tipo di servizio è preferibile quando si vuole la velocità anziché la velocità.
Sono basati su questa connesione i servizi i streaming e sevizi di gaming online. 



