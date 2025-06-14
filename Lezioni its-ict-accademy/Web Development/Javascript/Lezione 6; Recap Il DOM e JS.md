Rappresenta gli oggetti degli elementi [[HTML]]. 
Fa da ponte tra il codice e l'interfaccia utente e ha una struttura ad albero con relazioni padre-figlio.
![[DOM.png]]

## JS
IN origine [[Lezione 1 I fondamenti Javascript|JS]] è stato creato per essere eseguito nei browser, ma oggi, grazie a tecnologie come Node.JS e Deno è possibile utilizzarlo anche al di fuori di essi.
Tuttavia, ci concetreremo più su React.
`var` ha scope funzionale mentre il `let` e il `const` ha scope a istruzione, cioè vengono eseguiti solo nel blocco in cui sono dichiarati.
JS ha due tipi di dato:
i primitivi 
e oggetti(funzione, classi,etc.).
La differenza è che il primitivo ha un assagnazone per il vlaore cioè nella clella di memoria se il primitivo è 5 allora è diretto a 5 mentre per gli oggetti sono un assegnazione per riferimento, quindi se si ha un array l'assegnazione è il riferimento in memoria dove si trova quell'array 
```js
fro (var i=0; i<4;i++ ){
console.log(i);
}
{
let a = 5
console.log(a)
}
const b=[1,2];
const b2=b; 
b.push(3);
console.log(b,b2);
```

### Import/Export
In questo corso vedremo la sisntassi di importazione ed esportazione in JS per manrtenere il codice manutenibile, specialmente in progetti avanzati.
I moduli servono per fare da importazione ed esportazione da un file ad un altro
Andiamo a creare un file chiamato `utils.js`:
```
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>
<script src ="app.js" type ="module"></script>

</body>

</html>
```

Nel file utils.js  possimao esportare un modulo usando un API key:
```js
export let API_KEY = "chiave segreta"
export const SECRET_KEY = "CHIAVE SEGRETA"
```

Nel file app.js importiamo queste key:
```js
import * as util from './utils.js';
	console.log("API KEY", util.API_KEY)
	console.log ("SECRET KEY", util.SECRET_KEY)
```
La destrutturazione in JS è importare in un file, attraverso l'utilizzo delle parantesi graffe, solo alcuni parametri o variabili.
Un oggetto in JS può essere creato in questo modo attraverso la literal object:
```js
const marco = {
nome: "Marco"
cognome: "Pierleoni"
età: 27
"città": "Roma"
}
marco.nome
marco["nome"]
let a = marco[0]
let congnome = marco[1]
console.log("La mia città", marco["città"])

```
La creazione di oggetti in JS è un array associativo di chiave-valore (come nei [[Collections#I dictionaries|dizionari di python]] o i file [[File in Python#File JSON|JSON]]).

### Gli oggetti in JS 
Abbiamo visto come creare gli oggetti in JS.
Un altro modo altenrativo per creare gli oggetti è creare un oggetto vuoto con la new, cioè si va a creare o meglio a clonare un oggetto reale 
```
const rob = new Object()
```
Cioè l'oggetto object è vuto e con la new si va a clonare quell'oggetto per aggiunere in modo dinamico i parametri in real-time
```
const rob = new Object()
automobile.marca = "Fiat";
automobile.modello = "500";
autoobile.colore = "rosso"
```
Gli oggetti possono essere innestati o annidati tra loro in JS ad esempio:
```
const persona = {
	nome: "Mario";
	cognome: "Rossi";
	età : 22;
	indirizzo:{
		via: "VattelaAPesca"
		nCivico: 33
	}
}
```


```js
function persona(){
	this.nome = "";
	this.cognome = "";
	this.indirizzo = "";
	this.email = "";
}
const p1 = new persona();
p1.nome = "Erica"
p1.cognome = "Stocazzo"
p1.telefono = "3456789211"
console.log("il mio nome:", p1.nome " "  +p1.congnome)
persona.prototype.telefono = "9876"
const p1 = new persona("Erica", "Stocazzo");
const p2 = new persona ("Mario", "Rossi");
p2.telefono = "123444";
console.log(p1.telefono, p2.telefono);
```




