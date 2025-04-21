
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

In questo esempio, `fido` è un oggetto della classe `Dog`. Possiamo notare che:

- `fido` può **chiamare il metodo `speak()`** definito nella classe `Animal`, perché `Dog` **eredita** da `Animal`;
    
- `fido` può anche **chiamare `bark()`**, definito direttamente nella classe `Dog`.

Questo accade perché nella definizione della classe `Dog`, abbiamo scritto `class Dog(Animal)`, cioè stiamo dicendo che **`Dog` è una sottoclasse di `Animal`**.  
In altre parole, `Dog` **is-a** `Animal` (relazione di generalizzazione → [[Generalizzazioni#^is-aDef|is-a]]).

Il concetto di ereditarietà delle classi è rappresentato tramite il **sillogismo aristotelico**: 
==Il **sillogismo aristotelico** è una forma di **ragionamento deduttivo** composta da **due premesse** (una maggiore e una minore) e una **conclusione** che deriva logicamente da esse.==  
È uno strumento classico della logica formale, introdotto da **Aristotele**, per dedurre una verità a partire da affermazioni generali.  ^sillogismoAristotelico-Def
#### Struttura del sillogismo aristotelico
1. **Premessa maggiore**: affermazione generale.
2. **Premessa minore**: affermazione specifica.
3. **Conclusione**: deduzione logica. 

L'esempio canonico di questo sillogismo è: 
1. **Premessa maggiore**: Tutti gli uomini sono mortali
2. **Premessa minore**: Socrate è un uomo.
3. **Conclusione**: Quindi Socrate è un uomo

Nel nostro caso possiamo usare il sillogismo aristotelico per dedurre che:
1. **Tutti gli animali hanno il metodo `speak()`**
    
2. **Dog eredita da Animal**
    
3. **Quindi Dog eredita anche il metodo `speak()`**.


> [!NOTE]- Questo sillogismo può risultare debole, perché difatti lo è:
> Deriva da una capacità funzionale da una struttura, non è formalmente deduttivo.
> In altre parole Dog eredita anche il metodo `speak()` è una conseguenza comportamentale, vera nel codice, ma meno rigorosa in logica pura. 
> Questo perché:
> - Non tratta **categorie ontologiche** (come "uomo", "mortale", "filosofo" ecc.).
   > 
>- Ma descrive un **meccanismo tecnico di ereditarietà** (una regola del linguaggio di programmazione).
>  Quindi: 
>  ✅**È corretto nel contesto della OOP** (è "logico" all’interno delle regole della programmazione).
>- ❌ **non è logica deduttiva pura aristotelica**, perché non si basa su inclusioni di insiemi concettuali stabili, bensì su una "propagazione di comportamenti" data da un sistema formale (il linguaggio).
>Infatti questo tipo di ereditarietà non è una relazione `is-a` ma è **Ereditarietà comportamentale (`has-a method`):** 
>==relazione **pratica e funzionale** in cui una classe eredita metodi/attributi da un'altra per **riusare il comportamento**.== 
>Questo tipo di relazione è fondamentale nella OOP, ma differisce dalla relazione `is-a` in quanto non implica necessariamente una categorizzazione concettuale.
>> [!example] **Esempio:** 
>>`Dog` eredita `speak()` da `Animal`, ma non significa che la logica `is-a` sia sempre corretta.
>
>|Concetto|`is-a` (Relazione logica/strutturale)|Ereditarietà comportamentale (`has-a method`)|
|---|---|---|
| **Definizione**|Relazione concettuale tra due entità|Condivisione di metodi/attributi tramite ereditarietà|
| **Origine**|Logica formale, filosofia|Programmazione ad oggetti (OOP)|
| **Scopo**|Categorizzare, creare gerarchie logiche|Riutilizzare codice, condividere funzionalità|
| **Implementazione in OOP**|Tramite `class Sottoclasse(Superclasse)`|Tramite ereditarietà (stessa sintassi)|
|✅ **Quando è corretta**|Quando la sottoclasse **è un tipo** della superclasse|Quando la sottoclasse **ha bisogno dei metodi** della superclasse|
|⚠️ **Rischi**|Pochi, se usata con coerenza concettuale|Se usata solo per "riciclare codice", porta a design debole|
| **Esempio valido**|`Dog is-a Animal`|`Dog` eredita `speak()` da `Animal`|
|🚫 **Esempio scorretto**|`Button is-a Clickable` (non sempre vero logicamente)|`Button` eredita `onClick()` solo per riuso|


> [!ticket] Regola Chiave del sillogismo aristotelico 
> La **premessa minore** (in questo caso "il cane è un animale") deve sempre incastrarsi con la **premessa maggiore** (in questo caso "tutti gli animali fanno X"), per dedure la **conclusione logica corretta** ("che il cane fa X")


> [!deep] **La relazione "is-a" (`è un`) nel sillogismo aristotelico**
> Non esiste una regola specifica per dove può trovarsi la relazione [[Generalizzazioni#^is-aDef|`is-a`]] all'interno del sillogismo:
> può trovarsi sia nella premessa minore che nella conclusione, dipende dal tipo di sillogismo che si va a formulare.
> Nel esempio canonico:
> 1. **Tutti gli uomini sono mortali** (relazione "uomo → mortale").
> 2. **Socrate è un uomo**(relazione `is-a`).
> 3. **Quindi Socrate è mortale**
> Qui la relazione `is-a` (Socrate è un uomo) è nella premessa minore, la conclusione, invece, è in inferenza di proprietà ereditate ("Socrate è mortale").
>
>
>Anche nel esempio tra la classe `Dog` e la classe `Animal` la relazione `is-a` si trova comunque nella **premessa minore**, ma se si formulasse un diverso sillogismo tra queste due classi, ovvero:
>- Premessa maggiore: Tutti i cani sono animali 
>- Premessa minore: Fido è cane
>- Conclusione: Quindi Fido è un animale → `is-a`
> In questo caso è la conclusione ad esprimere la relazione `is-a`. 
> > [!example] **In sintesi**
> > | Dove si trova   | È coretto | Quando succede?                                               |
| --------------- | --------- | ------------------------------------------------------------- |
| Premessa minore | ✅         | Quando si descrive un caso particolare ("X è un Y")           |
| Conclusione     | ✅         | Quando deduci una gerarchia o appartenenza ("X è anche un Z") |
> > 
> > 
> > 




## Il metodo `super.__init()__` 
L'ereditarietà in Python non si limita ai **metodi**, ma si estende anche agli **attributi** definiti nel costruttore `__init__` della superclasse.  
Per inizializzare correttamente la superclasse all’interno di una sottoclasse, si utilizza il metodo `super().__init__()`:
==questo metodo permette di invocare il costruttore della superclasse, così da inizializzare correttamente tutti gli attributi e i comportamenti definiti nella classe padre.==
In altre parole, consente alla sottoclasse di **riutilizzare il costruttore della superclasse(`__init__`)** senza dover duplicare codice.  
Va notato che **i metodi della superclasse sono ereditati automaticamente**, ma il costruttore deve essere invocato esplicitamente.

### Spiegazione di come lavora il `super.__init__()`
`super()` restituisce un **oggetto temporaneo** che rappresenta la superclasse della classe corrente, ==quindi chiamando il `super.__init__()` si esegue il costruttore della superclasse permettendo di riutilizzare il codice già scritto senza doverlo copiare nella sottoclasse==. 
Questo approccio è fondamentale quando la superclasse contiene logica di inizializzazione che si vuole **mantenere e riutilizzare**.



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
In questo caso, la classe `Dog` **non richiama il costruttore** della classe `Animal`, quindi si deve ridefinire esplicitamente gli stessi attributi.
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
    
- Quindi si evita la ripetizione del codice e manteniamo la gerarchia di ereditarietà.

> [!NOTE] Nota: `super()` è particolarmente utile in presenza di più livelli di ereditarietà e in scenari di ereditarietà multipla.

### L'overriding dei metodi 
Cosa succede se nella classe padre e nella/e classe/i figlia/e si hanno metodi con lo stesso nome e parametri? 
Avviene l'overriding dei metodi:
l'overridding di un metodo si verifica quando una sottoclasse definisce un metodo con lo stesso nome e gli stessi parametri di un metodo presente nella sua superclasse. 
La versione che viene definita nella sottoclasse sostituisce quella eredita dalla classe padre.
Lo scopo di questo comportamento è quello di personalizzare o estendere il comportamento di un metodo ereditato dalla classe padre, e di realizzare il polimorfismo: stessa interfaccia, comportamenti diversi. 
Ovviamente, siccome con l'overriding si va a sovrascrivere tramite il metodo della classe figlia il metodo della classe padre, **il metodo della classe figlia ha la priorità su quello della classe padre.**
==Quindi quando si ridefinisce un metodo che esiste già nella superclasse, il metodo della sottoclasse prende il posto di quello originale.==
Detto in termini pratici: 
==quando si richiama quel metodo su una istanza della sottoclasse, verrà eseguita la versione della sottoclasse, non quella della superclasse.==

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


