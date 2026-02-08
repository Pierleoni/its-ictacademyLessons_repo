### I [[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#**Utilizzo dei Decoratori** `@property` **per Getter e Setter**|decorators]] in Flask
Le funzioni sono **first class objects:** 
- ==una funzione può essere passata come parametro di un altra funzione, non il valore di ritorno della funzione ma la funzione stessa.==
Quindi si può scrivere una cosa del genere: 
```python
def fun1()->str:
	return "Hello"
	
def fun2(fun):
	fun()

fun2(fun1) #Da notare che passo la funzione stessa senza parentesi quello che viene indicato è la zona di memoria dove fun1 si trova
```

L'inteprepte py quando legge le funzioni prima di eseguirle va a leggere lo spazio in memoria dove sono salvate.
In questo caso sto passando il riferimento di memoria, se eseguo fun2 questa funzione richiama qualsiasi funzione gli sto passando in questo caso `fun()`. 
Quindi quando eseguo fun2 questa esegue la funzuone fun che altro non è che la funzione fun1 nell'invocazione di fun2.
In altre parole: 
```python
def ciao()
	return "Hello"

def fun2(fun):
	fun()

fun2(ciao)
```


I decorators fanno qualcosa di simile: è una funzione che prende in input un altra funzione, quella che vogliamo decorare, viene decorato dal decoratore, in questo caso fun2 sarebbe il decoratore mentre ciao è la funzione che ogliamo decorare.

Inner function e outer function
Una funzione può prendere in ingresso un altra funzione ma può anche ritornarla: 
fun2 può prendere in ingresso ciao() ma può anche ritornare ciao().



Differenza tra funzioni estrene ed interne:
Le funzioni possono contenere quello che volgiamo:
```python
def parent():
	print("Printing from parent()")
	
	def first_child():
		print("Printing from first child")
	def second_child():
		print("Printing from second child")
	second_child()
	first_child()
```

QUanda la funzione parent è stata eseguita tutta se non trovo il modo di tirare fuori le funzioni interne non possono essere usate globalmente.
I deocrators vanno ad espandere le funzionalità delle funzioni, l'esempio è il cronometro, usando un decoratrs sulla funzione del cronometro posso, ad esempio vedere il tempo di runnig della inner function cronometro().

Andiamo a vedere come fare un decorator cronometro: 
```python
import time
def cronometro(fun): #è il decorators (@cronometro)
	def wrapper() #avvolge la funzione che si vuole decorare
		start = time.time()
		fun()
		print(time.time()-start)
	return wrapper #non l'ho ritorno con le parentesi ma ritorno il riferimento perché non volgio passare la funzione ma il suo indirizzo di memoria 
```

Una volta definito l'heaer ho bisogno di una inner function.
Ora: 
voglio sapere quanto ci mette questa funzione a runnare, uso quindi il decorator cronometro
```python
@cronometro
def ciao():
	print("hello")
```

Un modo per applicare il decoratore è cosi, quando scrivo la chiocciola sto facendo : 
```python
ciao = cronometro(ciao)
```
QUindi quando assegno ciao al cronometro eseguo wrapper e i riferimeti di ciao si trovano nel corpo di wrapper (`fun()`) quindi la funzione ciao contiene il wrapper del cronometro. 
Quindi se eseguo ciao() sto ritornando la funzione wrapper (), la differenza è che nella funzione wrapper fun() ha come valore ciao().
Questo
```python
ciao = cronometro(ciao)
```

viene definito da
```python
@cronometro
```

È solo sintassi, detto anche zucchero sintattico; se scriviamo `ciao = cronometro(ciao)` è la stessa cosa di `@cronometro`. 

Quindi il decoratore è una funzione che prende in input una funzione e restiruisce la funzione decorata.
Metto `*args` nel decorator perchè devo poter passar qualsiasi arogmento nel wrapper e in fun().
```python
import time

def cronometro(fun):

    def wrapper(*args):

        start = time.time()

        fun(*args)

        print(time.time()- start)

    return wrapper

@cronometro

def ciao():

    print("Hello")

# ciao = cronometro(ciao)

# @cronometro

ciao()
```


Questo è un disegn pattern per risparmiare codice.

