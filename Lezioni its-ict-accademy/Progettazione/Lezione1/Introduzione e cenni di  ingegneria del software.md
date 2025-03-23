In questo corso ci allontaniamo dall'approccio "artigianale" dell'informatica, dove si prende un problema e si scrive direttamente il codice. Qui entriamo nel mondo dei sistemi complessi, dove la progettazione è fondamentale. **Non scriveremo codice**, ma ci concentreremo su come progettare sistemi software robusti e scalabili, indipendentemente dalla tecnologia utilizzata.
Quindi è importanti capire i dati di interesse e come sono correlati tra loro, non esiste una via unica, l'importante che le scelte fatte lungo il progetto siano ben ragionate.
Quindi impareremo a ragionare logicamente e a capire le conseguenza delle nostre azioni. 

## Cosa impareremo?
- **Progettare applicazioni software reali e di dimensioni non banali**: 
  non è possibile definire direttamente il codice senza prima aver compreso a fondo i dati e le loro interrelazioni.
    
- **Ragionare logicamente**: 
  non esiste una soluzione unica, ma bisogna fare scelte ragionate e valutare le alternative.
    
- **Scomporre problemi complessi in sotto-problemi**: 
  il metodo è generale e va adattato intelligentemente al problema specifico.

### Esempio di applicazione
Analizziamo due esempi di applicazione:
1. **Applicazione per la gestione dei contatti:**
Ci viene richiesto di progettare una app che permetta di mantenere informazioni su un insieme di contatti telefonici(telefonici e email). 

- **Requisiti**:
    - Ogni contatto deve avere: nome, cognome, numeri di telefono (casa, ufficio, mobile), indirizzo email.
        
    - I contatti possono appartenere a gruppi.
        
    - L'applicazione deve permettere di aggiungere, modificare, cancellare contatti, assegnarli/rimuoverli da gruppi e ricercarli per nome/cognome.
        
- **Commento**: Questo è un problema semplice, quasi banale, che potremmo risolvere con un programma Python. È come costruire una capanna sull'albero: tutti possono farlo.

Mentre invece nel secondo esempio:
2. **Sistema di gestione per una banca**:
Si vuole sviluppare un sistema che permetta ad una banca di gestire i conti correnti dei clienti, i loro
investimenti, oltre che la propria rete di promotori finanziari

• Il sistema deve tenere traccia di tutti gli acquisti e vendite di azioni, obbligazioni, etc. effettuati dai clienti,
e deve poter calcolare in tempo reale la valorizzazione corrente del loro portafoglio
• Inoltre, l’applicazione deve assistere i promotori finanziari nella scelta degli strumenti finanziari più
adeguati da proporre ai clienti, e deve permettere ai responsabili di agenzia di controllare la
professionalità dei promotori.
Impossibile scrivere direttamente lo schema relazionale e il programma per l’applicazione!
- **Requisiti**:
    
    - Gestione dei conti correnti, investimenti e rete di promotori finanziari.
        
    - Tracciamento di acquisti/vendite di azioni, obbligazioni, etc.
        
    - Calcolo in tempo reale della valorizzazione del portafoglio.
        
    - Assistenza ai promotori nella scelta degli strumenti finanziari.
        
    - Controllo della professionalità dei promotori da parte dei responsabili di agenzia.
**Commento**: Qui la complessità è molto più alta. Non possiamo scrivere direttamente il codice senza prima aver capito a fondo il problema. Ad esempio, cosa è un conto corrente? Come si definisce la valutazione di un portafoglio? Queste domande richiedono tempo e analisi.

## Tempi di Progettazione
Mettiamo che per progettare questo software ci si metta un anno e mezzo:
- **Capire il problema**: 6 mesi (33% del tempo totale).

- **Progettazione**: 9 mesi (50% del tempo).

- **Realizzazione del codice**: 3 mesi (solo il 17% del tempo).

- **Test e verifica**: ulteriore tempo necessario.

Difatti l'obiettivo del corso è imparare a realizzare progetti complessi come applicazioni software da distribuire nel cloud.

### Chi partecipare a un progetto software? 
Per capire com'è fatto un progetto dobbiamo capire chi sono le figure che partecipano al progetto:
- Committente: 
  è l'azienda che commissiona lo sviluppo del sistema
-  Esperti del dominio: 
  persone che conoscono a fondo il settore in cui il software verrà utilizzato
-  Analisti: 
  team di progettazione, si occupano di raccogliere e analizzare i requisiti.
-  Progettisti: 
  definiscono l'architettura e il design del sistema.
-  Programmatori: 
  le aziende che si occupano di sviluppare il software
-  Utenti finali: 
  gli utenti che utilizzano il sistema
-  Manutentori: 
  le azienda che si occupano di mantenere il software( aggiornarlo aggiustare i bug, etc.) e di aggiornarlo e corregerrerlo dopo la sua messa in esercizio.  
  Non sempre i manutentori sono sempre i programmatori stessi. 
I programmatori lavorano sul progetto e documentano il progetto, di conseguenza  i manutentori fanno riferimento al progetto documentato.
Detto questo per dare un esempio concreto:

