# Introduzione 
Prima di spiegare cos’è Docker, è importante comprendere **perché** questa tecnologia è diventata così centrale nello sviluppo moderno, specialmente nei contesti orientati ai microservizi e alle metodologie DevOps, dove agilità, portabilità e scalabilità sono fondamentali.

## La virtualizzazione 
**Ma cos'è docker?**
La risposta a questa prima domanda è:
==Docker è una tecnologia di virtualizzazione.==
La virtualizzazione è una tecnica che consente di: 
==**astrarre l’hardware fisico** e creare ambienti virtuali isolati all’interno di un sistema operativo. 
In questi ambienti, i programmi **credono di essere eseguiti direttamente su una macchina fisica**, con una propria CPU, RAM, disco, ecc., ma in realtà stanno utilizzando risorse **virtualizzate** fornite da un software intermedio.== 
Quindi la  virtualizzazione serve per astrarre il concetto di computer fisico: ovvero, in concreto, permette di creare un ambiente virtuale dentro il SO della macchina. 
In altre parole: un sistema che al suo interno ospita un altro sistema/ambiente virtuale.
In altri termini, la virtualizzazione consente di creare al **di sopra del sistema operativo reale**, uno o più ambienti "simulati", ciascuno dei quali si comporta come un computer indipendente, dotato di proprie risorse (virtuali). Questo permette, ad esempio, di simulare una macchina con 2 o 4 core CPU, con una certa quantità di RAM, ecc.
Le tecnologie di virtualizzazione — come quelle che permettono di creare **macchine virtuali (VM)** — nascono proprio per facilitare:

- la **portabilità** degli ambienti software,
    
- la **replicabilità** delle configurazioni,
    
- l’**ottimizzazione dei costi** (soprattutto in ambienti server e cloud),
    
- e in generale per **isolare i contesti di esecuzione**.

Docker si inserisce in questo scenario come una **tecnologia di virtualizzazione più leggera**, che consente una gestione più efficiente di ambienti e applicazioni, rendendole facilmente trasportabili ed eseguibili su molteplici sistemi, senza complicazioni legate all’installazione o alla configurazione dell’ambiente sottostante.


### Confronto tra VM e Docker

Per comprendere davvero il funzionamento di Docker, è essenziale distinguere il suo approccio da quello delle macchine virtuali classiche.
#### Le macchine virtuali (VM)
Una macchina virtuale si basa su un'infrastruttura a più livelli:
1. **Hardware fisico**  
	(CPU, RAM, disco rigido, motherboard, ecc.)
2. **Hypervisor**:
	   Si tratta di un software specializzato che gestisce la virtualizzazione. L’hypervisor si interpone tra l’hardware fisico e i sistemi operativi "ospiti" (guest), virtualizzando le risorse della macchina e assegnandole alle singole VM.
	   Esempi di hypervisor sono VirtualBox, VMware Workstation, VMware ESXi, ecc.
	   
> [!info] Gli hypervisor si suddividono in 2 principali categorie:
> 1.Bare metal: 
> 	Direttamente sull'hardware senza SO host.
>     E sono VMware ESXi, Microsoft Hyper-V Server.
> 2. Hosted: 
> 	Sopra un sistema operativo host.
> 	Ad esempio VirtualBox, VMware Workstation, Parallels  

	   
3. <mark style="background: #00FF02A6;">Guest OS(Sistema operativo ospite)</mark>: 
	È il sistema operativo installato all’interno della VM. Può essere Windows, Linux, macOS, ecc. Ogni VM ha il **proprio sistema operativo completo**, separato da quello dell’host.
	Inoltre all'interno della nostro Hypervisor possiamo avere diversi SO ospiti.
4. <mark style="background: #00FF02A6;">Liberie BIN</mark>: 
	   Sono le librerie e i runtime specifici del sistema operativo ospite, ad esempio .NET per Windows, le glibc per Linux, ecc.
