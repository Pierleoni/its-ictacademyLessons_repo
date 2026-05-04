# Introduzione 
Prima di spiegare cos’è Docker, è importante comprendere **perché** questa tecnologia è diventata così centrale nello sviluppo moderno, specialmente nei contesti orientati ai microservizi e alle metodologie DevOps, dove agilità, portabilità e scalabilità sono fondamentali.

## La virtualizzazione 
**Ma cos'è docker?**
La risposta a questa prima domanda è:
==Docker è una tecnologia di virtualizzazione.==
La virtualizzazione è una tecnica che consente di: 
- ==**astrarre l’hardware fisico** e creare ambienti virtuali isolati all’interno di un sistema operativo.== 

==In questi ambienti, i programmi **credono di essere eseguiti direttamente su una macchina fisica**, con una propria [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]], [[Il modello di Von Neumann#RAM|RAM]], disco, ecc., ma in realtà stanno utilizzando risorse **virtualizzate** fornite da un software intermedio.== 
Quindi la  virtualizzazione **serve per astrarre il concetto di computer fisico:** 
-  ==in concreto, permette di creare un ambiente virtuale dentro il SO della macchina.== 
In altre parole: 
- ==**un sistema che al suo interno ospita un altro sistema/ambiente virtuale.**==
  
In altri termini, la virtualizzazione consente di creare al **di sopra del sistema operativo reale**, uno o più ambienti "simulati", ciascuno dei quali si comporta come un computer indipendente, dotato di proprie risorse (virtuali). 

> [!example] Questo permette, ad esempio, di simulare una macchina con 2 o 4 core CPU, con una certa quantità di RAM, ecc.
> 

Le tecnologie di virtualizzazione — come quelle che permettono di creare **macchine virtuali (VM)** — nascono proprio per facilitare:

- ==la **portabilità** degli ambienti software.==
    
- ==la **replicabilità** delle configurazioni.==
    
- ==l’**ottimizzazione dei costi** ([[Lezione 1 - Introduzione al Cloud Computing|soprattutto in ambienti server e cloud]]).==
    
- ==e in generale per **isolare i contesti di esecuzione**==.

Docker si inserisce in questo scenario come una **tecnologia di virtualizzazione più leggera**, che consente una gestione più efficiente di ambienti e applicazioni, rendendole facilmente trasportabili ed eseguibili su molteplici sistemi, senza complicazioni legate all’installazione o alla configurazione dell’ambiente sottostante.


### Confronto tra VM e Docker

Per comprendere davvero il funzionamento di Docker, è essenziale distinguere il suo approccio da quello delle macchine virtuali classiche.
#### Le macchine virtuali (VM)
Una macchina virtuale si basa su un'infrastruttura a più livelli:


![[VM esempio.png]]

Partendo da questa immagine possiamo vedere almeno **5 livelli:** 
1. **Hardware fisico**  
	(CPU, RAM, disco rigido, motherboard, ecc.)
2. **[[I fundamentals di un Sistema Operativo#^hypervisorSO|Hypervisor]]**:
	  -  Si tratta di un software specializzato che gestisce la virtualizzazione. 
	    
	  - ==L’hypervisor si interpone tra l’hardware fisico e i sistemi operativi "ospiti" (guest), virtualizzando le risorse della macchina e assegnandole alle singole VM.==
	
	^hypervisor

> [!example] **Esempi di hypervisor**
> -  VirtualBox 
> - VMware Workstation, 
> - VMware ESXi, 
> - ecc.

	
   
> [!info] Gli hypervisor si suddividono in 2 principali categorie:
> 1. Bare metal: 
> 	- Direttamente sull'hardware senza SO host.
>	- Esempio: VMware ESXi, Microsoft Hyper-V Server.
> 2. Hosted: 
>	- Sopra un sistema operativo host.
>	- Ad esempio: VirtualBox, VMware Workstation, Parallels  

	   
3. <mark style="background: #00FF02A6;">Guest OS(Sistema operativo ospite)</mark>: 
	- ==È il sistema operativo installato all’interno della VM.== 
	- Può essere Windows, Linux, macOS, ecc. 
	- ==Ogni VM ha il **proprio sistema operativo completo**, separato da quello del host==.
	- Inoltre all'interno della nostro Hypervisor possiamo avere diversi SO ospiti.
4. <mark style="background: #00FF02A6;">Liberie BIN</mark>: 
	  -  ==Sono le librerie e i runtime specifici del sistema operativo ospite, ad esempio .NET per Windows, le glibc per Linux, ecc.==
5. **<mark style="background: #00FF02A6;">Applicazioni: </mark>**
    - ==Infine, le applicazioni che vogliamo eseguire sono installate **sopra** tutto questo stack==.



 

Tuttavia, come si può notare, [[VM esempio.png|questo modello]] introduce una certa **ridondanza**: 
- ==ogni VM ha bisogno di un intero sistema operativo, più tutte le librerie necessarie a supportare l'applicazione.== 
- ==Difatti questo comporta un uso intensivo di risorse, tempi di avvio più lenti e maggiore complessità nella gestione.==

Ed è proprio qui che entra in gioco Docker, proponendo un’alternativa **più leggera ed efficiente**: la **containerizzazione**.


#### Docker: virtualizzazione container
Vediamo ora come funziona la tecnologia dei container, come quella su cui si basa Docker.
Partendo da questa immagine di riferimento possiamo notare come anche Docker abbia **5 livelli nella sua struttura**.  

![[Tecnologia Container.png]]

Alla base di questa architettura abbiamo:
1. **<mark style="background: #ADCCFFA6;">Hardware fisico della macchina:</mark>**
	   (CPU, RAM, disco, ecc.)
2. **<mark style="background: #ADCCFFA6;">Sistema operativo nativo:</mark>** 
	-    Può essere sia Linux che Windows. 
	- ==I container possono essere eseguiti su entrambi, a seconda del contesto e della compatibilità.==
3. **<mark style="background: #ADCCFFA6;">Container Engine:</mark>**
    - ==Questo è il “fratello” dell’hypervisor.==
	- ==A differenza di quest’ultimo, però, **non è un sistema operativo**, ma un motore (engine) che si occupa di gestire i container.== 

> [!hint] **Docker, ad esempio, è un container engine molto diffuso**
> - Esso si occupa di creare, avviare, isolare e controllare i container sul sistema operativo sottostante.

1.  <mark style="background: #E5FF00A6;">Librerie BIN:</mark>
	 -  ==Sono le dipendenze e i runtime necessari per eseguire l'applicazione.== 
	 - ==Ogni container può portare con sé le proprie librerie==, ad esempio una specifica versione di Java o Python. 
2. <mark style="background: #E5FF00A6;">le applicazioni: </mark>
	 -   ==Le app vere e proprie, che vengono eseguite all'interno del container, insieme alle dipendenze necessarie==.



A differenza delle **[[#Le macchine virtuali (VM)|macchine virtuali]]**, dove ogni istanza porta con sé anche un sistema operativo completo, i **container** sono molto più leggeri: 
- ==includono solo l’applicazione e le sue dipendenze==. 
- ==Inoltre il **sistema operativo** è **unico** e condiviso tra tutti i container attraverso il container engine.==

Questo rende i container:

- ==**più veloci da avviare**==
    
- ==**meno pesanti** in termini di consumo di risorse (RAM, CPU, disco)==
    
- ==**più portabili** tra ambienti diversi.==

Quindi i container risultano **più leggeri e compatti rispetto alle VM:** 
- ==contengono solamente **le applicazioni** e le **librerie di cui hanno bisogno** per funzionare (come ad esempio Java, Node.js, Python, ecc.).== 
   
Al contrario, nelle macchine virtuali ogni applicazione viene impacchettata **insieme al proprio sistema operativo completo**, oltre che alle sue dipendenze: 
- ==Questo rende le VM molto più pesanti in termini di consumo di risorse==.

Nel mondo dei container, invece, il **sistema operativo è uno solo**: 
- quello del sistema host, che viene **condiviso da tutte le applicazioni** tramite il container engine (come Docker). 
- Riprendo [[Tecnologia Container.png|l'immagine di riferimento della struttura di Docker]]: 
	- Notiamo come <mark style="background: #E5FF00A6;">App1</mark> e <mark style="background: #D76E08A6;">App2</mark>, pur condividendo lo stesso sistema operativo, sono eseguite **in ambienti isolati**: 
		- ==ogni container ha il proprio spazio di esecuzione, e un’applicazione non è a conoscenza dell’altra==.

> [!info] **Va però evidenziata una differenza importante:** 
> Nelle **macchine virtuali**, l’isolamento tra applicazioni è più forte: 
> - ==poiché ognuna gira all’interno di un proprio sistema operativo.== 
>   
>   Nei container, invece, ==l’isolamento è gestito dal motore dei container e **avviene a livello di processo:**== 
> - quindi è tecnicamente più "leggero", anche se comunque sicuro.  
> In condizioni normali, <mark style="background: #E5FF00A6;">App1</mark> non può interagire né sapere dell’esistenza di <mark style="background: #D76E08A6;">App2</mark>, salvo bug o vulnerabilità nel container engine stesso.

Questo approccio ha numerosi **vantaggi pratici**:

- I container sono **più piccoli:** 
	- perché non contengono un intero sistema operativo.
    
- Sono **più economici in termini di risorse**: 
	- ==la [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]], la [[Il modello di Von Neumann#RAM|RAM]] e il disco vengono utilizzati in modo più efficiente rispetto alle VM==.
    
- ==L’avvio di un container è **molto più rapido** rispetto al boot di una macchina virtuale.==
    

- Ma soprattutto, i container offrono una **forte portabilità**: 
	- ==l’applicazione e le sue dipendenze vengono impacchettate in un unico oggetto eseguibile, che può essere facilmente eseguito su qualsiasi macchina che abbia un container engine compatibile==.  
Questo approccio elimina il classico problema dello sviluppatore:

> _“Funziona sul mio computer, ma non sul server di produzione.”_

==Finché l’ambiente in cui si esegue il container supporta il container engine (come Docker), l’applicazione si comporterà **esattamente nello stesso modo**, indipendentemente dal sistema operativo host o dalle configurazioni di sistema==.

Anche con le VM si può ottenere una certa portabilità, ma con un **peso molto maggiore**, perché si trasporta l’intera macchina virtuale con il suo sistema operativo. 
Con i container, invece, si trasporta solo **l’essenziale**: 
- ==l’applicazione e ciò che serve per farla girare==.

In questo modo, agli sviluppatori viene offerta la possibilità di **impacchettare le proprie applicazioni in modo più snello e modulare**, facilitando enormemente il deployment in ambienti diversi, come sviluppo, test e produzione.

### Linux Building Blocks 
Quindi abbiamo detto che i container Docker siano ottimizzati per gli ambienti Linux, ora vediamo come Docker si appoggia sui meccanismi del [[I fundamentals di un Sistema Operativo#Kernel|kernel]] Linux. 
In Linux esistono 3 blocchi fondamentali su cui Docker si appoggia per far funzionare i container: 
1. [[#Namespace|Namespace]] 
2. [[#Control Groups (cgroups)|Control Groups(cgroups)]]
3. [[#Union Mount Filesystems (overlayfs)|Union Filesystem]]
#### Namespace
==Il Namespace è il meccanismo per wrappare (racchiudere) una risorsa globale del sistema.== 
==In questo modo ogni processo di una risorsa in esecuzione che è racchiusa in un namespace non sarà a conoscenza degli altri processi in esecuzione al di fuori del suo namespace.== 
Questo blocco, quindi, consente l'**isolamento** tra i container.
Il kernel Linux espone ai processi una visione delle risorse di sistema (processi, rete, filesystem, ecc.). Con i namespace, è possibile creare **viste isolate e indipendenti** di queste risorse per gruppi di processi diversi.

In pratica: **ogni container vive in un proprio set di namespace**, e quindi "crede" di essere l'unico processo sul sistema, pur condividendo lo stesso kernel.

I namespace principali sono:

| Namespace | Cosa isola                                                 |
| --------- | ---------------------------------------------------------- |
| `PID`     | L'albero dei processi (ogni container ha il proprio PID 1) |
| `NET`     | Interfacce di rete, porte, routing table                   |
| `MNT`     | Il filesystem montato (mount points)                       |
| `UTS`     | Hostname e domain name                                     |
| `IPC`     | Code di messaggi e semafori tra processi                   |
| `USER`    | Utenti e permessi (UID/GID)                                |
>[!example] **Analogia: Namespace** 
>Immagina un'azienda con più **compartimenti separati**. 
>**Ogni dipendente lavora nella propria stanza, si occupa solo della sua mansione e non sa che esistono altri dipendenti nelle altre stanze.** 
>Ogni processo all'interno di un namespace è esattamente così: ==isolato, inconsapevole di tutto ciò che esiste al di fuori del suo spazio.==


#### Control Groups (cgroups)
I **cgroups** risolvono un problema diverso rispetto ai namespace: 
- ==mentre i namespace gestiscono l'**isolamento**, i cgroups gestiscono il **controllo delle risorse**.==
In particolare: 
- ==i cgroups sono una caratteristica del kernel Linux e permettono  di organizzare i processi in gruppi gerarchici i quali usano i vari tipi di risorse che possono essere limitate e monitorate.==

In altre parole: ==i cgroups permettono di **limitare, misurare e prioritizzare** quante risorse hardware un gruppo di processi può consumare.==

Risorse controllabili tramite cgroups:

- **CPU** → ==quanti core o quanta percentuale di CPU può usare il container==
- **RAM** → ==limite massimo di memoria utilizzabile==
- **I/O disco** → ==velocità massima di lettura/scrittura==
- **Rete** → ==banda disponibile==
Quindi usare i cgroups significa specificare una configurazione per un particolare processo o per un gruppo di processi su come essi dovrebbero essere in grado di accedere a quelle particolari risorse di sistema. 
>[!example] **Analogia: Cgroups** 
>I cgroups funzionano come i **cartelli del limite di velocità** su una strada: ==non impediscono alla macchina di esistere né di muoversi, ma stabiliscono un tetto massimo oltre il quale non può andare==. 
>Allo stesso modo, i cgroups non bloccano un processo, ma limitano quante risorse (CPU, RAM, disco) può consumare.

Per comprendere meglio i cgroups scriviamo il CLI: 
```shell
cat /proc/cgroups
```

[![Screenshot-2026-05-01-at-10-55-57-devops-directive-docker-course-02-technology-overview-README-md-at.png](https://i.postimg.cc/c4kf11Pd/Screenshot-2026-05-01-at-10-55-57-devops-directive-docker-course-02-technology-overview-README-md-at.png)](https://postimg.cc/TpmKCxRs)
Ogni riga rappresenta un tipo di risorsa controllabile dal kernel. Le colonne principali sono:


| Colonna        | Siginificato                                   |
| -------------- | ---------------------------------------------- |
| `#subsys_name` | Il nome del sottosistema (es. `cpu`, `memory`) |
| `hierarchy`    | A quale gerarchia appartiene                   |
| `num_cgroups`  | Quanti cgroup esistono per quel sottosistema   |
| `enabled`      | Se è attivo o meno                             |
>[!info] **Sottosistemi notevoli**
>
>- `blkio` → controlla la velocità di lettura/scrittura su disco
>- `freezer` → permette di "congelare" e riprendere un gruppo di processi
>- `pids` → limita il numero massimo di processi che un container può creare
#### Union Mount Filesystems (overlayfs)
L'**Union Filesystem** è la tecnologia che rende le **immagini Docker stratificate ed efficienti**.

L'idea di base è che: 
- ==un filesystem union permette di **sovrapporre più layer (strati) di filesystem** e presentarli all'utente come un unico filesystem coerente, su cui si può operare come se fosse uno solo.==

#####  Come funziona OverlayFS in pratica

Per capire concretamente come Docker gestisce le operazioni sui file, consideriamo questo schema:
[![Screenshot-2026-04-30-at-14-36-18-devops-directive-docker-course-02-technology-overview-README-md-at.png](https://i.postimg.cc/28FGPJdL/Screenshot-2026-04-30-at-14-36-18-devops-directive-docker-course-02-technology-overview-README-md-at.png)](https://postimg.cc/SJRc9gvm)
L'OverlayFS lavora su tre livelli:

- **Lower** → ==i layer read-only dell'immagine (Build Layer + Base Image)==
- **Upper** → ==il Container Layer, l'unico scrivibile==
- **Overlay** → ==la **vista unificata** che il container vede realmente==

Quando il container opera sui file, possono verificarsi tre scenari:

| Operazione                           | Cosa succede                                                          | Risultato nell'Overlay                                                     |
| ------------------------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Lettura** (`file-1`)               | Il file esiste solo nel Lower, viene letto direttamente               | `file-1` appare invariato                                                  |
| **Modifica** (`file-2a` → `file-2b`) | Docker non può toccare il Lower, crea una copia modificata nell'Upper | L'Upper ha la precedenza: l'Overlay mostra `file-2b`                       |
| **Cancellazione** (`file-4`)         | Docker non può eliminare dal Lower, crea un **whiteout** nell'Upper   | Il whiteout dice all'Overlay di ignorare `file-4` — appare come cancellato |

> [!info] **Whiteout**
>  ==Un whiteout è un file speciale creato da Docker nell'Upper layer per **simulare la cancellazione** di un file del Lower. Il file nel Lower esiste ancora fisicamente, ma l'Overlay lo nasconde.==


###### Come funziona con Docker

Quando costruisci un'immagine tramite un Dockerfile, **ogni istruzione crea un nuovo layer read-only**:
```dockerfile
FROM ubuntu:22.04        # Layer 1: OS base
RUN apt-get install java # Layer 2: installazione Java
COPY app.jar /app/       # Layer 3: la tua applicazione
```
Quando si avvia un container, ==Docker aggiunge sopra questi layer read-only un **layer scrivibile** (detto _container layer_), che è l'unico modificabile durante l'esecuzione==:
```text
[ Container layer — scrivibile ]   ← modifiche runtime
[ Layer 3 — app.jar ]   ← read-only
[ Layer 2 — Java ]   ← read-only
[ Layer 1 — Ubuntu 22.04 ]   ← read-only
```


> [!done] **Questo approccio porta numerosi vantaggi pratici:**
> 
> 
> - ==**Efficienza dello spazio**: se più container condividono la stessa immagine base, quel layer viene salvato **una sola volta** su disco.==
> - ==**Build veloci**: se modifichi solo un layer, Docker ricalcola solo quello, riutilizzando i precedenti dalla **cache**.==
> - ==**Portabilità**: l'intera pila di layer costituisce l'immagine che puoi pushare su Docker Hub.==

> [!info] Implementazione concreta Docker usa di default **OverlayFS** (`overlay2`), il driver UnionFS più diffuso su Linux moderno. In passato venivano usati AUFS e DeviceMapper.

>[!example] **Analogia: Union Filesystem** Funziona come **Git**. 
>Ogni commit aggiunge uno strato sopra il precedente senza modificarlo — i commit precedenti sono immutabili. 
>Tu però vedi sempre un'unica versione del progetto, non una lista di diff separati. 
>Con l'UnionFS è uguale: ==ogni layer è read-only e si sovrappone al precedente, ma il container vede tutto come un unico filesystem unificato.==


---
### Installare docker su windows 
Per installare docker su windows è necessario installare anche il docker desktop.
[Per vedere la documentazione officiale per installare docker su windows](https://docs.docker.com/desktop/setup/install/windows-install/)

> [!hint] **Consiglio**
> Cliccare su *" Docker Desktop for windows - x86_64"* per scaricare l'installer del docker desktop


### L'architettura dell'applicazione Docker
Per capire come è strutturato Docker, è utile distinguere i suoi componenti principali. 
La prima distinzione da fare è tra **Docker Desktop** e **Docker Engine**.
[![Screenshot-2026-05-01-at-11-05-25-devops-directive-docker-course-02-technology-overview-README-md-at.png](https://i.postimg.cc/QC1N2mLf/Screenshot-2026-05-01-at-11-05-25-devops-directive-docker-course-02-technology-overview-README-md-at.png)](https://postimg.cc/y36z9F8R)
##### Docker Desktop

==**Docker Desktop** è l'applicazione che si installa sui sistemi di sviluppo (Windows, Mac).== Come abbiamo già visto nella sezione [[#Installare docker su windows|sull'installazione]], Docker Desktop fornisce due macro-componenti:

1. **Client** (lato sviluppatore):
    - **Docker CLI** →==l'interfaccia a riga di comando con cui interagisci con Docker (tutti i comandi `docker run`, `docker ps`, ecc. che abbiamo visto finora)==
    - **GUI** → ==il Docker Desktop che abbiamo usato per visualizzare container e immagini==
    - **Docker Credential Helpers** → ==gestione delle credenziali per accedere ai registry==
    - **Extensions** → ==plugin di terze parti==
2. **Linux Virtual Machine** (lato server):
    - **Docker Daemon** (`dockerd`) → ==il processo centrale che gestisce container, immagini e volumi, esposto tramite le **Docker [[Lezione 6 - API#API (Application Programming Interface)|API]]**== 
    - **(Opzionale) Kubernetes cluster** → ==per orchestrare i container in ambienti più complessi==

>[!note] **Licenza** 
>Docker Desktop è **gratuito per uso personale**, ma richiede una sottoscrizione a pagamento per alcuni casi di uso commerciale.

##### Docker Engine

==**Docker Engine** è il sottoinsieme open source e gratuito di Docker Desktop, installabile **solo su Linux**.== 
Include esclusivamente:

1. ==**Docker CLI**==
2. ==**Docker Daemon** (`dockerd`) con le Docker API==

>[!hint] **Quando usare Docker Engine invece di Docker Desktop?** 
>==Docker Engine è la scelta tipica per i **server di produzione Linux**, dove non serve l'interfaccia grafica né le funzionalità extra di Desktop. ==
>==Docker Desktop è invece pensato per i **sistemi di sviluppo**.==

##### Registry

==I **registry** non fanno parte di Docker stesso, ma sono il meccanismo principale per **archiviare e condividere immagini**.== 
Come abbiamo già visto, il registry ufficiale di Docker è **Docker Hub**, ma ne esistono molti altri (es. GitHub Container Registry `ghcr.io`, Google Container Registry, ecc.).


> [!caution] **Registry Eureka vs. Registry Docker**
> A primo impatto il termine "registry" potrebbe rimandare al concetto di [[Lezione 2 - Architetture dei microservizi#2. Registry|registry]] in Eureka e più generalmente ai microservizi. 
> In realtà il registry docker e il registry dei microservizi sono concetti completamente diversi nonostante condividano il nome. 
> 
>|                    | Docker Registry                   | Service Registry (Eureka)                        |
| ------------------ | --------------------------------- | ------------------------------------------------ |
| Cosa contiene      | **Immagini** container            | **Indirizzi** dei microservizi attivi            |
| Scopo              | Archiviare e distribuire immagini | Permettere ai microservizi di trovarsi a vicenda |
| Quando viene usato | Al momento del **deploy**         | A **runtime**, durante le chiamate tra servizi   |
| Esempio            | Docker Hub, ghcr.io               | Eureka Server                                    |
>
>
>In sostanza:
>
>- Il **Docker Registry** è come una **libreria di CD** — ==ci vai a prendere il software da installare==
>- Il **Service Registry (Eureka)** è come una **rubrica telefonica** — ==ci vai per sapere dove si trova qualcuno in questo momento==
>L'unica cosa in comune è l'idea generica di "registro centralizzato dove cercare qualcosa" — ma il contesto, il contenuto e lo scopo sono completamente diversi.




### La persistenza dei dati nei containers 

Come abbiamo visto nella sezione sull'[[#Union Mount Filesystems (overlayfs)|Union Filesystem]], ogni container in esecuzione ha un **Container Layer** in cima allo stack dei layer — ed è l'unico layer **R/W (Read/Write)**.

Tutti i dati scritti durante l'esecuzione del container (file di log, dati salvati, modifiche al filesystem) finiscono in questo layer.
[![Screenshot-2026-04-30-at-14-04-08-devops-directive-docker-course-04-using-3rd-party-containers-readm.png](https://i.postimg.cc/05VsGtFR/Screenshot-2026-04-30-at-14-04-08-devops-directive-docker-course-04-using-3rd-party-containers-readm.png)](https://postimg.cc/5jQTbmfn)
```txt
[ Container Layer — scrivibile ]   ← creato a runtime con docker run
[ Build Layer 3               ]   ← RUN
[ Build Layer 2               ]   ← COPY
[ Build Layer 1               ]   ← RUN
[ Base Image                  ]   ← FROM
```

>[!ticket] **I dati nei container sono effimeri (ephemeral)** 
>==Quando un container viene fermato e rimosso con `docker rm`, il **Container Layer viene eliminato insieme a lui** — e tutti i dati scritti al suo interno vengono persi in modo permanente.==

Questo è un problema concreto: 
- immaginiamo un container con **PostgreSQL**. ==Se i dati del database finiscono nel Container Layer, ogni volta che il container viene rimosso e ricreato, **tutti i database vengono eliminati**.==
#### La soluzione: montare storage esterno

Per rendere i dati **persistenti**, Docker offre 2 meccanismi che permettono di salvare i dati **al di fuori** del Container Layer effimero:
1. **Bind Mount:**  ^a18577
	-  ==Collega direttamente una cartella del container a una cartella **scelta da te** sul filesystem dell'host.==
	- ==È l'utente a controllare il percorso, ad esempio `/home/users/dati`.==
2. **Volume Mount:**
	-  ==I dati vengono salvati in una cartella **gestita direttamente da Docker**==, nel percorso standard `/var/lib/docker/volumes/`.
	- ==Non è l'utente a scegliere dove, è Docker a gestire quella cartella.==
[![volumes.jpg](https://i.postimg.cc/G3yftXRx/volumes.jpg)](https://postimg.cc/MXz5rbvn)

Analizziamo questa immagine: 
All'interno dell'Host, abbiamo un container dentro la VM del docker desktop, all'interno di questa struttura il container monta(salva) i dati in una cartella gestita direttamente da docker.
Mentre al di fuori di questa struttura i dati vengono salvati in una cartella nel filesystem dell'Host, in un path che può essere deciso dall'utente. 
Grazie quindi a questi due meccanismi Docker garantisce la persistenza dei dati del container, in modo che se il container venisse rimosso l'utente può facilmente recuperare i dati andati persi 

La differenza chiave è quindi **chi gestisce il percorso**:

|                                   | Bind Mount                   | Volume Mount               |
| --------------------------------- | ---------------------------- | -------------------------- |
| Percorso scelto da                | l'utente                     | Docker                     |
| Posizione                         | Qualsiasi cartella dell'host | `/var/lib/docker/volumes/` |
| Dati persistenti dopo `docker rm` | ✅                            | ✅                          |


==In entrambi i casi, i dati **sopravvivono** alla rimozione del container — risolvendo il problema dell'effemeralità del Container Layer.==

####  Installare dipendenze a runtime

Come abbiamo visto, ogni container ha il proprio **Container Layer** separato. 
Questo ha una conseguenza importante: 
- ==tutto ciò che viene installato o modificato a runtime esiste **solo in quel container specifico**.==

Proviamo a dimostrarlo concretamente:
```docker
# Creiamo un container ubuntu interattivo
docker run --interactive --tty --rm ubuntu:22.04

# Proviamo a usare ping
ping google.com -c 1 # ❌ bash: ping: command not found

# Installiamo ping
apt update
apt install iputils-ping --yes

ping google.com -c 1 # ✅ Funziona!
exit
```


- `docker run` → ==crea e avvia un nuovo container==
- `--interactive` (o `-i`) → tiene aperto lo **stdin**, ==permettendoti di scrivere comandi nel container==
- `--tty` (o `-t`) → ==emula un **terminale reale** con prompt, colori e history dei comandi==

> [!remeber] `--interactive` `--tty` vs `-it`
> `--interactive` `--tty` vs `-it`
>**In Linux/Unix è una convenzione generale poter concatenare le flag abbreviate in un'unica stringa.** 
>==Quindi `-it` non è una flag speciale — è solo `-i` e `-t` scritte insieme per comodità.==
>>[!link] Abbiamo già incontrato questa abbreviazione ogni volta che facevamo partire la struttura docker con postgresql: 
>>```docker
>>docker exec -it nome_container bash
>>```

- `--rm` → ==**elimina automaticamente** il container e il suo Container Layer quando fai `exit`==
- `ubuntu:22.04` → immagine da cui creare il container
- `ping google.com -c 1` → ==invia **1 pacchetto** a google.com per testare la connettività. 
	- `-c 1` ==specifica il numero di pacchetti==
- `apt update` → ==aggiorna la lista dei pacchetti disponibili nel container==
- `apt install iputils-ping --yes` → ==installa `ping`. `--yes` conferma automaticamente senza chiedere conferma==
- `exit` → ==esce dal container, che viene eliminato automaticamente grazie a `--rm`==
Ora proviamo a creare un **nuovo** container dalla stessa immagine:
```docker
docker run -it --rm ubuntu:22.04
ping google.com -c 1 # ❌ Fallisce di nuovo!
```

- `docker run -it` → ==forma abbreviata di `--interactive --tty`==
- `--rm` → ==container effimero, eliminato dopo `exit`==
- `ping google.com -c 1` → ==fallisce ❌ perché questo è un **nuovo** Container Layer, separato dal precedente==

>[!faq] **Perché fallisce?** 
>Abbiamo detto che i dati dei container sono effimeri, quindi quando si elimina il container i dati al suo interno vengono rimossi in automatico.
>
>Difatti, in questo caso, ==`ping` era stato installato nel **Container Layer** del primo container. ==
>==Quando quel container è stato rimosso (`--rm`), il suo layer è stato eliminato. Il secondo container ha un **Container Layer nuovo e vuoto** — le modifiche del primo non esistono più.==

##### Riutilizzare lo stesso container

Se vogliamo che le modifiche persistano, possiamo evitare di rimuovere il container e dargli un nome:
```docker
# Creiamo il container SU nome e SENZA --rm
docker run -it --name my-ubuntu-container ubuntu:22.04

# Installiamo ping
apt update
apt install iputils-ping --yes
ping google.com -c 1 # ✅
exit

# Riavviamo lo stesso container
docker start my-ubuntu-container
docker attach my-ubuntu-container

ping google.com -c 1 # ✅ Funziona ancora!
exit

# Verifica che il container esista ancora
docker container ps -a | grep my-ubuntu-container

# Ispeziona i dettagli completi del container
docker container inspect my-ubuntu-container
```

Analizziamo questo snippet:

- `docker run -it --name my-ubuntu-container ubuntu:22.04` → ==crea e avvia un nuovo container interattivo con terminale emulato==
- `--name my-ubuntu-container` → ==assegna un **nome** al container invece dell'ID generato automaticamente da Docker==
- nessun `--rm` → ==il container **non viene eliminato** dopo `exit`, il suo Container Layer rimane su disco con tutte le modifiche==
- `apt update` → ==aggiorna la lista dei pacchetti disponibili nel container==
- `apt install iputils-ping --yes` → ==installa `ping`.== 
	- `--yes` ==conferma automaticamente l'installazione senza chiedere conferma interattiva==
- `ping google.com -c 1` → ==invia **1 pacchetto** a google.com per testare la connettività. ==
	- `-c 1` ==specifica il numero di pacchetti==
- `exit` → ==esce dal container, che si **ferma** ma non viene eliminato==
- `docker start my-ubuntu-container` → ==riavvia il container fermo, preservando il suo Container Layer con `ping` già installato==
- `docker attach my-ubuntu-container` → ==si aggancia al **processo principale** (PID 1) del container già in esecuzione, portandoti dentro il suo terminale==
- `ping google.com -c 1` → **funziona ancora ✅**
	- ==perché stiamo operando sullo **stesso Container Layer** del container precedente==
- `docker container ps -a` → ==lista **tutti** i container, inclusi quelli fermi.== 
	- ==`-a` sta per `--all`==
- `| grep my-ubuntu-container` → ==**filtra** l'output mostrando solo la riga che contiene il nome del nostro containe==r
- `docker container inspect my-ubuntu-container` → ==mostra i dettagli completi del container in formato **[[Lezione 5 - Il Formato JSON#**Struttura di un documento JSON**|JSON]]** (configurazione, volumi montati, rete, variabili d'ambiente)==. 
	- Utile per il debugging

> [!info] **`docker start` vs `docker run`**
>
>- ==`docker run` → crea un **nuovo** container da un'immagine==
>- ==`docker start` → riavvia un container **già esistente**, preservando il suo Container Layer==
>- **`docker container inspect`→** ==Mostra tutti i dettagli del container in formato JSON: configurazione, volumi montati, rete, variabili d'ambiente, ecc. Utile per il debugging.==

###### La soluzione corretta: costruire le dipendenze nell'immagine

Tuttavia, affidarsi a un container specifico per mantenere le dipendenze non è una buona pratica. 
==La soluzione corretta è includere tutto ciò che serve direttamente nell'**immagine**, tramite un Dockerfile:==

```docker
FROM ubuntu:22.04
RUN apt update && apt install iputils-ping --yes
```

- `FROM ubuntu:22.04` → definisce la **Base Image:**
	- ==il punto di partenza dell'immagine.== 
	- ==Crea il primo layer read-only dello stack==
- `RUN apt update && apt install iputils-ping --yes` → ==esegue il comando durante la **build** dell'immagine, creando un secondo layer read-only.== 
	- ==`&&`(AND) garantisce che `apt install` venga eseguito solo se `apt update` ha avuto successo==

```docker
# Build dell'immagine
docker build --tag my-ubuntu-image --<<EOF
FROM ubuntu:22.04
RUN apt update && apt install iputils-ping --yes
EOF

# Ogni container creato da questa immagine avrà già ping installato
docker run -it --rm my-ubuntu-image
ping google.com -c 1 # ✅ Funziona sempre!
```

- `docker build` → ==legge il Dockerfile e costruisce l'immagine layer per layer==
- `--tag my-ubuntu-image` → ==assegna un **nome** all'immagine prodotta, così puoi riferirtici facilmente==
- `--<<EOF ... EOF` → ==sintassi alternativa(EOF = End Of File) per passare il Dockerfile **inline** direttamente nel comando, senza creare un file separato su disco.== 
	- ==Tutto ciò che è tra `<<EOF` e `EOF` viene trattato come contenuto del Dockerfile==
- `docker run -it --rm my-ubuntu-image` → ==crea un container dall'immagine appena costruita con terminale interattivo, eliminandolo dopo `exit`==
- `ping google.com -c 1` → eseguito **dentro il container**, funziona ✅ 
	- ==perché `ping` è stato installato nel layer read-only durante la build — non nel Container Layer effimero==

> [!caution] **`--<<EOF` vs Dockerfile separato** 
> ==Nella pratica reale si usa quasi sempre un **file Dockerfile separato**.== 
> **La sintassi `<<EOF` è utile per esperimenti rapidi o demo, ma per progetti reali avere un Dockerfile dedicato è più leggibile e mantenibile.**

>[!ticket] **Regola generale** 
>==Tutto ciò di cui l'applicazione ha bisogno per funzionare deve essere **costruito nell'immagine**. L'unica eccezione sono le **configurazioni specifiche dell'ambiente** (variabili d'ambiente, file di config), che possono essere fornite a runtime.==

> [!info]
> ####  Docker run, start, attach ed exec a confronto
> 
> Lavorando con i container, è importante distinguere questi quattro comandi che spesso vengono confusi tra loro.
> 1. **`docker run`:**
> 	- ==Crea **e** avvia un nuovo container da un'immagine.== 
> 	- ==Ogni volta che lo usi, stai generando un Container Layer nuovo e separato.==
> ```docker
> docker run -it --name my-ubuntu-container ubuntu:22.04
> ```
> 2. **`docker start`** 
> 	- ==Avvia un container **già esistente** ma fermo, preservando il suo Container Layer con tutte le modifiche precedenti. ==
> 	- ==Il container riparte in background.==
> ```docker
> docker start my-ubuntu-container
> ```
> 
> 3. **`docker attach`** 
> 	- ==Si aggancia al **processo principale** (PID 1) di un container già in esecuzione, portandoti dentro il suo terminale.==
> ```docker
> docker attach my-ubuntu-container
> ```
> 
> >[!warning] **Attenzione** 
> >==Fare `exit` da una sessione `attach` **ferma il processo principale** del container, quindi lo ferma completamente.==
> 
> 4. **`docker exec`** 
> 	- ==Lancia un **processo nuovo** all'interno di un container già in esecuzione, senza toccare il processo principale.==
> ```docker
> docker exec -it my-ubuntu-container bash
> ```
> 
> >[!hint] **Quando usare `exec` invece di `attach`?** 
> >==Quando il container sta già eseguendo un'applicazione (es. PostgreSQL, nginx) e lo si vuole **ispezionare o debuggare** senza interromperne il funzionamento.==
> 
> 



| Comando         | Crea container | Avvia container | Entra nel container     |
| --------------- | -------------- | --------------- | ----------------------- |
| `docker run`    | ✅              | ✅               | ✅ (con `-it`)           |
| `docker start`  | ❌              | ✅               | ❌                       |
| `docker attach` | ❌              | ❌               | ✅ (processo principale) |
| `docker exec`   | ❌              | ❌               | ✅ (processo nuovo)      |
##### Persistere i dati prodotti dall'applicazione

Come abbiamo visto, i dati scritti nel Container Layer vengono persi quando il container viene rimosso. 
Proviamo a dimostrare concretamente il problema dell'efemeralità:
```docker
# Creiamo un container e scriviamo un file al suo interno
docker run -it --rm ubuntu:22.04

mkdir my-data
echo "Hello from the container!" > /my-data/hello.txt

# Verifichiamo che il file esista
cat my-data/hello.txt # ✅
exit

# Creiamo un NUOVO container dalla stessa immagine
docker run -it --rm ubuntu:22.04

cat my-data/hello.txt # ❌ cat: my-data/hello.txt: No such file or directory
```

- `docker run -it --rm ubuntu:22.04` → ==crea un nuovo container interattivo con terminale emulato.== 
	- ==`--rm` lo eliminerà automaticamente dopo `exit`==
- `mkdir my-data` → ==crea una cartella chiamata `my-data` nel **Container Layer** del container corrente==
- `echo "Hello from the container!"` → ==stampa la stringa tra virgolette==
- `>` → ==**redirige** l'output di `echo` nel file specificato invece di stamparlo a schermo==
- `/my-data/hello.txt` → ==percorso assoluto del file da creare. Il file viene scritto nel **Container Layer**==
- `cat my-data/hello.txt` → **legge e stampa il contenuto del file ✅** — ==il file esiste purché ci troviamo ancora nello stesso container==
- `exit` → esce dal container. 
	- ==Poiché c'è `--rm`, il container viene eliminato insieme al suo **Container Layer** — e quindi anche `my-data/hello.txt` viene perso==
- `docker run -it --rm ubuntu:22.04` → ==crea un **nuovo** container dalla stessa immagine, con un Container Layer **nuovo e vuoto**==
- `cat my-data/hello.txt` → **fallisce ❌** 
	- ==perché questo container non ha mai visto quel file — è nato dopo che il container precedente è stato eliminato==

> [!warning] **Questo è il problema dell'efemeralità**
>  ==Il file `hello.txt` non esisteva nell'immagine `ubuntu:22.04` — era stato creato nel Container Layer del primo container. Quando quel container è stato rimosso, il layer è stato eliminato insieme a lui.==


Come abbiamo [[#La persistenza dei dati nei containers|anticipato sopra]], per garantire la persistenza dei dati , oltre il ciclo di vita di un container, Docker offre **3 meccanismi:**

| Tipo                       | Dove vengono salvati i dati                         | Persistenti dopo `docker rm` |
| -------------------------- | --------------------------------------------------- | ---------------------------- |
| [[#^2254ce\|Volume Mount]] | Area gestita da Docker (`/var/lib/docker/volumes/`) | ✅                            |
| [[#^3f26be\|Bind Mount]]   | Cartella scelta da te sul filesystem host           | ✅                            |
| tmpfs Mount                | Memoria RAM                                         | ❌                            |
>[!info] **tmpfs Mount** 
>Questo tipo di Mount, che non abbiamo visto precedentemente,
>==salva i dati temporaneamente in **RAM** invece che su disco.==
>**Di conseguenza i dati spariscono quando il container si ferma.** 
>==Viene usato per dati sensibili temporanei (es. credenziali) che non si vuole lasciare su disco.==

##### **1. Volume Mount**
Abbiamo dimostrato che i dati scritti nel Container Layer vengono persi quando il container viene rimosso. La soluzione è usare un **volume** — ==un'area di storage **esterna** al container, gestita direttamente da Docker.==

Il primo passo è creare il volume:
```docker
# Creiamo un volume named
docker volume create my-volume
```

==Una volta creato, lo montiamo nel container al momento dell'avvio.== 
Docker offre due sintassi equivalenti:
```docker
# Montiamo il volume nel container (Sintassi estesa)
docker run -it --rm --mount source=my-volume,destination=/my-data/ ubuntu:22.04

# Sintassi breve equivalente
docker run -it --rm -v my-volume:/my-data ubuntu:22.04
```

Ora tutto ciò che scriviamo in `/my-data/` non finisce nel Container Layer effimero, ma **nel volume**:
```docker
echo "Hello from the container!" > /my-data/hello.txt
exit
```
Anche dopo che il container viene eliminato, il file persiste. Possiamo verificarlo montando lo stesso volume in un nuovo container:
```docker
docker run -it --rm --mount source=my-volume,destination=/my-data/ ubuntu:22.04
cat my-data/hello.txt # ✅ Il file esiste ancora!
exit
```


>[!help] **Dove si trovano fisicamente i dati?** 
>==Su Linux i dati si trovano in `/var/lib/docker/volumes/`.== 
>Su **Docker Desktop (Windows/Mac)**, Docker gira su una VM Linux interna — ==quindi i dati si trovano nel filesystem di quella VM, non direttamente sull'host.==

**È possibile ispezionare fisicamente il filesystem della VM Linux interna usando un container privilegiato:**
```docker
docker run -it --rm --privileged --pid=host justincormack/nsenter1@sha256:5af0be5e42ebd55eea2c593e4622f810065c3f45bb805eaacf43f08f3d06ffd8
```

Una volta dentro, si può navigare nel volume e verificare che i dati siano fisicamente lì:
```shell
ls /var/lib/docker/volumes/my-volume/_data
cat /var/lib/docker/volumes/my-volume/_data/hello.txt # ✅ I dati sono qui!
```

> [!warning] **Attenzione** 
> ==Questo container gira in modalità **privilegiata** con accesso root alla VM Linux di Docker. Usarlo solo quando strettamente necessario e solo con immagini di cui ci si fida.==

> [!info] **Perché pinniamo l'hash dell'immagine?** 
> ==Il flag `@sha256:...` garantisce che venga eseguita **esattamente** quella versione dell'immagine, non una versione aggiornata potenzialmente modificata. È una buona pratica di sicurezza per immagini privilegiate.==

Un caso d'uso concreto che già conosciamo è **PostgreSQL:** 
- ==Finora avevamo sempre riavviato lo stesso container con `docker start` per non perdere i dati.== 
- ==Con un volume, possiamo eliminare e ricreare il container quante volte vogliamo== — i dati del database sopravvivono:
```docker
# Il volume pgdata persiste i dati del database anche se il container viene rimosso
docker run -it --rm -v pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=foobarbaz postgres:15.1-alpine
```
>[!info] **`-e POSTGRES_PASSWORD=foobarbaz`** 
>==Il flag `-e` passa una **variabile d'ambiente** al container. In questo caso imposta la password dell'utente root di PostgreSQL — obbligatoria per avviare il container postgres.==

##### **2. Bind Mount**

A differenza del Volume Mount — dove è **Docker** a gestire dove i dati vengono salvati — il Bind Mount ti permette di: 
- ==scegliere **tu** una cartella specifica sul filesystem dell'host da collegare direttamente al container.==

Anche qui Docker offre due sintassi equivalenti:
```docker
# Sintassi estesa
docker run -it --rm --mount type=bind,source="${PWD}"/my-data,destination=/my-data ubuntu:22.04

# Sintassi breve equivalente
docker run -it --rm -v ${PWD}/my-data:/my-data ubuntu:22.04
```


> [!NOTE] **Nota:**
> Siccome con il Bind Mount è l'utente ha gestire tutta la configurazione è necessario la creazione della cartella `my-data`, prima di montare il volume in un qualsiasi container
>```docker
> mkdir my-data
>```
>Questo perché con il Volume Mount, come abbiamo già detto, la configurazione viene gestita interamente dalla VM di Docker Desktop mentre con il Bind Mount la cartella dei dati deve essere creata dall'utente prima che il container venga montato


Tutto ciò che scriviamo in `/my-data/` dentro il container viene salvato **direttamente sul filesystem dell'host**:
```docker
echo "Hello from the container!" > /my-data/hello.txt
exit

# Il file è visibile direttamente sull'host!
cat my-data/hello.txt # ✅
```
Nota che l'ultimo `cat` viene eseguito **fuori dal container** — ==direttamente nel terminale dell'host.== 
==Il file è visibile perché non è mai finito nel Container Layer, ma nella cartella dell'host che avevamo collegato.==
>[!tip] **Volume Mount vs Bind Mount: quale usare?**
>||Bind Mount|Volume Mount|
|---|---|---|
|**Gestito da**|Te|Docker|
|**Percorso**|Scelto da te|`/var/lib/docker/volumes/`|
|**Visibilità diretta dall'host**|✅|❌|
|**Consigliato per**|Sviluppo|Produzione|
>
>Il **Bind Mount** è comodo durante lo **sviluppo** perché: 
>- ==puoi vedere e modificare i file direttamente dall'host senza entrare nel container.==.
>
>Il **Volume Mount** è **preferibile in produzione**: 
> - ==è più veloce, più portabile e interamente gestito da Docker.==


### Use Cases: Database containerizzati
Ora che abbiamo capito come funzionano volumi e mount, possiamo applicare questi concetti a uno dei casi d'uso più comuni nei container: i **database**.

**Installare e configurare un database è notoriamente complesso — le istruzioni variano tra versioni e sistemi operativi, e mantenere più versioni dello stesso database sulla stessa macchina è spesso un problema.** 
Con Docker, tutta la complessità di installazione è gestita dall'immagine: 
- ==basta fornire alcune variabili di configurazione e il database è pronto.==

Quando si esegue un database in un container, ci sono tre considerazioni fondamentali:

1. **Volume Mount per i dati**: 
	- ==i database salvano i propri dati in percorsi specifici del container. ==
	- ==È necessario montare un volume su quei percorsi per garantire che i dati persistano anche se il container viene rimosso.==
2. **Bind Mount per la configurazione**: 
	- ==i database spesso usano file di configurazione per modificare il comportamento a runtime. ==
	- ==Con un [[#^a18577|bind mount]] puoi creare il file sull'host e montarlo nel percorso corretto del container.==
3. **Variabili d'ambiente**: 
	- ==molti database usano variabili d'ambiente per la configurazione di base (es. la password dell'amministratore). ==
	- ==Si passano con il flag `-e`.==

Vediamo i comandi per i database più comuni:
###### PostgreSQL
**Commando base**
```docker
docker run -d --rm \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=foobarbaz \
  -p 5432:5432 \
  postgres:15.1-alpine
```

- `docker run -d` → ==avvia il container in **background** (detached mode) — il container gira ma non occupa il terminale==
- `--rm` → ==elimina il container automaticamente quando viene fermato==
- `-v pgdata:/var/lib/postgresql/data` → ==monta il volume `pgdata` nel percorso dove PostgreSQL salva fisicamente i dati del database==
- `-e POSTGRES_PASSWORD=foobarbaz` → ==passa la **password dell'utente root** di PostgreSQL come variabile d'ambiente==
- `-p 5432:5432` → ==espone la porta 5432 del container sulla porta 5432 dell'host — quella standard di PostgreSQL==
- `postgres:15.1-alpine` → ==immagine di PostgreSQL versione 15.1 basata su **Alpine Linux**, una distribuzione Linux ultra-leggera pensata per i container==
**Comando con file di configurazione custom:**

```docker
docker run -d --rm \
  -v pgdata:/var/lib/postgresql/data \
  -v "${PWD}/postgres.conf:/etc/postgresql/postgresql.conf" \
  -e POSTGRES_PASSWORD=foobarbaz \
  -p 5432:5432 \
  postgres:15.1-alpine -c 'config_file=/etc/postgresql/postgresql.conf'
```

Come possiamo notare non cambia molto  al comando base, eccetto per due aggiunte:
- `-v "${PWD}/postgres.conf:/etc/postgresql/postgresql.conf"` → ==**bind mount** che collega un file di configurazione custom creato sull'host nel percorso esatto dove PostgreSQL si aspetta di trovarlo dentro il container==
- `-c 'config_file=/etc/postgresql/postgresql.conf'` → ==dice esplicitamente a PostgreSQL di **usare quel file di configurazione** all'avvio==

###### MongoDB
```docker
docker run -d --rm \
  -v mongodata:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=foobarbaz \
  -p 27017:27017 \
  mongo:6.0.4

# Con file di configurazione custom
docker run -d --rm \
  -v mongodata:/data/db \
  -v "${PWD}/mongod.conf:/etc/mongod.conf" \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=foobarbaz \
  -p 27017:27017 \
  mongo:6.0.4 --config /etc/mongod.conf
```

###### Redis
```docker
docker run -d --rm \
  -v redisdata:/data \
  redis:7.0.8-alpine

# Con file di configurazione custom
docker run -d --rm \
  -v redisdata:/data \
  -v "${PWD}/redis.conf:/usr/local/etc/redis/redis.conf" \
  redis:7.0.8-alpine redis-server /usr/local/etc/redis/redis.conf
```

###### MySQL
```docker
docker run -d --rm \
  -v mysqldata:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=foobarbaz \
  -p 3306:3306 \
  mysql:8.0.32
```

> [!warning] **Attenzione ai percorsi dei volumi**
>  ==I percorsi dove ogni database salva i propri dati sono specifici per ciascun database e versione.== 
>  **Prima di usare questi comandi in produzione, verifica sempre sulla documentazione ufficiale del database che il percorso del volume sia corretto**.

> [!info] **Cambiare versione del database** 
> ==Con Docker, passare da una versione all'altra del database è semplice come cambiare il **tag** dell'immagine.==
>  Ad esempio per PostgreSQL:
>```docker
>  postgres:14.6  # versione 14
>  postgres:15.1  # versione 15
>```


###  Ambienti di Test Interattivi

Un altro caso d'uso molto comune dei container è la creazione di **ambienti di test interattivi** — ==container temporanei che si avviano, si usano e si eliminano senza lasciare traccia sul sistema host.==

> [!done] **Questo è particolarmente utile quando vuoi testare qualcosa in un ambiente pulito senza installare nulla sulla tua macchina.**
> 

#### 1. Sistemi Operativi

Puoi avviare un container con un sistema operativo completo e interagire con esso come se fosse una macchina virtuale, ma in modo molto più leggero:
```docker
# Ubuntu 22.04
docker run -it --rm ubuntu:22.04

# Debian in versione slim (più leggera)
docker run -it --rm debian:bullseye-slim

# Alpine Linux - distribuzione ultra-leggera pensata per i container
docker run -it --rm alpine:3.17.1

# BusyBox - immagine minimale con molte utility di sistema preinstallate
docker run -it --rm busybox:1.36.0
```


>[!faq] **Perché `-it --rm`?** 
>==Come abbiamo già visto, `-it` apre un terminale interattivo nel container, mentre `--rm` lo elimina automaticamente dopo `exit` — perfetto per sessioni di test temporanee che non devono lasciare traccia.==

#### 2. Runtime di Programmazione

Allo stesso modo, puoi avviare un container con un runtime di programmazione specifico — ==utile quando vuoi testare codice in una versione specifica di Python, Node.js o altri linguaggi senza installarli sull'host==:
```docker
# Python 3.11.1 - avvia direttamente il REPL interattivo
docker run -it --rm python:3.11.1

# Node.js 18.13.0 - avvia direttamente la console Node
docker run -it --rm node:18.13.0

# PHP 8.1
docker run -it --rm php:8.1

# Ruby su Alpine Linux - versione leggera
docker run -it --rm ruby:alpine3.17
```

>[!hint] **Caso d'uso pratico** 
>==Immagina di dover testare velocemente uno script Python 3.11 senza averlo installato sul tuo PC. Con Docker basta un `docker run -it --rm python:3.11.1` e hai immediatamente un REPL Python pronto all'uso — e quando esci, non rimane nulla sul tuo sistema.==

###  CLI Utilities: eseguire strumenti a riga di comando senza installarli

Dopo aver visto come creare **ambienti di test interattivi** con interi sistemi operativi o runtime di programmazione, esploriamo un caso d’uso ancora più leggero ma estremamente pratico: 
- ==**eseguire singoli utility CLI all’interno di container usa‑e‑getta**.==

Quante volte ti è capitato di dover usare un comando come `jq`, `yq`, `base64` o `sed` e scoprire che:

- **la versione installata sul tuo sistema è troppo vecchia (o troppo nuova) e si comporta diversamente;**
    
- **il comando non è affatto installato e non vuoi ingombrare la tua macchina con strumenti che userai una sola volta;**
    
- **sei su Windows (WSL o non) e vorresti usare un’utility tipicamente Linux senza configurare nulla?**
    

Docker risolve elegantemente questi problemi: 
- ==**puoi eseguire la utility dentro un container** – leggi i dati dallo stdin (o da un file) e ottieni l’output nel tuo terminale.== 
==Il container viene creato al volo, esegue il comando e poi viene rimosso (`--rm`), lasciando il tuo sistema **perfettamente pulito**.==

>[!important] **Il trucco sta nel reindirizzamento dell’input.** 
>==Con `docker run -i` (o `--interactive`) lo stdin del container viene collegato al tuo terminale, quindi puoi **passare il contenuto di un file** usando `<` oppure **incollare direttamente l’output di un altro comando** tramite [[Linux#Pipeline|pipe]] (`|`).==

#### 1. `jq` – l’elaboratore JSON da riga di comando

`jq` è: 
- ==uno strumento indispensabile per filtrare, trasformare e estrarre dati da file [[Lezione 5 - Il Formato JSON#**Struttura di un documento JSON**|JSON]].== 
Invece di installarlo sulla tua macchina, lo lanci in un container.

> [!warning] **Attenzione all’immagine `stedolan/jq`**  
> L’immagine storica `stedolan/jq` su Docker Hub è ormai deprecata (usa lo schema 1, non più supportato dai Docker recenti). 
> Quindi è consigliabile usare l’immagine ufficiale dal GitHub Container Registry: `ghcr.io/jqlang/jq`.

**Esempio base:** 
supponiamo di avere il file `sample-data/test.json` con questo contenuto:
```json
{"key1": "Ciao ", "key2": "Mondo"}
```

Per concatenare i due valori:
```docker
docker run --rm -i ghcr.io/jqlang/jq < sample-data/test.json '.key1 + .key2'
```

Output:
```text
"Ciao Mondo"
```

**Spiegazione del comando:**

- `--rm` → ==il container viene eliminato dopo l’esecuzione.==
    
- `-i` → ==mantiene aperto lo stdin, così possiamo redigere il file.==
    
- `< sample-data/test.json` → ==il contenuto del file viene **iniettato** nello stdin del container.==
    
- `'.key1 + .key2'` → ==il filtro `jq` da applicare ai dati.==
    

Se vuoi passare i dati **via [[Linux#Pipeline|pipe]]** (ad esempio dall’output di un altro comando):
```shell
echo '{"key1": "Ciao ", "key2": "Mondo"}' | docker run --rm -i ghcr.io/jqlang/jq '.key1 + .key2'
```

>[!link] **Ricorda:** 
>con la pipe non serve il ri-direzionamento `<`, perché `echo` scrive direttamente sullo stdout che viene incanalato nello stdin del container.

#### 2. yq – per file YAML

==`yq` è l’equivalente di `jq` ma per YAML.== 
**L’immagine di riferimento è `mikefarah/yq`.**

Esempio con `sample-data/test.yaml`:
```yaml
key_1: "Hello "
key_2: "World"
```

```shell
docker run --rm -i mikefarah/yq < sample-data/test.yaml '.key_1 + .key_2'
```

Output:
```txt
Hello World
```


#### 3. sed – attenzione alle differenze tra GNU sed e BSD sed

==Molti sviluppatori che passano da Linux a macOS scoprono che `sed` si comporta in modo leggermente diverso (soprattutto con l’opzione `-i` per la modifica in-place).== 
Per essere sicuri di usare la **versione GNU**, basta eseguirla dentro un container `busybox`.

**Esempio:** 
==**sostituire tutte le occorrenze di `file.` con `file!` in un file di testo.**==
```docker
docker run -i --rm busybox:1.36.0 sed 's/file./file!/g' < sample-data/test.txt
```
- ==`busybox` è un’immagine minimalissima (qualche MB) che contiene una corposa suite di utility UNIX, tra cui `sed`, `grep`, `awk`, `base64`, ecc.==

#### 4. base64 – coerenza tra piattaforme

==Anche `base64` ha piccole differenze tra GNU e BSD.== 
Per esempio, **GNU `base64` va a capo dopo 76 caratteri, mentre la versione macOS non lo fa (di default).** 
Per avere un comportamento **prevedibile**:
```docker
echo "Stringa sufficientemente lunga da andare a capo nel GNU base64" | docker run -i --rm busybox:1.36.0 base64
```

In alternativa, codificare il contenuto di un file:
```docker
docker run -i --rm busybox:1.36.0 base64 < sample-data/test.txt
```


#### 5. CLI dei cloud provider (AWS, GCP)

Un caso d’uso molto diffuso è quello di eseguire i comandi `aws` o `gcloud` senza installare gli SDK sulla macchina locale. L’unico accorgimento è **montare le credenziali** (e la configurazione) dentro il container, usando un [[#^a18577|bind mount]].

###### AWS CLI

L’immagine ufficiale è `amazon/aws-cli`. 
Supponendo che tu abbia già configurato `~/.aws` con le tue credenziali:
```docker
docker run --rm -v ~/.aws:/root/.aws amazon/aws-cli:2.9.18 s3 ls
```

- `-v ~/.aws:/root/.aws` → ==monta la cartella `.aws` dell’host nel percorso `/root/.aws` del container (dove `aws-cli` cerca le credenziali).==
    
- ==Il comando successivo (`s3 ls`) è il sottocomando AWS che vuoi eseguire.==
    

> [!info] Puoi usare qualsiasi comando AWS, ad esempio `aws ec2 describe-instances` – tutto funziona esattamente come se avessi installato l’AWS CLI.

###### Google Cloud CLI

L’immagine ufficiale è sul Google Container Registry: 
- `gcr.io/google.com/cloudsdktool/google-cloud-cli`. 
Anche qui monti la cartella delle credenziali:
```docker
docker run --rm -v ~/.config/gcloud:/root/.config/gcloud gcr.io/google.com/cloudsdktool/google-cloud-cli:415.0.0 gsutil ls
```

>[!caution] **Attenzione alla dimensione dell’immagine!**  
>==L’immagine `google-cloud-cli` è **enorme** (~2,8 GB) perché contiene tutto l’SDK Google Cloud.== 
>Se devi usarla spesso, considera di creare un’immagine più leggera su misura, oppure di installare `gcloud` nativamente. 
>Per un uso occasionale, comunque, il container rimane una soluzione valida.


### Migliorare l’esperienza d’uso (Ergonomics)

Abbiamo visto come eseguire utility CLI all’interno di container usa‑e‑getta. 
Il metodo funziona, ma digitare ogni volta un comando lungo come:
```docker
docker run --rm -i -v ${PWD}:/workdir mikefarah/yq < file.yaml '.chiave'
```

diventa rapidamente **tedioso**, specialmente se usi spesso `jq`, `yq` o `aws-cli`.

L’obiettivo è **far sì che il programma dentro il container si comporti il più possibile come se fosse installato nativamente sulla tua macchina** – stesso nome, stessi argomenti, supporto a pipe e reindirizzamenti.

La shell (bash, zsh, fish) ci offre due meccanismi per incapsulare il comando Docker in modo trasparente: 
1. **funzioni** 
2. **alias**.

####  1. Funzione shell

Una funzione può racchiudere qualsiasi comando. La sintassi generica per il nostro caso è:
```shell
nome-funzione() {
  docker run --rm -i -v ${PWD}:/workdir immagine "$@"
}
```

- `"$@"` → ==si espande in **tutti gli argomenti** passati alla funzione, preservando spazi e quoting.== 
In pratica, ==tutto ciò che scrivi dopo il nome della funzione viene passato esattamente così al comando Docker.== 

**Esempio concreto per `yq`**:
```shell
yq-shell-function() {
  docker run --rm -i -v ${PWD}:/workdir mikefarah/yq "$@"
}
```

Una volta definita, la usi esattamente come se fosse `yq` installato localmente:

```shell
yq-shell-function <sample-data/test.yaml '.key_1 + .key_2'
```

>[!info] **A cosa serve `-v ${PWD}:/workdir`?**  
>==Monta la directory corrente dell’host (`$PWD`) dentro il container nel percorso `/workdir`.== 
>==Se in futuro volessi passare un _file_ come argomento (invece di usare solo lo stdin), il programma lo troverà dentro `/workdir`.==  
>>[!note] **Con il solo `<` (re-direzione dello stdin) non serve, ma per coerenza e flessibilità molti esempi lo includono.**

####  2. Alias

==Un alias è più semplice, ma anche più limitato rispetto a una funzione.== 
Si definisce così:
```shell
alias 'yq-alias=docker run --rm -i -v ${PWD}:/workdir mikefarah/yq'
```

Uso:

```shell
yq-alias <sample-data/test.yaml '.key_1 + .key_2'
```

**Differenze sostanziali:**

- ==L’alias viene **espanso testualmente** dalla shell prima di interpretare il resto della riga.==
    
- ==Non puoi inserire logica complessa (if, cicli, variabili locali).==
    
- ==Non sempre gestisce correttamente argomenti con spazi o caratteri speciali.==
    

> [!done] **Per il semplice wrapper di un comando Docker, l’alias _funziona_, ma la funzione è più robusta e consigliata.**
> 

### Come si crea un container 

Ora che abbiamo capito come funziona l'[[#Union Mount Filesystems (overlayfs)|Union Filesystem]] e la struttura a layer, possiamo capire concretamente come nasce un container.

Il punto di partenza è sempre una **immagine container** — ==un file che descrive staticamente tutti i passaggi necessari per costruire un ambiente eseguibile.== 
Contiene informazioni come:

- ==il sistema operativo di base (es. Ubuntu 22.04, Alpine, Debian)==
- ==le dipendenze dell'applicazione (es. Node.js, Java, Python)==
- ==l'applicazione stessa (es. file `.jar`, `.py`, `.js` ecc.)==
- ==eventuali comandi da eseguire all'avvio==

==Questa immagine viene definita all'interno di un **Dockerfile**, un file di testo che funge da vera e propria "ricetta" per creare il container.== 
Una volta scritto il Dockerfile, si esegue il comando di build:
```docker
docker build -t nome-immagine .
```

Il Docker Engine leggerà il Dockerfile riga per riga, e **costruirà un layer read-only per ogni istruzione**, come abbiamo visto nella sezione sull'[[#Union Mount Filesystems (overlayfs)|Union Filesystem]]. 
==Quando questa immagine viene eseguita con `docker run`, Docker aggiunge il **Container Layer scrivibile** in cima allo stack — ed è in quel momento che l'immagine diventa un container.==

> [!example] Analogia con la programmazione OOP
> Il Dockerfile è come una **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi|classe Python]]:**  
>- l'immagine è come la **definizione della classe**,  
>- e il container è **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#Istanze di una classe|l'istanza reale]]**, ovvero l'oggetto in memoria.

Inoltre, le immagini create localmente possono essere **pubblicate su registry remoti**, in modo da essere condivise o riutilizzate su altri ambienti. Il più noto è [Docker Hub](https://hub.docker.com/repositories), una registry pubblica gratuita per uso personale, dove si possono trovare migliaia di immagini ufficiali e di terze parti.
>[!info] **Le immagini sono immutabili**
>==Una volta costruita, un'immagine **non cambia mai**. Se modifichi il Dockerfile e rifai la build, ottieni una **nuova immagine** — quella vecchia rimane intatta. Questo garantisce che lo stesso container si comporti sempre in modo identico su qualsiasi macchina.==

>[!abstract] **WSL e container Docker** **WSL** (Windows Subsystem for Linux) 
>==è un sottosistema che integra un [[I fundamentals di un Sistema Operativo#Kernel|kernel]] Linux reale all'interno di Windows.== 
>In pratica, ==vive affiancato al sistema operativo Windows e permette di eseguire ambienti Linux nativi senza la necessità di installare una macchina virtuale tradizionale.==
>
>Sebbene Windows supporti anche container nativi Windows, nella pratica la tecnologia di containerizzazione dà il meglio di sé in ambienti Linux, perché è nata lì ed è ottimizzata per quel contesto. Infatti, la stragrande maggioranza dei container Docker eseguiti nel mondo reale sono container **Linux**, anche quando vengono lanciati da un computer con sistema operativo Windows.
>
>==Per questa ragione, quando si installa Docker Desktop su Windows, esso si **appoggia a WSL2** per offrire un ambiente Linux in cui i container possano funzionare nativamente e con prestazioni elevate.==
>
>![[La vera struttura di docker.png]]


### Docker run e Docker pull
Questi due comandi sono utili per capire il flusso di lavoro con Docker.

1. `docker run`: 
	- ==Crea e avvia un **container** a partire da un’immagine.==  
	- ==Se l’immagine non è già presente in locale, **Docker la scarica automaticamente.**==
2. `docker pull`: 
	- ==Scarica un’immagine da un **registry** (di default Docker Hub) verso il tuo computer ma non la esegue.==


> [!example] **Esempio:**
> Proviamo ora a scrivere 
>```docker
>docker run hello-world
>```
>
>- Docker cerca localmente l’immagine `hello-world`.
  >  
>- Non la trova → fa automaticamente il **pull** dal Docker Hub.
 >   
>- Una volta scaricata, crea un **container** dall’immagine.
>    
>- Lo avvia, che stampa il messaggio di benvenuto, poi si chiude.
>
>Mentre  con il comando 
>```docker
>docker pull
>```
>
>Cosa succede:
>
>1. Docker scarica (o aggiorna) l’immagine `hello-world` dal Docker Hub.
  >  
 >   - Se ce l’hai già in locale, la controlla e può riscaricarla se ci sono aggiornamenti.
  >      
>2. Nessun container viene creato o avviato.
>   
>  ### Differenza
>- `docker run` = usa l’immagine per creare un container ed eseguirlo (e se serve fa anche il pull).
 >   
>- `docker pull` = **scarica solo l’immagine** senza avviare nulla.
>



## Concetti basi di Docker
Prima di imparare i comandi di Docker, dobbiamo comprendere alcuni concetti fondamentali.
### 1. Docker container vs. Docker Images

Per capire come lavora Docker, è importante distinguere tra **immagini** e **container**.

- Nel tab **Containers** di Docker Desktop vediamo i container attivi o già eseguiti.

![[Docker Containers.png]]
    
- Nel tab **Images** vediamo invece le immagini disponibili localmente. 
![[Docker Images.png]]


Come possiamo vedere ci sono diversi container, in particolare 3,  con l'immagine hello world, ma se ci spostiamo nella tab *"Images"* notiamo una sola immagine `hello world`. 
Questo perché: 
Se eseguiamo più volte `docker run hello-world`, in **Containers** compariranno più container, ma in **Images** vedremo sempre e solo **una** immagine `hello-world`



#### Relazione tra immagini e container 
**Le immagini, di fatto, sono come dei template per i containers:** 
- Specificano: 
	- ==Il contenuto di un file system==
	- ==che applicazioni ha installato l'utente== 
	- ==variabili di ambiente==
	- ==E il comando di default che farà partire il container.==
Quindi possiamo pensare a una immagine come: 
- ==un recipiente per eseguire una applicazione.==

I container dall'altro canto sono: 
- ==il gruppo di processi che vengono lanciati ed seguono le istruzioni specificate nell'immagine docker.==

Quindi ==ogni volta che si esegue un immagine docker essa crea in automatico un nuovo container basato sul quell'immagine.== 
Quindi è possibile avere più container, anche basati sulla stessa immagine, in esecuzione in quel momento. 
Come abbiamo detto sul docker desktop vi sono le tab images e containers che mostrano le immagini o i container, oppure per vedere solo le immagini presenti si può eseguire il CLI
```docker 
docker image ls
```

Mentre per vedere i container in esecuzione il CLI è
```docker
docker ps
```
^dockerPs

> [!info] Se invece si volesse vedere tutti i docker, non solo in esecuzione ma anche quelli: 
> - **fermati**
> - **usciti** (es. `hello-world` dopo aver stampato il messaggio)
> - **In errore**
> - **creati ma mai avviati** 
>```docker
> docker ps -a
>```
>
>> [!hint] Per rimuovere rapidamente i container 'morti' che restano elencati in `docker ps -a` 
>>```
>> docker rm <container_id>
>>```
>>
>>1. Rimuovere un container specifico
>>Per rimuovere un container fermo (ad esempio con ID `7a1b2c3d4e5f`)
>>```docker
>>docker rm 7a1b2c3d4e5f 
>>```
>>
>>Cancella solo quel container.
>>
>>2. Rimuovere più container
>>Ovviamente a questo comando possiamo associare più ID di diversi container 
>>```docker
>>docker rm 7a1b2c3d4e5f ab12cd34ef56
>>
>>```
>>
>>3. Rimuovere tutti i container fermi
>>  Tuttavia può risultare verboso eliminare tutti i container fermi ID per ID, Docker ci viene in aiuto offrendoci il comando 
>>```
>> docker container prune 
>>```
>>
>>Elimina solo tutti i container fermi in una volta sola: 
>>- Spesso dopo prove con `hello-world` o `ubuntu` restano decine di container “Exited”, di conseguenza questo comando permette di eliminare tutti i container fermi.
>>Dopo la sua esecuzione chiede la conferma dell'azione: 
>>```docker
>>WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N]
>>
>>```
>>==Utile quando si fanno tanti test e si vuole fare pulizia velocemente.==
>>
>>4. Rimuovere forzatamente  i container anche se attivi
>> Se si volesse eliminare direttamente un container ancora in esecuzione 
>>```
>> docker rm -f <container_id>
>>```
>>
>>Fa prima uno stop e poi lo rimuove. 
>>
>>5. Pulizia totale
>>  Se si volesse fare pulizia completa di container, immagini e volumi non usati
>>```docker
>> docker system prune -a
>>```
>>
>>
>>> [!caution] Attenzione: elimina tutto ciò che non è in uso, incluso immagini non collegati a container
>>> ==Utile quando si vuol fare "reset pulizia" quasi totale.==


> [!info] Per vedere solo gli ID dei container (utile negli script)
>```docker
> docker ps -q
>```


### Port mapping in Docker

Per spiegare questo concetto usiamo  `nginx` web server: 
- È disponibile pubblicamente nel [dockerhub](https://hub.docker.com/_/nginx)
- ==È il registro dell'immagine di default del docker uses se non viene specificato esplicitamente== 
Ovvero quando, ad esempio lanciamo il comando: 
```docker
docker run nginx
```

Docker deve andare a recuperare l'immagine `nginx` 
Ma da dove la prende? 
Se non si specifica il registro, Docker per default va a cercarla su **Docker Hub**:   
- ==è il registro ufficiale pubblico delle immagini.==  ^dockerHub

Quindi scrivere: 
```docker
docker run nginx
```

è equivalente a scrivere in modo esplicito: 
```docker
docker run docker.io/library/nginx
```

Dove: 
-  `docker.io` → ==indica Docker Hub==
    
- `library` → ==namespace predefinito per le immagini ufficiali (come nginx, ubuntu, redis, ecc.).==
Quindi se eseguiamo un immagine senza specificare il registro ( `docker.io`, `ghcr.io`, `quay.io`, ecc.), Docker userà **Docker Hub** come registro predefinito andando a scaricare ,in questo caso, l'immagine `nginx` da lì.

In ogni caso, quando esegui:

```docker
docker run nginx
```

- Docker crea un **container isolato** con `nginx`.
    
- Nel Docker Desktop, alla tab **Containers**, vedrai il container in esecuzione.
    
- **Ma se si prova ad accedere a `http://localhost` dal browser**, non verrà visualizzato nulla.
Questo perché: 
-  ==I container **per default non espongono le porte all’host**.==
    
- ==Il container gira in un **network isolato**, quindi l’host non può comunicare direttamente con il server `nginx`.==

#### Come rendere accessibile `nginx` all'host
Per comunicare con `nginx` server dobbiamo pubblicare la porta in modo che l'host possa vederla.
In altre parole fare il port mapping: 
- ==cioè “pubblicare” una porta del container su una porta dell’host.==
Per fare ciò dobbiamo andare sul terminale: 
Interrompere il download di `nginx`
```shell
CTRL + c
```

Ed eseguire il comando 
```docker
docker run -p <host_port>:<container_port> nginx
```

- `<container_port>` → porta su cui l’applicazione gira dentro il container (nginx usa 80)
    
- `<host_port>` → porta che vuoi esporre sul tuo computer.

###### Esempio pratico: 

```docker
docker run -p 80:80 nginx
```

Ad esempio mettiamo che il `<port_number>` sia `80:80`
- La porta 80 del tuo PC sarà collegata alla porta 80 del container.
    
- Ora, aprendo `http://localhost` nel browser, vedrai la pagina: **“Welcome to nginx!”**.

> [!important] **Nota Pratica:** 
> Nel caso che la porta 80 del host sia già occupata (es: da un altro server), si possono usare altre porte, per esempio: 
>```
> docker run -p 8080:80 nginx
>```
>
>- Ora l’host porta 8080 → container porta 80
 >   
>- Aprendo `http://localhost:8080` vedrai il sito `nginx`.
>  
>> [!abstract]- Spiegazione del host port e container port
>> 1. **Container port**
  >>  
>>- ==È la porta **su cui l’applicazione dentro il container sta ascoltando**.==
  >>  
>>- ==Nel caso di `nginx`, di default **nginx ascolta sulla porta 80**, quindi **il container port deve essere 80** se non modifichi la configurazione interna di nginx.==
>>    ^containerPort
 >>   
>>
>>2. **Host port**
  >>  
>>
>>- ==È la porta sul tuo computer (host) a cui vuoi collegare il container.==
  >>  
>>- ==Può essere **qualsiasi porta libera**, ad esempio 8080, 3000, ecc.==
  >>  
>>- ==Serve per evitare conflitti se la porta 80 è già occupata da un altro servizio sul PC.==
>>    ^hostPort
>

### 3.Eseguire container in background
