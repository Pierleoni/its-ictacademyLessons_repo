React utilizza un modo di scrivere del codice chiamato JSX, permette di scrivere il codice come l'HTML, ma in realtà produce file JS .
Ci sono siti che convertono l html in JS [come ad esempio questo.](https://transform.tools/html-to-jsx) 
Il concetto di stato: fa riferimento ai dati archiaviti da visulaizzazione diverse. Lo stato si basa in genere sull'utente e sulle operazioni eseguite dall'utente. Ad esempio, l'accesso 


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
