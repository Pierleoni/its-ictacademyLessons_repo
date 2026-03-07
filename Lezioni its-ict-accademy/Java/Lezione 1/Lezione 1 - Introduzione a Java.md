
# Introduzione a Java
Java è un linguaggio di programmazione nato all’inizio degli anni '90 con il nome di **Oak**, sviluppato dal **Green Team** di Sun Microsystems guidato da **James Gosling**. 
L’idea alla base era quella di creare un linguaggio **orientato agli oggetti (OOP)**, **indipendente dalla piattaforma**, robusto e sicuro, capace di affrontare le nuove esigenze del mercato del software emergente con l’espansione di Internet.

L’OOP (Object-Oriented Programming) non è solo una tecnica di programmazione, è un **paradigma:**
==ovvero un modello che definisce **principi e regole di progettazione** per strutturare il software in modo modulare, riutilizzabile e manutenibile.==

Una delle caratteristiche più importanti di Java fin dall’inizio è stata la **portabilità**: 
- ==il codice scritto in Java può essere eseguito su qualsiasi piattaforma senza modifiche.== 
Negli anni '80, invece, i software erano sviluppati in maniera artigianale: ciascun programma era progettato per una **macchina o server specifico**, rendendo difficile la distribuzione su scala più ampia. 
Con la diffusione di Internet negli anni '90, questa esigenza è diventata cruciale: un software house doveva poter distribuire il proprio prodotto **indipendentemente dall’hardware del client**. Java risolveva questo problema permettendo al client di eseguire il codice tramite una **[[#La JVM e l’indipendenza dalla piattaforma|Java Virtual Machine (JVM)]]**, senza preoccuparsi della piattaforma sottostante.
Java nasce nel 1991 con il nome di OAK, adesso la sua gloria è scesa a causa di Python. 

### Storia di Java
- **1992 – Star Seven (OAK)**  
    Il Green Team rilasciò un prototipo chiamato **Star Seven**, basato su quattro tecnologie sviluppate internamente:
    
    1. Il linguaggio **Oak**
        
    2. **GreenOS**, un sistema operativo sperimentale
        
    3. Una **interfaccia utente innovativa**
        
    4. Il **dispositivo fisico** stesso  
        Per presentare il sistema, il team utilizzò un personaggio chiamato **Duke**, che guidava l’utente all’interno del mondo virtuale.  
        Dopo questo progetto, il Green Team provò a entrare nel mercato della **TV on-demand**, ma dovette abbandonare l’iniziativa dopo alcuni anni.
        
- **1994-1995 – Nascita di Java**  
    Dopo il fallimento del progetto iniziale, Oak venne ripensato per il **web**. Nel gennaio 1995 il linguaggio fu **rinominato Java**. Nello stesso anno:
    
    - **Patrick Naughton e Chris Warth** (Van Hoff era coinvolto nello sviluppo di compilatori) scrissero un **compilatore dedicato**
        
    - Fu progettato **HotJava**, un browser scritto in Java per mostrare le potenzialità del linguaggio
        
    - Il **23 maggio 1995**, in occasione del SunWorld ’95, Sun Microsystems presentò ufficialmente Java
        
    - Nello stesso anno, **Netscape** incorporò Java nel suo browser, aumentando rapidamente la diffusione del linguaggio  
        Il successo fu immediato perché Java rispondeva alle nuove esigenze legate a **rete e Internet**, consentendo lo sviluppo di software portabile e interattivo sul web.
        
- **2010 – Java e Oracle**  
    Nel 2010 Sun Microsystems fu acquisita da **Oracle**, che da allora ha gestito lo sviluppo di Java. Oracle ha anche assorbito altre aziende produttrici di tecnologie **Java-oriented**, come **BEA Systems** e **MySQL**, consolidando la propria posizione nel mercato enterprise.

