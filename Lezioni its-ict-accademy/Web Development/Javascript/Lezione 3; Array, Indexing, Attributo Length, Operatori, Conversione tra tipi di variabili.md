# Introduzione 
Abbiamo visto nella [[Lezione 2 Le variabili in Javascript|scorsa lezione]] come inizializzare le variabili, fare il casting e altre funzionalità built-in, ora vediamo come utilizzare gli array di JS.

## Definire Array in JS
Gli array consentono di associare più valori ad un unico nome di variabile (o
identificatore). 
In genere i valori contenuti in un array hanno una qualche affinità (ad esempio l’elenco dei giorni della settimana). L’uso degli array evita di definire più variabili e semplifica lo svolgimento di operazioni cicliche su
tutti i valori. 
Ad es:
```js
var giorniDellaSettimana = [
"lunedì",
"martedì",
"mercoledì",
"giovedì",
"venerdì",
"sabato",
"domenica"];
```
Come si vede in questa dichiarazione i valori dell’array sono delimitati da
parentesi quadre e separati da virgole. 
Questo è un modo di definire un array basato sulla rappresentazione letterale (literal).
La sintassi per scrivere un array è:
==dichiarare la variabile `nome_variabile` seguita dal segno uguale e dalle parentesi quadre con all'interno gli elementi separati da una virgola.== 
Esempio:
```
var nomi = [ ‘Mario’ , ‘Anna’ , ‘Luca’ ] ;
```

Gli array in Javascript sono **dinamici**:
==crescono o si riducono in base alla necessità e non è necessario dichiarare una dimensione fissa per l’array al momento==
==della creazione:==
```js
nomi = [‘Mario’ , ’Anna’ , ‘Luca’ , ‘Francesca’] ;
```

### Indicizzazione degli array
I valori all'interno dell'array sono detti **elementi,** e ogni elemento ha una posizione numerica chiamata **indice**.
![[Indexing di un array.png]]

Questo vuol dire che se si vuole stampare o utilizzare, ad esempio, il valore `marzo` si deve fare:
```js
console.log(mesi[2]) //'marzo'
var meseScelto = mesi[2]
console.log(meseScelto) //'marzo'
```

