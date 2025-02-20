## I valori [[Gli Operatori#^boolean-operator|booleani]] in Python

In questo caso `true` è equivalente al numero intero `1` in operazioni aritmetiche, mentre `false` è equivalente al numero intero `0`. 
```python
 print(True+1)
2
```
Di fatto se inserisco questa operazione in [[Introduzione a Python|Python]] mi restituisce `2` perché `true` equivale al numero intero `1`, quindi $$ 1+1 = 2$$
### L'operatore [[Le architetture di un Computer#L'algebra Booleana|AND]] 
Analogamente se uso l'operatore [[Le architetture di un Computer#^andOp-Def|`and`]]:
come sappiamo questo operatore valuta l'espressioni da sinistra verso destra e restituisce il primo valore **falso** trovato, ==perché restituisce vero se entrambi gli operandi sono veri==. Infatti se non trova valori falsi, restituisce l'ultimo valore, questo comportamento è noto come **short-circuit evaluation.** 
```python
print(True and 1)
1

 print (True and 0)
0
 type (True and 0)
<class 'int'>
```
 1. Nel primo esempio: 
 - `True` è valutato, è "vero", quindi l'operazione continua 
 - `1` è valutato ed è "vero" 
 
> [!danger] !!!in Python, qualsiasi numero diverso da 0 è "vero"!!! ^0IsFalse

Quindi siccome entrambi gli operandi sono veri e non ci sono valori falsi, `and` restituisce l'ultimo valore : cioè `1` 

1. Nel secondo esempio:
   - `True` è valutato, è "vero "
   - `0` è valutato ed è "falso"
Quindi l'operatore `and` restituisce il primo valore falso: `0`.  ^sec-ex

