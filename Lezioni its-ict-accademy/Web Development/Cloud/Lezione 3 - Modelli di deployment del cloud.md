# Introduzione: dal “come funziona” al “dove lo metto”

Nei capitoli precedenti abbiamo visto **cosa rende possibile il cloud** ([[Lezione 1 - Introduzione al Cloud Computing#La Virtualizzazione il DNA del Cloud Computing|virtualizzazione]] e [[Lezione 1 - Introduzione al Cloud Computing#1. Astrazione dell’Hardware|astrazione]]), **quali benefici offre** (scalabilità, flessibilità, gestione semplificata) e **perché cambia il modo di progettare le applicazioni web**.

A questo punto la domanda naturale non è più _se_ usare il cloud, ==ma **come e dove utilizzarlo**.==

Un’azienda, infatti, non deve solo scegliere _quante_ risorse usare o _come_ scalarle, ma anche:

- ==**dove risiedono fisicamente i dati**;==
    
- ==**chi gestisce l’infrastruttura**;==
    
- ==**quanto controllo e quanta responsabilità mantenere**.==
    

Queste scelte definiscono il **modello di deployment del cloud**, ovvero il modo in cui le risorse cloud vengono distribuite e gestite.

## Un’analogia intuitiva: organizzare una festa 

Per comprendere i modelli di deployment, utilizziamo un’analogia concreta.

Immagina di dover organizzare una festa:

1. **A casa tua**  
    Devi comprare tutto, cucinare, pulire prima e dopo.  
    → **Cloud Privato**
    
2. **Affittare una sala**  
    Paghi solo per la serata e qualcun altro gestisce pulizie e logistica.  
    → **[[#Cloud Pubblico|Cloud Pubblico]]**
    
3. **Usare entrambe le soluzioni**  
    Antipasti a casa, cena nella sala.  
    → **Cloud Ibrido**
    
4. **Affittare più sale contemporaneamente**  
    Una per il pranzo, una per la cena, magari da gestori diversi.  
    → **Multi-Cloud**
    

Allo stesso modo, nel cloud un’azienda può decidere **come combinare risorse proprie e risorse esterne**, in base a costi, sicurezza, flessibilità e vincoli normativi.


## Cloud Pubblico

Il **cloud pubblico** è un modello di deployment in cui:
- ==un’azienda **utilizza risorse informatiche messe a disposizione da un provider esterno**, anziché possedere e gestire un’infrastruttura propria.==

In questo modello:

- ==l’azienda **affitta risorse di calcolo, archiviazione, database e rete**;==
    
- le risorse sono fornite da grandi cloud provider come:
    
    - **Amazon Web Services (AWS)**,
        
    - **Microsoft Azure**,
        
    - **Google Cloud Platform (GCP)**;
        
- ==l’infrastruttura è **condivisa** tra più clienti (multi-tenant), ma **logicamente isolata** grazie alla [[Docker#La virtualizzazione|virtualizzazione]].==
    

Quindi le risorse **non risiedono fisicamente presso l’azienda**, 
==ma sono ospitate all’interno dei **data center del provider**, che si occupa interamente della loro gestione.==

> [!tldr] **Glossario: Data center**  
> Strutture industriali altamente specializzate che ospitano **migliaia di server operativi 24 ore su 24**, dotate di:
> 
> - ==alimentazione elettrica ridondata;==
>     
> - ==sistemi avanzati di raffreddamento;==
>     
> - ==sicurezza fisica e logica;==
>     
> - ==monitoraggio continuo e automazione.==
>     
> 
> Il cliente non accede mai direttamente all’hardware fisico: 
> - interagisce con l’infrastruttura **solo tramite console web o [[Lezione 6 - API#API (Application Programming Interface)|API]]**.

In sintesi, nel cloud pubblico: 
- ==**l’azienda si concentra sull’uso delle risorse**,== 
- ==mentre **il provider gestisce l’intera infrastruttura fisica**, consentendo costi variabili, rapidità di provisioning e alta scalabilità.==

### Come funziona operativamente il Cloud Pubblico

Dal punto di vista pratico, l’utilizzo del cloud pubblico segue un flusso ben definito e altamente automatizzato.

Il processo tipico è il seguente:

1. si accede alla **[[Lezione 2 - Data center astratto#La soluzione dell’astrazione il Pannello di Controllo Unificato (console web del cloud provider)|console web del cloud provider]]** oppure si utilizzano le relative **[[Lezione 6 - API#API (Application Programming Interface)|API]]**;
    
2. si seleziona il **tipo di risorsa** da creare (ad esempio una **[[Docker#Le macchine virtuali (VM)|macchina virtuale]]**);
    
3. si configurano i principali parametri:
    
    - potenza di calcolo (CPU e RAM),
        
    - sistema operativo,
        
    - rete e regole di accesso;
        
4. si conferma la creazione della risorsa;
    
5. **nel giro di pochi minuti** il server virtuale è operativo e pronto all’uso.
    

#### Modello di costo: _Pay-as-you-go_

Il cloud pubblico adotta un modello di costo **a consumo**, noto come _pay-as-you-go_:

- ==si paga **solo per il tempo effettivo di utilizzo** della risorsa;==
    
- ==quando una risorsa non è più necessaria, può essere **spenta o eliminata**, interrompendo immediatamente i costi.==
    

Il principio è analogo a quello di una **bolletta elettrica**:

> ==**usi la risorsa → consumi → paghi**==

Questo modello elimina gli investimenti iniziali elevati e rende i costi **proporzionali all’uso reale**, favorendo 
- sperimentazione, 
- scalabilità 
- controllo della spesa.

##### Vantaggi del cloud pubblico

> [!done] **Nessun investimento iniziale**
> - non è necessario acquistare hardware;
 >   
>- non servono decine di migliaia di euro in anticipo;
  >  
>- puoi partire con costi minimi (anche pochi euro al mese).
   > 
>
>Questo abbassa drasticamente la **barriera di ingresso**, soprattutto per startup e piccoli progetti.


> [!done] **Velocità e time-to-market**
> 
>
>- **prima**: ordinare un server fisico richiedeva mesi;
  >  
>- **ora**: un server è disponibile in pochi minuti.
  >  
>
>Questo consente di:
>
>- testare idee rapidamente;
  >  
>- ridurre il time-to-market;
  >  
>- reagire velocemente al mercato.


> [!done] **Scalabilità automatica**
>  
>
>Il cloud pubblico cresce e si riduce insieme al carico:
>
>- pochi utenti → poche risorse;
   > 
>- picchi improvvisi → molte risorse create automaticamente;
   > 
>- fine del picco → risorse eliminate.
  >  
>
>Il tutto avviene senza interventi manuali e senza sprechi strutturali.



> [!done] **Manutenzione delegata**
> Il provider si occupa di:
>
>- sostituzione dell’hardware guasto;
  >  
>- aggiornamenti dell’infrastruttura;
   > 
>- alimentazione e continuità elettrica;
   > 
>- raffreddamento e sicurezza fisica.
   > 
>
>Dal punto di vista dell’azienda, l’infrastruttura **semplicemente funziona**.

##### Svantaggi del cloud pubblico

> [!failure] **Minore controllo sull'hardware**
> - non puoi accedere fisicamente ai server;
  >  
>- non sai su quale macchina fisica gira il tuo carico di lavoro;
   > 
>- devi fidarti del provider.
  >  
>
>Per molte aziende questo non è un problema, ma in alcuni contesti può esserlo.


> [!failure] **Vincoli normativi e legali**
>
>Alcuni settori hanno obblighi specifici:
>
>- dati bancari;
  >  
>- dati sanitari;
  >  
>- dati governativi.
  >  
>
>In certi casi, la legge impone che i dati rimangano:
>
>- in un determinato paese;
  >  
>- o addirittura all’interno di una specifica struttura.


> [!failure] **Costi variabili e imprevedibili**
> 
>
>Il modello pay-as-you-go richiede attenzione:
>
>- una risorsa dimenticata accesa continua a generare costi;
  >  
>- un successo improvviso può aumentare rapidamente la spesa.
  >  
>
>Il cloud pubblico **non è “economico di default”**, ma **economico se gestito correttamente**.

#### Esempio pratico
Consideriamo il caso di **Mario**, che apre un piccolo **negozio online**.

###### Situazione iniziale: traffico normale

- **Giorno 1**
    
    - circa **10 visitatori al giorno**;
        
    - è sufficiente **un server molto piccolo**;
        
    - **costo**: circa **5 € al mese**.
        

Mario paga solo le risorse realmente necessarie per il traffico iniziale del suo sito.
###### Evento eccezionale: Black Friday

Durante il **Black Friday**, il traffico aumenta improvvisamente:

- **10.000 visitatori in pochi giorni**;
    
- un solo server non sarebbe sufficiente;
    
- il sistema cloud **scala automaticamente**:
    
    - vengono attivati **circa 50 server**;
        
    - solo per **48 ore**.
        

Il costo totale per gestire questo picco è di circa **300 €**, perché:

- i server extra esistono **solo per il tempo necessario**;
    
- appena il traffico torna normale, vengono **spenti automaticamente**.
    
###### Ritorno alla normalità

- **Gennaio**
    
    - il traffico si stabilizza;
        
    - il sistema torna a utilizzare **un solo server**;
        
    - **costo mensile** di nuovo pari a **5 €**.
        

Mario non continua a pagare risorse inutili.



##### Confronto con l’infrastruttura tradizionale

Se Mario avesse adottato un’infrastruttura **fisica tradizionale**:

- avrebbe dovuto acquistare **in anticipo** server sufficienti per il Black Friday;
    
- investimento iniziale di **decine di migliaia di euro**;
    
- per **363 giorni all’anno**, quei server sarebbero rimasti:
    
    - accesi ma inutilizzati, oppure
        
    - spenti ma comunque già pagati.
        


> [!done] **Il vero vantaggio del cloud pubblico**
>
> 
> Il cloud pubblico cambia completamente la logica dei costi:
> 
> - non devi **prevedere il successo** in anticipo;
>     
> - non devi **scommettere capitali** su picchi occasionali;
>     
> - paghi **solo quando il successo arriva davvero**.
>     
> 
>> [!example] In sintesi:
> >
> > ==Il cloud pubblico trasforma un rischio economico elevato in un costo variabile e proporzionale all’utilizzo reale delle risorse.==
> 
> Questo è uno dei motivi principali per cui il cloud pubblico è particolarmente adatto a **startup, e-commerce e applicazioni con traffico variabile**.


## Cloud Privato 

Il **cloud privato** è un modello in cui: 
- ==**l’infrastruttura informatica è di proprietà esclusiva dell’azienda**.==

In termini semplici:

- ==l’azienda **acquista i server fisici**;==
    
- ==li installa **all’interno di una propria sede** (ufficio, data center aziendale, capannone);==
    
- ==mantiene **pieno controllo** su hardware, rete, dati e sicurezza.==
    

Questo modello rappresenta il **modo tradizionale di gestire l’IT**, diffuso prima della diffusione del cloud pubblico (pre-2010) e tuttora utilizzato in contesti particolarmente regolamentati.

> [!link] **A differenza del [[#Cloud Pubblico|cloud pubblico]]:**
> 
> 
> - ==**le risorse non vengono affittate**;==
>     
> - ==**l’infrastruttura non è condivisa** con altre aziende;==
>     
> - ==**tutta la responsabilità ricade sull’organizzazione**.==

###  Come funziona operativamente

Nel cloud privato, il ciclo di vita dell’infrastruttura è interamente gestito dall’azienda:

1. ==vengono acquistati **server fisici professionali** (es. Dell, HP, Lenovo);==
    
2. i server vengono installati in ambienti dedicati con:
    
    - ==raffreddamento;==
        
    - ==cablaggio di rete;==
        
    - ==sistemi di alimentazione protetta;==
        
3. ==viene assunto o mantenuto un **team IT interno**;==
    
4. ==ogni guasto hardware viene gestito direttamente;==
    
5. per aumentare la capacità:
    
    - ==si acquistano nuovi server;==
        
    - ==si attendono consegna, installazione e configurazione (settimane).==
        

Il modello è quindi **rigido e pianificato**, non elastico.


#### Vantaggi del Cloud Privato 

> [!done] **Controllo totale dell’infrastruttura**
> - l’azienda **sceglie ogni componente**:
 >   
  >  - marca dei server;
  >      
  >  - configurazione hardware;
 >       
 >   - rete e firewall;
>        
>- i server sono **fisicamente accessibili**;
  >  
>- nessuna dipendenza da provider esterni.


> [!done] **Massimo controllo sui dati**
> - i dati risiedono **fisicamente all’interno dell’azienda**;
 >   
>- l’accesso fisico è limitato e controllato;
 >   
>- non esiste il rischio di co-locazione con dati di terzi.
  >  
>
>Questo aspetto è cruciale per:
>
>- banche;
  >  
>- enti pubblici;
 >   
>- sanità;
  >  
>- settori soggetti a normative stringenti.


> [!done] **Costi più prevedibili**
> - la spesa principale è **iniziale ([[Lezione 2 - Data center astratto#^596c2c|CAPEX]])**;
>    
>- una volta acquistata l’infrastruttura:
 >   
  >  - ==non ci sono costi variabili imprevedibili;==
  >      
  >  - ==il costo ricorrente principale è l’elettricità.==
  >      
>
>Non esiste il rischio di “bollette cloud fuori controllo”.




> [!done] **Operatività locale**
> - i sistemi interni possono funzionare anche:
>    
 >   - senza connessione Internet;
 >       
 >   - in reti isolate (intranet).
 >       
>
>Questo è un vantaggio in contesti industriali o critici.


#### Svantaggi del Cloud Privato 


> [!failure] **Investimento iniziale elevato**
>
>- l’infrastruttura va acquistata **prima di sapere se servirà davvero**;
  >  
>- investimento tipico:
>    
>    - da **decine a centinaia di migliaia di euro**;
 >       
>- se il progetto fallisce:
>    
>    - l’investimento è già stato sostenuto;
>        
>    - l’hardware perde rapidamente valore.



> [!failure] **Scarsa velocità di adattamento**
>
>- ottenere nuove risorse richiede:
 >   
 >   - ordini;
>        
 >   - attese di settimane;
>        
 >   - installazioni manuali.
>        
>
>> [!link] Confronto:
>>
>>- **cloud privato** → settimane;
>>    
>>- **cloud pubblico** → minuti.


> [!failure] **Costi del personale**
>
>- è necessario un **team IT dedicato**:
>    
 >   - sistemisti;
 >       
 >   - esperti di rete;
 >       
 >   - tecnici di manutenzione;
 >       
>- stipendi elevati e continui, indipendenti dall’uso reale dei sistemi.






> [!failure]  **Responsabilità totale dei guasti**
>
>- ogni problema è a carico dell’azienda:
 >   
  > 	 - dischi rotti;
  >      
  > 	 - blackout;
  >      
  > 	 - problemi di raffreddamento;
   >     
>- sono necessari:
 >   
 >   - UPS;
  >      
  > 	 - generatori di emergenza;
  >      
  > 	 - piani di disaster recovery.


> [!failure]  Spreco di risorse
>
>- l’infrastruttura viene dimensionata per i **picchi massimi**;
  >  
>- per gran parte del tempo:
 >   
  > 	 - molte risorse restano inutilizzate;
  >      
  > 	 - ma continuano a consumare energia e spazio.

####  Esempio pratico: banca con cloud privato

Una banca di medie dimensioni:

- 200 dipendenti;
    
- sala server nel seminterrato della sede;
    
- 20 server fisici in armadi rack;
    
- impianto di raffreddamento dedicato;
    
- 5 tecnici IT a tempo pieno;
    
- generatore diesel per blackout;
    
- **investimento iniziale**: circa **300.000 €**.
    

##### Perché sceglie il cloud privato?

- la normativa impone che:
    
    - ==i dati bancari restino **sotto controllo diretto**;==
        
    - ==l’infrastruttura sia localizzata sul territorio nazionale;==
        
- l’uso di cloud pubblico potrebbe:
    
    - ==violare vincoli normativi;==
        
    - ==rendere opaca la localizzazione dei dati.==


> [!example]  **In sintesi**
>
>Il **cloud privato** offre:
>
>- massimo controllo;
 >   
>- massima sicurezza fisica;
  >  
>- costi prevedibili.
  >  
>
>Ma richiede:
>
>- grandi investimenti iniziali;
  >  
>- tempi lunghi;
  >  
>- personale specializzato;
   > 
>- scarsa elasticità.
   > 
>
>È una soluzione **potente ma rigida**, adatta solo a contesti in cui **controllo e compliance** sono più importanti di **flessibilità e velocità**.

## Cloud Ibrido

Il **cloud ibrido** è un modello di deployment in cui: 
- ==**[[#Cloud Privato|cloud privato]] e [[#Cloud Pubblico|cloud pubblico]] convivono e collaborano** all’interno della stessa architettura.==

In termini semplici:

- ==una parte dell’infrastruttura è **di proprietà dell’azienda** (cloud privato);==
    
- ==un’altra parte è **affittata da un provider esterno** come AWS, Azure o GCP (cloud pubblico).==
    

L’azienda sceglie **quali carichi di lavoro mantenere internamente** e **quali delegare al cloud pubblico**, in base a criteri di:

- ==sicurezza;==
    
- ==normativa;==
    
- ==costo;==
    
- ==scalabilità.==
    

> [!example] **Analogia**  
> È come avere una cucina in casa ma ordinare cibo d’asporto quando arrivano molti ospiti:  
> usi le tue risorse per il quotidiano, e risorse esterne solo quando serve.
### Come funziona operativamente

Nel cloud ibrido l’infrastruttura viene **suddivisa per criticità**:

1. ==i **dati sensibili o regolamentati** rimangono sui server interni;==
    
2. ==i servizi meno critici o più variabili vengono spostati sul cloud pubblico;==
    
3. i due ambienti comunicano tramite:
    
    - ==connessioni Internet sicure;==
        
    - ==VPN o link dedicati cifrati;==
        
4. in caso di necessità, l’azienda può:
    
    - ==**espandersi temporaneamente** sul cloud pubblico;==
        
    - ==ridurre le risorse una volta terminato il picco.==
        

Questo meccanismo è spesso chiamato **cloud bursting**.

#### Vantaggi del Cloud Ibrido

> [!done] Il meglio di entrambi i mondi
> 
> 
> Il cloud ibrido consente di combinare:
> 
> - **controllo e sicurezza** del cloud privato;
>     
> - **elasticità e velocità** del cloud pubblico.
>     
> 
>> [!example] **Esempio:**
>> 
>> - dati sensibili → cloud privato;
>>     
>> - sito web o API → cloud pubblico.
>>     
> 



> [!done] **Conformità normativa senza rinunciare all’innovazione**
> 
> 
> Molte aziende devono rispettare leggi che impongono:
> 
> - localizzazione dei dati;
>     
> - controllo diretto dell’infrastruttura.
>     
> 
> Con il cloud ibrido:
> 
> - ==i dati regolamentati restano interni;==
>     
> - ==i servizi innovativi (app, analisi, AI) possono sfruttare il cloud pubblico.==
>     
> 
> ==Questo permette di essere **compliant** e allo stesso tempo **agili**.==
> 



> [!done] **Gestione efficiente dei picchi di carico**
> 
> 
> L’infrastruttura interna viene dimensionata per il carico normale.
> 
> In caso di picchi:
> 
> - si affittano risorse aggiuntive nel cloud pubblico;
>     
> - si pagano solo per il tempo necessario;
>     
> - al termine del picco si torna alla configurazione standard.
>     
> 
> Il risultato è:
> 
> - niente sprechi;
>     
> - costi proporzionati all’uso reale.



#### Svantaggi del Cloud Ibrido

> [!failure] **Maggiore complessità architetturale**
> 
> 
> - devono essere gestiti **due ambienti diversi**;
>     
> - servono competenze sia:
>     
>     - on-premise;
>         
>     - cloud;
>         
> - aumenta la complessità di:
>     
>     - ==configurazione;==
>         
>     - ==monitoraggio;==
>         
>     - ==troubleshooting.==

   



> [!failure] **Costi di connessione**
> 
> 
> - la comunicazione tra cloud privato e pubblico deve essere:
>     
>     - veloce;
>         
>     - stabile;
>         
>     - sicura;
>         
> - spesso sono necessarie:
>     
>     - connessioni dedicate;
>         
>     - soluzioni di rete avanzate.
>         
> 
> Questi collegamenti possono avere **costi significativi**.
> 

> [!failure] **Superficie di sicurezza più ampia**
>  
> 
> Nel cloud ibrido devono essere protetti:
> 
> - il data center interno;
>     
> - l’infrastruttura sul cloud pubblico;
>     
> - il canale di comunicazione tra i due.
>     
> 
> La sicurezza diventa quindi **più articolata** e richiede maggiore attenzione.


####  Esempio pratico: ospedale con cloud ibrido

Un ospedale con 500 medici adotta un modello ibrido.

##### [[#Cloud Privato|Cloud privato]] (interno all’ospedale)

- **cartelle cliniche dei pazienti;**
    
- **esami diagnostici;**
    
- **sistemi clinici critici.**
    

Questi dati:

- **sono altamente sensibili;**
    
- **per legge devono rimanere sotto controllo diretto.**
    
##### [[#Cloud Pubblico|Cloud pubblico]] (AWS)

- sito web istituzionale;
    
- app mobile per prenotazioni;
    
- sistemi di analisi dati e supporto alla ricerca.
    

Questi servizi:

- devono scalare rapidamente;
    
- beneficiano dell’elasticità del cloud pubblico.

##### Integrazione

Quando un paziente prenota online:

- ==l’app sul cloud pubblico;==
    
- ==comunica in modo sicuro;==
    
- ==con i sistemi interni dell’ospedale.==
    

Il cloud ibrido permette quindi di:

- ==rispettare la privacy;==
    
- ==migliorare i servizi digitali;==
    
- ==mantenere flessibilità e controllo.==


> [!example] **In sintesi**
> 
> 
> Il **cloud ibrido** è una soluzione di compromesso che:
> 
> - ==unisce sicurezza e flessibilità;==
>     
> - ==riduce sprechi;==
>     
> - ==abilita l’innovazione anche in contesti regolamentati.==
>     
> 
> È particolarmente adatto a organizzazioni medio-grandi che:
> 
> - ==non possono spostare tutto sul cloud pubblico;==
>     
> - ==ma non vogliono rinunciare ai suoi vantaggi.==


## Multi-Cloud

Il **multi-cloud** è un modello di deployment in cui:
- ==un’azienda utilizza **più [[#Cloud Pubblico|cloud pubblici]] contemporaneamente**, appartenenti a provider diversi.==

In pratica:

- non si sceglie un solo fornitore (come AWS);
    
- si usano **più piattaforme cloud** nello stesso sistema informativo, ad esempio:
    
    - Amazon Web Services;
        
    - Microsoft Azure;
        
    - Google Cloud Platform.
        

> [!example] **Analogia**  
> È come fare la spesa in supermercati diversi:  
> vai da ciascuno per acquistare ciò che fa meglio o costa meno.

L’obiettivo non è solo la scalabilità, ma **evitare dipendenze** e **sfruttare le specializzazioni** di ogni provider.

### Come funziona operativamente

Nel multi-cloud:

- ==ogni cloud viene scelto per uno **scopo specifico**;==
    
- ==i vari servizi devono **comunicare tra loro** attraverso Internet in modo sicuro.==
    

Un’architettura tipica può prevedere che:

1. ==il sito web e i server applicativi siano ospitati su AWS;==
    
2. ==i servizi di intelligenza artificiale sfruttino Google Cloud;==
    
3. ==l’autenticazione utenti e l’integrazione aziendale usino Azure;==
    
4. ==tutte queste componenti scambino dati tramite API e connessioni protette.==
    

Dal punto di vista tecnico, il multi-cloud richiede:

- ==progettazione accurata;==
    
- ==integrazione tra piattaforme eterogenee;==
    
- ==strumenti di orchestrazione e monitoraggio avanzati.==

####  Vantaggi del Multi-Cloud

> [!done] **Nessuna dipendenza da un singolo provider**
>  
> 
> Uno dei principali motivi per adottare il multi-cloud è evitare il **vendor lock-in**.
> 
> Questo significa:
> 
> - ==se un provider ha un disservizio, altri possono continuare a funzionare;==
>     
> - ==se un fornitore aumenta i prezzi, esistono alternative già operative.==
>     
> 
> L’azienda mantiene così un **maggiore potere contrattuale**.
> 



> [!done] **Sfruttare il meglio di ogni piattaforma**
>  
> 
> Ogni cloud provider ha punti di forza specifici:
> 
> - ==Google Cloud è spesso scelto per AI e data analytics;==
>     
> - ==AWS è molto forte su infrastruttura e servizi di database;==
>     
> - Az==ure si integra nativamente con l’ecosistema Microsoft.==
>     
> 
> Il multi-cloud permette di:
> 
> - scegliere il servizio migliore per ogni esigenza;
>     
> - non accontentarsi di soluzioni “generaliste”.
>     
> 

> [!done] **Conformità normativa internazionale**
>  
> 
> In contesti globali, le leggi sui dati variano da paese a paese.
> 
> Con il multi-cloud:
> 
> - ==in Europa si possono usare cloud conformi al GDPR==;
>     
> - ==in Cina si possono adottare provider locali obbligatori per legge;==
>     
> - ==in altri paesi si scelgono soluzioni compatibili con le normative locali.==
>     
> 
> Questo modello facilita la **presenza globale** senza violare le leggi.


####  Svantaggi del Multi-Cloud

> [!failure] **Complessità molto elevata**
>  
> 
> Ogni cloud ha:
> 
> - ==strumenti diversi;==
>     
> - ==interfacce diverse;==
>     
> - ==modelli di sicurezza differenti.==
>     
> 
> Gestire più piattaforme equivale a:
> 
> - ==imparare più “linguaggi operativi”;==
>     
> - ==aumentare la probabilità di errori.==





> [!failure] **Necessità di team altamente specializzati**
>  
> 
> Il multi-cloud richiede competenze profonde su:
> 
> - AWS;
>     
> - Azure;
>     
> - Google Cloud.
>     
> 
> Questo implica:
> 
> - ==team numerosi;==
>     
> - ==costi di personale elevati;==
>     
> - ==maggiore difficoltà nel coordinamento.==
>     



> [!failure] **Costi di trasferimento dati**
> 
> 
> Spostare dati da un cloud a un altro:
> 
> - ==non è gratuito;==
>     
> - ==può diventare molto costoso su grandi volumi.==
>     
> 
> ==Ogni provider applica tariffe per l’uscita dei dati, rendendo il traffico inter-cloud un fattore di costo rilevante.==
> 



> [!failure] **Gestione economica complessa**
>  
> 
> - ==fatture separate per ogni provider;==
>     
> - ==modelli di pricing differenti;==
>     
> - ==maggiore difficoltà nel controllo della spesa.==
>     
> 
> ==Senza strumenti adeguati, il rischio è **perdere visibilità sui costi reali**.==

#### Esempio pratico: azienda internazionale di videogiochi

Una grande azienda di videogiochi adotta una strategia multi-cloud.

##### AWS

- server di gioco in Europa e America;
    
- archiviazione dei file di gioco (immagini, audio, asset).
    

##### Google Cloud

- intelligenza artificiale per i bot;
    
- analisi del comportamento dei giocatori.
    

##### Azure

- autenticazione tramite account Microsoft;
    
- integrazione con Xbox e servizi Microsoft.

##### Perché sceglie il Multi-Cloud

- ==ogni provider viene usato per ciò che fa meglio;==
    
- ==se un cloud ha problemi, il servizio continua sugli altri;==
    
- ==l’azienda può negoziare condizioni economiche migliori con più fornitori.==


> [!example]  **In sintesi**
>
> 
> Il **multi-cloud** è una strategia potente ma avanzata che:
> 
> - riduce la dipendenza da un singolo vendor;
>     
> - aumenta flessibilità e resilienza;
>     
> - consente di sfruttare le eccellenze di ogni provider.
>     
> 
> È però adatto soprattutto a:
> 
> - grandi aziende;
>     
> - organizzazioni internazionali;
>     
> - team con elevate competenze tecniche e budget adeguati.

### Confronto tra i Modelli di Deployment del Cloud

Dopo aver analizzato singolarmente **[[#Cloud Pubblico|cloud pubblico]], [[#Cloud Privato|privato]], [[#Cloud Ibrido|ibrido]] e [[#Multi-Cloud|multi-cloud]]**, è utile metterli a confronto diretto.  
Questo confronto aiuta a capire **quali compromessi** introduce ciascun modello e **in quali contesti** risulta più adatto.

#### Confronto sintetico
| Criterio                   | Cloud Pubblico          | Cloud Privato | Cloud Ibrido | Multi-Cloud  |
| -------------------------- | ----------------------- | ------------- | ------------ |:------------:|
| **Costi iniziali**         | Molto bassi             | Molto alti    | Alti         |    Bassi     |
| **Scalabilità**            | Praticamente illimitata | Limitata      | Alta         |  Illimitata  |
| **Controllo**              | Basso                   | Totale        | Medio        |    Medio     |
| **Complessità gestionale** | Bassa                   | Alta          | Molto alta   |   Massima    |
| **Time-to-market**         | Minuti                  | Mesi          | Settimane    |    Minuti    |
| **Conformità normativa**   | Limitata                | Totale        | Alta         |    Media     |
| **Vendor lock-in**         | Alto                    | Nessuno       | Medio        |    Basso     |
| **Dimensione del team**    | Piccolo                 | Grande        | Grande       | Molto grande |
Questa tabella evidenzia un punto chiave:  
- ==**non esiste una soluzione “migliore in assoluto”**, ma solo soluzioni **più adatte a uno specifico contesto**.==

### Capire i modelli tramite analogie

Le analogie aiutano a fissare i concetti in modo intuitivo.

#### [[#Cloud Pubblico|Cloud Pubblico]] – _Affittare un appartamento_

- ==Non è tuo, ma lo usi quando serve;==
    
- ==paghi un canone proporzionale all’uso;==
    
- ==se qualcosa si rompe, se ne occupa il proprietario.==
    

> [!ticket] ==È ideale quando vuoi **velocità, flessibilità e pochi pensieri**, accettando un controllo limitato.==
>  



#### [[#Cloud Privato|Cloud Privato]] – _Comprare una casa_

- ==È tua e la gestisci come vuoi;==
    
- ==paghi tutto (o quasi) subito;==
    
- ==manutenzione e problemi sono a tuo carico.==
    

> [!ticket] ==È adatto quando servono **controllo totale, sicurezza e conformità normativa**, anche a costo di rigidità e spese elevate.==
>  



#### [[#Cloud Ibrido|Cloud Ibrido]] – _Casa tua + garage in affitto_

- ==La casa ospita ciò che è critico e personale;==
    
- ==il garage esterno serve per esigenze temporanee o extra;==
    
- ==i due spazi comunicano tra loro.==
    

> [!ticket] ==È una soluzione di compromesso che unisce **sicurezza e flessibilità**, ma aumenta la complessità gestionale.==




#### [[#Multi-Cloud|Multi-Cloud]] – _Tre case in città diverse_

- una casa a Milano, una a Roma, una a Napoli;
    
- usi quella più comoda a seconda della situazione;
    
- ma devi gestire più contratti, più regole e più costi.
    

> [!ticket] Offre **massima resilienza e libertà**, ma richiede **molte competenze e risorse**.
>  



#### Quale modello scegliere? Una guida pratica

La scelta del modello cloud non è tecnica, ma **strategica**.  
Dipende da fattori come dimensione dell’azienda, budget, vincoli normativi e obiettivi di business.

##### Linee guida semplificate

- **Startup o piccola azienda**
    
    - 👉 _Cloud Pubblico_
        
    - ==Costi bassi, velocità di avvio, possibilità di crescere rapidamente.==
        
- **Banche, ospedali, enti pubblici**
    
    - 👉 _Cloud Privato o Ibrido_
        
    - ==Dati sensibili, obblighi normativi, necessità di controllo.==
        
- **Grandi multinazionali**
    
    - 👉 _Multi-Cloud_
        
    - ==Presenza globale, requisiti normativi diversi, elevata capacità organizzativa.==
        
- **In caso di dubbio**
    
    - 👉 _Inizia dal Cloud Pubblico_
        
    - ==È il punto di partenza più semplice, economico e flessibile.==
        
    - ==In seguito è sempre possibile evolvere verso modelli ibridi o multi-cloud.==
        



### Conclusione

I modelli di deployment del cloud rappresentano diversi equilibri tra: 
- costo, 
- controllo, 
- flessibilità 
- complessità.

Comprenderli significa:

- ==progettare sistemi più adatti al contesto reale;==
    
- ==ridurre rischi inutili;==
    
- ==usare il cloud come **leva strategica**, non solo come scelta tecnologica.==