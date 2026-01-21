
# Introduzione
Dopo aver analizzato **dove** viene eseguito il cloud ([[Lezione 3 - Modelli di deployment del cloud#Cloud Pubblico|pubblico]], [[Lezione 3 - Modelli di deployment del cloud#Cloud Privato|privato]], [[Lezione 3 - Modelli di deployment del cloud#Cloud Ibrido|ibrido]], [[Lezione 3 - Modelli di deployment del cloud#Multi-Cloud|multi-cloud]]) è necessario introdurre un secondo asse fondamentale: **chi è responsabile di cosa**.

I **modelli di deployment** descrivono: 
- _la posizione dell’infrastruttura_ e _come viene distribuita_,  
mentre i **modelli di servizio** ([[#IaaS – Infrastructure as a Service (Infrastruttura come Servizio)|IaaS]], [[#PaaS – Platform as a Service (Piattaforma come Servizio)|PaaS]], [[#SaaS – Software as a Service (Software come Servizio)|SaaS]]) descrivono: 
- **come vengono suddivise le responsabilità operative** tra:

- il **cloud provider** (AWS, Azure, Google Cloud);
    
- l’**azienda o lo sviluppatore** che utilizza il servizio.
    

Questa suddivisione è spesso rappresentata come una **piramide della responsabilità**:  
- ==scendendo verso la base aumenta il controllo, ma aumentano anche le attività di gestione;==  
- ==salendo verso l’alto diminuisce il carico tecnico, ma anche la libertà di configurazione.==

## Piramide delle responsabilità 
Nel cloud non esiste una soluzione unica valida per tutti:  
- ogni progetto può scegliere **quanto lavoro tecnico svolgere in prima persona** e **quanto delegare al provider**.

Un’analogia efficace è quella della **pizza**:

- **[[#IaaS – Infrastructure as a Service (Infrastruttura come Servizio)|IaaS (Infrastructure as a Service)]]**  
    - ==Prepari la pizza partendo dagli ingredienti grezzi (farina, lievito, pomodoro, mozzarella).==  
    - ==Hai il massimo controllo sul risultato finale, ma devi occuparti di ogni singolo passaggio.==
    
- **[[#PaaS – Platform as a Service (Piattaforma come Servizio)|PaaS (Platform as a Service)]]**  
    - ==Parti da un impasto già pronto e aggiungi solo i condimenti.==  
    - ==La base è gestita da altri, tu ti concentri sulla personalizzazione.==
    
- **[[#SaaS – Software as a Service (Software come Servizio)|SaaS (Software as a Service)]]**  
    - ==Ordini la pizza già pronta a domicilio.==  
    - ==Non ti occupi di nulla: la usi e basta.==
    

Allo stesso modo:

- **più sei in basso nella piramide (IaaS)** →  
    - ==più **controllo**, **flessibilità** e **responsabilità** hai;==
    
- **più sali verso PaaS e SaaS** →  
    - più il provider gestisce infrastruttura, sistema operativo, aggiornamenti e sicurezza,  permettendoti di concentrarti solo sul tuo obiettivo principale:
    
	    - **sviluppare codice,**
        
	    - **gestire un servizio,**
        
	    - **oppure semplicemente usare un’applicazione.**
        

La piramide della responsabilità aiuta quindi a capire **non solo cosa offre il cloud**, ma soprattutto ==**come cambia il ruolo dello sviluppatore e dell’azienda** a seconda del modello scelto.== 


## IaaS – Infrastructure as a Service (Infrastruttura come Servizio)

Nel modello **IaaS:**
- ==il cloud provider fornisce **esclusivamente i componenti fondamentali dell’infrastruttura IT**,== 
- ==mentre **tutta la gestione software ricade interamente sull’utente**.==

In concreto, il provider mette a disposizione:

- ==**risorse di calcolo** sotto forma di computer virtuali;==
    
- ==**spazio di archiviazione** per dati e applicazioni;==
    
- ==**rete e meccanismi di sicurezza di base**.==
    

Tutto ciò che si trova _al di sopra_ di questi elementi — come il **sistema operativo**, le **applicazioni**, le **configurazioni**, gli **aggiornamenti** e la **manutenzione** — **deve essere installato, configurato e gestito direttamente dall’utente**.

> [!example] **Analogia: l’appartamento vuoto**  
> Il modello IaaS può essere paragonato all’affitto di **un appartamento completamente vuoto**:
> 
> - il provider fornisce la struttura dell’immobile (mura, pavimenti e impianti);
>     
> - l’utente deve occuparsi dell’arredamento, della gestione quotidiana e della manutenzione.
>     
> 
> L’ambiente è disponibile, ma **ogni scelta operativa e ogni responsabilità restano in capo all’utente**.
### Cosa fornisce il cloud provider

Nel modello **IaaS** (ad esempio su AWS), il cloud provider si occupa **esclusivamente della fornitura e della gestione fisica dell’infrastruttura**, mettendo a disposizione dell’utente i seguenti componenti fondamentali:

- **Server virtuali**
    
    - ==[[Docker#Le macchine virtuali (VM)|Macchine virtuali]] astratte, sulle quali l’utente può installare liberamente qualsiasi sistema operativo e software.==
        
- **Storage (spazio di archiviazione virtuale)**
    
    - ==Dischi virtuali collegabili ai server, utilizzati per ospitare sistemi operativi, applicazioni e dati persistenti.==
        
- **Rete virtuale**
    
    - **Infrastruttura di rete software-defined**, che comprende:
        
        - ==[[Network, Transport, Session, Presentation, Application Layers#La Maschera di Rete (Subnet Mask Structure)|subnet]], [[Network, Transport, Session, Presentation, Application Layers#Logical Addressing - IP Address|indirizzi IP]], [[Network, Transport, Session, Presentation, Application Layers#routingProc Routing Process|routing]] e collegamenti logici tra le risorse.==
            
- **Firewall virtuali**
    
    - ==Meccanismi di filtraggio e controllo del traffico di rete in ingresso e in uscita, configurabili dall’utente.==
        

Questi elementi costituiscono l’**infrastruttura di base** del modello IaaS:

- ==l’hardware fisico è interamente gestito dal provider, mentre il controllo logico e la configurazione operativa sono affidati all’utente.==
#### Cosa deve gestire l’utente

Nel modello **IaaS:**
- ==la maggior parte delle responsabilità operative è **a carico dell’utente**, che assume un ruolo attivo nella gestione dell’intero stack software.== 
In particolare, l’utente deve occuparsi di:

- **installazione e configurazione del sistema operativo**
    
    - ==[[Linux|Linux]], Windows o altre distribuzioni, inclusa la configurazione iniziale.==
        
- **installazione, configurazione e manutenzione dei software applicativi**
    
    - ==Web server, database, servizi di backend e componenti di supporto.==
        
- **configurazione della rete e della sicurezza a livello software**
    
    - ==Regole di accesso, porte, utenti, permessi e servizi esposti.==
        
- **gestione degli aggiornamenti e delle patch**
    
    - ==Sia del sistema operativo sia delle applicazioni installate.==
        
- **protezione del sistema e delle applicazioni**
    
    - ==Hardening del sistema, gestione delle credenziali e mitigazione delle vulnerabilità.==
        
- **definizione ed esecuzione di backup e piani di disaster recovery**
    
    - ==Strategie di salvataggio, ripristino e continuità operativa.==
        

> [!ticket] **Concetto chiave**  
> Con IaaS ottieni **massima libertà e controllo sull’ambiente**, ma ti assumi anche **l’intera responsabilità della gestione operativa e della sicurezza software**.
#### Esempi di servizi IaaS su AWS

##### EC2 – Elastic Compute Cloud

**EC2** rappresenta il servizio centrale del modello **IaaS** su AWS e ==fornisce **potenza di calcolo virtuale on-demand**.==

Il nome chiarisce bene il concetto:

- **[[Lezione 1 - Introduzione al Cloud Computing#1. Compute – Potenza di Calcolo Virtuale|Compute]]**
    
    - ==risorse di calcolo sotto forma di [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] e [[Il modello di Von Neumann#RAM|RAM]];==
        
- **Elastic**
    
    - ==le risorse possono essere aumentate o ridotte in base alle esigenze, anche dinamicamente;==
        
- **Cloud**
    
    - ==le macchine sono virtuali e risiedono nei data center del provider, non su hardware fisico dell’utente.==
        

Con EC2, l’utente può:
- **creare**, 
- **configurare,** 
- **avviare e spegnere server virtuali** 
Tutto questo in pochi minuti, scegliendo dimensioni, sistema operativo e configurazioni.

**Esempio operativo**:

> “Crea una macchina virtuale con 4 vCPU e 16 GB di RAM”.

##### VPC – Virtual Private Cloud

Il servizio **VPC** consente di: 
- ==definire una **rete privata virtuale** all’interno del cloud AWS, completamente isolata e sotto il controllo dell’utente.==

Il significato del nome evidenzia le sue caratteristiche principali:

- **Virtual**
    
    - ==la rete è definita a livello software;==
        
- **Private**
    
    - ==è isolata dalle reti degli altri clienti AWS;==
        
- **Cloud**
    
    - ==è ospitata e gestita nell’infrastruttura del cloud provider.==
        

All’interno di una VPC è possibile configurare **[[Network, Transport, Session, Presentation, Application Layers#La Maschera di Rete (Subnet Mask Structure)|subnet]], [[Network, Transport, Session, Presentation, Application Layers#Logical Addressing - IP Address|indirizzi IP]], [[Network, Transport, Session, Presentation, Application Layers#routingProc Routing Process|routing]] e regole di accesso**, creando un’architettura di rete simile a quella di un data center tradizionale.

**Esempio**:

> ==“Crea una rete privata in cui solo i miei server possono comunicare tra loro in modo sicuro”.==



##### EBS – Elastic Block Storage

**EBS** fornisce ==**storage a blocchi persistente** da collegare alle istanze EC2.==

In pratica, EBS funziona come:

- ==un **hard disk virtuale** collegato a una macchina virtuale;==
    
- ==uno spazio di archiviazione ridimensionabile;==
    
- ==un supporto per dati persistenti, anche in caso di riavvio o sostituzione della macchina.==
    

EBS è tipicamente utilizzato per:

- ==sistemi operativi;==
    
- ==database;==
    
- ==applicazioni che richiedono storage affidabile e continuo.==


> [!done]  **Vantaggi del modello IaaS**
>
>Il modello IaaS è ideale quando serve **massima libertà tecnica**.
>
>- **Controllo totale**  
> 	 - ==Possibilità di installare e configurare qualsiasi software.==
 >   
>- **Flessibilità massima**  
>	- ==Nessun vincolo su database, linguaggi o architetture.==
>    
>- **Conveniente per profili esperti**  
>	- ==Se il team ha competenze sistemistiche, si paga solo l’infrastruttura base.==


> [!FAILURE] **Svantaggi del modello IaaS**
>
>Il prezzo del controllo è la complessità.
>
>- **Richiede competenze tecniche avanzate**  
>	- Sistemi operativi, sicurezza, networking, patching.
>    
>- **Carico operativo elevato**  
>	- Tutta la manutenzione è a carico dell’utente.
>    
>- **Tempi di configurazione più lunghi**  
>	- Preparare un ambiente completo può richiedere giorni o settimane.

## PaaS – Platform as a Service (Piattaforma come Servizio)

Nel modello **PaaS**, il cloud provider va oltre la semplice fornitura dell’infrastruttura di base e ==offre **una piattaforma applicativa completa, già configurata e pronta all’uso**.==

In pratica:

- **l’infrastruttura fisica e virtuale è interamente gestita dal provider**;
    
- **il sistema operativo è già installato, configurato e mantenuto**;
    
- **i principali servizi di supporto** — come database, rete, scalabilità e backup — **sono integrati e automatizzati**;
    
- **lo sviluppatore lavora quasi esclusivamente sul codice dell’applicazione** e sulla logica di business.
    

==Il PaaS nasce per **astrarre la complessità operativa**, ridurre il carico di gestione sistemistica e consentire ai team di concentrarsi sullo sviluppo funzionale e sull’innovazione.==

> [!example] **Analogia: l’appartamento ammobiliato**  
Il modello PaaS è paragonabile a **un appartamento già arredato e funzionante**:
>
>- struttura, impianti ed elettrodomestici sono già presenti e operativi;
   > 
>- all’inquilino resta solo da portare i propri effetti personali.
  >  
>
>Allo stesso modo, nel PaaS **l’ambiente applicativo è già pronto**: 
>- ==lo sviluppatore **carica il codice e l’applicazione può essere eseguita immediatamente**, senza occuparsi dell’infrastruttura sottostante.==

### Cosa fornisce il cloud provider

Nel modello **PaaS** (ad esempio su AWS), il cloud provider si fa carico ==**dell’intero strato infrastrutturale e sistemistico**, offrendo allo sviluppatore un ambiente già pronto per l’esecuzione delle applicazioni.==

In particolare, il provider fornisce:

- **Server virtuali preconfigurati**
    
    - ==pronti all’uso, senza necessità di provisioning manuale;==
        
- **Sistema operativo già installato e mantenuto**
    
    - ==aggiornamenti, patch di sicurezza e configurazioni sono gestiti automaticamente;==
        
- **Database gestiti**
    
    - ==già operativi, con alta disponibilità, backup e manutenzione inclusi;==
        
- **Aggiornamenti automatici della piattaforma**
    
    - ==sia a livello di sistema che di runtime;==
        
- **Backup automatici e ripristino**
    
    - ==senza interventi manuali da parte dell’utente;==
        
- **Scalabilità automatica**
    
    - ==le risorse aumentano o diminuiscono in base al carico applicativo;==
        
- **Monitoraggio e gestione dell’infrastruttura**
    
    - ==la piattaforma controlla stato, performance e affidabilità del sistema.==
        

==In questo modello, **tutta la complessità sistemistica viene assorbita dalla piattaforma**, liberando lo sviluppatore dalla gestione dell’infrastruttura e consentendogli di concentrarsi esclusivamente sull’applicazione e sul suo comportamento.==


#### Cosa deve fare l’utente

Nel modello **PaaS**, il ruolo dell’utente è **fortemente semplificato** rispetto a IaaS e si concentra quasi esclusivamente sull’aspetto applicativo.

In particolare, l’utente deve:

- **caricare il codice dell’applicazione**
    
    - ==ovvero il software che realizza le funzionalità richieste;==
        
- **configurare alcune impostazioni di base**
    
    - ==come variabili d’ambiente, versioni del runtime, parametri di scalabilità o risorse minime;==
        
- **sviluppare e mantenere la logica applicativa**
    
    - ==cioè le regole di business, i flussi applicativi e il comportamento dell’applicazione.==
        

Tutte le attività infrastrutturali e sistemistiche — come **provisioning dei server, gestione del sistema operativo, patch di sicurezza, backup e manutenzione di base** — **sono interamente a carico del cloud provider**.

> [!ticket] **Concetto chiave**  
> ==Nel modello PaaS l’utente **accetta un livello di controllo inferiore** sull’ambiente sottostante in cambio di **maggiore velocità di sviluppo, semplicità operativa e riduzione del carico di gestione**.==

AWS mette a disposizione diversi servizi che rientrano nel modello **PaaS**, ciascuno progettato per **ridurre il carico operativo** e **accelerare il deployment** delle applicazioni.

#### Esempi di servizi PaaS su AWS
##### Elastic Beanstalk

**Elastic Beanstalk** ==è un servizio PaaS pensato per il **deployment rapido di applicazioni web**, senza la necessità di gestire direttamente l’infrastruttura.==

Il nome richiama due concetti chiave:

- **Elastic**
    
    - ==la piattaforma adatta automaticamente le risorse in base al carico;==
        
- **Beanstalk**
    
    - ==metafora della crescita automatica dell’applicazione.==
        

**Funzionamento**:

- ==l’utente carica il codice dell’applicazione;==
    
- AWS si occupa automaticamente di:
    
    - ==creare i server;==
        
    - ==configurare la rete;==
        
    - ==impostare il bilanciamento del carico;==
        
    - ==gestire lo scaling.==
        

**Esempio pratico**:

> “Carico il mio sito WordPress e, in pochi minuti, l’applicazione è online e pronta a gestire il traffico”.



##### RDS – Relational Database Service

==**RDS** è un servizio PaaS che fornisce **database relazionali completamente gestiti**.==

Supporta i principali DBMS:

- MySQL;
    
- PostgreSQL;
    
- MariaDB;
    
- Oracle.
    

Il provider si occupa automaticamente di tutte le attività operative più complesse, tra cui:

- ==backup automatici;==
    
- ==aggiornamenti e patch;==
    
- ==replica dei dati;==
    
- ==alta disponibilità e fault tolerance.==
    

**Esempio pratico**:

> “Creo un database MySQL con pochi click e, in circa 10 minuti, è operativo senza dover installare o configurare nulla”.

##### AWS Lambda _(PaaS / Serverless)_

**AWS Lambda** rappresenta una forma evoluta di PaaS, spesso indicata come **serverless:** 
- ==perché elimina completamente la gestione dei server.==

Le caratteristiche principali sono:

- ==esecuzione di **solo codice**, senza preoccuparsi dell’infrastruttura;==
    
- ==attivazione **solo quando necessario** (event-driven);==
    
- ==pagamento basato **esclusivamente sul tempo di esecuzione**.==
    

In questo modello:

- ==non esistono server da configurare;==
    
- ==la scalabilità è automatica;==
    
- ==l’utente si concentra unicamente sulla funzione da eseguire.==
    

**Esempio pratico**:

> “Ogni volta che un utente carica una foto, una funzione Lambda ridimensiona automaticamente l’immagine”.

> [!done] **Vantaggi del modello PaaS**
> 
> Il PaaS è ideale per **sviluppo rapido e produttività**.
> 
> - **Velocità elevata**
>     
>     - ==Dall’idea a un’app funzionante in ore.==
>         
> - **Minori competenze richieste**
>     
>     - ==Non serve essere esperti di sistemi.==
>         
> - **Manutenzione automatica**
>     
>     - ==Aggiornamenti, backup e sicurezza di base sono gestiti dal provider.==
>         
> - **Risparmio di tempo operativo**
>     
>     - ==Il team si concentra solo sul codice.==
>         

>[!failure] **Svantaggi del modello PaaS**
>
>La semplificazione comporta alcuni compromessi.
>
>- **Minore controllo**
 >   
>	- ==Configurazioni limitate rispetto a [[#IaaS – Infrastructure as a Service (Infrastruttura come Servizio)|IaaS]].==
  >      
>- **Costo potenzialmente più alto**
  >  
  >	- ==Si paga la comodità (spesso 20–30% in più rispetto a IaaS).==
  >      
>- **Vendor lock-in**
  >  
>	- L==’uso di servizi specifici del provider rende più complessa la migrazione.==


## SaaS – Software as a Service (Software come Servizio)

Nel modello **SaaS**, il cloud raggiunge il **massimo livello di astrazione**:

- ==il provider fornisce **un’applicazione completa e pronta all’uso**, accessibile direttamente tramite browser.==
    

L’utente **non installa nulla**, **non configura nulla** e **non gestisce alcuna infrastruttura**.  
È sufficiente aprire il sito del servizio, autenticarsi e iniziare a lavorare.

> [!example] **Analogia: il ristorante**  
> Il SaaS è paragonabile ad andare **al ristorante**:
> 
> - non cucini;
>     
> - non lavi i piatti;
>     
> - non pensi agli ingredienti.
>     
> 
> Ti siedi e utilizzi il servizio già pronto.  
> ==Allo stesso modo, nel SaaS **usi il software senza occuparti di come funziona dietro le quinte**.==

### Cosa fornisce il provider

Nel modello SaaS, il provider gestisce **l’intera pila tecnologica**:

- ==l’applicazione software;==
    
- ==i server e l’infrastruttura;==
    
- ==i database;==
    
- ==la sicurezza;==
    
- ==i backup;==
    
- ==gli aggiornamenti e la manutenzione.==
    

Dal punto di vista dell’utente, l’unico requisito è:

- un **account** (username e password);
    
- una **connessione Internet**.

#### Cosa deve fare l’utente

Il ruolo dell’utente nel SaaS è ridotto al minimo:

- creare un account;
    
- accedere al servizio;
    
- utilizzare l’applicazione.
    

Tutta la complessità tecnica è **completamente nascosta**.

> [!ticket] **Concetto chiave**  
> ==Con SaaS **rinunci totalmente al controllo tecnico** in cambio di **massima semplicità e immediatezza**.==

#### Esempi comuni di SaaS (non legati ad AWS)

Molti dei servizi digitali più usati quotidianamente sono esempi di SaaS:

- **Gmail**
    
    - ==servizio di posta elettronica pronto all’uso;==
        
    - ==nessuna installazione o configurazione server.==
        
- **Google Drive**
    
    - ==spazio di archiviazione online;==
        
    - ==i file sono accessibili ovunque senza sapere dove sono fisicamente salvati.==
        
- **Netflix**
    
    - ==servizio di streaming video;==
        
    - ==l’utente guarda contenuti senza preoccuparsi dell’infrastruttura.==
        
- **Salesforce**
    
    - ==software CRM (Customer Relationship Management);==
        
    - ==utilizzato dalle aziende per gestire clienti e vendite.==
        
- **Dropbox**
    
    - ==backup e sincronizzazione dei file;==
        
    - ==un file caricato è subito disponibile su tutti i dispositivi.==
##### Servizi AWS classificabili come SaaS

AWS è focalizzata principalmente su **IaaS e PaaS**, ma offre anche alcuni servizi SaaS:

- **Amazon Chime**
    
    - ==piattaforma di videoconferenze aziendali (simile a Zoom).==
        
- **Amazon WorkMail**
    
    - ==servizio di posta elettronica aziendale gestita.==
        
- **Amazon WorkDocs**
    
    - ==piattaforma per la condivisione e gestione dei documenti.==


> [!done]  Vantaggi del modello SaaS
>
>Il SaaS è la scelta più semplice dal punto di vista dell’utente:
>
>- **Nessuna competenza tecnica richiesta**
>    
 >	- ==si usa come un normale sito web.==
>      
>- **Costi prevedibili**
>    
> 	- ==di solito un abbonamento mensile per utente.==
>
>- **Aggiornamenti automatici**
>    
>	- ==nuove funzionalità disponibili senza interventi manuali.==
>
>- **Accessibilità totale**
>   
 >	- ==utilizzabile da qualsiasi dispositivo con browser.==
>  
>- **Nessuna installazione locale**
>    
>	- ==non occupa spazio sul computer;==
> 
>	- ==non rallenta il sistema.==



> [!failure] Svantaggi del modello SaaS
>
>La semplicità ha però un prezzo:
>
>- **Assenza di controllo**
>    
>	- ==il software è quello fornito dal provider;==
  >      
>	- ==possibilità di personalizzazione limitate.==
  >      
>- **Dipendenza totale dal fornitore**
>    
>	- ==se il servizio chiude o cambia prezzo, l’utente deve adeguarsi.==
 >       
>- **Dati ospitati altrove**
>    
>	- ==i dati risiedono sui server del provider;==
>        
>	- ==è necessario fidarsi delle sue politiche di sicurezza.==
 >       
>- **Dipendenza dalla connessione Internet**
>    
>	- ==senza Internet il servizio non è utilizzabile (salvo modalità offline limitate).==
> 


### Chi gestisce cosa?

#### Il modello di responsabilità nei diversi servizi cloud

Dopo aver analizzato **IaaS, PaaS e SaaS**, è fondamentale chiarire **come cambiano le responsabilità operative** passando da un modello all’altro.  
Il concetto chiave è semplice: 
- ==**più sali di livello, più il provider si occupa degli aspetti tecnici**, mentre l’utente si concentra su livelli sempre più alti (applicazione e dati).==
#### Modello Tradizionale (On-Premise)

Nel modello tradizionale, ==**tutta la responsabilità è dell’azienda**.==

L’utente (o l’organizzazione) deve gestire direttamente:

- ==hardware fisico (server, dischi, rete);==
    
- ==virtualizzazione;==
    
- ==sistema operativo;==
    
- ==software di base (database, web server, runtime);==
    
- ==applicazione;==
    
- ==dati.==
    

> ==In questo scenario **non esiste alcun supporto esterno**: ogni problema tecnico, aggiornamento o guasto è a carico tuo.==


#### IaaS – Infrastructure as a Service

Con **IaaS**, inizia la prima vera delega al cloud provider.

**Il cloud provider gestisce:**

- ==hardware fisico;==
    
- ==virtualizzazione.==
    

**L’utente gestisce:**

- ==sistema operativo;==
    
- ==software di base (database, web server, servizi);==
    
- ==applicazione;==
    
- ==dati.==
    

> ==IaaS fornisce **libertà totale**, ma richiede **competenze sistemistiche avanzate**.==


##### PaaS – Platform as a Service

Con **PaaS**, ==la responsabilità operativa dell’utente diminuisce drasticamente.==

**Il cloud provider gestisce:**

- ==hardware fisico;==
    
- ==virtualizzazione;==
    
- ==sistema operativo;==
    
- ==software di base.==
    

**L’utente gestisce:**

- ==applicazione;==
    
- ==dati.==
    

> ==In questo modello **lo sviluppatore si concentra sul codice**, mentre la piattaforma si occupa di tutto il resto.==


##### SaaS – Software as a Service

Nel modello **SaaS**, ==il cloud provider gestisce **l’intero stack tecnologico**.==

**Il cloud provider gestisce:**

- ==hardware;==
    
- ==virtualizzazione;==
    
- ==sistema operativo;==
    
- ==software di base;==
    
- ==applicazione.==
    

**L’utente gestisce:**

- ==solo i propri dati (ciò che inserisce nell’applicazione).==
    

> ==Il SaaS è il modello con **massima semplicità e minimo controllo**.==

### Quale modello scegliere? – Guida pratica

La scelta del modello cloud dipende da **competenze, obiettivi e contesto**.

#### Quando scegliere IaaS

Scegli **IaaS** se:

- ==sei uno sviluppatore o sistemista esperto;==
    
- ==hai bisogno di **controllo totale**;==
    
- ==devi installare software molto specifico;==
    
- ==hai esigenze particolari non supportate dai servizi gestiti.==
    

**Esempio**:

> “Devo installare un database custom che non esiste come servizio gestito”.

#### Quando scegliere PaaS

Scegli **PaaS** se:

- ==vuoi concentrarti sullo sviluppo applicativo;==
    
- ==hai bisogno di **velocità di rilascio**;==
    
- ==non disponi di un grande team di sistemisti;==
    
- ==vuoi manutenzione e scalabilità automatiche.==
    

**Esempio**:

> “Ho un’idea per un’app e voglio metterla online rapidamente senza gestire server”.

#### Quando scegliere SaaS

Scegli **SaaS** se:

- ==non sei uno sviluppatore;==
    
- ==vuoi semplicemente usare un software;==
    
- ==non vuoi occuparti di aspetti tecnici;==
    
- ==hai esigenze standard.==
    

**Esempio**:

> “Mi serve una mail aziendale funzionante subito”.


### Esempi reali di combinazione dei modelli

##### Startup che sviluppa un’app mobile

Una startup tipicamente **combina più modelli**:

- **[[#IaaS – Infrastructure as a Service (Infrastruttura come Servizio)|IaaS]]**
    
    - ==server [[Lezione 6 - API#API (Application Programming Interface)|API]] personalizzati con configurazioni specifiche;==
        
- **[[#PaaS – Platform as a Service (Piattaforma come Servizio)|PaaS]]**
    
    - ==database gestiti (RDS);==
        
    - ==funzioni serverless per notifiche (Lambda);==
        
- **[[#SaaS – Software as a Service (Software come Servizio)|SaaS]]**
    
    - ==email aziendale;==
        
    - ==strumenti di collaborazione (chat, videoconferenze).==

#### Agenzia di marketing

Un’agenzia marketing **evita IaaS** per mancanza di competenze sistemistiche.

Utilizza principalmente:

- **PaaS**
    
    - hosting dei siti web dei clienti;
        
- **SaaS**
    
    - CRM (Salesforce);
        
    - email marketing (Mailchimp);
        
    - analisi (Google Analytics);
        
    - design (Canva, Figma);
        
    - archiviazione file (Dropbox).


> [!example] Riepilogo con analogia del trasporto
>
>Un’analogia efficace per comprendere i modelli è quella dei mezzi di trasporto:
>
>- **IaaS = Noleggiare un’auto**
>    
>	- massima libertà;
>        
>	- massima responsabilità.
 >       
>- **PaaS = Prendere un taxi**
>    
>	- tu dici dove andare;
>        
>	- la guida è gestita da altri.
>        
>- **SaaS = Prendere l’autobus**
>    
>	- percorso già deciso;
>        
>	- zero gestione.


#### Costi orientativi (esempio: piccolo sito web)

- **IaaS (EC2)**
    
    - 20–50 €/mese;
        
    - ma molto tempo di configurazione e manutenzione.
        
- **PaaS (Elastic Beanstalk + RDS)**
    
    - 50–100 €/mese;
        
    - infrastruttura completamente gestita.
        
- **SaaS (es. Shopify)**
    
    - 30–300 €/mese;
        
    - zero competenze richieste, tutto incluso.
        


### Concetto finale da ricordare

> [!ticket] **Nel cloud non esiste una scelta “migliore” in assoluto:** 
> - ==esiste solo la scelta più adatta al contesto.==
