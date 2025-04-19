
# Introduzione delle Ereditarietà delle classi in Python

# Introduzione
Abbiamo già affrontato il concetto di ereditarietà delle classi nella lezione [[Le Classi]] in Python e nella lezione [[Generalizzazioni]] in Progettazione. 
In questa lezione andremo a vedere come implementare l'ereditarietà della classi in Python.
**Cos'è l'ereditarietà?**
==È un meccanismo che permette a una classe figlia di **riutilizzare metodi e attributi** definiti in una classe padre, riducendo la ridondanza e favorendo la riusabilità del codice.==




### Sintassi
```python
class Baseclass:
	def method_base(self)->None:
		pass 
class Derivedclass(Baseclass):
	def method_defived(self)->None:
		pass
```

| Componenti   | Descrizione                                                    |
| ------------ | -------------------------------------------------------------- |
| BaseClass    | Il padre(superclasse) che definisce il comportamento condiviso |
| DerivedClass | Il figlio (sottoclasse) che eredita dalla BaseClass            |
| `:`          | Dichiara l'inizio della definizione della classe               |
| `()`         | Usata per specificare la classe padre che viene ereditata      |

### Esempio di ereditarietà
```run-python
class Animal:
	def speak(self) -> None:
		print("The animal makes a sound")

class Dog(Animal):
	def bark(self) -> None:
		print("Woof!")


fido:Dog = Dog()
fido.speak() # Output: "The animal makes a sound"
fido.bark() # Output: "Woof!"
```

Quindi `Fido` eredità sia il metodo `speak()` della classe `Animal`, ma viene anche chiamato il suo metodo `bark() `.
Tuttavia in queste esempio abbiamo chiamato i diversi metodi delle due classi separatamente mentre nella definizione della classe (`()`) abbiamo messo la classe `Animal`: questo significa che la classe `Dog` is-a `Animal`.
Però la classe `Dog` non eredita gli attributi e i metodi della classe base `Animal`. 

### Il metodo `super.__init()__` 
L'ereditarietà non si limita ai metodi, ma si estende anche agli **attributi** definiti nel costruttore `__init__` della superclasse.
Per richiamare correttamente il costruttore della classe padre, si utilizza `super().__init__()`: 
==questo metodo permette di invocare il costruttore della superclasse, così da inizializzare correttamente tutti gli attributi e i comportamenti definiti nella classe padre.==
Quindi questo metodo inizializza gli attributi della classe padre ed esegue il suo costruttore nella sottoclasse. 
In realtà il `super().__init__()` non è necessario per ereditare i metodi, poichè essi sono disponibili automaticamente in Python.
#### Spiegazione di come lavora il `super.__init__()`
`super()` restituisce un **oggetto temporaneo** che rappresenta la superclasse della classe corrente, ==quindi chiamando il `super.__init__()` si esegue il costruttore della superclasse permettendo di riutilizzare il codice già scritto senza doverlo copiare nella sottoclasse==. 
Questo è fondamentale soprattutto quando la superclasse contiene inizializzazioni(attributi, logica) che si vuole mantenere nella sottoclasse.



#### Esempio senza `super.__init__()`:

```run-python
# Without super()
class Animal:
	def __init__(self, name:str) -> None:
		self.name:str = name
		print("Animal initialized")
class Dog(Animal):
	def __init__(self, name:str) -> None:
		self.name:str = name
		print("Dog initialized")
fido:Dog = Dog("Rudy")
# Output: Dog initialized
```
In questo caso, la classe `Dog` **non richiama il costruttore** della classe `Animal`, quindi deve ridefinire esplicitamente gli stessi attributi.
#### Esempio con il `super__init()__`:

```run-python
# With super()
class Animal:
	def __init__(self, name:str) -> None:
		self.name:str = name
		print("Animal initialized")

class Dog(Animal):
	def __init__(self, name:str) -> None:
		super().__init__(name)
		print("Dog initialized")

fido:Dog = Dog("Rudy")
print(fido)
# Output: Animal initialized
# Dog initialized
```
In questo esempio:

- `super().__init__(name)` chiama il costruttore della superclasse `Animal` e inizializza `self.name`.
    
- Evitiamo la ripetizione del codice e manteniamo la gerarchia di ereditarietà.

> [!NOTE] Nota: `super()` è particolarmente utile in presenza di più livelli di ereditarietà e in scenari di ereditarietà multipla.

Si può avere metodi perosnalizzati, cosa succede se la classe padre ha attributi e metodi hanno gli stessi nomi e arogmenti della classe figlia? 
Avviene il metodo overridding:
occore quando una sottoclasse definisce un metodo con lo stesso nome e paramenri come un metodo della calsse padre.
I metodi e gli attributi della sottoclasse hanno la priorità più alta.
In questo esempio possiamo vedere questo metodo:
```run-python
class Animal:
	def speak(self) -> None:
		print("The animal makes a sound")


class Cat(Animal):
	def speak(self) -> None:
		print("Meow!")


kitty:Cat = Cat()
kitty.speak() # Output: "Meow!"
```
Quindi bisogna fare attenzione. 
Ogni sottoclasse eertedita della superclasse ttributi e meotdi, poi possono avere i propri attributi e metodi e ma possono anche sovrascrivere i metodi della classe padre

> [!attention] L'overide avviene solo ed esclusivamente con i metodi