Il Comune di XYZ intende automatizzare la gestione delle informazioni relative alle contravvenzioni
elevate sul suo territorio
• In particolare, intende dotare ogni vigile di una app per smartphone che gli consenta di
comunicare al sistema informatico il veicolo a cui è stata comminata la contravvenzione, il luogo in
cui è stata elevata e la natura dell’infrazione
• Il sistema informatico provvederà a notificare, tramite posta ordinaria, la contravvenzione al
cittadino interessato.
• Il Comune bandisce opportune gare per la progettazione, realizzazione e manutenzione del
sistema, che vengono vinte, rispettivamente, dalle ditte ITSolutions s.p.a., Develop s.r.l. e Ops s.r.l.
Quali sono gli attori coinvolti in questa applicazione software?
- **Committente**: Comune di XYZ.
    
- **Analisti e Progettisti**: ITSolutions s.p.a.
    
- **Programmatori**: Develop s.r.l.
    
- **Manutentori**: Ops s.r.l.
- **Esperti del dominio:** 
  Dal punto di vista legale qualcuno che ci spieghi qual è la procedura corretta per le contravvenzioni, quindi ci servono esperti del settore ergo:
  il codice della strada→ Il comune
Infatti, talvolta, gli esperti di dominio possono combaciare sia con i committenti che con gli esperti ma possono anche essere gli utenti finali. 
Spesso nei software complessi gli esperti vengono scelti fuori dalla azienda.
### Il ciclo di vita del software
Il ciclo di vita del software è composto da diverse fasi, che possono essere viste come un modello a cascata o iterativo (a spirale). 
Ecco le principali fasi:
1. **Studio di Fattibilità**:
    
    - Comprendere i requisiti di alto livello.
        
    - Valutare costi e benefici.
        
    - Pianificare attività e risorse.
        
    - Individuare l'ambiente di programmazione (hardware/software).
        
2. **Raccolta dei Requisiti**:
    
    - Raccolta dei requisiti presso i diversi attori.
        
    - Stesura e sintesi iniziali.
        
    - Raffinamento dei requisiti: eliminare ambiguità e imprecisioni.
        
3. **Analisi Concettuale dei Requisiti**:
    
    - **Obiettivo**: produrre lo schema concettuale dell'applicazione, che definisca **cosa** l’applicazione dovrà realizzare, indipendentemente dal **come**.
        
    - Lo schema concettuale modella i dati di interesse, le loro interrelazioni e i servizi computazionali che l'applicazione dovrà offrire.
        
4. **Progetto (Design) dell'Applicazione**:
    
    - Specificare **come** l’applicazione dovrà realizzare le sue funzioni.
        
    - Scegliere il mix tecnologico ottimale.
        
    - Definire l'architettura e le strutture di rappresentazione dei dati.
        
5. **Realizzazione (Implementazione)**:
    
    - Scrivere il codice.
        
    - Scrivere la documentazione.
        
6. **Integrazione e Verifica**:
    
    - Integrare le diverse componenti dell'applicazione.
        
    - Verificare che l'applicazione svolga correttamente i suoi compiti.
        
7. **Messa in Esercizio**:
    
    - L'applicazione viene messa in funzione (fase critica).
        
8. **Manutenzione**:
    
    - Monitorare l'applicazione durante l'esercizio.
        
    - Produrre correzioni e aggiornamenti quando necessario.

> [!info] ==Al termine di ogni fase, se necessario, si può tornare indietro.==
> 

Questo visto finora si chiama **modello a cascata (waterfall model):**
ogni fase inizia quando termina la precedente. 
È un modello didattico, poco utilizzato nella pratica.

Nel mondo reale questa cosa non si può fare veramente, poiché [[#Tempi di Progettazione|i tempi di progettazione]] sono lunghi e complicati quindi  si preferisce usare il **modello spirale o iterativo:**
==si sviluppano versioni sempre più complete del software, con cicli di feedback e miglioramento.==
![[il modello iterativo.pdf.png]]

### Unified Modeling Language (UML)
==UML è un linguaggio di modellazione utilizzato per rappresentare visivamente un sistema software.== 
In totale esistono 14 diagrammi diversi per modellare l'applicazione sotto prospettive diverse, in questo corso se ne utilizzano alcuni.
 I principali tipi di diagramma sono:
• **Diagrammi strutturali:**
	• Diagramma delle classi e degli oggetti (class and object diagram)(questo si )
• **Diagrammi comportamentali:**
	• Diagramma degli use case (use case diagram),
	• Diagramma degli stati e delle transizioni (state/transition diagram),
	• Interaction (Sequence e Collaboration diagram),
	• Activity diagram
• **Diagrammi architetturali:**
	• Component diagram
	• Deployment diagram

La metodologia che illustriamo in questo modulo si basa su UML, in particolare, ci concentriamo solo sugli aspetti base e sui diagrammi più importanti.
Nell’analisi concettuale useremo solo i seguenti diagrammi (e di questi diagrammi useremo solo le
caratteristiche più importanti):
- Diagrammi strutturali:
	- Diagramma delle classi e degli oggetti (class and object diagram)
- Diagrammi comportamentali:
	- Diagramma degli use case (use case diagram),
	- Diagramma degli stati e delle transizioni (state/transition diagram)
UML ci aiuterà a modellare l'applicazione in modo chiaro e preciso, ma nel corso ci concentreremo solo sugli aspetti più importanti e utili per la progettazione concettuale.

In sintesi, questo corso ci prepara a gestire progetti software complessi, partendo dalla comprensione del problema fino alla progettazione e alla realizzazione. Impareremo a ragionare in modo strutturato, a scomporre problemi complessi e a utilizzare strumenti come UML per modellare le nostre soluzioni.