# Introduzione
Abbiamo parlato nelle scorsa lezione della [[Responsabilità]] e dell'[[Responsabilità#L'aggregazione|aggregazione]].
Ora vedremo come implementare in Python la [[Responsabilità#^6a5c39|responsabilità singola]].

Immaginiamo un caso in cui nel diagramma delle classi si ha una responsabilità che parte dalla classe `Studente` e va verso la classe `Modulo`, e la responsabilità ha una association class `esame` con l'attributo `voto:Voto <<immutabile>>` e un vincolo `0..*` da entrambe le parti:
![[Impl Resp Singola.png]]

In sostanza l'interpretazione di questo diagramma è:
 - Uno studente può sostenere nessun modulo o più moduli 
 - Ogni modulo può essere sostenuto da nessuno studente o da più studenti
 - Ogni `Esame` collega un `Studente` a un `Modulo` e **registra un voto**.
 -  La **Responsabilità Singola** è data al `Studente`, che **gestisce i suoi esami**.


Per implementare questo diagramma in python ci riferiremo a questa immagine:
![[Logica di implementazione.png]]
- Un oggetto `Studente` (`s1`) mantiene un **dizionario `_esami`**.
    
- Le chiavi del dizionario sono `Modulo` (es. `m1`, `m2`), i valori sono `Esame` (es. `e1`, `e2`).
    
- Ogni oggetto `Esame` conosce lo studente, il modulo e il voto.

Ora detto questo implementiamo questo diagramma in Python:
### Implementazione in Python
Prima di implementare le classi vanno fatti un paio di  `import`:
```python
from __future__ import annotations
```
Importa la funzionalità sperimentale `annotations` dal modulo speciale `__future__`.
Serve per abilitare una funzionalità opzionale (ma utile) nel parsing dei tipi di Python.
Questa direttiva, in sostanza:
==Dice a Python di **ritardare l’analisi delle annotazioni di tipo** (type hints) fino a runtime.== 
In pratica tutte le annotazioni di tipo (come `Studente`, `Modulo`,etc.) vengono trattate come stringhe, anziché come oggetti veri e propri (es: `"Studente"` invece di `Studente`) finché non viene lanciato il programma.
Questo è utile quando si usa una classe prima che sia stata definita (in genere senza questo tipo di direttiva si riceve un errore di tipo `NameError`).
In sintesi ==permette i riferimenti incrociati anche se le classi sono dichiarate dopo==.  ^fromFuture

#### La classe `Studente`:
Definiamo degli attributi privati al di fuori del costruttore
```Python
_nome: str
_esami: dict[Modulo, _esame]
```

- `_nome`: nome dello studente.
    
- `_esami`: **collezione di chiave-valore di esami**, **gestita dal lato Studente**. 
  Usa `Modulo` come chiave e l'associazioni `_esame` come valore.
  
> [!NOTE] Il `dict` è usato per garantire **unicità** del modulo per studente (nessun doppio esame sullo stesso modulo).



Quindi nel costruttore :
```python
def __init__(self, nome: str) -> None:
    self._nome = nome
    self._esami = dict()	
```

Inizializza il nome e un dizionario vuoto per registrare gli esami.

##### Inizializzazione "interna" degli attributi
Questa pratica di dichiarare gli attributi prima del costruttore `__init__()` rispecchia perfettamente la logica della progettazione a oggetti e aggiunge una serie di vantaggi:

#### Caratteristica 
- **Tipizzazione chiara e specifica** degli attributi `_nome` e `_esami`.
- Gli attributi sono **[[Public, Private and Class Attibutes, Class and Static Methods#Attributi privati|privati]] per convenzione** (underscore iniziale). 
- Il dizionario `_esami` viene **sempre inizializzato vuoto** all’interno del costruttore.
Di conseguenza l'utente della classe non può inserire esami direttamente alla creazione, il che riflette l'idea che gli esami non siano noti alla nascita (come è indicato nel commento) [[Impl Resp Singola.png|poichè rispetta il vincolo di molteplicità `0..*`]].
In sostanza questa pratica rende più sicuri gli attributi perché il controllo è completamente nella classe: quindi non ci saranno esami "malformati" passati dall'esterno.

> [!success] **Quando usare questa pratica**
> - ==Quando vuoi garantire che l’oggetto venga costruito **con certe condizioni iniziali fisse**.==
 >   
>- ==Quando vuoi mantenere il controllo interno sulla **gestione degli attributi**.==
 >   
>- ==Quando _gli esami devono essere aggiunti successivamente con appositi metodi_.==


> [!abstract]- Differenza tra l'inizializzazione interna degli attributi vs. inizializzazione degli attributi nel costruttore
> Questa pratica vista finora è la buona pratica di programmazione in Python quando si lavora con le classi e i loro attributi, tuttavia fino a poco tempo fa si inizializzavano gli attributi nel costruttore stesso della classe.
> Anche questa seconda pratica non è sbagliata ma presenta alcune differenze fondamentali con la prima pratica:
> **1. Dichiarare gli attributi prima del costruttore**
>```python
> class Studente:
 >   _nome: str
  >  _esami: dict[Modulo, _esame]
>
 >   def __init__(self, nome: str) -> None:
 >       self._nome = nome
 >       self._esami = dict()
>```
>
>>[!done]  Vantaggi
>>- **Documenta l’interfaccia della classe**: 
>> 	 ==chi legge la classe sa subito quali attributi avrà ogni oggetto.==
 >> 
>>-  **Tipizzazione statica (type hints)**: 
>> 	 ==gli strumenti come **mypy**, **Pyright** o **IDE (es. PyCharm)** possono rilevare errori prima di eseguire.==
 >>   
>>-  **Più robusto nei progetti grandi o collaborativi**: 
>> 	 aiuta a evitare refusi e inconsistenze nei nomi.
 >>   
>>-  Può essere usato da strumenti automatici per la generazione di documentazione.
>>  - **Più facile da mantenere e refactorare**.
>>    
>>  - **Evita errori comuni:** 
>>     come ad esempio `self.nomee = nome`
>  
> ==L'unico limite di questa pratica è che non crea davvero le variabili: cioè queste non vengono inizializzate nell'`__init__`.== 
> In questo modo è come dire che: " Ogni istanza di `Studente` avrà questi attributi con questa tipizzazione, garantito".
> Difatti in questo modo si sta dichiarando le intenzioni della classe e facilitandone la lettura a strumenti e collaboratori.
> Quindi quando si dichiarano gli attributi prima del costruttore vuol dire in sostanza che quel attributo viene condiviso tra tutte le istanze di quella classe
>```python 
>class Prova:
  >  nome = "pippo"  # attributo di classe condiviso tra tutte le istanze
>x = Prova()
>y = Prova()
>print(x.nome, y.nome)  # pippo pippo
>x.nome = "pluto"       # x ora ha un suo attributo d’istanza!
>print(x.nome, y.nome)  # pluto pippo
>```
>Se si assegna direttamente nella definizione della classe,  si sta creando un **attributo di classe**. Tutte le istanze condividono lo stesso valore **finché non lo sovrascrivono**.
 >Se invece modifichi x.nome, Python crea un nuovo attributo d’istanza per x, che oscura l’attributo di classe.
> 
> **2. Dichiarare e inizializzare gli attributi solo nel costruttore**
>```python 
>class Studente:
 >   def __init__(self, nome: str, esami: dict):
 >       self._nome = nome
 >       self._esami = esami
>```
>
>>[!done] **Vantaggi**
>> - **Più compatto**
>> - **Più flessibile e utile** quando ==non si sa in anticipo quali attributi avrà la classe o quando se vuole costruirli in base a condizioni.==
>
>
>> [!fail] **Svantaggi**
>>  - **Meno chiaro:**
>> 	   ==Non si sa facilmente quali attributi avrà l'oggetto leggendo solo la definizione della classe==
>>  - **Niente type checking anticipato:**
>>      ==Aumenta la possibilità di riscontrare errori sui nomi o sui tipo che possono comparire **solo a runtime.**==
>> - **Gli strumenti non sanno cosa "aspettarsi":**
>>     ==Da parte degli strumenti di analisi e IDE vi è un supporto minore per quanto riguarda l'autocomplete, linting e refactoring automatico.==  
>Quindi a differenza del primo esempio di assegnazione diretta della classe (attributo di classe), l'inizializzazione dentro il costruttore:
>```python
>class Persona:
  >  def __init__(self, nome):
 >       self.nome = nome  # attributo d'istanza
>
>persona1 = Persona("Luca")
>print(persona1.nome)  # Luca
>```
>Questo sta a significare che `nome` è un attributo d'istanza: cioè appartiene all'oggetto `persona1`
>
>>[!tip] **Consiglio Pratico**
>> - ==Usa la dichiarazione **prima del costruttore** quando vuoi scrivere **codice pulito, tipizzato e manutenibile**.==
 >>   
>>- ==Riservati l’inizializzazione solo nel costruttore se stai facendo qualcosa di molto dinamico o sperimentale.==

### I getter e i setter della classe `Studente`
Definiamo i getter e i setter della classe `Studente`:
```python
def nome(self) -> str:

        return self._nome

  

    def set_nome(self, nome: str) -> None:

        self._nome = nome

  

    def esami(self) -> frozenset[_esame]:

        return frozenset(self._esami.values())

  

    def esame(self, modulo: Modulo) -> _esame:

        return self._esami[modulo]
```

**Spiegazione:**
- `def nome(self) -> str: return self._nome`:  
	 
	 [[Le Classi#**Gestione degli Attributi con Getter e Setter**|Restituisce il valore]] dell'attributo privato `_nome` dell'istanza
	   
- `def set_nome(self, nome: str) -> None:  self._nome = nome`:
	  
	[[Le Classi#**Gestione degli Attributi con Getter e Setter**|Imposta]] l'attributo privato `_nome` con il valore passato come argomento.
	  
- `def esami(self)->frozenset[_esame]: return frozenset(self._esami.values()`:
	 Restituisce un `frozenset` contenente tutti gli oggetti [[`_esame`]] ([[Impl Resp Singola.png|derivati dalla association class]]). 
	 L'uso di `frozenset` garantisce l'immutabilità del set, impedendo modifiche accidentali come l'aggiunta o la rimozione di esami.
	 Inoltre  il metodo [`.values()`](https://www.w3schools.com/python/ref_dictionary_values.asp)viene usato per ottenere solo i valori (cioè gli oggetti `_esame`) del dizionario `_esami`.
	 
- `def esame (self,modulo:Modulo)->_esame: return self._esami[modulo]`:
	  Restituisce l'oggetto `_esame` associato al `modulo` passato come argomento.  
     ==In particolare, accede al dizionario `_esami` usando il `modulo` come chiave.== 
	  ^DefEsame
  

       

        
#### I metodi della classe `Studente`
##### Il metodo `add_esame()`
Dopodiché siccome la responsabilità è di `Studente` verso la classe `Modulo`, si aggiunge il primo metodo, ovvero quello che consente di aggiungere gli esami sostenuti dallo studente relativi a quel modulo:
```python
def add_esame(self, modulo: Modulo, voto: int) -> None:
	 # # ci assicuriamo che in self._esami non ci sia già un esame del modulo 'modulo'

        #Todo assicurarsi che in self._esami non ci sia già un esame del modulo 'modulo'

    ''' NON HO BISOGNO DI FARE IL CICLO!

        for link in self.esami():

            if link.modulo() == modulo:

                raise ValueError(f"Lo studente {self.nome()} ha già superato il modulo {modulo.codice()}")'''

        if modulo in self._esami:

            raise KeyError(f"Lo studente {self.nome()} ha già superato il modulo {modulo.codice()}")

  

        l: _esame = _esame(self, modulo, voto)

        self._esami[modulo] = l
```

Il controllo ` if modulo in self._esami` effettua il controllo nel dizionario `_esami` per vedere se il modulo (ovvero la chiave ) è già presente: 
==Se il modulo è già presente tra gli esami dello studente (`self._esami`), viene sollevata un'eccezione `KeyError` per segnalare che lo studente ha già superato quel modulo.==
In caso contrario  viene creato un nuovo oggetto di `_esame` (`l`) e viene assegnato come valore della chiave `modulo` nel dizionario `self._esami`. 
Questo è perfettamente coerente con la responsabilità singola: solo `Studente` crea i suoi esami.

##### Il metodo `remove_esame()`
Il prossimo metodo permette di rimuove un esame specifico associato a un modulo:
```python
 def remove_esame(self, modulo: Modulo) -> None:

        if modulo not in self._esami:

            raise KeyError(f"Lo studente {self.nome()} non ha superato il modulo {modulo.codice()}!")

        del self._esami[modulo]
```

- Il controllo `if modulo not in self._esami`: controlla che il modulo (cioè la chiave del dizionario `self._esami`) non stia nel dizionario, se non lo trova allora vuol dire che lo studente non ha superato quel modulo e viene, quindi, sollevato un errore di tipo `KeyError`.
- `del self._esami[modulo]`: Se la chiave `modulo` si trova nel dizionario viene eliminata, poiché si intende **rimuovere** l'esame associato a quel modulo (ad esempio in caso di errore o ritiro).

#### Il metodo `media_voti()`
Questo metodo restituisce un `float` che equivale alla media dei voti di esami sostenuti dallo studente in quel modulo.
```python
def media_voti(self) -> float:

        try:

            somma: int = 0

            for esame in self.esami():

                somma += esame.voto()

            return somma / len(self.esami())

        except ZeroDivisionError:

            raise RuntimeError(f"{self.nome()} non ha superato alcun esame, quindi non ha una media!")
```

Il corpo della funzione viene gestito dentro un blocco di `try-except` per catturare e gestire l'eccezione in caso avvenga la divisione per zero.
- `somma`: viene inizializzata una variabile somma uguale a `0`.

- `for esame in self.esami()`: 
	viene usato un ciclo `for` per cui per ogni singolo esame nel dizionario `self._esami` (ovvero per ogni valore del dizionario):
		- `somma+=esame.voto()` : il valore della variabile `somma` si somma al getter `esame()` restituendo il valore del [[voto]].
		- `return somma/len(self.esami())`: infine ritorna la divisione della somma di tutti i voti degli esami relativi al modulo, fratto la lunghezza di [[#^DefEsame|`self.esami`]] ovvero delle chiavi del dizionario `self._esami`.

- `except ZeroDivisionError:  raise RuntimeError(f"{self.nome()} non ha superato alcun esame, quindi non ha una media!"):
	  Questo except gestisce l'errore della divisione per zero, se ciò accade (solo se lo studente non avendo superato/sostenuto nessun esame di quel modulo allora non può avere una media) solleva l'errore di `RuntimeError` se non sono presenti esami. 

#### il metodo speciale `__repr__()`
```python
 def __repr__(self) -> str:

	 return f"Studente({self.nome()})"
```
Questo metodo speciale restituisce una rappresentazione testuale tecnica dell’oggetto, utile per i programmatori, ad esempio durante il debugging.
A differenza del metodo speciale [[Le Classi#Il metodo `__str__`|`__str__()`]] che è pensato per una rappresentazione più leggibile per l’utente finale.
### La classe `Modulo`
```python
class Modulo:

	_codice: str
```

Come per la classe `Studente`, anche qui viene dichiarato un **attributo con tipizzazione** a livello di classe, ma questo serve **solo a scopo documentale** (per IDE e type checker come `mypy`). 
L’attributo effettivo dell’istanza viene inizializzato nel costruttore.

#### Il costruttore, i getter e i setter di `Modulo`
```python
def __init__(self, codice: str) -> None:

        self._codice = codice

  

    def codice(self) -> str:

        return self._codice

  

    def set_codice(self, codice: str) -> None:

        self._codice = codice

  

    def __repr__(self) -> str:

        return f"Modulo({self.codice()})"
```

**Spiegazione:**
- **`__init__()`**: Il costruttore riceve come argomento una stringa `codice`, che viene assegnata all'attributo privato `_codice`. Questo rappresenta il codice identificativo del modulo (es. "INF101", "MAT202", ecc.).
    
- **`codice()`**: Questo è il **metodo getter** che restituisce il valore dell'attributo `_codice`. È utile per accedere al valore rispettando l’incapsulamento.
    
- **`set_codice()`**: Questo è il **metodo setter**, che consente di modificare il valore del codice del modulo. Sebbene in alcuni casi il codice di un modulo non dovrebbe cambiare, questo metodo offre flessibilità nel caso in cui ciò sia necessario.
    
- **`__repr__()`**: Restituisce una rappresentazione testuale **tecnica** dell’oggetto, utile per debugging e logging. Ad esempio, un modulo con codice "INF101" verrà rappresentato come:
```python
Modulo(INF101)
```

### La classe `_esame`:
![[Impl Resp Singola.png|Questa classe è relativa all'associazione di classe]]
Questa classe rappresenta l'associazione tra `Studente` e `Modulo` nel diagramma UML. Serve a modellare il concetto di **esame sostenuto da uno studente in un determinato modulo**, associato a un voto.
```python
class _esame:

    _studente: Studente

    _modulo: Modulo

    _voto: int
```

Come per le altre classi, gli attributi vengono dichiarati **a scopo descrittivo e di supporto alla tipizzazione** (type hinting), ma **l’inizializzazione reale avviene nel costruttore**.

#### Il costruttore, i getter, i setter e i metodi speciali della classe `_esame`
```python
	def __init__(self, studente: Studente, modulo: Modulo, voto: int) -> None:

		self._studente = studente

		self._modulo = modulo

		self._voto = voto

  

	def voto(self) -> int:

		return self._voto

  

	def studente(self) -> Studente:

		return self._studente

  

	def modulo(self) -> Modulo:

		return self._modulo

  

	def __hash__(self) -> int:

		return hash((self._studente, self._modulo))

  

	def __eq__(self, other: Any) -> bool:

		if type(self) != type(other) or hash(self) !=   hash(other):
			return False

		return self.studente() is other.studente() \

            and self.modulo() is other.modulo()

  

	def __repr__(self) -> str:

		return f"{self.studente()} prende {self.voto()} a {self.modulo()}"
```


**Spiegazione:**
**`__init__()`**: Costruttore che riceve tre argomenti:

- uno studente (`Studente`),
    
- un modulo (`Modulo`),
    
- un voto (`int`).

Insieme, rappresentano il fatto che **quello studente ha sostenuto quell’esame in quel modulo** con un certo voto.

**Getter**:

- `voto()`: 
	==restituisce il punteggio ottenuto.==
    
- `studente()`: 
	==restituisce l’oggetto `Studente` associato.==
    
- `modulo()`: 
	==restituisce l’oggetto `Modulo` associato.==

**Metodi speciali:**
- [[Le Classi#La funzione `__hash__(self)`|`__hash__`]] : 
	  Viene usato il metodo hash per generare un hash basato su **studente e modulo**, in modo da poter usare oggetti `_esame` come chiavi in dizionari o membri di insiemi (`set`).  
	  Il voto non contribuisce all’hash perché **non definisce l’identità univoca dell’associazione**.
	  ==Qui si calcola l’hash **basandosi sugli oggetti di `Studente` e di `Modulo`**, quindi se due esami sono relativi **agli stessi oggetti**, il loro hash sarà uguale.==
- [[Le Classi#Il metodo `__eq__(self, other)`|`__eq__`]]: 
	  Viene implementato il metodo `__eq__` per confrontare due oggetti `_esame`.
	  Questi oggetti sono considerati uguali se:
		  - ==Sono della stessa classe e hanno lo stesso hash (quindi stessi oggetti di `Modulo` e `Studente`).==

	- ==E fanno riferimento **agli stessi oggetti** `Studente` e `Modulo` (confronto tramite `is`, cioè identità).==
		
> [!info] In UML, quando un’associazione ha attributi (come il voto in questo caso), è comune rappresentarla come una **classe intermedia** (qui `_esame`), che “lega” due classi (Studenti e Moduli) e aggiunge nuove informazioni.


> [!remember] Perché si usa `is` nel metodo `__eq__()` al posto di \== nella classe Esame
> In python `is` e \== hanno significati diversi ed è una scelta deliberata quella di usare `is` nel metodo `__eq__()` in questo contesto.
> Vediamolo nel dettaglio:
>```python 
> return self.studente() is other.studente() and self.modulo() is other.modulo()
>```
>==In questo caso si vuole verificare che **i due esami si riferiscano esattamente agli stessi oggetti di `Studente` e `Modulo`.**==
>==Quindi non vogliamo confrontare i valori delle istanze (ovvero usando il simbolo \=\=) di queste due classi, ma questi gli oggetti, in questo caso, **devono essere lo stesso oggetto in memoria.**== 
>**Esempio:**
>```python
>s1 = Studente("Mario Rossi")
s2 = Studente("Mario Rossi")  # stesso valore, ma oggetto diverso
>
>print(s1 == s2)  # può essere True se `__eq__` è definito
>print(s1 is s2)  # False, sono due oggetti diversi in memoria 
>```
> Nel contesto di `_esame`, ha senso usare `is` perché:
>
>- ==**Uno studente può avere lo stesso nome ma essere rappresentato da oggetti diversi**.==
 >   
>- **==Un modulo può avere lo stesso codice ma essere istanze distinte.==**
  >  
>- Quindi, per dire che un esame è davvero “lo stesso”, dobbiamo essere certi che si riferisca **agli stessi oggetti**.
>
>> [!example] **In sintesi** 
>> ==`is` garantisce che i riferimenti delle istanze delle classi siano identici, mentre il simbolo 'uguale a'(\=\=) verifica solo che il contenuto (ovvero il valore) delle istanze di una classe sia lo stesso.== 
>> In questo caso della classe `_esame`, ==si vuole un confronto **basato sull'identità degli oggetti associati,** non sui loro valori==

### In conclusione
La classe `_esame` rappresenta perfettamente un esempio di classe di associazione con responsabilità singola nel diagramma UML ristrutturato delle classi:
- ==Serve a **collegare in modo esplicito** due classi (`Studente` e `Modulo`) tramite un’istanza che **incapsula una responsabilità ben definita**: il voto di un esame.==
    
- ==La responsabilità della classe `_esame` è quindi **limitata e chiara**: tracciare un evento (l’esame) che coinvolge due entità (`Studente` e `Modulo`), associandovi un’informazione aggiuntiva, ovvero il `voto`.== 



A questo link trovi il codice completo:
  
[[Studente(associazione responsabilità singola).py]] 
