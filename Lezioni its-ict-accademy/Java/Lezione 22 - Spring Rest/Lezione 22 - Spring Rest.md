# Introduzione applicazioni web 
Le applicazioni distribuite sono applicazioni in cui vari componenti che compongono il sstema si trovano su macchine destinte. 
Quindi i vari processi cooperano scambiandosi dati e messaggi 

Un applicazione distribuita è strutturata solitamente con un archiettetura multi layer 
Ongi laye è costituito da u n set di componenti 
ongi set di componenti un set di funzionalità. 
Quindi prima si aveva l'applicazione web dove il client vi accedeva digitanfo il nome di dominio sulla ricerca di browser ma ad oggi questw applicazioni web hanno esteso alla applicazioni mobile, cio non significa che quando si scarica l'app mobile di amazon si scaricano tutte le dipendenze di amazon, ma si scarica solo l'interfaccia utente con le sue funzionalità che comunica con i server amazon sparsi in diverse parti nel mondo. 
QUindi data la complessita di questa struttura si suddivide in layer, questo perché i server possono essere più di 1 fino ad esempio 30 server sparsi in giro per il globo. 
Ma a che pro? Per utilità e scalabilità del sistema. 
Come si stratifica? 
L'archittetura più diffusa è l'archittettura three-tier. 
Essa prevede: 
1. Client Layer 
2. Logic Layer 
3. Data Layer 
Ci occuperemo principalmente del logic Layer, per queste lelzioni simuleremo questi tre attori sul nostro host. 
#### Client layer 
Scopo principale : visualizzare le informazioni e raccogliere dati dall'utente → interazioni con l'utente 
Questo tier di livello superiore, ad esempio, può essere eseguito su un browser web, come applicazione o come GUI (finestra grafica). 
Generalmente, i tier presentazione web sono svilluapti utilizzando HTML, CSS e JS. 

#### Logic Layer 
Lo scopo è recupeare informazioni dal client tier elaborale e metterle in relazione con il data tier 
Questo tier è il livello intermedio contiene la logica di bussiness, un insieme specifico di regole e comportamenti che il sistema fornisce. 
Il tier applicativo può aggiungere, eliminare o modificare i dati nel data tier 

Il tier applicativo è tipicamente sviluppato utilizzando Python, Java, Perl, PHP o Ruby e comunica con il data Tier tramite API. 

#### Data tier Livello persistenza 
Scopo principale: archiviare e gestire i dati persistenti dell'applicazione, solitamente attraverso un database 
QUesto tier è il livello più basso e interagisce con il livello applicativo. 
Questo livello si realizza con database relazionali come PostgresSQL, MySQL, Oracle, MariaDB. 

JDBC è vecchia ma è utile per capire come funziona questa cosa. JDBC sconfina con SLQ ma con Hybernet non sconfina più cpn SQL ma perché con Hybernet si scrivono le classi e gli oggetti e poi le query le fai lui di background, usando JDBC, ma il programmatore non deve scriverle lui. 
In questo corso la persistenza verrà simulata tramite le mappe java perché sono costituite da coppie chiave-valore che ricordano la struttura di un JSON ma soprattutto le tabelle SQL. 
Ovviamente le tabelle sono più potenti delle mappe java. 


### Applicazioni client - server 
Un sistema client-server è un contesto applicativo di rete dove un programma detto CLIENT richiede servizi ad un altro programma detto SERVER
 Il programma cliente e il programma server girano tipicamente su macchine distinte collegate in rete.
Il Client potrebbe usare differenti dispositivi per collegarsi al Server
 Regole generali:
1. Il server eroga servizi (su richiesta) per i client
2. I client si collegano ai server e richiedono servizi
3. Client e server devono aver concordato un protocollo di comunicazione e scambio dati
Possiamo simulare un client - server sulla nostra macchina ad esempio 

Un esempio è GMAIL: quando si sta su gmail e arriva un email si ha la sensazione che il server abbia agito di sua iniziativa ma in relata è l'applicazione GMAIL che di backgorund continua ad interrogare un server di continuo, quindi anche quando si ha la sensazione che il server agisca di sua iniziattiva in realta è il client che di bakground continua ad interrogarla fino a che non eroga la richiesta.

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