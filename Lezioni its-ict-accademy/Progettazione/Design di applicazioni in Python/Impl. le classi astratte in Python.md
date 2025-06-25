Per impl una classe astratte dobbiamo scrivere:
```python
from abc import ABC
```

Se scriviamo 
```python
from abc import ABC
class Persona(ABC):
	def __init__(self,nome):
		self.nome = nome
	def saluta(self,nome):
		print(f"Ciao {nome}")

mario:Persona = Persona()
mario.saluta("Alice")
```

QUesta cosa funzionerebbe perchè stiamo dicendo a Python che Persona eredita da ABC e quindi puoò essere una classe astratta, quindi una classe si dice astratta se implementa almeno un metodo astratto:
```python
from abc import ABC
class Persona(ABC):
	def __init__(self,nome):
		self.nome = nome
	@abstractmethod
		def ignora_metodo(self):
			pass
	def saluta(self,nome):
		print(f"Ciao {nome}")
	

mario:Persona = Persona()
mario.saluta("Alice")
```

In questo caso mi darebbe errore perché nella classe Persona è presente almeno un metodo astratto.
Tuttavia questo metodo di dichiarare un metodo astratto a caso è poco efficiente e anche brutto, 
quindi si astrae il costruttore della classe.
Tuttavia un metodo astratto può contenere logica al suo interno
```
from abc import ABC
class Persona(ABC):
	_nome:str
	@abstractmethod
	def __init__(self,nome)->None:
		if len(nome)<2:
			raise ValueError("Il nome deve avere almeno due caratteri")
		self.nome = nome.capitalize
	
	def saluta(self,nome):
		print(f"Ciao {nome}")
	

mario:Persona = Persona()
mario.saluta("Alice")
```

Ora questo fa di Persona una classe astratta.

```python
from abc import ABC
class Persona(ABC):
	_nome:str
	@abstractmethod
	def __init__(self,nome)->None:
		if len(nome)<2:
			raise ValueError("Il nome deve avere almeno due caratteri")
		self.nome = nome.capitalize
	
	def saluta(self,nome):
		print(f"Ciao {nome}")

class Studente (Persona):
	_matricola:int 

	def __init(self,nome:str, matricola:int)->None:
		super().__init__(nome)
		self._matricola = matricola 
	# Benchè l'init di Persona sia astratto lo si poù invocare nelle sue sottoclassi quindi se si fa:

mario:Persona = Studente("Mario", 1234) #Viene invocato ("Mario") viene invocato Object

print(type(mario))
print(isinstance(mario,Persona))

print(Studente.mro()) #mro() fa vedere, a partire da una classe fa vedere la catena di ereditarietà della classe 



```

![[Impl. classi astratte.png]]

Quando implemento la classe `Persona` in questo caso la si fa astratta.
La persona ha nome e telefono, quindi l'init inizializzera nome e telefono benché sia un metodo astratto.
Tutti gli argomenti che vengono dopo l'asterisco devono essere forniti da keyword.

Quando ad esempio ci sono più args dello stesso tipo, come nome o cognome è utile per risolvere l'eventuale ambiguità.

```python
from abc import ABC
class Persona(ABC):
	_nome:str
	@abstractmethod
	def __init__(self,nome)->None:
		if len(nome)<2:
			raise ValueError("Il nome deve avere almeno due caratteri")
		self.nome = nome.capitalize
	
	def saluta(self,nome):
		print(f"Ciao {nome}")

class Studente (Persona):
	_matricola:int 

	def __init(self,*,nome:str, matricola:int)->None:
		super().__init__(nome)
		self._matricola = matricola 
	# Benchè l'init di Persona sia astratto lo si poù invocare nelle sue sottoclassi quindi se si fa:

mario:Persona = Studente(nome ="Mario", matricola = 1234) #Viene invocato ("Mario") viene invocato Object

print(type(mario))
print(isinstance(mario,Persona))

print(Studente.mro()) #mro() fa vedere, a partire da una classe fa vedere la catena di ereditarietà della classe 



```


Per implementare le genralizzazioni `disjoint`  da una classe astratta non dobbiamo fare nulla di speciale in Python.

Ora immaginiamo che nel diagramma portato come esempio qui:
	La persona ha il nome 
	Lo studente ha il numero di matricola
	Il lavoratore ha la data di assunzione 
Però immaginiamo di avere solo il complete o niente, noi vorremo un modo di poter cambiare lo stato di Persona:
una persona può diventare uno studente e dopo un lavoratore e da lavoratore può diventare studente, ma da lavoratore torna ad essere una Persona.

Facciamo caso che sia Una Persona sia solo Persona ma non è ne stud o working, poi una persona può diventare o stud o lavoratore, poi un lavoratore può diventare stud, insomma tutti possono diventare tutto.
In Python questa cosa non non è possbile perché un oggetto una volta creato rimane di quella classe.
QUindi dobbiamo fare la fusione delle sottoclassi con la classe padre (questa cosa si può fare non solo se c'è il complete ma anche quando gli oggetti hanno bisogno di cambiare la loro classe piu specifica).
Immaginiamo questo caso:
![[Fusione.png]]

Innanzitutto immaginiamo che il docente si un lavoratore con un vincolo su Dipartimento `0..*` e dal lato lavoratore un altro vincolo `0..*`.
Come si può vedere in questa immagine vwengono messi dei vincoli esterni sugli attributi e anche due attributi in più che restituiscono un booleano
Questo perché:
```
per ogni p:Persona 
↓
p.is_studente = True 
```

Quindi come gestire questi vincoli in Python?
Una persona come può nascere? 
Gli attributi is_studente e is_lavoratore diventano gli attributi aggiunti in fase di design durante il passo di ristr. delle generalizzazioni per fusione sono pubblici, eventuali attributi sono privati o protetti.
Una persona quando nasce, in questo sistema, può essere sia studente che lavoratore, quindi è possibilmente non noto alla nascita:
In python questa cosa si scrive così:
