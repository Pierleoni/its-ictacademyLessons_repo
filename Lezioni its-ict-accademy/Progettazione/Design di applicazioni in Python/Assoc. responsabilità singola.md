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
In sintesi ==permette i riferimenti incrociati anche se le classi sono dichiarate dopo==.

#### La classe `Studente`:
Definiamo degli attributi privati al di fuori del costruttore
```Python
_nome: str
_esami: dict[Modulo, _esame]
```

- `_nome`: nome dello studente.
    
- `_esami`: **collezione di chiave-valore di esami**, **gestita dal lato Studente**. 
  Usa `Modulo` come chiave e l'associazioni `_esame` come valore

Quindi nel costruttore :
```python
def __init__(self, nome: str) -> None:
    self._nome = nome
    self._esami = dict()	
```

Inizializza il nome e un dizionario vuoto per registrare gli esami.
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

Il controllo ` if modulo in self._esami` effettua il controllo nel dizionario `_esami` per vedere se il modulo (ovvero la chiave ) è già presente, 
se il modulo si trova in `self._esami` viene sollevato l'errore di `KeyError`.
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
- `del self._esami[modulo]`: Se la chiave `modulo` si trova nel dizionario viene eliminata, poiché lo studente ha superato quel modulo

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
- `somma`: viene inizializzata una variabile somma uguale a `0`
- `for esame in self.esami()`: 

[[Studente(assoc. resp. singola).py]] 
