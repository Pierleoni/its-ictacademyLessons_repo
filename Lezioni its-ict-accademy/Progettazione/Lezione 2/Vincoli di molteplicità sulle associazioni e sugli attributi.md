 

I diagrammi delle classi visti finora ci permettono di rappresentare la realtà attraverso entità (classi) e relazioni (associazioni). ==Tuttavia, queste rappresentazioni sono spesso **troppo generiche** e non catturano pienamente i vincoli logici e concettuali che esistono nel mondo reale.==

Ipotizziamo che si deve progettare un sistema che registra la data di nascita di un impiegato in una città, come abbiamo negli esempi riportati nelle immagini sopra i modelli concettuali definiti finora **permettono configurazioni che potrebbero non essere realistiche,** questo perché senza vincoli precisi il modello accetta qualsiasi combinazione che sia formalmente corretta, anche se **non ha senso dal punto di vista logico.** 
Se guardiamo l'immagine riportata qui sotto ad esempio, possiamo vedere che:
![](https://i.imgur.com/PR5bO1D.png)

1. **[[Analisi dei requisiti mediante UML#^inLevel|Livello Intensionale]] (in alto):**

- Il modello concettuale prevede due classi:
    
    - `Impiegato`, con gli attributi `nome` e `cognome`.
        
    - `Città`, con l’attributo `nome`.
        
- L’associazione `nascita` collega un `Impiegato` a una `Città`, indicando dove è nato l’impiegato.
2. **[[Analisi dei requisiti mediante UML#^exLevel|Livello Estensionale]] (in basso):**
- Sono presenti istanze concrete delle classi:

	- `anna:Impiegato`, con nome `"Anna"` e cognome `"Bianchi"`.
    
	- Due città: `roma:Città` (`"Roma"`) e `milano:Città` (`"Milano"`).
	
Ora, qui il problema è che Anna risulta nata sia a Roma che a Milano, il che è possibile nel modello ma nel mondo reale non ha senso. 
Infatti la nota "Ammesso ma..." sottolinea che questa configurazione è ammessa nel diagramma delle classi, ma non rispetta i vincoli del mondo reale, poiché una persona non può essere nata contemporaneamente in due città diverse. 
Difatti una persona può nascere in una sola città, quindi il modello necessita di un vincolo per imporre questa regola. 
Proprio per questo si parla di vincoli di **vincoli di molteplicità sulle associazioni e sugli attributi,** i quali impongono delle restrizioni su:
- **Le associazioni** (es: Un impiegato deve essere nato in una sola città)
- **Gli attributi** (es: il nome di una città non può essere vuoto). 
I vincoli di molteplicità permettono di migliorare la qualità del modello, rendendolo più aderente alla realtà e riducendo errori nella progettazione del sistema.
### Vincoli di integrità 
diagrammi delle classi in UML ci permettono di definire la struttura di un sistema attraverso entità (classi) e relazioni (associazioni). Tuttavia, per garantire che il modello rispecchi fedelmente la realtà e sia privo di inconsistenze, è necessario introdurre **vincoli di integrità**. 
==Questi vincoli aggiungono restrizioni ulteriori rispetto a quelle puramente strutturali, imponendo regole più stringenti sui valori degli attributi e sulle relazioni tra oggetti.==
Vincoli di integrità : impongono ulteriori restrizioni (oltre a quelle strutturali imposte dal diagramma) sui livelli estensionali.  Sono ettichette che si mettono nel programma, cioè un'asserzione che impone una restrizione.  
In altre parole ==è una regola che limita i valori ammissibili per attributi, associazioni o interi oggetti in un modello.== 
A differenza dei vincoli di molteplicità, che si occupano esclusivamente del numero di relazioni tra classi, i vincoli di integrità controllano aspetti più articolati.

(il vincolo fi integrità è un espediente tecnologico per imporre dei limiti che esistono nel mondo reale)

![](https://i.imgur.com/73Z1k8Y.png)
In questo esempio:
1. **Classe `Impiegato`**:
    
    - Attributi: `nome` (Stringa), `cognome` (Stringa).
        
    - Vincoli di molteplicità sull’associazione `nascita`:
        
        - `0..*` (lato `Impiegato`): Un oggetto città   **può non essere associato** a nessun impiegato (0) o a molti impiegati (`*`).
            
        - `1..1` (lato `Città`): Ogni oggetto impiegato **deve essere associata a una citta.**

Senza questo vincolo il modello permette configurazioni illogiche, come un impiegato nato in due città diverse. 
Infatti la nota "non più ammesso" indica che, introducendo vincoli aggiuntivi (es: `1..1` sul lato `Impiegato`), questa incoerenza viene eliminata.

> [!danger]- **I vincoli di molteplicità e di integrità non sono la stessa cosa ne sono sotto categorie una dell'altra**
> I vincoli di molteplicità vengono sono una prerogativa di UML.
> - **Cosa fanno**:  
  >  Definiscono **quante istanze** di una classe possono essere collegate a un'istanza di un'altra classe **in un'associazione UML**.
  >  
>- **Esclusività**:  
 >   Concetto nativo e specifico dei **diagrammi delle classi UML**. Non esiste in database o codice (se non come traduzione indiretta, es: cardinalità in SQL).
> Mentre i vincoli di integrità sono Universali.
> - **Cosa fanno**:  
  >  Impostano **regole generiche** su valori, stati o relazioni, applicabili in **qualsiasi contesto** (UML, database, programmazione).
  >  
>- **Dove si usano**:
 >   
 >   - **In UML**: Su attributi/classi (es: `{prezzo > 0}`).
   >     
  >  - **In database**: `NOT NULL`, `UNIQUE`, `CHECK`.
  >      
 >   - **In codice**: Validazioni a runtime (es: `if(età < 18) throw Error()`).
 >       
>- **Esempio UML vs DB**:
  >  
  >  - **UML**: `{nome.length ≤ 50}` su un attributo `nome`.
  >      
 >   - **SQL**: `CREATE TABLE (nome VARCHAR(50) NOT NULL)`.
 >Tuttavia esiste una relazione tra i due:
 >- **Analogia**:  
  >  I vincoli di molteplicità **sono a UML** ciò che i vincoli di integrità referenziale **sono ai database** (es: `FOREIGN KEY`), ma:
  >  
   > - I primi sono **sintattici** (parte del linguaggio UML).
 >       
  >  - I secondi sono **semantici** (concetti logici indipendenti dal linguaggio).
  >      
>- **Collaborazione**:  
  >  In UML, **entrambi** servono a restringere il modello:
>
 >   - La molteplicità dice _"quanti"_ (relazioni).
   >     
  >  - L'integrità dice _"come"_ (valori/regole).
>> [!example] **In Sintesi**
>>
>>|                 | Vincoli di Molteplicità  | Vincoli di Integrità           |
| --------------- | ------------------------ | ------------------------------ |
| natura          | Specifici di UML         | Universali                     |
| Scopo           | Quantità di relazioni    | Qualsiasi regola logica        |
| Esempio UML     | `impiegato 1..* Azienda` | `{eta ≥ 18}`                   |
| Esempio non-UML | Non applicabile          | `CHECK (prezzo > 0)`<br>In SQL |

 
Inoltre i vincoli **di integrità aggiungono restrizioni ulteriori e più ampie rispetto ai soli vincoli di molteplicità**.

**1. Vincoli di Molteplicità (base)**

- **Cosa restringono**:  
    ==Solo il **numero di collegamenti** in un'associazione tra classi.==  
    Esempio:
     
- Uno studente può essere iscritto a _molti_ corsi (`*`), ma ogni corso deve avere _almeno uno_ studente (`1`).
        
- **Limite**:  
    ==Non controllano il contenuto degli attributi o altre regole complesse.==
    

**2. Vincoli di Integrità (restrizioni aggiuntive)**

- **Cosa restringono**:  
    Tutto ciò che i vincoli di molteplicità **non coprono**:
    
    - Valori degli attributi (es: `nome ≠ ""`).
        
    - Regole complesse tra attributi (es: `se età < 18 allora genitore ≠ null`).
        
    - Unicità (es: `matricola univoca`).
        

Quindi senza vincoli di integrità, il modello sarebbe **formalmente corretto ma logicamente errato** (es: città senza nome, impiegati con età negativa). Introducendoli, si garantisce coerenza con il mondo reale e si prevengono errori nel sistema finale.

### Semantica dei vincoli di molteplicità sui ruoli delle associazioni
I vincoli di molteplicità in UML hanno una semantica precisa che aiuta a capire a quale classe fanno riferimento e danno un'interpretazione univoca al diagramma:
![Semantica dei vincoli|0x0](https://i.imgur.com/UINDioH.png)
Prendendo come riferimento questa immagine possiamo notare che: 
Le classe coinvolte sono:
- `Impiegato`, con attributi `nome` e `cognome`
- `Città`, con attributo `nome`.
L'associazione `nascita` collega `Impiegato` a `Città`.
Sotto alla linea della associazione, posti alle estremità vediamo scritti i due vincoli di molteplicità:

`0..*` (zero to star): 
significa che ==un'istanza della classe può partecipare a zero o più associazioni==.  ^zeroToStart
- Il valore minimo (`0`) indica che l'oggetto **potrebbe non essere coinvolto in alcuna associazione**.
- Il valore massimo (`*`, ovvero "infinito") indica che **può essere coinvolto in un numero qualsiasi di associazioni**.
  
`1..1`(uno a uno): 
Significa che ==ogni istanza della classe deve essere associata esattamente a un'istanza dell'altra classe.==
Il valore minimo (`1`) e massimo (`1`) indicano che **l'oggetto deve sempre essere coinvolto in una e una sola associazione**.

>[!example]- Riassumendo
>| Vincolo | Significato                                                         |
| ------- | ------------------------------------------------------------------- |
| `0..*`  | L'oggetto può essere coinvolto in **zero o più** associazioni.      |
| `1..1`  | L'oggetto **deve essere coinvolto in una e una sola** associazione. |
>


> [!NOTE] **==Quando analizziamo i vincoli di molteplicità, dobbiamo leggerli "al contrario"==**
> 

==Ovvero lo "**zero to star**"(`0..*`) si riferisce alla agli oggetti della classe citta, mentre il vincolo uno a uno (`1..1`) si riferisce agli oggetti della classe impiegato.== 
Quindi quando impostiamo i vincoli di molteplicità, dobbiamo porci la seguente domanda:

 **==A quanti [[#^b5cc77|TARGET]] è collegato un [[#^sourceClass|SOURCE]] tramite [[Analisi dei requisiti mediante UML#^associationsDef|ASSOCIAZIONE]]?==**.   ^multiConstraints-def
 
 ##### **Legenda della Frase**
 
 1.**[[#^multiConstraints-def|Source]] (Classe Sorgente):** 
 ==È la classe da cui parte l'associazione (il punto di partenza del "link").==   
Corrisponde alla classe **di cui stiamo analizzando le relazioni** quando formuliamo domande del tipo;
 *A quanti \[target] può essere collegato un \[source].*  
 ^sourceClass
 
 
 2.**[[#^multiConstraints-def|Target]] (Classe di destinazione):** 
 ==È la classe **a cui arriva l'associazione** (il punto di destinazione del "link").==   
Corrisponde alla classe **di cui vogliamo contare gli oggetti collegati** al source.    ^b5cc77

3. **[[#^multiConstraints-def|Associazione]]:** [[Analisi dei requisiti mediante UML#^associationsDef|vedi la definizione]] 

Detto ciò, in questo caso le domande da porci sono: 
 1. **==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite link dell'associazione `nascita`?==**
    - **[[#^sourceClass|Classe Sorgente]]**:   `Impiegato` (partenza dell'associazione)
    - **[[#^b5cc77|Classe target]]:** `Citta` (destinazione)
    - **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]**: `nascita`
	- La risposta è `1..1` perché ogni impiegato **può essere nato in una sola città**.
	- Questo vincolo garantisce che non possano esistere due città diverse associate alla stessa persona tramite l'associazione "nascita".

2. **"A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite il link `nascita`?"** 
	-  **[[#^sourceClass|Classe Sorgente]]**: `Città` (partenza dell'associazione)
	- **[[#^b5cc77|Classe target]]:** `Impiegato` (destinazione)
	- **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]**: `nascita`
	-   La risposta è `0..*` perché una città **può avere un numero qualsiasi di impiegati nati al suo interno**.
	- Questo significa che una città potrebbe non avere alcun impiegato associato oppure averne moltissimi.

Prendiamo come esempio anche questa immagine 

![](https://i.imgur.com/dgHnOYY.png)
Nel [[Analisi dei requisiti mediante UML#^inLevel|livello intensionale]] ci sono due classi:
- `Persona`: ha un attributo  `nome` di tipo `stringa`
- `Automobile`: ha un attributo `targa`, presumibilmente di tipo `stringa`
La relazione tra `Persona` e `Automobile` è chiamata **"possiede"** ed è caratterizzata da un vincolo di molteplicità **`0..*`** dal lato di `Automobile`.
Nel [[Analisi dei requisiti mediante UML#^exLevel|livello estensionale]] , difatti, possiamo notare che:
l'istanza della classe `Persona` è `anna:Persona` da cui partono vari link verso le istanze della classe `Automobile`(`a1:Automobile`, `a2:Automobile`, `a3:Automobile`, e così via).
Il vincolo di molteplicità accanto a queste istanze è [[#^zeroToStart|`0..*`]] e conferma il vincolo imposto nel livello soprastante: ovvero una persona può possedere **zero, una o più** automobili.
Quindi la freccia con il vincolo `0..*` mostra la relazione di possesso, infatti una persona può possedere più automobili ma non è obbligata a possederne almeno una. 

> [!remember]- **Ricorda: La distinzione tra livello intensionale ed estensionale**
> - Il [[#^inLevel|primo]] mostra le classi e le loro relazioni generali.
   > 
>- Il [[#^exLevel|secondo]] mostra esempi concreti (istanze) che rispettano il modello.

#### Esercizio 1
 Definire i vincoli di molteplicità sui ruoli delle associazioni del seguente diagramma delle classi.
 ![](https://i.imgur.com/QkcwhFE.png)
In questa immagine possiamo notare 3 classi:
- `Hotel`: 
  con l'attributo `nome` di tipo `Stringa`.
- `Prenotazione`: 
  con l'attributo `istante` di tipo `DataOra`.
- `Persona`: 
  con gli attributi `nome` e `cognome`, entrambi di tipo `Stringa`.
E due associazioni:
1. **`hotel_prenotato`** tra `Hotel` e `Prenotazione`.
    
2. **`cliente_prenotazione`** tra `Prenotazione` e `Persona`.

Per definire i vincoli di molteplicità tra queste prime due classi (associazione `hotel_prenotato`) devo pormi le seguenti domande:
1. "==A quanti oggetti della classe `Prenotazione` può essere collegato un oggetto della classe `Hotel` tramite il link dell'associazione `hotel_prenotato`?**=="
	  
	- **[[#^sourceClass|Classe Sorgente (source)]]:** `Hotel`(partenza dell'associazione).
	- **[[#^b5cc77|Classe Target]]:** `Prenotazione` (destinazione).
	- **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `hotel_prenotato`. 
	**Ergo:** Un hotel può avere **zero, una o più prenotazioni** nel tempo.  
	**Risposta:** `0..*` (zero o più prenotazioni per ogni hotel).
	
2) . "**==A quanti oggetti della classe `Hotel` può essere collegato un oggetto della classe `Prenotazione` tramite il link dell'associazione `hotel_prenotato`?==**"
	- **[[#^sourceClass|Classe sorgente (source)]]:** `Prenotazione` (partenza dell'associazione)
	- **[[#^b5cc77|Classe Target]]:** `Hotel` (destinazione)
	- **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `hotel_prenotato`
    **Ergo:** Una prenotazione è sempre riferita **a un solo hotel**.  
    **Risposta:** `1..1` (ogni prenotazione è associata a un solo hotel).
    

> [!done] **Risultato**
> - `Hotel` → `0..*` `Prenotazioni`
>     
> - `Prenotazione` → `1..1` `Hotel`

Passando alla seconda coppia di classi (associazione `cliente_persona`): 
Qui dobbiamo porci le seguenti domande:
3) "**==A quanti oggetti della classe `Persona` può essere collegato un oggetto della classe `Prenotazione` tramite il link dell'associazione `cliente_prenotazione`?==**"
	- **[[#^sourceClass|Classe Sorgente (source)]]:** `Prenotazione` 
	- **[[#^b5cc77|Classe Target]]:** `Persona` (destinazione)
	- **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `cliente_prenotazione`
	**Ergo:** Una prenotazione può essere effettuata da **una sola persona** (di solito il titolare della prenotazione).  
	- **Risposta:** `1..1` (ogni prenotazione ha un solo cliente associato).
	
4) "**==A quanti oggetti della classe `Prenotazione` può essere collegato un oggetto della classe `Persona` tramite il link dell'associazione `cliente_prenotazione`?==**"
	 - **[[#^sourceClass|Classe Sorgente (Source)]]:** `Persona`
	 - **[[#^b5cc77|Classe Target]]:** `Prenotazione` (destinazione)
	 - **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `cliente_prenotazione`
	**Ergo:** Una persona può effettuare **zero, una o più prenotazioni** nel tempo.  
    -  **Risposta:** `0..*` (una persona può avere più prenotazioni, o nessuna).


> [!done ] **Vincoli finali corretti**
> 1. `Hotel` → `0..*` `Prenotazione`
 >   
>2. `Prenotazione` → `1..1` `Hotel`
 >   
>3. `Persona` → `0..*` `Prenotazione`
  >  
>4. `Prenotazione` → `1..1` `Persona`

![Soluzione dell'esercizio](https://i.imgur.com/Dsqzoiw.png)

Quindi il punto non è come dai la risposta ma come poni la domanda : ==perché la molteplicità dipende sempre da **quanti oggetti di una classe sono collegati a un oggetto dell'altra classe** nell'associazione.== 
In parole povere: 
Il fulcro è **come poni la domanda**, perché la molteplicità **non** riguarda una singola classe in sé, ma il **numero di oggetti collegati tra le due classi** attraverso l'associazione.


> [!hint] **Regola chiave:**
> Non bisogna chiedersi "**Quante relazioni ha questa classe?**", ma =="**Quanti oggetti di questa classe sono collegati a un oggetto dell'altra classe?**"==.
> Riprendendo l'esercizio qui sopra una **domanda errata** è: 
> > [!fail] "**Quante prenotazioni ha una persona?**"
> > Questo è troppo generico e può creare confusione.
> 
> Quindi la **domanda corretta** da porsi è:
> > [!done] **"A quante prenotazioni partecipa una singola persona?"**
> > Ciò ti porta direttamente alla risposta corretta(`0..*`)
> 
> **Il trucco è:**
> pensa sempre in termini di **oggetti specifici**, non di intere classi.


#### Esercizio 2
- Si vuole progettare un sistema che gestisca i dati anagrafici delle persone.
-  Di ogni persona interessa il nome, il cognome, la data di nascita, la città di nascita e quella di residenza.
-  Si definisca un diagramma delle classi concettuale per l’applicazione.

Quindi ci servono due classi:
1. `Persona`: 
   con gli attributi;
	- `nome`: di tipo `stringa`
	- `cognome`: di tipo `stringa`
	- `data_nascita`: di tipo `Data`
2. `Città`:
   con l'attributo
	- `nome`: di tipo `stringa`  

Dopodiché  andremo a definire due associazioni tra queste classi:
1. `nascita`
2. `residenza`


Ora andiamo a porci le seguenti domande per impostare i vincoli di molteplicità:
1. "**==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite il link dell'associazione `nascita`?==**"
   - **[[#^sourceClass|Classe sorgente(source)]]:** `Impiegato`(partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Città` (destinazione)
   - **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `nascita`. 
   **Ergo:** Una persona può essere nato in una sola città.
   **Risposta:** `1..1` (ogni persona ha solo una città di nascita).
   
1. "**==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite il link dell'associazione `residenza`?==**"
   - **[[#^sourceClass|Classe sorgente(source)]]:** `Impiegato` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Città`(destinazione)
   - **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `residenza`
   **Ergo:** Una persona può risiedere in una sola città.
   **Risposta:**`1..1`(ogni persona ha solo una citta di residenza).
   
1. "**==A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite il link dell'associazione `nascita` ?==**"
   - **[[#^sourceClass|Classe sorgente (source)]]:**`Città` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:**`Impiegato` (destinazione)
   - **[[Analisi dei requisiti mediante UML#^associationsDef|associazione]]:**`nascita` 
   **Ergo:** Una città può essere la citta di nascita di nessuna o di una o di più persone.
   **Risposta:** `0..*`(ogni città ha nessuna, una o più persone che vi sono nati).
   
1. "**==A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite il link dell'associazione `residenza`?==**"
   - **[[#^sourceClass|Classe sorgente (source)]]:** `Città` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Impiegato` (destinazione)
   - **[[Analisi dei requisiti mediante UML#^associationsDef|Associazione]]:** `residenza`
   **Ergo:** Una citta può essere la citta di residenza di nessuna o di una o di più persone. 
   **Risposta:** `0..*`(ogni città ha nessun, uno o più persone che vi risiedono).

![Esercizio 2](https://i.imgur.com/j30YVFi.png)



## Associazioni che insistono più volte sulla stessa classe
Supponiamo di voler modellare i sovrani di un regno ormai scomparso.
• Di ogni sovrano interessa il nome, il periodo in cui ha regnato, ed il predecessore.
Qui abbiamo bisogno di una classe `Sovrano`:
gli attributi sono;
- `nome`: di tipo `stringa`
- `inizio`: di tipo `Data`
- `fine`: di tipo `Data`
![La classe sovrano|339x224](https://i.imgur.com/QCteEn5.png)
Qui bisogna ricordare che ogni sovrano può essere un **predecessore** e un **successore**, in questo caso si usano **le associazioni con ruoli distinti**:
==**Un'associazione ricorsiva con ruoli distinti** è un tipo di associazione in cui una classe è collegata a sé stessa, rappresentando una relazione tra le istanze della stessa classe.== 
==Per evitare ambiguità, ogni partecipazione della classe all’associazione è caratterizzata da un **ruolo distinto**, che specifica il significato dei diversi estremi della relazione.==  ^def-AssRecuWithDistRole

### Caratteristiche principali 
- **Associazione ricorsiva**: 
  ==una classe partecipa più volte alla stessa associazione.==  
  
-  **Ruoli distinti**: 
   ==ogni istanza assume ruoli diversi nell’associazione per rendere chiaro il significato della relazione==.  ^roleDef
 
- **Molteplicità**: 
  specifica il numero minimo e massimo di istanze coinvolte in ciascun ruolo.  
-  **Esempi comuni**: gerarchie, genealogie, strutture organizzative.
Come per gli esempi riportati prima anche qui posso applicare lo schema:
**"==A quanti [Target] è collegato [Source] tramite [Associazione]?=="**
Tuttavia rimane un problema, ovvero come faccio a capire chi è il predecessore e chi è il successore in un associazione ricorsiva?
Devo assegnare due ruoli ben distinti nella stessa associazione

![](https://i.imgur.com/hS2QigU.jpeg)
Sappiamo che le istanze dell’associazione sono coppie (s1, s2) di oggetti (istanze) di classe Sovrano.
• La classe Sovrano gioca due ruoli nell’associazione.
In questo caso  UML ci obbliga a dare esplicitamente nomi distinti ai due ruoli
Quindi assegnando un ruolo A (predecessore) e un ruolo B (successore) alla associazione ricorsiva `successione` si è risolto il problema dell'ambiguità proprio perché avendogli assegnato questi ruoli si va a chiarire il significato della relazione all'interno della classe `Sovrano`. 
==Senza i due ruoli non si capirebbe chi è il predecessore e/o chi il successore di quale sovrano.== 

Ora per applicare i vincoli di molteplicità dobbiamo chiederci:
1. **"A quanti oggetti della classe `Sovrano` può essere collegato un oggetto della classe `Sovrano` nel ruolo di `successore`?"**
	- **[[#^sourceClass|Classe Source]]:** `Sovrano`
	- **[[#^b5cc77|Classe Target]]:** `Sovrano`
	- **[[#^roleDef|Ruolo]]:** `successore`
   **Risposta:**`0..1`: ogni oggetto sovrano può partecipa con il **ruolo di** successore al link della associazione successione  da 0 a 1 volta
2. **"A quanti A quanti oggetti della classe `Sovrano` può essere collegato un oggetto della classe `Sovrano` nel ruolo di `predecessore` ?"**
	- **[[#^sourceClass|Classe Source]]:** `Sovrano`
	- **[[#^b5cc77|Classe Target]]:** `Sovrano`
	-  **[[#^roleDef|Ruolo]]:** `predecessore`
**Risposta:** `0..1`; ogni oggetto sovrano può partecipa con il **ruolo di** `predecessore` al link della associazione successione da 0 a 1 volta.

![Livello intensionale della classe Sovrano|423x188](https://i.imgur.com/9EY4OaU.png)
^livInt-ClassSov


Questo perché:
nel caso del ruolo di `successore`;
- `0`: se è il primo della dinastia e non ha predecessori
- `1`: se è ha un predecessore e prende il suo posto al trono 
Mentre, nel caso di ruolo di `predecessore`:
- `0`: se è l'ultimo della dinastia o non ha successori
- `1`: se viene sostituito da un successore

Quindi nel [[Analisi dei requisiti mediante UML#^exLevel|livello estensionale]] verrà modellizzato così:
![](https://i.imgur.com/buFM1fY.png)

Come vediamo da questa immagine ci sono due istanze specifiche della classe `Sovrano`:
- `ric2:Sovrano`: che rappresenta **Riccardo II**
- `car1:Sovrano`: che rappresenta **Carlo I**

Queste due istanze sono collegate dalla relazione `successione`, con i seguenti ruoli:
- `ric2` (Riccardo II) è il **predecessore**.
    
- `car1` (Carlo I) è il **successore**.

#### Come il livello estensionale deriva dal livello intensionale
L'immagine del livello intensionale mostra la **classe** `Sovrano` e la relazione `successione`, specificando i ruoli `predecessore` e `successore` con molteplicità `0..1`.  
Ora, nel livello estensionale vediamo **istanze** di questa classe che rispettano la struttura definita:

- `ric2` è collegato a `car1` come predecessore → rispettando la cardinalità `0..1`, ogni sovrano può avere al massimo **un successore**.
    
- `car1` è collegato a `ric2` come successore → rispettando la cardinalità `0..1`, ogni sovrano può avere al massimo **un predecessore**.
    

In sintesi, il livello **[[Analisi dei requisiti mediante UML#^exLevel|estensionale]]** è un'istanza concreta del modello teorico definito nel livello **intensionale**, applicando la relazione `successione` a due sovrani reali.


> [!example] **In sintesi:**
> Quindi, nel livello estensionale abbiamo:
>
>- Due oggetti specifici (`ric2` e `car1`), che sono istanze della classe `Sovrano`.
  >  
>- La relazione `successione`, che collega `ric2` come predecessore e `car1` come successore.
  >  
>- Una corrispondenza diretta con la struttura generale descritta nel livello intensionale.

### Casi particolari: il sovrano può essere predecessore di se stesso?
In teoria, una relazione ricorsiva potrebbe permettere che un oggetto sia collegato a sé stesso. Tuttavia, nel contesto di una successione dinastica, questo scenario è poco realistico: un sovrano non può essere il proprio predecessore.
In realtà, se andiamo a vedere meglio ci sono stati casi storici dove un sovrano è stato il proprio predecessore (si pensi ad esempio alla proclamazione multipla di Napoleone Bonaparte che è stato Imperatore dei francesi per ben due volte). 
Tuttavia in questo caso si richiederebbe una modellizzazione più complessa, magari con attributi aggiuntivi che distinguano i diversi periodi di governo.


### **Concetti correlati: Riflessività e Simmetria**
Per comprendere meglio questi due concetti nelle associazioni ricorsive con ruoli distinti, riprendiamo l’esempio della classe `Sovrano`.
Con questa classe andiamo a definire una relazione di successione dinastica, che segue un ordine temporale ben definito.
Tuttavia la successione non  **però non è simmetrica:**
se un sovrano A è predecessore di un sovrano B, di conseguenza B non è predecessore di A nello stesso momento. 
Quindi, la successione segue una direzione temporale ben definita e possiamo osservare una catena di successori:
**==se A è predecessore di B, B è predecessore di C==.**
Detto in altri termini: 
==se **Luigi XV** è predecessore di **Luigi XVI**, allora **Luigi XVI** e predecessore di **Luigi XVII.**== 
Si crea così una gerarchia storica di regnanti che possiamo modellare nella nostra associazione. 
Questo esempio mostra che **la successione è transitiva** (perché il predecessore di un predecessore è comunque un predecessore), ma **non è simmetrica** (perché il successore non può essere anche predecessore di chi lo ha preceduto).
Questa "linea" si chiama **Simmetria**: 
==la successione tra sovrani **non è simmetrica**, perché se A è il predecessore di B, B non può essere contemporaneamente il predecessore di A.== 
Tuttavia, si può avere una **catena di successori**, per cui se A è predecessore di B e B è predecessore di C, si crea una gerarchia successiva di sovrani.

Mentre nel caso di Napoleone Bonaparte (o di altri regnanti) un sovrano, come abbiamo già detto prima, può essere il proprio predecessore, governando in periodi distinti: difatti, Napoleone fu imperatore di Francia dal **1804 al 1814** e poi di nuovo nel **1815** durante i Cento Giorni.
Questo scenario può essere modellato nella nostra associazione, permettendo che un sovrano possa risultare successore di sé stesso.
Questo caso si chiama **Riflessività**: 
==in una relazione riflessiva, un elemento può essere in relazione con sé stesso.== 
Ad esempio, se considerassimo la relazione **"è il proprio successore"**, potremmo modellare un sovrano che governa in periodi distinti.
Questa situazione rappresenta un caso di **riflessività:**
==ovvero una relazione in cui un elemento può essere in relazione con sé stesso==.
Nel nostro modello, ciò si traduce nella possibilità che un sovrano possa essere sia predecessore che successore di sé stesso, permettendo di rappresentare regni interrotti e ripresi.



> [!abstract]- **Implementazione di questi esempi in UML**
> **[[#^livInt-ClassSov|Esempio 1]]:** **Luigi XVI** → **Luigi XVII**
> Immaginiamo di modellare la successione tra Luigi XVI e Luigi XVII
>
| Istanza `Sovrano` | Nome       | Ruolo        |
| ----------------- | ---------- | ------------ |
| `luigi16`         | Luigi XVI  | Predecessore |
| `luigi17`         | Luigi XVII | Successore   |
>
>**Interpretazione nel modello UML**
>
>- `luigi16` è collegato a `luigi17` come predecessore.
>    
>- `luigi17` è collegato a `luigi16` come successore.
>    
>- Rispetta la molteplicità `0..1`, poiché ciascun sovrano ha **al massimo un successore e un predecessore**
>
>**Esempio 2**: Napoleone Bonaparte (caso di riflessività)
>Napoleone fu imperatore in due periodi distinti (**1804-1814** e **1815** durante i Cento Giorni). Qui il **predecessore e il successore coincidono**.
>
| Istanza `Sovrano` | Nome                           | Ruolo                     |
| ----------------- | ------------------------------ | ------------------------- |
| `napo1`           | Napoleone (1 regno 1804- 1814) | Predecessore e Successore |
| `napo2`           | Napoleone (2 regno 1815)       | Successore e Predecessore |
>**Interpretazione nel modello UML**
>
>- `napo1` è predecessore di `napo2` (il Napoleone del 1815 è successore del Napoleone del 1804-1814).
 >   
>- `napo2` è successore di `napo1`, ma è anche il suo **predecessore** in un certo senso, dato che si tratta della **stessa persona in due regni distinti**.
 >- Questo è un caso particolare di riflessività, che il nostro modello può gestire.
>
>Esempio 3: Ultimo Sovrano di una dinastia
>Consideriamo il caso di un sovrano che **non ha successori**, come **Carlo I d'Inghilterra**, che venne giustiziato nel 1649 e non fu immediatamente sostituito da un monarca.
>
| Istanza `Sovrano`   | Nome    | Ruolo        |
| ------------------- | ------- | ------------ |
| `carlo1`            | Carlo I | Predecessore |
| (Nessun successore) | -       | -            |
**Interpretazione nel modello UML**
>
>- `carlo1` ha un predecessore, ma **nessun successore** (molteplicità `0`).
 >   
>- Il nostro modello supporta questa situazione grazie alla molteplicità `0..1`.



