## Cos'è il match Statement in [[Introduzione a Python|Python]]
Il **match statement** è una funzionalità introdotta in Python 3.10 che permette di eseguire operazioni basate sulla corrispondenza di pattern (pattern matching). È particolarmente utile quando si devono gestire diversi casi in modo chiaro e leggibile, evitando lunghe catene di [[Cicli e condizionali#Sintassi dei conditional statements|`if`]] ,[[Cicli e condizionali#^elif-Def|`elif`]] ,[[Cicli e condizionali#^else|`else`]].
==Il match statement funziona confrontando il valore di una variabile con una serie di pattern (casi).== 
==Se un caso corrisponde, viene eseguito il blocco di codice associato. Se nessun caso corrisponde, viene eseguito il caso di default (`case _`).==
==In altre parole Il match statement è ideale quando devi gestire molti casi distinti basati sul valore di una variabile.==  ^matchStats-Def


Supponiamo di stare a una festa di simulare il gioco di Mario Kart, dobbiamo fare 3 giri di una pista e finito il terzo giro ogni giocatore finisce il gioco e viene visualizzata la classifica. 
Vogliamo di raccogliere le posizioni finali: se l'utente inserisce la posizione uno il programma la ritorna in posizione cardinale (`1st`) e cosi via.
Considera l'utente inserisca i numeri 1,2,3 e ci deve stampare i numeri cardinali `1st`, `2nd`, `3rd`, dal 4 in poi si usa il `th` 
```python
n = int(input("Inserire un numero:"))

  

if n == 1:

    print(f"{n}st!")

elif n == 2:

    print(f"{n}nd!")

elif n == 3:

    print(f"{n}rd!")

elif n == 4:

    print(f"{n}th!")

else :

    print(f"{n}th!")
```
^ex-matchCase

In questo esempio sono stati valutati tutti i valori possibili di `n` e per ogni valore veniva stampato il messaggio con la nomenclatura cardinale. Questo ovviamente diventa complicato quando scriviamo righe e righe di codice, in questo caso viene in aiuto il match statement: 
è un metodo che ==migliora la leggibilità del codice e la comprensione e fa parte della buona pratica di programmazione==.
### Funzionamento e sintassi del Match Statement
Si parte da una variabile con un determinato valore, e si prende questa variabile si fanno vari casi e per ogni caso deve eseguire una determinata istruzione. 
Se nessun case è vero allora si passa al case di default (`case _`). 
In parole povere la sintassi del match case è: 
```python
match variabile:
    case pattern1:
        # Blocco di codice da eseguire se variabile corrisponde a pattern1
    case pattern2:
        # Blocco di codice da eseguire se variabile corrisponde a pattern2
    case pattern3 (opzionale(if condizione)):
        # Blocco di codice da eseguire se variabile corrisponde a pattern3 E la condizione è vera
    case _:
        # Blocco di codice da eseguire se nessun caso corrisponde (caso di default)
```
#### Componenti della sintassi
1. `match variabile`:
- ==Inizia il match statement specificando la variabile che vuoi confrontare con i vari pattern== (ad esempio: nell'[[#^ex-matchCase|esercizio]] sopra la variabile da confrontare è `n`, di conseguenza scriverò `match n`, dove `n` è la variabile da confrontare). 
1. `case pattern:`: 
- ==Definisce un caso specifico.== 
  Se il valore della variabile corrisponde al pattern, viene eseguito il blocco di codice associato (Ad esempio: nell'[[#^ex-matchCase|esercizio]] sopra al posto di `if n==1:` scriverò `case 1:` perché corrisponde al caso in cui la variabile è uguale a `1`).
1. [[#Il match statement e le condizioni|`if condizione`]]: 
- si può usare i conditionals statements con i match case, questo aspetto verrà approfondito più avanti.  ^cond-stats-N-matchCase
1. `case _:`:
  -  ==Rappresenta il caso di default, che viene eseguito se nessun altro caso corrisponde.== 
   In parole povere `case _:` gestisce tutti i casi non coperti dai pattern precedenti.  ^defaultCase

Quindi [[#^ex-matchCase|l'esercizio]] può essere riscritto così:
```python
match n:
	n = 1
	case 1:
		print(f"{n}st!")
	n = 2:
	case 2:
		print(f"{n}nd!")
	n = 3
	case 3:
		print (print(f"{n}rd!")
	n = 4 
	case 4:
		print(f"{n}th!")
	#default case
	case _: 
		print(f"{n}th!")

```
Come si può vedere da questo esempio il match abbiamo dichiarato il `match n` all'inizio del blocco di codice del match statement.
In seguito abbiamo definito i `case pattern` in base al valore della variabile che vogliamo confrontare. 
Per ultimo abbiamo impostato il caso di default `case _:`: se tutti gli altri pattern non sono veri allora il flusso analizza il caso di default ed esegue l'azione che corrisponde a quel caso.

Il match statement può essere usato in qualsiasi contesto (match annidati, `if, elif, else`, `while` e `for` loop). 

### Match statements e [[Gli Operatori#Gli operatori logici|OR]](`|`)
Si può usare l'operatore `|`(OR) per combinare più pattern in un singolo caso. Questo è utile quando vogliamo gestire più valori nello stesso modo. 
#### Gestione di codici di stato HTTP
Supponiamo di avere [[Lezione 4 - Protocollo HTTP 2 parte#Status Code HTTP|uno stato HTTP]] da gestire.
Posso confrontare più valori associati a quello stato in 2 modi:
1. **Primo Modo:**
```python
#http status (if/elif/else version)
http_status = 200
if http_status ==200 or http_status ==201:
	print("success")
elif http_status==400:
	print("Bad Request")
elif http_status==500 OR http_status==501
	print("Server Error")
case _:
	print("Unknown")
```
1. **Secondo modo (Match statement):**

```python
http_status = 200
match http_status:
	case 200|201:
		print ("Success")
	case 400:
		print("Bad Request")
	case 404:
		print("Not Found")
	case 500|501:
		print("Server Error")
	case_:
		print ("Unknown")
```

> [!NOTE] Da notare come in questo caso l'OR è tradotto con il simbolo `|`, questo perché nel match statement se scrivo `or` Python mi dà errore. 
>Inoltre l'uso di `|` rende il codice più compatto e leggibile rispetto a una catena di `if-elif`. 


### Il match statement e le [[Cicli e condizionali#Conditional Statements|condizioni]] 
Puoi aggiungere condizioni specifiche a un caso usando `if`. 
[[#^cond-stats-N-matchCase|Questo ti permette di gestire casi più complessi]].
#### Classificazione di numeri in base a prorietà 
```python
#insert a number
n = int(input("Insert a number"))
match n:
case n if n>0 and n%2==0: #in questo caso l'if diventa sia: "se il caso n sia maggiore di zero e pari"
	print (f"{n} is positive and even")
case n if n>0 and n%2!=0:
	print(f"{n} is postive and odd)
case n if n<0 and n%2==0:
	print(f"{n} is negative and even")
case n if n<0 and n%2==0:
	print(f"{n} is negative and odd")
case_:
	print("The inserted number is 0")
```
Analizzando questo esempio possiamo vedere come l'utilizzo di `if` sia utile. 
In particolare:
- **`case n if condizione`**: 
Puoi usare `if` per aggiungere condizioni specifiche a un caso.
- **Flessibilità**: 
Questo approccio è molto flessibile e ti permette di gestire casi complessi senza dover scrivere codice ridondante.
Il match si usa solo quando la variabile assume diverse valori e seguendo questi valori devo far eseguire determinate azioni.

Visto così in realtà il match statement sembra essere un'alternativa più elegante e leggibile ai tradizionali **conditional statements** in Python, tuttavia sono due modi di procedere diversi:
1. **Match Statements:**
è particolarmente utile in situazioni specifiche dove il **pattern matching** (corrispondenza di pattern) semplifica notevolmente il codice e lo rende più intuitivo.
Il match statement è ideale quando devi gestire molti casi distinti basati sul valore di una variabile
1. **[[Cicli e condizionali#Conditional Statements|Conditional Statements]]:**
Utile quando le condizioni sono complesse e non si basano su pattern specifici (es: confronti tra più variabili, operazioni logiche intricate), i conditional statements tradizionali sono più adatti.

> [!Example] Esempio Pratico 
>```python
>x = 10
y = 20
>
>if x > y:
  >  print("x è maggiore di y")
>elif x < y:
 >   print("x è minore di y")
>else:
 >   print("x è uguale a y") 
>```


> [!example] In Conclusione
>
> Usa il **match statement** quando:
>
>- Devi gestire molti casi basati su valori specifici.
  >  
>- Lavori con strutture dati complesse (liste, dizionari, tuple).
  >  
>- Vuoi estrarre valori da strutture dati.
  >  
>- Vuoi migliorare la leggibilità del codice.
  >  
>
>Usa i **conditional statements tradizionali** quando:
>
>- Le condizioni sono complesse e non basate su pattern.
>- Devi supportare versioni di Python precedenti alla 3.10

### Match Statement e [[Introduzione a Python#Variabili|variabili]] 
Mettiamo si abbiano 2 variabili:
```python
g = "f"
age = 5
match (g,age):
	case ("f", 5):
		print("Piccola!")
	case ("m", 5):
		print("Piccolo!")
	case (f",10):
		print("Grande")
	case ("m", 10):
		print("Gigante")
	case_:
		print("Kinder Sorpresa!")
```
Quindi riprendendo dalla [[#^matchStats-Def|definizione di match statements]], in questo esempio una volta dichiarati le variabili `g` e `age` con i rispettivi valori, queste variabili vengono racchiuse in una tupla `g, age` e ogni `case` rappresenta un pattern specifico per la tupla.
Quindi ogni `case` definisce un pattern che la tupla (`g, age`) deve soddisfare:
1. **Primo `case` (`case (f, 5)`):**
- Questo caso corrisponde se `g == "f"` **e** `age == 5`.
- Se la tupla `(g, age)` è `("f", 5)`, viene eseguito il blocco di codice associato: `print("Piccola!")`.
2. **Secondo `case` (`case ("m", 5)`):**
- Questo caso corrisponde se `g == "m"` **e** `age == 5`.
- Se la tupla `(g, age)` è `("m", 5)`, viene eseguito il blocco di codice associato: `print("Piccolo!")`.
3. Terzo `case` (`case ("f", 10`)): 
- Questo caso corrisponde se `g == "f"` **e** `age == 10`. 
- Se la tupla `(g, age)` è `("f", 10)`, viene eseguito il blocco di codice associato: `print("Grande!")`.
4. **Quarto `case`(`case("m", 10)`):** 
- Questo caso corrisponde se `g == "m"` **e** `age == 10`.
- Se la tupla `(g, age)` è `("m", 10)`, viene eseguito il blocco di codice associato: `print("Gigante!")`.
5. **Caso di default (`case _`):** 
- Il caso di default (`case _:`) viene eseguito se **nessuno dei casi precedenti** corrisponde.
- Rappresenta tutti i casi non coperti dai pattern specifici.
- Nel tuo esempio, se la tupla `(g, age)` non corrisponde a nessuno dei casi precedenti, viene eseguito il blocco di codice associato: `print("Kinder Sorpresa!")`.




### Match Statement e [[Collections#Le liste|liste]] 
Puoi usare il match statement per confrontare liste e gestire casi specifici in base al loro contenuto o lunghezza fissa.
#### Gestione di ingredienti   
```python
ingredienti = ["Pomodoro", "mozzarella", "basilico"]
match ingredients:
	case ["pomodoro", "mozzarella", "basilico"]:
		print("Puoi fare una Caprese!")
	case ["pomodoro", "mozzarella", *_]: 
		print("Puoi fare la Pasta al pomodoro")
	case ["Pane", "Prosciutto", "Formaggio"]:
		print("Puoi fare un Panino!")
	case_:
		print("Non saprei cosa consigliare...sperimenta!")
```
Analizziamo questo esempio:
- `*_`: 
Rappresenta "tutti gli elementi rimanenti". 
Ad esempio, `case ["Pomodoro", "Mozzarella", *_]` corrisponde a una lista che inizia con "Pomodoro" e "Mozzarella", seguita da qualsiasi altro elemento.
Quindi se ho una lista che inizia con gli elementi `"Pomodoro"` e `"Mozzarella"`, mi riporterà subito al caso due. 


### Match statement e dizionari
Puoi usare il match statement per confrontare dizionari e gestire casi specifici in base alle loro chiavi e valori.

#### Gestione di utenti

```python
user = ("nome": "Luca", "ruolo": "admin")
match user: 
case("nome": name, "ruolo": "admin"): #la variabile name serve per definire il fatto che volgio concdntrarmi sul valore della chiave ruolo perchè non voglio porre l'attenzione sulla chiave nome. 
	print(f"Benvenuto amministratore {name}")
case ("nome": name, "ruolo": "utente")
	print(f"Bwenvenuto utente {name}")
case _:
	print ("Ruolo non riconosciuto")
```
Questo mi è utile quando voglio estrare i valori da un dizionario e usarli nel blocco di codice associato al caso. 
Ad esempio Ad esempio, `{"nome": name}` estrae il valore associato alla chiave `"nome"` e lo assegna alla variabile `name`.

> [!Error] Da non confondere con l'altro metodo per estrare i valori dei dizionari visto fino ad adesso 
>```python
> user = ["nome": "Luca", "ruolo": "admin"]
>match user:
>	case ("nome": name["Luca"], "ruolo": "admin"):
>```
>In questo caso mi ritornerà errore perché, in Python, con il match case non si può fare

> [!success] 
> 
> ```python
>  
> 		print("Admin")
> 	case ("nome": name, "ruolo": "admin"): 
> 		print("admin")
> ```

### Match statement e tuple
Puoi usare il match statement per confrontare tuple e gestire casi specifici in base ai loro elementi.
#### Gestione di punti in un piano cartesiano
```python
point = (3,5)
match point:
	case (0,0):
		print("Origine")
	case(x, 0):
		print(f"Punto sull'asse x: ((x), 0)")
	case (0, y):
		print(f"Punto sull'asse y: (0,(y)")
	case _:
		print(f"Punto generico: (point)")	
```
Analizziamo questo esempio
- **Estrazione di elementi**: Puoi estrarre elementi da una tupla e usarli nel blocco di codice associato al caso. Ad esempio, `case (x, 0)` estrae il primo elemento e lo assegna alla variabile `x`.
- **Pattern matching su tuple**: Puoi confrontare tuple di lunghezza fissa o variabile.
