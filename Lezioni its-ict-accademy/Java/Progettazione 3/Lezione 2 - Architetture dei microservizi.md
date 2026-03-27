# Architettura dei Microservizi

Fino ad ora abbiamo visto i microservizi da un punto di vista concettuale e commerciale — [[Lezione 1 - Applicazioni cloud a microservizi#Cos'è un'Applicazione a Microservizi|cosa sono]], [[Lezione 1 - Applicazioni cloud a microservizi#Monolite vs Microservizi — Il Confronto Visivo|perché convengono]], [[Lezione 1 - Applicazioni cloud a microservizi#Scalabilita di un applicazione a microservizi|come scalano]] e [[Lezione 1 - Applicazioni cloud a microservizi#Premessa al Concetto di Resilienza|come gestiscono i guasti]]. 
Ma non abbiamo ancora risposto a una domanda fondamentale: **come sono strutturati internamente e come comunicano tra loro?**

Un singolo microservizio, preso da solo, assomiglia molto a quello che abbiamo costruito negli esercizi precedenti — una applicazione Spring con [[Lezione 22 parte 2 - Spring framework#La Classe Controller|Controller]], [[Lezione 22 parte 2 - Spring framework#Il Service|Service]], [[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]], [[Lezione 22 parte 2 - Spring framework#DTO vs Entity|Entity]] e [[Lezione 22 parte 2 - Spring framework#Il DTO — Data Transfer Object|DTO]]. La vera complessità non sta nel singolo microservizio, ma in **come questi microservizi vengono esposti al mondo esterno** e in **come il sistema nel suo insieme viene orchestrato**.

Pensiamo all'esempio di Amazon: il client — che sia un browser, un'app mobile o un'app desktop — non può conoscere gli indirizzi IP di tutti i microservizi interni. Non può sapere dove gira il microservizio degli ordini, dove gira quello dei pagamenti, quante istanze sono attive in un dato momento. Avere questa complessità esposta direttamente al client sarebbe insostenibile.

La soluzione è introdurre componenti infrastrutturali dedicati che si occupano di orchestrare la comunicazione — il più importante dei quali è il **[[Lezione 1 - Applicazioni cloud a microservizi#Lo Scenario|Gateway]]:**
- ==È lui il punto di ingresso unico tra il mondo esterno e la rete interna dei microservizi, ed è attorno a lui che si costruisce l'intera architettura.== 


## Le Due Architetture dei Microservizi

Un'applicazione a microservizi si struttura su 2 livelli architetturali distinti — uno interno e uno esterno — ==che insieme definiscono sia come ogni microservizio è costruito che come comunica con gli altri==.


### Architettura Interna

L'architettura interna riguarda la struttura di ogni singolo microservizio preso individualmente. 
Non è nulla di nuovo — è esattamente l'architettura **Controller/Service/Repository** che abbiamo costruito negli esercizi precedenti, con Entity, DTO, Mapper e gestione degli errori. 
Ogni microservizio è a tutti gli effetti una piccola applicazione Spring autonoma, con il proprio database dedicato.
Se il microservizio prevede anche una [[Lezione 22 parte 2 - Spring framework#I Tre Livelli dell'MVC|View]] — ad esempio una pagina HTML — si aggiunge anche il layer di presentazione. Altrimenti, come nel nostro caso, il microservizio espone solo API REST.
### Architettura Esterna

L'architettura esterna riguarda invece i **meccanismi di comunicazione** tra i microservizi e con il mondo esterno. Guardando l'immagine, il punto cruciale è che i client — web e mobile — non comunicano mai direttamente con i singoli microservizi. Passano sempre attraverso l'**API Gateway**, che fa da unico punto di ingresso verso la rete interna.

I meccanismi di comunicazione tra i microservizi sono due:

- **Chiamate REST** — comunicazione sincrona tramite [[Lezione 4 - Protocollo HTTP 2 parte|HTTP]], come abbiamo già visto
- **Code e Broadcast** — [[Lezione 1 - Applicazioni cloud a microservizi#^comunicazioneAsincrona|comunicazione asincrona tramite]] sistemi di messaggistica, come nell'esempio dell'email di conferma dopo un pagamento

> [!info] **Il confine tra architettura interna ed esterna è netto:**
>-  ==l'interna riguarda **come** un microservizio è fatto,== 
>- ==l'esterna riguarda **come** i microservizi parlano tra loro.== 
>Sono due preoccupazioni completamente separate — e questa separazione è uno dei principi fondamentali del design a microservizi.

### Esempio di struttura 
Per comprendere meglio questa suddivisione analizziamo questa immagine: 
[![Screenshot-2026-03-26-at-11-45-13-Microsoft-Power-Point-Applicazioni-cloud-a-microservizi-Microse.png](https://i.postimg.cc/FFT6SN1y/Screenshot-2026-03-26-at-11-45-13-Microsoft-Power-Point-Applicazioni-cloud-a-microservizi-Microse.png)](https://postimg.cc/NLrbqh6F)

Abbiamo due client — un'applicazione web e un'applicazione mobile — che vogliono accedere ai servizi di un e-commerce. Entrambi inviano le loro [[Lezione 4 - Protocollo HTTP 2 parte#Struttura delle Request e delle Response HTTP|richieste HTTP]] non direttamente ai microservizi, ma all'**[[Lezione 6 - API#API (Application Programming Interface)|API]] [[Lezione 1 - Applicazioni cloud a microservizi#^8e68e0|Gateway]]**: 
- ==il punto di ingresso unico dell'applicazione, che fa da "portiere" smistando ogni richiesta al microservizio corretto.==

**In base alla richiesta ricevuta, il Gateway la inoltra al microservizio appropriato:** 
- `Catalog` per consultare i prodotti, 
- `Shopping Cart` per gestire il carrello, 
- `Discount` per applicare sconti, 
- `Ordering` per gestire gli ordini. 
Ognuno di questi microservizi ha il **proprio database dedicato:** 
- ==nessuno condivide i dati con gli altri, rispettando il principio di autonomia che abbiamo visto in precedenza.==

### La DMZ — Zona Demilitarizzata

Nell'architettura a microservizi la sicurezza della rete interna è fondamentale — **i microservizi devono poter comunicare tra loro in modo sicuro, senza essere esposti direttamente a internet.** 
È qui che entra in gioco la **DMZ** (Demilitarized Zone).

La **DMZ** è: 
- ==una zona "franca" che separa la **rete non protetta** (internet) dalla **[[Reti di computer#^bc9db9|LAN]] interna** dove vivono i microservizi.== 
Funziona come un buffer di sicurezza a doppio strato:

- **Firewall esterno:**
	- ==primo filtro che blocca le chiamate indesiderate provenienti da internet.== 
	- ==La rete esterna conosce solo l'IP del firewall, non sa nulla di quello che c'è dietro.== 
- **API Gateway:**
	- ==unico punto di accesso autorizzato alla rete interna.== 
	- ==Tutte le richieste legittime passano attraverso di lui.==
- **Firewall interno:**
	- ==secondo filtro di protezione nel caso in cui il firewall esterno venga superato.==

Grazie a questa struttura, i microservizi nella rete interna possono comunicare tra loro nella fiducia di un ambiente sicuro — senza preoccuparsi di filtrare o validare le richieste in ingresso, perché ci ha già pensato la DMZ.

>[!example] **Analogia Condominio:**
>È esattamente come un condominio con cancello elettronico e portiere: 
>- ==il cancello (firewall esterno) blocca gli estranei,== 
>- ==il portiere (Gateway) decide chi può entrare,== 
>- ==e una volta dentro gli inquilini (microservizi) possono muoversi liberamente in un ambiente protetto.==

[![Screenshot-2026-03-27-at-11-06-07-Microsoft-Power-Point-Applicazioni-cloud-a-microservizi-Microse.png|335x203](https://i.postimg.cc/sg00TyRs/Screenshot-2026-03-27-at-11-06-07-Microsoft-Power-Point-Applicazioni-cloud-a-microservizi-Microse.png)](https://postimg.cc/jDPXjp5F)
###  Il Boundary — Il Perimetro dell'Applicazione

Tutto ciò che abbiamo visto finora — microservizi, database, Gateway, DMZ — ==vive all'interno di un **perimetro logico e infrastrutturale** ben definito che separa l'intero sistema dai sistemi esterni.== 
Questo confine si chiama **Boundary**.

**Il Boundary non contiene solo i microservizi applicativi, ma tutto ciò che è necessario per far funzionare il sistema nel suo insieme**:

1. **Microservizi e database** — ==i servizi applicativi veri e propri, ognuno con il proprio database dedicato come abbiamo già visto.==

2. **Servizi infrastrutturali** — componenti che NON contengono logica di business ma sono INDISPENSABILI per il funzionamento dell'architettura:

	- **Configurazione** — ==gestisce le configurazioni centralizzate di tutti i microservizi==
	- **Registry** — ==tiene traccia di quali microservizi sono attivi e dove si trovano==
	- **Gateway** — ==il punto di ingresso unico che abbiamo già analizzato==

3. **Sistema di messaggistica a code:**
	- ==strumenti come **Kafka** o **RabbitMQ** che gestiscono la [[Lezione 1 - Applicazioni cloud a microservizi#^fdb296|comunicazione asincrona tra i microservizi]] — l'equivalente infrastrutturale dell'esempio dell'email di conferma che abbiamo visto.==

4. **Orchestrazione** — **Kubernetes:**
	- ==lo strumento che gestisce automaticamente il ciclo di vita dei microservizi:== 
		- ==li avvia,== 
		- ==li scala,== 
		- ==li riavvia in caso di guasto.==

5. **Componenti di sicurezza interna:** 
	- ==gestione delle identità e degli accessi all'interno della rete interna.==

6. **Logging e monitoring condivisi:**
	- ==sistemi centralizzati per monitorare lo stato di tutti i microservizi e raccogliere i log in un unico posto:== 
		- ==indispensabili in un sistema distribuito dove i problemi possono manifestarsi in qualsiasi punto della rete.==

>[!info] Il Boundary è quindi la risposta alla domanda "dove finisce la nostra applicazione e dove inizia il mondo esterno?". 
> Tutto ciò che è dentro il Boundary è sotto il controllo e la responsabilità del team di sviluppo — tutto ciò che è fuori è internet, cioè territorio non controllato.
###  Il Gateway

Il **Gateway** è la porta logica dell'applicazione a microservizi — ==l'**entry point** unico che collega il mondo esterno all'ecosistema dei microservizi interni al Boundary.==

È il componente più strategico dell'architettura esterna perché accentra in sé tutte le responsabilità trasversali che altrimenti ogni microservizio dovrebbe gestire autonomamente:

1. **Sicurezza e autenticazione:**
	- ==tutte le richieste in ingresso vengono validate dal Gateway prima di essere inoltrate ai microservizi interni.== 
	- ==Un microservizio non autenticato o una richiesta malformata viene bloccata qui, senza mai raggiungere la rete interna.==

2. **Rate limiting:**
	- ==il Gateway limita il numero di richieste che un client può fare in un dato intervallo di tempo, proteggendo il sistema da abusi, attacchi DDoS e sovraccarichi improvvisi.==

3. **Load balancing:** 
	- ==distribuisce le richieste in arrivo tra le varie istanze dello stesso microservizio, garantendo che nessuna istanza sia sovraccaricata mentre le altre sono inattive.== 
	- ==È il meccanismo che rende concreta la scalabilità orizzontale che abbiamo visto in precedenza.==

4. **Instradamento:** 
	- ==in base all'URL e al tipo di richiesta, il Gateway determina quale microservizio deve gestirla e la inoltra all'istanza corretta, consultando il **Registry** per conoscere gli indirizzi aggiornati.==

> [!link] **Nota il parallelismo con il Controller che abbiamo visto nelle nostre applicazioni Spring:** 
> esattamente come il [[Lezione 22 parte 2 - Spring framework#La Classe Controller|Controller]] fa da centralino tra il client e i layer interni dell'applicazione, il Gateway fa da centralino tra internet e la rete interna dei microservizi. 
>>[!attention] ==La differenza è che il Gateway opera a livello infrastrutturale — non contiene logica di business, solo logica di instradamento e protezione.==

## I Tre Microservizi Infrastrutturali

Ora che abbiamo compreso cos'è il Boundary — il perimetro che contiene tutta la nostra applicazione — possiamo approfondire uno degli aspetti che ho solo accennato: **i servizi infrastrutturali**.

Nel Boundary, accanto ai microservizi di business (come `Catalog`, `Ordering` o `Shopping Cart`), troviamo **tre microservizi speciali** che non contengono logica di business ma sono **indispensabili per il funzionamento stesso dell'architettura**. Sono loro a rendere possibile la coordinazione di un sistema distribuito composto da decine o centinaia di servizi.

Questi tre servizi infrastrutturali sono:

#### 1. Configurazione Centralizzata

Immagina di avere 20 microservizi, ognuno con il proprio file `application.properties` che contiene:

- l'URL del database,
    
- le credenziali di accesso,
    
- i timeout delle connessioni,
    
- gli endpoint dei servizi esterni.
    

Se devi cambiare una configurazione — ad esempio l'URL del database perché stai passando dall'ambiente di sviluppo a quello di produzione — **dovresti modificare 20 file diversi e riavviare 20 microservizi**. Un incubo.

Il **Config Server** risolve questo problema:

- ==centralizza **tutte** le configurazioni di **tutti** i microservizi in un unico luogo.==
    
- ==Ogni microservizio, all'avvio, non legge il proprio file locale ma **chiede al Config Server** quali sono le sue configurazioni.==
    
- ==Le configurazioni diventano così **un punto unico di verità**, gestito centralmente.==
    

> [!example]  È come se ogni inquilino di un condominio, invece di tenere le proprie chiavi, le ritirasse ogni giorno dal portiere — così se si decide di cambiare la serratura del cancello, basta dare le nuove chiavi al portiere, non a tutti i residenti.
>

#### 2. Registry

Abbiamo detto che il Gateway deve inoltrare le richieste ai microservizi corretti. Ma come fa a sapere **dove si trovano** quei microservizi in un dato momento?

In un ambiente dinamico come Kubernetes, i microservizi:

- ==si avviano e si spengono continuamente,==
    
- ==cambiano indirizzo IP a ogni riavvio,==
    
- ==vengono scalati orizzontalmente creando nuove istanze.==
    

Il **Registry** (o Service Discovery) è l'elenco telefonico dell'architettura:

- ==Ogni microservizio, quando si avvia, **si registra** al Registry comunicando: "sono il servizio `Catalog`, mi trovo all'indirizzo IP `10.0.1.23` sulla porta `8081`".==
    
- ==Il Gateway, quando riceve una richiesta per il servizio `Catalog`, **chiede al Registry**: "dove si trova `Catalog` in questo momento?".==
    
- ==Il Registry risponde con l'indirizzo aggiornato, e il Gateway inoltra la richiesta.==
    

Se un'istanza muore o viene sostituita, il Registry ne viene a conoscenza e aggiorna la propria lista. 
==Il Gateway non ha mai bisogno di conoscere indirizzi statici — chiede sempre al Registry l'indirizzo **corretto in quel momento**==.

#### 3. Gateway

Del Gateway abbiamo già parlato in dettaglio nella sezione precedente — è il punto di ingresso unico che fa da "portiere" dell'intera architettura.

Rivediamone rapidamente le responsabilità alla luce dei due servizi appena introdotti:

- ==Riceve la richiesta dal client esterno==
    
- ==**Autentica** e **valida** la richiesta==
    
- ==Applica **rate limiting** per proteggere il sistema==
    
- ==**Chiede al Registry** dove si trova il microservizio destinatario==
    
- ==**Inoltra la richiesta** all'istanza corretta, eventualmente bilanciando il carico se ce ne sono più di una==
    
- ==**Restituisce la risposta** al client==
    

> [!info] **La trilogia infrastrutturale:**
> 
> - ==Il **Config Server** dice a ogni microservizio **come** deve configurarsi.==
>     
> - ==Il **Registry** dice al Gateway **dove** trovare i microservizi.==
>     
> - ==Il **Gateway** è il **punto di ingresso** che usa queste informazioni per instradare le richieste.==
>     
> 
> Senza uno solo di questi tre, un'applicazione a microservizi di medie-grandi dimensioni diventerebbe impossibile da gestire.

#### Approfondimento: Perché la Configurazione Centralizzata è Così Importante

==Abbiamo detto che il Config Server centralizza le configurazioni di tutti i microservizi.== 
Ma perché è così fondamentale? Per capirlo, dobbiamo considerare il contesto in cui opera un'applicazione a microservizi.

Un sistema di questo tipo può avere facilmente **decine di servizi**, sviluppati in momenti diversi, da team diversi, e potenzialmente anche con **linguaggi di programmazione diversi** (Java, Python, Node.js...). 
Ogni servizio ha le sue configurazioni: 
database, credenziali, endpoint esterni, timeout, feature flag, e così via.

Se ogni servizio gestisse la propria configurazione in un file `application.yml` locale — come abbiamo fatto finora negli esercizi — ci troveremmo di fronte a tre problemi concreti:

1. **Gestione incoerente:**
	- ==ogni team potrebbe organizzare le configurazioni in modo diverso, rendendo difficile capire dove cercare quando qualcosa non funziona.==
    
2. **Mancanza di uniformità:**
	- ==se un parametro come il timeout delle chiamate HTTP deve essere lo stesso per tutti i servizi, non c'è modo di garantirne l'uniformità se ognuno lo definisce per conto proprio.==
    
3. **Modifiche globali impossibili:**  
	- ==se devi cambiare l'URL del database di produzione per tutti i servizi, dovresti modificare decine di file, fare altrettante build, e riavviare altrettanti servizi. Un'operazione che da pochi minuti diventerebbe ore o giorni.==
    

Il **Configuration Server** risolve tutti questi problemi grazie a quattro caratteristiche fondamentali:

1. **Separa codice e configurazione:**  
	- La configurazione non è più impacchettata dentro il JAR/WAR del microservizio. 
	- Diventa un asset esterno, gestito indipendentemente dal codice. 
	- Questo significa che puoi cambiare un parametro senza dover ricompilare e ridistribuire il servizio.

2. **Centralizza la gestione:**   
	- Tutte le configurazioni di tutti i microservizi vivono in un unico posto (tipicamente un repository Git). 
	- Vuoi sapere come è configurato il servizio `Ordering` in produzione? Vai in un posto solo e lo scopri.

3. **Versiona la configurazione:** 
	-   Poiché le configurazioni sono gestite su Git, ottieni automaticamente la cronologia: chi ha cambiato cosa, quando, e perché. 
	- Puoi fare rollback se qualcosa va storto, esattamente come fai con il codice.

4. **Modifiche senza rebuild:**  
	- **Questa è la vera killer feature:** 
		- ==puoi cambiare una configurazione in produzione — ad esempio disabilitare una funzionalità problematica tramite feature flag — e **far sì che i microservizi la ricevano senza essere riavviati**. Basta un aggiornamento dinamico, nessuna downtime, nessuna ricompilazione.==

> [!example] **In sintesi:**  
> Con le configurazioni locali, ogni modifica richiede una nuova build, un nuovo deploy, un riavvio. 
> Con il Config Server, la configurazione diventa **viva e modificabile** mentre il sistema è in esecuzione. 
> In un ambiente dove la continuità di servizio è critica, questa non è una comodità — è una necessità.


### Spring Cloud Config — L'implementazione di riferimento

Finora abbiamo parlato del Config Server in termini concettuali — ==un componente che centralizza le configurazioni==. Ma come si realizza concretamente in un ecosistema Spring?

Il framework che implementa questo pattern si chiama **Spring Cloud Config**. 
==È una soluzione standardizzata per fornire una configurazione centralizzata in applicazioni distribuite, e in particolare in architetture a microservizi basate su Spring Boot==.

#### Come funziona Spring Cloud Config

Il sistema si compone di due attori:

1. **Il Configuration Server** — un microservizio speciale il cui unico compito è:
    
    - ==**Recuperare** le configurazioni da un backend di storage (un repository Git, un database, o anche il semplice file system)==
        
    - ==**Esporre** queste configurazioni via **[[Lezione 7 - Sistemi REST#Sistemi REST|API HTTP]]** ai microservizi che le richiedono==
        
2. **I Configuration Client** — tutti gli altri microservizi dell'applicazione:
    
    - ==All'avvio, invece di leggere il proprio `application.yml` locale, **fanno una chiamata HTTP** al Configuration Server dicendo: "dammi la configurazione per il servizio `Catalog` nell'ambiente `production`"==
        
    - ==Ricevono la risposta e si configurano di conseguenza==
        

##### Un dettaglio cruciale: l'ordine di avvio

C'è un aspetto fondamentale da tenere a mente:

> [!attention] **Il Configuration Server è il primo servizio che va avviato in tutta l'architettura.**

Ha senso, se ci pensi: 
- ==tutti gli altri microservizi, per potersi configurare, hanno bisogno che il Config Server sia già attivo e in ascolto.== 
- ==Se il Config Server non è partito, nessun altro microservizio può avviarsi correttamente.==

È il **servizio zero** — ==quello da cui tutto dipende, e che quindi deve essere il più stabile e resiliente possibile.==

#### Esempio concreto
Vediamo ora come si configura concretamente un Configuration Server con Spring Cloud Config. 
Lo snippet che segue mostra un tipico file `application.properties` per questo microservizio speciale:
```properties
# Identità del servizio
spring.application.name = config-server

# Profilo attivo
spring.profiles.active = native

# Configurazione per il profilo "native" — configurazioni lette dal file system
spring.cloud.config.server.native.search-locations = classpath:/config

# Disabilita compatibility verifier
spring.cloud.compatibility-verifier.enabled = false

# Porta su cui il Config Server rimane in ascolto
server.port = 8071
```

Analizziamo riga per riga:

1. **`spring.application.name = config-server`:**
	- ==Come per ogni microservizio [[Lezione 22 parte 2 - Spring framework#Spring Boot|Spring Boot]], diamo un nome a questo servizio. Nel caso del Configuration Server,== 
	- ==la convenzione è chiamarlo `config-server`.== 
	- ==Questo nome sarà utilizzato dal Registry per identificarlo.==

2. **`spring.profiles.active = native`:**   
	- Spring Cloud Config supporta diversi backend di storage per le configurazioni (chiamati "profili"):

		- `native`: 
			- ==le configurazioni vengono lette dal **file system locale**==
    
		- `git`: 
			- ==le configurazioni vengono lette da un **repository Git** (la soluzione più comune in produzione)==
    
		- `vault`: 
			- ==le configurazioni vengono lette da **HashiCorp Vault** (per secret management)==
    

	In questo esempio usiamo `native` per semplicità — utile in sviluppo o per capire il meccanismo.

3. **`spring.cloud.config.server.native.search-locations = classpath:/config`:** 
	- ==Con il profilo `native`, questa proprietà dice al server dove trovare i file di configurazione. `classpath:/config` significa "cerca nella cartella `config/` all'interno del JAR".==  

> [!Note] **_Nota:_**
>  se preferisci, puoi usare anche un percorso assoluto sul filesystem, ad esempio `file:/etc/config-server/`.

4. **`spring.cloud.compatibility-verifier.enabled = false`:** 
	- ==Disabilita il controllo di compatibilità tra le versioni di [[Lezione 22 parte 2 - Spring framework#Spring Boot|Spring Boot]] e Spring Cloud.== 
	- ==In alcuni ambienti questo controllo può generare warning fastidiosi quando le versioni non sono perfettamente allineate.==

5. **`server.port = 8071`:** 
	- ==La porta su cui il Configuration Server espone le sue API HTTP.== 
	- ==I microservizi client faranno chiamate a questa porta per recuperare la loro configurazione.== 
	- `8071` è un valore di esempio — in produzione potrebbe essere un'altra porta, ma è importante che sia **fissa e ben nota** dato che tutti i servizi devono sapere dove trovarlo.

> [!tip] **I due approcci principali:**
> 
> - **`native`** — ==semplice, ideale per sviluppo e test, ma richiede di distribuire i file di configurazione insieme al server==
>     
> - **`git`** — **l'approccio standard in produzione:** 
> 	- ==le configurazioni vivono in un repository Git, ottenendo versionamento, audit trail e aggiornamenti senza ricostruire il server==
>     

Nelle prossime sezioni vedremo come si configura un microservizio client per interrogare questo server all'avvio e recuperare le proprie impostazioni.

### Il Registry — Il DNS dei Microservizi

Abbiamo visto che il Configuration Server è il primo servizio da avviare — il "servizio zero". 
Subito dopo, nel boot order dell'architettura, c'è il secondo pilastro infrastrutturale: il **[[#2. Registry|Registry]]** (chiamato anche Service Discovery).

Ma cosa fa esattamente il Registry? Il suo scopo è semplice da capire ma cruciale per il funzionamento:
- ==gestisce e mantiene aggiornata la lista di tutti i microservizi disponibili, con tutti i dettagli necessari per contattarli: IP, porta, nome logico, numero di istanze attive, e così via.==

#### Come funziona nel dettaglio

Il meccanismo è simile a quello di un condominio con un tabellone all'ingresso:

1. **Registrazione all'avvio** — ogni microservizio, quando si avvia, si presenta al Registry e comunica:
    
    - ==il suo **nome logico** (ad esempio `catalog-service` o `ordering-service` — un nome stabile che non cambia mai)==
        
    - ==il suo **[[Network, Transport, Session, Presentation, Application Layers#Logical Addressing - IP Address|indirizzo IP]]** (che in un ambiente dinamico come Kubernetes può cambiare a ogni riavvio)==
        
    - ==la **porta** su cui è in ascolto==
        
2. **Aggiornamento continuo** — il Registry tiene traccia non solo di quali servizi sono attivi, ma anche:
    
    - ==quante istanze di ogni servizio sono in esecuzione in questo momento (grazie allo scaling orizzontale)==
        
    - ==lo stato di salute di ogni istanza (se risponde o meno alle richieste)==
        
3. **Scoperta per interrogazione** — quando il Gateway (o un altro microservizio) ha bisogno di contattare un servizio, non usa indirizzi fissi. Invece:
    
    - ==chiede al Registry: "dove si trova `catalog-service` in questo momento?"==
        
    - ==il Registry risponde con l'indirizzo IP e la porta dell'istanza (o delle istanze) attualmente disponibili==
        

> [!example] **Analogia:**  
> Il Registry è il **[[Modello TCP-IP#DNS Domain Name System (DNS)|DNS]] dei microservizi:** 
> Come per il DNS, che trasforma un nome di dominio (come `www.google.com`) in un [[Network, Transport, Session, Presentation, Application Layers#Logical Addressing - IP Address|indirizzo IP]], il Registry trasforma un nome logico di servizio (come `ordering-service`) nell'[[Network, Transport, Session, Presentation, Application Layers#Logical Addressing - IP Address|indirizzo IP]] e porta dove quel servizio è effettivamente in esecuzione in quel momento. 
> **La differenza è che il Registry è dinamico:** 
> - ==gli indirizzi cambiano in tempo reale mentre i servizi si avviano, si spengono e si scalano.==



> [!deep] #### Eureka — Il Service Registry di Netflix
>
>L'implementazione più famosa e utilizzata di questo pattern è **Eureka**, un Service Registry open source sviluppato da Netflix e integrato in Spring Cloud.
>
> **Cosa fa Eureka:**
>
>Eureka è un microservizio speciale che svolge tre compiti fondamentali:
>
>1. **Permette ai servizi di registrarsi all'avvio** — ==ogni microservizio client contiene un "Eureka Client" che, quando parte, chiama Eureka Server dicendo "sono qui".==
>
>2. **Permette ai servizi di scoprire dinamicamente gli altri** — ==quando un servizio (o il Gateway) ha bisogno di chiamare un altro servizio, chiede a Eureka: "dove si trova? quali istanze sono attive?".==
>
>3. **Espone il registro via API REST** — ==tutto ciò che Eureka sa è accessibile tramite semplici chiamate HTTP. Puoi puntare un browser all'endpoint di Eureka e vedere in tempo reale quali servizi sono registrati.==
>
>4. **Mantiene numero e stato delle istanze** — ==Eureka sa non solo quali servizi esistono, ma anche quante istanze di ciascuno sono attive e se sono "UP" (salute) o "DOWN" (guaste).==
>
>> [!attention] **Un chiarimento importante:**  
>> Il Registry **non si occupa dell'instradamento** — non decide dove mandare le richieste, non fa load balancing, non inoltra nulla. Il Registry si limita a **fornire informazioni** su dove si trovano i servizi. L'instradamento è responsabilità del Gateway (o del client che fa la chiamata).
>
>##### L'ordine di avvio: Registry dopo Config
>
>Abbiamo detto che il Configuration Server è il primo servizio ad avviarsi. Eureka è il **secondo**. C'è una ragione precisa per questo ordine:
>
> ==Il Registry DEVE caricare la sua configurazione dal Config Server prima di potersi avviare.==
>
>Questo significa che:
>
>1. **Prima** si avvia il Config Server (porta `8071` nell'esempio precedente)
 >   
>2. **Poi** si avvia Eureka, che:
 >   
  >  - Interroga il Config Server per sapere:
  >      
 >       - ==su quale porta deve ascoltare==
 >           
 >       - ==qual è il proprio nome==
 >           
 >       - ==dove trovare eventuali backend di persistenza==
  >          
  >      - ==parametri di comportamento (tempi di heartbeat, soglie di eliminazione, ecc.)==
  >          
  >  - Dopo aver ricevuto la configurazione, si avvia e si mette in ascolto per le registrazioni
  >      
>
>>[!faq] Cosa succede se Eureka non è attivo?
>>
>>Le conseguenze sono a cascata e bloccano l'intera architettura:
>>
>>- **I microservizi non si registrano** — all'avvio, ogni microservizio cerca Eureka per registrarsi. Se Eureka non risponde, il microservizio può:
  >>  
  >>  - ==andare in errore e terminare==
  >>      
  >>  - ==continuare a ritentare in loop, ma rimanere "invisibile" agli altri==
  >>      
>>- **Il Gateway non riesce a fare service discovery** — ==il Gateway, quando riceve una richiesta per, ad esempio, `catalog-service`, chiede a Eureka: "dove si trova?" Senza Eureka, non ottiene risposta, e la richiesta del client fallisce.==
 >>   
>>
>>In pratica, **senza Eureka, l'intero sistema è paralizzato**. 
>>Per questo motivo, nella sequenza di boot di un'applicazione a microservizi, Eureka è tra i primi componenti ad essere avviati — subito dopo il Config Server, ma prima di qualsiasi microservizio applicativo.

fino a pag 44