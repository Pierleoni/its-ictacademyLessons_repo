# Introduzione
Nella scorsa lezione abbiamo dato nuovamente un occhiata a cos'è il [[Lezione 6; DOM e ripasso JS#Come funziona il DOM|DOM]] e abbiamo introdotto nuove caratteristiche di Javascript come i [[Lezione 6; DOM e ripasso JS#Rest parameters|rest parameters]] o gli [[Lezione 6; DOM e ripasso JS#Spread operator|spread operators]].
Oggi vedremo cos'è e cosa fa React.
## Introduzione a React JS
**React** è una **libreria JavaScript** sviluppata da **Facebook** nel 2013, oggi **open-source** e supportata da una vasta community di sviluppatori.

>  ==È progettata per **creare interfacce utente (UI)** moderne e reattive, cioè capaci di aggiornarsi dinamicamente **senza ricaricare l’intera pagina**.==

### Perché React è utile
- **Aggiornamenti dinamici:**  
    ==Le modifiche ai dati vengono riflesse automaticamente nella UI, senza bisogno di refresh manuali.==
    
- **Sviluppo in tempo reale:**  
    Grazie a strumenti come **_Hot Reload_**: ==puoi vedere subito le modifiche che fai nel codice.==
    
- **Modularità:**  
    ==React si basa su **componenti**, ovvero blocchi riutilizzabili che semplificano lo sviluppo di interfacce complesse.==
    
- **Flessibilità:**  
    ==Può essere integrato facilmente con altre librerie o framework.== 
    Ad esempio, puoi usarlo con Redux per la gestione dello stato, o con librerie di routing e backend API.
### React è la "V" dell'architettura MVC
M.V.C è un modello architetturale molto usato nello sviluppo software.
Sta per **Model View Controller,** dove nello specifico:
- M = Model → ==gestisce i dati e la logica dell'applicazione==
- V = View → ==Mostra i dati all'utente (interfaccia grafica).==
- C = Controller → ==gestisce le azioni dell'utente e aggiorna View e Model==

In tutto questo React si inserisce solo nella parte "View", cioè:
- ==**Visualizza i dati** all'utente== (ad esempio una lista di prodotti, un form, ecc.)
    
- ==**Gestisce l’interazione dell’utente**== (es. clic, scrittura in input, ecc.).
In parole semplici, React si occupa solo di **come appaiono le cose** e **come reagiscono agli input**.  
Non gestisce **cosa fare con i dati**, né **come farli arrivare o salvarli**.

Difatti React **non si occupa direttamente di:**
1. **Model** (la logica di business e i dati):
    
    - Ad esempio: Come si salva un utente nel database? Quali sono le regole di validazione?
        
    - Queste cose vengono gestite dal backend o da altre parti del codice.
        
2. **Controller** (flusso e controllo dell’app):
    
    - Ad esempio: Quando clicco su un bottone, cosa succede? Dove vado?
        
    - React può intercettare l’evento (es. `onClick`), ma non gestisce _di per sé_ il controllo di tutto il flusso. Per questo puoi usare router o librerie specifiche.
        
3. **Stato globale o chiamate a server (API)**:
    
    - Se vuoi tenere traccia dello **stato complessivo** dell’app (es. utente loggato, carrello, ecc.), React non ha una gestione avanzata incorporata.
        
    - Per questo usi librerie **aggiuntive**, ad esempio:
        
        - **Redux**, **Zustand** → per gestire lo **stato globale**
            
        - **Axios**, **Fetch API** → per fare chiamate al backend (es. ottenere dati dal server)


> [!example] **In sintesi**
> React è: 
> - Una **libreria UI** JavaScript (non un framework)
 >   
>- Focalizzata sulla **parte visuale** e sugli **eventi dell’utente**
 >   
>- **Leggera e flessibile**, non impone regole rigide
 >   
>- Ottima per costruire **SPA** (Single Page Applications)

### Cos'è React 
React è una delle prime librerie JavaScript nate con un obiettivo preciso: ==diventare la soluzione ideale per sviluppatori front-end e app mobile basate su HTML5, una sorta di "panacea" per chi vuole costruire interfacce utente dinamiche e complesse mantenendo tutto semplice e intuitivo.==  
Creata da Facebook, React è la colonna portante del social network più popolare al mondo e alla base dell’interfaccia web di Instagram.

