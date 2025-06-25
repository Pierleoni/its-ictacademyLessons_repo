# Introduzione

Nella lezione precedente abbiamo introdotto il concetto di [[Associazione a responsabilità singola|associazioni a responsabilità singola]] analizzando il progetto "_Voli Aerei 1_" prendendo ad esempio [[Impl Resp Singola.png|questo diagramma]] UML delle classi:
In questi casi, **una sola delle due classi** coinvolte è responsabile della gestione dell'associazione.

## Associazioni a responsabilità doppia
Ora affrontiamo un caso più articolato: le **associazioni a responsabilità doppia**.

Un associazione a responsabilità doppia e quando non c'è una chiara responsabilità in un unico verso di navigabilità da una classe all'altra, ma quando entrambe le classi sono responsabili dell'associazione.
Quindi in questo tipo di associazioni **entrambe le classi sono responsabili del legame** che le unisce:
non è possibile assegnare la responsabilità in un unico verso (es. da `Studente` a `Modulo` o viceversa).
![[Esempio assoc. a respl. doppia.png]]

Come si può osservare in questo esempio UML, sia la classe `Studente` che la classe `Modulo` sono coinvolte e **partecipano attivamente** alla gestione dell’associazione `esame`.
### Obiettivo: implementare un’associazione a responsabilità doppia
Per capire come tradurre questo schema in Python, analizzeremo un caso concreto:
Il design _Azienda 1_, nel quale vogliamo modellare l’associazione `coinvolto` tra le classi `Impiegato` e `Progetto`.
![[Class Diagram Design Azienda 1.png]]

Questa associazione:

- ha **responsabilità doppia**
    
- ha **molteplicità `0..*` su entrambi i lati** (cioè un impiegato può essere coinvolto in più progetti e viceversa), ed entrambi **_certamente non noti alla nascita_** 

## Scelta progettuale
Ci chiediamo: **come si aggiunge un impiegato a un progetto**?
Potremmo considerare 3 opzioni:
1. `alice.add_progetto(progetto)`
2. `progetto.add_impiegato(alice)`
3. `coinvolto.add(alice,progetto)`
A questo punto dobbiamo decidere se:
- (a) implementare la **prima** opzione
    
- (b) implementare la **seconda**
    
- (c) implementare **entrambe**
    
- (d) implementare una **factory esterna** che gestisca l’associazione

### Opzione d
Scegliamo l’opzione **(d)**: utilizzare una factory chiamata `coinvolto`, che fornisce un’interfaccia centralizzata per creare e gestire i legami tra `Impiegato` e `Progetto`.

Questa scelta è motivata da:

- la necessità di mantenere **sincronizzata** l’associazione da entrambe le parti
    
- la volontà di separare la **logica di collegamento** dalle entità del dominio
    
- l’opportunità di **incapsulare i dati** dell’associazione (`data`, ecc.)
    

In sintesi:

- `coinvolto` rappresenta l’**associazione UML**
    
- all’interno di `coinvolto`, la classe interna `_link` rappresenta ogni **istanza concreta dell’associazione**
    
- la factory `coinvolto` fornisce metodi per **creare (`add`) e rimuovere (`remove`)** questi legami

### La class `coinvolto`

In Python creiamo una classe `coinvolto`, nel seguente modo:

1. Importiamo una serie di moduli
```python
from __future__ import annotations

from datetime import date

from typing import TYPE_CHECKING, Any

  

if TYPE_CHECKING:

    from azienda.impiegato import Impiegato

    from azienda.progetto import Progetto
```

