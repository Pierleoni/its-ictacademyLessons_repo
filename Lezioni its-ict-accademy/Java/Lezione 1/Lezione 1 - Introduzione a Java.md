
# Introduzione

Java nasce nel 1991 con il nome di OAK, adesso la sua gloria è scesa a causa di Python. 


All'inizio il Green Team, guidato da Goislin, creo un estensione del compilattore C++. 
linguaggio OOP,
Indipendente dalla piattaforma, 
robusto e sicuro. 

L'OOP è un paradigma: un modello, dice quali sono i principi che devi seguire. 
Quindi l'OOP 

Una delle caratteristiche importanti all'epoca: 
indepdenza della piattaforma: 
si intende che il codce JAVA si scrive una volta sola è poi deve poter girare su qyakiasi macchina o piattaforma. 
NEgli anni 80 i software venivano fatti in maniera artigianle: il cleinte aveva una macchina /server specifico e il software veniva costruito per quella piattaforma specifica. 

Negli anni 90 con il boom con intenret una softawre house poteva vendere il proprio software a chi voleva: il problema era che non si spaeva che macchina avesse il client, quindi è sorta l'esigenza di avere un linguaggio che potesse girare su qualsiasi macchina.
Qui Java ovviava a questo problema, al massimo era il client a preocupparsi che doveva interpretarlo. 

### Linguagigo macchina
Il linguaggio macchina (codice binario) è l'unico linguaggio comprensibile alla macchina, i linguaggi di programmazione consente di impartire istruzioni alla macchina con una visione più vicina all'essere umano. 
Questi vengono chiamati linguaggi di alto livello: 
- servono per scrivere istruzioni ad alto livello, che devono essere poi tradotte in linguaggio macchina 
Chi traduce in linguaggio macchina? Da un software che traduce i linguaggi 

linguaggi compilati: 
	- C'è un solo software che è il compilatore: 
		-rileva eventuali errori di sintassi e di semantica 
		- Traduce il codce sorgente in codice macchina 
Esiste un compilatore per ogni piattaforma: 
	- un file exe eseguibile solo sulla piattaforma per la quale è stato compilato.
Linguaggi intepretati: 
un linguaggio interpreato usa il compilatore per: 
- rilevare errori(sintassi e semantica)
- traduce il codice sorgente in bytecode, linguagigo macchina virtuale da intepretare successivamente 
- questi tipi di linguaggi preve l'uso di un seocndo progemma: l'inteprete 
Il bytecode viene eseguito istruzione per istruzioen e non viene mai creato l'eseguibile 
Le eccezioni sono un modo in cui l'inteprete mentre sta interprendo ha incontroato una anomalia. 

La JVM 
è la specifica di un software che interpreta il bytecode java
Le vaire implementazioni consentono la traduzione del codice java in codice macchina specifico. 
QUando si scarica eclipse questi chiede il SO utilizzato questo perchè eclipse ha JAVA già installato dentro quindi in base al SO si avra un particolare inteprete. 


> [!NOTE] Title
> I linguaggi intepretati esistevano anche prima di java, ma il meccanismo dell'intepretazioen del codice divenne 

Robusto (affidabile): 
Rilevamento errori e typechecking a tempo di compilazione e di esecuzione, prima si deve passare il compilatore (fa almeno lì80% ) e la jvm fa ulteriori controlli ma prima di arrivare ad essa si deve passare i controlli del compilatore. 


Mascheramento dei puntatori all'utente : il puntatore è l'indirizzo di memoria di una certa variabile. 
Ma una cosa è l'indirizzo e una cosa è il contentuto: dei linguaggi di basso livello permettono di avere accesso all'indirizzo ma non il contentuto, mentre java e python permettono questa cosa ma usano riferimento all'indirizzo in memoria.
Quindi si usano le refenrce, c'è un mascheramento dei puntatori perché sono più vicini 
La refernce è il telecomando dell'oggetto: l'indirizzo è troppo a basso livello, invece la refernce pilota una azione sull'oggetto 
```python
p = Persona()
```

`p` pilota l'oggetto `Persona`

Gestione delle eccezzioni da parte dell'utente 

Gestione della memoria (allocazione e GC ): quanddo si alloca un oggetto in memroai il programmatore non decide dove allocare l'oggetto in memoria, quindi gli oggetti non più refernziati vengono marcati come sovrascribili, quondi la zona di memoria viene sorascritta. 


Multithreading: permette che un linguaggio si può splittare in più processi, ad esempio quando ti collegghi ad amzon.com ti collegghi alla pagina pensando di essere li da solo ma in realta sei collegato con chissa quanti client contemporaneamente. 


### Java Development Kit (JDK)
Dal sito della Oracle è possibile scaricare il Kit base per lavorare in Java che comprende:
- Il compilatore
- L’interprete java (JVM per la piattaforma prescelta)
- La libreria standard
- altri tools utili
- Il kit si chiama JDK – java development kit
- dipende dalla piattaforma  Linux, Windows, Mac OS
- ha una versione
	-  8 (2014), 11 (2018), 13 (2019), 15 (2020), 19 (2022)
- Esistono 2 kit principali
	- Java SE → JDK con Standard Edition
	- Java EE → JDK + supporto applicazioni distribuite
Noi queste cose le abbiamo dentro eclipse perche l'IDE ha un JDK già installato nella versione di Java e a seconda dell'ambiente il JDK supporta fino a una certa realese

JRE : l'ambiente di runtime, gli eseguibili sono → java, javaw, librarie, rt.jar


### Scrivere `Hello, World!`
Su ecplise per creare un progetto cliccare sulla sinistra alla voce `create Java Project`.
Si apre la finestra di creazione del progetto: 
	- Inserire il nome del progetto 
	- Tenere spuntato la casella "`Use default location`"
	- Decidere la versione di Java
	- Togliere la spunta al `create model info java file`
	- Cliccare su next
TI porta sulla finestra Java settigns
andare nella tab Libraries 
Tornando a source eclipse dice che crea un .bin che moralmente è un eseguibile ma non è un vero un proprio esegubile 
Dentro la cartella del progetto c'è una directory filgia chiamata src.
Clicco su finish e dentro la cartella del progetto trovo la src e la libreria che è linkata: cioè se creo 5 progetti non creo 5 volta la libreria 
Dentro la `src` creo il file `helloWorld` → tasto destro→`New` → `Package` 
I pachhetti sono esinzialmente dei pacchetti
COsi facendo ecplise 
Dal package→tasto destro → class

> [!NOTE] Lettera maiuscola sul nome del file
> No spazi nel nome quindi o underscore o camel case 

Spunto la prima casella "`public static void main (String[] args)`"
La seconda e terza spunta hanno a che fare con costruttori delle classi, classi astratte, etc. 
Infine clicco su `finish` 
Notare la directory bin non si vede nella vista del progetto non si vede ma nel file system è presente. 
Il nome del pacchetto comparen le sorgente: il pacchetto non è una semplice direcotry ma il file Java sa di appartenere a quel pacchetto 

La funzione main è l'entry point della JVM quindi se voglio runnare il file o far partire il file serve questo signature. 

syso + CTRL + spazio: shortcut il print statement


Se il file non è salvato compare un asterisco sulla destra accanto del nome del file

Se slavi e non hai errori lui compila il file .class nella bin
Noi lanciamo la virtual machine di java non il file stesso 

Il println() stampa e va accapo come il print in python