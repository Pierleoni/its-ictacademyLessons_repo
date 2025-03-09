Supponiamo di calcolare su Vs Code tutti i numeri interi tra `1` a `10`, da `20` a `37`, da `35` a `49`.

**Expected Output:**
- Somma gli interi da `1` a `10` = `55`
- Somma gli interi da `20` a `37` = `513`
- Somma gli interi da `35` a `49` = `630`
Per fare ciò normalmente bisognerebbe fare questo:

```python
somma:int = 0

for number in range (1,11):

    somma += number

    print(somma)

  

sum:int= 0

for numbers in range (20, 38):

    sum = sum + numbers

    print(sum)

  
  

summa:int = 0

for i in range (35, 50):

    summa+=i

    print(summa)
```
Da notare come ho dovuto riscrivere per tre volte lo stesso codice, l'unica cosa che cambia è il range dei numeri, cioè i parametri che la funzione `.range()` assume.
Come abbiamo visto nell'esempio, alle volte ci troviamo con la necessita di riscrivere più e più volte lo stesso codice, quindi dobbiamo trovare uno strumento che ci permette di scrivere il codice lo stresso codice e richiamarlo più volte, Come per i cicli che iterano ad esempio più volte il commando al suo interno.


## Le funzioni
==Permettono di eseguire un insieme di istruzioni più volte senza doverlo riscrivere.==  
Grazie alle funzioni, possiamo definire un blocco di codice una sola volta e richiamarlo ogni volta che serve, rendendo il programma più organizzato e leggibile.
### **Cos'è una funzione?**

Una **funzione** è un insieme di istruzioni progettato per eseguire una specifica operazione. A questo gruppo di istruzioni viene assegnato un **nome**, che ci permette di richiamarle all'interno del codice senza doverle riscrivere ogni volta.


> [!done] Vantaggi delle funzioni
>  - **Modularità** : 
>    Suddividono il codice in parti più piccole e organizzate.  
 > - **Riutilizzabilità** : 
 >   Permettono di evitare la duplicazione del codice.  
>  - **Flessibilità** : 
>    Possono ricevere **valori in input**, eseguire operazioni e **restituire un valore in output**.

### Sintassi
La sintassi di una funzione di [[Introduzione a Python|Python]] è la seguente: 
1. `def`: 
   ==Keyword che indica l’inizio della definizione di una funzione.==
   Quindi "informa" Python che si sta definendo una funzione.  
2. `functionName`: 
   ==Il nome assegnato alla funzione.==
