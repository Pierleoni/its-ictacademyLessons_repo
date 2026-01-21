
## Introduzione: dal Web al Cloud Computing

Nel percorso svolto finora abbiamo analizzato i **[[Lezione 1; Fondamenti delle Applicazioni Web|fondamenti delle applicazioni web moderne]]**, concentrandoci su come avviene la comunicazione tra [[Reti di computer#1. Modello Client/Server|client e server]].

Abbiamo visto come un’applicazione web si basi sul **[[Lezione 3; Protocollo HTTP; il Modello TCP- IP, il Modello ISO-OSI e la comunicazione tra livelli|protocollo HTTP/HTTPS]]**, su cui si innestano le **[[Lezione 6 - API|API]]**, spesso progettate secondo lo **[[Lezione 7 - Sistemi REST|stile architetturale REST]]**, con l’uso di [[Lezione 7 - Sistemi REST#Il concetto di Risorsa in REST|risorse]], [[Lezione 7 - Sistemi REST#Livello 2 Verbi HTTP(HTTP Verbs)|metodi HTTP]] e [[Lezione 7 - Sistemi REST#1. Vincolo Statelessness|vincoli come la statelessness]].  
Abbiamo inoltre approfondito aspetti cruciali della sicurezza e del controllo delle richieste nel browser, come la **[[Lezione 9 - Same Origin Policy e CORS#La Same-Origin Policy|Same Origin Policy]]**, il meccanismo **[[Lezione 9 - Same Origin Policy e CORS#Cos’è CORS (Cross-Origin Resource Sharing)|CORS]]** e le **[[Lezione 9 - Same Origin Policy e CORS#Cos’è una Preflight Request|preflight request]]**, comprendendo come il browser governi l’accesso alle risorse remote.  
Infine, attraverso strumenti come **[[Lezione 8 - Chiamate Curl|cURL]]**, abbiamo osservato in modo concreto come queste comunicazioni avvengano a basso livello, al di fuori del browser.

A questo punto sorge una domanda naturale:  
- **dove “vivono” realmente queste applicazioni, queste API e questi server?**

È qui che entra in gioco il **cloud computing**.  
Il cloud rappresenta il livello infrastrutturale che rende possibile tutto ciò che abbiamo studiato finora: 
- è l’ambiente in cui vengono eseguiti i server web, le API REST, i database e i servizi di rete che rispondono alle richieste HTTP dei client.

Studiare il cloud computing significa quindi capire **come vengono fornite, gestite e scalate le risorse** che permettono alle applicazioni web di funzionare in modo affidabile, sicuro e performante.

## Cos’è il Cloud

Il **cloud** può essere visto come un’**astrazione delle risorse informatiche fondamentali**:

- ==potenza di calcolo;==
    
- ==spazio di archiviazione;==
    
- ==rete.==
    

Invece di preoccuparci di server fisici, dischi o cablaggi di rete, il cloud ci permette di lavorare con queste risorse in modo **virtuale**, come servizi accessibili via Internet.
### Cos’è il Cloud Computing

==Il **cloud computing** è un **modello di erogazione delle risorse informatiche** tramite Internet.==  
Server, storage, database, reti e software non vengono più gestiti localmente su macchine di proprietà, ma sono forniti da grandi provider come **Amazon (AWS)**, **Microsoft (Azure)** o **Google (Google Cloud)**.

In termini semplici, possiamo immaginare il cloud come ==un **computer remoto estremamente potente**, che non si trova fisicamente sulla nostra scrivania ma in un data center gestito da terzi.==  
Noi lo utilizziamo tramite la rete e **paghiamo solo per le risorse effettivamente consumate**, in modo simile a quanto avviene con l’energia elettrica.


### Il concetto di Data Center Astratto

Uno degli aspetti chiave del cloud computing è il concetto di **[[Lezione 2 - Data center astratto#Data Center Astratto|astrazione del data center]]**.

Nel cloud:

- ==**non ci interessa più** su quale server fisico gira la nostra applicazione;==
    
- ==inviamo semplicemente il nostro **carico di lavoro** (applicazioni, API, servizi);==
    
- **il provider cloud si occupa di tutto il resto: hardware, manutenzione, ridondanza, guasti.**
    

Questo approccio consente di concentrarsi **sullo sviluppo del software**, lasciando la complessità infrastrutturale al provider.
### I Tre Pilastri del Cloud Computing

Il cloud computing si basa su tre componenti fondamentali, che rappresentano la **versione virtuale di un data center tradizionale**.

#### 1. Compute – Potenza di Calcolo Virtuale

Il **Compute** rappresenta la capacità di elaborazione: 
- [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] e [[Il modello di Von Neumann#RAM|memoria RAM]] [[Docker#La virtualizzazione|virtualizzate]].

Nel cloud possiamo creare **server virtuali on-demand**, senza acquistare hardware fisico. 
La potenza di calcolo può essere **scalata dinamicamente**:

- ==da un piccolo sito web con esigenze minime;==
    
- ==fino ad applicazioni complesse come sistemi di machine learning che richiedono decine o centinaia di core.==
    

In AWS, il servizio principale per il compute è **EC2 (Elastic Compute Cloud)**.  
Nel concreto, il compute serve a **far girare il codice** della nostra applicazione web o delle nostre API REST.

#### 2. Storage – Spazio di Archiviazione

Lo **Storage** è lo spazio dedicato alla conservazione dei dati:

- ==file;==
    
- ==immagini;==
    
- ==video;==
    
- ==backup;==
    
- ==dati applicativi.==
    

==Nel cloud lo spazio di archiviazione è **praticamente illimitato** e viene pagato in base all’uso effettivo.==  
Esistono diverse tipologie di storage, ottimizzate per esigenze differenti: prestazioni elevate, costi ridotti, archiviazione a lungo termine.

#### 3. Network – Connettività e Rete

Il **Network** gestisce tutta la comunicazione tra i componenti del sistema:

- ==come i server comunicano tra loro;==
    
- ==come gli utenti accedono alle applicazioni;==
    
- ==come i dati viaggiano in modo sicuro.==
    

Include strumenti fondamentali come:

- ==load balancer;==
    
- ==firewall;==
    
- ==reti private virtuali;==
    
- ==CDN per la distribuzione globale dei contenuti.==
    

Nel cloud è possibile definire reti virtuali completamente personalizzate.  
In AWS, il servizio principale è **VPC (Virtual Private Cloud)**.  
Nel concreto, il network serve a **proteggere l’applicazione**, controllare gli accessi e gestire il traffico.

In AWS, il servizio di riferimento è **S3 (Simple Storage Service)**.  
Nel concreto, ==lo storage serve ad esempio a **salvare i contenuti caricati dagli utenti** o i file associati a un’applicazione.==

### La Virtualizzazione: il DNA del Cloud Computing

La **virtualizzazione** rappresenta il vero **fondamento tecnologico del cloud computing**.  
È grazie a questa tecnologia che oggi esistono piattaforme come **AWS**, **Google Cloud** e **Microsoft Azure** così come le conosciamo.

Senza virtualizzazione, il cloud moderno non sarebbe possibile: mancherebbero la flessibilità, la scalabilità e l’efficienza che caratterizzano i servizi cloud.
## Cosa si intende per Virtualizzazione

==[[Docker#La virtualizzazione|La virtualizzazione]] è la tecnologia che consente di **suddividere un singolo computer fisico in più computer virtuali indipendenti**, chiamati **[[Docker#Le macchine virtuali (VM)|macchine virtuali (VM)]]**.==

Un’analogia efficace è quella di un **palazzo**:

- il palazzo rappresenta il **server fisico**;
    
- ogni appartamento rappresenta una **macchina virtuale**;
    
- ogni inquilino vive in modo indipendente, pur condividendo la stessa struttura fisica.
    

Ogni macchina virtuale dispone di:

- ==un proprio sistema operativo;==
    
- ==risorse dedicate (CPU, RAM, storage virtuale);==
    
- ==isolamento rispetto alle altre VM.==
#### Prima e Dopo la Virtualizzazione

##### Prima della virtualizzazione

**Nel modello tradizionale:**

- ==**1 server fisico = 1 sistema operativo = 1 applicazione**==
    
- ==utilizzo delle risorse estremamente basso (circa **10–15%**);==
    
- ==costi elevati per l’acquisto e la manutenzione dell’hardware;==
    
- ==scarsa flessibilità in caso di variazioni del carico.==
    

Questo modello portava a un enorme **spreco di risorse** e a tempi di risposta molto lenti alle nuove esigenze.

### Con la virtualizzazione

==Con l’introduzione della virtualizzazione:==

- ==1 server fisico può ospitare 10, 50 o più macchine virtuali;==
    
- ==utilizzo delle risorse molto più efficiente (80–90%);==
    
- ==CPU, RAM e storage vengono condivisi in modo intelligente;==
    
- ==le VM possono essere spostate automaticamente tra host fisici;==
    
- ==non è più rilevante sapere su quale server fisico gira una VM.==
    

Questo approccio abilita un modello molto più **flessibile, economico e scalabile**, tipico del cloud.

## Perché la Virtualizzazione è il Fondamento del Cloud

### 1. Astrazione dell’Hardware

Il cloud si basa su una forte **astrazione dell’hardware**:
```nginx
Hardware fisico → Hypervisor → Macchine Virtuali → Applicazioni
```
Al centro di questo processo c’è l’**[[Docker#^hypervisor|hypervisor]]**, ovvero il “cervello” della virtualizzazione.

L’hypervisor è il software che:

- ==crea e gestisce le macchine virtuali;==
    
- ==consente a più sistemi operativi di funzionare sullo stesso server fisico;==
    
- ==nasconde la complessità dell’hardware sottostante.==
    

In pratica, l’hypervisor si occupa di:

1. **Astrazione dell’hardware**  
    - ==Le risorse fisiche (CPU, RAM, dischi) vengono “mascherate” e presentate alle VM come se fossero dedicate.==
    
2. **Allocazione delle risorse**  
    - ==Le risorse vengono distribuite dinamicamente alle VM in base alle loro necessità, garantendo efficienza e flessibilità.==
    
3. **Isolamento**  
    - ==Ogni VM è separata dalle altre: un problema su una macchina virtuale non compromette le restanti.==
    

Grazie a questa astrazione, **allo sviluppatore o all’azienda non interessa più il server fisico**, ma solo il servizio fornito dal cloud.

### 2. Elasticità e Scalabilità: il Cuore del Cloud

Un’altra conseguenza diretta della virtualizzazione è la possibilità di ottenere **elasticità e scalabilità**, concetti fondamentali nel cloud computing.

Grazie alle VM, il cloud permette di:

- **[[#Scaling Up (Scalabilità Verticale)|Scaling Up]]**: 
	- ==aumentare le risorse di una [[Docker#Le macchine virtuali (VM)|VM]] esistente;==
    
- **[[#Scaling Out (Scalabilità Orizzontale) aggiungere nuove macchine|Scaling Out]]**: 
	- ==creare nuove [[Docker#Le macchine virtuali (VM)|VM]] in pochi secondi;==
    
- **[[#Auto-scaling il pilota automatico delle risorse|Auto-scaling]]**: 
	- ==creare o distruggere automaticamente [[Docker#Le macchine virtuali (VM)|VM]] in base al carico.==
    

Questo trasforma la gestione delle risorse IT da un modello **statico e lento** a uno **dinamico e immediato**.



#### Scaling Up (Scalabilità Verticale)

Lo **Scaling Up**, o scalabilità verticale, ==consiste nell’**aumentare la potenza di una singola macchina virtuale**.==

##### Come funziona

Grazie all’[[Docker#^hypervisor|hypervisor]], che gestisce un pool condiviso di risorse fisiche:

- ==è possibile aumentare i **core CPU** assegnati a una VM;==
    
- ==aumentare la **quantità di RAM**;==
    
- ==estendere lo spazio di storage.==
    

Questa operazione avviene tramite il pannello di controllo del cloud provider, spesso con pochi click.

###### Il vantaggio principale

La vera rivoluzione è la **tempestività**:

- ==l’operazione richiede pochi minuti;==
    
- ==spesso è sufficiente un semplice riavvio della VM (o talvolta neanche quello);==
    
- ==non è necessario acquistare nuovo hardware o intervenire fisicamente sui server.==
    

In sintesi, lo Scaling Up permette di **“potenziare” una macchina esistente** in modo rapido e trasparente, ad esempio in previsione di:

- **un picco di traffico;**
    
- **una campagna di marketing;**
    
- **l’elaborazione di grandi volumi di dati.**

#### Scaling Out (Scalabilità Orizzontale): aggiungere nuove macchine

Lo **Scaling Out**, detto anche **scalabilità orizzontale:**
- ==consiste nell’**aumentare la capacità complessiva di un sistema aggiungendo nuove macchine virtuali**, invece di potenziarne una sola.==

**A differenza dello [[#Scaling Up (Scalabilità Verticale)|Scaling Up]]:** 
- ==non si “ingrandisce” una VM esistente, ma si **replica** la stessa macchina più volte, facendole lavorare **in parallelo**.==

##### Come funziona

Nel cloud, le macchine virtuali vengono create a partire da **immagini o template**: 
- ==modelli preconfigurati che contengono sistema operativo, configurazioni e applicazioni.==

Il processo è il seguente:

- ==si parte da una VM “base”;==
    
- ==l’hypervisor utilizza il template per **creare cloni identici**;==
    
- ==le nuove VM vengono avviate in **secondi o minuti**;==
    
- ==un **load balancer** (bilanciatore di carico) distribuisce il traffico in ingresso tra tutte le VM disponibili.==
    

Il **load balancer** ha il compito di: 
- ==evitare che una singola macchina venga sovraccaricata, migliorando **prestazioni** e **affidabilità**.==

> [!done] **Il vero vantaggio: “secondi, non settimane”**
> Questo approccio rappresenta una rottura netta rispetto all’IT tradizionale.
> 
> Nel modello classico, aggiungere un nuovo server significava:
> 
> - approvazione del budget;
>     
> - ordine dell’hardware;
>     
> - attesa della consegna;
>     
> - installazione fisica nel data center;
>     
> - cablaggio;
>     
> - installazione del sistema operativo e del software.
>     
> 
> Un processo che poteva richiedere **settimane o mesi**.
> 
> ==Nel cloud, invece, lo Scaling Out consente di **replicare una VM quasi istantaneamente**, rendendo il sistema estremamente reattivo.==

> [!example] **In sintesi**
>  
> 
> Lo Scaling Out è particolarmente indicato per:
> 
> - gestire **picchi di traffico imprevedibili**;
>     
> - costruire architetture **ad alta disponibilità**;
>     
> - aumentare l’affidabilità del sistema.
>     
> 
> Se una VM smette di funzionare, le altre continuano a servire le richieste, evitando l’interruzione del servizio.

#### Auto-scaling: il pilota automatico delle risorse

L’**Auto-scaling** rappresenta l’evoluzione naturale dello Scaling Up e dello Scaling Out.  
È un meccanismo che ==**combina questi approcci in modo completamente automatico**, senza intervento umano.==

##### Come funziona

Nel cloud è possibile definire **regole basate su metriche di performance**, ad esempio:

- **Regola di [[#Scaling Out (Scalabilità Orizzontale) aggiungere nuove macchine|Scaling Out]]**  
    - ==“Se l’utilizzo medio della [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] supera l’80% per più di 5 minuti, crea una nuova [[Docker#Le macchine virtuali (VM)|VM]]”.==
    
- **Regola di Scaling In**  
    - ==“Se l’utilizzo medio della [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] scende sotto il 20% per più di 10 minuti, elimina una [[Docker#Le macchine virtuali (VM)|VM]]”.==
    

Il sistema di orchestrazione del cloud monitora costantemente le metriche e applica queste regole in tempo reale.

> [!done] **I vantaggi dell’Auto-scaling**
>  
> 
> L’Auto-scaling offre il meglio di entrambi i mondi:
> 
> - **Performance**  
>     - ==In caso di picchi improvvisi (ad esempio un forte aumento di utenti), il sistema crea automaticamente nuove VM, mantenendo l’applicazione reattiva.==
>     
> - **Ottimizzazione dei costi**  
>     - ==Quando il carico diminuisce, le VM non necessarie vengono eliminate, evitando di pagare per risorse inutilizzate.==
>     

> [!example] **In sintesi**
>  
> 
> L’Auto-scaling è il **cuore del modello “pay-as-you-go”** del cloud:
> 
> - garantisce sempre la potenza necessaria;
>     
> - evita sprechi;
>     
> - migliora resilienza ed efficienza economica.

### 3. Isolamento e Sicurezza: un altro pilastro del cloud

Un aspetto fondamentale della virtualizzazione è l’**isolamento completo tra le macchine virtuali**.

Ogni VM è separata dalle altre, anche se condividono lo stesso hardware fisico.  
Un’analogia efficace è quella di una **nave a compartimenti stagni**:

- ==ogni VM è una stanza sigillata;==
    
- ==se una stanza ha un problema, l’acqua non invade le altre;==
    
- ==l’intera nave rimane operativa.==
    

#### Come viene garantito l’isolamento

L’hypervisor fornisce a ogni VM:

- ==una **CPU virtuale**;==
    
- ==una **RAM virtuale**;==
    
- ==una **scheda di rete virtuale**;==
    
- ==un **disco virtuale**.==
    

==La VM “crede” di avere hardware dedicato e **non è consapevole dell’esistenza delle altre VM**.==

Inoltre, l’hypervisor agisce come un **controllore del traffico estremamente rigoroso**:

- ==ogni accesso all’hardware fisico passa attraverso di lui;==
    
- ==una VM può usare solo le risorse che le sono state assegnate;==
    
- ==è impossibile interferire direttamente con le altre VM.==

> [!done] **Vantaggi pratici dell’isolamento**
> 
> 
> **A. Resistenza ai guasti (Fault Tolerance)**
> 
> Se una VM va in crash, il problema resta **confinato**.
> 
> **Scenario:**
> 
> - VM 1: applicazione web
>     
> - VM 2: database critico
>     
> - VM 3: ambiente di test
>     
> 
> Un bug sulla VM 1 causa un crash.
> 
> **Risultato:**
> 
> - solo la VM 1 smette di funzionare;
>     
> - la VM 2 e la VM 3 continuano a operare normalmente;
>     
> - il “raggio d’esplosione” del guasto è limitato.
>  **B. Sicurezza e contenimento delle minacce**
> 
> L’isolamento è anche una **barriera di sicurezza fondamentale**, soprattutto nei contesti multi-tenant.
> 
> **Scenario:**
> 
> - un attaccante compromette l’applicazione sulla VM 1.
>     
> 
> **Risultato:**
> 
> - l’attaccante resta confinato nella VM 1;
>     
> - non può accedere alla memoria delle altre VM;
>     
> - non può intercettare il traffico di rete altrui;
>     
> - non può accedere al file system del server fisico.
>     
> 
> Questa “sandbox” virtuale rende il cloud **intrinsecamente più sicuro**, limitando la propagazione degli attacchi.

### 4. Migrazione Live: continuità senza interruzioni

Un’ulteriore capacità chiave della virtualizzazione è la **migrazione live** delle macchine virtuali:

- ==Le VM possono essere spostate da un server fisico a un altro **senza interrompere il servizio**.==

#### Come funziona la migrazione live

Il processo avviene in modo estremamente rapido:

1. **Copia della memoria**  
    - ==L’hypervisor copia la RAM della VM dal Server A al Server B mentre la VM è ancora attiva==.
    
2. **Sincronizzazione delle modifiche**  
    - ==Le modifiche alla memoria vengono tracciate e sincronizzate.==
    
3. **Il passaggio finale**  
    - ==La VM viene messa in pausa per pochi millisecondi, le ultime modifiche vengono copiate e la VM riparte sul Server B.==
    
4. **Aggiornamento della rete**  
    - ==La rete viene aggiornata per puntare al nuovo server==.
    

Per l’utente finale, l’operazione è **impercepibile**.



> [!done]  **Vantaggi della Migrazione Live**
> 1. **Manutenzione a zero downtime**
> 
> Senza migrazione live, la manutenzione richiederebbe lo spegnimento delle VM e ore di downtime.
> 
> Con la migrazione live:
> 
> - le VM vengono spostate su altri server;
>     
> - la manutenzione avviene a caldo;
>     
> - il servizio resta sempre disponibile.
>     
> 
> 2. **Tolleranza ai guasti automatica**
> 
> I sistemi cloud monitorano costantemente l’hardware.
> 
> Se viene rilevato un problema imminente:
> 
> - le VM vengono migrate automaticamente su server sani;
>     
> - il guasto viene prevenuto prima di causare un’interruzione.
>     
> 
> Questo rende la gestione dell’infrastruttura **proattiva**, aumentando drasticamente l’affidabilità.

