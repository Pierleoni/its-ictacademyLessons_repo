# Introduzione

**==Lambda è una piccola funzione utile quando vogliamo definire una funzione in maniera veloce e semplice, ed è spesso usata come argomento di altri funzioni.==** 

## Sintassi
La sintassi di lambda è la seguente:
```
lambda argumets: expression
```
Quindi keyword lambda l'argomento e dopo i due punti l'espressione che andiamo a definire.
### Come lavora lambda
Una lambda può avere un **qualsiasi numero di argomenti**, ma ha **==una sola espressione che ritorna in modo automatico==**. 


Come facciamo a tipizzare gli argoemnti e il valore di ritorno di la lambda?
Per poterla tipizzare scriviamo
```
from typing import Callable
Callable [[ArgType, ArgType2,...],ReturnType]

```
Quindi nelle parentesi quadre nestante mettiamo i tipi di arogoemtno e fuori torniamo il tipo di ritorno degli arogoemnti
```
from typing import Callable
multiply:Callalbe [[int,int], int] = lambda a,b: a*b
```
Per esempio:
```run-python
from typing import Callable
square:Callable[[int],int] = lambda x:x**2
print(square(5)) #Output 25
#La controparte come funzione normale
def square (x:int):
	return x**2
```
Lambda è utile quando un operazione la devo usare poco volte e quindi in una sola riga uso lambda

Un altro esempio:
Un altra lambda per moltiplicare due variabili:
```
from typing import Callable
multiply:Callable[[float,float],float] = lambda a,b: a*b
print(multiply(3,4)) #Output 12
```

Esempio con if 
```
from typing import Callable
positive_or_negative:Callable[[int],int] = lambda x : "Positivo" if x >0 else \ "Zero o Negativo"
print(positive_or_negative(5))
print(positive_or_negative(-3))
#Controparte 
def positive_or_negative(x:int) ->str:
	if x > 0:
		return "Positivo"
	else: 
		return "Negativo"
```

Fin qui abbiamo definito lambda come funzione da utilizzare nel codice, ma lambda viene usato anche come argomento di funzione di altri funzioni, come ad esmepio:
Filter: 
```run-python
num:list[int] = [1,2,3,4,5,6]
even:list[int] = list(filter(lambda x:x%2==0, num))
print(even)
```

Qui volgio prendere tramite la funzione filter(che torna uno oggetto di tipo filter), volgio filtrare la prima lista per ritornare una lista di numeri interi pari. 
Qui lambda dice se per x di x se si verifica x è pari, quindi filter applica questa logica sulla lista nums e se questa logica è vera mette gli elementi pari nella lista evens. In questo modo in unica riga ho filtrato una lista.
Qui non abbiamo importato il Callable perché non sto creando la almbda ma la sto mettendo come argoemtno di una funzione.
Sorted:
```run-python
names:list[str] = ["Alice", "bob", "Charlie"]
sorted_by_lenght:list[str] =sorted(names, key=lambda name:len(name))
print(sorted_by_lenght)
```

Per ordinare in base alla lunghezza dei nomi, nel caso di `sorted` prevede che come argomento n 1 è la lista su cui deve agire. 
Il key=lambda mi permette di agire su come agisce `sorted()`, quindi lambda name:len(name). QUindi in questa funzione lambda prendo la variabile name e deve ritornami la lunghezza delle strignhe di questa varibile poiché name sono gli elementi di names.
Questa lambda e come se facessimo:
```
def ... ->int
	for name in names:
		return [name]
```
Se la volessimo al contrario:
```run-python
names:list[str] = ["Alice", "bob", "Charlie"]
sorted_by_lenght:list[str] =sorted(names, key=lambda name:len(name), reverse=True)
print(sorted_by_lenght)
```

QUando usare e non usare labmda?
Quando si necessita di una funzione per un breve periodo di tempo, quimdi una funzione che devo usare poche volte.
QUando non si vuole definere una funzione nella sua interezza

Non si usa quando la funzione è complessa e la logica deve essere strutturata su più linee, quando deve essere riusata più volte e quando compromette la laegibilità. 

Lamda e RTegEx insieme:
```
import re
words:list[str] = ["abc123","456", "43", "hello", "98abc", "test999"]
only_digits = list(filter(lambda x: re.fullmatch(r"\d+",x),words))
print(only_digits)
```

Fullmatch: controlla che il match rispetti esattamente il pattern
lambda definisce la condizione inline
filter(): applica lambda a tutte le strighe nella lista.

Esempio:
```run-python
import re
text:str = "Price: 100 dollars, Tax:20 dollars"
new_text:str = re.sub(r"\d+",lambda m: str(int(m.group())*2),text)
print(new_text)
```
m.group è il match: quindi 100 perchè trova la corrsipondenza e la inser