- [[Associazione a responsabilità singola#^fromFuture|`from __future__ import annotations`]] abbiamo gia visto cosa fa nella scorsa lezione.
- `from datetime import date`: questa direttiva importa il dato `date` dal modulo `datetime`.
- `from typing import TYPE_CHECKING`:  questa direttiva è uno strumento di typing statico usato per evitare import circolari o inutili a runtime.
  La costante `TYPE_CHECKING` è definita nel modulo `typing` ed è sempre falsa a runtime, ma vera durante l'analisi statica del codice da parte di strumenti come: mypy,Pyright o IDE come Pycharm o VSCode (che usano l'analisi statica).

> [!abstract] **Come funziona e perché usarlo**
> In questo codice:
>```python
>from typing import TYPE_CHECKING
>
>if TYPE_CHECKING:
 >   from azienda.impiegato import Impiegato
>  from azienda.progetto import Progetto
>```
>Ciò significa che: 
>- Quando si esegue il programma questi import non vengono eseguiti
>- Ma quando si analizza il codice con uno strumento di type-checking (es: mypy), gli import vengono considerati per l'annotazione dei tipi.
>
>**Perché si usa**
>1. Per evitare import circolari
>	  Supponiamo che:
>		- `impiegato.py` importi `Coinvolgimento` (per aggiornare i progetti).
>		
>		- coinvolgimento.py importi Impiegato (per annotare il tipo). 
>  In questo caso si avrebbe un **ciclo:**
>  `impiegato → coinvolto→impiegato` => Questo può portare a errori di runtime.
>  Quindi per ovviare al problema si scrive:
>```python
>  if TYPE_CHECKING:
 >   from azienda.impiegato import Impiegato
>```
>L'import avviene solo durante il controllo dei tipi, non durante l'esecuzione, quindi in questo modo si evita il ciclo e al momento di runtime non viene eseguito evitando anche rallentamenti o errori.
>



2. Dichiariamo la class `coinvolto` e i suoi metodi di classe:
```python
class coinvolto:

  

    @classmethod

    def add(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> _link:

        l = cls._link(progetto, impiegato, data)

        progetto._add_link_coinvolto(l)

        impiegato._add_link_coinvolto(l)

        return l # restituisco il link appena creato, per comodità di utilizzo

  

    @classmethod

    def remove(cls, l: _link) -> None:

        l.progetto()._remove_link_coinvolto(l)

        l.impiegato()._remove_link_coinvolto(l)

        del l   # devo cancellare il link
```

Questo codice implementa una classe di gestione dell'associazione a responsabilità doppia tra `Progetto` e `Impiegato`, usando un classe intermedia chiamata `_link` .

Contiene due metodi di classe:
2.2) Metodo `add`:
	==Crea un oggetto `_link` che rappresenta il collegamento tra un `Progetto` e un `Impiegato` a partire da una data, e aggiorna entrambe le classi (`progetto` e `impiegato`) per **registrare questa relazione**.==
Vediamolo in dettaglio step per step:
	
```python
l = cls._link(progetto, impiegato, data)
```

- Crea un Crea un nuovo oggetto della classe  `_link` con i dati dell'associazione.

```python
progetto._add_link_coinvolto(l)
impiegato._add_link_coinvolto(l)
```

Aggiunge il collegamento agli attributi interni  di `progetto` e `impiegato`.

```python
return l
```
- Ritorna il link per comodità: in futuro lo si può usare per rimuovere l’associazione.

  2.3) Metodo `remove`:
  ==Rimuove un collegamento `_link` precedentemente creato, **interrompendo l'associazione** tra il `Progetto` e l'`Impiegato`.==

Vediamo in dettaglio step per step:
```python
l.progetto()._remove_link_coinvolto(l)
l.impiegato()._remove_link_coinvolto(l)

```

- ==Rimuove il collegamento dagli oggetti coinvolti.==  
  ==Notare che `progetto()` e `impiegato()` sono due getter che restituiscono i riferimenti agli attributi `self._progetto` e `self._impiegato` inizializzati nella classe `_link` che vedremo poco più avanti==.

```python
del l
```
- Il collegamento viene esplicitamente cancellato.

In sostanza la class `coinvolto` rappresenta l'associazione tra `Progetto` e `Impiegato`, separando la logica dell'associazione dalle entità stesse.



#### La class `_link`

Ora aggiungiamo una class `_link` all'interno della class factory `coinvolto`:  
==la class `_link` rappresenta l’**istanza concreta** dell’associazione UML `coinvolto`.==

==In termini concettuali, si tratta di un **oggetto associativo**, ovvero una struttura che incarna un legame **bidirezionale** tra un `Impiegato` e un `Progetto`, a una certa **data**.==

Questa inner class è **completamente gestita** dalla factory `coinvolto`:

- non viene mai istanziata direttamente;
    
- viene costruita dal metodo `coinvolto.add(...)`;
    
