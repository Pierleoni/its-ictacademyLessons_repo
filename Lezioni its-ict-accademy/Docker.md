# Introduzione 
Prima di spiegare cos’è Docker, è importante comprendere **perché** questa tecnologia è diventata così centrale nello sviluppo moderno, specialmente nei contesti orientati ai microservizi e alle metodologie DevOps, dove agilità, portabilità e scalabilità sono fondamentali.

## La virtualizzazione 
**Ma cos'è docker?**
La risposta a questa prima domanda è:
==Docker è una tecnologia di virtualizzazione.==
La virtualizzazione è una tecnica che consente di: 
- ==**astrarre l’hardware fisico** e creare ambienti virtuali isolati all’interno di un sistema operativo. 

==In questi ambienti, i programmi **credono di essere eseguiti direttamente su una macchina fisica**, con una propria CPU, RAM, disco, ecc., ma in realtà stanno utilizzando risorse **virtualizzate** fornite da un software intermedio.== 
Quindi la  virtualizzazione **serve per astrarre il concetto di computer fisico:** 
-  ==in concreto, permette di creare un ambiente virtuale dentro il SO della macchina.== 
In altre parole: 
- **un sistema che al suo interno ospita un altro sistema/ambiente virtuale.**
  
In altri termini, la virtualizzazione consente di creare al **di sopra del sistema operativo reale**, uno o più ambienti "simulati", ciascuno dei quali si comporta come un computer indipendente, dotato di proprie risorse (virtuali). 

> [!example] Questo permette, ad esempio, di simulare una macchina con 2 o 4 core CPU, con una certa quantità di RAM, ecc.
> 

Le tecnologie di virtualizzazione — come quelle che permettono di creare **macchine virtuali (VM)** — nascono proprio per facilitare:

- ==la **portabilità** degli ambienti software.==
    
- ==la **replicabilità** delle configurazioni.==
    
- ==l’**ottimizzazione dei costi** (soprattutto in ambienti server e cloud).==
    
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
> 1.Bare metal: 
> 	Direttamente sull'hardware senza SO host.
>     E sono VMware ESXi, Microsoft Hyper-V Server.
> 2. Hosted: 
> 	Sopra un sistema operativo host.
> 	Ad esempio VirtualBox, VMware Workstation, Parallels  

	   
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

- I container sono **più piccoli: ** 
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
> Il Dockerfile è come una **[[Le Classi|classe Python]]**,  
>	l'immagine è come la **definizione della classe**,  
>		e il container è **[[Le Classi#Istanze di una classe|l'istanza reale]]**, ovvero l'oggetto in memoria.

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




---
### Installare docker su windows 
Per installare docker su windows è necessario installare anche il docker desktop.
[Per vedere la documentazione officiale per installare docker su windows](https://docs.docker.com/desktop/setup/install/windows-install/)

> [!hint] **Consiglio**
> Cliccare su *" Docker Desktop for windows - x86_64"* per scaricare l'installer del docker desktop

### Docker run e Docker pull
Questi due comandi sono utili per capire il flusso di lavoro con Docker.

1. `docker run`: 
	- Crea e avvia un **container** a partire da un’immagine.  
	- Se l’immagine non è già presente in locale, **Docker la scarica automaticamente.**
2. `docker pull`: 
	- Scarica un’immagine da un **registry** (di default Docker Hub) verso il tuo computer ma non la esegue.


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
Le immagini, di fatto, sono come dei template per i containers: 
- Specificano: 
	- Il contenuto di un file system
	- che applicazioni ha installato l'utente 
	- variabili di ambiente
	- E il comando di default che farà partire il container.
Quindi possiamo pensare a una immagine come un recipiente per eseguire una applicazione.

I container dall'altro canto sono il gruppo di processi che vengono lanciati ed seguono le istruzioni specificate nell'immagine docker.

Quindi ogni volta che si esegue un immagine docker essa crea in automatico un nuovo container basato sul quell'immagine. 
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
