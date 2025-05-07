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
