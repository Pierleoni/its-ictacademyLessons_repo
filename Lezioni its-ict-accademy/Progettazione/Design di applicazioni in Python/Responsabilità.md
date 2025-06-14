# Introduzione 

Ogni volta che dobbiamo implementare le associazioni si deve tenere conto delle responsabilità delle classi su quella [[Analisi dei requisiti mediante UML#Cosa sono le associazioni?|associazione]] .
## Le responsabilità 
Riprendiamo come esempio il diagramma ristrutturato delle classi di [[Esercitazione Azienda 1|Azienda 1]] ,
in questo caso per stabilire la responsabilità delle classi sulle associazioni che le coinvolgono, bisogna porsi le seguenti domande:
È utile conoscere il progetto in cui è convolto l'impiegato? Si
È utile sapere quale impiegato dirige il dipartimento? Si
Oppure un impiegato deve conoscere i dipartimenti in cui afferisce perché deve assicurarsi che il vincolo `0..1` deve essere valido.
Quindi in sostanza:
Per ogni associazione dobbiamo decidere quali delle 2 classi coinvolte ne hanno la responsabilità.
**Una classe C ha la responsabilità su una associazione A (nella quale è coinvolta) se un oggetto `c:C` deve poter**:
- ==conoscere in quali link di A è coinvolto==
- ==aggiungere, eliminare, modificare i link nei quali è coinvolto==
In generale per ogni associazione, almeno una delle due classi deve esserne responsabile.


### In quali casi serve la responsabilità?
Serve se c'è un operazione di classe o un use-case e si ha bisogno in qualche modo che un oggetto della classe possa accedere ai link in qualche modo.
Ad esempio: 
![[Operazioni di classe_Responsabilità.png]]

Qui abbiamo aggiunto un operazione di classe `numero_impiegati` su dipartimento, ciò vuol dire che il dipartimento deve conoscere il numero di impiegati e quindi un oggetto dipartimento deve avere la responsabilità di percorrere il numero di impiegati che vi afferiscono.
Un altro caso è quando il vincolo non è `0..*`, perché la classe deve assicurarsi che il suo vincolo sia soddisfatto, quindi ad esempio al vincolo `0..1` l'impiegato ha la responsabilità sull'associazione `afferenza` perché un impiegato si deve assicurare che quel vincolo sia rispettato, ciò significa che almeno un impiegato deve afferire a quel dipartimento.
In sostanza possiamo dire che **una classe C ha responsabilità in una associazione A se:**
- ==Esiste una operazione di classe/use - case in cui l'algoritmo necessita che un oggetto della classe `C` (`c:C`) può accedere/aggiungere/eliminare/modificare i suoi link di associazione A.==
- ==Inoltre partecipa alla associazione A con vincoli di molteplicità diversi da `0..*` (questo perché senza responsabilità sull'associazione A, un oggetto `c:C` non potrebbe assicurarsi di soddisfare i vincoli di molteplicità).== 

#### Esempio di responsabilità sulle associazioni
Per capire meglio il concetto di responsabilità e come applicarlo nel diagramma ristrutturato delle classi partiamo da un esempio:
![[Esempio1 Responsabilità.png]]

In questo diagramma la classe `Studente` è coinvolta nell'associazione `iscritto` con un vincolo di molteplicità `1..1`. 
Proprio per questo, di conseguenza, la classe `Studente` deve avere la responsabilità nell'associazione `iscrito` perché partecipa all'associazione con un vincolo diverso dallo `0..*`. 
Inoltre non c'è nessuna operazione di classe e/o use-case che chiede, dato un corso di laurea, si debba poter risalire ai suoi studenti.
Difatti la classe `CorsoDiLaurea` potrebbe non avere responsabilità nell'associazione `iscritto`


> [!caution] Raccomandazione:
> Bisogna essere molto prudenti nel togliere la responsabilità di classi ad associazioni. 
> Il codice potrà risultare più semplice ed efficiente ma meno estendibile.

### Il verso di navigabilità delle responsabilità nei diagrammi 

Quindi, potrebbe anche essere che lo studente ha responsabilità sul corso di laurea ma da un corso di laurea non ci interessa sapere gli studenti iscritti,
in questo caso, si dice che la **responsabilità è singola**:
==nel diagramma delle classi ristrutturato, alle associazioni a responsabilità di una singola classe si associa un verso di navigabilità,==  
cioè: 
==una sola freccia che parte dalla classe che ha la responsabilità e va verso la classe di cui si è responsabili==.   
![[Esempio di responsabilità singola.png]]
Quindi l'associazione può essere "navigata" solo in quel verso. ^6a5c39

Riprendiamo il diagramma delle classi ristrutturato di [[Esercitazione Azienda 1|Azienda 1]], facciamo una modifica al diagramma aggiungendo la classe Città: 
immaginiamo che da un dipartimento deve conoscere la sua citta, ma dall'altra parte non chiederemo a una citta di sapere i suoi dipartimenti, perché al dipartimento serve conoscere il suo link verso citta ma non viceversa:

![[Responsabilità.png]]

In questo caso:
bisogna tener conto che il vincolo di molteplicità, legato alla classe `Dipartimento`,(`1..1`) deve essere rispettato, poiché si deve immaginare che nel sistema ci sia un operazione che dato un dipartimento bisogna conoscere la sua citta, ma data una città non serve conoscere i dipartimenti che risiedono  in quella città. 

### L'aggregazione
Quando succede questo, ovvero che la responsabilità è singola e l'associazione non ha attributi, si chiama aggregazione e si fa con il rombo: questo significa che la città è una proprietà di dipartimento come quasi se fosse un suo attributo. 
![[Esempio aggregazione.png]]
L'aggregazione modella la relazione `has-a`:
==gli oggetti della classe responsabile hanno o possono avere (come “parte”, cioè come se fosse un attributo) riferimenti diretti ad uno o più oggetti dell’altra classe (in base al vincolo di molteplicità).== 
Ad esempio, in questo caso,  uno studente ha un riferimento diretto a un corso di laurea.


Da notare come le aggregazione funzionano anche con lo `0..*` ad esempio una persona ha visitato una città, la responsabilità è singola quindi persona ha un aggregazione verso città 