5. **<mark style="background: #00FF02A6;">Applicazioni: </mark>**
    Infine, le applicazioni che vogliamo eseguire sono installate **sopra** tutto questo stack.


> [!example] Esempio concreto
> Prendiamo ad esempio una macchina che abbia 


![[VM esempio.png]]
Come si può notare, questo modello introduce una certa **ridondanza**: 
ogni VM ha bisogno di un intero sistema operativo, più tutte le librerie necessarie a supportare l'applicazione. Questo comporta un uso intensivo di risorse, tempi di avvio più lenti e maggiore complessità nella gestione.
Ed è proprio qui che entra in gioco Docker, proponendo un’alternativa **più leggera ed efficiente**: la **containerizzazione**.


#### Docker: virtualizzazione container
Vediamo ora come funziona la tecnologia dei container, come quella su cui si basa Docker.
Alla base di questa architettura abbiamo:
1. **Hardware fisico della macchina:**
	   (CPU, RAM, disco, ecc.)
2. **Sistema operativo nativo:** 
	   Può essere sia Linux che Windows: i container possono essere eseguiti su entrambi, a seconda del contesto e della compatibilità.
3. **Container Engine:**
    Questo è il “fratello” dell’hypervisor.
	A differenza di quest’ultimo, però, **non è un sistema operativo**, ma un motore (engine) che si occupa di gestire i container. Docker, ad esempio, è un container engine molto diffuso. Esso si occupa di creare, avviare, isolare e controllare i container sul sistema operativo sottostante.
4.  <mark style="background: #E5FF00A6;">Librerie BIN:</mark>
	  Sono le dipendenze e i runtime necessari per eseguire l'applicazione. Ogni container può portare con sé le proprie librerie, ad esempio una specifica versione di Java o Python. 
5. <mark style="background: #E5FF00A6;">le applicazioni: </mark>
	   Le app vere e proprie, che vengono eseguite all'interno del container, insieme alle dipendenze necessarie.

![[Tecnologia Container.png]]

A differenza delle **macchine virtuali**, dove ogni istanza porta con sé anche un sistema operativo completo, i **container** sono molto più leggeri: includono solo l’applicazione e le sue dipendenze. 
Il **sistema operativo** è **unico** e condiviso tra tutti i container attraverso il container engine.

Questo rende i container:

- **più veloci da avviare**
    
- **meno pesanti** in termini di consumo di risorse (RAM, CPU, disco)
    
- **più portabili** tra ambienti diversi.

Possiamo notare come i container risultino **più leggeri e compatti rispetto alle VM**, in quanto contengono solamente **le applicazioni** e le **librerie di cui hanno bisogno** per funzionare (come ad esempio Java, Node.js, Python, ecc.).  
Al contrario, nelle macchine virtuali ogni applicazione viene impacchettata **insieme al proprio sistema operativo completo**, oltre che alle sue dipendenze. Questo rende le VM molto più pesanti in termini di consumo di risorse.

Nel mondo dei container, invece, il **sistema operativo è uno solo**: quello del sistema host, che viene **condiviso da tutte le applicazioni** tramite il container engine (come Docker). App1 e App2, pur condividendo lo stesso sistema operativo, sono eseguite **in ambienti isolati**: ogni container ha il proprio spazio di esecuzione, e un’applicazione non è a conoscenza dell’altra.

Va però evidenziata una differenza importante:  
Nelle **macchine virtuali**, l’isolamento tra applicazioni è più forte, poiché ognuna gira all’interno di un proprio sistema operativo. Nei container, invece, l’isolamento è gestito dal motore dei container e **avviene a livello di processo**, quindi è tecnicamente più "leggero", anche se comunque sicuro.  
In condizioni normali, App1 non può interagire né sapere dell’esistenza di App2, salvo bug o vulnerabilità nel container engine stesso.

Questo approccio ha numerosi **vantaggi pratici**:

- I container sono **più piccoli**, perché non contengono un intero sistema operativo.
    
- Sono **più economici in termini di risorse**: la CPU, la RAM e il disco vengono utilizzati in modo più efficiente rispetto alle VM.
    
- L’avvio di un container è **molto più rapido** rispetto al boot di una macchina virtuale.
    

Ma soprattutto, i container offrono una **forte portabilità**: l’applicazione e le sue dipendenze vengono impacchettate in un unico oggetto eseguibile, che può essere facilmente eseguito su qualsiasi macchina che abbia un container engine compatibile.  
Questo approccio elimina il classico problema dello sviluppatore:

> _“Funziona sul mio computer, ma non sul server di produzione.”_

Finché l’ambiente in cui si esegue il container supporta il container engine (come Docker), l’applicazione si comporterà **esattamente nello stesso modo**, indipendentemente dal sistema operativo host o dalle configurazioni di sistema.

Anche con le VM si può ottenere una certa portabilità, ma con un **peso molto maggiore**, perché si trasporta l’intera macchina virtuale con il suo sistema operativo. Con i container, invece, si trasporta solo **l’essenziale**: l’applicazione e ciò che serve per farla girare.

In questo modo, agli sviluppatori viene offerta la possibilità di **impacchettare le proprie applicazioni in modo più snello e modulare**, facilitando enormemente il deployment in ambienti diversi, come sviluppo, test e produzione.


### Come si crea un container 

Per comprendere come nasce un container, è necessario introdurre prima il concetto di **immagine container**.
Un immagine container è, in sostanza, un file di testo che descrive staticamente **tutti i passaggi necessari per costruire un ambiente eseguibile** all’interno di un container.

Contiene informazioni come:

- il sistema operativo di base (es. Ubuntu 22.04, Alpine, Debian)
    
- le dipendenze dell’applicazione (es. Node.js, Java, Python)
    
- l’applicazione stessa (es. file `.jar`, `.py`, `.js` ecc.)
    
- eventuali comandi da eseguire all'avvio 
Questa immagine viene definita all’interno di un **Dockerfile**, un file di testo che funge da vera e propria **"ricetta"** per creare il container.
Una volta scritto il Dockerfile, si può eseguire il comando di build:
```shell
docker build -t nome-immagine .
```
Il Docker engine leggerà il Dockerfile, lo interpreterà, e **costruirà l'immagine** sulla base delle istruzioni contenute.
Quando questa immagine viene "attivata", cioè **eseguita in un ambiente containerizzato**, essa diventa un **container**.

> [!example] Analogia con la programmazione OOP
> Il Dockerfile è come una **[[Le Classi|classe Python]]**,  
>	l'immagine è come la **definizione della classe**,  
>		e il container è **[[Le Classi#Istanze di una classe|l'istanza reale]]**, ovvero l'oggetto in memoria.

Inoltre, le immagini create localmente possono essere **pubblicate su repository remoti**, in modo da essere condivise o riutilizzate su altri ambienti.  
Il più noto è il [Docker Hub](https://hub.docker.com/repositories), una **registry pubblica gratuita per uso personale**, dove si possono trovare migliaia di immagini ufficiali e di terze parti.

> [!abstract]  WSL e container Docker
> **WSL** (Windows Subsystem for Linux) **è un sottosistema che integra un kernel Linux reale all'interno di Windows**.
>  ==In pratica, vive **affiancato** al sistema operativo Windows e permette di eseguire ambienti Linux nativi senza la necessità di installare una macchina virtuale tradizionale==.
> 
> Sebbene **Windows supporti anche container nativi Windows**, nella pratica la **tecnologia di containerizzazione dà il meglio di sé in ambienti Linux**, perché è nata lì ed è ottimizzata per quel contesto.
> 
> Infatti, la **stragrande maggioranza dei container Docker** eseguiti nel mondo reale sono container **Linux**, anche quando vengono lanciati da un computer con sistema operativo Windows.
> 
> ==Per questa ragione, quando si  installa Docker Desktop su Windows, esso si **appoggia a WSL2** per offrire **un ambiente Linux** in cui i container possano funzionare **nativamente** e con prestazioni elevate==.
 