- viene distrutta dal metodo `coinvolto.remove(...)`.
    

Gli attributi (_impiegato, _progetto, _data) sono **immutabili e noti alla nascita**, cioè fissati una volta sola nel costruttore.  
La classe implementa anche i metodi `__eq__` e `__hash__` per poter confrontare i legami ed evitarne la duplicazione.


> [!NOTE] **Nota: la class factory**
> Da notare come la class Python `coinvolto`, ora che è stata dichiarata una nuova classe al suo interno diventi e agisca a tutti gli effetti come una **class factory:**
> ==cioè una classe che non viene mai istanziata, ma fornisce solo metodi di classe (`@classmethod`) per creare e gestire oggetti associativi.==
> 
>> [!summary] Cos'è una class factory
>> Una class factory è una classe che:
>> - non viene mai istanziata direttamente
>> - serve esclusivamente a produrre altre istanze (di solito di una inner class o helper class).
>> - Spesso incapsula la logica di **costruzione, validazione o gestione condivisa** degli oggetti generati. 
>>  
>>  **Quindi, perché `coinvolto` è una class factory**
>>  1. ==Nessun `__init__` definito nella classe `coinvolto`, quindi questa classe non è pensata per essere istanziata.==
>>  2. ==Contiene solo metodi di classe (`@classmethod`)==:
>>```python
>> @classmethod
>> def add(cls,progetto, impiegato, data):
>> 	
>> @classmethod
>> def remove(cls,l)
>>```
>>
>>Quindi tutte le sue funzioni operano a livello di classe
>>3. ==Genera oggetti della inner class `_link`==:
>>```python
>>l = cls._link(progetto, impiegato, data)
>>  
>>```
>>4. ==Incapsula l'intera logica di costruzione, collegamento e distruzione degli oggetti `_link`.==
>
>
>
>> [!abstract]- Differenza tra le factory class e le classi astratte
>> Detto questo, per maggiore chiarezza le **class factory** e le [[Classi astratte|classi astratte]] differiscono per finalità:
>>
>>- ==La **classe astratta** rappresenta un **tipo concettuale incompleto**, cioè una generalizzazione **non direttamente istanziabile**==.  
 >>   Immaginiamo un diagramma delle classi con due sottoclassi `Studente` e `Lavoratore` che ereditano da `Persona`, con vincolo `{disjoint, complete}`.   
>>
>>> [!caution] ❗ ==In UML, `{complete}` indica che **ogni istanza della superclasse è anche istanza di una sottoclasse**:==  
>>> ==cioè **tutti gli oggetti `Persona` sono o `Studente` o `Lavoratore`**==.
>>
>>- Tuttavia, **in Python un oggetto non può cambiare classe dopo la creazione**. Questo implica che:
>>    
 >>   - ==una volta creato come `Studente`, un oggetto **non può diventare** `Lavoratore`==
  >>      
 >>   ==- e viceversa.==
>>        
>>
>>✳ Per questa ragione, **spesso si evita `{complete}`** nelle generalizzazioni UML quando si implementa in Python, e si considera la superclasse (`Persona`) come **classe astratta**, cioè un tipo comune che:
>> 
>> - ==definisce metodi astratti (interfaccia)==
>>     
>> - ==**non viene mai istanziato direttamente**==
>>     
>> - ==obbliga le sottoclassi (`Studente`, `Lavoratore`) a implementare determinati comportamenti.==
>>   
>>   
>> MMentre una **class factory**, come abbiamo detto prima, ha lo scopo di:
>>
>>- ==creare e costruire oggetti==
>>  
>>- ==non rappresentare un'entità del dominio (ma una logica di costruzione)==
>>  
>>- ==spesso non viene mai istanziata==
>>  
>>
>>Infatti, in questo contesto (associazione `coinvolto` tra `Impiegato` e `Progetto`) si usa una **classe factory** perché:
>>
>>- ==**non si sta modellando un tipo**, come nel caso delle classi astratte (`Persona`, `Veicolo`, `Animale`...)==
>>  
>>- si sta invece **modellando una relazione tra due oggetti**, che:
>>    
>>   - ==può essere **creata e rimossa dinamicamente**==
>>        
>>    - ==ha **attributi propri** (`data`)==
>>        
>>   - ==deve essere gestita **in modo centralizzato** per tenere coerenti entrambi i lati (`Impiegato` ↔ `Progetto`)==
>>        
>>- ==la relazione stessa è rappresentata da un oggetto (`_link`), ma la **logica di costruzione è incapsulata** nella factory `coinvolto`.==
>>   
>>
>>In altre parole, **si usa una class factory invece di una classe astratta** perché:
>>
>>1. ==La class `coinvolto` **non rappresenta una classe del dominio**, ma un’associazione tra entità.==
>>    
>>2. ==Serve a **gestire e controllare il ciclo di vita dei link** (creazione, registrazione, rimozione).==
>>    
>>3. ==È coerente con la semantica UML di **associazione a responsabilità doppia** e con l'approccio Pythonico alla modularità.==


