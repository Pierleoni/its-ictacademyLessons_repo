# Javascript
Javascript è un linguaggio di programmazione orientato agli oggetti e agli eventi, comunemente utilizzato nella programmazione web lato client (esteso poi anche al lato server) per la creazione, nei siti web e applicazioni web, di effetti dinamici interattivi tramite funzioni di script invocate da eventi innescati a loro volta in vari modi dall'utente sulla pagina web in uso (mouse, tastiera ecc...).
Originariamente sviluppato da Netscape con il nome di LiveScript, in seguito è stato rinominato "Javascript" ed è stato Standardizzato per la prima volta nel 1997 dalla ECMA con il nome ECMAScript.
Rende dinamico l'HTML.
## ECMAScript
ECMAScript (o ES) è la specifica tecnica di un linguaggio di scripting, standardizzata e mantenuta da ECMA International. Le implementazioni più conosciute di questo linguaggio (spesso definite come dialetti) sono Javascript, JScript e Actionscript che sono entrati largamente in uso, inizialmente, come
linguaggi lato client nello sviluppo web.

### Le tre fasi evolutive di JS
Js fase 1: nato nel 1993 fino al 2009 veniva utilizzato solo nel front-end quindi nel lato client, 
fase 2: dal 2009 è stato creato il Node.js; il fratello del browser, cioè è lo stesso motore del browser che esegue lo stesso codice che esegue un browser ma sul lato server, quindi posso usare js per sviluppare software sia lato client che lato server.
Fase 3: la Microsoft ha acquistato JS è aggiunto Typescript: è un Js dove sono state aggiunte 3 cose
1. Tipizzazione forte:
2. Interfaccia:
3. generics:

Queste fasi evolutive portano ad avere 5 codici diversi, sia lato front-end e back-end, c'è anche una differenza tra questi due, questo perché Js possiamo definirlo un linguaggio furbo perchè sfrutta l'ambiente:
ad esempio il `print()` in python è una funzione di python, mentre Js sfrutta le librerie dell'ambiente (es: `document`).
Quindi se si implementa un codice front-end in un ambiente back-end, questo non funzionerà perché vengono usati oggetti non proprietari dell'ambiente.
Quindi JS sfrutta le librerie esterne non built-in ma date dall'ambiente di implementazione.
Nel 2009 è uscito la versione ESS5 e poco dopo l'ESS6, che hanno cambiato il linguaggio aggiungendo molte funzionalità.
ESS: sta per ECMAScript, Ecma sta per Ecma international che è dedicata per la standardizzazione per i linguaggi di programmazione, questo ente dedicato per dare regole standard per i linguaggi di programmazione web.
Quindi EcmaScript non è la versione di JS ma è le regole che JS segue per rimanere un linguaggio standardizzato.

V8 è l'engine JS che sta dentro Chrome o negli altri Browser che rispettono gli standard dell'ECMA.

### Come scrivere Js Client
Posso scrivere codice JS inline, blocco dentro il file HTML o come file esterno:
per scrivere codice JS inline:
tramite un evento
```html
<div onlick ="test()"></div>
```
in questo caso ho usato l'evento `onclick` come attributo del tag `<div>`, oppure tramite l'evento richiamo una funzione definita nel tag `<script>` definito nell'`head` del file HTML. 
Questo modo è più corretto, in realtà il modo corretto di farlo e scrivere un file JS esterno e tramite la chiamata dell'evento sul tag HTML richiamo la funzione JS.

Prima di scrivere codice Javascript bisogna dire che il lato client Javascript viene utilizzato in "collaborazione" con l’HTML, mentre lato server viene utilizzato
singolarmente senza nessuna "collaborazione". Ed è per questo che lato server lavoreremo con dei semplici file.js.
Mentre lato client, dovendosi interfacciare con l’HTML, possiamo scrivere il codice in 3 modi diversi :
1. **Inline:**
	Consiste nell’inserire direttamente le istruzioni Javascript nel codice di un elemento HTML, assegnandolo ad un attributoche rappresenta un evento. Chiariamo il concetto con un esempio :