## Principali caratteristiche di Java
Java è un linguaggio molto apprezzato per una serie di caratteristiche che ne hanno favorito la diffusione e l’adozione sia in ambito accademico che industriale. Tra queste:
1. **Object Oriented (OOP)**  
    - Java è basato sul paradigma **object oriented**, che non è un linguaggio di per sé, ma un **modello di programmazione**. 
    - ==L’OOP organizza il software attorno agli **oggetti**, che rappresentano entità reali o concettuali, e ai **metodi** che operano su di essi.== 
    - I concetti chiave includono:
    
	    - **[[Lezione 8 - L'incapsulamento|Incapsulamento]]:** 
		    - ==che consente di nascondere i dettagli interni di un oggetto e di esporre solo ciò che è necessario.==
        
	    - **[[Ereditarietà e polimorfismo#Concetto di ereditarietà|Ereditarietà]]:** 
		    - ==che permette di creare nuove classi basate su classi esistenti, favorendo il riuso del codice.==
        
	    - **[[Ereditarietà e polimorfismo#Polimorfismo|Polimorfismo]]:** 
		    - ==che consente di trattare oggetti di classi diverse in modo uniforme quando condividono la stessa interfaccia o classe base.==
        
    
	Tra i linguaggi orientati agli oggetti coetanei di Java troviamo **C++**, **Objective C**, **Perl 5**, mentre linguaggi più recenti includono **Scala**, **Kotlin** e **Swift**. Alcuni linguaggi, come JavaScript, supportano l’OOP in maniera più limitata o “debole”.
    
2. **Semplice**  
    - Java è stato progettato per essere più semplice rispetto al C++ da cui deriva. Mantiene una sintassi familiare agli sviluppatori C/C++, ma elimina molti costrutti pericolosi:
    
	    - ==non permette l’aritmetica diretta sui puntatori==
        
	    - ==gestisce automaticamente la memoria tramite il **garbage collector**, evitando la de-allocazione manuale e gli errori ad essa associati==
        
    
    Java è completamente **tipizzato**, il che significa che i tipi di dati sono definiti in fase di compilazione, aumentando la sicurezza e la leggibilità del codice. 
    Un limite è che, essendo un linguaggio ad alto livello, Java ha un accesso ridotto alle funzionalità di basso livello; in questi casi si può ricorrere a **JNI (Java Native Interface)** per integrare codice nativo.
    
1. **[[#Indipendenza dalla piattaforma|Indipendente dalla piattaforma]]**  
    Uno dei punti di forza principali di Java è la **portabilità**. 
    Grazie alla **Java Virtual Machine (JVM)**, ==un programma scritto in Java può essere eseguito su qualsiasi piattaforma senza modifiche al codice sorgente.== 
    In pratica, si scrive il programma **una volta sola**, e la ==JVM si occupa di tradurre le istruzioni in un formato eseguibile sul sistema operativo sottostante, sia esso **Windows**, **Linux** o **macOS**.==

Esempio semplificato:

```java
public class Studente {     
	// codice della classe 
}
```

Questo codice potrà girare su qualsiasi piattaforma che disponga di una JVM compatibile, senza necessità di ricompilazione.

4. **[[#Robusto (affidabile)|Robusto e sicuro]]**  
    - Java include meccanismi di gestione degli errori e controlli di sicurezza che riducono i rischi di crash e vulnerabilità, contribuendo a creare applicazioni stabili.
    
5. **[[#Concorrente (Multithreading)|Concorrente]]**  
    - Java supporta il **multithreading**: 
	    - ==cioè la possibilità di eseguire più processi in parallelo all’interno dello stesso programma, sfruttando al meglio le risorse hardware moderne==.
    
6. **Gratuito e open source**  
    - Infine, Java è disponibile liberamente e con licenze open source, il che ne favorisce l’adozione e lo sviluppo di librerie e framework da parte della comunità.

### Linguaggi di programmazione e traduzione per la macchina

==Un **linguaggio di programmazione** è uno strumento che consente agli sviluppatori di **impartire istruzioni alla macchina** in modo strutturato e comprensibile per l'operatore umano.== 
Questo perché l’unico linguaggio realmente “leggibile” dal computer è il **linguaggio macchina ([[Le architetture di un Computer#il Codice Binario|codice binario]]) :** 
- ==costituito da sequenze di bit (0 e 1) che rappresentano direttamente comandi eseguibili dall’hardware.==

Scrivere direttamente in linguaggio macchina sarebbe estremamente complesso e soggetto a errori. Per questo motivo sono stati sviluppati i **linguaggi di alto livello**, come **C++**, **Java** o **Visual Basic**. 
==Questi linguaggi permettono di scrivere istruzioni comprensibili all’uomo, più vicine al linguaggio naturale, che devono poi essere **tradotte in linguaggio macchina** affinché la [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] possa eseguirle.==

![[Linguaggio macchina e linguaggi ad alto livello.png]]



### I linguaggi di programmazione: compilati e interpretati

I linguaggi di programmazione si suddividono principalmente in due macro categorie: **compilati** e **interpretati**.

#### 1. Linguaggi compilati 
Un linguaggio compilato utilizza un **compilatore**, un programma speciale con due funzioni principali:

1. **Controllo del codice**: 
	- ==Il compilatore rileva eventuali errori di **sintassi** (errori nella scrittura delle istruzioni) o di **semantica** (operazioni non consentite o tipi di dati incompatibili).==
    
2. **Traduzione in codice macchina**: 
	- ==Converte il codice sorgente in un formato eseguibile direttamente dalla [[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]], come un file `.exe` su Windows.==
    

Un esempio classico di linguaggio compilato è il **C**. 
È importante ricordare che un file compilato è **specifico per la piattaforma**: 
- ==un programma creato su Windows non funzionerà automaticamente su Linux o macOS senza una ricompilazione per la piattaforma di destinazione==.

![[Esempio linguaggio compilato in C.png]]

#### 2. Linguaggi interpretati 
I linguaggi interpretati, come **Java**, utilizzano un meccanismo diverso che li rende **portabili su qualsiasi piattaforma**, basato su **bytecode** e **interpreti**.

Il flusso di esecuzione è il seguente:

1. ==Il programmatore scrive il **codice sorgente**== (ad esempio `Esempio.java`).
    
2. ==Il codice sorgente viene **compilato in bytecode** (`Esempio.class`), un formato intermedio indipendente dalla piattaforma.==
    
3. ==Il **bytecode** viene eseguito dalla **[[#La JVM e l’indipendenza dalla piattaforma|Java Virtual Machine (JVM)]]**, istruzione per istruzione, senza creare un file eseguibile specifico==.
    

Il compilatore Java, come quello dei linguaggi compilati, ha due compiti principali:

- **Controllare il codice**: rileva errori di sintassi e di semantica.
    
- **Tradurre in bytecode**: crea un formato intermedio che la JVM può interpretare su qualsiasi sistema operativo.
    

![[Interprete.png]]


In questo modo, a differenza dei linguaggi compilati tradizionali, il codice Java può essere scritto **una sola volta** e poi eseguito su **qualsiasi piattaforma** dotata di JVM, garantendo la famosa caratteristica di Java:

> **“Write once, run anywhere”**.

### La JVM e l’indipendenza dalla piattaforma

==La **Java Virtual Machine (JVM)** è una specifica software che definisce come interpretare ed eseguire il **bytecode Java**.== 
Esistono diverse implementazioni della JVM per i principali sistemi operativi: 
==ciascuna traduce lo stesso bytecode in **istruzioni comprensibili dalla macchina sottostante**.== 
Questo meccanismo è ciò che garantisce la famosa caratteristica di Java:

> **scrivi una volta, esegui ovunque**.

Sebbene i linguaggi interpretati esistessero già prima di Java, l’uso dell’interpretazione divenne cruciale **negli anni ’90**, con la diffusione di Internet e la necessità di distribuire software su piattaforme diverse senza dover ricompilare il codice per ciascuna macchina. Java combinò così la sicurezza dei linguaggi compilati con la **portabilità tipica dei linguaggi interpretati**, diventando una soluzione ideale per applicazioni web e distribuite.
#### Come funziona l'esecuzione 
Il flusso di esecuzione in Java è il seguente:

1. ==Si scrive il **codice sorgente** in Java (`.java`).==
    
2. ==Il **compilatore Java** (`javac`) trasforma il codice sorgente in **bytecode** (`.class`).==
    
3. ==La **JVM** legge ed esegue il bytecode, traducendolo dinamicamente in istruzioni macchina specifiche del sistema operativo in uso.==
    

Il bytecode viene interpretato **istruzione per istruzione**, senza creare un file eseguibile specifico per la piattaforma. Grazie a questo meccanismo, lo stesso programma può funzionare su **Windows, Linux o macOS**, semplicemente utilizzando la JVM appropriata per ciascun sistema.

![[JVM.png]]

> [!info] Quando si installa Eclipse, il programma richiede il sistema operativo in uso: questo perché Eclipse integra Java al suo interno e utilizza l’interprete appropriato in base alla piattaforma.



> [!example] **Riassunto concettuale**
> 
> 
> - La **JVM** è l’**interprete** che permette al bytecode di funzionare su qualsiasi piattaforma.
>     
> - Ogni sistema operativo ha la sua **implementazione della JVM**, che traduce il bytecode in linguaggio macchina specifico per quella piattaforma.
>     
> - Il **bytecode** funge da “lingua comune” tra Java e il linguaggio macchina, permettendo alla JVM di comunicare con la **CPU e l’hardware**, pur mantenendo l’indipendenza dalla piattaforma.
>     
> 
> > [!ticket] **In breve:** la JVM interpreta il bytecode e lo traduce dinamicamente in istruzioni macchina specifiche, consentendo a Java di essere portabile e sicuro.
> 


### Indipendenza dalla piattaforma 
Come già detto in precedenza una delle caratteristiche che ha reso Java un linguaggio rivoluzionario  è l’**indipendenza dalla piattaforma**. 
==Questo significa che lo stesso codice sorgente può essere eseguito su sistemi operativi diversi senza modifiche, grazie all’uso del **bytecode** e della **[[#La JVM e l’indipendenza dalla piattaforma|Java Virtual Machine (JVM)]]**.==

Il processo funziona così: 
1. ==il codice sorgente (`.java`) viene compilato in **bytecode** (`.class`), un formato intermedio che non dipende dal sistema operativo.== 
2. ==Successivamente, ogni piattaforma utilizza la propria implementazione della **JVM** per interpretare il bytecode e tradurlo in istruzioni macchina specifiche per quel sistema operativo.==

Ad esempio:

- Su **Linux**, il bytecode viene eseguito dalla **JVM per Linux**.
    
- Su **Windows**, il bytecode viene eseguito dalla **JVM per Windows**.
    
- Su **macOS**, il bytecode viene eseguito dalla **JVM per macOS**.
    

In questo modo, lo stesso programma Java può funzionare su diverse piattaforme senza ricompilazioni, garantendo la portabilità e la facilità di distribuzione del software.
![[Indipendenza dalla piattaforma.png]]


### Robusto (affidabile)

Java è un linguaggio **robusto**, cioè: 
- ==progettato per ridurre al minimo errori e crash durante l’esecuzione dei programmi.== 
Questo si ottiene attraverso diversi meccanismi:

- ==Il **rilevamento degli errori** e il **type checking** avvengono sia a **tempo di compilazione** che a **runtime**, garantendo che il codice rispetti le regole dei tipi di dati e riducendo bug potenziali==.
    
- ==Java **maschera i puntatori all’utente**, evitando manipolazioni dirette della memoria che potrebbero causare instabilità==.


> [!faq] **Cos' e il mascheramento dei puntatori** 
> In Java (così come in Python), non si lavora direttamente con **puntatori** come nei linguaggi di basso livello (ad esempio C o C++).
>
>Un **puntatore**: 
>- ==è l’indirizzo di memoria in cui risiede una variabile==. 
>Nei linguaggi di basso livello è possibile manipolare direttamente questi indirizzi, ma ciò comporta rischi elevati, come accessi non controllati alla memoria o corruzione dei dati.
>
>Java e Python **mascherano i puntatori** tramite il concetto di **reference**. 
>==Una **reference** non è l’indirizzo di memoria vero e proprio, ma un “**telecomando**” che permette di interagire con l’oggetto a cui punta==. 
>In altre parole:
>
>- L’indirizzo è troppo “basso livello” e pericoloso per l’utente.
  >  
>- ==La reference permette di **pilotare l’oggetto**, eseguendo azioni sul suo contenuto senza accedere direttamente alla memoria.==
  >  
>
>Ad esempio, in Python:
>
>```python
>p = Persona()
>```
>
>Qui, ==`p` non è l’indirizzo della memoria dove si trova l’oggetto `Persona`, ma una **reference** che permette di manipolare l’oggetto in modo sicuro e controllato.==
>
>Questo approccio contribuisce alla **robustezza e sicurezza** del linguaggio, evitando errori comuni nella gestione diretta della memoria.
>
    
- La **gestione delle eccezioni:** 
	- ==permette agli sviluppatori di intercettare e gestire errori in modo controllato, senza bloccare l’intero programma.==
   
- La **gestione della memoria:** 
	- con allocazione automatica e **garbage collector (GC)**, libera automaticamente la memoria non più utilizzata, riducendo il rischio di memory leak e crash.

> [!faq] **Gestione della memoria (allocazione e garbage collector)**
> In Java, come in Python, la **gestione della memoria** è automatica e sicura, grazie al meccanismo di **allocazione e garbage collector (GC)**.
>
>Quando si crea un oggetto, il programmatore **non decide direttamente dove allocarlo in memoria**: 
>- ==questa scelta è delegata alla JVM.== 
>- ==Una volta allocato, l’oggetto rimane in memoria finché esiste almeno una **reference** che lo punti.==
>
>Gli oggetti **non più referenziati** vengono automaticamente identificati dal **garbage collector** come **riutilizzabili**. 
>==La memoria occupata da questi oggetti può quindi essere **sovrascritta** per allocare nuovi dati==.
>
>Questo meccanismo riduce notevolmente i problemi tipici dei linguaggi di basso livello, come i **memory leak** o gli accessi a zone di memoria non valide, contribuendo alla **robustezza e affidabilità** dei programmi Java.



Questi meccanismi rendono Java particolarmente affidabile e sicuro per lo sviluppo di applicazioni complesse e mission-critical.

### Concorrente (Multithreading)

Java supporta la **concorrenza:**
- ==cioè la capacità di eseguire più processi o parti di un programma **simultaneamente**, analogamente a come il sistema operativo gestisce il **multitasking**.== 
- In pratica, un programma può essere suddiviso in **thread**, ognuno dei quali svolge un compito specifico in parallelo agli altri.

Ad esempio, quando ti colleghi a un sito come `amazon.com`, tu vedi la pagina come un singolo utente, ma in realtà il server gestisce **centinaia o migliaia di client contemporaneamente**. 
Ogni connessione può essere considerata un thread separato che viene eseguito in parallelo agli altri.

Java mette a disposizione **API specifiche per il multithreading:**  
- ==permettono di creare e gestire thread in modo semplice e sicuro, senza doversi preoccupare della complessità della gestione dei processi a basso livello==.

Questo rende Java particolarmente adatto per applicazioni che richiedono **esecuzioni parallele**, come server web, applicazioni scientifiche, software di calcolo intensivo e qualsiasi programma che debba sfruttare al massimo le risorse del processore.
### Sicuro

La sicurezza è un altro punto di forza di Java, fondamentale soprattutto per applicazioni che gestiscono **informazioni sensibili** e comunicano attraverso la rete.

- Dal punto di vista architetturale, Java elimina i rischi legati ai **puntatori**, evitando manipolazioni arbitrarie della memoria, e previene il **stack overflow a runtime**.
    
- Inoltre, Java offre **[[Lezione 6 - API|API]] specifiche per la sicurezza**, tra cui:
    
    - **JCE (Java Cryptography Extension)** per crittografia e protezione dei dati
        
    - **JSSE (Java Secure Socket Extension)** per comunicazioni sicure su rete
        
    - **JAAS (Java Authentication and Authorization Service)** per gestione di autenticazione e autorizzazioni
        

Grazie a queste caratteristiche, Java consente di sviluppare applicazioni affidabili e sicure, adatte a scenari in cui la protezione dei dati è cruciale.

### Java: linguaggio e tecnologia

Java non è solo un linguaggio di programmazione, ma anche una **piattaforma tecnologica completa**.

- Come **linguaggio**, Java è tra i più utilizzati al mondo, apprezzato per la sua portabilità, robustezza e semplicità.
    
- Con il termine **“Java”** ci si riferisce sia al linguaggio di programmazione sia all’intero ecosistema tecnologico.
    
- La **tecnologia Java** comprende una **famiglia di prodotti e strumenti** software e hardware, di cui il linguaggio è solo una parte.
    
- All’interno di questa piattaforma esistono numerose **sotto-tecnologie**, come librerie, [[Lezione 6 - API|API]], strumenti per sviluppo web, applicazioni enterprise, dispositivi embedded e molto altro, che rendono Java una soluzione completa per sviluppare applicazioni di vario tipo.
    

In sintesi, quando si parla di Java non si parla soltanto di un linguaggio, ma di un ecosistema tecnologico ampio e versatile, consolidato sia nel mondo del software che in quello dell’hardware.
![[Linguaggio e tecnologie.png]]

### Java Development Kit (JDK)
l **Java Development Kit (JDK)** ==è il kit base necessario per sviluppare applicazioni Java.== 
Può essere scaricato dal sito ufficiale di Oracle e include tutto il necessario per scrivere, compilare ed eseguire programmi Java:

- ==**Il compilatore Java** (`javac`), che trasforma il codice sorgente in bytecode.==
    
- ==**L’interprete Java**, cioè la **[[#La JVM e l’indipendenza dalla piattaforma|JVM]]** specifica per la piattaforma in uso, che esegue il bytecode==.
    
- ==**La libreria standard** di Java, che contiene classi e API pronte all’uso.==
    
- ==**Altri strumenti utili** per lo sviluppo e il debug.==
    

Il JDK è disponibile per diverse piattaforme, come **Linux, Windows e macOS**, e viene rilasciato in diverse versioni principali: 8 (2014), 11 (2018), 13 (2019), 15 (2020) e 19 (2022).

Esistono due principali tipologie di JDK:

- **Java SE (Standard Edition)**: 
	- contiene tutto il necessario per lo sviluppo di applicazioni standard.
    
- **Java EE (Enterprise Edition)**: 
	- include il JDK standard più strumenti e librerie per lo sviluppo di applicazioni distribuite e enterprise.
    

Quando si utilizza un **IDE** come **Eclipse**, il JDK è già integrato e configurato in base alla versione di Java scelta. Questo semplifica notevolmente lo sviluppo, perché l’ambiente fornisce automaticamente il compilatore, la JVM e le librerie necessarie.
#### Java Runtime Environment (JRE)

==Il **Java Runtime Environment (JRE)** rappresenta l’**ambiente di esecuzione** necessario per lanciare programmi Java già compilati.== 
Include:

- ==L’interprete Java (`java` e `javaw`)==
    
- ==Le librerie di runtime (`rt.jar`)==
    
- ==La JVM per la piattaforma in uso==
    

Il JRE non contiene il compilatore, quindi è sufficiente per **eseguire** applicazioni Java, ma non per **svilupparle**.

#### Variabili d’ambiente

Per utilizzare Java da riga di comando è necessario configurare alcune variabili di ambiente:

- **PATH**: indica dove si trovano gli eseguibili del JDK, ad esempio:
```shell
PATH = C:\Programmi\Java\jdk1.8.0_91\bin
```
In questo modo è possibile compilare e lanciare programmi Java da qualsiasi cartella.
    
- **CLASSPATH**: indica dove cercare le classi necessarie al programma, comprese quelle della libreria standard:
```shell
CLASSPATH = .;C:\Programmi\Java\jdk1.8.0_91\lib
```

Questa configurazione consente alla JVM di trovare tutte le classi utilizzate nei programmi senza errori di esecuzione.
### Scrivere `Hello, World!` in Java con Eclipse

Per creare un nuovo progetto Java in **Eclipse**:

1. Cliccare su **`Create Java Project`** nella barra laterale.
    
2. Nella finestra di creazione del progetto:
    
    - Inserire il **nome del progetto**.
        
    - Tenere selezionata la casella **`Use default location`**.
        
    - Scegliere la **versione di Java** da utilizzare.
        
    - Togliere la spunta a **`Create module-info.java file`**.
        
    - Cliccare su **Next** per passare alle impostazioni Java.
        
3. Nella finestra **Java Settings**, accedere alla tab **Libraries** per verificare le librerie associate al progetto.
    
4. Tornando alla vista **Source**, Eclipse crea una cartella `bin` (che contiene i file compilati `.class`) e una cartella `src` per i file sorgente.
    
    - La cartella `bin` non è visibile nella vista del progetto, ma esiste nel file system.
        
    - Le librerie sono condivise tra progetti: se crei più progetti non vengono duplicate.
        
5. Per creare la classe principale:
    
    - Nella cartella `src`, cliccare con il tasto destro → **New → Package**.
        
        - I pacchetti servono a organizzare le classi in spazi logici.
            
    - All’interno del pacchetto, cliccare con il tasto destro → **New → Class**.
        
        - Dare un nome alla classe con **lettera maiuscola** e senza spazi (usare **CamelCase** o underscore).
            
        - Spuntare **`public static void main(String[] args)`**, che crea il metodo **main**, l’**entry point** della JVM.
            
        - Le altre spunte riguardano costruttori o classi astratte e possono essere lasciate deselezionate.
            
        - Cliccare su **Finish**.
6.  Scrivere il codice `Hello, World!`:
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

> [!tip] Shortcut utile: digitare `syso` e premere `Ctrl + Spazio` per generare automaticamente `System.out.println()`.

7. Salvando il file (`Ctrl + S`), Eclipse compila automaticamente il codice in bytecode `.class` nella cartella `bin`.
    
    - La JVM esegue **il bytecode**, non direttamente il file `.java`.
        
    - Se il file non è salvato, compare un asterisco accanto al nome del file.
        
8. L’istruzione `System.out.println()` stampa il testo a console e aggiunge automaticamente un **a capo**, simile al comportamento di `print` in Python.