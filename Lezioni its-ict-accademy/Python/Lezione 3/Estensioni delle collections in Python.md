# Le collections
Come abbiamo visto nella lezione delle [[Collections|collections]], ci sono vari metodi per le 
## Estensioni dei set
La funzione `.update()` ci consente di aggiornare gli elementi di una collection. 
`set.update(iterable):` aggiunge tutti gli elementi da un iterazione specifica (Es: liste, tuple, set o dizionari)
C'è un differenza tra `.update()` e `.union()`:
- `.update` va a sovrascrivere il valore di un set 
```python
first_set = {1,5,7,8}
second_set = {2,3,7,6}
first_set.update(second_set)

```

- `union` invece crea un nuovo set che ha tutti gli elementi del primo set + tutti gli elementi del secondo set ma il primo set rimane invariato

Siccome non posso accedere manualmente agli elementi del set o a un indice specifico, l'unico modo per accedervi è quello di ciclare il set: 
quindi farlo tramite il ciclo `for`, immaginiamo di avere un set:
```python
myset = {5,4,8,10}
for value in myset:
	print(value)
```

> [!info] Da notare che i set sono collezioni non ordinate ogni volta l'ordine degli elementi in output può variare 

Immaginiamo di avere un altro set:
```python
myset={1, "Hello", 3, 0.5, True, False, 2}
#se vado a fare il print del set
print(myset)


```
Anche se gli elementi del set fanno parte di una collezione non ordinata a noi può sembrare che gli elementi in output siano state ordinate, questo perché python utilizza le cosiddette funzione hash table: sono strutture dati che servono a memorizzare i dati e accedervi velocemente quindi come il singolo elemento del set viene salvato in memoria
Per questo motivo dobbiamo stare attenti quando su un set abbiamo valori in float, int e bool:
Questo perché in python i valori booleani vengo intrapresi come 0(false) e 1 (True), quindi in questo caso python lo interpreta come integer, quindi uno di questi due valori vengono fatti fuori proprio perché grazie alle funzioni di hash vengono memorizzati oppure no, difatti nell'output non avrò il valore `True` perché all'interno del set è presente il valore integer `1` ed è quello che è stato letto e salvato prima di conseguenza il valore `True` viene considerato come duplicato del valore `1`. 
In questo caso abbiamo la stringa "Hello" ed essendo un valore diverso che non ha duplicati viene salvato esattamente come 0.5, 2, 3. 
Quindi se tolgo 1 l'output mi stampa il valore `True`
```
myset = {0.5, True, False, 2,3, "Hello"}
print(myset)
```
Stessa cosa se tolgo `True` mi verrà stampato il valore `1`.

### Come leggere i valori nei dizionari

Se io per esempio voglio 
```python
mydict = ["key1": "value1", "key2":"value2"]
for key in mydict:
	print(key)
```
In questo caso stampo le sole chiavi del dizionario

```python
mydict = ["key1": "value1", "key2":"value2"]
for key in mydict:
	print(key)
```
In questo caso stampa l'elemento associato a quella chiave.

```python
mydict = ["key1": "value1", "key2":"value2"]
for key, values in mydict.items():
	print(f"Chiave:{keys}, valore:{values})
	
```
La funzione `.items` ci ritorna una lista di tuple e all'interno delle tuple vengono salvate delle chiavi del dizionario e il valore a essa associata.
Se io elimino elementi i valori nel mio dizionario mi toglie la tupla corrispondente viceversa se aggiungo elementi

`dictionary.values()`: Ritorna una visualizzazione dei valori del dizionario. Questa visualizzazione è dinamica e riflette i cambiamenti del dizionario, permette una maggiore iterazione più efficiente oltre le chiavi. 
```python
mydict = ["key1":5, "key2":3]
for key in mydict.keys():
	print(key)
```
Quindi ti torna una lista di chiavi in output. 

### Estensione delle liste 
list.extend(): aggiunge più elementi all'interno della lista contemporaneamente rispetto all'`.insert` o `.append`,
questa funzione vuole come argomento vuole un oggetto che sia iterabile, esattamente come la funzione `.update`. Ciò significa che un oggetto iterabile è un oggetto a cui posso accedere elemento per elemento tramite indici o chiavi o posso eseguire operazioni di iterazioni su di esse. 
Io posso estendere la lista con altri elementi di altri collections. 
Ci sono 2 modi diversi per estendere la lista:
1. Primo metodo:
```
firstlst = [1,5,7,8]
secondolst = [2,3,7,6]
firstlst.extend(secondolst)
```

2. Secondo modo 
```
thirdlst = firstlst + secondolst 
```
 Nel primo caso la prima lista non cambia, mentre qui si. 

Nel caso dell'`extend`: 
```python
firstlist = [1,2,3,4,5]
firstlst.extend((8,7,6))
firstlst.extend ({8,7,6}) #In questo caso sto aggiungendo elementi della tupla alla lista e vengono aggiunti in fondo alla lista come la funzione append
```

Io posso anche estendere una lista con un dizionario
```python
firstlst = [1,2,3,4,5]
firstlst.extend({"key": "value", "Bool": True})
print(firstlst)
```

In questo caso mi aggiungerà le chiavi del dizionario perché io nel caso dei dizionari itero sulle chiavi e non sull'elemento, esattamente come nel caso del `for key in mydict` io accedo alle chiavi del dizionario e non direttamente ai valori. 
Se io volessi aggiungere con i solo valori del dizionario `.values`: mi restituisce una lista di elementi che ha i singolo valori del dizionario. 

Esempio pratico
```python
firstlst = [1,2,3,4,5]
firstlst.extend({"key": "value", "Bool": True}.items())
print(firstlst) #In questo caso mi aggiunge anche le chiavi dei valori associati
```
