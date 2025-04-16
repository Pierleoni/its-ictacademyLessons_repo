 Un 'asserzione in [[Introduzione a Python|Python]] è considerato un **sanity check**: ==cioè verifica se il nostro codice è sano e non ci siano problemi.== 
 Viene utilizzato a scopo di debugging e vengono inseriti in punti strategici del codice per verificare se la condizione è vera a un punto specifico del codice.
 Se la condizione non è vera, Python solleva un errore di `AssertionError`. 
 Sintassi:
```python
 assert condition, "Optional error message"
```

esempio
```run-python
x = 5
assert x>0, "x must be positive"
```


La differenza tra `assert` è `if` è che:
- ==`assert` viene usato per scopi di debugging== 
- ==l'`if` si usano per modellare il comportamento del codice.== 
Lo scopo delle asserzioni è che siano vere durante l'esecuzioni, non permettono l'interattività e quindi non permettono di gestire l'input dell'utente.

### Ottimizzare il parametro (-O)
Quando si scrive un codice molto grande si inizieranno ad avere molti `assert`, per evitare che questi `assert` vengono valutati ogni volta durante l'esecuzione posso avviare il programma scrivendo
```python
python -O script.py
```
Le asserzioni, in questo modo, vengono ignorate, se levo `-O` le asserzioni non vengono ignorate e vengono rivalutate e rieseguite ogni volta che il programma viene eseguito.