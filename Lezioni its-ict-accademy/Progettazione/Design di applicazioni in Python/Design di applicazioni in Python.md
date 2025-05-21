# Introduzione
Finora abbiamo visto come fare l'analisi concettuale: cos'è il sistema che stiamo realizzando, in termini quali sono i dati da rappresentare, etc.

 Da d'ora in poi bisogna utilizzare questo sistema come un programma python, da questa scelta derivano un'altra serie di scelte in fase di design:
1. Decidere i tipi di dato concettuali in tipi di dato supportato da Python: ovvero far corrispondere ogni tipo di dato concettuale in tipi supportati da Python.
2. Progettare l'architettura dell'applicazione Python tenendo conto di tutti i vincoli isolati in fase di analisi. 


In questa  prima fase si deve ristrutturare il diagramma concettuale, rappresentando come oggetti python le classi, le associazioni, etc. 
Così facendo, il diagramma concettuale delle classi diventa un diagramma ristrutturato delle classi da cui sarà facile scrivere codice Python o di qualsiasi altro linguaggio si sceglie di utilizzare (es: Java, SQL, etc.).
Bisogna tenere conto di 3 passaggi:
1. Sostituzione dei tipi di dato concettuale con opportuni tipi supportati 


## Progettare e realizzare i tipi di dato
L'obiettivo è quello di ristrutturare il diagramma UML concettuale delle classi in uno equivalente che contenga solo attributi di tipi di dato supportati dal linguaggi di programmazione scelto.
La metodologia è:
- Si deve scegliere un opportuno tipo di dato supportato dal linguaggio per ogni attributo, anche definendo nuove class per rappresentare le istanze (tipi di dato definiti dall'utente).
Come abbiamo visto nel diagramma UML concettuale delle classi esistono almeno 4 macro categorie per i tipi di dato:
1. **Tipi di dato concettuale:**
	- Intero (`int`)
	- Reale (`float`)
	- Booleano (`Bool`)
	- DataOra (`datetime`)
	- Data (`datetime.date`)
	- Ora (`datetime.time`)
	  E così via.
	Come possiamo vedere da questa lista, questi tipi di dato hanno un immediato corrispettivo in Python ([Dai un'occhiata alla documentazione ufficiale](https://docs.python.org/3/library/datatypes.html))
2. **[[Tipi di dato concettuale#Tipi di dato enumerativo|Tipi concettuali enumerativi]]:** 
	ad esempio i dati che vanno a definire il genere di una persona (`{M,F}`).
	Per usare questi tipi di dato in Python si deve importare la libreria `enum`, come vedremo in seguito.
3. **[[Operazioni di classe e Specializzazioni degli attributi, di associazioni e operazioni#445701 Specializzazione di attributi Esempio pratico|Tipi concettuali specializzati]]:** 
	Ad esempio `intero>0`, `reale<=0`, `x..y` 
4. **[[Tipi di dato concettuale#Tipi di dato composti(record)|Tipi concettuali definiti dall'utente o composti]]:**
    Ad esempio il tipo di dato `Indirizzo`.

Per questi tipi di dati non implementati nativamente nel linguaggio di programmazione bisogna utilizzare implementazioni del tipo disponibili nelle librerie esistenti, se possibile.
Altrimenti bisogna definire ulteriori class Python (che non hanno alcun corrispettivo nel diagramma delle classi) le cui istanze rappresentano valori del tipo. Gli oggetti di queste class saranno immutabili e Python dovrà poter riconoscere se oggetti diversi rappresentano in realtà lo stesso valore.

> [!NOTE] Nota:
> Da d'ora in avanti, per distinguere le classi del diagramma UML dalla classi Python, le prime continueranno ad essere chiamate "Classi" mentre le seconde verranno nominate "Class".
> Inoltre Class e Classi non sono sovrapponibili quindi li chiamiamo con nomi diversi.

### Esempio di progettazione dei tipi di dato in un diagramma ristrutturato
![[Ristrutturazione Python.png]]



### Realizzazione dei tipi di dati enumerativi
La procedura per realizzare i tipi di dati enumerativi in python è la seguente:
```run-python
from typing import Self, Any
from enum import *
class Genere(StrEnum): #
	uomo = auto() #crea un simbolo che si chiama come questa variabile 
	donna = auto() #crea il vlaore di tipo di dato uomo o donna che però è anche il tipo di dato donna o uomo

class Continente(StrEnum):
	asia = auto()
	europa = auto()
	america = auto()

print(Genere.uomo)
print(f"\n{Genere.donna}")
print(f"\n{type(Genere.uomo)}")
print(f"\n{Genere.uomo.upper()}")

print(f"\n{Continente.america.capitalize}")
```


### Realizzazione dei tipi di dato specializzati 

Per realizzare i tipi di dato specializzati in Python (ad esempio il valore intero dell'attributo `voto` da 18 a 31) è la seguente:
i voti sono interi ma sono interi da 18 e 31, tuttavia non si definiscono tramite una classe ma si ereditano da `init`, in questo modo ogni volto che uso un valore dell'attributo `voto` esso è anche un intero:

```run-python
from typing import Self

class Voto(int):
    def __new__(cls, v: int | float | Self) -> Self:
        v = int(v)
        if not (18 <= v <= 30):
            raise ValueError(f"Valore non valido: {v}. Deve essere tra 18 e 30.")
        return super().__new__(cls, v)

if __name__ == "__main__":
    v1 = Voto(28)
    v2 = Voto(v1)
    print(v1, type(v1))
    print(v2, type(v2))

```

**Spiegazione:**
1. Importa `Self` dal modulo `typing`.  
	`Self` è un **alias del tipo della classe corrente**, utile per annotare metodi che restituiscono un'istanza della classe stessa.  
	 `Self` è disponibile solo in **Python 3.11 o versioni successive**.
Così facendo si definisce una nuova classe `Voto` che **eredita da `int`**.  
Questo significa che ogni oggetto `Voto` **è anche un numero intero**, ma con un **controllo sui valori consentiti** (tra 18 e 30 inclusi).
2. `def **new**(cls, v: int | float | Self) -> Self:`:
	✅ `__new__` è il metodo speciale usato per **creare** un'istanza immutabile (come `int`, `float`, `str`).  
- `cls` è la classe (qui `Voto`).
- `v` è il valore che vogliamo usare per creare l'oggetto. Può essere:
  - `int`: es. `Voto(25)`
  - `float`: es. `Voto(25.0)`  
  - `Self`: cioè un altro oggetto `Voto`, es. `Voto(Voto(28))`

La notazione `-> Self` indica che il metodo restituirà un oggetto della **stessa classe `Voto`**.
In altre parole converte `v` in intero (serve nel caso in cui venga passato un `float` o un altro `Voto`).

3. **blocco `if not (18 <= v <= 30):`:**

```python
 if not (18 <= v <= 30): 
 raise ValueError(f"Valore non valido: {v}. Deve essere tra 18 e 30.") return super().__new__(cls, v):
```
	
✅ Controlla che il valore sia **compreso tra 18 e 30 inclusi**.  
Se non lo è, lancia un’**eccezione `ValueError`**.
Usa `super()` per chiamare il metodo `__new__` di `int`, passando il valore convalidato.  
Questo è **il vero momento in cui viene creato l'oggetto `Voto`**.

4. **Blocco codice test:**
```python
if __name__ == "__main__":
    v1 = Voto(28)
    v2 = Voto(v1)
    print(v1, type(v1))
    print(v2, type(v2))

```
- `v1 = Voto(28)` → Crea un oggetto `Voto` con valore 28 ✅
    
- `v2 = Voto(v1)` → Crea un altro `Voto` partendo da un oggetto `Voto(28)` ✅
    
- `print(...)` mostra:
```
28 <class '__main__.Voto'>
28 <class '__main__.Voto'>
```

Tuttavia in questo codice se venisse fatta la somma  `Voto(18) + Voto(18)` non darebbe errore perché `Voto` è un `int` e di fatto si otterrebbe il valore `36`.
Ma questo valore non è un voto valido quindi **bisognerebbe impedire questo comportamento** o almeno **ricontrollarlo dopo l’operazione.** 
Per ovviare a questo problema bisogna definire il metodo speciale `__add__()`:
==Sovrascrivere `__add__` ci consente di **controllare il risultato della somma** e restituire un nuovo `Voto` **valido** oppure lanciare un errore.== 
```run-python
from typing import Self

class Voto(int):
    def __new__(cls, v: int | float | Self) -> Self:
        v = int(v)
        if not (18 <= v <= 30):
            raise ValueError(f"Valore non valido: {v}. Deve essere tra 18 e 30.")
        return super().__new__(cls, v)

    def __add__(self, other: Self) -> Self:
        result = int(self) + int(other)
        return Voto(result)  # Viene ricontrollato anche qui

if __name__ == "__main__":
    v1 = Voto(18)
    v2 = Voto(18)
    try:
        v3 = v1 + v2
        print(v3)
    except ValueError as e:
        print(f"Errore nella somma: {e}")

```

In realtà si può risolvere questo problema anche in un altro modo ma è più verboso e complesso del primo.
```run-python
from typing import Self

class Voto:
    def __init__(self, v: int | float | 'Voto'):
        if isinstance(v, Voto):
            v = v._v
        v = int(v)
        if not (18 <= v <= 30):
            raise ValueError(f"Valore non valido: {v}. Deve essere tra 18 e 30.")
        self._v = v

    def __add__(self, other: Self) -> Self:
        return Voto(self._v + other._v)

    def __int__(self) -> int:
        return self._v

    def __repr__(self) -> str:
        return f"Voto({self._v})"

if __name__ == "__main__":
    v1 = Voto(18)
    v2 = Voto(18)
    try:
        v3 = v1 + v2
        print(v3)
    except ValueError as e:
        print(f"Errore nella somma: {e}")

```

In questo caso non  si eredita da `int`, ma lo si usa internamente. 
Bisogna, quindi, delegare tutte le operazioni manualmente.

> [!NOTE] Nota
> Bisogna definire manualmente `__int__()`, `__repr__()` e **qualsiasi altra operazione** che si vuole supportare (`__eq__`, `__lt__`, ecc.).

In conclusione:
**Se vuoi un tipo specializzato che “è anche” un numero**, l’ereditarietà da `int` è la soluzione più Pythonica.  
**Se invece vuoi un tipo più astratto e controllato**, senza comportamento implicito da `int`, allora va bene l’attributo `_v`, ma il codice sarà più lungo e meno naturale da usare.

### Realizzazione  di dati composti
Se si vuole modellare il tipo di dato indirizzo, due indirizzi se hanno lo stessa via e lo stesso civico sono due indirizzi uguali (in teoria).
```run-python
from typing import Self, Any

class Indirizzo:
    _via: str 
    _civico: int 

    def __init__(self, via: str, civico: int) -> None:
        self._via = via
        self._civico = civico

    def via(self) -> str:
        return self._via

    def civico(self) -> int:
        return self._civico

    def __hash__(self) -> int:
        return hash((self._via, self._civico))

    def __eq__(self, other: Any) -> bool:
        if other is None or \
           not isinstance(other, type(self)) or \
           hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico

i1: Indirizzo = Indirizzo("Viale Cesare Pavese", civico=205)
i2: Indirizzo = Indirizzo("Viale Cesare Pavese", civico=205)

print(i1 == i2)         # True
print(hash(i1) == hash(i2))  # True

```

==Se si  facesse `i1 != i2`  si ottiene `False` (giusto), ma se non si implementasse `__eq__` e `__hash__`, verrebbe fatto il confronto sull'identità fisica (`is`) e darebbe `True` solo se sono **lo stesso oggetto in memoria**.== 

Quando  si implementa `__eq__`, ==conviene **ottimizzare il caso in cui il confronto dà False**, perché nella pratica si confrontano più oggetti diversi che uguali==. 
Per questo motivo conviene prima controllare i casi che escludono subito l’uguaglianza (tipo diverso, hash diverso...)

Ora si possono usare oggetti `Indirizzo` come **chiavi di un dizionario**, perché abbiamo sono stati implementati `__hash__` e `__eq__`:
```
d: dict[Indirizzo, int] = {}
d[i1] = 9
print(d[i2])  # 9, perché i2 è considerato uguale a i1

```


> [!NOTE] Nota
> ==Per poter usare oggetti come chiavi nei dizionari o all’interno di un `set`, **è obbligatorio** implementare correttamente **sia `__eq__` che `__hash__`**. Se due oggetti sono uguali secondo `__eq__`, devono anche avere lo **stesso valore di hash**.==

