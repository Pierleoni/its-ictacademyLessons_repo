
Quindi l'HTML è un linguaggio per il posizione del contenuto, mentre il CSS è un lignaggio grafico nato per dare all'HTML

Il DOM è una ibreria, anzi è un oggetto cioè è un contenitore dove posso metterci gli attributi(valori/variabili) e i metodi (le azioni). 
Il DOM è un oggetto ed è l'unico in grado di modificare l'HTML in modo dinamico:
cioè quando clicco su un bottone lo sofnodo diventa verde, etc.
All'intenro del dom quindi ci sono attributi e metodi, per usare il DOM devo utilizzare JS (simile a python).
Come utilizzare il DOM:
2 modi:
Da solo: se uso il dom direttamente non c'è logica applicativa(if, for,while,..)
trmaie a JS: c'è logica applicativa
QUeste due modilatià somo legati ad eventi (cioè quando clicco su un pulsante succede x,...).


### Come scrivere con il DOM(Document Object Model)
Il dom è quello oggetto che visualizza la pagina HTML in modo gerarchico, il dom vede la nostra pagina a cartelle; ovvero all'intenro della cartella HTML ci sono tutti i vatri tag che contengono a loro volta altre cartelle(tag).
Con il dom posso fare 5 cose:
1. Recupero l'elemento
2. Decidere cosa applicare all'elemento(fa prendere 3 strade diverse):
	   2.1) modificare un attributo
	   2.2) gestire un evento
	   2.3) modificare il CSS
	   2.4)creare i tag
	   
Esempio con la modifica:
```html
<h2><div onclick="document.body.style.background='red'">cambia colore</div></h2>
```
Gli eventi del dom sonon tanti, se si è curiosi di conoscerli basta andare [sulla pagina di w3schools](https://www.w3schools.com/jsref/dom_obj_event.asp)
Gli eventi non sono altro che attibuti html.
Tornando all'esempio ho creato un bottone dove se clicco sopra lo sfondo della pagina diventa rossa.
Da solo il DOM non c'è applicativa, cioè come in questo esempio, se clicco sul bottone lo sfondo diventa rosso, mentre se si usa un file JS esterno posso applicare logica di programmazione, cioè psso usare gli statemets e i loop, etc.
JS funziona come CSS, può essere scritto sia inline che come documento esterno, ma come CSS inline non si usa mai. QUello che si usa tanto è il blocco o esterno, per usare il tag script che può essere messo ovunque(nache se adesso lo metteremo nel Head, questo perché JS viene eseguito come l'HTML dall'alto verso il basso, riga per riga).
```html
<!DOCTYPE html>

<html lang="en">

<head>

	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<title>L</title>
	<script>
		function test(){
			document.body.style.background ="red"
		}
	</script>

</head>
```

`<script>function test(){document.body.style.background ="red"``}</script>`
questo è una dimostrazione in block dell'uso di DOM JS.
Con il DOM io posso recuperare ogni singolo elemento, ma se io voglio recuperare un elemento:
`getElementById()`, per recuperare il singolo elemento devo usare l'id che è scritto come attributo del tag(gli id sono univoci). Ci sono anche altri modi 
`getElementsByTagName`, etc tuttavia questi altri metodi non recuperano il singolo elemento ma gli elementi con lo stesso nome, classe, etc

```html
<!DOCTYPE html>

<html lang="en">

<head>

	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<title>L</title>
	<script>
		function test(){
			document.body.style.background ="red"
			len x =document.getElementById("mio titolo")
			x.style.color = "blue"
				x.setAttribute("onclick","document.body.style.background")
		}
		
	</script>

</head>
<body>
	<h1 id ="mio titolo">
</body></html>
```

Per creare un elemento:
```html
<!DOCTYPE html>

<html lang="en">

<head>

	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<title>L</title>
	<script>
		function test(){
			document.body.style.background ="red";
			len x =document.getElementById("mio titolo");
			x.style.color = "blue";
				x.setAttribute("onclick","document.body.style.background")
			let y = document.createElement("h1");
			y.innerHTML = "Ciao";
			y.style.color = "yellow";
			y.style.background.color = "black";
			x.append(y);
			
		}
		
	</script>

</head>
<body>
	<h1 id ="mio titolo">
</body></html>
```