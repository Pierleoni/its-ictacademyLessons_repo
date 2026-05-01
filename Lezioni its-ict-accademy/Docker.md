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
1. Namespace 
2. Control Groups(cgroups)
3. Union Filesystem
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
- mentre i namespace gestiscono l'**isolamento**, i cgroups gestiscono il **controllo delle risorse**.
In particolare: 
- ==i cgroups sono una caratteristica del kernel Linux e permettono  di organizzare i processi in gruppi gerarchici i quali usano i vari tipi di risorse che possono essere limitate e monitorate.==

In altre parole: ==i cgroups permettono di **limitare, misurare e prioritizzare** quante risorse hardware un gruppo di processi può consumare.==

Risorse controllabili tramite cgroups:

- **CPU** → quanti core o quanta percentuale di CPU può usare il container
- **RAM** → limite massimo di memoria utilizzabile
- **I/O disco** → velocità massima di lettura/scrittura
- **Rete** → banda disponibile
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
Quando avvii un container, Docker aggiunge sopra questi layer read-only un **layer scrivibile** (detto _container layer_), che è l'unico modificabile durante l'esecuzione:
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
>[!ticket] **I dati nei container sono effimeri (ephemeral)** 
>==Quando un container viene fermato e rimosso con `docker rm`, il **Container Layer viene eliminato insieme a lui** — e tutti i dati scritti al suo interno vengono persi in modo permanente.==

Questo è un problema concreto: 
- immaginiamo un container con **PostgreSQL**. ==Se i dati del database finiscono nel Container Layer, ogni volta che il container viene rimosso e ricreato, **tutti i database vengono eliminati**.==
#### La soluzione: montare storage esterno

Per rendere i dati **persistenti**, Docker offre 2 meccanismi che permettono di salvare i dati **al di fuori** del Container Layer effimero:
1. **Bind Mount:** 
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

```docker
# Build dell'immagine
docker build --tag my-ubuntu-image .

# Ogni container creato da questa immagine avrà già ping installato
docker run -it --rm my-ubuntu-image
ping google.com -c 1 # ✅ Funziona sempre!
```