Gli attributi possono essere protetti sono attributi anche privarti ma le sottoclasse possono accedervi, 
difatti un attributo protetto può essere visibile solo dalla classe di appartenenza o dalle sue sottoclassi.
Per definire se gli attributi sono protetti bisogna mettere un solo underscore (es: `_attribute` o `_method`).
La protezione in python  è solo una convenzione, mentre in altri linguaggi gli attributi sono realmente privati o protetti.
Esempio:
```run-python
class Animal:
	def __init__(self) -> None:
		self._type:str = "Mammal" # Protected attribute
	def _sound(self) -> None: # Protected method
		print("Generic animal sound")
class Dog(Animal):
	def describe(self) -> None:
		print(f"I am a {self._type}") # Accessing protected attribute
		self._sound() # Calling protected method
fido:Dog = Dog()
fido.describe() # Output: "I am a Mammal"
# Generic animal sound
```




```run-python
class Persona:
#Inizializza un oggetto della classe Persona
    def __init__(self,name,last,age):

        self.setName(name)

        self.setlastname(last)

        self.setage(age)

   def __str__(self):

        pass

        print(f"Nome: {self.name}\nCognome: {self.lastname} \nEtà: {self.age}")

    '''

    Mi consente di impostare un valore per self.name

    '''

    def set_name(self, name:str ) -> None:
	if:
        self.name = name
   else:
	   print("Errore")

    '''

    Mi consente di impostare un valore per self.lastname

    '''

    def set_lastname(self, lastname:str ) -> None:
	if:
        self.lastname = lastname
	else:
		print("Errore)
    '''

    Mi consente di impostare un valore per self.age

    '''

    def set_age(self, age:int ) -> None:

        if age <0 or age>130:

            self.age = 0

        else:

            self.age = age

    # Mi ritorna il valore di self.name

    def getName(self)->str:

        return self.name

    def getLastName(self) -> str:

        return self.lastname

    def getAge(self) -> int:

        return self.age

    

  

# Crea un oggetto di tipo Persona

m:Persona = Persona ("Marco", "Pierleoni", 27)

# Imposta i nomi di una Persona

m.set_name("Marco")

  

# Imposta i cognomi di una persona

m.set_lastname("Pierleoni")

  

# Imposta l'età di una persona

m.set_age(29)

# Stampa i dati della persona creata

m.display_data()

print("-----------")

print(m.getName(), m.getLastName(), m.getAge())
```

dobbiamo abituarci a scrivere gli attributi della classe. 
Il metodo `__init__` ci costruisce gli attributi della classe, prende in input name, lastname, `age:int`:
le altre volte abbiamo usato il modo canonico `self.nomeattributo = attributo`, in realtà sarebbe mehlio usare il metodo set nell'init, questo perché se l'utente mette un dato non valido il metodo set controlla la validità del dato e garantisce la validità e se il metodo set verrà richiamato nel codice i nostri dati saranno sempre valida. 
QUindi il metodo set prende sempre in input come argomento, essendo che se scrivessi il set fuori dall'`__init__` per controllare la validità del dato sarebbbe una ridondanza mentre se scrivo il set nell'`init` sto controllando ad esempio che `name` non sia una stringa vuota

Il metodo speciale str permette di visualizzare in output un oggetto della classe Persona, senza questo metodo mi printa l'oggetto della classe Persona la sua posizione in memoria il che no n mi serve, quindi tramite il metodo str mi permette di lavorare tramite il print, a differneza del metodo display_data lo devo ricihamare ogni volta.
Tramite il metodo set faccio un controllo che la stringa sia vuota, se non è vuota tramite il `self.name = name` sto dicendo che l'attributo name sia uguale a una stringa non vuota.
Stessa cosa per il metodo `setLastname`.
Il metodo setAge controlla che l'età sia un vlaore valido, cioè compreso tra 0 e 130 se è all'intenro di questo range mi ritorna il valore di age.
I metodi get peremtte di riotnare i vlaori degli attributi name, last e age, sono importnati perchè una Classe cosi definita a gli attributi pubblici ma di solito le informazioni all'intenro della classe vengono nascosti e quindi si usa il get per ritonare il valore di un attributo proprio perché noin si può accedere direttamente al valore di quell'attributo.

Definiamo una classe Persona dove abbimao definito, nome.cognome ed età e andiamo a definire una classe Studente e vogliamo che abbia le stresse identiche prorpietà di una Persona anche con gli stessi metodi, ma vogliamo anche aggiungere delle informazioni in più come ad esempio un attributo matricola e un metodo che calcoli la media dei voti degli esami sostenuti. 
ci sono due vie per fare cio:
riscirvere da capo tutti gli attributi e i metodi nel coaso devo scrivere tante cose c'è la via smart che è quella di sfruttare le ereditarietà: ereditò nella classe Studente tutti gli attributi e metodi della classe Persona. Questo mi peremette di scirvere il mio codice in maniera efficiente e veloce.
Quando si lavora con le classi bisofgna tenere le varie classi separate tra loro
Quindi nel file `studente.py` importo la classe `Persona`. 
Per dire a python che la classe Studente eredità persona scrivo così:
```python
from Persona_2 import Persona as P

class Studente(P):
```

l'overidding di un metodo significa: io posso ridefinire un metodo già presente nella classe padre che viene ridefinito nella classe figlia al fine che faccia cose diverse.


