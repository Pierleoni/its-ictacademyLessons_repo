# Costruire i propri [[Introduzione a Python#Data types|Data Types]]


> [!NOTE] **pycache**
>È una cartella creata automaticamente quando si esegue codice Python. 
>Funziona come una memoria cache che contiene file bytecode compilati (.pyc), permettendo a Python di eseguire il codice più velocemente nelle esecuzioni successive senza doverlo ricompilare. Non è necessario **versionare (cioè includerla nei sistemi di controllo versione come Git)** questa cartella perché il bytecode è specifico per la versione di Python usata e viene rigenerato automaticamente quando necessario. Per questo motivo viene solitamente inclusa nel file `.gitignore` per evitare di salvare file non necessari nel repository.


## [[Introduzione a Python#Object-Oriented|Objected Oriented Programming]] 

La programmazione orientata agli oggetti (OOP) è un paradigma che permette di strutturare il codice in modo modulare ed efficiente attraverso l'uso delle **classi**. 
==Una classe rappresenta un concetto o un'entità, definendo le caratteristiche e i comportamenti comuni a più oggetti.== 
Comprendere le classi è essenziale per scrivere codice scalabile e manutenibile, ma la parte più complessa spesso non è tanto capire cosa sia una classe, quanto determinare quando e come utilizzarla correttamente.
### Che cos'è una Classe
Una classe è un modello astratto che definisce le caratteristiche comuni di un insieme di oggetti.
In parole povere una classe è una generalizzazione di un'**entità**:
==un modello astratto che definisce un insieme di caratteristiche e comportamenti comuni.== 
Le classi vengono usate per scrivere meno codice e renderlo più leggibile.

**Esempio Pratico:**
L'ITS deve sviluppare un gestionale per gestire il corso, qui si individuano i concetti che possono essere intesi come entità.   ^ITS-GesEx

- gli studenti ad esempio possono essere generalizzati nella classe `studente`: 
  ==Questa classe non rappresenta un singolo studente, ma fornisce una struttura generica che descrive le caratteristiche e i comportamenti comuni a tutti gli studenti.==   

#### Attributi e metodi di una classe
Le classi di solito specificano gli attributi(dati) e metodi(funzioni).
1. **Attributi:**
   ==Rappresentano le caratteristiche/proprietà della classe.==   ^attrs
   
> [!example] Sono i rettangoli nei diagrammi ER.
> 


2. **Funzioni/Metodi:**
   ==Stabiliscono il comportamento della classe.== 
   In altre parole ==sono azioni che la classe può compiere o che possono essere compiute sulla classe.==   ^methods

Quindi gli attributi della classe `Studente`, possono essere ad esempio: 
- `nome`
- `cognome` 
- `codice fiscale` 
- `residenza`.
Mentre alcuni metodi potrebbero essere:
- `calcolo_media_voti()`:
  per calcolare la media dei voti 
- `calcolo_presenze()`:
  Per determinare il numero di assenze e presenze.

> [!example] Esempio Pratico di un metodo:
>```run-python
>def calcola_media_voti(self, voti):
>	return sum(voti) / len(voti) if voti else 0
> 
>```
> 

### Istanze di una classe
==Un'istanza di una classe è un oggetto concreto creato a partire dalla classe stessa.== 
Possiamo immaginare questo concetto con un'analogia:
- ==La **classe** è uno **stampo per biscotti**: definisce la forma generale, ma non è un biscotto in sé.==  
      ^e6e18e
- ==Ogni **biscotto prodotto** con lo stampo è un'istanza della classe: anche se hanno la stessa forma, ogni biscotto è un oggetto distinto.== 

Quindi con un solo stampo posso creare più biscotti (generalizzazione). Lo stampo non rappresenta nessun biscotto in particolare, ma se viene usato insieme alla pasta frolla produce un biscotto concreto. Ogni biscotto è diverso dall'altro (istanza).
Un'istanza è quindi un elemento unico che deriva da una classe, con valori specifici per i suoi attributi. 
Creare un'istanza significa prendere la definizione generale della classe e assegnarle dati reali. 
In termini pratici, un'istanza è una **realizzazione concreta** di una classe.
Tuttavia non bisogna confondere un'istanza con un attributo della classe. Un'istanza è un oggetto completo, mentre un attributo è solo un dato che quell'oggetto contiene. 

> [!example] **Ad esempio:**
> 
> ```run-python
> studente1 = Studente("Marco", "Pierleoni", "MRCPLN98A01H501Z", "Roma")
> studente2 = Studente("Luca", "Bianchi", "LCABNC99B02F205T", "Milano")
> ```
> ^instanceCode
>

In questo caso, ==`studente1` e `studente2` sono due istanze della classe `Studente`==.  Il nome è un attributo, ma la stringa `"Marco"` è solo un valore assegnato a quell'attributo.


>[!example] **Per fare chiarezza: Analogia con le istanze di un Plugin Audio** 
>Le istanze di una classe in Python possono essere paragonate alle istanze di un plugin audio in una DAW: Immagina di utilizzare lo stesso identico plugin sulla catena degli insert in una traccia, con gli stessi settaggi, in una DAW (Pro Tools, Reaper, Cubase, FL Studio, Ableton, ecc.). Sebbene si tratti dello stesso plugin (cioè della stessa classe), ogni istanza è indipendente e separata dalle altre. Ad esempio, consideriamo il compressore 1176 della UAD: ![[1176.png]]
>
>- Il plugin UAD 1176 rappresenta una classe; definisce le caratteristiche e il comportamento del processamento della compressione sulla sorgente audio (traccia).
>- Ogni volta che il plugin viene caricato in uno slot della traccia, viene creata una nuova istanza del plugin. Di conseguenza, anche se i parametri tra due istanze sono identici, esse sono comunque oggetti distinti con memoria separata. Lavorano e influenzano la CPU insieme, ma in modo indipendente. 
>
>  Quindi, se modifichi un parametro su un'istanza del 1176, questa modifica non si riflette automaticamente sull'altra, proprio come se assegnassi un nuovo valore a un attributo di un'istanza di una classe in Python.   ^instanceEx

#### Sintassi delle istanze 
Per creare una istanza di una classe in Python, bisogna seguire determinati passaggi:
1. **Definire la classe:**
   - Creare una classe (`class NomeClasse`)
   - Definire il metodo speciale `__init__` per inizializzare gli attributi
