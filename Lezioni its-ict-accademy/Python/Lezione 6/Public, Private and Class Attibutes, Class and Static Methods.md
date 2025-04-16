
# Introduzione
Un attirbuto è pubblioc quando è accessibile da chiunque nel codice e per defineirlo basta non inserire nessun undersocre prima del nome, tuttavia è pericoloso perchè sono accessibili da chiunque nel codice e soprattutto sono modificabili.
Esempio:
```run-python
class Animal:
	def __init__(self) -> None:
		self.name:str = "Generic Animal" # Public attribute

animal:Animal = Animal()
print(animal.name) # Output: "Generic Animal"
animal.name = "It's a dog" # MODIFIES the public attribute 'name'
print(animal.name) # Output: "It's a dog"
```
nel primo print è generic animal ma nel secondo caso si assegna un nuovo valore stringa all'attributo name ed è pericoloso.
### Rischio degli attributi pubblici
nessuna protezione
nessun controllo
può portare a bugs
un alternativa è usare attributi privati o accedere via getter e setter per mentenre il controllo.

### Attributi privati
Un attirbuto è privato quando è vompletamente nascoto quindi non è accessibile al di fuori della classe 
Per usare un attributo privato scrivere un doppio underscore, tuttavia quando un attrirbtup è privato è sicuramente nasconsto rispetto al protetto ma quando un attributo è privato rinomina l'attributo in `___ClassName__attribute`, quindi non è privato ma è nascosto nel codice.
Esempio con attributi privati:
```run-python
class Animal:
	def __init__(self) -> None:
		self.__name:str = "Generic Animal" # Private attribute

animal:Animal = Animal()
print(animal.name) # Error: not accessible directly
animal.name = "It's a dog" # Creates a NEW public attribute 'name'
print(animal.name) # Output: "It's a dog"
```

Come si può vedere infatti se si prova ad accedere all'attributo nel primo print mi da errore, e quando vado a modificare `animal.name = "It's a dog"` non sto modificando l'attributo name ma ne sto creando uno nuovo di tipo pubblico.
Ora avendo definito un attributo di tipo name ho bisofno di un metodo che possa accedere a quell'attributo(get/set).
Esempio:
```run-python
Class Animal:
	def __init__(self) -> None:
		self.__name:str = "Generic Animal" # Private attribute
# Makes 'name' accessible again
def get_name(self) -> str:
	return self.__name

animal:Animal = Animal()
print(animal.get_name()) # Output: "Generic Animal"
```
Quindi se l'utente chiama get_name legge il valore dell'attributo mentre per modificarlo avrei dovuto usare un setter.

> [!ticket] Quindi per gli attributi privati uso un getter per leggere il valore e un setter per modificarlo.


Di norma i getter e i setter vanno insieme 

### Gli attirbuti di classe e i metodi statici
il metodo statico: definisce con l'operatore chiocciola `@staticmethod`, possiamo usare quel metodo senza creare un'istanza della classe.
gli attributi di classe sono legati alla classe e non alla sua instanze quindi sono condivisi con tutte le istanze della classe ma non appartengono all'istanza stessa ma è legato alla classe.
Esempio attributi di classe:
```run-python
class Person:
	population:int = 0 # Public class attribute
	def __init__(self, name:str) -> None:
		self.__name:str = name # Private attribute
		Person.population += 1


print(Person.population) # Output: 0
person1:Person = Person("Alice")
print(Person.population, person1) # Output: 1
person2 = Person("Bob")
print(Person.population, person2) # Output: 2
```

In questo caso population è un attributo di classe e infatti viene condiviso con le istanze ma appartiene alla classe Person.
Dopodiche popolation incrementa di uno ogni volta che creo un'istanza della classe Person.

Esempio con metodi statici:
```run-python
class Math:
	PI:float = 3.14 # Public class attribute
	
	@staticmethod
	def circle_area(radius) -> float: # Static Method
		return Math.PI * radius * radius


print(Math.PI) # Output: 3.14
print(Math.circle_area(5)) # Output: 78.5
```
Qui manca il self perchè non è legato all'istanza, infatti nel primo print mi stmapa l'attributo di classe e nel secondo print mi stampa il risultato del calcolo dell'area di un cerchio.  

> [!ticket] io ho usato il metodo `circle_area` senza che ho creato l'istanza di `Math`

### Metodo di classe
un class method quindi è un metodo legato all'istanza ma alla classe e come paramtri di definizione prende `cls` e non `self`, perchè fa riferimento agli attributi di classe al fine di manipolarli.

Esempio:
```run-python
class Person:
	__population:int = 0 # Private class attribute
	def __init__(self, name:str) -> None:
		self.__name:str = name # Private attribute
		Person.__population += 1

@classmethod
def get_population(cls):
	return cls.__population

print(Person.get_population()) # Output: 0
person1 = Person("Alice")
print(Person.get_population()) # Output: 1
person2 = Person("Bob")
print(Person.get_population()) # Output: 2
```
