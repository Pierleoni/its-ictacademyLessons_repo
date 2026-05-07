# Costruire le immagini dei container docker
Fino ad ora abbiamo utilizzato **immagini di terze parti** — [[Lezione 2 - Demo Application#1. PostgreSQL|PostgreSQL]], [[Lezione 2 - Demo Application#2. API Node.js|Node.js]], e [[Lezione 1 - Introduzione a Docker e ai container#La soluzione corretta costruire le dipendenze nell'immagine|Ubuntu]] — scaricandole direttamente da Docker Hub e avviandole con `docker run`. 
Vedremo  come [[#Dockerfile|un'immagine viene costruita a partire da un Dockerfile]], e come ogni istruzione del Dockerfile crei un layer read-only nello stack dell'[[Lezione 1 - Introduzione a Docker e ai container#Union Mount Filesystems (overlayfs)|Union Filesystem]].

Ora è il momento di imparare a **costruire immagini proprie** in modo professionale — non solo funzionanti, ma ottimizzate per:

- 🔒 **Sicurezza** → ridurre le vulnerabilità e il rischio di attacchi
- 🏎️ **Velocità di build** → sfruttare la cache dei layer per build più rapide
- 👁️ **Chiarezza** → rendere il Dockerfile leggibile e manutenibile da altri sviluppatori

Per farlo useremo i tre servizi dell'applicazione di esempio che abbiamo già avviato — `api-node`, `api-golang` e `client-react` — ciascuno dei quali contiene una serie di Dockerfile progressivi (`Dockerfile.0` → `Dockerfile.N`):

- ==`Dockerfile.0` → l'approccio più semplice e naïve==
- ==`Dockerfile.N` → la versione finale ottimizzata che useremo in produzione==

Ogni step migliora il precedente applicando una o più **best practice** che vedremo nel dettaglio nelle sezioni successive.

>[!info] **Come buildare i Dockerfile progressivi** 
>Il Makefile di ciascun servizio espone un target `build-N` per buildare un Dockerfile specifico:
>```shell
># Esempio: builda il Dockerfile.4 di api-golang
>cd api-golang && N=4 make build-N
>```
## Dockerfile

Ora che abbiamo capito come funziona l'[[Lezione 1 - Introduzione a Docker e ai container#Union Mount Filesystems (overlayfs)|Union Filesystem]] e la struttura a layer, possiamo capire concretamente come nasce un container.

Il punto di partenza è sempre una **immagine container** — ==un file di testo che descrive staticamente tutti i passaggi necessari (i comandi) per costruire un ambiente eseguibile.== 
Possiamo pensarlo come una ricetta per la nostra applicazione, contiene alcuni layer di base come:

- ==il sistema operativo di base (es. Ubuntu 22.04, Alpine, Debian)==
- ==le dipendenze dell'applicazione (es. Node.js, Java, Python)==
- ==l'applicazione stessa (es. file `.jar`, `.py`, `.js` ecc.)==
- ==eventuali comandi da eseguire all'avvio==

==Questa immagine viene definita all'interno di un **Dockerfile**, un file di testo che funge da vera e propria "ricetta" per creare il container.== 
Una volta scritto il Dockerfile, si esegue il comando di build:
```docker
docker build -t nome-immagine .
```

Il [[Lezione 1 - Introduzione a Docker e ai container#Docker Engine|Docker Engine]] leggerà il Dockerfile riga per riga, e **costruirà un layer read-only per ogni istruzione**, come abbiamo visto nella sezione sull'[[#Union Mount Filesystems (overlayfs)|Union Filesystem]]. 
==Quando questa immagine viene eseguita con `docker run`, Docker aggiunge il **Container Layer scrivibile** in cima allo stack — ed è in quel momento che l'immagine diventa un container.==

> [!example] Analogia con la programmazione OOP
> Il Dockerfile è come una **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi|classe Python]]:**  
>- l'immagine è come la **definizione della classe**,  
>- e il container è **[[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#Istanze di una classe|l'istanza reale]]**, ovvero l'oggetto in memoria.

Inoltre, le immagini create localmente possono essere **pubblicate su [[Lezione 1 - Introduzione a Docker e ai container#Registry|registry]] remoti**, in modo da essere condivise o riutilizzate su altri ambienti. Il più noto è [Docker Hub](https://hub.docker.com/repositories), una registry pubblica gratuita per uso personale, dove si possono trovare migliaia di immagini ufficiali e di terze parti.
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


### Docker Build

Il Dockerfile è accoppiato con il cosiddetto **build context (contesto di build)**.  
Scriviamo tutte le istruzioni nel Dockerfile e il build context è, in genere, una directory presente sul nostro host.  
**Questo build context non è superfluo:** ==contiene tutto il nostro codice sorgente.==

> [!Info] **Può anche essere un URL**  
> Come ad esempio un URL che punta a una repo pubblica di GitHub che fa da build context.

Prendendo queste due cose insieme ed eseguendo il comando di build di Docker, ==quest'ultimo prenderà queste informazioni e sarà in grado di eseguire le istruzioni contenute nel Dockerfile e produrre un'immagine del container.==

![[Docker built context.png]]

>[!NOTE] **Il file `.dockerignore`**  
>Nel nostro build context possiamo includere questo file `.dockerignore` e, come per il file `.gitignore`, questo file permette a Docker di ignorare alcuni file che dichiariamo.
>![[dockerignore.png]]
>
>
>> [!example] **Caso d'uso: i Node modules**  
>> Supponiamo, come visto nella scorsa lezione, di aver installato i node modules localmente e che non vogliamo che vengano copiati nel Dockerfile poiché ==porterebbero a incompatibilità tra l'installazione sul nostro host system e il sistema operativo installato nel container.==

### Scrivere un Dockerfile
Ora vediamo nella pratica come scrivere a mano un Dockerfile, il formato è il seguente
```docker
# Comment
INSTRUCTION arguments
```

- `# comment` : i commenti in docker
- `INSTRUCTION`: sono le istruzioni, cioè i comandi, che dovrà eseguire docker per costruire un container basandosi sull'immagine 
- `arguments`: sono gli argomenti, ovvero cosa fa l'istruzione che li segue

> [!NOTE] **Nota**
> ==Le istruzioni sono case-insensitive==.
>Tuttavia per convezione è ==buona pratica scriverle in maiuscolo in modo da distinguerle più facilmente dagli argomenti==

**Esempio:**
```docker
# Comment
RUN echo 'we are running some # of cool things'
```

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