##### Vantaggi di usare una class Factory in questo contesto

| Vantaggio                        |                                          Descrizione                                          |
| -------------------------------- |:---------------------------------------------------------------------------------------------:|
| Separazione delle responsabilità |              L'associazione viene gestita **fuori** da `Impiegato` e `Progetto`               |
| Codice centralizzato             |                  Tutta la logica di creazione/rimozione è in un unico punto.                  |
| Coerenza con UML                 |     L’associazione è modellata come **classe autonoma**, proprio come nel diagramma UML.      |
| Manutenzione più facile          | Se in futuro cambiano i vincoli o gli attributi della relazione, si modifica una sola classe. |
| Possibilità di estensione        |          Si possono aggiungere metodi di ricerca, serializzazione, validazione, ecc.          |
Tornando all'implementazione della class `_link`:
1. Dichiariamo la classe
```python
class _link:
```

Definizione della _class Python_ `_link`, annidata nella _class factory_ `coinvolto`.  
Il nome `_link` è prefissato da underscore per indicare che **è un oggetto interno**, non destinato all’uso diretto all’esterno (convenzione Python per l’**uso interno**).

2. Definiamo le annotazioni di tipo 
```python
    _impiegato: 'Impiegato'     # ovviamente immutabile, noto alla nascita
    _progetto: 'Progetto'       # ovviamente immutabile, noto alla nascita
    _data: date                 # immutabile, noto alla nascita

```

 Questi sono **attributi d’istanza** della classe:
  - `_impiegato`: riferimento all’oggetto `Impiegato` coinvolto
     
 - `_progetto`: riferimento all’oggetto `Progetto` coinvolto
     
 - `_data`: oggetto di tipo `date` (modulo `datetime`), che rappresenta **la data di inizio coinvolgimento.**
 
     
 
 La nota `"immutabile, noto alla nascita"` significa che:
 
 - questi dati **vengono fissati nel costruttore (`__init__`)**
     
 - **non cambiano mai** nel corso della vita dell’oggetto `_link` (immutabilità logica)
     

3. Inizializziamo gli attributi nel costruttore `__init__()`:
```python
    def __init__(self, progetto: Progetto, impiegato: Impiegato, data: date) -> None:
        self._impiegato = impiegato
        self._progetto = progetto
        self._data = data

```

- Assegna i riferimenti alle istanze `Impiegato` e `Progetto` e alla `data`
    
- Viene **chiamato solo dalla factory `coinvolto.add()`**, quindi la costruzione è **centralizzata** (pattern factory).
  Di conseguenza l'utente finale non ha accesso diretto alla creazione di `_link`.
    

Questo oggetto `_link` **rappresenta l’associazione concreta** tra un certo impiegato e un certo progetto, a una certa data.

4. Implementiamo i metodi getter di questa classe:
```python
    def impiegato(self) -> 'Impiegato':
        return self._impiegato

    def progetto(self) -> 'Progetto':
        return self._progetto

    def data(self) -> date:
        return self._data

```

- `def impiegato(self) -> 'Impiegato':return self._impiegato`: 
	restituisce l’oggetto `Impiegato` associato.  
	==Notare: **non esiste un setter** → il riferimento è **immutabile**.==  
  ^getProgetto
  
- `def progetto(self) -> 'Progetto':return self._progetto`:
	restituisce l’oggetto `Progetto` associato  