La creazione di applicazioni web, indipendentemente dal framework scelto, coinvolge sempre i tre linguaggi fondamentali della piattaforma:

- **[[HTML]]** per la struttura
    
- **[[CSS]]** per la stilizzazione
    
- **[[Lezione 1 I fondamenti Javascript|JavaScript]]** per la logica applicativa
    

Le applicazioni React sono spesso **Single Page Applications (SPA)**:
==si basano su una sola pagina HTML che funge da **contenitore dinamico** per l’interfaccia utente, costruita e aggiornata tramite JavaScript.==

La forza di React rispetto ad altre librerie è la possibilità di usare un approccio **dichiarativo** molto simile all’HTML per definire i componenti che rappresentano parti significative e logiche dell’interfaccia utente, come ad esempio un commento a un articolo o la lista degli stessi commenti.
## Perché usare **ReactJS**

ReactJS è una **libreria open-source**, il che significa che chiunque può contribuire al suo sviluppo, segnalando problemi o inviando [pull request](https://github.com/facebook/react) tramite GitHub.  
Proprio come accade per questi documenti!

#### Vantaggi principali di React

- **Approccio dichiarativo:**  
    React adotta uno stile **dichiarativo**: 
    ==descrivi ciò che desideri venga mostrato nell’interfaccia, e React si occupa automaticamente di aggiornare il DOM per riflettere quei cambiamenti.== 
    Questo semplifica lo sviluppo e rende il codice più chiaro e prevedibile.
    
- **Architettura a componenti:**  
    ==Le applicazioni in React si costruiscono tramite **componenti modulari e riutilizzabili**==.  
    ==Ogni componente è un blocco autonomo che gestisce il proprio **stato** e può essere facilmente collegato ad altri per creare interfacce complesse. In questo modo, è possibile passare i dati all’interno dell’app senza manipolare direttamente il DOM.==
    
- **Filosofia “Learn once, write anywhere”:**  
    Il motto ufficiale di React è **“Impara una volta, scrivi ovunque”**.  
    ==L’obiettivo è riutilizzare il codice il più possibile, indipendentemente dalla piattaforma== (web, mobile con [React Native](https://reactnative.dev), ecc.).  
    React non fa supposizioni rigide sull’ambiente in cui viene usato, permettendo la massima flessibilità nell’integrazione con altre tecnologie.
    



### Tecnologie chiave integrate in React

- **JSX (JavaScript XML):**  
    ==JSX è una **estensione di sintassi** che consente di scrivere codice simile all’HTML all’interno di file JavaScript.==  
    Anche se visivamente ricorda l’HTML, ==viene **trasformato in JavaScript puro** durante la compilazione==. 
    JSX rende più leggibile e naturale la definizione dei componenti UI.
    
- **Virtual DOM:**  
    Il **DOM (Document Object Model):** 
    ==è la struttura che rappresenta l’interfaccia utente nel browser.==  
    In una normale applicazione, ogni cambiamento allo stato comporta aggiornamenti diretti al DOM, che possono rallentare le prestazioni.  
    React utilizza invece un **DOM virtuale**, una copia leggera in memoria del DOM reale.  
    ==Quando lo [[Lezione 7; React#Il concetto di stato in React|stato]] cambia, React aggiorna prima il Virtual DOM, confronta le differenze con il DOM reale e applica **solo le modifiche necessarie**.== Questo approccio migliora notevolmente la performance.
    
- **Rendering delle visualizzazioni:**  
    Le **view** sono gli elementi che l’utente vede nel browser.  
    In React, la visualizzazione è legata al concetto di **rendering di componenti**: 
    ==definisci quali elementi mostrare, e React si occupa di renderizzarli in base allo [[Lezione 7; React#Il concetto di stato in React|stato]] corrente.==  
    Tutto è gestito in modo reattivo, così che la UI si aggiorna automaticamente ogni volta che i dati cambiano.


> [!info] Ci sono siti che convertono l html in JS [come ad esempio questo.](https://transform.tools/html-to-jsx) 


#### Il concetto di stato in React
==Lo **stato** (_state_) rappresenta i **dati dinamici** che una visualizzazione utilizza per adattarsi all’interazione dell’utente.==  
==In genere, lo stato dipende da **chi è l’utente** e da **quali operazioni compie** durante l’uso dell’app.==

Ad esempio, quando un utente effettua l’accesso a un sito web, la pagina del profilo (cioè la **visualizzazione**) può mostrare il suo **nome, email o immagine del profilo**: questi sono **dati di stato**, e cambiano da utente a utente.  
==La struttura della visualizzazione resta la stessa, ma **il contenuto cambia in base allo stato**==.


> [!example] Analogia con Facebook
> Nel caso dell'app di Facebook (o qualunque app simile):
> 
>- ==La visualizzazione (ossia la struttura della pagina del profilo: layout, sezioni, pulsanti, ecc.) è sempre la stessa per tutti gli utenti.==
 >   
>- ==Ma lo **stato** (cioè i dati personali come **nome**, **email**, **immagine del profilo**, **post pubblicati**, ecc.) **cambia da utente a utente**, in base a **chi ha effettuato l’accesso**.==
  >  
>
>> ==Quindi React usa la **stessa struttura di componente** per tutti i profili, ma li **riempie con dati diversi** a seconda dello stato dell'app (cioè dell’utente loggato in quel momento)==.

In sintesi, il concetto di stato si può riassumere così:
- **Stessa visualizzazione** → struttura comune per tutti
    
- **Stato diverso** → contenuti personalizzati per ogni utente

> [!info]  Benché dichiarativa, la rappresentazione del componente in realtà si traduce in chiamate all'API di React che intervengono, nel modo più veloce e performante possibile, sul DOM della pagina per creare gli elementi necessari.



> [!remember]- **Differenze tra React, AngularJS e JQuery**
>1. React vs AngularJS
>
>- **AngularJS è più completo, ma anche più complesso:**  
  >  AngularJS offre una **soluzione “full stack”**, gestendo tutto (routing, stato, logica, interfaccia...).  
 >   Ma per questo motivo, è **più difficile da imparare e più rigido**.
 >   
>- **React è più leggero e flessibile:**  
 >   React si concentra solo sulla **UI** (View) e lascia la libertà allo sviluppatore di scegliere **altre librerie** (come Redux, Axios o persino jQuery) per coprire gli altri aspetti dell'app.
>    
>
> Diverso approccio alla struttura del codice
>
>- Alcuni sviluppatori **AngularJS** criticano React perché:
 >   
 > 	“Mescola logica e presentazione nello stesso file/componente.”
>    
>- React invece **non separa rigidamente la logica dal markup**, ma adotta un’altra filosofia chiamata:
  >  
 >    “Separation of Concerns” (Separazione delle responsabilità **funzionali**)
   > 
 >   - Con React, l'obiettivo è **raggruppare tutto ciò che serve a un componente (logica, stato e markup)** in un unico modulo riutilizzabile.
  >      
>    - Questo **semplifica la manutenzione** e **aumenta la riusabilità**, anche se non c'è una separazione netta tra “view” e “logica”.
>        
>
>  In pratica: React **organizza il codice per “componente”**, non per tipo di responsabilità (come fa Angular).
>  2. React vs jQuery
>
>Rispetto a **jQuery**, React offre un approccio **più moderno e automatizzato** alla gestione dell’interfaccia utente:
>
>- **Niente ID o classi obbligatorie:**  
 >   In React **non serve assegnare manualmente ID o classi** agli elementi per manipolarli.
  >  
>- **Nessuna manipolazione diretta del DOM:**  
 >   Mentre con jQuery **lo sviluppatore interagisce direttamente con il DOM** (es. `.html()`, `.hide()`, ecc.), con React **questo avviene in modo automatico**.
 >   
>- **React gestisce tutto internamente:**  
  >  React **aggiorna il DOM** sulla base:
 >   
   > 1. della **struttura dichiarata** nei componenti,
  >      
  >  2. dello **stato interno** del componente,
  >      
 >   3. e delle **props** (cioè i dati passati ai componenti).
   >     
>
>  **In sintesi:**  
> Con React tu **descrivi l’interfaccia** in modo dichiarativo (tramite componenti e dati), e sarà la libreria stessa a **ottimizzare e gestire le modifiche al DOM** per ottenere le migliori performance possibili.


I file esterni di JS non vanno messi nell'head ma a chiusura del body, questo perché nel caricamento della pagina i file esterni JS pesano di più e quindi vanno messi a chiusura del body, mentre i file CSS vanno messi nell'head.

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>
<h1></h1>
....
<script src = "index.js"></script>

</body>

</html>
```

Il `querySelector` prende un solo elemento che ha quel selettore mentre il `querySelectorAll` prende tutti gli elementi che hanno quel selettore:
il primo viene usato con l'attributo `id` mentre il secondo viene usato per l'attributo class o con gli altri attributi o i tag hmtl.
Se scriviamo .querySelector("div >p") prende tutti i figli (i p annidati dentro i div) diretti di un div
Se in un div si ha uno span e dentro un tag p questo querySelector non funzionerà.
.createElement(): prende 3 parametri 
	1. il tag
	2. un oggetto con attributi  
	3. il contenuto  
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>
<h1></h1>
<script>
	const h1 = React.createElement("h1", {
	style:{
		color: "red"
		border: "1px #000 solid",
		padding: "5px",
		}
	}, "Primo tag h1 con react)
	root.Render(h1)
</script>
<script src = "index.js"></script> <!-- Esempio di file esterno JS importato -->  

</body>

</html>
```

Esempio completo:

```html
<!DOCTYPE html> 
<html lang="en"> 
<head> 
	<meta charset="UTF-8"> 

	<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<title>Document</title> 
	<style>
		.big{
			font: "5rem"
		}

</head> 
<body> 
	<div id="root"></div> 
	<script src="[https://unpkg.com/react@18/umd/react.development.js](https://unpkg.com/react@18/umd/react.development.js)">
	</script> 
	<script src="[https://unpkg.com/react-dom@18/umd/react-dom.development.js](https://unpkg.com/react-dom@18/umd/react-dom.development.js)">
	</script> 
	<script> 
		const rootElement=document.querySelector("#root"); 
		const root =ReactDOM.createRoot(rootElement); 
		console.log(rootElement); 
	const e= React.createElement;	
		const h1= e(
		"h1",{ 
		key:"h1"
			style:{ 
				color:"red", 
				border:"1px #000 solid", 
				padding:"5px" 
			},
			className: "big", 
			onClick: (e)=>{console.log(e),
			onClick: function(el){console.log(el.target)}
	} "Primo tag h1 con react")},
	const main = createElement("main", {}, h1);		
			
	 root.render(h1);
		 const ul = e(key: "ul", {}, [
		 e("li", {}, "PHP"), 
		 e("li", {}, "JS"), 
		 e("li", {}, "Python"), 
		 ]);
	 const main = e("main",{}, [h1,ul])
	 root.render(main)
	</script> 
</body> 
</html>
```

usare l'unità di misura rem riprende l'unita di misura impostato come default del browser, se il font del browser viene aumentato dall'utente l'unità rem si adatta meglio al font diversamente dei pixel.
Di default il browser è impostato a 16 quindi se vengono assegnati 5rem,il calcolo sarà $5*16$ (stessa cosa se il font del browser viene aumentato di 18 e si assegna sempre 5rem, allora il calcolo sarà $5*18$).

Nel context React la prop key è utilizzata per aiutare React a identificare quali elementi sono cambiati, o aggiunti, o rimossi tra diversi render. Le keys dovrebbero essere assegnate agli elementi all'intenro di un array agli elementi una identità.

Ogni volta che si vuole creare un applicazione con Node.js si deve eseguire una serie di comandi sul terminale o di vs code o del prompt di comandi:
```shell
Set-ExecutionPolicy -ExecueSigned -Scope CurrentUser
```

e 
```shell
npx create-react-app nomeDellApplicazione
```

questo comando lo si deve eseguire ogni volta che si vuole creare una nuova applicazione in un nuova working directory.

se si scrive 
```shell
npm install
```
se si ha necessita di esportare la cartellla public e metterla in un altra working directory si può cancellare il resto o meglio solo la directory `node_modules` e tramite questo comando mi re installa tutti i pacchetti di Node.js
La directory `src` 

Come si ad lanciare l'applicazione 
```shell
npm start
```
in questo modo si crea il server che lancia l'applicazione react.

Sul file `App.js` scriviamo 
```jsx
function app(){

return (
	<div className="App">
	<h1>Prima App React</h1>
	</div>
);
}

export default app;
```

In questo modo:
1. Eliminimao l'uso dell'estensione Live Server di Vs Code
2. Evitiamo di dover scrivere un file `.html` poiché viene gia scritto da react stesso quando lanciamo il comando `npx create-react-app nomeDellApplicazione` e tutta l'applicazione react gira dentro a un `<div id = "root">`

```jsx
function app(){
let nome = "Marco"
return (
	<div className="App">
	<h1>Prima App React {nome}</h1>
	</div>
);
}

export default app;
```

Dentro JSX non si possono usare i conditional statements nei i loop statements, al massimo si possono farlo fuori:
```jsx
function app(){
let nome = "Marco"
if (true){
	//istruzioni da eseguire
}

for (){
	//istruzioni da eseguire
}
return (
	<div className="App">
	<h1>Prima App React {nome}</h1>
	</div>
);
}

export default app;
```

Tutt'al più si possono usare dentro JSX gli operatori ternari per scirvere statements condizionali:
```

```

un altra cosa che si può fare è scrivere funzioni:
```jsx

function getDate(date){
return  date.toLocaleDateString()+" "+date.toLocaleTimeString();
}
function app(){
let nome = "Marco"
return (
	<div className="App">
	<h1>Prima App React {nome}</h1>
	<h2>
	{
	new Date().toLocalDateString()+" "+new Date().toLocaleTimeString
	}
	</h2>;
	<h3>{getDate(new Date())}</h3>;
	
	<h3>{getDate(new Date())}</h3>;
	
	<h3>{getDate(new Date())}</h3>;
	</div>
);
}

export default app;
```


Il componente di React è un unità indipendete di codice che rappresenta una parte di UI

COme si fa ad usare BootsTrap in questa applicazione?
1. Passare il link nel html 
2. Scrvere:
```shell
nmp install bootstrap
```

> [!tip]  `i` è l'abberviazione di `install`
> 

premendo avvio scarica il pacchetto di Bootstrap

Una volta installato il pachetto sul file index.js 
si deve importare bootstrap:
```jsx
import "bootstrap/dist/css/bootstrap.css"
```


Perchè in App.js è meglio usare i fragment anziche i div?
Perché il div viene reinderizzato e si prende l'abbitudine di usare il div per raccgiudere i componenti nei div e questo ci sporca l'html e rovina l'ottimizzazione e fa leggere male la pagina agli spider.
Quindi è meglio usare i fragment
```jsx
<>
il codice che deve essere eseguito
</>
```

si possono scrivere anche cosi
```jsx
<React.Fragment>
...
</React.Fragment>
```

Creiamo un nuovo file `Clock.js`:
```
const Clock = () =>{
	 const date new Date()
	return(
	<div>{date.toLocalDateString()+" "+date.toLocalTimeString()}
	)
}
export defualt Clock
```

Su App.js:
```jsx

function getDate(date){
return  date.toLocaleDateString()+" "+date.toLocaleTimeString();
}
function app(){
let nome = "Marco"
return (
	<div className="App">
	<h1>Prima App React {nome}</h1>
	<h2>
	{
	new Date().toLocalDateString()+" "+new Date().toLocaleTimeString()
	}
	</h2>;
	<h3>{getDate(new Date())}</h3>;
	
	<h3>{getDate(new Date())}</h3>;
	
	<h3>{getDate(new Date())}</h3>;
	<h3><Clock></Clock></h3>
	<h3><></Clock></h3>
	
	<h3><Clock timezone = "2" country = "ITALY"></Clock></h3>
	<h3><Clock timezone = "4" country = "USA"></Clock></h3>
	<h3><Clock timezone = "8" country = "JAPAN"></Clock></h3>
	</div>
	<footer></footer>
);
}

export default app;
```


Ora che aggiunto i due attributi o props a clock adesso posso scrivere:
```jsx
const Clock = (timezone,country) =>{
	 console.log(props.timezone.props.country)
	 const date new Date()
	return(
	<div>{date.toLocalDateString()+" "+date.toLocalTimeString()}
	<h3> in {country} sone le {date.toLocaleDateString()}
	)
}
export defualt Clock
```

Di conseguenza posso conacellare i tah h3 che wrappano i clock
Ora sempre su clock:
```jsx
const Clock = (timezone,country) =>{ const t = Date.now()+3600*timezone*1000
const date = new Date(t) return(
<div>
  {date.toLocalDateString()+" "+date.toLocalTimeString()}
  <h3>
    in {country} sone le {date.toLocaleDateString()} ) } export defualt Clock
  </h3>
</div>

```
