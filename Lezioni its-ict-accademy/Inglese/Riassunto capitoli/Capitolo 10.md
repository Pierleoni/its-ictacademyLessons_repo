# Usare le astrazioni e i patterns

Oltre a memorizzare i dati, questi tipi incorporati forniscono molte delle proprie funzioni per manipolare i loro contenuti. Ad esempio:

```run-python
capulets = ['Juliet', 'Tybalt', 'Nurse'] # lista
capulets.append('Rosaline') # Aggiunge un nuovo elemento
pi = 3.142 # float
pi.is_integer() # Valuta a False
sentence = 'It was the best of times, it was the worst of times'
sentence.split(' ') # Valuta a: ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']
```

Tali funzioni rappresentano operazioni molto comuni. Approfittare di esse aiuta a ridurre la quantità di lavoro da fare, quindi prenditi del tempo per conoscere le funzioni disponibili (vedi il riferimento online del linguaggio Python: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)). Riutilizzarle significa non dover fare il lavoro da solo, e in più sono ampiamente testate e ottimizzate.

### CREARE I PROPRI TIPI

A volte, una struttura emergerà dalla tua soluzione che nessun tipo incorporato può soddisfare. Ad esempio, nello scenario di noleggio veicoli del Capitolo 4, sono emersi diversi schemi, tra cui 'auto', 'furgone' e 'motocicletta'. Inoltre, questi erano tutti versioni del concetto più generale di 'veicolo'. Ogni tipo ha supportato proprietà particolari (come la quantità di carburante, la capacità) e operazioni (per esempio, check-in, report chilometraggio).

Python non fornisce tipi veicolari per aiutarti in questo caso. In una situazione come questa, quando nessun tipo incorporato soddisfa i tuoi requisiti, puoi creare i tuoi. In Python, ciò significa familiarizzare con la programmazione orientata agli oggetti (OOP), un argomento con una vasta quantità di materiale. Coprire tutta l'OOP, anche brevemente, esula dallo scopo di questo libro. Invece, esamineremo solo il materiale di immediata rilevanza per la creazione di astrazioni in Python. Per illustrare questo processo, useremo lo scenario di noleggio veicoli.

Indipendentemente dal fatto che un tipo sia incorporato o meno, un tipo è come un modello o una pianta. Un oggetto è un'istanza di un tipo, creato a partire da questo modello. Di conseguenza, c'è un solo modello definitivo per ogni tipo, ma puoi produrre quanti oggetti desideri da esso. Quando vuoi creare il tuo tipo, devi scrivere un 'modello' che dica al computer come creare oggetti del tuo tipo personalizzato.

### PRIMI PASSI

In Python, i tipi sono chiamati classi. Il punto di partenza per creare un nuovo tipo in Python è definire una nuova classe:
```python
class Car:
    pass
```

La parola chiave `pass` in Python dice effettivamente "Sto lasciando deliberatamente vuota la definizione di questa cosa." È utile quando vuoi tracciare la struttura di un programma ma devi rimandare l'aggiunta dei dettagli.

Questi due righi da soli creano una nuova classe. Puoi provarlo eseguendo questi comandi:

```python
x = Car()
print(type(x)) # Stampa: <class 'Car'>
```

La riga `x = Car()` crea un nuovo oggetto della classe `Car` (cioè istanzia un oggetto di tipo Car). Creare un nuovo oggetto in questo modo è qualcosa che puoi fare con qualsiasi tipo, anche quelli incorporati:
```run-python
my_integer = int() # Equivale a my_integer = 0
print(my_integer) # Stampa 0
print(type(my_integer)) # Stampa <class 'int'>
my_list = list() # Equivale a my_list = []
print(my_list) # Stampa []
print(type(my_list)) # Stampa <class 'list'>
```

Ammettiamo che `Car` sia piuttosto inutile così com'è. Non può memorizzare informazioni rilevanti e non ha operazioni per manipolare i dati. Prima che possa diventare utile, dobbiamo completare la sua definizione. Ora possiamo iniziare a costruire le astrazioni che abbiamo scoperto quando abbiamo pianificato lo scenario del noleggio veicoli.

Quando costruisci astrazioni, ricorda che operi in un determinato contesto che ti dice a quale livello operare. Ad esempio, un veicolo può essere compreso a diversi livelli di dettaglio. Chi modella il traffico autostradale può trattare un veicolo come un oggetto singolo, mentre chi si occupa di sicurezza automobilistica deve considerare un'auto come composta da molti componenti, ognuno con il proprio comportamento.

Per ogni astrazione, avrai identificato:

1. le proprietà che appartengono a ciascuna astrazione;
    
2. le operazioni che possono essere applicate a ciascuna astrazione.
    

Queste corrispondono a due cose che le classi in Python forniscono:

