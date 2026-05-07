# Sample Web Application: architettura a 3 livelli

Fino ad ora abbiamo esplorato Docker partendo dalle fondamenta — [[Lezione 1 - Introduzione a Docker e ai container#La virtualizzazione|la virtualizzazione]], i [[Lezione 1 - Introduzione a Docker e ai container#Linux Building Blocks|Linux Building Blocks]], la [[Lezione 1 - Introduzione a Docker e ai container#La persistenza dei dati nei containers|persistenza dei dati]] e i casi d'uso con [[Lezione 1 - Introduzione a Docker e ai container#Use Cases Database containerizzati|database]] e [[Lezione 1 - Introduzione a Docker e ai container#Ambienti di Test Interattivi|ambienti di test]]. 
**Tutti questi concetti ci hanno preparato ad affrontare quello che è il vero obiettivo di Docker nel mondo reale:** 
- ==containerizzare applicazioni complete.==

Per farlo in modo concreto, utilizzeremo una **web application di esempio** costruita con un'architettura a **3 livelli** ([[Lezione 1; Fondamenti delle Applicazioni Web#Architettura multilivello|three-tier architecture]]) — un pattern che abbiamo già incontrato nel percorso fatto con Spring Boot:
```text
[ Client React      ]  ← Presentation Layer (Frontend)
[ Node.js / Golang  ]  ← Business Logic Layer (Backend/API)
[ PostgreSQL        ]  ← Data Layer (Database)
```

Ogni livello è separato e indipendente — esattamente come nei [[Lezione 1 - Applicazioni cloud a microservizi|microservizi]] che abbiamo studiato. 
La differenza è che ora ogni livello girerà **dentro il proprio container Docker**.

I tre componenti dell'applicazione sono:

- **[[Lezione 7; React|React]] Frontend** → ==interfaccia utente che interroga le due API e visualizza i risultati==
- **Node.js e Golang API** → ==due backend con [[Lezione 6 - API#Endpoint|endpoint]] `/` (interroga il database per l'ora corrente) e `/ping` (restituisce `pong`)==
- **[[Introduzione a SQL e il DDL|PostgreSQL]]** → ==database vuoto usato per mostrare la connettività.== 
	- ==Le [[Lezione 6 - API#API (Application Programming Interface)|API]] eseguono `SELECT NOW() as now;` per ottenere l'ora corrente==

> [!info] **Perché due API diverse?**
>  **Node.js e Golang espongono gli stessi endpoint ma sono scritti in linguaggi diversi** — ==questo permette di confrontare come Docker gestisce runtime completamente diversi all'interno della stessa architettura.==

> [!hint] **PostgreSQL in container** 
> Come abbiamo già visto nella sezione sui [[#Use Cases Database containerizzati|database containerizzati]], PostgreSQL è uno dei casi d'uso più comuni per i container. Qui lo ritroveremo applicato in un contesto applicativo reale.

### Avviare l'applicazione

Prima di avviare i singoli componenti, è importante sapere che tutti i comandi necessari sono raccolti in un **Makefile** — un file che funge da "scorciatoia" per eseguire comandi complessi con un'unica istruzione `make`.

> [!faq] **Cos'è un Makefile?** 
> Un **Makefile** è un file che raccoglie una serie di **target** — comandi abbreviati eseguibili con `make nome-target`. Nato nel mondo C/C++ per automatizzare la compilazione del codice, oggi viene usato in qualsiasi progetto per standardizzare operazioni ripetitive come build, test e avvio dei servizi.
> La struttura di ogni target è sempre la stessa:
>```
>> .PHONY: nome-target
>>nome-target:
>>	comando da eseguire
>```
>- `.PHONY` → ==dice a `make` che il target **non è un file** ma sempre un comando da eseguire, evitando conflitti con eventuali file con lo stesso nome presenti nella cartella==
>- `nome-target:` → ==definisce il nome del target e le azioni che eseguirà==
>**Variabile DATABASE_URL**
>```
>DATABASE_URL:=postgres://postgres:foobarbaz@localhost:5432/postgres
>```
>
>È la **stringa di connessione** al database PostgreSQL, scomposta nei suoi componenti:
>
>| Componente | Valore        | Significato                         |
| ---------- | ------------- | ----------------------------------- |
| Protocollo | `postgres://` | Tipo di database                    |
| Utente     | `postgres`    | Nome utente per la connessione      |
| Password   | `foobarbaz`   | Password dell'utente                |
| Host       | `localhost`   | Indirizzo del server database       |
| Porta      | `5432`        | Porta standard di PostgreSQL        |
| Database   | `/postgres`   | Nome del database a cui connettersi |
>
>
>>[!link] **Formato familiare** 
>>==Questo formato è lo stesso che abbiamo già visto nel `application.properties` di Spring Boot con `spring.datasource.url` — cambia solo la sintassi.==
>
>>[!abstract]- **Spiegazione del makefile**
>>1. **Target:`run-postgres`**
>>```
>>.PHONY: run-postgres
>>run-postgres:
>>	@echo Starting postgres container
>>    -docker run \
>>		-e POSTGRES_PASSWORD=foobarbaz \
>>		-v pgdata:/var/lib/postgresql/data \
>>		-p 5432:5432 \
>>		postgres:15.1-alpine
>>```
>>- `@echo Starting postgres container` → ==stampa un messaggio nel terminale==. 
>> 	 - `@` ==sopprime la stampa del comando stesso, mostrando solo il suo output==
>>- `-docker run` → ==il `-` prima di `docker run` dice a `make` di **ignorare eventuali errori** e continuare — utile se il container è già in esecuzione==
>>- `-e POSTGRES_PASSWORD=foobarbaz` → ==passa la password come variabile d'ambiente==
>>- `-v pgdata:/var/lib/postgresql/data` → ==monta il volume per persistere i dati del database==
>>- `-p 5432:5432` → ==espone la porta PostgreSQL sull'host==
>> 
>> 2. **Target: run-api-node**
>>```
>> .PHONY: run-api-node
>>run-api-node:
>>	@echo Starting node api
>>	cd api-node && \    
>>		DATABASE_URL=${DATABASE_URL} \
>>		npm run dev
>>```
>>- `cd api-node` → ==entra nella cartella del progetto Node.js==
>>- `&&` → ==esegue il comando successivo solo se il precedente ha avuto successo==
>>- `DATABASE_URL=${DATABASE_URL}` → ==passa la variabile di connessione al database definita in cima al Makefile==
>>- `npm run dev` → ==avvia l'API in **development mode** con nodemon, che riavvia automaticamente il server ad ogni modifica al codice==
>>
>>3. **Target: run-api-golang**
>>```
>>.PHONY: run-api-golang
>>run-api-golang:
>>	@echo Starting golang api
>>	cd api-golang && \
>>		DATABASE_URL=${DATABASE_URL} \
>>		go run main.go
>>```
>>
>>- `cd api-golang` → ==entra nella cartella del progetto Golang==
>>- `DATABASE_URL=${DATABASE_URL}` → ==passa la stringa di connessione al database==
>>- `go run main.go` → ==compila ed esegue direttamente il file principale dell'API Golang==
>>
>>4. **Target: run-client-react:**
>>```
>>.PHONY: run-client-react
>>run-client-react:
>>	@echo Starting react client
>>	cd client-react && \
>>		npm run dev
>>```
>>
>>- `cd client-react` → ==entra nella cartella del progetto React==
>>- `npm run dev` → ==avvia il frontend React con **Vite** in development mode, con hot reload automatico ad ogni modifica al codice==


I quattro componenti vanno avviati separatamente, ciascuno nel proprio terminale:

#### 1. PostgreSQL

Come abbiamo già visto nella sezione sui [[#Use Cases Database containerizzati|database containerizzati]], PostgreSQL è il candidato ideale per girare in un container:
```shell
# Prima ci spostiamo nella cartella del progetto
cd "/mnt/c/Users/Project Lead/Desktop/Docker-test/example-web-app/05-example-web-application"
# Dopodiché avviamo il container Docker con PostgreSQL
make run-postgres
```

Avvia PostgreSQL in un container e pubblica la porta `5432` del container sulla porta `5432` dell'host.

#### 2. API Node.js

Prima di avviare l'API Node.js è necessario installare le dipendenze del progetto:
```shell
# Prima ci spostiamo nella cartella del progetto
cd "/mnt/c/Users/Project Lead/Desktop/Docker-test/example-web-app/05-example-web-application"
# In seguito navighiamo nella directory del progetto node.js
cd api-node
# Installiamo le dipendenze
npm install
# navighiamo indietro nella directory '05-example-web-application' dove si trova il makefile
cd ..
# Avviamo l'API in development mode
make run-api-node
```

==`make run-api-node` avvia l'API con **nodemon** — uno strumento che monitora i file del progetto e riavvia automaticamente il server ogni volta che viene rilevata una modifica al codice sorgente.==

Possiamo notare che nel file `package.json` abbiamo una serie di dipendenze: 
```json
"dependencies": {
	 "express": "^4.18.2",
	 "morgan": "^1.10.0",
	 "pg": "^8.8.0"
  },
```

- `"express": "^4.18.2"` ==un package che serve a costruire API REST==
- `"morgan": "^1.10.0",`: ==una dipendenza che aiuta a configurare il logging all'API REST in maniera più semplice==
- ` "pg": "^8.8.0"`: **è il package di postgres.**
	- ==permette di creare un client e di connetterlo al database==

> [!info] **Versioni usate** Node.js `v19.4.0` e npm `v9.2.0`

>[!warning] **Problema su Windows: `ERR_INVALID_ARG_TYPE` in `db.js`** Su **Windows**
>l'API Node.js potrebbe crashare con questo errore:
>```shell
>TypeError [ERR_INVALID_ARG_TYPE]: The "path" argument must be of type string or an instance of Buffer or URL. Received undefined
> 	   at Object.readFileSync (node:fs:440:14)
> 	   at Object.<anonymous> (...api-node\src\db.js:7:6)
>```
>**Causa:** Il codice in `db.js` legge la stringa di connessione al database in questo modo:
>```js
>databaseUrl =
> 	 process.env.DATABASE_URL ||
> 	 fs.readFileSync(process.env.DATABASE_URL_FILE, 'utf8');
>```
>==Se `DATABASE_URL` non viene letta correttamente dal processo Windows, Node.js tenta di leggere `DATABASE_URL_FILE` — che però è anch'essa `undefined` — causando il crash.==
>
>**Cause aggiuntive su Windows:**
>
>- Node.js potrebbe essere in una versione incompatibile (`v22.x` invece di `v19.4.0`)
>- La variabile d'ambiente passata dal Makefile non viene propagata correttamente al processo Windows
> **Soluzione:**
>
>1. Installare **nvm** per gestire le versioni di Node.js:
>```shell
>curl -o- https://raw.githubusercontent.com/nvm->sh/nvm/v0.39.7/install.sh | bash
>source ~/.bashrc
>nvm install 19.4.0
>nvm use 19.4.0
>```
>2. Avviare l'API esportando manualmente la variabile d'ambiente:
>```shell
>DATABASE_URL=postgres://postgres:foobarbaz@localhost:5432/postgres npm run dev
>```
>>[!important]- **Nota importante!**
>> ==Il problema non è tanto Windows vs Mac, ma il fatto che **Node.js di Windows e WSL sono due ambienti separati**. La soluzione è assicurarsi di usare sempre Node.js installato **dentro WSL** tramite nvm, non quello installato su Windows.==

Ora se andiamo su la porta `3000` del localhost vediamo una cosa del genere: 
```json
{
	"now":"2026-05-06T14:37:33.628Z",
	"api":"node"
}
```

Questo è la risposta dell'endpoint dell'api node.js che sta  interrogando PostgreSQL con `SELECT NOW() as now;` e restituisce:

- `now` → ==l'ora corrente del database==
- `api` → ==indica che la risposta viene dall'API Node.js==

#### 3. API Golang

Adesso spostiamoci su l'api di golang, prima di tutto se non abbiamo installato golang su host dobbiamo eseguire questo CLI su terminale WSL: 
```shell
sudo apt install golang-go
```

Dopodiché verifichiamo l'installazione: 
```shell
go version
```

E poi segui le istruzioni del `README.md` presenti nella cartella `api-golang`:
```shell
cd "/mnt/c/Users/Project Lead/Desktop/Docker-test/example-web-app/05-example-web-application/api-golang"
mkdir go-workspace
export GOPATH=$PWD/go-workspace
go mod download
go run main.go
```

> [!info] **Versione usata** Go `v1.19.1`

Queste istruzioni sono necessarie per una prima configurazione dell'api scritta in golang.
Una volta eseguiti per far partire l'api basta semplicemente eseguire questi due comandi:

```shell
# Navigo nella cartella 'api-golang'
cd "/mnt/c/Users/Project Lead/Desktop/Docker-test/example-web-app/05-example-web-application/api-golang"
# Riesporto il path
export GOPATH=$PWD/go-workspace
# Navigo indietro di un livello
cd ..
# Build e avvio dell'API
make run-api-golang
```

>[!help] **Perché riesportare GOPATH?** 
>==`export GOPATH` imposta una variabile d'ambiente **solo per la sessione corrente** del terminale.== 
>**Ogni volta che si apre un nuovo terminale WSL, la variabile viene persa e va reimpostata.**



#### 4. Client React
Ora che abbiamo avviato l'api in golang proviamo ad avviare il frontend in React.
Diamo un occhiata alle dipendenze del file `package.json`: 
```json
"dependencies": {
	"@tanstack/react-query": "^4.22.4",
	"axios": "^1.2.3",
	"react": "^18.2.0",
	"react-dom": "^18.2.0"
},
```

- **`react: ^18.2.0`** → è il core di **React** — ==la libreria principale per costruire l'interfaccia utente a componenti==
- **`react-dom: ^18.2.0`** → ==è il layer che permette a React di **renderizzare i componenti nel browser**, traducendoli in elementi HTML reali nel DOM==
- **`axios: ^1.2.3`** → è una libreria per fare **chiamate HTTP** — ==in questo caso viene usata per fare le richieste alle due API (Node.js e Golang) e ricevere i dati JSON==
- **`@tanstack/react-query: ^4.22.4`** → ==è una libreria per la **gestione delle chiamate asincrone** in React.== 
	- ==Semplifica il fetching dei dati dalle API gestendo automaticamente loading, errori, cache e refresh dei dati==


> [!abstract] **Come si collegano tra loro**
> **Nel contesto di questa applicazione il flusso è:**
>```text
> react-query → chiama axios → che interroga le API Node.js/Golang
>	↓
>React + react-dom renderizzano i dati ricevuti nel browser
>```

Prima di avviare l'applicazione seguiamo i passaggi mostrati nel file `README.md`:
```markdown
nvm ls
nvm use node 19.4
npm install
npm run dev
```

Ora per eseguire al meglio questi comandi nel giusto contesto vediamo il flusso: 
```shell
# navigo nella cartella '05-example-web-application'
cd "/mnt/c/Users/Project Lead/Desktop/Docker-test/05-example-web-application"
# Dopodiché assicuriamoci di usare la versione corretta di node(v19.4)
nvm use 19.4

# visualizziamo i file e le directory della cartella di progetto
ls

# navighiamo dentro la cartella 'client-react'
cd client-react/

# installiamo le dipendenze del progetto React + Vite
npm install

# Ora facciamo partire l'applicazione 
npm run dev
```

In alternativa a tutti questi comandi possiamo eseguire, per le esecuzioni successive dalla cartella `05-example-web-application`, il CLI: 

```shell
# Avvia il client in development mode
make run-client-react # definito nel Makefile
```


`make run-client-react`: 
- avvia il frontend React con **Vite** — ==un build tool moderno pensato per lo sviluppo frontend, che offre un server di sviluppo molto veloce con hot reload automatico.==

>[!warning] **Attenzione!** 
>==`make run-client-react` non esegue `npm install` — se aggiungi nuove dipendenze al progetto dovrai eseguire manualmente `npm install` dentro la cartella `client-react` prima di riavviare.==

> [!Note] **Nota importante**
>  ==L'obiettivo di questa sezione non è eseguire l'applicazione in locale in modo tradizionale, ma capire come i singoli componenti si collegano tra loro prima di containerizzarli completamente. Il workflow di sviluppo con Docker verrà approfondito nelle sezioni successive del corso.==
