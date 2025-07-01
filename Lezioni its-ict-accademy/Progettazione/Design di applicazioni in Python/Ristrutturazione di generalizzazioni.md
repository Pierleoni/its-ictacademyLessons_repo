# Introduzione 
In questa lezione vediamo come **ristrutturare le generalizzazioni** nel passaggio dal **diagramma UML concettuale** al **diagramma UML ristrutturato**, in vista dell’implementazione in Python.

### Obiettivo

Il diagramma ristrutturato **non deve contenere**:

1. **Generalizzazioni non disgiunte** tra classi o associazioni  
    → In Python, **un oggetto può appartenere a una sola classe concreta**:  
    ==non è possibile avere un’istanza che appartenga contemporaneamente a più sottoclassi.== 
    
2. **Generalizzazioni in cui gli oggetti (o i link associativi)** possono **cambiare tipo** durante la loro vita  
    → ==In Python, **un oggetto non può cambiare classe dopo la sua creazione**.==  
    Quindi il tipo specifico (es. `Studente`, `Lavoratore`) deve essere fissato all’origine.
    




## Implicazioni pratiche

Le generalizzazioni **non disgiunte** o **dinamiche** (in cui il tipo cambia nel tempo) devono essere **ristrutturate o eliminate** nel diagramma UML prima di procedere all’implementazione in codice.

 Prendiamo ad esempio Go:
 ![[Class Diagram Go.png]]
In Go un'istanza di `Partita` nasce come oggetto della classe `Partita` e nel tempo può diventare istanza di `Punteggi` o di `Rinuncia` (ovviamente non può morire come oggetto di Giocatore).
Tuttavia in Python,  quando si crea, ad esempio, una classe `Persona` e una classe `Studente(Persona)` e si istanzia l'oggetto di quella classe:

```python
mario = Persona()
```

Esso non può diventare una istanza di Studente perché senno sarebbe un altro oggetto.