1. **attributi dati**: variabili che appartengono a un particolare oggetto.
    
2. **metodi**: funzioni che appartengono a un particolare oggetto.
    

Aggiungiamo un attributo alla nostra classe: la categoria del veicolo, che identifica questo tipo di auto (cioè, 'B'):
```python
class Car:
    category = 'B'
```

Ora `category` è diventato un attributo di ogni oggetto `Car` che creeremo. Questo lo rende una variabile di classe, poiché il valore è lo stesso per ogni istanza di questa classe:
```python
fiat = Car() # Crea una nuova istanza della classe Car
ford = Car() # Crea un'altra nuova istanza della classe Car
print(fiat.category) # Stampa 'B'
print(ford.category) # Stampa 'B'
```

Alcuni attributi variano tra le diverse istanze della stessa classe. Ogni auto può essere categoria 'B' per definizione, ma ogni auto ha il proprio nome del modello. Python tratta tali attributi (variabili di istanza) in modo leggermente diverso:

```
class Car:
    category = 'B'
    def __init__(self, model):
        self.model = model
```

Alcuni commenti su questo:

- Abbiamo aggiunto un nuovo metodo con un nome insolito alla classe `Car`: `__init__`. Questo è un metodo speciale chiamato inizializzatore, che viene eseguito automaticamente ogni volta che viene creata una nuova istanza di una classe. Il suo scopo è fornire un posto per aggiungere istruzioni che ogni oggetto deve eseguire quando viene creato per la prima volta. Viene spesso utilizzato per specificare i valori iniziali degli attributi di un oggetto.
    
- Il nome del metodo `__init__` inizia e termina con una coppia di trattini bassi. Questa è una convenzione applicata a tutti i metodi speciali che un oggetto può avere.
    
- Un metodo `__init__` ha sempre almeno un parametro. Per convenzione, viene chiamato `self`. Non è necessario passare questo parametro tu stesso – appare magicamente ed è sempre il primo parametro.
    
    - `self` rappresenta l'oggetto stesso. È un modo per permettere a un oggetto di essere introspectivo e di manipolare le proprie proprietà.
        
- Oltre al parametro `self`, un inizializzatore può avere un numero arbitrario di parametri aggiuntivi.
    

Ora possiamo creare oggetti con valori iniziali e accedere a quegli attributi successivamente:
```
cars = [Car('Ford Anglia'), Car('Morris Minor')]
for car in cars:
    print(car.model)
```

Aggiungiamo un altro attributo alle auto, che è molto importante per un'agenzia di noleggio: il chilometraggio. Ogni auto registrerà il proprio chilometraggio e fornirà anche un'operazione per aggiornarlo.
**Polimorfismo**

Il polimorfismo permette di trattare oggetti di classi diverse in modo uniforme, grazie a metodi che si comportano in modo diverso a seconda del tipo di oggetto. Un esempio è dato dalla classe `Van`, che eredita da `Vehicle` e implementa un proprio metodo `__init__()` per inizializzare l'attributo `payload`. In questo modo, ogni tipo di veicolo, come un furgone o una macchina, può avere attributi propri, ma il codice può comunque operare su una lista di veicoli con il metodo `hasattr` per verificare se un veicolo ha l'attributo `payload`.

**Composizione degli Oggetti**

Quando la relazione tra due oggetti non è "è un" (come nel caso delle classi derivate), ma "ha un" (come una sezione di parcheggio che ha parcheggi), si utilizza la composizione degli oggetti. Invece di far ereditare una classe dall'altra, si creano oggetti che possiedono altri oggetti, come nel caso di una sezione di parcheggio che contiene più posti auto. La composizione è spesso preferita all'ereditarietà perché è più flessibile, ma l'ereditarietà è utile quando una gerarchia di classi segue una struttura familiare chiara.

**Pattern e Abstratti**

I pattern di progettazione sono soluzioni standardizzate a problemi ricorrenti nella programmazione, che riducono il tempo di sviluppo, migliorano la comprensione e forniscono un vocabolario comune per descrivere il design del software. In Python, alcuni pattern sono supportati direttamente dal linguaggio, come la comprensione delle liste o l'uscita anticipata da un ciclo. Altri, come lo "scambio temporaneo" di variabili o l'inizializzazione pigra, devono essere implementati manualmente.

**Pattern di Progettazione: Facade, Factory, e Method Chaining**

- **Facade Pattern**: Maschera la complessità di un sistema tramite un'interfaccia più semplice, come nel caso di un sistema di accensione di un'auto che nasconde la complessità dietro un'unica chiamata al metodo `start_car`.
    
- **Factory Pattern**: Aiuta a creare oggetti complessi, delegando la creazione a una fabbrica. Ad esempio, una classe `EngineFactory` potrebbe creare componenti del motore in base al tipo di motore. Questo aiuta a mantenere il codice più semplice e modulare.
    