1. Per quanto riguarda il terzo esempio: 
   Qui fa la stessa cosa del [[#^sec-ex|secondo esempio]] ma questa operazione è messa come argomento della [[Introduzione a Python#^typeFun-def|funzione type]], quindi dopo che l'espressione è stata valutata e ha restituito `0`, Python determina il tipo dell'oggetto tramite questa funzione:
   - Siccome `0` in Python è un oggetto del tipo `int`, restituisce `<class 'int'>` 

> [!faq] Perché `0` è di tipo `int`? 
> In Python i valori booleani `True` e `False` sono implementati come sottoclassi di `int`:
> quindi, `True` equivale a `1` e `False` equivale a `0` quando vengono usati in contesti numerici ([[#^0IsFalse|Saint Thomas' Law]]).  
> Nel caso di `True and 0`, il risultato è semplicemente il valore `0`, che non viene "convertito" in `bool`, perché `and` restituisce direttamente uno dei suoi operandi senza modificarne il tipo.

Quindi se scrivo questa operazione logica perché mi ritorna 5?
```python
 print (6 and 5)
5
```
Come detto poco sopra: siccome sia `6` che `5` sono valutati e considerati entrambi "vero", `and` restituisce l'ultimo valore : cioè `5` perché non ci sono valori falsi 

### L'operatore [[Le architetture di un Computer#^orOp-Def|OR]] 
L'operatore `or` in Python:
==Restituisce il **primo valore** truthy ("vero") che trova, oppure l'ultimo valore se tutti sono falsy ("falsi").==  ^orOp-Py
La valutazione viene fatta da sinistra verso destra. ^de8a18
```python
print(5 or 6)
5
```
In questo esempio: 
1. la valutazione parte dal primo operando (`5`) che è valutato ed è vero
2. La valutazione passa all'operatore `or` che restituirà il primo valore che è "vero" (truthy).
3. Quindi essendo già il primo operando (cioè `5`) "vero", Python lo restituisce senza neanche valutare il secondo (cioè `6`).
In questo caso: 
```python
print (0 or 6)
6
```
Questo perché?
![[#^0IsFalse]]
Quindi essendo `0` falso l'operatore `or` restituisce il secondo ed ultimo valore: cioè `6`. 
Che succede se entrambi gli operandi sono falsy?
```python
print(0 or False)
False

print(False or 0)
0
```
In entrambi i casi restituisce l'ultimo valore valutato (quindi rispettivamente `False` e `0`) poiché entrambi gli operandi sono falsi 
### L'operatore [[Le architetture di un Computer#^notOp-Def|NOT]]  
In Python se uso l'operatore `not`: 
questi ==inverte il valore booleano di un'espressione==.  ^notOp-Py

Quindi in questo caso: 
```python
print (not 6)
False 
```
Bisogna ricordare che in Python, qualsiasi numero diverso da `0` è truthy ("vero"), quindi `0` è l'unico valore falsy ("falso").  
Quindi l'operatore `not`, inverte il valore booleano: 
- ==Se il valore è "vero", `not` lo trasforma in "falso".== 
- ==Se il valore è "falso", `not` lo trasforma in "vero".== 
Quindi `not 6` (che ricordiamo essendo per definizione `6` è diverso da `0`, quindi è "True") inverte il valore truthy di `6` e restituisce `False`.   

## [[Collections#^ListsDef|Liste]] e il controllo della [[Cicli e condizionali#Conditional Statements|Condizione]] 
In Python, ==una lista è considerata come truthy se non è vuota==, cioè: 
```python
l = ["a", 5, "?", True]

if l: 
	print ("ciao")


if len(l) >0: 
	print("ciao")

l=['a', 5, '?', True]
```
Come possiamo vedere da questo caso;
- `if l:`
  valuta se la lista contiene almeno un elemento. 
  In questo caso `l` contiene almeno 4 elementi, di conseguenza l'espressione è vera e stampa `"ciao"`.
- `if len(l) >0:`
  Verifica esplicitamente che la lunghezza della lista sia maggiore di `0`. 
  Anche in questo caso la condizione è vera.
Nel caso contrario se la lista `l` fosse stata vuota sarebbe stata valuta come falsy (falsa) quindi non avrebbe stampato la stringa `"ciao"`. 
Per rendere più chiaro questo esempio: 
```python
l = []  # Lista vuota

if l:
    print("ciao")
else:
    print("lista vuota")

```
==Questo accade perché una lista vuota in Python è considerata _falsy_, mentre una lista con uno o più elementi è _truthy_.==  ^truthy-falsyListCond


> [!NOTE] Per controllare se una lista contiene elementi si fa:
> 
>```python
> l = ["a", 5, "?", True]  # Esempio di lista con elementi
>
>if l:  # Controlla se la lista non è vuota
 >   print(1)
>else:
 >   print("La lista è vuota")
>```
>In questo caso Python controlla se la lista contiene elementi e se ciò è truthy allora stampa `1` mentre se è falsy stampa `La lista è vuota`

### Uso delle liste come condizioni

Cosa fa questo? 
```python
l = ["a", 5, "?", True]
if [False]:
	print(1) 
```
[[#^truthy-falsyListCond|Quindi come detto in precedenza ]], `1` viene stampato poiché 
Stampa 1 perché uso una lista come condizione e siccome la lista ha almeno un elemento al suo interno stampa l'argomento del print.

```
if len ([False, False, False]):
	print(1)
```
Stampa uno perché ci sono almeno tre elementi nella lista ?


```
if [[]]:
	print("ciao!")
```
stampa comunque la stringa perché 


```
>>>len([[]])
1
```

```
for x in [[]]:
	print (x)
[[]]
```

```
if len([[]]) > 0
	print (1)
1
```

```
l[:]
["a", 5, "?", True]
```
Modo corretto per copiare una lista in [[Introduzione a Python|Python]]. 
Se io volessi creare 
```
l1= l[:]
```


> [!faq] Funzione `.pop()` nelle liste 
> Contents

Cosa fa questo?
```python
if [[]][0]:
	print("ciao")
```
la seconda parentesi quadra indica l'indice del primo elemento della lista interna quindi la lista vuota e quindi non stampa nulla perchè accede al primo elemento della lista ma non c'è nessun elemento dentro la lista e quindi non c'è contenuto, Di conseguenza l'output sarà: 
```
[]
```

Ciò torna utile quando mi creo delle sotto-liste o liste vuote a cui posso [[Spiegazione esercizi Lezione 1 Python#La funzione `append`|appendere]] elementi all'interno della lista. 

Per quanto riguarda le tuple invece:
```
t = (5, 'a', False)
if t: 
	print(1)

```

Per far diventare una lista in una tupla 
```
l = [1,2,3]
tuple(l)
```


Le funzioni dei set
.add
.intersection
.difference 
.difference_update
.discard: Rimuove un elemento se è un numero altrimenti non fa nulla (è un remove sicuro)
.isdisjoint
.issubset




