# Introduzione

Le funzioni in JS sono un blocco di codice nel quale sono contenute delle istruzioni. La sintassi è molto semplice: 
```JS
function nomeFunzione(){
… istruzioni …
}
```

La parola `function` è riservata solo per dichiarare una funzione.
Il browser carica lo script JS  in maniera sequenziale e le funzioni le pre-carica e le esegue solo se trova una chiamata di quella funzione.
Le parenesi tonde è dove si trovano i paramtri di quella funzione, mentre le parentesi graffe racchiudono le istruzioni delle funzioni.
## Le funzioni 
Una funzione può ricevere dei parametri e ritorna un valore (se non ritorna nulla l'output sarà `undefined`). 
Come per python, le funzioni in JS ci aiutano a non ripetere blocchi di codice ma organizzarli in modo funzionale.
Quindi servono per automatizzare e riusare comportamenti del programma che in caso contrario bisognerebbe ripetere il codice (Dry concept).

### Esempio 
Per fare un esempio e andiamo a scrivere una funzione in blocco che fa la somma di due numeri:
```JS
<script>
	function somma(num1,num2){
		document.write(num1 + num2);
	}
</script>
```
Questa funzione non torna nulla perché è scritta direttamente nella pagina e se esguo la pagina non si trova nulla perché nessuno sta chiamando la funzione.
Questa funzione non torna la somma tra `num1` e `num2` ma scrive la somma direttamente nella pagina o documento HTML.

Per richiamare una funzione, come in python, basta riscrivere il suo nome:
```
<script>
	function somma(num1,num2){
		document.write(num1 + num2);
	}
somma(5,6)

</script>
```

Per ritonranre un risultato bisogna usare la key-word `return`:
```js
function testProva(){
	console.log('corso JS')
	return 'benvenuto'
}

var risultato = testProva() //corso JS
console.log(risultato) //benvenuto 
```
Questa funzione, se ignoiamo il `console.log()`, torna una stringa.
Per fare un altro esempio:
```JS
<script>
function saluto(nome1,nome2,nome3){
	document.write(‘’Benvenuto’’ + nome1);
	document.write(‘’Benvenuto’’ + nome2);
	document.write(‘’Benvenuto’’ + nome3);
}
saluto(‘’Mario’’,’’Luca’’,’’Giovanna’’); // cosa succede ?
saluto(‘’Mario’’,’’Luca’’); // cosa succede ?
</script>
```
In questp caso JS ha un approccio accomodante, ovverro in qualunque caso JS fa uscire la pagina: in questo caso la funzione ha 3 parametri e nelle chiamata ne stiamo definendo tre arogmenti quindi qui verra stampato gli  

### Array arguments
L’oggetto arguments è una variabile locale disponibile in tutte le funzioni. È possibile fare riferimento agli argomenti di una funzione all’interno della funzione utilizzando l’oggetto arguments.
Questo oggetto contiene una voce per ogni argomento passato a una funzione, che ci aiuterà a conoscere il numero di questi argomenti e ad
accedervi.
Come abbiamo detto, l’oggetto arguments è un oggetto (array), ed ha una proprietà `length()`. Quindi possiamo accedere ai valori individuali
usando la notazione di indicizzazione dell’array arguments \[i].
```JS
function myFunction (a,b,c){
	console.log(arguments[0])
	console.log(arguments[1])
	console.log(arguments[2])
}
myFunction(1,2,3)
```

### Variabili locali e globali 
Possiamo dichiarare le variabili all’interno del corpo di una funzione. Queste variabili sono accessibili soltanto all’interno della funzione e non vengono viste fuori di essa o, in termini tecnici, hanno uno scope locale.
Lo scope o ambito di visibilità di una variabile è la parte di uno script all’interno del quale si può fare riferimento ad essa. Le variabili dichiarate all’interno di una funzione sono dette locali alla funzione dal momento che sono accessibili soltanto
all’interno del suo corpo.
Le variabili dichiarate fuori da qualsiasi funzione sono dette globali e sono accessibili da qualsiasi punto dello script, anche all’interno di funzioni.

#### Espressioni di Funzione 
Un modo alternativo per scrivere una funzione è attraverso la tecnica di «espressione di funzione» cioè memorizzare una funzione all’interno di una variabile in questo modo :
```
function test1(){}
```

```JS
var test1 = function (){

}
```


Prima cosa da notare è che abbiamo messo il punto e virgola alla fine, in quanto è una assegnazione (`nomeVariabile = valore`) con l’unica differenza che il valore è una funzione.
Per richiamare la funzione è sufficiente usare il nome della variabile seguito dalle parentesi tonde (quindi nello stesso modo della dichiarazione di una
funzione normale). La domanda quindi è… effettivamente cosa cambia tra le due modalità ?

La differenza sta nel fatto che se la dichiaro come variabile non posso richiamarla ovunque, ma solo dopo averla dichiarata e valorizzata, mentre se la dichiaro nel modo «classico» posso chiamarla ovunque anche prima di dichiararla.
Questo perché javascript all’avvio fa una cosa «strana» (tanto per cambiare) chiamata «HOIST» :
cioè prende tutte le funzioni e le mette in testa al codice in modo da poterle richiamare ovunque.

```JS
test1();//Errore
test2();//OK
var test1 = function(){
	console.log('espressione di funzione);
}
function test2(){
	console.log('funzione classica')
}
```


### Parametri di defualt 
Prima di ES6 non era possibile dare dei valori di default ai parametri di una funzione. Quindi se avevamo una funzione con dei parametri in ingresso dovevamo controllarli con una if ed eventualmente se vuoti assegnargli manualmente dei valori in questo modo :
```JS
function prova (a,b){
	a = a||0
	b = b || 0 
	console.log(a);
	console.log(b);
}
prova(); //0 0
prova (5,6); // 5 6
```

Invece con ES6 è possibile dare dei valori di default (come in per le funzioni di Python) direttamente in ingresso alla funzione in questo modo :
```
function prova (a = 0, b = 0){
	console.log(a);
	console.log(b);
}
prova(); // 0 0
prova (5, 6); // 5 6

```