>[!ticket] **Regola generale** 
>==Tutto ciò di cui l'applicazione ha bisogno per funzionare deve essere **costruito nell'immagine**. L'unica eccezione sono le **configurazioni specifiche dell'ambiente** (variabili d'ambiente, file di config), che possono essere fornite a runtime.==

####  Docker run, start, attach ed exec a confronto

Lavorando con i container, è importante distinguere questi quattro comandi che spesso vengono confusi tra loro.
1. **`docker run`:**
	- ==Crea **e** avvia un nuovo container da un'immagine.== 
	- ==Ogni volta che lo usi, stai generando un Container Layer nuovo e separato.==
```docker
docker run -it --name my-ubuntu-container ubuntu:22.04
```
2. **`docker start`** 
	- ==Avvia un container **già esistente** ma fermo, preservando il suo Container Layer con tutte le modifiche precedenti. ==
	- ==Il container riparte in background.==
```docker
docker start my-ubuntu-container
```

3. **`docker attach`** 
	- ==Si aggancia al **processo principale** (PID 1) di un container già in esecuzione, portandoti dentro il suo terminale.==
```docker
docker attach my-ubuntu-container
```

>[!warning] **Attenzione** ==Fare `exit` da una sessione `attach` **ferma il processo principale** del container, quindi lo ferma completamente.==

4. **`docker exec`** 
	- ==Lancia un **processo nuovo** all'interno di un container già in esecuzione, senza toccare il processo principale.==
```docker
docker exec -it my-ubuntu-container bash
```

>[!hint] **Quando usare `exec` invece di `attach`?** 
>==Quando il container sta già eseguendo un'applicazione (es. PostgreSQL, nginx) e lo si vuole **ispezionare o debuggare** senza interromperne il funzionamento.==


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

>[!fail] **Il file non esiste più** 
>==Il nuovo container ha un **Container Layer nuovo e vuoto** — il file scritto nel container precedente è andato perso insieme al suo layer.==

Come abbiamo [[#La persistenza dei dati nei containers|anticipato sopra]], per garantire la persistenza dei dati , oltre il ciclo di vita di un container, Docker offre tre meccanismi:

| Tipo         | Dove vengono salvati i dati                         | Persistenti dopo `docker rm` |
| ------------ | --------------------------------------------------- | ---------------------------- |
| Volume Mount | Area gestita da Docker (`/var/lib/docker/volumes/`) | ✅                            |
| Bind Mount   | Cartella scelta da te sul filesystem host           | ✅                            |
| tmpfs Mount  | Memoria RAM                                         | ❌                            |
>[!info] **tmpfs Mount** 
>Questo tipo di Mount, che non abbiamo visto precedentemente,
>==salva i dati temporaneamente in **RAM** invece che su disco.==
>**Di conseguenza i dati spariscono quando il container si ferma.** 
>==Viene usato per dati sensibili temporanei (es. credenziali) che non si vuole lasciare su disco.==

i. Volume Mount
```docker
# Creiamo un volume named
docker volume create my-volume

# Montiamo il volume nel container (sintassi estesa)
docker run -it --rm --mount source=my-volume,destination=/my-data/ ubuntu:22.04

# Sintassi breve equivalente
docker run -it --rm -v my-volume:/my-data ubuntu:22.04

# Creiamo un file nel volume
echo "Hello from the container!" > /my-data/hello.txt
exit

# Creiamo un NUOVO container con lo stesso volume montato
docker run -it --rm --mount source=my-volume,destination=/my-data/ ubuntu:22.04
cat my-data/hello.txt # ✅ Il file esiste ancora!
exit
```

>[!help] **Dove si trovano fisicamente i dati?** 
>==Su Linux i dati si trovano in `/var/lib/docker/volumes/`.==
> **Su Docker Desktop (Windows/Mac), Docker gira su una VM Linux interna** — ==quindi i dati si trovano nel filesystem di quella VM, non direttamente sull'host.==

Su Docker Desktop è possibile ispezionare fisicamente il filesystem della VM Linux interna usando un container privilegiato:
```docker
docker run -it --rm --privileged --pid=host justincormack/nsenter1@sha256:5af0be5e42ebd55eea2c593e4622f810065c3f45bb805eaacf43f08f3d06ffd8
```

Una volta dentro, si può navigare nel volume:
```shell
ls /var/lib/docker/volumes/my-volume/_data
cat /var/lib/docker/volumes/my-volume/_data/hello.txt # ✅ I dati sono qui!
```

> [!warning] **Attenzione** ==Questo container gira in modalità **privilegiata** con accesso root alla VM Linux di Docker. Usarlo solo quando strettamente necessario e solo con immagini di cui ci si fida.==

> [!info] **Perché pinniamo l'hash dell'immagine?** 
> ==Il flag `@sha256:...` garantisce che venga eseguita **esattamente** quella versione dell'immagine, non una versione aggiornata potenzialmente modificata. È una buona pratica di sicurezza per immagini privilegiate.==

Un caso d'uso concreto che già conosci — **PostgreSQL**:
```docker
# Il volume pgdata persiste i dati del database anche se il container viene rimosso
docker run -it --rm -v pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=foobarbaz postgres:15.1-alpine
```

**ii. Bind Mount**
```docker
# Sintassi estesa
docker run -it --rm --mount type=bind,source="${PWD}"/my-data,destination=/my-data ubuntu:22.04

# Sintassi breve equivalente
docker run -it --rm -v ${PWD}/my-data:/my-data ubuntu:22.04

echo "Hello from the container!" > /my-data/hello.txt
exit

# Il file è visibile direttamente sul filesystem host!
cat my-data/hello.txt # ✅
```

>[!tip] **Volume Mount vs Bind Mount: quale usare?**
>
>- ==Il **Bind Mount** è comodo quando vuoi **visibilità diretta** sui dati dall'host (es. durante lo sviluppo).==
>- ==Il **Volume Mount** è **preferibile in produzione**: è più veloce, più portabile e interamente gestito da Docker.==
### Come si crea un container 

Per comprendere come nasce un container, è necessario introdurre prima il concetto di **immagine container**.
Un immagine container è, in sostanza, ==un file di testo che descrive staticamente **tutti i passaggi necessari per costruire un ambiente eseguibile** all’interno di un container.==

Contiene informazioni come:

- ==il sistema operativo di base (es. Ubuntu 22.04, Alpine, Debian)==
    
- ==le dipendenze dell’applicazione (es. Node.js, Java, Python)==
    
- ==l’applicazione stessa (es. file `.jar`, `.py`, `.js` ecc.)==
    
- ==eventuali comandi da eseguire all'avvio== 

Questa immagine viene definita all’interno di un **Dockerfile**, un file di testo che funge da vera e propria **"ricetta"** per creare il container.
Una volta scritto il Dockerfile, si può eseguire il comando di build:
```docker
docker build -t nome-immagine .
```

==Il Docker engine leggerà il Dockerfile, lo interpreterà, e **costruirà l'immagine** sulla base delle istruzioni contenute.==
Quando questa immagine viene "attivata", cioè **eseguita in un ambiente containerizzato**, essa diventa un **container**.

> [!example] Analogia con la programmazione OOP
> Il Dockerfile è come una **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi|classe Python]]**,  
>	l'immagine è come la **definizione della classe**,  
>		e il container è **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#Istanze di una classe|l'istanza reale]]**, ovvero l'oggetto in memoria.

Inoltre, le immagini create localmente possono essere **pubblicate su repository remoti**, in modo da essere condivise o riutilizzate su altri ambienti.  
Il più noto è il [Docker Hub](https://hub.docker.com/repositories), una **registry pubblica gratuita per uso personale**, dove si possono trovare migliaia di immagini ufficiali e di terze parti.

> [!abstract]  WSL e container Docker
> **WSL** (Windows Subsystem for Linux) **è un sottosistema che integra un [[I fundamentals di un Sistema Operativo#Kernel|kernel]] Linux reale all'interno di Windows**.
>  ==In pratica, vive **affiancato** al sistema operativo Windows e permette di eseguire ambienti Linux nativi senza la necessità di installare una macchina virtuale tradizionale==.
> 
> Sebbene **Windows supporti anche container nativi Windows**, nella pratica la **tecnologia di containerizzazione dà il meglio di sé in ambienti Linux**, perché è nata lì ed è ottimizzata per quel contesto.
> 
> Infatti, la **stragrande maggioranza dei container Docker** eseguiti nel mondo reale sono container **Linux**, anche quando vengono lanciati da un computer con sistema operativo Windows.
> 
> ==Per questa ragione, quando si  installa Docker Desktop su Windows, esso si **appoggia a WSL2** per offrire **un ambiente Linux** in cui i container possano funzionare **nativamente** e con prestazioni elevate==.
> 
> ![[La vera struttura di docker.png]]
>Questa immagine difatti mostra come docker si basi su un kernel linux


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