```
<button type="button" onclick="window.alert(‘x’)">Vai</button>
```
==Abbiamo assegnato all’attributo `onclick` dell’elemento `button` la stringa `alert('Ciao!’)`. L’attributo `onclick` rappresenta l’evento del clic sul pulsante del mouse, quindi in corrispondenza di questo evento verrà analizzato ed eseguito il codice JavaScript assegnato.== 
==Nel caso specifico verrà visualizzato un box con la scritta `'Ciao'`==.

2. **In blocco:**
	L’approccio inline può risultare immediato perché mette direttamente in relazione il codice da eseguire con un elemento HTML. 
	==Risulta però scomodo quando il codice da eseguire è più complesso o abbiamo necessità di definire variabili e funzioni.== 
	==In questi casi possiamo ricorrere al tag `<script>` per inserire blocchi di codice in una pagina HTML==, come nel seguente esempio:
```JS
<script> alert('Ciao!') </script>
```
Possiamo inserire blocchi di codice (e i relativi tag `<script>`) nella sezione `<head>` o nella sezione `<body>` della pagina HTML.

3. **File esterno:**
	Il terzo approccio, quello più consigliato, consiste nel collegare alla pagina HTML, codice Javascript presente in un file esterno. Questa tecnica permette di agganciare script e librerie in modo non intrusivo, con il vantaggio di una separazione netta tra la struttura del documento e il codice, come accade per i fogli di stile CSS, che separano struttura e presentazione. Per inserire un file Javascript esterno ci serviamo sempre del tag `<script>` in cui si specifica l’attributo `src`, come mostrato dal seguente esempio:
```HTML
<script src="codice.js"></script>
```

l riferimento al file Javascript può essere relativo alla pagina HTML corrente oppure assoluto:
```html
<script src="http://www.server.com/codice.js"></script>
```


> [!caution] Attenzione!
> Da notare che, nel caso in cui utilizzo il blocco (o il file esterno), in qualche modo devo avere un «riferimento» al codice da eseguire, questo riferimento si realizza attraverso le funzioni (che vedremo più avanti).
>Per il momento pensiamo ad una funzione come ad un blocco di codice che viene racchiuso tra parentesi graffe e a questo blocco viene dato un nome (nel nostro caso prova()) e le parentesi tonde stanno ad indicare all’engine V8 che si tratta di una funzione.


## JS lato server 

Il lato server Javascript viene eseguito senza nessuna "collaborazione". Ed è per questo che con il lato server lavoreremo con dei semplici `file.js`
scrivendo il codice in un uncico modo : tramite file esterni.
Come abbiamo detto in precedenza se lato client Javascript "sfrutta" e viene eseguito sul browser, lato server abbiamo bisogno di Node.js.

#### Node.js
Node.js è una runtime di JavaScript Open source multipiattaforma orientato agli eventi per l'esecuzione di codice JavaScript, costruita sul motore JavaScript V8 di Google Chrome.
In origine JavaScript veniva utilizzato principalmente lato client. In questo scenario gli script JavaScript, generalmente incorporati all'interno dell'HTML di una pagina web, vengono interpretati da un motore di esecuzione incorporato
direttamente all'interno di un Browser. 
Node.js consente invece di utilizzare JavaScript anche per scrivere codice da
eseguire lato server, ad esempio per la produzione del contenuto delle pagine web dinamiche prima che la pagina venga inviata al Browser dell'utente.


> [!info] Come nasce il Node.js
> Nel 2009 l’idea «rivoluzionaria» del progettista di Node.js Ryan Dahl è stata quella di prendere il motore V8 ed inserirlo all’interno di un nuovo ambiente in cui eseguire codice JavaScript. Questo ambiente prende il nome di Node.js che non opera lato client ma opera lato server.
> ![[JS Lato Server.png]]

Per installare localmente Node.js bisogna andare
sul sito ufficiale [www.nodejs.org](https://nodejs.org/en) e scaricare il pacchetto per il nostro sistema operativo.
Inoltre Node.Js va utilizzato da riga di commando. Per verificare che l'installazione è andata a buon fine si deve aprire il terminale del computer e digitare il comando `node -v`.

