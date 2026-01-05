# Introduzione: dal cloud come infrastruttura al cloud come astrazione

Nelle sezioni precedenti abbiamo visto come il **[[Lezione 1 - Introduzione al Cloud Computing#Cos’è il Cloud Computing|cloud computing]]** si fondi su concetti chiave quali **[[Lezione 1 - Introduzione al Cloud Computing#La Virtualizzazione il DNA del Cloud Computing|virtualizzazione]]**, **[[Lezione 1 - Introduzione al Cloud Computing#2. Elasticità e Scalabilità il Cuore del Cloud|scalabilità]]**, **[[Lezione 1 - Introduzione al Cloud Computing#3. Isolamento e Sicurezza un altro pilastro del cloud|isolamento]]**, **[[Lezione 1 - Introduzione al Cloud Computing#Auto-scaling il pilota automatico delle risorse|auto-scaling]]** e **[[Lezione 1 - Introduzione al Cloud Computing#4. Migrazione Live continuità senza interruzioni|migrazione live]]**, che permettono di superare i limiti dell’infrastruttura fisica tradizionale.

A questo punto emerge un cambio di prospettiva ancora più profondo:  
nel cloud **non ci interessa più “dove” gira fisicamente la nostra applicazione**, né **su quale server reale** si trovino CPU, RAM o dischi.

Questo passaggio è possibile grazie al concetto di **astrazione**, che rappresenta uno dei principi più potenti e caratterizzanti del cloud computing.  
==L’astrazione trasforma un data center fisico, complesso e fragile, in un **data center astratto**, semplice da usare, governabile tramite interfacce software e indipendente dall’hardware sottostante.==

## [[Lezione 1 - Introduzione al Cloud Computing#Il concetto di Data Center Astratto|Data Center Astratto]]

Nel contesto del **cloud computing**, il **data center fisico scompare dal punto di vista dello sviluppatore e dell’azienda**.

Non è più necessario conoscere o gestire direttamente:

- quale **server fisico** esegue il nostro carico di lavoro;
    
- dove sono **collocati i dischi**;
    
- come sono **cablate le reti**;
    
- quale macchina verrà **aggiornata, sostituita o manutenuta**.
    

Il modello operativo cambia radicalmente:

> **Inviamo il nostro carico di lavoro al cloud e demandiamo al provider la gestione dell’infrastruttura sottostante.**

Il data center non è più percepito come un insieme di macchine fisiche, ma come una **risorsa astratta**, accessibile e controllabile tramite:

- **[[Lezione 6 - API#API (Application Programming Interface)|API]]**;
    
- **pannelli di controllo**;
    
- **configurazioni software**.

###  I benefici dell’astrazione nel Cloud Computing

L’**astrazione** rappresenta il vero _superpotere_ del cloud computing.  
Il suo obiettivo è **nascondere la complessità dell’infrastruttura fisica** dietro **interfacce semplici, coerenti e facilmente utilizzabili**.

Il principio è tanto semplice quanto rivoluzionario:

- ==sotto il cofano esiste un sistema estremamente complesso;==
    
- ==all’utente viene esposta **solo l’interfaccia necessaria per utilizzarlo**, senza obbligarlo a comprenderne i dettagli interni.==
    

> [!example] **Analogia: l’automobile**
>
>Un’analogia efficace è quella della guida di un’automobile.
>
>Quando guidi:
>
>- **non è necessario sapere** come funziona il motore, la trasmissione o l’elettronica;
  >  
>- **è necessario sapere** come utilizzare volante, pedali e cambio.
  >  
>
>L’astrazione nasconde la complessità tecnica e consente all’utente di concentrarsi esclusivamente sull’uso.
>
>Il cloud applica esattamente lo stesso principio all’infrastruttura IT.

### I “superpoteri” dell’astrazione nel cloud

Nel cloud, l’astrazione si manifesta attraverso tre caratteristiche fondamentali che trasformano profondamente il modo di progettare e gestire i sistemi informatici:

1. **[[#La soluzione dell’astrazione il Pannello di Controllo Unificato|Pannello di controllo unificato]]**
    
2. **[[#La rivoluzione della scalabilità nel cloud|Scalabilità]]**
    
3. **Flessibilità**
    

Questi elementi consentono di passare da un modello rigido e hardware-centrico a uno **dinamico, software-driven e orientato ai servizi**.


#### 1. Gestione Semplificata (Simplified Management)

###### Il problema del “prima”: il peso del mondo fisico

Prima del cloud, gestire un data center tradizionale **non era un singolo lavoro**, ma richiedeva competenze distribuite su molteplici ruoli altamente specializzati.

Un team IT doveva coprire almeno cinque ambiti distinti.

##### 1.1 Esperto Hardware

La gestione dell’hardware non si limitava all’acquisto di CPU e RAM, ma implicava:

- verifica delle **compatibilità tra componenti**;
    
- scelta di **alimentatori adeguati** ai carichi massimi;
    
- pianificazione dello **spazio fisico nei rack**;
    
- prevenzione di **colli di bottiglia hardware**.
    

Un singolo errore di compatibilità poteva compromettere l’intero sistema



##### 1.2 Esperto di Networking

La gestione della rete richiedeva:

- progettazione della **[[Reti di computer#Computer Network Topology|topologia di rete]]**;
    
- configurazione di **VLAN** per l’isolamento del traffico;
    
- gestione di **firewall fisici**;
    
- configurazione di **[[ISO E OSI Model#Network Switch|switch]] e [[Reti di computer#^9d3cf6|router]]** spesso eterogenei;
    
- **cablaggio fisico** dell’infrastruttura.
    

Un solo cavo difettoso poteva causare ore di troubleshooting.



##### 1.3 Esperto di Storage

Lo storage comportava decisioni strategiche complesse, tra cui:

- scelta del **livello RAID** (bilanciando performance, ridondanza e costo);
    
- gestione di **SAN** costose e difficili da manutenere;
    
- pianificazione dei **backup**, spesso manuali e soggetti a errori.
    

Ogni scelta introduceva compromessi difficili da modificare nel tempo.



##### 1.4 Tecnico di Manutenzione

La manutenzione era invasiva e rischiosa:

- **downtime pianificati**, spesso notturni o nel weekend;
    
- spegnimento fisico dei server;
    
- sostituzione manuale dei componenti;
    
- rischio di problemi al riavvio o di **firmware che rendevano inutilizzabile la macchina**.
    



##### 1.5 Responsabile della Sicurezza Fisica

Infine, era necessario garantire:

- controllo degli **accessi fisici** (badge, biometria);
    
- monitoraggio di **temperatura e umidità**;
    
- gestione di **UPS e generatori** per prevenire blackout.
    



#### Il risultato

Il risultato di questo modello era un team IT che:

- dedicava la maggior parte del tempo a **mantenere l’infrastruttura operativa**;
    
- aveva poco spazio per innovazione, ottimizzazione e sviluppo applicativo;
    
- operava in un contesto fragile, costoso e lento da evolvere.
    



#### Il cambiamento introdotto dal cloud

Con l’astrazione del cloud:

- tutta questa complessità **viene assorbita dal provider**;
    
- l’infrastruttura diventa **software-defined**;
    
- la gestione avviene tramite **[[Lezione 6 - API#API (Application Programming Interface)|API]] e pannelli di controllo**;
    
- il team può concentrarsi su **applicazioni, logica di business e valore**.
    

In altre parole, l’astrazione libera il team IT dal “peso del ferro” e trasforma l’infrastruttura in uno **strumento flessibile**, non in un vincolo.

### La soluzione dell’astrazione: il Pannello di Controllo Unificato (console web del cloud provider)

Il cloud computing affronta e risolve la complessità del data center tradizionale facendo leva su un principio fondamentale:  
- **l’astrazione completa dell’infrastruttura fisica**.

Nel modello on-premise, la gestione dell’IT richiedeva una molteplicità di strumenti, competenze e interfacce differenti.  
Nel cloud, tutta questa complessità viene ==**condensata in un unico punto di controllo centralizzato**==, chiamato **pannello di controllo unificato** o **console web del cloud provider**.

Il paradigma operativo cambia radicalmente e diventa estremamente semplice e immediato:

> ==**Interfaccia Web (o [[Lezione 6 - API#API (Application Programming Interface)|API]]) → Click (o comando) → Risorsa attiva**==

Quando utilizzi la console di **AWS, Microsoft Azure o Google Cloud**, ogni azione che compi — come creare un server, assegnare spazio di storage o configurare una rete — ==**si traduce internamente in una o più chiamate API**.==

Queste chiamate attivano una complessa catena di automazioni che orchestrano software, hypervisor e sistemi fisici all’interno dei data center del provider.  
In pochi secondi vengono eseguite operazioni che, nel modello tradizionale, richiedevano **settimane di lavoro manuale**, pianificazione, acquisti hardware e l’intervento coordinato di più figure specialistiche.

Il cambiamento concettuale è profondo:

- ==l’utente **non interagisce più con l’hardware fisico**;==
    
- ==l’infrastruttura viene gestita come **software**;==
    
- ==il controllo avviene tramite **API e interfacce standardizzate**.==
    

In altre parole, lo sviluppatore o l’azienda **dialoga con un sistema software che governa l’hardware al suo posto**, beneficiando di: 
- ==velocità,== 
- ==affidabilità== 
- ==e scalabilità== 
Che sono impossibili da ottenere in un data center tradizionale.


##### Esempi pratici:
> [!example] **Dal giorno alla notte**
> **1. Prima del cloud: lanciare un nuovo progetto**
>
>Avviare un nuovo progetto significava affrontare un processo lungo, costoso e rigido:
>
>1. **Mese 1:** 
>	- Nasce l’idea. 
>	- Si prepara una richiesta di budget per un nuovo server.
  >  
>2. **Mese 2** – Il budget viene approvato e si ordina l’hardware.
  >  
>3. **Mese 3** – Il server arriva, viene montato nel rack, cablato e installato il sistema operativo.
  >  
>4. **Mese 4** – Configurazione, messa in sicurezza e consegna al team di sviluppo.
  >  
>
>> [!failure] **Tempo totale:** 3–4 mesi  
>
>
>> [!failure] **Costo:** migliaia di euro, anche se il progetto fallisce
>
>**2. Con il cloud: lanciare un nuovo progetto**
>
>Nel cloud lo scenario è completamente diverso:
>
>1. **Giorno 1, ora 1:** 
>	- Il team ha un’idea.
  >  
>2. **Giorno 1, ora 1, minuto 2:** 
>	- Si accede alla console cloud, si sceglie:
>    
  > 		- potenza della macchina;
 >       
  > 		 - immagine del sistema operativo;
  >      
  > 		 - configurazione di base.  
  >      Si clicca **“Launch”**.
  >      
>
>> [!done] **Tempo totale:** pochi minuti 
>
>
>> [!done] **Costo:** pochi centesimi all’ora 
> 
>Se il progetto fallisce, la risorsa si spegne e **si smette immediatamente di pagare**.


> [!example] **Gestione dei guasti: da emergenza notturna a non-evento**
>**1. Prima del cloud: guasto di un hard disk alle 3 di notte**
>
>1. **03:05** – Scatta un alert: disco guasto.
  >  
>2. **03:30** – Arrivo al data center, identificazione del server e del disco difettoso.
  >  
>3. **04:00** – Sostituzione fisica del disco e avvio del rebuild RAID.
  >  
>4. **08:00** – Dopo ore di attesa, il sistema torna stabile.
  >  
>
>Stress, downtime potenziale e rischio elevato.
>**2. Con il cloud: guasto di un hard disk**
>Nel cloud:
>
>- ==l’[[Docker#^hypervisor|hypervisor]] rileva automaticamente l’anomalia;==
  >  
>- ==la macchina virtuale viene **spostata su un host sano senza interruzioni**;==
   > 
>- ==il disco difettoso viene gestito dal provider.==
  >  
>
>L'utente **non fa nulla**.  
>Al massimo ricevi un’email che ti informa che un problema è stato risolto proattivamente.


### La rivoluzione della scalabilità nel cloud
#### Il problema del “prima”: la gabbia dell’infrastruttura fisica

Nel mondo tradizionale, scalare significava **fare previsioni rischiose** e convivere con limiti rigidi.

##### 1. La scommessa impossibile: prevedere il futuro

La pianificazione della capacità richiedeva di rispondere a una domanda irrealistica:

> “Di quanta potenza avremo bisogno tra sei mesi?”

Questo portava a due scenari, entrambi negativi:

- **Overprovisioning**  
    - ==Si comprava troppo hardware → spreco di capitale, server inutilizzati.==
    
- **Underprovisioning**  
    - ==Si comprava troppo poco → rallentamenti, downtime, perdita di clienti e reputazione.==
    


##### 2. Tempi lunghi che bloccano il business

Se serviva più potenza, il processo poteva durare mesi:

1. approvazione del budget;
    
2. acquisto dell’hardware;
    
3. attesa della consegna;
    
4. installazione fisica;
    
5. configurazione software.
    

In un mercato veloce, **mesi di ritardo equivalgono a opportunità perse**.

##### 3. CapEx vs OpEx e limiti fisici

L’infrastruttura tradizionale richiedeva **investimenti iniziali enormi (CapEx)**:  
- ==grandi spese anticipate per capacità futura incerta.==   ^596c2c

Il cloud trasforma tutto in **spesa operativa (OpEx)**:

- ==paghi solo ciò che usi;==
    
- ==mese per mese;==
    
- ==come una bolletta.==
    

Inoltre, i data center fisici hanno limiti invalicabili:

- ==spazio nei rack;==
    
- ==potenza elettrica;==
    
- ==capacità di raffreddamento.==
    

Superati questi limiti, l’unica soluzione era **costruire un nuovo data center**, con costi e tempi enormi.

#### La magia dell’astrazione: elasticità e Auto Scaling

==Nel cloud, le risorse diventano un **pool virtualmente infinito** che si espande e si contrae automaticamente.==

**È come un supermercato che apre e chiude casse in tempo reale in base alle code.**

### Come funziona l’[[Lezione 1 - Introduzione al Cloud Computing#Auto-scaling il pilota automatico delle risorse|Auto Scaling]]

- **Carico alto**  
    Se una regola (es. CPU > 70%) viene superata:
    
    - ==vengono create nuove istanze da template;==
        
    - ==il bilanciatore di carico distribuisce il traffico.==
        
- **Carico basso**  
    Se il carico scende:
    
    - ==le istanze inutili vengono rimosse;==
        
    - ==il costo si azzera immediatamente.==

Tutto questo **cambia radicalmente le regole del gioco**.  
Se nel modello tradizionale tempi e costi rappresentavano un freno significativo, oggi il cloud rende **molto più semplice, rapido ed economicamente sostenibile** lanciare, gestire e manutenere un’applicazione web.

L’infrastruttura non è più un ostacolo da prevedere e finanziare in anticipo, ma una **risorsa elastica** che si adatta dinamicamente al successo (o all’insuccesso) dell’applicazione.  
In questo modo, ciò che prima rappresentava un rischio elevato diventa un’opportunità controllabile.

#### Dal rischio all’opportunità: esempi concreti

> [!example] **E-commerce e Black Friday**
> 
> 
> Nel modello tradizionale, per gestire il picco di traffico concentrato in un solo giorno all’anno era necessario mantenere **10 server attivi per 365 giorni**, sostenendo costi elevati per una capacità inutilizzata quasi sempre.
>
>Con il cloud, invece, l’infrastruttura si adatta automaticamente:
>
>- **prima:** capacità massima costante per tutto l’anno;
  >  
>- **ora:** i server aggiuntivi vengono attivati solo per **24–48 ore**, durante il periodo di picco.
  >  
>
>Il costo diventa così **proporzionale all’utilizzo reale**, eliminando sprechi strutturali.



> [!example] **Startup in crescita**
> 
> 
> In passato, anche un’idea promettente richiedeva **decine di migliaia di euro di investimento iniziale** solo per predisporre l’infrastruttura necessaria a un possibile successo.
>
>Con il cloud:
>
>- **prima:** l’infrastruttura andava finanziata _prima_ di avere utenti;
  >  
>- **ora:** si parte con **pochi euro al mese** e si scala solo se e quando la crescita avviene.
  >  
>
>La conseguenza è la **drastica riduzione della barriera all’ingresso**, che rende accessibile l’innovazione anche a piccoli team o singoli sviluppatori.
> 


> [!example] **Applicazione virale**
> 
> Nel modello tradizionale, un successo improvviso rappresentava spesso un problema:
>
>- l’infrastruttura non era pronta;
  >  
>- il traffico causava rallentamenti o downtime;
  >  
>- un’opportunità di visibilità si trasformava in un danno reputazionale.
  >  
>
>Nel cloud, grazie all’auto-scaling:
>
>- **prima:** il picco di traffico portava al collasso del sistema;
   > 
>- **ora:** le risorse vengono allocate in tempo reale, mantenendo l’applicazione stabile e reattiva.
  >  
>
>Il successo non è più subito passivamente, ma **gestito e sfruttato attivamente**.

#### Tipi di scalabilità

L’Auto Scaling utilizza tre strategie principali:

1. **[[Lezione 1 - Introduzione al Cloud Computing#Scaling Up (Scalabilità Verticale)|Vertical Scaling (Scale Up)]]**  
    - ==Aumentare CPU, RAM o disco di una singola macchina.== 
    - ==Utile, ma con limiti fisici.==
    
2. **[[Lezione 1 - Introduzione al Cloud Computing#Scaling Out (Scalabilità Orizzontale) aggiungere nuove macchine|Horizontal Scaling (Scale Out)]]**  
    - ==Aggiungere più macchine identiche che lavorano in parallelo.== 
    - ==È il modello più potente.==
    
3. **[[Lezione 1 - Introduzione al Cloud Computing#Auto-scaling il pilota automatico delle risorse|Auto Scaling]]**  
    - ==L’orchestratore intelligente che decide **quando e come scalare**, mantenendo performance e costi sotto controllo.==

### La flessibilità del Cloud

##### Scegliere lo strumento giusto per ogni lavoro

Se la **scalabilità** risolve il problema di _quanto_ crescere, la **flessibilità** risponde a una domanda ancora più strategica:  
- ==**come adattarsi rapidamente al cambiamento**, sperimentare nuove soluzioni e innovare senza essere vincolati da scelte tecniche irreversibili.==

La flessibilità del cloud rappresenta quindi il passaggio da un’IT rigida e pianificata a lungo termine a un’IT **dinamica, modulare e orientata all’evoluzione continua**.



#### 1. Il problema del “prima”: le catene dell’infrastruttura fisica

Nel modello IT tradizionale, ogni decisione infrastrutturale era un **impegno a lungo termine**.  
==Acquistare hardware significava legarsi per anni a scelte che potevano diventare rapidamente obsolete o inadatte==.

##### Vendor lock-in hardware: la dipendenza forzata

Una volta scelto un fornitore di hardware (Dell, HP, IBM, ecc.), si entrava nel suo ecosistema:

- ==componenti progettati per funzionare al meglio solo tra loro;==
    
- ==compatibilità limitata con soluzioni concorrenti;==
    
- ==costi di migrazione elevatissimi.==
    

Anche se il mercato offriva soluzioni migliori o più economiche, **cambiare direzione era spesso impraticabile**.  
==L’azienda rimaneva vincolata alle roadmap, ai prezzi e alle scelte tecnologiche di un singolo vendor.==



##### Configurazioni rigide: la “camicia di forza” tecnologica

Un server acquistato rappresentava una fotografia statica delle esigenze del momento.  
Il problema è che il business non è statico.

Se nel tempo le necessità cambiavano — ad esempio:

- ==più RAM e meno CPU;==
    
- ==storage più veloce;==
    
- ==workload diversi da quelli inizalmente previsti== —
    

la macchina rimaneva invariata per tutto il suo ciclo di vita (3–5 anni).

L’analogia è evidente:  
**comprare un’auto sportiva e scoprire, dopo un anno, di aver bisogno di un furgone**.



##### Sperimentazione costosa: l’innovazione come rischio

Nel mondo pre-cloud, sperimentare nuove tecnologie era economicamente rischioso:

- provare un nuovo database;
    
- testare una piattaforma di analytics;
    
- validare un’architettura alternativa.
    

Ogni esperimento richiedeva **nuovo hardware dedicato**, con costi elevati anche solo per “provare”.

Il risultato era un IT conservativo:

- ==meno sperimentazione;==
    
- ==più inerzia tecnologica;==
    
- ==adozione tardiva dell’innovazione.==
    



#### 2. Il potere dell’astrazione: un catalogo di “Lego” tecnologici

L’astrazione del cloud demolisce queste barriere.  
Non si acquistano più server fisici, ==ma si accede a un **catalogo di servizi specializzati**, combinabili e sostituibili in qualsiasi momento==.

La vera forza non è solo la quantità di opzioni disponibili, ma la ==**libertà di cambiare strumento senza rifare l’infrastruttura**==.

#### Potenza di calcolo: risorse su misura

La potenza di calcolo diventa configurabile come un abito sartoriale:

- ==istanze piccole ed economiche per sviluppo e test;==
    
- ==macchine bilanciate per applicazioni web standard;==
    
- ==istanze ottimizzate per RAM per database in-memory;==
    
- ==istanze con GPU per machine learning e calcolo parallelo.==
    

Ogni carico di lavoro può essere eseguito **sull’hardware virtuale più adatto**, senza sprechi.

##### Storage: ogni dato al posto giusto

Nel cloud non tutti i dati vengono trattati allo stesso modo:

- ==dati ad accesso frequente su storage veloce;==
    
- ==dati consultati raramente su storage più economico;==
    
- ==archivi storici su soluzioni a bassissimo costo.==
    

Questo permette di **ottimizzare i costi senza sacrificare le performance**, pagando solo ciò che serve davvero.

##### Database: il motore giusto per ogni applicazione

Il cloud mette a disposizione un’intera “officina” di basi di dati:

- ==database relazionali gestiti;==
    
- ==database NoSQL altamente scalabili;==
    
- ==data warehouse per analisi massive;==
    
- ==cache in-memory per ridurre la latenza.==
    

La scelta del database **non è più definitiva:**  
- ==può essere **cambiata o affiancata** in base all’evoluzione del progetto.==



#### 3. Flessibilità reale: adattarsi alla velocità del business

##### Machine Learning: dal prototipo alla produzione

Un progetto di machine learning attraversa fasi molto diverse:

- sviluppo a basso costo;
    
- training intensivo e temporaneo;
    
- inferenza stabile in produzione.
    

Il cloud consente di usare **risorse estremamente potenti solo quando servono**, spegnendole subito dopo.  
==Il costo segue il ciclo di vita del progetto, non lo anticipa.==

##### Startup che cambia strategia (pivot)

Nel cloud, cambiare direzione non richiede la sostituzione dell’infrastruttura fisica.

Un’azienda può:

- ==dismettere servizi non più adatti;==
    
- ==attivarne altri più coerenti con il nuovo modello di business;==
    
- ==riconfigurare l’architettura in pochi giorni.==
    

==L’organizzazione si adatta **alla velocità del mercato**, non a quella degli acquisti hardware.==
##### Sperimentazione continua

Il cloud rende economico il fallimento controllato:

- ==creare ambienti di test completi in pochi minuti;==
    
- ==validare rapidamente un’idea;==
    
- ==eliminare tutto se l’esperimento non funziona.==
    

==Fallire non è più un problema finanziario, ma un **passaggio di apprendimento**.==  
Questa libertà è uno dei veri motori dell’innovazione.



### Il risultato combinato

Quando **gestione semplificata**, **scalabilità** e **flessibilità** agiscono insieme, l’effetto è sistemico.

#### Time-to-market

- prima: mesi per predisporre l’infrastruttura;
    
- ora: ore o giorni.
    

#### Riduzione del rischio

- prima: investimenti massicci anticipati;
    
- ora: crescita graduale e proporzionale al successo.
    

#### Accelerazione dell’innovazione

- prima: pochi esperimenti, molto costosi;
    
- ora: molti esperimenti, a basso costo.
    

#### Focus sul valore

Il tempo del team cambia radicalmente:

- meno gestione dell’infrastruttura;
    
- più sviluppo, analisi e innovazione.
    



### Conclusione: l’astrazione come leva di business

L’astrazione del cloud non è solo una comodità tecnica, ma una **leva strategica** che:

- democratizza l’accesso alla tecnologia;
    
- accelera l’innovazione;
    
- riduce i rischi economici;
    
- libera i talenti da compiti a basso valore.
    

L’IT smette di essere un **centro di costo** e diventa un **motore di crescita e sperimentazione continua**.