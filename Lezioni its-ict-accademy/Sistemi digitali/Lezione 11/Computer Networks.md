
# Internetwork
Internetwork o Internet è una una raccolta di diverse reti collegate tramite un gateway. 
Ogni rete utilizza hardware diverso e, cosa ancora più importante, protocolli diversi per gestire la comunicazione interna.
![[Internetwork.png]]

## Protocolli
La comunicazione tra varie entità all'interno delle reti è gestita da protocolli. Un protocollo di rete è un insieme formale e predefinito di regole che governano le interazioni tra due o più dispositivi elettronici connessi per facilitare la comunicazione. Queste regole riguardano principalmente i componenti software dei dispositivi.

Le prime reti di computer si concentravano principalmente sull'hardware, considerando il software semplicemente come un complemento. Questo approccio è obsoleto. Nei contesti moderni, il software di rete è strutturato in modo complesso e gioca un ruolo centrale nella funzionalità della rete.

### Il ruolo centrale di un software di rete

Il software di rete gioca un ruolo centrale nelle moderne infrastrutture di rete, poiché è responsabile della gestione delle funzionalità, della compatibilità e della comunicazione tra diversi componenti hardware. La sua importanza è evidente in vari aspetti:

**Complessità delle Funzionalità**:  
Le reti moderne devono supportare un'ampia gamma di servizi e applicazioni, dalla semplice trasmissione dei dati a operazioni di sicurezza complesse, gestione del traffico, ottimizzazione delle prestazioni e integrazione con il cloud. Queste funzioni richiedono software sofisticato in grado di gestire dinamicamente varie esigenze e configurazioni.

**Adattabilità e Scalabilità**:  
Le reti odierne devono essere altamente adattabili e scalabili per rispondere rapidamente alle mutevoli esigenze aziendali o dei consumatori. Il software di rete consente questa flessibilità, permettendo aggiornamenti e modifiche da implementare molto più rapidamente e a costi inferiori rispetto ai cambiamenti hardware.

**Sicurezza**:  
La sicurezza delle reti moderne si basa fortemente su software avanzato per implementare firewall, sistemi di rilevamento delle intrusioni, crittografia e altre misure di sicurezza essenziali per proteggere i dati e mantenere la rete sicura contro minacce sempre più sofisticate.

Quindi il software di rete è cruciale non solo per gestire la funzionalità, ma anche per garantire compatibilità e comunicazione tra diversi componenti hardware. Agendo come intermediario, consente a dispositivi diversi, potenzialmente di vari produttori, di lavorare insieme senza problemi. Questa interoperabilità è fondamentale per costruire sistemi di rete flessibili ed efficienti che possano adattarsi a nuove tecnologie e requisiti.

### Gli strati dei livelli
Per semplificare il design, le reti sono strutturate in strati che si basano l'uno sull'altro. Le differenze tra le reti possono includere: 
• Il numero di strati. 
• I nomi degli strati.
• Il contenuto di ciascun strato.
• La funzionalità di ciascun strato.
![[Stack of Layers.png|right]] Ogni strato serve a fornire servizi specifici agli strati superiori, mentre astrae i dettagli su come tali servizi sono implementati.









Archittetura di rete
é organizzata su livelli diversi dove ogni livello offre servizi solo al livello immediatamente superiore. Possono variare per numero di livello e le funzionalità che offrono.
I protocolli governao la comunicazione tra dispositivi quindi dobbiamo avere più livelli.
![[Layer Protcol.png]]
Seguendo l'immagine possiamo vedere che il livello 5 comunica con l'altro livello 5 e cosi via,
I protocolli sono regole formali e sono importani quando c'è una comunicazione tra più parti. 


Sia Location A che Location B 
La comunicazione è verticale ma a livello astratto e teorico è parallela. 
In realta la persona che si trova al livello 3 a mandato il messaggio al filosofo al suo livello sulla location b ma non gli importa cosa succede ai livelli sotto.

### Network communication


Interfaccia è quel punto dove i due livelli si incontrano e il livello sooto puo offrire servizi al livello sopra 

Il modello TCCP non è uno standard ufficiale ma lo è diventato de facto.
Se i o produco un dispositivio ma non è confemro ai modelli TCHP il mio dispoitvio non potra comunicare con altri dispositivi in rete 

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



