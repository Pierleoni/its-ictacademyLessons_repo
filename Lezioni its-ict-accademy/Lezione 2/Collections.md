## Altri tipi [[I modificatori#Modificare i dati|dati]] 
In [[Introduzione a Python#Variabili|Python]], sono delle strutture dei dati più complesse delle variabili, nelle variabili fino ad adesso abbiamo salvato solo un tipo di dati contenuti e per salvare due valori interi devo scrivere 2 variabili per salvare due valori.
Nelle collection possiamo salvare più valori nella stessa struttura.
Se noi vogliamo tenere traccia di tutti i valori assegnati, devo usare la collection: 
le collection ci permettono di memorizzare tanti tipi di dati nella stessa struttura.

## Le liste 
Sono una sequenza ordinata di elementi di valori, questi valori possono essere tutti dello stesso tipo o di tipo diversi, tutti i valori che si trovano nella lista si chiamano elementi della lista.
```python
list1=[1,2,3,4,5]
list2=[A,B;C]
```
Nei primi due casi abbiamo due liste che contengono tutti elementi dello stesso tipo mentre nel terzo sono elementi di tipo diversi tra loro. 
Può capitare che all'interno della lista l'elemento è una lista anch'esso
```python
list4=[[2,3,4], 5,6] 
```
In questo caso si dice nested list(liste annidate): 
gli elementi `[2,3,4]` è una lista dentro la list4.
Per stampare gli elementi di una lista 
```python
#display all list
list1=[1,2,3,4]
print(list1)
```
Se vogli stampare gli elementi ella lista senza parentesi scriverò
```python
print(*list1)
```
Se voglio separare gli elementi della lista tra loro con un carattere preciso:
```python
print="*list1, sep=*,/,|, etc.
```

La cosa importante è sequenza ordinata di elementi: io posso accedere agli elementi o singolo elemento attraverso delgi indici, una struttura non ordianta non me lo fa fare.
```python
indexing
mylist= ["Alice", Bob, "Charlie"]
```
IO ho una lista con N elementi, in questo caso le posizioni, come per le stringhe, la lista è indicizzata zero-based (parte da zero):
Alice è posizione 0
Bob posizione 1

In anlogia con le stringhe noi possiamo accedere a un detemrianto elemento della lista.
Es:
```python
print=(mylist[0])
>>> "Alice"
```
Io sto chiendendo l'elemento alla posizione 0 della mia lista.
Le liste possono sia avere indici positivi che negativi, perché noi possiamo leggere le liste in 2 modi diversi:
1. Leggere la lista da sx verso dx (classico), quidni il primo elemento in posizione 0 e cosi via
2. La stessa lista posso leggerla da dx verso sx e quidni il primo valore diventa l'ultimo e l'ultimo valore diventa il primo.
   Utilizzeremo quindi indici negativi
```python
   mylist=["Alice", "Bob", "Charlie"]
   index=    0        1       2     
   reverse
   index=     -3       -2      -1
```


> [!tip] L'operatore `in`
> Per individuare un determinato elemento in una lista usare l'operatore `in`.
>```
>```


```python
print(mylist[-1])
>>> Charlie
```

Es:
```python
myList=["Andrea", "Benedetta", "Camilla",]
print(myList)
myList[2]="Carlo"
print(myList)
```

In questo caso gli ho detto di sostiuire "Camilla" con "Carlo"

Posso farlo anche cosi: 
```python
myList=["Andrea", "Benedetta", "Camilla",]
print(myList)
myList[-1]="Carolina"
print(myList)
```

Come prima l'output verrà visalizzato come 
```python
Andre, Benedetta, Carolina
```

Posso accedere ai miei elementi solo tramite indice.
La lista può essere modificata con elementi nuovi o sostituirli 
In una lista posso avere elementi duplicati:
```python
[2, 5, 2]
["x", "x", 3]
```
Utile nel caso in cui in una lista mi tornano elementi con lo stesso valore

Funzione `.append(element)`:
Supponiamo di volere aggiungere l'elemento `Davide`
```python
myList.append("Davide")
```
Quindi la funzione `.append` aggiunge un elemento a una lista.
Se ad esempio voglio aggiungere `Erald` alla lista:
```python
myList.append("Erald")
print(myList)
```
L'elemento aggiunto sarà sempre l'ultimo della lista 

Funzione `.insert`:
vuole due valori in input:
1. l'indice
2. l'elemento che si vuole inserie a quell'indice specificato.

Es:
```python
myList.insert(1, Andrea_2.0)
print(myList)
>>>[Andrea, Andrea_2.0, ...]
```
In questo caso aggiungo all'indice 1 `Andrea_2.0`. 

### Come rimuovere gli elementi di una lista 
Voglio rimuovere `Andrea_2.0` quindi farò `.remove()`:
toglie l'input che si vuole rimuovere.
Es:
```python
myList.remove("Andrea_2.0")
print(myList)
```

Se voglio rimuovere un elemento inserendo l'indice devo usare `.pop()`:
rimuove l'elemento in una detemrianta posizione, basta dargli come input un determianto indice (sia negativo che positivo).
```python
myList.pop(3)
print(myList)
```

La funzione `Extend`:
Ci sonsente di estendere la lista con più valori insieme
```python
myList = ["Al"]
```

Funzione `.del`:
serve per eliminare la lista, la memoria del mio computer che era stata usata per salvare la lista viene liberata e la lista all'interno del codice non esisterà mai più

Modo di scorrere delle liste 
Dove si scrive gli indici per accedere agli elementi si scrive invece `print(myList[0:2])`
il primo indice è quello di partenza
l'ultimo è quello di arrivo 
Quindi significa che parto dal primo elemento al secondo mi stamperà solo l'indice 0 e l'indice 1.
Se cambia la posizione del nostro indice
```python
print (myList[1:1]) # viene visualizzato dall'indice 1 tutti gli elementi della lista 

print(myList[:1]) #viene visualizzata solo l'elemento 

```
Lo si puo fare con gli indici negativi:
```python
print(myList[-2:]) #viene visualizzato gli ultimi due eleemnti della lista
```

![[Recording 20241217135846.webm]]