- **Method Chaining**: Permette di concatenare chiamate a metodi, in modo che l'output di un metodo venga passato direttamente come input al successivo. Questo riduce la necessità di memorizzare variabili temporanee e rende il codice più fluido.
    

**Conclusioni**

Nel pensiero computazionale, un buon approccio è quello di evitare la ripetizione del codice (DRY, "Don't Repeat Yourself") e di identificare ciò che varia per incapsularlo in una struttura modulare. Utilizzare pattern pre-esistenti, come quelli descritti, può velocizzare lo sviluppo e migliorare la qualità del codice, mentre la creazione di astrazioni proprie aiuta a risolvere problemi specifici in modo elegante e riutilizzabile. I pattern di progettazione sono strumenti essenziali per affrontare problemi complessi e rendere il software più facilmente manutenibile.




---
# Traduzione in inglese

## Using abstractions and patterns
In addition to storing data, these built-in types provide many of their own functions for manipulating their contents. For example:
```run-python
capulets = ['Juliet', 'Tybalt', 'Nurse']  # list
capulets.append('Rosaline')  # Adds a new item
pi = 3.142  # float
pi.is_integer()  # Evaluates to False
sentence = 'It was the best of times, it was the worst of times'
sentence.split(' ')  # Evaluates to: ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times']
```

Such functions represent very commonly used operations. Taking advantage of them helps reduce the amount of work you have to do, so spend some time getting to know the functions available (see the Python language online reference: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)). Reusing them means you don’t have to do the work yourself, plus they’re heavily tried, tested, and optimized.

**CREATING YOUR OWN TYPES**

The car rental example was introduced in Chapter 4; see the section ‘Context and layers’.

Sometimes, a structure will emerge from your solution that no built-in type can satisfy. For example, in the vehicle rental scenario of Chapter 4, several patterns emerged, including ‘car’, ‘van’, and ‘motorcycle’. Furthermore, these were all versions of the more general concept ‘vehicle’. Each type turned out to support particular properties (such as fuel amount, capacity) and operations (for example, check-in, report mileage).

Python provides no vehicular types to help you here. In a case like this, when no built-in types meet your requirements, you can create your own. In Python, that means getting familiar with object-oriented programming (OOP), a subject with a wealth of material behind it. Covering all of OOP, even briefly, is out of scope for this book. Instead, we’ll examine only the material of immediate relevance to the creation of abstractions in Python. To illustrate this process, we’ll use the car rental scenario.

Whether built-in or not, a type is like a blueprint or template. An object is an instance of a type, created from this blueprint. As such, there’s only one definitive blueprint for each type, but you can manufacture as many objects from it as you like. When you want to create your own type, you must write a ‘blueprint’ that tells the computer how to create objects of your custom type.

**First Steps**

In Python, types are called classes. The starting point to creating a new type in Python is to define a new class:
```python
class Car:
    pass
```

The `pass` keyword in Python effectively says ‘I’m purposefully leaving the definition of this thing empty.’ It’s useful when you want to lay out the structure of a program but need to defer adding details.

Those two lines alone create a new class. You can prove it by entering these lines below:
```python
x = Car()
print(type(x))  # Prints: <class 'Car'>
```
The line `x = Car()` creates a new object of the Car class (that is, it instantiates a Car object). Creating a new object this way is something you can do with any type, even the built-in ones:
```run-python
my_integer = int()  # Equivalent to my_integer = 0
print(my_integer)  # Prints 0
print(type(my_integer))  # Prints <class 'int'>
my_list = list()  # Equivalent to my_list = []
print(my_list)  # Prints []
print(type(my_list))  # Prints <class 'list'>
```

Admittedly, `Car` is pretty useless as written. It can’t store relevant information and it has no operations to manipulate data. Before it can become useful, we must flesh out its definition. Now we can start to build the abstractions we discovered when planning the vehicle rental scenario.

When you build abstractions, remember that you’re operating in a certain context that tells you at what level to operate. For example, a vehicle can be understood at different levels of detail. Someone modelling highway traffic can treat a vehicle as a single object, whereas someone working with car safety has to consider a car as made up of many components, each with its own behaviours.

For each abstraction, you will have identified:

1. properties that belong to each abstraction;
    
2. operations that can be applied to each abstraction.
    

These correspond with two things that classes in Python provide:

1. data attributes: variables that belong to a particular object.
    
2. methods: functions that belong to a particular object.
    

Let’s add an attribute to our class – the regulatory vehicle category that identifies this type of car (that is, ‘B’):
```python
class Car:
    category = 'B'
```