Quindi una volta definito un array ==si può accedere ai singoli elementi facendo riferimento al nome della variabile e all'indice corrispondente all'elemento== (come in Python per accedere all'indice di un elemento di una [[Collections#Le liste|lista]]).
E, come per le liste di python o più generalmente per le collection, ==la numerazione degli elementi di un array parte da zero (o zero-based)==.
Quindi se riprendiamo l'array con i giorni della settimana:
```js
var giorniDellaSettimana = [
"lunedì",
"martedì",
"mercoledì",
"giovedì",
"venerdì",
"sabato",
"domenica"];

var primoGiorno = giorniDellaSettimana[0]
console.log(primoGiorno) // 'lunedì'
```

Come per le liste in Python, anche gli array di Javascript accettano valori di qualsiasi tipo di dato supportato in Javascript, quindi si possono avere array con elementi di diversi tipo:
```js
var mioArray = [123, "stringa", true, null];
```
Inoltre gli elementi degli array in JS possono essere sparsi, ovvero gli elementi non sono obbligati ad avere indici contigui
```js
let nomi = [];
nomi[0] = 'Mario';
nomi[1] = 'Anna';
nomi[2] = 'Luca';
nomi[3] = 'Francesca';
// questi non vengono assegnati: restano "vuoti"
nomi[9] = 'Carlo';

console.log(nomi); 
// ["Mario", "Anna", "Luca", "Francesca", <5 empty items>, "Carlo"]

```
In questo caso la posizione con indice 4,5,6,7,8 esistono ma rimangono vuote; quindi se si provasse a stampare [[#Attributo `length`|la lunghezza dell'array]] il risultato sarà che l'array ha 10 elementi.

In sintesi possiamo dire che le [[Collections#Le liste|liste di Python]] e gli array di JS presentano alcune analogia ma hanno una differenza chiave:
- ==entrambi sono **collezioni ordinate**==;
    
- ==entrambi possono contenere **elementi eterogenei**== (es. numeri, stringhe, oggetti);
    
- ==entrambi supportano **indicizzazione**== (es. `arr[0]` per accedere al primo elemento);
    
- ==entrambi supportano **metodi di modifica**== (es. `push`/`append`, `pop`, `slice`, ecc.).
Le differenze chiave tra array e liste sono:
1. **Array è un tipo "nativo ma speciale" in JS**:
    
    - Gli array in JS sono **oggetti** con metodi speciali.
        
    - In Python le liste sono un **tipo built-in** vero e proprio.
        
2. **Metodi e funzioni diverse**:
    
    - JS ha `map()`, `filter()`, `reduce()` come metodi dell’array.
        
    - In Python, `map()` e `filter()` sono **funzioni globali**, non metodi della lista.
3. **Mutabilità e confronto**
	abbiamo detto che sia le liste che gli array di JS e le lite di python sono mutabili:
```js
let arr = [1, 2];
arr[0] = 99;      // mutato
console.log(arr); // [99, 2]
```

``` run-python
lst = [1, 2]
lst[0] = 99       # mutato
print(lst)        # [99, 2]
```

Tuttavia cambia il confronto:
In JS gli array si confrontano per riferimento:
```js
console.log([1, 2] == [1, 2]);  // false
console.log([1, 2] === [1, 2]); // false
```
==Anche se il contenuto è lo stesso, i due array sono oggetti diversi in memoria, quindi il risultato è `false`==.
Ma se si assegna lo stesso riferimento:
```js
let a = [1, 2];
let b = a;
console.log(a === b);  // true
```

In Python, invece, come sappiamo le liste si confrontano per contenuto:
``` run-python
print([1, 2] == [1, 2])  # True
```
==In Python, il confronto =\= **verifica il contenuto**, non il riferimento.==

4. **Prestazioni e metodi avanzati:**
	In python le liste offrono una maggiore flessibilità e metodi potenti come `extend()`, `remove()`, `reverse()`, `count()`, `index()`, etc.
	Mentre in JS gli array sono ottimizzati per il browser e quindi sono più veloci in operazioni semplici, ma:
	- Hanno metodi avanzati integrati;
	- e, ad esempio, non esiste un metodo `insert()` diretto; si deve usare `splice`
```js
let arr = ["a", "b", "d"];
arr.splice(2, 0, "c"); // inserisce "c" in posizione 2
console.log(arr);      // ["a", "b", "c", "d"]
```

### Attributo `length` 
Questo attributo torna un integer che indica il numero di elementi che indica quanti elementi sono presenti all'interno di un array.
```
var giorniDellaSettimana = [
"lunedì",
"martedì",
"mercoledì",
"giovedì",
"venerdì",
"sabato",
"domenica"];

console.log(giorniDellaSettimana.length) // 6 (l'indicizzazione parte da 0 e arriva a 6)
```


> [!caution] Attenzione!
> Fare attenzione nel distinguere l’indice dell’array con la lunghezza dell’array.
>Ricordiamo che l’indice parte da ZERO mentre il conteggio della lunghezza parte da UNO.
>Questo vuol dire che, tornando all’esempio dei giorni della settimana, l’array ha una lunghezza di 7 elementi con indice che va da 0 a 6.

### Operatori aritmetici 
Per quel che riguarda il tipo di dato numerico, abbiamo gli operatori aritmetici, che, come in [[Gli Operatori#Gli operatori aritmetici|Python]] consentono la combinazione di valori numerici. 
Si tratta di operatori binari corrispondenti ai classici operatori matematici:

| Operatore |      Nome       |
| :-------: | :-------------: |
|    `+`    |    addizione    |
|    `-`    |   sottrazione   |
|    `/`    |    divisione    |
|    `*`    | moltiplicazione |
|    `%`    | modulo o resto  |

> [!Note] Da notare come manca il floor division (`//`) in JS

Anche in questo caso Gli operatori aritmetici seguono le regole di precedenza matematiche e, come in matematica, possiamo utilizzare le parentesi (ma soltanto quelle tonde) per modificare il loro ordine di valutazione:
$4 + 5 * 6 + 7 = 41$
$(4 + 5) * (6 + 7) = 117$

```js
let num1 = 10
console.log(num1); //10
console.log(num1/2); // 5
console.log(num1*3); // 30
console.log(num1* 'ciao'); //NaN
console.log(num1 + 'ciao'); // 10ciao
console.log(num1 + 10); // 20
```

### Gli operatori Compatti 
Come in Python per gli [[Gli Operatori#Gli operatori di assegnazione|operatori di assegnazione ]], ==oltre all’operatore uguale (=), esistono altri operatori di assegnamento derivanti dalla combinazione degli operatori aritmetici e dell’ operatore = ==. 
Essi rappresentano una abbreviazione di espressioni di assegnamento la cui espressione da assegnare utilizza lo specifico operatore aritmetico.

| Forma Compatta | Scritta Equivalente |
| -------------- | ------------------- |
| `x += y`       | `x = x + y`         |
| `x -= y`       | `x = x - y`         |
| `x *= y`       | `x = x * y`         |
| `x /= y `      | `x = x / y`         |
| `x %= y`       | `x = x % y`         |

### Operatori Unari
Questi tipi di operatori non esistono in Python e servono per incrementare, decrementare o assegnare segno positivo o negativo ai [[Lezione 2 Le variabili in Javascript#Numeri in JS|numeri in JS]]:

| Operatore | Nome                            |
| --------- | ------------------------------- |
| `+`       | Numero Positivo o cast a numero |
| `-`       | Negazione                       |
| `++`      | Incremento                      |
| `--`      | Decremento                      |
La negazione consente di ottenere un valore negativo di un numero. 
Ad esempio, `-x` è il valore negativo del valore numerico rappresentato dalla variabile `x`. 
Gli operatori di incremento e decremento, invece sono applicabili soltanto a variabili e consentono di ottenere un valore rispettivamente aumentato o diminuito di uno. 
È molto importante la posizione dell’operatore:
==se l’operatore si trova a sinistra dell’operando, l’operazione di incremento o decremento viene eseguita prima della valutazione dell’espressione, mentre se si trova a destra l’operazione viene eseguita dopo==. 
Chiariamo il concetto con due esempi:
```js
var x = 3;
var y = ++x;
```
In questo caso la variabile `x` verrà prima incrementata di uno ed il risultato verrà
assegnato alla variabile `y`. Quindi la situazione finale vedrà `x` e `y` con il
valore di `4`.
Mentre nel secondo caso:
```js
var x = 3;
var y = x++;
```
Il valore della variabile `x` verrà assegnato alla variabile `y` e soltanto successivamente `x` verrà incrementata di uno. 
Come risultato avremo `x` con il valore di `4` e `y` con il valore di `3`.

### Operatori relazionali 
Questi operatori sono, analogamente, [[Gli Operatori#Operatori di confronto (Comparison Operators)|gli operatori di confronto]] di Python:

| Operatore | Nome                                 |
| --------- | ------------------------------------ |
| `<`       | minore                               |
| `<=`      | Minore o uguale                      |
| `>`       | maggiore                             |
| `>=`      | maggiore o uguale                    |
| \==       | Valore Uguale (uguale a)             |
| `!=`      | Valore diverso (diverso da)          |
| \===      | Strettamente uguale (tipo o valore)  |
| \!==      | Strettamente diverso (tipo o valore) |

#### Coercizione in Javascript: Implicita vs. esplicita
Qui bisogna notare come gli operatori di confronto **uguale a** (\==) e **diverso da** (`!=`) agiscono in modo diverso rispetto agli operatori **strettamente uguale** (\=\==) e **strettamente diverso** (`!==`).  
La differenza sta nel concetto di **conversione (o coercizione)** in JavaScript, che può avvenire in due modi:
1. **Coercizione implicita:**
	==Avviene in maniera automatica, ad esempio con ` =​=` o `!=`==​.  ^coercizioneImplicita

```js
"5" == 5       // true  → stringa "5" viene convertita in numero 5
false == 0      // true  → false → 0
true == 1       // true  → true → 1
"" == false     // true  → "" → false
null == undefined // true → caso speciale
"true" == true  // false → "true" NON si può convertire in numero (diventa NaN)
```

In questi casi JavaScript applica **regole di conversione automatica** tra i tipi.

Per esempio, `"5" == 5`:

- Trova tipi diversi: stringa e numero
    
- Converte `"5"` in numero → `5`
    
- Confronta: `5 == 5` → `true`


> [!ticket] la coercizione implicita va usata **solo quando sei certo** di voler effettuare una conversione automatica.


2. **Coercizione esplicita:**
	==È quando forzi tu la conversione del tipo usando funzioni di **type casting**, ovvero forzando in maniera esplicita la conversione del valore del tipo di dato usando, ad esempio, `String()`, `Number()`, `Boolean()`, etc.==  ^coercizioneEsplicita
```js
Number("5")      // 5
Boolean("")      // false
Boolean("ciao")  // true
String(42)       // "42"
```

#### Esempi di coercizione esplicita
Con \=== e !\== non avviene nessuna conversione automatica, di conseguenza se i tipi sono diversi è subito `false` :
```js
"5" === 5   // false
true === 1  // false
"" === false // false
```


> [!ticket] Regola d'oro: Usare sempre \=== e !\== a meno che non si voglia intenzionalmente la conversione automatica tra i tipi di dato 

Detto questo notiamo come tutte le espressioni che utilizzano gli operatori relazionali,  restituiscono un valore booleano in base all’esito del confronto

```js
4 > 2 // true
5 != 4 + 1 //false
```



> [!danger]- **Attenzione ai confronti con i booleani**  
Come in Python, anche in JavaScript bisogna fare attenzione quando si confrontano valori con `true` o `false`.  
Questo perché JavaScript applica la **coercizione implicita**, e considera:
>
>- `true` equivalente a `1`
 >   
>- `false` equivalente a `0`
>```js
>var numero1 = 1;
>var numero2 = true;
>var numero6 = numero1 == numero2;    // coercizione implicita
>var numero7 = numero1 === numero2;   // confronto stretto (nessuna coercizione)
>
>console.log(numero6 + ' è di tipo ' + typeof(numero6)); // true è di tipo boolean
>console.log(numero7 + ' è di tipo ' + typeof(numero7)); // false è di tipo boolean
>```
>Spiegazione:
> - `numero1 == numero2` → `1 == true`
  >  
  > 	 - JS converte `true` in `1` (coercizione implicita) 
>	  - Risultato: `1 == 1` → `true`   
> 	- Quindi `numero6` è `true` e di tipo `boolean`
  > 	     
>- `numero1 === numero2` → `1 === true`
  >  
 >   - Tipi diversi: `number` vs `boolean`
 >       
 >   - Nessuna conversione automatica
 >       
 >   - Risultato: `false`
 >       
 >   - Quindi `numero7` è `false` e di tipo `boolean`
 > > [!done] Come accennato poco sopra, anche se `true == 1` restituisce `true`, `true === 1` restituisce `false` perché confronta anche i tipi.  
>> Di conseguenza è sempre meglio usare \=== per evitare ambiguità e risultati inaspettati dovuti alla **coercizione implicita**.


### Operatori logici 
Come per [[Gli Operatori#Gli operatori logici|Python]] anche JS ha i suoi operatori logici:
==consentono la combinazione di espressioni booleane.== 
JavaScript prevede due operatori binari e un operatore unario:

| Operatore | Nome |
|:---------:| ---- |
|   `&&`    | and  |
|  `\|\|`   | or   |
|    `!`    | not  |

Le seguenti sono espressioni che utilizzano operatori logici:
```
5 > 2 && 3 != 4 // true
true || 4 >= 6 // true
!5==5 // false
```

Siccome la combinazione di operatori logici con altre espressioni può essere insidiosa, nel senso che le regole di precedenza nella valutazione possono
generare valori diversi da quelli attesi. È opportuno pertanto utilizzare le parentesi per indicare esplicitamente l’ordine di valutazione e per renderle
più leggibili. Le espressioni precedenti diventano pertanto:
```js
(5 > 2) && (3 != 4) // true
true || (4 >= 6) // true
!(5==5) // false
```



---
## Conversione tra tipi di variabili

In JavaScript, le **variabili sono dinamiche**: possono contenere valori di qualsiasi tipo e **cambiare tipo** in qualsiasi momento.  
Questa flessibilità libera lo sviluppatore dal dover dichiarare esplicitamente il tipo di dato, ma **scarica sull’interprete JavaScript** il compito di effettuare **conversioni implicite** nei momenti critici.
Ad esempio :
```js
var x = "12";
var y = "13";
var z = x * y;
```
In questo caso, **le stringhe vengono convertite in numeri** perché l’operatore `*` funziona solo su numeri.  
✅ Risultato: `z = 156` (perché `"12" * "13"` → `12 * 13`)

Ma vediamo un altro esempio:
```js
var x = "12";
var y = x + 13;
```

L'output in questo caso sarà: `1213`, perché:
l’operatore `+` viene interpretato come **concatenazione**, poiché uno degli operandi è una stringa.
Mentre in questo caso:
```js
var x;
var y = x + 13;
```
L'output sarà `NaN`, perché:
`x` è `undefined`, e quando JavaScript prova a sommare `undefined + 13`, ottiene:  
❌ Risultato: `NaN` (`Not a Number`).

Quindi in assenza di indicazioni da parte dello sviluppatore, **JavaScript prende decisioni di conversione automatica**.  
Conoscere **le regole della coercizione** è fondamentale per evitare comportamenti inaspettati e bug difficili da individuare.
 Ogni tipo primitivo (number, string, boolean, undefined, null) può essere **convertito in un altro tipo** in maniera [[#^coercizioneImplicita|implicita]] o [[#^coercizioneEsplicita|esplicita]].


### Il metodo `prompt()`
Il metodo `prompt()` è una **funzione globale** di JavaScript che consente di far apparire una **finestra di dialogo** con un **campo di testo**, all'interno del quale l'utente può inserire del contenuto.

È possibile passare **una stringa come parametro** alla funzione: questa sarà visualizzata come **messaggio nella finestra** prima del campo di input.  
Se l’utente clicca su **"OK"**, `prompt()` restituisce il **valore inserito** (sempre come **stringa**).  
Se clicca su **"Annulla"**, restituisce `null`.

È analogo al metodo `input()` in Python:
```js
var nome = prompt(‘’inserisci il tuo nome’’);
console.log(nome);
```


> [!NOTE] Usa sempre **doppi apici (`"`) o singoli apici (`'`) corretti**, e non le virgolette tipografiche (come `‘’` o `“”`) che possono causare **errori di sintassi** in JavaScript.

