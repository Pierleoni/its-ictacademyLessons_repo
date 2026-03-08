

# Introduzione : da JDBC a Spring

Fino ad ora abbiamo visto come [[Lezione 21 - JDBC(Java Database Connectivity)#JDBC — Java Database Connectivity|JDBC]] permetta di comunicare con un database in modo diretto ed esplicito: 
- si apre una connessione, 
- si scrive la query SQL, 
- si itera sul `ResultSet`, 
- si chiude tutto. 
Funziona, ma in un'applicazione reale questo approccio diventa rapidamente **verboso e ripetitivo** — ==ogni operazione richiede decine di righe di codice per gestire connessioni, eccezioni e risorse.==

Inoltre JDBC lavora a **basso livello**: 
- ==sei tu a scrivere ogni query SQL, a mappare ogni riga del `ResultSet` su un oggetto Java, a gestire le transazioni manualmente.== 
In un'applicazione enterprise con decine di entità e centinaia di operazioni, questo diventa insostenibile.

È qui che entra in gioco **Spring**: 
- ==un framework che astrae tutta questa complessità, permettendo di concentrarsi sulla logica applicativa invece che sulla gestione dell'infrastruttura.== 
**Spring non sostituisce JDBC completamente:**
- ==lo usa internamente  sollevandoci dalla responsabilità di gestirlo direttamente.== 
Studiare JDBC prima di Spring non è quindi tempo sprecato: 
- ==è esattamente la base concettuale su cui Spring costruisce le sue astrazioni.==

## Le Applicazioni Distribuite
Prima di entrare in Spring, è necessario capire il contesto architetturale in cui opera. 
Le applicazioni moderne non sono più monolitiche — sono **applicazioni distribuite**: 
- ==sistemi in cui i vari componenti si trovano su macchine distinte e cooperano scambiandosi dati e messaggi.==

> [!example] **Un esempio concreto:**
>  quando si scarica l'app mobile di Amazon, non si scaricano tutte le dipendenze di Amazon — si scarica solo l'interfaccia utente, che comunica con server sparsi in diverse parti del mondo. Questa separazione non è casuale, ma risponde a esigenze di **scalabilità e disponibilità**: se un server è sovraccarico, se ne aggiunge un altro; se uno cade, gli altri continuano a funzionare.

Per gestire questa complessità, le applicazioni distribuite vengono organizzate in **layer** — strati con responsabilità separate. L'architettura più diffusa è la **[[Lezione 1; Fondamenti delle Applicazioni Web#Architettura multilivello|three-tier]]**:

1. **[[Lezione 1; Fondamenti delle Applicazioni Web#^clientLayer|Client Layer]]** — ==l'interfaccia utente (browser, app mobile)==
2. **[[Lezione 1; Fondamenti delle Applicazioni Web#^logicLayer|Logic Layer]]** — ==la logica applicativa, ovvero il cuore dell'applicazione==
3. **[[Lezione 1; Fondamenti delle Applicazioni Web#^dataLayer|Data Layer]]** — ==il database e la persistenza dei dati==

Nelle prossime lezioni ci occuperemo principalmente del **Logic Layer**, simulando tutti e tre gli strati sulla nostra macchina locale.
[![Screenshot-2026-03-08-at-16-34-58-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png|381x173](https://i.postimg.cc/tCgPhWq2/Screenshot-2026-03-08-at-16-34-58-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png)](https://postimg.cc/Z01Cm9yd)

### 1. Client Layer — Il Livello di Presentazione

Il Client Layer è il livello più vicino all'utente: 
- ==il suo scopo principale è **visualizzare le informazioni e raccogliere i dati** tramite l'interazione con l'utente.==

Può assumere forme diverse:

- **Browser web** — ==l'utente accede all'applicazione tramite un URL==
- **Applicazione desktop** — ==una GUI (interfaccia grafica a finestre) installata sulla macchina==
- **Applicazione mobile** — ==come nell'esempio di Amazon che abbiamo visto==

In tutti i casi, il Client Layer non contiene logica applicativa né accede direttamente al database — ==si limita a **presentare i dati** che riceve dal Logic Layer e a **inviare le richieste** dell'utente verso di esso.==

Nel contesto delle applicazioni web, questo livello è tipicamente sviluppato con il trio classico:

- **[[HTML|HTML]]** — ==struttura della pagina==
- **[[CSS|CSS]]** — ==stile e presentazione visiva==
- **[[Lezione 1 I fondamenti Javascript#Javascript|JavaScript]]** — ==interattività lato client==

> [!remember] È importante sottolineare che il Client Layer è l'unico strato con cui l'utente interagisce direttamente — tutto ciò che accade nei layer sottostanti (logica e dati) è completamente trasparente per lui.

### 2. Logic Layer — Il Livello Applicativo

Il Logic Layer è il **cuore dell'applicazione**: 
- ==riceve le richieste dal Client Layer, le elabora applicando la logica di business, e interagisce con il Data Layer per leggere o modificare i dati.==

> [!tldr] **La logica di business è l'insieme delle regole e dei comportamenti specifici del sistema**
>  ad esempio: "un utente non può acquistare un prodotto se non è autenticato", oppure "il prezzo finale deve includere l'IVA". 
>  Queste regole non appartengono né all'interfaccia utente né al database — **vivono nel Logic Layer.**

Le operazioni che può compiere sul Data Layer sono:

- ==**Leggere** dati per restituirli al client==
- ==**Aggiungere** nuovi dati==
- ==**Modificare** dati esistenti==
- ==**Eliminare** dati==

La comunicazione con il Data Layer avviene tramite **librerie e [[Lezione 6 - API#API (Application Programming Interface)|API]]** — ed è esattamente il ruolo che abbiamo visto svolgere a JDBC e, come vedremo, a Spring.

Questo livello è tipicamente sviluppato con linguaggi come **Java, Python, PHP, Ruby o Perl**. Nel nostro caso useremo **Java con Spring**.

> [!link] **È importante notare il collegamento con quanto già visto:** 
> il [[Lezione 21 - JDBC(Java Database Connectivity)#3. Componente `LibroDAO`|`LibroDAO`]] che abbiamo scritto con JDBC è a tutti gli effetti un componente del Logic Layer — ==contiene la logica di accesso ai dati e fa da ponte tra l'applicazione e il database.==

### 3. Data Layer — Il Livello di Persistenza

Il Data Layer è il livello più basso dell'architettura three-tier: 
- ==il suo scopo è **archiviare e gestire i dati persistenti** dell'applicazione.== 

Interagisce esclusivamente con il Logic Layer — non comunica mai direttamente con il Client Layer.

Questo livello si realizza tipicamente con:

- **Database relazionali** — PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server
- **Database NoSQL** — Cassandra, CouchDB, MongoDB (per strutture dati più flessibili)
#### JDBC, Hibernate e Spring — L'evoluzione della persistenza

JDBC, come abbiamo visto, opera a **basso livello**: 
- ==il programmatore scrive direttamente le query SQL e gestisce manualmente la mappatura tra righe del database e oggetti Java.==
**Questo lo rende didatticamente prezioso — capire JDBC significa capire cosa succede "sotto il cofano"** — ma in un'applicazione enterprise diventa rapidamente verboso e ripetitivo.

**Hibernate** risolve questo problema: 
- ==il programmatore scrive le classi Java e Hibernate si occupa di generare le query SQL in background, usando JDBC internamente.== 
- ==Non si "sconfina" più nel SQL — si lavora esclusivamente con oggetti Java.== 
- ==Questo approccio si chiama **ORM** (Object Relational Mapping).==

**Spring** va ancora oltre, integrando Hibernate e aggiungendo un'infrastruttura completa per lo sviluppo enterprise.

>[!Note] **Nota sul corso:** 
> ==Per simulare il Data Layer nelle prossime lezioni useremo le **mappe Java** (`Map<K,V>`) al posto di un database reale.== 
> [[Lezione 13 - Le map in Java#Introduzione alle Map in Java|Le mappe]], come abbiamo già visto, sono strutture chiave-valore che ricordano sia la struttura di un JSON che quella di una tabella SQL — ovviamente con molta meno potenza, ma sufficienti per simulare la persistenza dei dati durante lo sviluppo del Logic Layer con Spring.


### Applicazioni Client-Server

Un sistema **[[Reti di computer#1. Modello Client/Server|client-server]],** [[Lezione 1; Fondamenti delle Applicazioni Web#Architettura Client- Server|come abbiamo già visto diverse volte]],  è: 
- un modello di rete in cui un programma detto **CLIENT** richiede servizi a un altro programma detto **SERVER**. 
Client e server girano tipicamente su macchine distinte collegate in rete, anche se — come faremo durante il corso — è possibile simulare entrambi sulla stessa macchina locale.

Le regole generali sono tre:

1. Il **server** eroga servizi su richiesta
2. Il **client** si collega al server e richiede servizi
3. Client e server devono aver concordato un **protocollo di comunicazione**

> [!example] Un esempio chiarificatore è **Gmail**: 
> quando arriva una nuova email si ha la sensazione che sia il server ad agire di sua iniziativa. 
> In realtà è l'applicazione Gmail che, in background, continua ad interrogare il server a intervalli regolari fino a quando non riceve nuovi dati. Il server non "spinge" mai dati al client — è sempre il client che li va a chiedere.

### Le Applicazioni Web

Le applicazioni web sono **particolari applicazioni distribuite** che adottano l'architettura client-server e comunicano tramite il protocollo **TCP/IP**. Si dividono in due famiglie principali:

**1. Applicazioni a pagine:**
- il client è l'utente che, tramite browser, richiede un servizio al server e riceve in risposta una **pagina web**. Esempio: l'utente si collega al sito di Ryanair, naviga tra le pagine e visualizza i voli disponibili.

**2. Applicazioni a servizi:**
- il client è un **programma** che richiede un servizio al server e riceve in risposta **dati strutturati** (tipicamente JSON), non pagine web. Esempio: Skyscanner non ha i voli di Ryanair, EasyJet o altre compagnie nel suo database — fa da intermediario, interrogando i server delle singole compagnie e aggregando i risultati per mostrarli all'utente. In questo caso Skyscanner è esso stesso un client che parla con altri server.

>[!important] Questa distinzione è fondamentale per capire cosa costruiremo con Spring: 
>-  ==non applicazioni a pagine, ma **applicazioni a servizi** — componenti del Logic Layer che espongono dati in formato JSON e comunicano con altri programmi, non direttamente con l'utente finale.==

%% Contiunare da qui in giù %%
Quindi le applicazioni web sono particolari applicazioni dsitruite che usano il client - server 
Caratterisctiche 
Utilizzano il protocollo TCP/IP 
si dividono in 2 famiglie principali 
- Applicazioni a pagine → il client è l'utente, attraverso il browser, chiede un servizio al server in risposta una pagina web 
- Applicazioni a servizi → il client è un programma che cihede un serivzio al server e riceve in risposta 
Esempio: a pagine 
Il client si collega si collega via browser con il sito di rynaair per vedere i voli, ovviamente interagisco e visualizzo con le diverse pagine del sito 
Esempio : a servizi 
Il client si collega via browser a skyscanner che restituisce in modo un po statisco le varie compagnie che offrono il volo per quella località.
Questo perché per questi servizi fanno da consulente/ intermediaro client per te per scambiare JSON tra i vari server ryanair, easyjet, etc. 
### Caratteristiche di un’applicazione a servizi
1. Il client è un programma (come il server)
	-  Applicazione Android
	-  Applicazione IOS
	-  Browser che esegue codice Javascript in una pagina web
2. Client e server si scambiano SOLO dati
3. Il sistema client-server è interoperabile
	- Client e Server possono essere scritti con infrastruttura tecnologica e linguaggi indipendenti
4. La realizzazione segue uno di questi 2 stili principali:
	-  SOAP (stile classico)
	-  REST (nuovo stile)
### Protocollo TCP/IP
 Un protocollo è un insieme di regole per dialogare.
 Il protocollo TCP/IP è il protocollo utilizzato sul web
 Le figure base sono Client e Server
 Principio base: Il client invoca il server (mai il contrario)
 Il protocollo TCP/IP è una famiglia di protocolli composta da 4 livelli
 Ogni livello si occupa di un aspetto e prevede un set di regole
 I livelli sono: applicazione, trasporto, rete, fisico

#### Livelli del protocollo
 Il dialogo avviene correttamente solo se per ciascuno dei 4 livelli viene
utilizzato lo stesso sotto protocollo.
 Livello fisico  protocollo nativo
 Livello rete  IP
 Livello trasporto  TCP e UDP
 Livello applicazione 
vari protocolli specifici per varie esigenze
 HTTP  hyper text
 FTP  file di grandi dimensioni
 SMTP  mail
 ecc


### Protocollo HTTP: descrizione
 Il server offre servizi ed è in attesa del client
 Il client chiede un servizio indicando:
 URL → protocollo, ip, porta e path verso la risorsa da agganciare
```http
http://IP:port/path/resource
```
 VERB  sono parole codificate dal protocollo che servono a indicare il tipo di
azione che si vuole compiere sulla risorsa indicata dalla URL
In ambito REST si considerano solo le seguenti:
 GET  lettura
 POST  inserimento
 PUT  modifica totale
 PATCH  modifica parziale
 DELETE  cancellazione

### Traposto dei dati 
Il dato chie viene trasposrto nel body della richiesta, 
Se si fa una richiesta request il dato viene messo nel body. 
Il client ha 3 modi di inviare dati al server:
 Utilizzando la query string che si accoda alla URL
```http
http://ip:port/path/resource?var1=aaa&var2=bbb
```
 Inserendoli direttamente nella URL
```http
http://ip:port/path/resource/aaa/bbb
```
 Inserendoli nel body della richiesta
 Il server invece ha un solo modo di inviare dati:
 Inserendoli nel body della risposta

In uscita (Response object): se si hanno un oggetto pcon più valori lo si mette nel body del json. 

### Il formato JSON 
È simile all'XML, ma moto più leggero 
Questo è un oggetto rappresentato in formato JSON
Le proprietà sono racchiuse da {…} e separate da virgole.
Sono indicate con
nome (stringa) : valore (in base al tipo di variabile)
Il valore può essere numerico, testo oppure un oggetto strutturato in json
 Sia client che server possono inviare dati in formato JSON e devono
specificarlo nel content-type dell’header (della richiesta/risposta) in
questo modo:
```json
content-type=‘application/JSON’
```
Inoltre un JSON può contenere un oggetti basta mettere un alra chiave il cui valore è un oggetto json. 

## Spring 
Spring è un framework: 
un framework implementa l'inversione di controllo. 
Cioè fai una classe o un metodo e poi fai in modo che non venga mai chiamato in modo esplictito( il `.start()` dei Thread o il `toString()`). 
Questa cosa funziona meglio con l'ovverriding: ad esempio se stampiamao un oggetto che non implementa il `toString()` viene comunque stampato perché lo ovverrida da Object (seguendo il concetto di binding dinamico e  VMI). 
Quindi Spring andremo a creare una nostra classe, sapere come fa ad istanziarle (perché non abbiamo più il main) e sarà spring ad istanziarle e fare partire i metodi di quella classe al momento giusto.
Il framework è una librearia che gestisce i tui componenti tramite l'inversione di controllo.
Mentre una librearia fa il lavoro inverso: fino ad oggi abbiamo usato librerie come `ArrayList`; ovvero componenti passivi che noi istanziavamo, popolovamo e richiamavamo i suoi metodi e li facevamo partire. 

Spring è uno dei framework più famosi utilizzati in java.
E’ composto da una serie di progetti che aiutano
nella gestione delle principali problematiche nello
sviluppo di applicazioni:
-  Spring Web Flow per applicazioni web a pagine o a servizi
- Spring Data per la gestione della persistenza
- Spring Mobile, estensione di spring web per applicazioni mobile
- Spring Integration per l’integrazione di applicazioni aziendali
- Spring Security per gestire autenticazioni e autorizzazioni
Ognuno di questi sono dei framework che fanno l'inversione di controllo. 
Possiamo immaginarli come dei pacchetti ognuno con l proprie peculiarità 
Spring boot è: si occuppa della gesgione dei jar nel pom.xml 
Mentre un progetto maven è: un progetto che dipendera in questo caso dallo spring boot e serve per organizzare e gestire le diepndenze di un progetto Spring 
E dipende da uno Spring Boot. 
### Spring web
Spring web è il modulo di Spring che offre il supporto alla
realizzazione di applicazioni web con architettura MVC
 Il pattern MVC è un pattern architetturale
che propone di scomporre il sistema in 3 livelli:
1. Model → logica business (Backend)
2. View → strato presentazione (Frontend)
3. Controller → coordinamento Model/View 
	- Il controller serve per coordinare e dissacoppiere model e view. 
	- Questo perché in questo design pattern non si devono mai parlare quindi tutte le chiamate tra view e model rimbalzano su di lui.
	- Quindi il controller è una sorta di centralino e mediatore tra model e view ed è anche quello che si interfaccia con l'esterno quindi fa anche da punta di ingresso con i client. 
e rispettare lo schema di comunicazione
v → C → M → C → V

È un desgin pattern strutturale.
### Spring Boot
 Per utilizzare Spring web è necessario scaricare le librerie relative a questo modulo
 Le librerie si possono ottenere in questi modi:
-  scaricarle a mano → scelta sconsigliata, bisogna anche scaricare tutte le sottodipendenze
	- Aprire Eclipse > Menu Help>Eclipse Marketplace > Cercare Spring Tools (aka Spring Tool Suite) 5.0.1 Realease > Installare il plugin> Una volta finito l'installazione > Menu File> Project... > Cartella Spring Boot>Spring Starter Project>mettere il nome del progetto > Voce Type (stavbilisce in che modo gestire le dipendenze)> segliere la voce Maven > Java Version > Dalla versione 17 in su > Package > `com.nomeSocieta. nomePachetto`. 
	 Cliccakre su next> ora dobbiamo dire che dipebdenze usare > cercare nella casella di testo "Spring web" > flaggare la casella > cliccare su  "finish"
 creare un progetto Maven  scelta consigliata, perché gestisce tutte le sottodipendenze
 creare un progetto Spring Boot  scelta ottimale, perché configura Maven e lo attiva
 Spring Boot è un tool che aiuta nella
configurazione di un progetto spring.
 Se si lavora con Eclipse è possibile
scaricare il plugin per la creazione
di progetti Spring Boot.
il plugin 4.x funziona con versioni di Eclipse >= 2021


### Scomporre il Model 
Il pattern MVC sfferma che i componenti controller dovrebbero fare il coordinamento dei componenti model e NON devono contenere logica di business. 
Quindi l'esercizio della calcolatrive per quanto banali i metodi contenevano logica di bussiness, in realta il controller dovrebbe fare da centralino tra la view e il client. 
Tipicamente si usa scomporre il model in 3 layer principali: 
1. Layer service → classi che contengono la logica di bussiness ad alto livello. 
2. Layer dao → classi che contengono la logica di basso livello e quindi i meccanismi per l'accesso ai dati persistenti
	- QUeste classi dialogano col database o con gli ORM 
3. Layer entity → classi che modellano le entità del dominio ai dati sakvati nelle tabelle del db.
Cosa c'entra con la stratificazione del web server? 
Il dao verra invocato dal layer service, il layer service incapsula il DataSource e tra il layer service e il layer dao si scambiano le entità.
COme il dao incapsula ed usa il data source a noi non interessa. 


### IL DTO 
Le classi controller scambiano dati con il client con il client.
Questi oggetti vengono trasformati da Spring da java in JSON e viceversa
Le classi DTO(DATA Transfer Object) sono le classi che rappresentano gli oggetti da inviare al client (o da ricevere dal client).
I DTO sono simili alle classi entity ma posso raggrupare anche dati diversi entity(es. studenti con gli esami superati).
Perché non usare direttamente gli entity? 
1. Gli entity sono mappatti sulle tabelle(se si vuole tirare fuori i dati di una join l'entity non c'è l'ha, devi fare un DTO)
2. Gli entity sono disaccopiati dallo strato controller(In questo modo lo strato controller non li vede gli entity.) 
3. Gli entity pottebbero essere collegati ad un ORM (es. Hibernate) e nn devono essere toccatti fuori dal model(tipicamente i sistemi che usano spring usano Hibernate che permette di non scirvere il DAO perché lo fai lui; quindi quando si modifica l'entity Hibernate aggiorna autamaticamente il DAO).
Possiamo pensare ai DTO come le possibili queery/incroci tra le tabelle ma anche le query sulla singola tabella.
Gli entity sono le classi che corrispondono alle tabelle del DB, e gli oggetti corrispondono alle riga della tabella. 

### Le conversioni
Detto questo le classi Service scambiano DTO con le Controller e entity con i DAO e saranno quindi responsabili delle conversioni di tipo.
È preferibile creare delle funzioni di conversione riusabili che si possono poiszionare in una classe di utility separata.
```java
// metodi di trasformazione 
public static Utente daDTOAEntity(UtenteDTO dto){
	return new Utente(dto.getIdUtente(), dto.getNome(), dto.getCognome(), dto.getMail(), dto.getTelefono());
}

public static UtenteDTO daEntityADto(Utente ut){
	return new UtenteDTO(ut.getIdUtente(), ut.getNome(), ut.getCognome(), ut.getMail())
} 
```


### Inversione di controllo 

Una delle più famose caratteristiche di Spring framework è quella di
fornire un’implementazione dell’IoC principle.
 Il principio IoC – Inversion of Control - è un pattern per cui un
componente di livello applicativo riceve il controllo da un componente
appartenente a una libreria riusabile (solitamente un framework.

Quindi ci troviamo nel IoC quando abbiamo la nostra classe che viene invocata da un framework (es: il main) e la mia classe non parte finche non viene avviato il framework(in questo esempio il main).
Quindi finora è spring che ha chiamato le nostre classi nel controller. 
QUindi le classi sono passive e il frmaework è la parte passiva (Il Ioc viene detto anche il principio di hollywood). 
Inoltre se il controller che invoca le nostri classi non si trova nel pacchetto base il framework non lo trova.
Ad esempio quando abbiamo la notra applicazione e volgiamo istanziare un arrayList dal JSE Library in quel caso sarà la nostra applicazione ad essrre attiva perché basta importate la libreria degli arrayList mentre in questo caso con Spring sarà la nostra classe a diventare passiva e verrà chiamata dal framework.
Pensiamo al metodo run() dei thread: questo metodo non andrebbe mai chiamato direttamente perché non utilizza il multithreading ma va chiamato il metodo start() che invoca anche il run(). Questo è un esempio di IoC 
### Dependecy Injection 
La Dependency Injection è una forma di IoC
 Consiste nella capacità di un framework (detto Container) di creare
oggetti, in inversione di controllo, creando e settando anche gli
oggetti di cui sono composti (detti dipendenze).
 Esempio: il musicista
 Supponiamo di avere una classe Player che ha una dipendenza da Instrument
e di voler decidere il tipo di strumento dinamicamente.
 Per disaccoppiare musicista e strumenti devo creare l’interfaccia Instrument e gli
strumenti concreti che la implementano
 Infine posso chiedere a Spring Core di creare un player e di abbinargli
dinamicamente lo strumento che intendo fargli suonare
Ad esempio l'esercizio fatto della cartoleria: 
Avevamo la classe Magazzino e gli articoli che erano gomme e penne. 
Benchè la classe Magazzino non nominasse mai questi due prodotti nello specifico ma lavorava con entrambi perché lavorava con classe padre articolo.
é un particolare tipo di IoC ovverro: 
quando lo IoC instanzia l'oggetto può gestire le sue sotto- dipendenze : ovvero in questo caso si intendono le classi che dipendono dalla classe principale. 

Quindi per chiarrire se al Controller si danno le giuste cordinate è in grado di creare da solo il service, il DAO, i DTO e le entità. 

### Digramma delle classi delle esempio player
Abbiamo la classe player che ha un atttributo dell'interfaccia  instruments. 
L'interfaccia instruments ha un meotdo astratto play() che verra ereditato delle sotto- classi concrete Guitar, Violin e Drum
Inoltre la classe Player implementa anche un meytodo void playInstrument. 
Per usare l'attributo al fine di fare chiamate polimorifche all metodo play delle varie sottoclassi: 
quindi si usa una refenrce dell'interfaccia Instruemnt ma il tipo concreto dell'oggetto sarà un oggetto Guitar, Violin e Drum


### @Component e @AutoWired

L’annotation @Component si pone sulla classe che desidero venga
istanziata da Spring
 Un Component dovrebbe essere un javabean, cioè avere:
 costruttore 0-args
 getters/setters per le proprietà
 Se un Component ha una proprietà oggetto (non primitiva o String)
è possibile farla creare e iniettare da Spring usando l’annotazione
@Autowired sulla proprietà da iniettare
 La classe relativa all’oggetto da iniettare dovrà essere annotata
con @Component


#### Uso delle annotation
Classe Player: 
```java
@Component
public class Player{
	@Autowired
	private Instrument instrument; 
	
	public Player(){}; 
	
	public void playMyInstrument(){
		this.instrument.play();
	}
}
```





### Component primario
 Posso utilizzare l’annotation @Primary sotto l’annotation
@Component per indicare che quel componente è prioritario rispetto
agli altri dello stesso tipo.
 Quindi potrei impostare tutti gli strumenti come @Component e poi
aggiungere @Primary solo su di uno.

### Spring core 
Lo spring core è un IoC Container ed è responsabile di creare oggetti e iniettare le dipendenze, secondo le configurazione 

#### L'applicationContext 