`category` has now become an attribute of every `Car` object we will create. This makes it a class variable because the value is the same for each instance of this class:
```python
fiat = Car()  # Creates a new instance of the Car class
ford = Car()  # Creates another new instance of the Car class
print(fiat.category)  # Prints 'B'
print(ford.category)  # Prints 'B'

```
Some attributes vary among different instances of the same class. Every car may be category B by definition, but each car has its own model name. Python treats such attributes (instance variables) a little differently:
```python
class Car:
    category = 'B'
    def __init__(self, model):
        self.model = model
```

Some remarks about this:

- We’ve added a new, oddly named method to the Car class: `__init__`. This is a special method called an initializer, which is automatically executed whenever a new instance of a class is created. Its purpose is to provide a place for the programmer to add instructions that every object must execute when first created. It’s often used to specify the initial values of an object’s attributes.
    
- The `__init__` method name begins and ends with a pair of underscores. This is a convention applied to all the special methods that objects can have (see the box below).
    
- An `__init__` method always has at least one parameter. By convention, it is named `self`. You don’t pass this parameter yourself – it just magically appears and is always the first parameter. `self` represents the object itself. It’s a way of allowing an object to be introspective and able to manipulate its own properties.
    
- In addition to the `self` parameter, an initializer may have an arbitrary number of additional parameters following it.
    

A Python special method can be called using a specific syntax rather than by calling the method. For example, `__init__` is a special method because you don’t instantiate, say, a car by calling `Car.__init__()`, rather you just call `Car()` and that in turn calls `__init__()`.

Now, we can create objects with initial values and access those attributes later:

```python
cars = [Car('Ford Anglia'), Car('Morris Minor')]
for car in cars:
    print(car.model)
```
Let’s add another attribute of cars that’s very important to a rental agency: the mileage. We’ll have each car record its own mileage and also provide an operation to update it.
```run-python
class Car:
    category = 'B'
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage  # New attribute

    # New method
    def update_mileage(self, new_mileage):
        if new_mileage < self.mileage:
            print('Error: New mileage cannot be lower than current mileage!')
        else:
            self.mileage = new_mileage
```
Some remarks on that:

- We could have just written `my_car.mileage = 123789`, but since the process is more complicated than that (we first have to check that the odometer hasn’t been tampered with), we put the whole updating procedure into a class method and call that instead. By putting it in one place, this allows us to follow the advice from earlier (i.e., ‘don’t repeat yourself’).
    
- Once again, the `self` parameter appears. It has to be included because the method works with instance variables and so needs access to the particular object being dealt with (remember, many `Car` objects might exist and updating a car’s mileage applies only to one of them at a time). Again, it is passed automatically. Essentially, the value of `my_car` gets assigned to `self` without you needing to do anything.
In this chapter, we delve deeper into object-oriented programming and how thinking in terms of patterns can improve code design.

- **Inheritance and Composition**: The chapter explains the concepts of inheritance and object composition. Inheritance allows a class (like `Van`) to inherit from a parent class (like `Vehicle`), but it also allows specific attributes to be added, such as the `payload` for the `Van`. Composition, on the other hand, is illustrated with the example of a `ParkingSection`, which contains `ParkingBay` objects. This exemplifies the "has a" relationship, where an object contains other objects rather than inheriting from them. Although inheritance is suitable when there is an "is a" relationship, composition offers greater flexibility and is often preferred in real-world applications.
    
- **Using Patterns**: As you gain experience in coding, certain patterns will emerge repeatedly. These can be simple, such as using list comprehensions or breaking out of loops, or more complex like swapping variables. Understanding common programming patterns helps simplify code and provides a shared vocabulary for discussing solutions. These patterns can often be found in Python’s built-in features or manually implemented. An example of a simple pattern is lazy initialization, where an object’s attribute is initialized only when needed.
    
- **Design Patterns**: The chapter also introduces design patterns, specifically focusing on the facade pattern, which simplifies complex systems by hiding them behind a simpler interface. In the example of a car's ignition system, the complexity of several interacting components is simplified by the `IgnitionSystem` class, which consolidates all the steps to start the car into a single method.
    
- **Creational and Behavioural Patterns**: A design pattern is often created to solve a specific problem related to how objects are created or interact. The chapter explores the factory pattern, which simplifies complex object creation by delegating the task to a separate class. The `EngineFactory` class, for example, determines the type of engine and returns the appropriate battery for a car's ignition system.
    
- **Method Chaining**: Another pattern discussed is method chaining, where multiple methods can be chained together to perform a sequence of actions without storing intermediate results in variables. This is illustrated with an example of drawing power from a battery and passing it through various components of the ignition system.
    

The chapter concludes by highlighting the importance of recognizing patterns in your code to improve readability, reusability, and efficiency. It stresses the value of design patterns in organizing complex systems and provides a foundation for using them in programming practice.