-     `def data(self) -> date:return self._data`: 
	 restituisce la data dell’associazione

5. Implementazione dei metodi speciali:
```python
    def __hash__(self) -> int:
        return hash((self.impiegato(), self.progetto()))
```

Questo metodo consente di **usare `_link` come elemento di un `set` o come chiave di un `dict`**.  
L’hash è calcolato sulla **coppia `(impiegato, progetto)`**, ignorando la `data` → due `_link` con stessi impiegato e progetto ma date diverse saranno **considerati duplicati**.

```python
    def __eq__(self, other: Any) -> bool:
        if type(other) != type(self) \
           or hash(self) != hash(other):
            return False
        return (self.impiegato(), self.progetto()) == (other.impiegato(), other.progetto())

```

Ridefinisce il comportamento di confronto di uguaglianza (\=\=) tra due oggetti `_link`:

- Prima controlla che siano dello stesso tipo e abbiano lo stesso hash
    
- Poi confronta effettivamente la coppia `(impiegato, progetto)`
    

Anche qui la `data` **non viene considerata**: questo conferma che **due `_link` sono uguali se legano gli stessi due oggetti, indipendentemente dalla data**.  
(Questo potrebbe essere un vincolo di progetto: es. non può esistere un impiegato coinvolto più volte nello stesso progetto.)


> [!example] In Conclusione
> La _class Python_ `_link` è:
>
>- un **oggetto associativo** che incarna la relazione `coinvolto` tra `Impiegato` e `Progetto`
 >   
>- completamente **gestita dalla class factory** `coinvolto`
  >  
>- **immutabile**, con stato fisso al momento della creazione
  >  
>- **comparabile e hashabile**, per poter gestire insiemi di associazioni senza duplicati
 

### La class `Impiegato` 
La class `Impiegato` rappresenta, in Python, la **classe concreta** `Impiegato` del diagramma UML.  
Modella un’entità del dominio, che descrive i **dati personali e contrattuali** di un impiegato.

Dopo aver implementato la class factory `coinvolto` e la inner class `_link`, dobbiamo fornire in `Impiegato` i metodi necessari per **gestire localmente** i legami associativi.  
Questi metodi permettono di **registrare** e **rimuovere** un impiegato da un progetto, mantenendo **sincronia con la controparte `Progetto`**, secondo la logica definita centralmente dalla factory `coinvolto`.

==In questo caso, i metodi seguenti sono progettati per essere **chiamati esclusivamente dalla factory** e **non utilizzati direttamente** all’esterno.== 

1. Import e Forward Declaration:
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from azienda.coinvolto import coinvolto
    from azienda.progetto import Progetto
from custom_types import RealGEZ
from datetime import date
```

- `TYPE_CHECKING` evita **import ciclici** durante l'esecuzione del codice.
    
- I moduli `coinvolto` e `progetto` vengono importati **solo per i type hint**, cioè per aiutare strumenti statici e IDE.
    
- `RealGEZ`:  un tipo di dato specializzato definito a parte che è un `float >= 0`.

2. Attributi e costruttore:
```python
_nome: str
_cognome: str
_nascita: date
_stipendio: RealGEZ
_progetti: dict['Progetto', 'coinvolto._link']
```

- I primi 4 attributi rappresentano **dati immutabili o modificabili singolarmente**.
    
- `_progetti`: collezione dei progetti a cui l’impiegato è assegnato.  
    È un dizionario:
    
    - chiave = oggetto `Progetto`
        
    - valore = oggetto `_link` dell’associazione `coinvolto`.

3. Costruttore:
```python
def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
    self.set_nome(nome)
    self.set_cognome(cognome)
    self._nascita = nascita
    self.set_stipendio(stipendio)
    self._progetti = dict()
```

- Usa setter per `nome`, `cognome` e `stipendio` per centralizzare eventuali validazioni.
    
- Inizializza `_progetti` come dizionario vuoto, poiché i collegamenti saranno aggiunti in seguito **tramite la class factory `coinvolto`**.

4. Getter e setter di base:
```python
def nome(self) -> str: return self._nome
def cognome(self) -> str: return self._cognome
def nascita(self) -> date: return self._nascita
def stipendio(self) -> RealGEZ: return self._stipendio

