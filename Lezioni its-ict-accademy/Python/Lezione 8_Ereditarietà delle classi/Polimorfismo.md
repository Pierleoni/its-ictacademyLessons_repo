# Introduzione 
In programmazione ad oggetti ([[Introduzione a Python#Object-Oriented|OOP]]), il **polimorfismo** significa: *"avere molte forme"* .
Concretamente il polimorfismo ==permette di definire metodi con lo stesso nome in classi diverse, ma ognuno con un comportamento specifico==.
Questo è finalizzato in Python a rendere il codice più **flessibile, riutilizzabile e manutenibile.** 

## Cos'è il polimorfismo
In sostanza il polimorfismo è: 
==la possibilità di invocare lo stesso nome di un metodo su oggetti (istanze) di classi diverse, ottenendo risultati diversi a seconda dell'oggetto.==  ^polimorfismo-def
Il suo obiettivo e rendere il codice capace di gestire oggetti di tipo diverso usando una interfaccia comune (cioè usando uno stesso metodo con lo stesso nome).
In Python, **non serve** dichiarare esplicitamente il tipo degli oggetti (come in Java o C++), quindi il polimorfismo avviene in modo naturale: si parla infatti di **polimorfismo duck typing** ("se cammina come un'anatra e starnazza come un'anatra, allora è un'anatra"). 

### Esempio pratico di Polimorfismo
#### Step 1: File `Persona_2.py`
1. Andiamo a creare un file `.py` chiamato `Persona_2.py`, in questo file creiamo una classe `Persona`:
```python
class Persona: 
```
 
 2. dopodiché dobbiamo definire il [[Le Classi#**Definizione di una Classe e il Costruttore** `__init__()`|costruttore della classe]] (`__init__()`), che prende: 
	 come parametri l'attributo `name` (cioè il nome della persona), l'attributo `last` (cioè il lastname o cognome in italiano) e, infine, l'attributo `age` (cioè l'età della persona ).
```python
class Persona:

    def __init__(self, name:str, last:str, age:int):

        self.name = name

        self.lastname = last

        self.age = age
```

3. Inoltre implemento anche una serie di [[Le Classi#**Gestione degli Attributi con Getter e Setter**|setter e getter]] all'interno della classe e il metodo speciale [[Le Classi#Il metodo `__str__`|`__str__()`]]:

```python
 '''

    Mi consente di impostare un valore per self.name

    '''

    def set_name(self, name: str) -> None:

        self.name = name

    def __str__(self):

        return f"{self.name} {self.lastname}, {self.age} anni"

    '''

    Mi consente di impostare un valore per self.lastname

    '''

    def set_lastname(self, lastname: str) -> None:

        self.lastname = lastname

    '''

    Mi consente di impostare un valore per self.age

    '''

    def set_age(self, age: int) -> None:

        if age < 0 or age > 130:

            self.age = 0

        else:

            self.age = age

    '''

    funzione che mi consente di ritornare il valore di self.Name

    '''

    def getName(self) -> str:

        return self.name

    '''

    funzione che mi consente di ritornare il valore di self.lastname

    '''

    def getLastName(self) -> str:

        return self.lastname

    '''

    funzione che mi consente di ritornare il valore di self.age

    '''

    def getAge(self) -> int:

        return self.age
    def display_data(self) -> None:

        print(f"Nome: {self.name}")

        print(f"Cognome: {self.lastname}")

        print(f"Età: {self.age}")     
```

Da notare come il metodo `set_age()` lo si usi anche per controllare se il valore dell'attributo `age` sia un valore valido:
all'interno del metodo `def set_age(self):` impostiamo un blocco `if-else` per cui:
se il valore dell'attributo  `age` e minore di `0` o maggiore di `130` allora `self.age =0`, 
altrimenti (`else`);`self.age = age`.

4. Infine come ultima cosa, ma non per importanza, definiamo un metodo `speak()`, che andrà a stampare in output un messaggio di saluto:
```python
    def speak(self) -> None:

        print(f"Hello! My name is {self.getName()}")
```

#### Step 2: File `alieno.py`
1. Creiamo un file chiamato `alieno.py` e all'interno definiamo una classe `Alieno`:
```python
class Alieno:
```

2. Di un alieno ci interessa sapere la galassia di provenienza, per questo con il costruttore della classe andremo a definire un parametro `galaxy:str`:
```python
class Alieno:
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
```

Più o meno come per l'attributo `age`, il `self.setGalaxy(galaxy)` serve per controllare che il valore di `galaxy` sia valido, ad esempio che non sia una stringa vuota. 

3. Andiamo a definire un metodo per impostare il valore dell'attributo `self.galaxy`: 
```python
    def setGalaxy(self, galaxy:str)->None:

        if galaxy:

            self.galaxy=galaxy

        else:

            print("Errore! La galassia non può essere una stringa vuota")
```
 In questo metodo settiamo, attraverso l'uso di un setter, il valore di `galaxy` dentro un blocco `if-else`:
 nello statement `if`, andiamo a dire che se `galaxy` è `True`(cioè in questo caso non è una stringa vuota) allora deve impostare `self.galaxy = galaxy`, altrimenti deve stampare in output un messaggio di errore dicendo che la galassia non può corrispondere a una stringa vuota.

4. In seguito definiamo un metodo per restituire il valore dell'attributo `self.galaxy`:

```python
    def getGalaxy(self) -> str:
        return self.galaxy
```

5. Come per la classe `Persona`, definiamo un metodo `speak()`, che stampa in output un messaggio di saluto:
```python
    def speak(self)->None:

        print("hfdhfdjhfjhdfdfidshfdjkfh")
```

6. Andiamo a definire il [[Le Classi#Il metodo `__str__`|metodo speciale `__str__()`]] che ritorna in output la una stringa formatta: 
```python
    def __str__(self)->str:
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"
```

#### Step 3: File `polimorfismo.py`
1. Andiamo a creare il file `polimorfismo.py` e importiamo sia dal file `Persona_2.py` la classe `Persona` che dal file `alieno.py` la classe `Alieno`
```python
from Persona_2 import Persona
from alieno import Alieno
```

2. In seguito creiamo un oggetto o istanza di `Persona` (cioè l'istanza `p`) e stampiamo in output le informazioni dell'oggetto `p` della classe `Persona`:

```python
p:Persona = Persona("Antonio", "Scugnizzo", 22)
# Visualizzare le informazioni dell'oggetto p della classe Persona
print(p) #Output: Antonio Scugnizzo, 22 anni
```

3. Dopodiché creiamo l'istanza di `Alieno` (cioè l'istanza `et`) e stampiamo le informazioni dell'oggetto et della classe `Alieno`:
```python
et:Alieno = Alieno("Andromeda")
# Visualizzare le informazioni dell'oggetto et della classe ALieno
print("\n",et)
```

4. Adesso possiamo invocare il metodo `speak()` sia della classe `Persona` che della classe `Alieno`:
```python
'''
invocare il metodo speak() della classe Persona
'''
p.speak()

'''
invocare il metodo speak() di un ALieno
'''
et.speak()
```

Se runniamo il codice vediamo che l'output corrisponderà sia al messaggio del `print()` contenuto  nella funzione `speak()` della classe `Persona`, che al messaggio del `print()` contenuto nella funzione `speak()` della Classe `Alieno`. 
Quindi in output abbiamo 2 risultati diversi: prima diciamo all'oggetto `p`invoca  il metodo `speak()` che compie un'azione specifica relativa alla classe `Persona`, mentre  l'oggetto `et` invoca il metodo `speak()` che mi fa una azione specifica per la classe `Alieno`. 
In sintesi, come accennato prima: ==il polimorfismo è quindi avere metodi con lo stesso nome per classi diverse e definiti in maniera diversa per ogni classe.==

### Differenza tra Overriding e Polimorfismo
Sebbene l'overriding e il polimorfismo di primo impatto possano sembrare due concetti simili, non lo sono. 
Semmai sono due concetti **correlati ma distinti.**
#### Overriding
L'[[Ereditarietà delle classi#L'overriding dei metodi|overriding]] avviene quando una sottoclasse ridefinisce un metodo ereditato da una superclasse.
>==Serve per modificare o personalizzare il comportamento di un metodo già definito nella classe genitore.==

```run-python
class Alieno:
    def speak(self):
        print("Lingua aliena: bzz bzz bzz")

class Persona(Alieno):  # Persona eredita da Alieno
    def speak(self):  # Override del metodo speak
        print("Ciao, sono una persona")

p = Persona()
p.speak()  # --> "Ciao, sono una persona"

a = Alieno()
a.speak()  # --> "Lingua aliena: bzz bzz bzz"

```
**Spiegazione**:

- Anche se entrambi gli oggetti (`p` e `a`) hanno un metodo `speak()`, quello della **sottoclasse (`Persona`) ha sovrascritto** il comportamento del genitore.
    
- Python guarda il **tipo dell'oggetto** (`Persona` o `Alieno`) e usa il metodo corrispondente.

#### Cos’è invece il **Polimorfismo**?

Il **polimorfismo** è un concetto più generale:

> ==Permette di **usare lo stesso nome di metodo su oggetti di classi diverse**, indipendentemente dal fatto che una classe erediti dall’altra.==

Esempio:
```run-python
class Persona:
    def speak(self):
        print("Ciao! Sono umano.")

class Alieno:
    def speak(self):
        print("Krrgzzzt! Sono alieno.")
def chi_parla(essere):
    essere.speak()

chi_parla(Persona())  # --> "Ciao! Sono umano."
chi_parla(Alieno())   # --> "Krrgzzzt! Sono alieno."

```
Qui, non c’è **nessun legame di ereditarietà**, ma Python può comunque chiamare `speak()` su entrambi gli oggetti.  
Questo è **polimorfismo tramite duck typing**: se un oggetto ha il metodo `speak()`, allora può parlare, **a prescindere da che classe appartenga**.

Quindi come si fa a distinguere i due metodi delle due classi diverse?
Dipende dall'oggetto che lo invoca: 
se l'oggetto `p` invoca il metodo `speak()`allora sto dicendo a Python di invocare il metodo `speak()` della classe `Persona`, se l'oggetto `et` invoca il metodo `speak()` sto dicendo a Python di invocare il metodo `speak()` della classe `Alieno`.
==Python **non guarda il nome del metodo**, ma **a quale classe appartiene l’oggetto che lo invoca**.== 