2. **Definire [[#^attrs|attributi]] e [[#^methods|metodi]]:**
3. **Creare un'istanza della classe:**
   - Dichiaro una variabile, in questo caso `studente1`, e gli si assegna una nuova istanza della classe
   - Gli argomenti passati tra le parentesi servono per assegnare valori agli attributi (vengono anche chiamati **argomenti del costruttore**).
   - In parole povere;
```python
istanza = NomeClasse()
```


> [!example] Esempio Pratico:
>```python
>
> class Studente:
  >  def __init__(self, nome, cognome, codice_fiscale, citta):
  >      self.nome = nome
  >      self.cognome = cognome
  >      self.codice_fiscale = codice_fiscale
   >     self.citta = citta
> 
> def scheda(self):
   >     return f"{self.nome} {self.cognome}, CF: {self.codice_fiscale}, Città: {self.citta}"
> 
> # Creazione di istanze della classe Studente
>studente1 = Studente("Marco", "Pierleoni", "MRCPLN98A01H501Z", "Roma")
>studente2 = Studente("Luca", "Bianchi", "LCABNC99B02F205T", "Milano")
>
># Utilizzo di un metodo della classe
>print(studente1.scheda())  
>
># Output: Marco Pierleoni, CF: MRCPLN98A01H501Z, Città: Roma 
>```

In questo esempio:
- Il **[[#^builderInit|costruttore `__init__`]]** inizializza gli attributi  
- Quando crei `studente1`, gli passi i valori che vengono assegnati agli attributi della classe  
- Il metodo `scheda()` permette di ottenere una rappresentazione testuale dell'istanza
   


Come fa Python a determinare se due istanze sono lo stesso oggetto?
```run-python
studente:studente = studente("Marco", "Pierleoni")
studente:studente = studente("Marco", "Pierleoni")
```
Python confronta gli indirizzi di memoria delle due istanze. Anche se `studente1` e `studente2` hanno gli stessi valori negli attributi, sono due oggetti distinti perché occupano posizioni diverse in memoria.


Quindi per ricapitolare: 
==Le **classi** in Python sono modelli che definiscono come devono essere strutturati gli oggetti.== 
Da un punto di vista pratico, la classe è come uno stampo per creare oggetti che hanno [[#Attributi e metodi di una classe|attributi (caratteristiche) e metodi (azioni)]]. Ogni volta che crei un'istanza di una classe, stai creando un oggetto unico, proprio come ogni [[#^e6e18e|plugin in una DAW]], che, pur essendo basato sulla stessa "classe", funziona in modo indipendente con proprie impostazioni e memoria. 
In altre parole, una classe è un template per generare istanze distinte che condividono la stessa struttura ma possono avere valori diversi.

Riprendendo l'[[#^ITS-GesEx|esempio del gestionale dell'ITS]]:
Oltre alla classe `Studente` ci possono essere altre classi come:



- `Insegnanti`
    
- `Amministrazione`
    
- `Dispositivo`
    
- `Aula`
    
- `Corso`
    
- `Sede` (se ci sono più sedi)
    
- etc.
 ^myClass-List

In questo caso, le classi rappresentano **oggetti tangibili** all'interno del sistema. Tuttavia, le classi in Python possono anche rappresentare **concetti astratti**, come nel caso dei **Design Pattern:** 
==sono schemi di programmazione che aiutano a scrivere codice più efficiente e riutilizzabile, e sono fondamentali per il design del software== 
(il libro di riferimento è _Design Patterns: Elements of Reusable Object-Oriented Software_ pubblicato negli anni '80). 
Questi schemi possono essere implementati in qualsiasi linguaggio, e ==Python li supporta nativamente==.

Ad esempio, il Design Pattern _Strategy_: 
==è uno schema che definisce una famiglia di algoritmi, incapsulando ciascuno di essi in una classe separata==. 
Queste classi rappresentano **concetti astratti** che permettono di scegliere dinamicamente l'algoritmo da usare, a seconda della situazione. Per ora, tuttavia, ci concentreremo su concetti più **concreti**.

==Quando si confrontano due istanze, bisogna tenere a mente che le classi in Python sono come le **tabelle di un database**, dove non possono esserci due chiavi primarie uguali.== 
Sebbene in Python di default due istanze con lo stesso valore vengano considerate come "uguali" (perché confrontano i loro **attributi**), a livello di implementazione bisogna fare attenzione, poiché si potrebbe trattare di due oggetti distinti e separati.

Per capire meglio prendiamo l'esempio fatto sopra con le [[#^instanceCode|due istanze di `studente1` e `studente2`]]:
In questo caso, `studente1` e `studente2` sono due istanze della classe `Studente`. Sebbene abbiano un attributo simile (il nome e cognome), sono comunque oggetti distinti, con valori diversi per gli altri attributi (come il codice fiscale e la città). 
Questo dimostra che anche se le istanze appartengono alla stessa classe, i loro attributi possono differire e, di conseguenza, sono trattate come oggetti separati.

Un esempio pratico di come i Design Pattern vengano utilizzati in Python è su Google Maps. Se vogliamo implementare più algoritmi che fanno la stessa cosa, come ad esempio calcolare il percorso più breve, possiamo usare il _Strategy Pattern_, dove ogni "strategia" è rappresentata da un algoritmo differente.

Per approfondire i Design Pattern, oltre al libro, consiglio il sito [Refactoring Guru](https://refactoring.guru/design-patterns), che offre una panoramica dettagliata dei vari schemi di progettazione.

### Ereditarietà delle classi in Python
==L'**ereditarietà** è un meccanismo che permette a una classe (detta **classe derivata** o **sottoclasse**) di ereditare attributi e metodi da un'altra classe (detta **classe base** o **superclasse**).== 
Questo consente di riutilizzare il codice ed evitare duplicazioni, migliorando la **manutenibilità** e la **leggibilità** del programma.
Per spiegare al meglio il concetto di ereditarietà delle classi in Python riprendiamo il solito esempio del gestionale dell'ITS:
Abbiamo definito 4 classi per l'ITS, tutte queste classi, se ci pensiamo bene, hanno una cosa in comune:
**sono tutte persone**, anche se ogni classe fa una cosa diversa.


![[Ereditarietà delle classi.png]]
^GerarchiaClassi

Questa immagine rappresenta la gerarchia di classi utilizzando il concetto di ereditarietà nella programmazione OOP:
1. **Classe "Persona" (superclasse)**

- ==È la classe più generica della gerarchia.==
- Introduce due attributi: ==**età** e **altezza** (indicati come _Nuovo_ in verde perché sono definiti per la prima volta).==

2. **Classe "Studente" (sottoclasse di "Persona")**

- ==Eredita gli attributi **età** e **altezza** dalla classe `Persona`.==
- Introduce due nuovi attributi: ==**MatrNr** (numero di matricola) e **Università** (_Nuovo_ in verde).==

1. **Classe "Studente di scambio" (sottoclasse di "Studente")**
- Eredita tutti gli attributi delle classi superiori:  
    -  ==**età, altezza** (da `Persona`)==  
    -  ==**MatrNr, Università** (da `Studente`)==
- Aggiunge un nuovo attributo: ==**Università di origine** (_Nuovo_ in verde).==

#### **Cosa mostra l'immagine?**

Ogni classe eredita gli attributi dalla classe superiore, evitando la ripetizione del codice.  
**La gerarchia è costruita con il principio "[[Generalizzazioni#^is-a-Def|is-a]]"**:

- ==Uno `Studente di scambio` è anche uno `Studente` ed è anche una `Persona`.==  
-  ==Più si scende nella gerarchia, più le classi diventano specifiche==.

Queste 4 classi che possono essere raggruppate in una superclasse `Persona` perché hanno attributi in comune (ad esempio `Nome`, `Cognome`, `Codice Fiscale`, `Residenza` etc.). 
==Quindi andando a creare la classe `Persona` si va a formare una gerarchia di classi padri e classi figli==.

> [!info] In questo caso la classe `Persona`, diventa la classe padre di `Studente`, `Insegnante` ed etc.
> Quindi `Persona` ha la priorità più alta nella gerarchia delle classi

==Questa gerarchia padre-figlio è utile per non  scrivere tutti gli attributi e i metodi per ogni classe==.
Così facendo scrivo meno codice ogni volta per ogni classe che si riferiscono a persone, inoltre la possibilità di sbagliare è più bassa.
[[#^GerarchiaClassi|Prendendo in riferimento l'immagine sopra]], possiamo notare come le frecce indicano che il flusso vada dal basso verso l'alto, questo perché non tutte le persone sono studenti o studenti di scambio, ma tutti gli studenti sono persone e anche tutti gli studenti di scambio sono persone.
Per comprendere meglio questo concetto:
==`Studente` eredità la classe `Persona`, quindi lo studente è una persona ma non il contrario e non può andare nel senso opposto perché  posso dire che `A`(cioè la superclasse `Persona`) eredità `B` (la sottoclasse `Studente`) ma `B` non eredità `A`, tuttavia `C` (la sottoclasse `Studente di scambio`) può ereditare sia `A` che `B`.==
Come possiamo notare questa formula dell'ereditarietà delle classi segue il sillogismo aristotelico:
1. Tutti gli uomini sono mortali
2. Socrate è un uomo
3. Quindi Socrate è mortale

Nel nostro caso, l'analogia si traduce così:
1. **Premessa maggiore:**
   "Tutti gli `studenti` sono `Persone`"
   (Ogni istanza della classe `Studente` eredita le proprietà/metodi della superclasse `Persona`).
   Quindi è come dire che le istanze di `Studente` sono parte delle istanze di `Persona`
2. **Premessa minore:**
   "Non tutte le `Persone` sono `Studenti`"
   (Ciò significa che `Studente` è un **sottoinsieme proprio** della classe `Persona`, quindi l'inverso non è  valido.)
3. **Conclusione:**
   "L'insieme di `Studente` è un sottoinsieme proprio di `Persona`"
   (La gerarchia diventa chiara: `Persona` → `Studente` ).
✔ Se `B` eredita da `A`, allora `B` è un([[Generalizzazioni#^is-aDef|is-a]]) `A`.
==Questo perché io posso ereditare padre → figlio ma poi il figlio a sua volta può diventare padre, quindi `A → B → C`.== 
Quindi, in sostanza: 
`B` eredita `A` ma `C` eredità sia `A` che `B`.


> [!example]- **Analogia tra Programmazione OOP e DAW:**
> L’ereditarietà in programmazione può sembrare astratta, ma possiamo comprenderla meglio attraverso un'analogia con il mondo dell’audio. 
> In una DAW (come Reaper, Pro Tools, Cubase, etc.), organizziamo le tracce in **bus** per gestirle più facilmente, proprio come in OOP creiamo **classi e sottoclassi** per evitare ripetizioni e migliorare la gestione del codice.
> Supponiamo di avere `n` tracce di batteria:
> - Kick In 
> - Kick Out 
> - Snare Up 
> - Snare Bottom
> - Tom1, Tom2, Tom3, Tom4, Floor Tom
> - Overhead Left, Overhead Right
> - Drum Room Left, Drum Room Right 
> Ogni singola traccia può essere vista come un **oggetto** (istanza di una classe), con le sue caratteristiche (attributi) e azioni applicabili (metodi):
> - **Attributi:** 
>   caratteristiche della traccia (es. `KickIn` ha un certo livello di volume, un certo colore sonoro, ecc.).
> - **Metodi:**
>   azioni applicabili sulla traccia (EQ, compressione, riverbero, regolazione del pan, regolazione del volume di uscita del canale).
> 
> Per comodità e per velocizzare il flusso di lavoro, queste tracce vengono raggruppate in **bus group tracks** (tracce di gruppo). Ad esempio: 
> - Le tracce del **Kick** (`Kick In` + `Kick Out`) vengono raggruppate in una traccia bus `Kick`.
> -  Le tracce dello **Snare** (`Snare Up` + `Snare Bottom`) vengono raggruppate in un bus `Snare`.
> - Le tracce dei **Tom** (`Tom1`, `Tom2`, etc.) vanno in un bus `Toms`.
>- Tutte queste **bus group tracks** vengono infine raggruppate in un'unica traccia di gruppo chiamata `Drum Kit`.
>  
>Da qui possiamo fare un parallelismo con la Programmazione OOP:
>Questa struttura è simile alla gerarchia padre-figlio delle classi in programmazione orientata agli oggetti.
> - **Non tutte le tracce sono Kick o Snare**, ma tutte fanno parte della batteria.
 >   
>- **Non tutte le persone sono studenti, e non tutti gli studenti sono studenti di scambio**, ma ogni studente di scambio è sia uno studente che una persona.
>
> Esattamente come in programmazione classi specifiche (come `studenti di scambio`) possono ereditare attributi e metodi da classi più generali (`Studente` e `Persona`).
> Più si sale nella gerarchia, più il bus diventa generico, proprio come la classe `Persona` che rappresenta il livello più alto della gerarchia.
>Quindi i **le singole tracce di batteria:**
>Rappresentano gli **oggetti** (istanze) della classe e i loro **attributi** e **metodi**.
>I **Bus Group (Kick, Snare, Toms, ecc.)**:
>Rappresentano le  **sottoclassi**, ovvero raggruppano più tracce simili in un'unica entità con caratteristiche comuni.
>Esattamente come la classe `studente di scambio` eredita attributi e metodi della classe `Studente`. 
>Il **Bus Drum Kit (Superclasse):**
>Il Bus Drum Kit unisce Kick, Snare, Overheads, ecc., proprio come la classe `Persona` è la superclasse di `Studente`.
>
>Ovviamente la gerarchia nella programmazione non è intesa come flusso di segnali come in una DAW, ma un flusso di astrazione. 
>Tuttavia la logica della categorizzazione è simile. 
>Esattamente come nella gestione del suono, la gerarchia delle classi permette di organizzare il codice in modo più efficiente e modulare.
>
> > [!done] Vantaggio 
> >  Se voglio applicare una compressione comune a tutte le tracce di batteria, lo faccio sul **bus Drum Kit**, invece di settare manualmente ogni singola traccia → lo stesso principio vale nella programmazione: eredito attributi e metodi dalla superclasse per evitare ripetizioni inutili.
>>> [!Example] Parallelo completo tra DAW e programmazione a oggetti
>>> | Daw | Programmazione (OOP) |
>>> |-----------|-----------|
>>> | Tracce singole (KickIn, SnareUp, Tom1,etc.)    | **Oggetti/istanze** con attributi e metodi    | 
>>> | Moduli di canale (EQ, Send, Pan, Fader,etc.)   | **Metodi** (azioni eseguibili sulla traccia)    | 
>>> |Bus Kick, Snare, Toms, etc. | **Sottoclassi** (ereditarietà da una classe più generica)|
>>>|Bus Drum Kit| **Superclasse** (classe base da cui tutte le altre ereditano)|

Quando si creano gerarchie di classi, si definiscono nuovi tipi di dati. Ad esempio, la classe `Studente` eredita da `Persona`, il che significa che uno studente **è una persona** (relazione _[[Generalizzazioni#^is-aDef|is-a]]_). Più si scende nella gerarchia, più le classi diventano specifiche.
 
Se osserviamo l'immagine, la classe `Studente di scambio` (_Exchange Student_) è collegata con una freccia alla classe `Studente`. Questo perché **non tutti gli studenti sono studenti di scambio**, così come **non tutte le persone sono studenti**, ma **tutti gli studenti sono persone**.


> [!faq] **Principio "[[Generalizzazioni#^is-aDef|is-a]]"** 
> Il principio _is-a_ nella gerarchia dell'ereditarietà delle classi in Python rappresenta una relazione in cui una classe derivata è un tipo di oggetto della classe base. In altre parole, una classe derivata "è una" classe base, estendendo o specializzando il comportamento della classe da cui eredita.
> ==In parole povere questo principio riguarda specificatamente la relazione in cui la **sottoclasse** "è una" istanza della classe base, e può estenderla o specializzarla==.    ^is-aDef
> 
> 
>> [!example] Esempio di come si applica il principio is-a:
>>```python
>>class Animale:
  >>  def fare_suono(self):
  >>      pass
>>
>>class Cane(Animale):
  >>  def fare_suono(self):
  >>      return "Abbaia"
>>
>>class Gatto(Animale):
 >>  def fare_suono(self):
  >>      return "Miao"
>># Uso del principio is-a
>>animale = Cane()
>>print(isinstance(animale, Animale))  # True, perché Cane è un tipo di Animale
>>
>>
>>```
> In questo esempio: 
> - **Cane** e **Gatto** sono classi derivate da **Animale**.
>- Un oggetto di tipo **Cane** o **Gatto** _è una_ classe **Animale**, e quindi può essere trattato come un'istanza di **Animale**.
>Il principio _is-a_ è fondamentale per modellare gerarchie di classi in modo che oggetti di classi derivate possano essere utilizzati ovunque siano richiesti oggetti della classe base, sfruttando il polimorfismo.

### Come procedere nella progettazione?

Ci sono diversi modi per strutturare una gerarchia di classi, ma è fondamentale seguire alcuni principi:
1. **Non scrivere subito codice:** 
   ==Prima di iniziare a programmare, è essenziale progettare su carta, specialmente quando si lavora su sistemi complessi.==  
   Bisogna:
    - ==Identificare le classi==
    - ==Definire gli attributi e i metodi==
    - ==Stabilire le relazioni di ereditarietà==
2. **Scegliere un approccio di progettazione:** 
   Si può procedere in due modi:
    - **Dalla generalizzazione alla specializzazione:** 
      ==Partire da concetti generali e poi raffinare le classi più specifiche.==
    - **Dalla specializzazione alla generalizzazione:** 
      ==Partire da elementi concreti e raggrupparli in categorie più generali.== 

### I modelli in programmazione

==Un modello è un'astrazione della realtà==. 
Esistono molti tipi di modelli, ognuno dei quali descrive un aspetto specifico del mondo che ci circonda. Ad esempio, la **legge di gravitazione di Newton** è un modello che approssima il comportamento della gravità, senza rappresentare ogni dettaglio della realtà.

Anche in programmazione i modelli possono essere **molto specifici** o **più generici**. 
==Un modello troppo dettagliato potrebbe richiedere una gestione complessa dei dati, rallentando il sistema.== 
==D'altra parte, un modello troppo generico potrebbe risultare poco utile per risolvere problemi concreti==.

La scelta del livello di astrazione dipende quindi dal programmatore e dalle esigenze del sistema che si sta sviluppando.



---

## Implementare le classi in Python

==In Python, le classi permettono di creare strutture dati personalizzate e oggetti con caratteristiche specifiche.== 
Una classe rappresenta un modello per la creazione di oggetti, ciascuno con attributi e metodi propri.

### **Definizione di una Classe e il Costruttore** `__init__()`

Per definire una classe in Python, ==si utilizza la parola chiave `class`==. 
Gli attributi di una classe vengono generalmente assegnati attraverso il **costruttore**, un metodo speciale chiamato `__init__()`. 
==Questo metodo viene eseguito automaticamente ogni volta che viene creata una nuova istanza della classe.==

> [!faq]+ **Il costruttore `__init__`**
> Il metodo `__init__` non è obbligatorio ma è fortemente consigliato per inizializzare degli attributi specifici per ogni istanza della classe.
> ==Quindi il costruttore è utile per inizializzare gli attributi dell'oggetto, assegnando valori specifici quando viene creata un'istanza.==   
> Senza di esso si può comunque creare una classe e istanziare gli oggetti, ma si devo farlo manualmente:
> ```run-python
> class Persona:
>     pass  # Classe vuota
> 
> # Creiamo un'istanza
> persona1 = Persona()
> 
> # Aggiungiamo attributi manualmente
> persona1.nome = "Mario"
> persona1.cognome = "Rossi"
> persona1.eta = 30
> 
> print(persona1.nome)  # Mario
> 
> ```
> Tuttavia ogni volta che si crea una nuova istanza devi assegnare gli attributi manualmente, il che è scomodo e poco pratico. 
> Mentre con `__init__`, gli attributi vengono assegnati automaticamente:
> ```run-python
> class Persona:
>     def __init__(self, nome, cognome, eta):
>         self.nome = nome
>         self.cognome = cognome
>         self.eta = eta
> 
> # Creiamo un'istanza
> persona1 = Persona("Mario", "Rossi", 30)
> 
> print(persona1.nome)  # Mario
> 
> ```
> 
> > [!done] Vantaggi
> > Ogni istanza viene creata con i suoi dati senza bisogno di assegnarli manualmente.  
> >Il codice è più chiaro e organizzato.
> 
> Quindi `__init__` ==serve solo per inizializzare gli attributi di un'istanza== ma non i metodi della classe. 
> Difatti si può definire metodi senza usare `__init__`:
>```run-python
>class Persona:
  >  def saluta(self):
 >       return "Ciao, piacere di conoscerti!"
>
>p = Persona()
>print(p.saluta())  # Output: Ciao, piacere di conoscerti!
>```
>> [!note] ==Anche se `__init__()` non è obbligatorio per creare metodi, spesso è usato insieme ad essi per lavorare con gli attributi della classe.==
>
>> [!example] **In conclusione**
>> - `__init__()` **non è obbligatorio**, ma è utile per inizializzare gli attributi di un'istanza.
>>- Non serve per creare funzioni o metodi, ma solo per assegnare gli attributi di un oggetto.
>>- Una classe può avere altri metodi oltre a `__init__()`, indipendenti da esso.   ^builderInit

Ecco un esempio di definizione della classe `Person`, che rappresenta una persona con tre attributi: `nome`, `cognome` ed `eta`.

```python
class Person:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
```

- `self`: 
  ==rappresenta l'istanza attuale della classe e permette di accedere agli attributi e ai metodi dell'oggetto.== 
### **`Self` in Python**  

  
==Il `self` è un riferimento all'istanza della classe ed è utilizzato per accedere agli **attributi** e ai **metodi** dell'oggetto.==  
Grazie a `self`, ==ogni istanza mantiene i propri dati separati dalle altre, evitando sovrapposizioni.==  
È quindi indispensabile nei metodi di una classe quando si lavora con gli attributi dell'istanza.
#### **Dove si usa `self`?**
1️. Nel costruttore [[#**Definizione di una Classe e il Costruttore** `**__init__()**`|`__init__`]]  

Quando un oggetto viene creato, ==`self` permette di assegnare i valori agli attributi dell'istanza.==
```python
 class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome  # ✅ Necessario per salvare il valore nell'istanza
        self.cognome = cognome

```
2. Nei metodi d'istanza:
 ==`Self` permette di accedere agli attributi dell'oggetto anche dentro altri metodi della classe.==
```python
class Persona:
    def __init__(self, nome):
        self.nome = nome  # ✅ Memorizza il nome nell'oggetto

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome}!"  # ✅ Usa self per leggere l'attributo

persona1 = Persona("Luca")
print(persona1.saluta())  # ✅ Ciao, mi chiamo Luca!
   
```
>[!attention] **`Self` è solo una convenzione**
>Python non obbliga a usare proprio la parola `self`, ma è una convenzione universale. ==Rinominare `self` con un altro nome è considerato **una cattiva pratica**, perché rende il codice più difficile da leggere e capire==.
>```python 
>class Persona:
  >  def __init__(istanza, nome):  # Tecnicamente valido, ma sconsigliato
  >      istanza.nome = nome
>```

Il `Self` è importante perché senza di esso gli attributi non vengono salvati in [[Il modello di Von Neumann#RAM|RAM]] per l'istanza:
- Con `Self` l'attributo viene memorizzato nell'oggetto e rimane disponibile finché esiste l'istanza
- Senza `Self` il valore esiste solo dentro la funzione e viene eliminato quando la funzione termina.
  
```python 
class Persona:
    def __init__(self, nome):
        nome = nome  #  Non viene salvato nell'istanza!

persona1 = Persona("Luca")
print(persona1.nome)  #  Errore! L'attributo non esiste 
```

>[!example] **In Conclusione: l'importanza del self**
>- ==**`Self` è un parametro che serve per accedere agli attributi e ai metodi di un'istanza della classe.**== 
>- ==**Permette di salvare gli attributi nell'istanza dell'oggetto**, mantenendoli in memoria finché l'istanza esiste.== 
> - ==**È obbligatorio nei metodi d'istanza** per distinguere i dati dell'oggetto corrente da quelli di altre istanze.== 
> - ==**Non è una parola riservata**, ma è una convenzione fortemente consigliata.== 
>  
> Quindi,  grazie a `Self` ogni oggetto viene reso unico e separato dagli altri.


    
- `nome`, `cognome` ed `eta`: 
  ==sono i parametri passati quando si crea una nuova istanza della classe e vengono assegnati agli attributi dell'oggetto.== 
    

==Quando viene creato un nuovo oggetto, Python alloca memoria per l'istanza e i suoi attributi.== 
==Ogni istanza è indipendente dalle altre, occupando uno spazio di memoria separato.== 

### **Creazione di Oggetti**

Per creare un'istanza della classe `Person`, basta chiamare il costruttore passando i valori richiesti:

```python
persona1 = Person("Mario", "Rossi", 30)
persona2 = Person("Flavio", "Rossi", 31)
persona3 = Person("Flavia", "Asti", 29)
persona4 = Person("Flavio", "Adducci", 31)
```

==Ogni variabile (`persona1`, `persona2`, ecc.) rappresenta un'istanza distinta della classe `Person` con dati specifici.==

### **Gestione degli Attributi con Getter e Setter**

In Python, ==gli attributi di un oggetto sono generalmente accessibili direttamente, ma è buona pratica utilizzare metodi specifici per leggere e modificare i valori.== 
Questo permette di applicare controlli e garantire un accesso sicuro ai dati.
Esistono 2 metodi principali per gestire gli attributi:
1. **Getter:** 
   ==permettono di ottenere il valore di un attributo.==
   In altre parole è un ==metodo **read-only,** restituisce il valore dell'attributo e permette di leggerlo senza modificarlo.==  
2. **Setter:** 
   ==consentono di modificare i valori degli attributi in modo controllato.== 
   In parole povere ==permette di modificare il valore di un attributo, applicando eventualmente controlli o validazioni.== 


**Implementazione di Getter e Setter**
Un approccio tradizionale per gestire gli attributi di una classe è definire esplicitamente i metodi `get` e `set`. 

Esempio di getter e setter per l'attributo `nome`:

```python
class Person:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
```

Questo approccio permette di gestire l'accesso agli attributi e aggiungere logiche di validazione in futuro.

### **Accessibilità degli Attributi: Pubblici e Privati**

In Python, non esistono modificatori di accesso espliciti come in altri linguaggi (ad esempio `public`, `private` in Java). 
Tuttavia, per convenzione, ==un attributo può essere reso "privato" utilizzando un underscore (`_`) o due underscore (`__`) prima del nome dell'attributo.== 

Esempio:

```python
class Person:
    def __init__(self, nome, cognome, eta):
        self.__nome = nome  # Attributo privato
```

==L'uso di `__` (doppio underscore) attiva il **name mangling**, che modifica il nome dell'attributo internamente per rendere più difficile l'accesso diretto dall'esterno della classe. Tuttavia, non è una protezione assoluta.==


### **Utilizzo dei Decoratori** `@property` **per Getter e Setter**

Un'alternativa più elegante per gestire l'accesso agli attributi è ==l'uso dei decoratori `@property` e `@nome.setter`, che permettono di definire getter e setter in modo più intuitivo==:

```python
class Person:
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError("Il nome non può essere vuoto")
```

Questo approccio:
- Il metodo `nome()` con il decoratore `@property` agisce come un getter: 
  ==permette di leggere l'attributo come se fosse pubblico, ma senza modificarlo direttamente.== 
- Il metodo `nome()` con il decoratore `@nome.setter` agisce come un setter e permette di applicare controlli sulla modifica del valore. 

> [!info] Ovviamente per ogni attributo (`nome`, `cognome`, `eta`) bisogna usare il nome dell'attributo stesso nel decoratore (`@nome.setter`, `@cognome.setter`, `@eta.setter`)
>>[!example]- **Esempio:**
>>```python
>>class Person:
  >>  def __init__(self, nome, cognome, eta):
  >>      self.__cognome = cognome
  >>      self.__eta = eta
>>
  >>  # Getter e Setter per nome
  >>  @property
  >>  def nome(self):
  >>      return self.__nome
>>
  >>  @nome.setter
  >>  def nome(self, nuovo_nome):
  >>      if len(nuovo_nome) > 0:
   >>         self.__nome = nuovo_nome
   >>     else:
   >>         raise ValueError("Il nome non può essere vuoto")
>>
  >>  # Getter e Setter per cognome
  >>  @property
  >>  def cognome(self):
   >>     return self.__cognome
>>
  >>  @cognome.setter
   >> def cognome(self, nuovo_cognome):
   >>     if len(nuovo_cognome) > 0:
   >>         self.__cognome = nuovo_cognome
   >>     else:
   >>         raise ValueError("Il cognome non può essere vuoto")
   >> # Getter e Setter per eta
   >> @property
   >> def eta(self):
   >>     return self.__eta
>>
  >>  @eta.setter
   >> def eta(self, nuova_eta):
  >>      if nuova_eta > 0:
   >>         self.__eta = nuova_eta
   >>     else:
  >>          raise ValueError("L'età deve essere positiva")
>>```









> [!done] **Vantaggi dell'uso di Getter e Setter con `@property`**
> - **Incapsulamento:** Permette di nascondere l'implementazione interna e di esporre solo ciò che è necessario.
  >  
>- **Controllo e validazione:** È possibile inserire controlli sui dati prima di modificarli.
  >  
>- **Interfaccia coerente:** Gli attributi possono essere letti e modificati come se fossero pubblici, ma con un maggiore controllo.
>  
>- **Compatibilità futura:** Se in futuro si vorrà modificare l'accesso a un attributo (ad esempio rendendolo calcolato dinamicamente), non sarà necessario cambiare il codice esistente che usa la classe.

In conclusione, L'uso di getter e setter in Python dipende dalle necessità del progetto. 
Se non è necessario applicare controlli sugli attributi, si può accedere direttamente a essi. Tuttavia, per un codice più robusto e manutenibile, è consigliato l'uso di `@property` per una gestione più sicura e controllata degli attributi.

> [!example] **In sintesi** 
> - Gli **attributi pubblici** sono accessibili direttamente, ma potrebbero causare problemi di sicurezza e inconsistenza.
>  
>- Gli **attributi privati** (con `__`) riducono il rischio di modifiche accidentali, ma non sono completamente inaccessibili.
> 
>- I **getter e setter con **`@property` sono la soluzione più pulita per mantenere il codice leggibile e sicuro.

### **Ereditarietà: Creare Classi Derivate**

==L'ereditarietà consente di creare una nuova classe basata su un'altra esistente, evitando di riscrivere codice già definito.== 
==Una classe derivata eredita gli attributi e i metodi della classe base, ma può anche definirne di nuovi o sovrascrivere quelli esistenti.== 

**Esempio di una classe `Dipendente` che estende `Persona`, aggiungendo l'attributo `stipendio`:**

```run-python
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

class Dipendente(Persona):
    def __init__(self, nome, cognome, eta, stipendio):
        super().__init__(nome, cognome, eta)  # Richiama il costruttore della classe base
        self.stipendio = stipendio  # Nuovo attributo specifico della classe derivata

    def get_stipendio(self):
        return self.stipendio

```
In questo esempio:
- La classe `Dipendente` **eredita** da `Persona`, quindi può usare i suoi attributi (`nome`, `cognome`, `eta`).
- Il metodo `super().__init__(nome, cognome, eta)` chiama il costruttore della classe `Persona`, evitando di riscrivere lo stesso codice.
- **Aggiungiamo un nuovo attributo** `stipendio`, che è specifico della classe `Dipendente`.

Quindi l'uso di `super().__init__()` ==garantisce che il costruttore della classe base (classe padre) venga chiamato correttamente, evitando ripetizioni di codice==.
Questo è utile quando si eredita da un'altra classe e si vuole **riutilizzare** il codice del costruttore della classe base senza riscriverlo.


> [!done] **Perché usare `super().__init__()`?**
> - **Evita ripetizioni di codice:** 
>   Se la classe `Persona` ha molti attributi, non serve riscriverli in `Dipendente`.  
> - **Permette di estendere la classe padre** senza modificarne il codice.  
> -  **Gestisce automaticamente l’ereditarietà multipla** in modo pulito.

#### **Protezione degli Attributi Sensibili con Eccezioni**

In alcuni casi, è utile impedire l'accesso o la modifica di determinati attributi, come una password. 
Si può fare lanciando un'eccezione se si tenta di accedere a un valore sensibile:

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def get_password(self):
        raise ValueError("Non puoi accedere alla password")
```

In questo modo, chi tenta di leggere `get_password()` otterrà un'eccezione, proteggendo il dato.

> [!example]  **Conclusione**
> Riassumendo:
> - `**__init__()**`: 
>   ==è il metodo costruttore usato per inizializzare un oggetto.==
>     
> - `**self**`: 
>   ==permette di riferirsi all'istanza corrente della classe.==
>     
> - ==**Getter e setter** permettono di controllare l'accesso agli attributi.==
>     
> - ==**L'uso di** `_` **e** `__` aiuta a definire attributi "privati".==
>     
> - ==**I decoratori** `@property` offrono un modo più elegante per gestire gli attributi.== 
>     
> - ==**L'ereditarietà** permette di riutilizzare e estendere il codice esistente.==
>     
> - ==**Le eccezioni** possono essere usate per proteggere dati sensibili.== 

L'uso corretto delle classi rende il codice più organizzato, leggibile e manutenibile, consentendo di modellare in modo efficace problemi complessi con la programmazione a oggetti in Python.


Attributi di classe
Sono attributi globali, a che servono? Ad esmepio se ho 10 ogggetti di Person e si accede all'attributo di classe e slegato degli oggetti ma è legato alla classe e quindi è legato a tutti gli oggetti.
Es: 
```run-python
class Person:

    personCount = 0

    def __init__(self, name):

        self.name = name

        self.update()

    @classmethod #é una direttiva che va ad indicare che stai andando ad accedere agli attributi di classe, senza di esso il cls sotto verrebbe interpretato come un self

    def update(cls):

        cls.personCount += 1

alice = Person("Alice W.")

bob = Person("Bob M.")

print("------------------")

print(Person.personCount)
```

Quindi `Person.personCount` è un attributo della classe non dell'oggetto.

`cls`: è il modo corretto per accedere agli attributi della classe.

`@classmethod`:é una direttiva che va ad indicare che stai andando ad accedere agli attributi di classe, senza di esso il `cls` sotto verrebbe interpretato come un self.

La differenza tra cls e self:
cls: va ad accedere agli attriubuti globali della classe
self: va ad accedere agli attriubuti del costruttore o quelli che vanno ad essere definiti negli altri metodi della classe.

Tuttavia non posso ad accedere ad un attributo definito con il self anche con il cls, l'interprete mi dà un messaggio di errore in output e mi dice che quell'attributo non è stato definito.


---


## Metodi speciali
### il metodo `__str__`

Ci permette di rappresentare un oggetto della classe leggibile come stringa
```python
class Person:
	def __init__ (self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"{self.name}, {self.age} years old"

p = Person ("Luca", 30)
print(p)
```

Oltre a migliorare la leggibilità è utile per fare il debbuging. 
Se togliessi il metdo `__str__` mi ritornerebbe l'indirizzo di memoria. 
ciò è utile perchè io in questo caso printo solo l'oggetto senza associarlgi anche la funzione:
se io al posto del metodo `__str__` definissi una funzione, ad esempio `printMsg()` per stampare l'oggetto nel print dovrei fare `print(p.printMsg())`, mentre in questo modo me lo fa in automatico.

### Metodo `__call__`
Fa si che l'oggetto della classe può essere trattato come una funzione. Quindi:
```
class Greeter:
	def __init__(self, message):
		self.msg = message
	def __call__(self):
		return f"Hello, {self.msg}"

g = Greeter("Alice")
print(g())
```

In questo caso abbiamo le paretnesi perchè abbiamo l'oggetto g come se fosse una funzione