def set_nome(self, nome: str) -> None: self._nome = nome
def set_cognome(self, cognome: str) -> None: self._cognome = cognome
def set_stipendio(self, stipendio: RealGEZ) -> None: self._stipendio = stipendio

```

- `nascita` non ha un setter: è **immutabile**, come da nota UML.
    
- Gli altri campi possono essere modificati, ma solo tramite metodi espliciti.

Ora analizziamo i metodi connessi all’associazione `coinvolto`, tenendo presente la factory `coinvolto`: 
nella factory class, avevamo implementato questo codice
```python
@classmethod
def add(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> _link:
    l = cls._link(progetto, impiegato, data)
    progetto._add_link_coinvolto(l)
    impiegato._add_link_coinvolto(l)
    return l
```

`coinvolto.add(...)` genera un nuovo `_link` e lo registra sia nel progetto che nell’impiegato.  
I metodi seguenti sono quelli **chiamati internamente** da questa factory.

Di conseguenza ora nella class `Impiegato` si deve aggiungere 2 metodi:
5. `_add_link_coinvolto()`: 
==Aggiunge un'associazione tra questo `Impiegato` e un `Progetto` tramite un oggetto `_link`.== 

```python
def _add_link_coinvolto(self, l: 'coinvolto._link') -> None:
    if l.impiegato() != self:
        raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
    if l.progetto() in self._progetti:
        raise KeyError(f"L'impiegato è già coinvolto nel progetto {l.progetto()}")
    self._progetti[l.progetto()] = l
```
**Spiegazione:**
- **Controllo di coerenza**:  
    Il metodo verifica che `l.impiegato()` sia proprio `self` → evita errori logici nell'associazione.
    
- **Controllo di unicità**:  
    Se `self._progetti` contiene già `l.progetto()` come chiave, solleva `KeyError` → impedisce **duplicazioni** del legame impiegato-progetto.
    
- **Registrazione del link**:  
    Aggiunge il nuovo `_link` al dizionario `_progetti`, usando come chiave il progetto.


> [!NOTE] Questo metodo è **invisibile all’utente**: viene usato **esclusivamente dalla factory `coinvolto.add(...)`**.


6. `_remove_link_coinvolto`:

==Rimuovere il legame (associazione `coinvolto`) tra `self` e un progetto.==

```python
def _remove_link_coinvolto(self, l: 'coinvolto._link') -> None:
    if l.impiegato() != self:
        raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
    if l.progetto() not in self._progetti:
        raise KeyError(f"L'impiegato {self.nome()} non era coinvolto nel progetto {l.progetto()}")
    del self._progetti[l.progetto()]
```

**Spiegazione:**
- **Controllo di coerenza**:  
    Verifica che il link faccia effettivamente riferimento a `self`.
    
- **Controllo di esistenza**:  
    Solleva errore se il progetto non è presente nella mappa `_progetti`.
    
- **Rimozione**:  
    Cancella la chiave `l.progetto()` → elimina il legame. 

> [!NOTE] Questo metodo è chiamato **dalla factory `coinvolto.remove(l)`**, che si occupa anche di rimuoverlo dalla controparte `Progetto`.

7. `def progetti()`:
==Esporre in lettura **l’insieme dei progetti associati** a questo `Impiegato`.==

```python
def progetti(self) -> frozenset['coinvolto._link']:
    return frozenset(self._progetti.values())
```
**Spiegazione:**

- ==Utilizza `frozenset` → **immutabile**, impedisce modifiche accidentali da parte dell’esterno.==
    
- ==Restituisce un set di oggetti `_link`, ognuno dei quali rappresenta un legame tra questo `Impiegato` e un `Progetto`.==


> [!info] È il metodo più diretto per ottenere **tutte le collaborazioni attive** di un impiegato.



8. `is_coinvolto(progetto)`:
==Verificare se l’impiegato è attualmente assegnato a un certo progetto.==

```python
def is_coinvolto(self, progetto: 'Progetto') -> bool:
    return progetto in self._progetti
```
**Spiegazione:**
- Controlla se `progetto` è presente tra le chiavi del dizionario `_progetti`.
    

Molto utile per validazioni condizionali (es. evitare doppi inserimenti).


9. `data_coinvolgimento(progetto)`:
==Recuperare la data in cui è iniziata l'associazione con un certo progetto.== 

```python
def data_coinvolgimento(self, progetto: 'Progetto') -> date:
    if progetto not in self._progetti:
        raise ValueError(f"L'impiegato non è coinvolto nel progetto {progetto.nome()}")
    return self._progetti[progetto].data()
```

**Spiegazione:**
- ==Se il progetto non è tra quelli registrati, solleva un errore.==
    
- ==Altrimenti, ottiene l’oggetto `_link` e chiama `.data()` su di esso.== 

Consente di trattare la relazione come **oggetto con attributi**, non solo presenza/assenza.

10. Metodo `__str__`:
==Definire una rappresentazione stringa leggibile dell’oggetto `Impiegato`.==

```python
def __str__(self) -> str:
    return (f"{self.nome()} {self.cognome()}, "
            f"nascita: {self.nascita()}, "
            f"stipendio: {self.stipendio()}")
```

- Fornisce una rappresentazione leggibile dell’impiegato.
    
- Utile per debug, stampa o report.
**Esempio di output:**
```shell
Alice Rossi, nascita: 1990-05-10, stipendio: 2300.0
```


> [!link] Collegamento diretto alla [[#La class `coinvolto`|class factory `coinvolto`]]
> Quando si chiama:
>```python
coinvolto.add(progetto1, alice, date(2024, 1, 10))
>```
>Quello che succede è:
>- Viene creato un oggetto `_link` (interno alla factory).
> 
>- `progetto1._add_link_coinvolto(l)` registra il legame nella classe `Progetto`.
>  
>- `alice._add_link_coinvolto(l)` registra il legame in `Impiegato`.
>>[!remember] Questo garantisce **sincronizzazione bidirezionale**, in linea con il diagramma UML a **responsabilità doppia**.

### La class `Progetto`

La class `Progetto` rappresenta, in Python, la **classe concreta** `Progetto` definita nel diagramma UML.  
Come per la class `Impiegato`, anche questa class modella un’entità del dominio applicativo.

Partecipa all’associazione binaria `coinvolto`, che collega `Impiegato` e `Progetto`, e la cui gestione è demandata alla **class factory** `coinvolto`.  
Questa factory si occupa di **creare**, **registrare** e **rimuovere** i legami associativi, rappresentati da oggetti della inner class `_link`.

==Anche in questo caso, i metodi che seguono sono pensati per essere **utilizzati internamente** dalla factory `coinvolto`, al fine di garantire la **sincronia e la coerenza** tra le due estremità dell’associazione (`Impiegato` ↔ `Progetto`).== 


1. Attributi di `Progetto`:
```python
_nome: str                      # noto alla nascita
_budget: RealGEZ               # noto alla nascita
_impiegati: dict[Impiegato, coinvolto._link] # da associazione 'coinvolto', con vincolo di molteplicità [0..*]
```
- `_nome`, `_budget`: attributi **immutabili**, fissati nel costruttore.
    
- `_impiegati`: dizionario che registra tutti gli impiegati **coinvolti nel progetto**, con il rispettivo oggetto `_link` della factory `coinvolto`.

2. Costruttore `__init__()`:
```python
def __init__(self, nome: str, budget: RealGEZ) -> None:
    self._nome = nome
    self._budget = budget
    self._impiegati = dict()
```

- Inizializza nome e budget.
    
- Crea un dizionario vuoto per registrare i link di coinvolgimento con gli impiegati.

3. Getter Standard:
```python
	def nome(self) -> str:
		return self._nome

  
	def budget(self) -> RealGEZ:
		return self._budget

  
def get_nome(self) -> str:
	return self._nome

	def get_budget(self) -> RealGEZ:
		return self._budget
```

- Forniscono accesso controllato ai dati interni.
    
- Doppia versione (`nome` e `get_nome`) per compatibilità o preferenza stilistica (non strettamente necessaria).

4. `_add_link_coinvolto(self,l)`:

==Registra un impiegato coinvolto in questo progetto.==

```python
def _add_link_coinvolto(self, l: coinvolto._link) -> None:
    if l.progetto() != self:
        raise ValueError(...)
    if l.impiegato() in self._impiegati:
        raise KeyError(...)
    self._impiegati[l.impiegato()] = l

```


> [!link] Collegamento con `coinvolto.add()`
>Nel metodo della class factory `coinvolto`:
>```python
>progetto._add_link_coinvolto(l)
>```
>viene chiamato per registrare nel `Progetto` l’oggetto `_link` appena creato.

**Spiegazione:**
- **Controllo di coerenza**:
	  ==Verifica che il `progetto()` contenuto nel `link` sia proprio `self`(cioè il progetto corretto).==
    
- **Verifica di unicità**:
	  ==impedisce che lo stesso `Impiegato` venga coinvolto più volte nello stesso `Progetto`.==
    
- **Registrazione del legame**:
	  ==Inserisce l’oggetto `_link` nel dizionario `_impiegati`, con chiave l’impiegato..==


5. `_remove_link_coinvolto(self, l)`:

==Elimina l’associazione con un impiegato.==

```python
def _remove_link_coinvolto(self, l: coinvolto._link) -> None:
    if l.progetto() != self:
        raise ValueError(...)
    if l.impiegato() not in self._impiegati:
        raise KeyError(...)
    del self._impiegati[l.impiegato()]
```


> [!link] Collegamento con `coinvolto.remove()`
> nel metodo factory:
>```python
> progetto._remove_link_coinvolto(l)
>```
>Viene chiamato per aggiornare la parte “progetto” rimuovendo il legame.

**Spiegazione:**
- **Controlla che il `link` sia coerente** (ossia che faccia riferimento a `self`).
    
- **Verifica che l’impiegato fosse effettivamente registrato** nel dizionario `_impiegati`.
    
- **Rimozione** del collegamento dal dizionario.

6. `impiegati(self)` :
```python
def impiegati(self) -> frozenset['coinvolto._link']:
    return frozenset(self._impiegati.values())

```

**Spiegazione:**
==Restituisce un **insieme immutabile** degli oggetti `_link` che collegano questo progetto agli impiegati.==

- Fornisce una **vista esterna** sull’associazione.
    
**Utilità:**

Permette, ad esempio, di iterare sugli impiegati coinvolti accedendo anche alla data di coinvolgimento tramite gli oggetti `_link`.

7. `is_coinvolto(self, impiegato)`:
```python
def is_coinvolto(self, impiegato: Impiegato) -> bool:
    return impiegato in self._impiegati
```

**Spiegazione:**
==Verifica se l’impiegato specificato è già coinvolto in questo progetto.==

-  È utile per evitare doppie associazioni e per validazioni.

8. `data_coinvolgimento(self, impiegato)`:
```python
def data_coinvolgimento(self, impiegato: Impiegato) -> date:
    if impiegato not in self._impiegati:
        raise ValueError(...)
    return self._impiegati[impiegato].data()
```

**Spiegazione:**
==Restituisce la data di coinvolgimento per un dato impiegato.==

- Se l’impiegato non risulta coinvolto, solleva un’eccezione (`ValueError`).
    
- Altrimenti, accede al link per restituire l’informazione desiderata.

9. `__str__` e `__repr__`:

```python
def __str__(self) -> str:
    return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

def __repr__(self) -> str:
    return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"
```

**Spiegazione:**
- `__str__`: rappresentazione leggibile per l’utente.
    
- `__repr__`: rappresentazione più “tecnica” per debugging o console interattiva.


> [!link] Riepilogo rapporto con [[#La class `coinvolto`|la factory `coinvolto`]]
> Quando si chiama:
>```python
> coinvolto.add(progetto1, alice, date(2024, 5, 10))
>
>```
>il processo è il seguente:
>
>1. La factory `coinvolto` crea un oggetto `_link` che rappresenta il legame.
>   
>2. Il metodo `_add_link_coinvolto` viene chiamato sia su `progetto1` che su `alice`:
>    
>    - `progetto1._add_link_coinvolto(l)`
>        
>    - `alice._add_link_coinvolto(l)`
>        
>3. Entrambe le estremità della relazione sono aggiornate in modo **sincrono e coerente**.

Questa progettazione consente di **centralizzare la gestione dell’associazione** e **mantenere la consistenza** tra gli oggetti coinvolti.