3. `(list of parameters)`: 
   ==Elenco opzionale di [[#Argomenti e parametri|parametri]] che la funzione può ricevere in input.== 
4. `:`: 
   ==I due punti indicano l'inizio del blocco di codice della funzione.==
5. **Corpo della funzione (Blocco di codice indentato):**
   ==Contiene le istruzioni che verranno eseguite quando la funzione viene chiamata.==

```python
def functionName (list of parameters):
	instructions for function body
```
Se una variabile e una funzione hanno lo stesso nome, possiamo distinguerle grazie alle **parentesi tonde**:

- Se il nome è seguito da `()`, si tratta di una funzione.
- Se il nome è usato senza parentesi, è una variabile.
Alcune funzioni non richiedono particolari parametri input. 
Ad esempio le funzioni della classe stringa(`.lower()`, `.upper()`, etc), questo perché sono un particolare tipo di funzioni (dette [[#^built-inFun|built-in]]) che non richiedono parametri in input poiché agiscono sull tipo di dato(in questo caso la stringa) su cui sono chiamate. 
Ovviamente non tutte le funzioni native di Python non richiedono parametri in input , ad esempio la funzione [[Cicli e condizionali#La funzione `range`|`.range()`]] accetta tre valori in input. 


> [!Bug]- Nome delle variabili e nomi delle funzioni
> Come abbiamo già detto Python è un linguaggio [[Introduzione a Python#Object-Oriented|orientato agli oggetti]], per cui i nomi delle variabili [[Introduzione a Python#Le variabili di python sono dei puntatori non dei recipienti!|non sono dei recipienti ma dei puntatori]]. 
> Partendo da questi due concetti se si dichiara una variabile e le si assegna un valore:
>```python
>#Dichiaro una variabile
>number_value:int = 5
>print(number_value) #Output:5 
>print(type(number_value)) #Output:class int
>
>#Dichiaro una funzione con lo stesso >nome 
>def number_value():
>	print("Hello")
>
>print(number_value) #Output: function number_value at 0x0000021A9CCACA40
>print(type(number_value)) #Output: class function
>```
>Quindi come possiamo vedere dopo aver ridefinito `number_value` come funzione, il nome non fa più riferimento all'intero `5`, ma all'oggetto funzione



### Esempio pratico di una funzione in Python
Prendiamo come esempio questa funzione:
```python
def sum_range (a:int, b:int):
	result:int = 0
	for i in range (a, b+1):
		result = result +i
	return result
```

In questo caso voglio generalizzare la somma di tutti i numeri interi all'interno di un certo intervallo estremi inclusi, quindi ho bisogno di due valori `a` e `b`:

1. **Parametri in input**:
    - `a` (intero) → estremo inferiore dell’intervallo.
    - `b` (intero) → estremo superiore dell’intervallo.

2. **Inizializzazione della variabile `result`** a 0.

3. **Ciclo `for`**:
    - Scorre i numeri da `a` a `b` (incluso `b`, quindi si usa `range(a, b+1)`).
    - Ad ogni iterazione, aggiunge il valore corrente alla variabile `result`.
4. **Restituzione del risultato** con `return result`.

Come per la variabile che le si assegna un nome appropriato per rappresentare al meglio possibile il valore di quel dato, stessa cosa lo si fa per le funzioni. 




Per riutilizzare le funzioni devo (in Python si dice richiamare o invocare una funzione) una funzione devo scrivere il nome della funzione dopo averla definita:
```python
def sum(a:int, b:int):
	result:int = 0
	for i in range(a, b+1):
		result = result + i
	return result

mysum= sum (1,10)
```
Richiamo la funzione e la salvo nella variabile `mysum` per salvarla in memoria, come argomenti messi in input vi sono i numeri `1` e `10` che corrispondono rispettivamente ai parametri `a` e `b` della funzione.
Se vado a sostituire 1 e 10 all'interno della mia funzione?
Cambio i parametri per calcolare la somma tra i numeri interi.
Una volta definita la definizione posso riutilizzarla quante volte mi pare. 
Vediamo come possiamo riscrivere meglio questo pezzo di codice:
```python
def sum(a:int, b:int):
# define a sum to be computed
	result:int = 0
	# compute a sum
	for i in range(a,b+1):
		result = result + i
# return the value of sum as the output of the sum function
	return result
# use sum function to compute a sum of integers from 1 to 10
print(f"Sum from 1 to 10 is {sum(1,10)}")
# use sum function to compute a sum of integers from 20 to 37
print(f"Sum from 20 to 37 is {sum(20,37)}")
# use sum function to compute a sum of integers from 35 to 49
print(f"Sum from 35 to 49 is {sum(35,49)}")
```

In questo caso siccome la funzione `sum` ci restituisce un valore la posso anche scrivere direttamente all'interno di un `print()` formattato. 
Posso anche annidare funzioni tra loro 


---


#### Esercizio 
Definiamo una sottrazione `subtract`:
- Deve prendere 2 parametri in input 
- dentro la funzione deve sottrarre i due parametri 
- in seguito ritorna la funziona
```python
def subtract (a:int, b:int):

    result:int= 0

    result= a-b

    return result

print(f"La sottrazione tra 10 e 5 è: {subtract(10,5)}")
```


---

### User defined functions e le built-in functions
Python ha diversi tipi di funzioni
- **built-in functions**: 
  ==Funzioni integrate in Python== (`print()`,etc.).  ^built-inFun
  Sono le più efficienti in quanto offerte già da Python quando lo si installa.


- **User defined functions:** 
  ==Sono le funzioni scritte dal programmatore.== 
  Consentono ai programmatori di scrivere blocchi di codice riutilizzabili per rendere il codice più pulito e più leggibile, quindi possiamo dividere un problema complesso in parti più piccole e semplici da gestire.
Queste funzioni possono essere integrate in librerie esterne come `pyp` o `pip`, ad esempio.


> [!bug] Nomi delle funzioni
> 1. Non dare nomi alle funzioni User defined delle funzioni built-in (come ad esempio `min`, `max`, `range()`, etc.)
> 2. Non usare un nome assegnato a una variabile precedentemente e poi dare lo stesso nome alla funzione

> [!hint]
> È consigliabile non fare funzioni troppo generabili che funzionano per ogni dato, le funzioni devono avere un focus specifico per quell'operazione su quei dati specifici, esattamente come per le [[Collections#Le liste|liste]], nelle quali posso inserire ogni tipo di dato(integer, float, stringa, booleano), ma è sconsigliabile farlo. 
> Come per le esercizio della funzione di sottrazione; è meglio creare una funzione generale che dati due interi me li sottrae 

### Il Return 
Ogni volta che una funzione contiene un'istruzione `return`, ==essa restituisce un **valore** in output.== 
**Perché è importante restituire un valore?**
Se una funzione non ritorna un valore, non può essere sfruttata al meglio. Invece, se la funzione restituisce un valore, possiamo:
- ==**Salvare** il risultato in una variabile,==
- ==**Stampare** il risultato in output,==
- ==**Usarlo** in altre operazioni.== 
In altre parole, una funzione che non ha la parola chiave `return` non fornirà alcun risultato che possiamo utilizzare al di fuori di essa.
Questo significa che quando definisco la funzione `subtract`, questa mi ritorna il valore della sottrazione `a-b`.  

> [!hint]
> In alto a destra c'è una freccia che è scritta come `->:int` questo significa che la funzione restituisce un intero 
> ![[function Python.png]]
> Questo tipo di nomenclatura posso scriverla in Python.

#### Return vs Print
Immaginiamo di riprendere la funzione `subtract()` e di passarle in input `10` e `5`, sapendo che la sottrazione dà `5`. 
- **Con `print`**: 
  ==il valore della sottrazione viene **stampato in output**, ma non è accessibile altrove nel programma.==
- **Con `return`**: 
  ==Invece, la funzione **restituisce il valore** della sottrazione, permettendoti di salvarlo, utilizzarlo in altre operazioni o stamparlo in seguito.==
Se non salvi il risultato della funzione che utilizza `return` in una variabile, la sottrazione viene comunque eseguita, ma non puoi usarla di nuovo a meno che non la salvi prima.

**Prendiamo ad esempio una funzione senza il** `return`:
```python
def greet (name:str) →None:
	print(f"Hello {name}")
greet ("Angela")
>>>Hello Angela
Print(type(greet(Angela)))
>>> <class 'NoneType'>
```

In questo esempio:

- La funzione `greet` stampa un messaggio di saluto, ma non restituisce un valore (il ritorno implicito è `None`).
- Se proviamo a fare `print(type(greet("Angela")))`, il tipo restituito è `NoneType`, perché la funzione non ritorna nulla, ma solo stampa il messaggio.

In altri linguaggi di programmazione bisogna specificare i valori che ritorna quella funzione.

Per fare un ulteriore esempio:
```python
def greet(name):

    print(f"Hello, {name}")

user_name = greet("Angela")
print(user_name)
```
- La funzione `greet("Angela")` riceve l'argomento `"Angela"` e **stampa** `Hello, Angela` grazie al comando `print` all'interno della funzione.
  
- Tuttavia, la funzione `greet()` non ha un `return` esplicito, quindi **non restituisce nulla**. Per impostazione predefinita, se una funzione non ha un `return`, Python restituisce `None`.
  
- Quando provi a **stampare** `user_name`, il valore assegnato a `user_name` è `None`, perché la funzione non restituisce alcun valore, quindi `user_name` contiene `None`.
  
Mentre se io scrivessi:
```python
def greet(name):
	return(f"Hello, {name}")

user_name = greet("Angela")
print(user_name)
```
In questo caso: 
- La funzione `greet("Angela")` riceve l'argomento `"Angela"`.
- La funzione **resta nella memoria,** il risultato tramite `return f"Hello, {name}"`, che restituisce il messaggio `"Hello, Angela"`.
- La variabile `user_name` riceve questo valore di ritorno e quindi contiene la stringa `"Hello, Angela"`.
- Quando poi stampi `user_name`, il valore che contiene viene visualizzato in output, quindi **vedi** `Hello, Angela`.


> [!example] In sintesi
>- **`print()`** all'interno della funzione fa **solo visualizzare** il risultato in output, senza permettere di usarlo altrove nel programma.
>- **`return`** permetterebbe alla funzione di **restituire un valore** che puoi utilizzare successivamente.

#### Ritorno di più valori 
Python ci consente di ritornare in output più valori contemporaneamente da una funzione.
La forma più comune per farlo è tramite una **tupla**. 
Una funzione che restituisce una tupla può restituire più valori separati, e questi possono essere assegnati a variabili separatamente.
```python
# define a function returning multiple values(returning a tuple)
def operations(a: int, b: int) -> tuple[int, int]:

	sum_result:int = a + b
	diff_result:int = a – b
	# Returns a tuple with two values
	return sum_result, diff_result

# Assigns values to two variables
sum_value, diff_value = operations(10, 5)

print("Sum:", sum_value) # Output: Sum: 15

print("Difference:", diff_value) # Output: Difference: 5

print(type(operations(10,5)))

>>> <class 'tuple'>
```

Quando una funzione deve restituire più di un valore, Python offre diverse opzioni per farlo. 
In Python, una funzione può restituire più valori utilizzando **tuple, liste o dizionari**.
1. **[[Collections#Tuple|Tupla]]**: 
   ==una struttura dati che può contenere più valori, ed è **immutabile**, cioè non puoi modificarne gli elementi una volta che la tupla è stata creata.==  ^tuple-func
   
2. **[[Collections#Le liste|Lista]]**: 
   ==una struttura dati che può anch'essa contenere più valori, ma è **mutabile**, quindi puoi aggiungere, rimuovere o modificare gli elementi.==   ^list-func
   
3. **[[Collections#I dictionaries|Dizionari]]**: 
   ==Permettono di restituire valori con chiavi descrittive, migliorando la leggibilità del codice.==   ^dict-func


Come detto poco sopra, in Python, se una funzione deve restituire più di un valore, solitamente si usa una **tupla**. 
La sintassi per farlo è molto semplice, infatti puoi restituire i valori separandoli con delle virgole, e Python li restituirà automaticamente come una tupla.

**La tupla di un elemento è l'elemento stesso:**
==Quando una funzione restituisce solo un **singolo valore** separato da una virgola, Python lo interpreta come una **tupla di un solo elemento**.== 
Questo accade perché, in Python, le tuple sono definite da una **virgola**, non dalla parentesi tonde. Pertanto, se restituisci solo un valore seguito da una virgola, Python lo considera come una tupla contenente quel valore.

> [!example]+ Esempio
> ```python
> def single_value():
>     return 5,  # Questo è un ritorno di una tupla con un solo elemento
> 
> ```

Anche se c'è un solo elemento, Python considererà `5,` come una tupla con un solo valore: `(5,)`.
Se omettessi la virgola, Python restituirà un singolo valore senza creare una tupla.

> [!example]+ Esempio
> ```python
> def single_value():
> 	return 5
> 
> value = single_value()
> print(type(value))
> 
> #Output:
> <class 'int'>
> ```
> 

==Se invece restituisci una **lista**, Python ti permette di restituire più valori in una struttura **mutabile**, il che significa che i valori al suo interno possono essere modificati, aggiunti o rimossi.==  ^passing-list
> [!example]+ Esempio
>```python
> def return_list(a, b):
  >  return [a, b]  # Restituisce una lista contenente i due valori
>
>```


Stampa una tupla perché gli sto ritornando delle quantità definite secondo una sequenza ordinata e siccome questi valori non possono essere modificarti perché è la funzione li può modificare, e li ritorna in modo diretto, Python li calcola come se fosse una tupla perché le tuple non sono modificabili. 

### Passare una [[#^list-func|Lista]]
In Python, una funzione può restituire più di un valore utilizzando tuple, liste o dizionari. Il metodo più comune è la restituzione di una in cui i valori sono separati da una virgola dopo l'istruzione `return`.
[[#^passing-list|Come detto poco prima]], spesso è utile passare una lista a una funzione, sia che contenga nomi, numeri o oggetti più complessi, come ad esempio i [[Collections#I dictionaries|dizionari]].  
Quando si passa una lista a una funzione, quest'ultima ha accesso diretto ai suoi contenuti.
```python
# define a function returning a list
def get_coordinates(x:int, y:int) -> list[float]:
	return [x, y]

coords = get_coordinates(12.5, 45.8)

print(coords[0], coords[1], sep=", ")
>>> 12.5, 45.8

print(type(coords))
>>> <class 'list'>
```

Questa funzione **`get_coordinates`** prende in input due valori numerici `x` e `y` (di tipo `float`) e restituisce una **lista** (`return [x, y]`) contenente questi due valori.  
La notazione `-> list[float]` indica che il valore di ritorno è una lista di numeri in virgola mobile.

Con la variabile `coords = get_coordinates(12.5, 45.8)`, chiamiamo la funzione passandole `12.5` e `45.8`. La funzione restituisce la lista `[12.5, 45.8]`, che viene assegnata alla variabile `coords`.

Con `print(coords[0], coords[1], sep=", ")` stampiamo i due elementi della lista `coords`, separandoli con una virgola.  
Poiché `coords` è una lista con due valori (`[12.5, 45.8]`), il primo elemento (`coords[0]`) è `12.5` e il secondo (`coords[1]`) è `45.8`.

Con `print(type(coords))` verifichiamo il tipo di `coords`. L'output `<class 'list'>` conferma che `coords` è una lista.

#### Modificare una lista in una funzione 
Quando si passa una lista in una funzione, essa può modificare il contenuto della lista. Ogni cambiamento fatto alla lista che si trova dentro al corpo della funzione è permanente, e permette di lavorare in modo efficiente anche quando si ha a che fare con grandi quantità di dati. 

```python 
unprinted_designs:list[str] = ['phone case', 'robot pendant', 'Obs']

completed_models:list[str]= []

  
while unprinted_designs:
current_designs = unprinted_designs.pop()
print(f"Printing Model:{current_designs}")
completed_models.append(current_designs)


print("\nThe following models have been print:")
for completed_model in completed_models:
	  print(completed_model)
```
^cb-func

In questo esempio 
1. ho creato 2 liste:
	- La prima lista `unprinted_designs` contiene tre stringhe: `'phone case'`, `'robot pendant'` e `'Obs'`. 
	- La seconda lista è una lista vuota `completed_model`, che serve per contare i modelli stampati.
2. Dopodiché uso il ciclo `while` per spostare gli elementi:
	- `while unprinted_designs:`: 
	  Il ciclo `while` continua a eseguire il blocco di codice finché la lista `unprinted_designs` non è vuota.

> [!Info] 
> In Python, una lista vuota è considerata "falsy", quindi il ciclo termina quando tutti gli elementi vengono rimossi.

3. Uso la funzione `.pop()`:
   `current_designs = unprinted_designs.pop()`
   - La funzione `.pop()` rimuove gli elementi dalla lista e li restituisce
	   - Se `.pop()` viene chiamato senza argomenti, rimuove l'ultimo elemento della lista.
	   - Il valore rimosso viene salvato nella variabile `current_designs`. 
	   - l'ordine di rimozione sarà: `Obs`, poi `robot pendant` e infine `phone case`
4. Stampo l'elemento in fase di elaborazione:
   `print(f"Printing Model:{current_designs}")`.
5. Sposto il modello stampato nella lista:
   `completed_models.append(current_designs)`.
	- L'elemento rimosso da `unprinted_designs` viene aggiunto alla lista `completed_models`.
6. Dopo il `while` stampo i modelli completati:
   `print("\nThe following models have been print:")`
`for completed_model in completed_models:`
    `print(completed_model)`.
- Dopo che il ciclo `while` termina (cioè dopo che `unprinted_designs` è vuota), stampiamo tutti i modelli completati.

> [!faq]- Ordine di esecuzione del codice
>
> 
> 1. **Prima iterazione (`while unprinted_designs` non è vuota)**
>     - `.pop()` rimuove `'Obs'`
>     - Stampa: `"Printing Model: Obs"`
>     - Aggiunge `'Obs'` a `completed_models`
> 1. **Seconda iterazione**
>     - `.pop()` rimuove `'robot pendant'`
>     - Stampa: `"Printing Model: robot pendant"`
>     - Aggiunge `'robot pendant'` a `completed_models`
> 1. **Terza iterazione**
>     - `.pop()` rimuove `'phone case'`
>     - Stampa: `"Printing Model: phone case"`
>     - Aggiunge `'phone case'` a `completed_models`
> 1. **La lista `unprinted_designs` è ora vuota → il ciclo `while` termina.**
> 2. **Stampa finale della lista `completed_models`**

Possiamo riorganizzare questo codice scrivendo due funzioni, ognuna delle quali svolge un compito specifico. La maggior parte del codice non cambierà; lo struttureremo solo in modo più ordinato.

La prima funzione si occuperà della stampa dei modelli, mentre la seconda riassumerà i modelli che sono stati stampati.

```python
def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:

    """Sposta i modelli non stampati alla lista dei modelli completati."""

    while unprinted_designs:

        current_design = unprinted_designs.pop()

        print("Printing model:", current_design)

        completed_models.append(current_design)

  

def show_completed_models(completed_models: list[str]) -> None:

    """Mostra tutti i modelli stampati."""

    print("\nThe following models have been printed:")

    for completed_model in completed_models:

        print(completed_model)

  

# Liste iniziali

unprinted_designs: list[str] = ['phone case', 'robot pendant', 'Obs']

completed_models: list[str] = []  # Nome corretto

  

# Chiamata alle funzioni

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)
```

In questo caso: 
1. Abbiamo definito la funzione `print_models()` con due parametri: 
- una lista di designs che devono essere stampati (`unprinted_designs`)
- una lista dei modelli completi (`completed_models`). 
Date queste due liste, la funzione simula il printing di ogni design andando a svuotare la lista `unprinted_design` e riempiendo la lista `completed_models`. 
2. Definiamo la funzione `show_completed_models()` che ha un solo parametro:
   - La lista `completed_models`
Definendo la lista, `show_completed_models()` va visualizzare il nome di ogni modello che viene stampato.
Come possiamo notare questo programma ha lo stesso output della [[#^cb-func|versione senza le funzioni]], ma qui è più organizzato. 
Il codice che fa buona parte del lavoro è stato suddiviso in due funzioni separate, il che lo rende più facile da comprendere 
### Passare un [[#^dict-func|dizionario]] 
In Python, una funzione può restituire più di un valore utilizzando tuple, liste o dizionari. Il metodo più comune è la restituzione di una
in cui i valori sono separati da una virgola dopo l'istruzione return.
Come detto sopra, le funzioni in Python possono restituire più valori utilizzando tuple, liste e dizionari.
Ciò è utile quando devo maneggiare strutture dati complicate. 

```python
#define a function returning a dictionary
def get_user(myname:str, myrole:str) -> dict[str, str]:
	return {"name": myname, "role": myrole}

user = get_user(“Alice”, “Admin”)

print(user["name"]) # Output: Alice

print(user["role"]) # Output: Admin

print(type(user))
>>> Alice
>>> Admin
>>> <class 'dict'>
```

In questo caso:
1. - **Definizione della funzione `get_user()`**
    - Prende due parametri: `myname` e `myrole`, entrambi stringhe.
    - Restituisce un dizionario con due chiavi: `"name"` e `"role"`, i cui valori sono i parametri passati alla funzione.
- **Assegnazione della funzione a una variabile**
    - `user = get_user("Alice", "Admin")`
    - La funzione viene eseguita e il risultato (un dizionario) viene memorizzato nella variabile `user`.
- **Accesso ai valori del dizionario**
    - `print(user["name"])` → Stampa `"Alice"`, il valore associato alla chiave `"name"`.
    - `print(user["role"])` → Stampa `"Admin"`, il valore associato alla chiave `"role"`.
- **Verifica del tipo di dato**
    - `print(type(user))` mostra `<class 'dict'>`, confermando che `user` è un dizionario.

> [!deep]+ Differenza tra argomenti e parametri
> 
> Nell’esempio precedente, abbiamo definito la funzione `get_user()`, che accetta due parametri in input: `myname` e `myrole`.
> 
>Quando chiamiamo la funzione e le forniamo due valori (`"Alice"` e `"Admin"`), la funzione restituisce un dizionario con la formattazione corretta.
> 
> - **I parametri** `myname` e `myrole` sono **variabili definite nella funzione**, che rappresentano le informazioni di cui la funzione ha bisogno per svolgere il suo compito.
> - **Gli argomenti** `"Alice"` e `"Admin"` sono **i valori effettivi passati alla funzione** al momento della chiamata.
> 
> In altre parole, quando chiamiamo `get_user("Alice", "Admin")`,
> 
> - L'argomento `"Alice"` viene assegnato al parametro `myname`.
> - L'argomento `"Admin"` viene assegnato al parametro `myrole`.


> [!NOTE] Nota
> A volte le persone usano i termini **argomenti** e **parametri** in modo intercambiabile. Non sorprenderti se vedi le variabili nella definizione di una funzione chiamate **argomenti**, o le variabili in una chiamata di funzione chiamate **parametri**.
> >[!deep]- Spiegazione
> >Anche se i termini **argomento** e **parametro** hanno significati distinti in programmazione, capita spesso che vengano confusi o usati in modo errato.
>>
>>- **Parametro:** 
>>  ==È la variabile **dichiarata nella definizione della funzione**. È un segnaposto per il valore che verrà passato alla funzione.==
>>- **Argomento:**
>>  ==È il **valore effettivo** che viene fornito quando si chiama la funzione.==

### Funzioni e parametri 
Poiché una definizione di funzione può avere più parametri, una chiamata di una funzione potrebbe aver bisogno di argomenti multipli.
Esistono tre modi per passare argomenti a una funzione, assegnandoli ai rispettivi parametri
- ==passare l'argomento per [[#Argomento passato per posizione|posizione]]== 
- ==passare l'argomento per [[#Argomento passato per keyword|keyword]]== 
- ==passare l'argomento per [[#Argomenti passati per valori di default|valori di default]]== 
Quando gli argomenti vengono passati per posizione, gli argomenti nell'istruzione chiamante vengono abbinati ai parametri nell'intestazione della funzione
in base al loro ordine.
Ovvero:
- ==il primo argomento viene passato al primo parametro.==
- ==il secondo argomento viene passato al secondo parametro e così via.== 
#### Argomento passato per posizione
Quando chiami una funzione, Python deve abbinare ==ogni argomento della chiamata della funzione a un parametro nella definizione della funzione==.  
Il modo più semplice per farlo è basato sull'ordine degli argomenti forniti.
I valori che vengono matchati in questo modo sono chiamati argomenti posizionali (o passato per posizione).
```python
def describe_person(name:str, age:int, city:str):
print(f"my name is{name}, I'm {age} years old and I live in {city}.")

# Chiamata alla funzione con passaggio per posizione
describe_person("Alice", 25, "Rome")
>>>
>>>"my name is Alice, I'm 25 years old and I live in Rome" 
```
In questo esempio:
Ho tre parametri (`name`, `age`, `city`), che sono obbligatori e vengono passati **per posizione**.

- Il primo argomento passato è `"Alice"`, che corrisponde al parametro `name` (di tipo stringa).
- Il secondo argomento è `25`, che corrisponde al parametro `age` (di tipo intero).
- Il terzo argomento è `"Rome"`, che corrisponde al parametro `city` (di tipo stringa).
Se richiamassi la funzione ed invertissi i valori passati come argomenti nella chiamata della funzione,i valori verrebbero assegnati ai parametri in base alla loro posizione.

```python
def describe_person(name:str, age:int, city:str): 
	print(f"my name is{name}, I'm {age} years old and I live in {city}.") 
# Chiamata alla funzione con passaggio per posizione
describe_person("Rome", 25, "Alice" )
>>>
>>>"my name is Rome, I'm 25 years old and I live in Alice"
```
^describe-personCodeBlock

Questo perché negli argomenti passati per posizione, l'ordine degli argomenti deve seguire lo stesso ordine dei parametri che sono stati scritti. 

Difatti 
```python
def greet(name:str, age:int) -> None:
print("Hi, my name is" + name + " and I'm " + str(age) + " years old!")
greet("Angela", 13)
```
in questo caso è giusto, ma se si invertisse l'ordine degli argomenti; ad esempio scrivo prima l'intero `13` e poi la stringa `"Angela"` mi darebbe errore perché non posso concatenare un intero con delle stringhe in Python.

#### Argomento passato per keyword 
==Un argomento passato per keyword è una coppia nome-valore che viene passata a una funzione.==  
Associando direttamente il nome al valore all'interno dell'argomento, si evita ogni possibile ambiguità.
Questa tipologia è utile perché non c'è bisogno di ordinare correttamente gli argomenti nella chiamata della funzione e chiariscono il ruolo di ciascun valore all'interno della chiamata stessa. 
Per fare un esempio concreto, riprendiamo la funzione [[#^describe-personCodeBlock|`describe_person()`]]: 
```python
def describe_person(name:str, age:int, city:str) ->Any:

    greetings = f"Hello my name is {name}, I'm {age} years old and I live                 in {city}"
	 return greetings

  print(describe_person(age=25, city="Rome", name="Carlo"))
```

Posso invocare la funzione passando gli argomenti per keyword, ad esempio `age=25`, `city="Rome"` e `name="Carlo"`.  
Quando uso solo argomenti per keyword, **l'ordine non è importante:**
==perché ogni valore viene associato direttamente al parametro corrispondente in base al nome.==  
==Anche se nella chiamata della funzione gli argomenti vengono passati in un ordine diverso rispetto alla definizione, Python li abbina correttamente ai loro parametri.== 

Posso anche mischiare argomenti **posizionali e per keyword**, ma in questo caso ==**gli argomenti posizionali devono sempre venire prima di quelli per keyword**.==  
Non posso mettere un argomento posizionale dopo un **keyword argument**, perché Python non saprebbe più come abbinarli.
Per fare un ulteriore esempio:
```python 
def describe_person(name: str, age: int, city: str) -> str:
    greetings = f"Hello, my name is {name}, I'm {age} years old and I live in {city}."
    return greetings


# Solo keyword
print(describe_person(age=25, city="Rome", name="Carlo"))  

#Posizionale + keyword
print(describe_person("Alice", age=30, city="Milan"))

```
#### Argomenti passati per valori di default
Quando si scrive una funzione, è possibile definire un valore di default per ogni parametro.  
Se un argomento per un parametro viene fornito nella chiamata della funzione, Python utilizza il valore di quell'argomento.  
Se l'argomento non viene fornito, Python usa il valore di default definito per quel parametro.  
Pertanto, quando si definisce un valore di default per un parametro, è possibile escludere l'argomento corrispondente dalla chiamata della funzione.  
L'uso di valori di default semplifica la funzione e può aiutare a chiarire l'utilizzo tipico di essa.
**La sintassi è:**
```python
def function(par1, par2, par3=value3, par4=value4):
```
Prendendo come esempio questo blocco di codice, possiamo dire che:
- I primi due parametri sono obbligatori perché non hanno i valori di default.
  Quindi quando si chiama la funzione Python si apsetta che gli si fornisca un arogmento per ogni parametro obbligatorio (cioè per `par1`, `par2`).
- Gli ultimi due parametri (`par3` e `par4`) hano due valori di default. 
  Questo significa che puoi scegliere di fornire valori per questi parametri nella chiamata della funzione, ma **se non lo fai**, Python userà i valori di default definiti nella funzione.

> [!deep]- Perchè i primi due parametri sono obbligatori
> 1. **Posizione e ordine**: Python abbina gli argomenti alle variabili della funzione in base alla loro **posizione**. Gli argomenti devono essere passati nell'ordine in cui sono definiti nella funzione. Per esempio, se chiami la funzione come `function(1, 2)`, il primo argomento (1) viene assegnato a `par1` e il secondo (2) a `par2`. Se non fornisci questi argomenti, Python non sa cosa fare con `par1` e `par2`, quindi si verifica un errore.
>
>2. **Impossibilità di passare solo gli argomenti opzionali**: In Python, non puoi passare solo i parametri opzionali (quelli con valori di default) senza passare prima i parametri obbligatori. Quindi, devi sempre passare prima i parametri senza valore di default (posizionali) e poi puoi aggiungere quelli opzionali se lo desideri.

Ad esempio:
```python
def total(w, x, y=10, z=20):
return (w ** x) + y + z

# calling function total, while omitting the last two values
total(2, 3)
# Output: 38 -> calulated as 2^3 + 10 + 20

# calling function total, while omitting the last values
total(2, 3, 4)
# Output: 32 -> calculated as 2^3 + 4 + 20

# calling function total with 4 input values
total(2, 3, 4, 5)
# Output: 17 -> calculated as 2^3 + 4 + 5
```
In questo blocco di codice i primi due parametri (`w` e `x`) sono obbligatori, mentre i successivi due parametri (`y = 10` e `z = 20`) hanno dei valori di default. 
- Con il `return` mi ritorna in output la potenza tra i primi due parametri e l'addizione, del risultato della potenza tra `w` e `x`, con gli ultimi due parametri.
**Prima chiamata**
- invoco la funzione `total()` ed assegno dei valori passati come argomenti posizionali a primi due parametri:
  `w = 2` e `x = 3` 
  2^3 + 10 + 20 = 38
**Seconda chiamata:**
- chiamo la funzione `total()` ed assegno sempre ai primi due parametri due valori passati come argomenti posizionali:
  `w = 2` e `x = 3` 
- Nella chiamata cambio il valore della variabile `y` da `10` a `4`:
  `y = 4`
  2^3 + 4 + 20 = 32 
**Terza chiamata:**
- Nella chiamata cambio il valore della variabile `z` da `20` a `5`:
  `w = 2`,  `x = 3`,  `y = 4`, `z = 5`
  2^3 + 4 + 5 = 17.

Nella definizione di una funzione parliamo di parametri obbligatori (posizionali e keyword) e opzionali (default).

### Funzioni senza parametri
Ci sono funzioni senza paramentri in input:
```python
def hello():
print(‘‘Hello’’)
hello()
>>> Hello
```
Alcune funzioni, in Python, possono essere definite ed eseguite senza ricevere alcun valore di ingresso o parametro.
In Python, le funzioni non sempre richiedono argomenti per eseguire un'azione. Questi tipi di funzioni sono utili quando un'attività deve essere eseguito in modo standard, senza dipendere da input esterni.
Questi tipi di funzioni non hanno parametri di input, questo perché non devono dipendere da parametri in input ma sono funzioni che lavorano a livello generale.
Questo può essere utile quando devo lavorare con variabili globali, etc. 
Stessa cosa:
```python
def get_pi():
	return 3.14159

pi_value:float = get_pi()
print("The value of pi is:", pi_value)
>>> The value of pi is:3.14159
```


### Chiamare ed eseguire le funzioni
Per usare una funzione devo chiamarla o invocarla.
Quando un programma chiama una funzione, il controllo del programma viene trasferito alla funzione chiamata.
Una funzione chiamata restituisce il controllo al chiamante quando la sua istruzione di ritorno viene eseguita o la funzione è terminata.
Come viene eseguito questo programma?
L'interprete legge lo script nel file, riga per riga, a partire dalla riga 1.
Quando legge l'intestazione della funzione alla riga 1, memorizza la funzione con il suo corpo (righe 1-5).
corpo (righe 1-5) in memoria.
● Ricordate che la definizione di una funzione definisce la funzione, ma non ne determina l'esecuzione.

```python
def max(num1:int, num2:int)→int:
	if num1>num2:
		return num1
	else:
		return num2
#chiama la funzione max
numMax:int = max(3,4)
print(numMax)
```
Quando viene richiamata la funzione max , il valore 3 viene passato a num1 e il valore 4 a num2.
valore 4 viene passato a num2.
Il controllo viene trasferito alla funzione max e la funzione max viene eseguita.
viene eseguita.
Quando l'istruzione return della funzione max viene eseguita, la funzione max restituisce il controllo al chiamante.
restituisce il controllo al chiamante.
● Al termine della funzione max, il valore restituito dalla funzione max
viene assegnato a numMax (riga 8).
Il codice stampa il risultato (riga 9).
Prima della chiamata a max(3,4) , il controllo si trova nel programma
(nell'istruzione numMax = max(3,4) ).
Durante l'esecuzione della funzione, il controllo passa alla funzione max.
Quando la funzione max termina, il controllo torna al suo chiamante, che è l'istruzione numMax = max(3,4).
istruzione numMax = max(3,4).
In conclusione, il chiamante della funzione max è l'istruzione
numMax = max(3,4), che fa parte del programma


### Call Stacks
Ogni volta che una funzione è invocata, il sistema crea un record di attivazione che memorizza gli argomenti e le variabili per la funzione e colloca il record di attivazione in un'area di memoria nota come **Call Stack(stack di chiamate)**.
Quando una funzione chiama un'altra funzione, il record di attivazione del chiamante viene mantenuto intatto e viene creato un nuovo record di attivazione per la nuova chiamata di funzione.

Quando una funzione termina il suo lavoro e restituisce il controllo al chiamante, il suo record di attivazione viene rimosso dalla pila (stack) delle chiamate.
Una pila di chiamate memorizza i record di attivazione in modo che siano l'ultimo ad entrare e il primo ad uscire.
Il record di attivazione della funzione invocata per ultima viene rimosso per primo dallo stack.
Supponiamo che la funzione m1 chiami la funzione m2 e poi m3.
Il sistema di run-time inserisce nello stack il record di attivazione di m1, poi quello di m2 e infine quello di m3.
Dopo che m3 ha finito, il suo record di attivazione viene rimosso dalla pila.
Dopo che m2 ha finito, il suo record di attivazione viene rimosso dalla pila.
● Dopo che m1 ha terminato, il suo record di attivazione viene rimosso dalla pila.

Per quanto rigurada i parametri il primo paramentro ad entrare è il primo ad uscire

### Funzioni e `*args`
Io posso avere più argomenti in una lista.
```python
def add(a, b):
return a + b
print(add(2, 3))
```

se io scrivessi 
`print(add(2,3,4))`, mi torna errore perché l'ultimo argomento è mancante nella definizione della funzione `add`, se voglio aggiungere altri argoment i devo scrivere `*args`:
```python
def add(a, b):
return a + b
print(add(2, 3))

add(*args 1,2,4,5,10,56, "Hello")
```
Quindi quando richiamo la funzione e gli do `*args` posso passargli quanti parametri in input voglio(o per lo meno fino a che la RAM regge) di qualsiasi valore. 

Se faccio 
```
print(*myList)
```
Mi stampa gli elementi della lista senza le parentesi quadre 

### Funzioni e `**kwargs`
`*args` da una tupla di elementi
`**kwargs` passa i valori per chiave-valore. 
Quindi viene trattato come un dizionario infatti posso usare i metodi di un dizionario.
```python
def total_price(**kwargs):
	total:float = 0
	for product, price in kwargs.items():
		print(f"{product}: {price}€")
		total += price
	return round(total, 2)

print(total_price(coffee=2.99, cake=4.55, juice=2.99))
>>>
coffee: 2.99€
cake: 4.55€
juice: 2.99€
Total: 10.53€
```
Quindi è come se trattasi un dizionario.

### Built-in functions
come detto prima sono le funzioni di default date da python.
`print()`, `len()`, `max()`, `min()`, `sum()`, abs(), range(),etc. 


