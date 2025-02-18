
# Internetwork
Internetwork o Internet è una collezione di networks differenti connessi attraverso





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