Quindi il complete in Python non esiste mentre il disjoint si.
In UML, ovviamente, questo vincolo quando si crea una generalizzazione tra più classi (ad esempio una generalizzazione che parte da `Persona` e arriva a `Studente` e `Lavoratore`), significa che istanza di Persona può essere o un Lavoratore o uno Studente.
In Python questo comportamento non è possibile implementarlo perché:
==quando si crea un oggetto Python, come ad esempio `x:Studente = Studente(...)`, quell'oggetto è e resterà per sempre un istanza della classe `Studente`.==  
Quindi non è possibile che quell'oggetto si evolva in un oggetto di un'altra classe della stessa gerarchia, in sostanza l'oggetto `x` non può e non potrà mai essere un oggetto della classe `Lavoratore` o `Persona`.
Questo comportamento è legato al fatto che:
==il tipo (`type`) di un oggetto Python è immutabile dopo l'istanza.== 
A differenza invece delle [[Generalizzazioni#Vincoli sulle generalizzazioni `{disjoint}` e `{complete}`|generalizzazioni con vincolo]] del diagramma UML delle classi:
- Con il `{complete}` si sta dicendo che:
	  ==Ogni oggetto della superclasse appartiene a una (o più) delle sottoclassi.== 
- Mentre con il `{disjoint,complete}`:
	==L’oggetto **appartiene esattamente a una sottoclasse alla volta**, ma **può potenzialmente cambiare sottoclasse** durante la sua vita, se il dominio lo consente.== 
Come visto poco sopra questi due comportamenti non sono supportati nativamente quindi nel diagramma UML ristrutturato si elimina il vincolo `{complete}`. 
Questa non è l'unica operazione da fare: bisogna anche aggiungere un un attributo discriminante nella superclasse, ma questo punto lo approfondiremo più avanti. 
Ora esistono 4 casistiche con le generalizzazioni:
1.  Senza vincoli sulle generalizzazioni   ^noVincolo
2. [[Generalizzazioni#1. `{disjoint}`|Con il solo vincolo `{disjoint}`]].  ^soloDisjoint
3. [[Generalizzazioni#2. `{complete}`|Con il vincolo `complete`]].  ^soloComplete
4. [[Generalizzazioni#^db2378|Con il `{disjoint, complete}` ]].   ^siaComplete-disjoint


### Caso 1: [[#^noVincolo|Generalizzazione **senza vincolo**]] (ristrutturazione **non necessaria**)

Immaginiamo un caso in cui in un diagramma UML di partenza abbiamo una generalizzazione tra le classi `Persona` e `Studente`, **senza alcun vincolo** di `{disjoint}` o `{complete}`.



In questo caso, ==gli oggetti non hanno bisogno di cambiare la loro classe più specifica.== 

![[Ristr generalizzazioni.png]]

In questo caso: 

- La classe `Studente` è una sottoclasse di `Persona`
    
- Nessun vincolo impone che **ogni** `Persona` debba essere un `Studente` o viceversa
    
- L’associazione `iscritto` collega ogni `Studente` a un `CorsoDiLaurea`.

Detto questo l'interpretazione che possiamo dare a questo diagramma è:
==Gli oggetti non hanno bisogno di cambiare la loro classe più specifica nel tempo:==  
==una `Persona` nasce come `Studente`, oppure resta semplicemente una `Persona`.==

Di conseguenza nella ristrutturazione del diagramma, non è necessaria alcuna modifica al diagramma UML concettuale: 
==La ristrutturazione **non cambia** la struttura delle classi.==

##### Traduzione in Python
Quindi la generalizzazione concettuale tra le classi la si può tradurre direttamente con l'[[Ereditarietà delle classi|ereditarietà in Python]]:
```python
class Persona:
    def __init__(self, nome: str, genere: str) -> None:
        self._nome = nome
        self._genere = genere

class Studente(Persona):
    def __init__(self, nome: str, genere: str, matricola: str) -> None:
        super().__init__(nome, genere)
        self._matricola = matricola

```

Questo è un **caso canonico di ereditarietà**:

- in Python, può essere **implementato direttamente** così com’è nel modello UML
    
- non ci sono conflitti con la staticità delle classi in Python
    
- non richiede interventi di ristrutturazione, perché:
    
    - nessun oggetto deve cambiare tipo durante la sua vita
        
    - nessuna ambiguità sull’appartenenza a più sottoclassi


### Caso 2: [[#^siaComplete-disjoint|Generalizzazione con i vincoli `{disjoint},{complete}` ]] 

Nel diagramma UML concettuale delle classi abbiamo una generalizzazione dalla classe `Persona` verso `Studente` e `Docente`, con vincolo `{disjoint, complete}`. 
![[Ristr con complete.png]]

Come già sappiamo quando i due vincoli [[Generalizzazioni#^db2378|`{disjoint,complete}` ]]vengono messi insieme si uniscono i significati di entrambi i vincoli:
- `{disjoint}` → Ogni oggetto è **istanza di una sola** sottoclasse (mai entrambe)
    
- `{complete}` → Ogni istanza della superclasse è anche **istanza di almeno una** sottoclasse
Uniti insieme questi due vincoli:
==tutte le istanze della superclasse devono appartenere a **una sola** delle sottoclassi coinvolte.== 
Ora ci si presenta un problema, ovvero:
Python **non consente a un oggetto di cambiare classe** dopo essere stato istanziato.  
Di conseguenza, se un oggetto è `Studente`, **non potrà diventare** `Docente`, né viceversa.
Per ovviare a questo problema bisogna implementare una [[Classi astratte|classe Astratta]] in Python per rispettare il vincolo `{complete}` nel diagramma ristrutturato:
==ovvero una classe che non ha oggetti propri cioè non ci sono oggetti che sono istanza proprie di quella classe.==
Quindi  si ottiene una classe astratta e li `{complete}` viene levato dal vincolo sulla generalizzazione:
- `Persona` diventa **una classe astratta**
    
- cioè una **classe senza oggetti propri**: nessun oggetto sarà istanza diretta di `Persona`
    
- i soli oggetti ammissibili sono quelli di classi figlie: `Studente` o `Docente`

> [!NOTE] **Nota:**
> Nel diagramma, la classe astratta è indicata con **il nome in corsivo**: _Persona_

Quindi il risultato della ristrutturazione è:
- La gerarchia ereditaria rimane 
- Il vincolo `{complete}` è ristrutturato nella classe astratta
- Infine lasciando solo il vincolo `{disjoint}` viene garantito che tutti gli oggetti creati siano oggetti di `Studente` o `Docente`, mai solo oggetti di `Persona`.

##### Traduzione in Python
```python
from abc import ABC

class Persona(ABC):  # classe astratta
    def __init__(self, nome: str) -> None:
        self._nome = nome

class Studente(Persona):
    def __init__(self, nome: str, matricola: str) -> None:
        super().__init__(nome)
        self._matricola = matricola

class Docente(Persona):
    def __init__(self, nome: str, nascita: date) -> None:
        super().__init__(nome)
        self._nascita = nascita

```


> [!example] In conclusione
> Il vincolo `{disjoint, complete}` nel modello UML impone che:
>
>- ogni oggetto **appartenga a una sola sottoclasse**, e
 >   
>- ogni oggetto sia **istanza di una sottoclasse**
>    
>
> In Python, questo viene tradotto:
>- con una **classe astratta** come superclasse (`Persona`)
  >  
>- e con istanze **solo delle classi figlie** (`Studente`, `Docente`)
 >   
>
> Così si garantisce che non vi siano oggetti di tipo `Persona`, né che un oggetto `Studente` possa diventare `Docente` in corso d’opera.


### Caso 3: Generalizzazioni, senza vincoli `{disjoint}` o `{complete}`,  con più di una sottoclasse  
Nel diagramma UML concettuale delle classi, può verificarsi una situazione in cui:

- ==Un oggetto **può essere istanza di più sottoclassi contemporaneamente**==
    
- ==Oppure **può non essere istanza di nessuna delle sottoclassi**==
    

📌 **Esempio**: una persona può essere:

- solo uno studente
    
- solo un docente
    
- sia studente che docente
    
- né studente né docente
Qui si presenta lo stesso problema di prima:
In Python:

- Un oggetto **non può cambiare classe dinamicamente**
    
- Non esiste il concetto di **molteplicità multipla di classi** (cioè non può essere istanza di più classi non correlate contemporaneamente)

Quindi come possiamo risolvere questo problema? 
Usando la tecnica della fusione: 
==prendiamo le n sottoclassi e le fondo nella superclasse==

![[Fusione.png]]

Ovvero:
- Si eliminano le sottoclassi (`Studente`, `Docente`)
    
- Si **fondono attributi e ruoli** nella superclasse `Persona`:
	l'attributo di `matricola` di `Studente` diventa un attributo della classe `Persona` con vincolo `[0..1]` perché una Persona può avere un numero di matricola come può non averne nessuno.
	Stessa cosa succede per l'attributo `nascita` di `Docente`; diventa un attributo di `Persona` e gli viene aggiunto un vincolo `[0..1]` perché una persona può avere una data di nascita oppure può non averne nessuna.
    
- Si aggiungono **flag booleani** per distinguere i diversi "ruoli" o stati dell’oggetto:
	Difatti nel diagramma ristrutturato vengo aggiunti due ulteriori attributi; `is_studente:bool` e `is_docente:bool`.
- Inoltre i vincoli sulle associazioni `iscritto` (con la classe `CorsoDiLaurea`) e `afferenza`(con la classe `Dipartimento`) diventano opzionali poiché:
	Una persona può partecipare al link di associazione `iscritto`, se è ovviamente anche uno studente, come può non parteciparvi perché può non essere uno studente.
	Stessa cosa, una persona può partecipare al link di associazione afferenza con un dipartimento, solo se è un docente, come può non parteciparvi se non è un docente.

Quindi per capire meglio:
`Studente` ha il numero di matricola,
`Persona` ha il nome,
e `Docente` ha la data di nascita, 
Tutto questo viene messo nella superclasse Persona perché si deve catturare tutti i casi e quindi le due sottoclassi vengono fuse in una sola classe cioè `Persona`.
Però non tutte le persona hanno la matricola, quindi si mette l'attributo 
`is_studente` di tipo `bool` e l'attributo `matricola` diventa opzionale(`[0..1]`).

Inoltre ogni `Studente` è iscritto ha un corso di laurea, ma adesso la classe `Persona` ingloba la classe `Studente`, ma ogni Persona non è iscritto a un corso di Laurea come non afferisce a un dipartimento. 
Quindi, per garantire la correttezza semantica che era espressa nella generalizzazione originaria, si definiscono i vincoli esterni nella [[Documenti di specifica#specificaVincoliEx Specifica dei vincoli esterni|specifica dei vincoli esterni]]:
Per ogni `p: Persona` vale:

1. `p.is_studente = True` ⟺ `p.matricola` è valorizzata
    
2. `p.is_studente = True` ⟺ `p` partecipa a un link `iscritto`
    
3. `p.is_docente = True` ⟺ `p.nascita` è valorizzata
    
4. `p.is_docente = True` ⟺ `p` partecipa a un link `afferenza`

Di conseguenza si deve inserire anche un attributo `is_docente:bool`
Quindi anche l'attributo `nascita` diventa opzionale e come per l'associazione `iscritto` anche il vincolo su `afferenza` sul lato di `Dipartimento`, diventa `0..1` perché non tutte le Persone afferiscono a un Dipartimento.
Quindi per vedere se la ristrutturazione della generalizzazione è stata ristrutturata correttamente dobbiamo porci le seguenti domande: 
Una persona **può non essere** sia Docente che Studente? Si
Una persona **può essere solo** Studente? Si
Una persona **può essere solo** Docente? Si
Una persona **può essere** entrambi ? Si


> [!remember] Considerazioni
> - È possibile rappresentare **tutti i casi** (solo studente, solo docente, entrambi, nessuno)
 >   
>- La molteplicità minima degli attributi e dei ruoli provenienti dalle sottoclassi diventa `0`
 >   
>- La **logica di dominio è implementata tramite vincoli esterni** anziché tramite ereditarietà

Un esempio di implementazione in python potrebbe essere:
```python
class Persona:
    def __init__(self, nome: str, is_studente: bool = False, is_docente: bool = False,matricola: str | None = None, nascita: date | None = None) -> None:
        self.nome = nome
        self.is_studente = is_studente
        self.matricola = matricola
        self.is_docente = is_docente
        self.nascita = nascita

        self._corso = None   # riferimento a CorsoDiLaurea
        self._dipartimento = None  # riferimento a Dipartimento

```
Ovviamente bisogna poi **controllare i vincoli** a runtime nel costruttore o tramite property/setter.


> [!example] **In conclusione**
> Quando in UML abbiamo una generalizzazione **non `{disjoint}`** e/o **non `{complete}`**, e vogliamo che:
>- un oggetto possa assumere più “ruoli”
>    
>- o evolvere da uno stato all’altro
>    
>
>allora si applica la **fusione**:  
> tutti gli attributi e ruoli delle sottoclassi vengono portati nella superclasse  
> la logica si mantiene tramite **vincoli esterni** e **flag booleani**




Nel complete:
![[Ristr complete.png]]

In questo caso cambia solo il vincolo estenro perchè può essere sia docente che Studente, quindi si aggiunge un vincolo che per ogni p:Persona:
p.is_docente = True oppure p.is_studente = True

Nelle generalizzaioni di assoc.: 
non cambia nulla 
e se invece: 
![[Ristr assoc. con generalizzazioni.png]]
In questo caso ArticoloNuovo si è fuso con ArticoloInVendita, e Utente si è fuso con VenditoreProfessionale.
Inolte ArticoloInVendita ha l'attributo condizione(cond) che è un tipo enumerativo che mi dice che l'articolo e nuovo o usato. Stessa cosa per Utente che ha acqusito l'attributo tipo che mi dice se l'utente e un venditore professionale o un smeplice utente.
Avendo fuso queste due classi si deve fondere anche l'associazione, pero attenzione: dobbiamo mettere nella specifica dei vincoli estenri 
per ogni a:ArticoloInVendita:
	- se a.cond = 'nuovo' allora a.anni_garanzia di tipo IntGE2
	- se a.cond = 'nuovo' allora il link (a,u): venditore nel quale 'a' è coinvolto è tale che u.tipo = 'prof'. 
In questo caso sto dicendo che se la condzione dell'articolo è 'nuovo' allora l'istnaza di venditore che partecipa al link di associazione in cui è è coinvolto è tale che il vlaore dell'attributo tipo di Utente è professionale