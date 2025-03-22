 
Le classi in python e quindi anche gli oggetti sono un concetto astratto, ci sono delle differenze tra Python e la progettazione.
in fase di analisi ci concentriamo sulle classi che sugli oggetti:
==gli oggetti servono essenzialmente per descrivere elementi singoli particolarmente significativi==
==oppure per descrivere esempi.== 
È un approccio simile al paradigma della programmazione [[Introduzione a Python#Object-Oriented|objected-oriented]] (es:[[Introduzione a Python|Python]], Java,etc.).
==Quindi un programma si scrive definendo un insieme si classi (o class), non di oggetti poiché questi vengono creati, modificati e distrutti durante l'esecuzione del programma.== 
In UML ci sono tanti costrutti delle classi e degli oggetti ma ne andremmo ad escluderne molti in modo di avere un significato univoco per ogni diagramma. 
## Cos'è un oggetto in UML
Un oggetto in UML modella un elemento del dominio di analisi :

> [!deep]- **Significato di Dominio di analisi**
>  ==è l'insieme degli oggetti di interesse che si trovano nella porzione di mondo che il sistema deve rappresentare==

- un oggetto "ha vita propria": 
  ==cioè  può essere interpretato e compreso indipendentemente dagli altri oggetti del sistema e si risolve indipendentemente dagli altri oggetti.== 

> [!deep]- **Cosa si intende per "l'oggetto si risolve"?**
> ==Si intende che l'oggetto ha una sua **identità** e una sua **logica interna** che non dipendono direttamente dagli altri oggetti del sistema.== 
> > [!note] Questo concetto è fondamentale nella progettazione objected-oriented e nella modellazione UML.
> 
> Nello specifico:
>  1. **Identità autonoma**
>==Un oggetto rappresenta un'entità ben definita nel dominio di analisi (cioè nella porzione di mondo che il sistema deve rappresentare).== 
>
>> [!example]- Ad esempio, in un sistema di gestione dei contatti, un oggetto potrebbe essere un **Contatto** con attributi come nome, cognome, numero di telefono, ecc. 
>
>==Questo oggetto ha una sua **identità univoca** (ad esempio, un ID unico) che lo distingue dagli altri oggetti, anche se condividono gli stessi attributi.==
>
>2. **Logica interna indipendente**
>
>==Un oggetto ha una sua **logica interna** (cioè metodi o comportamenti) che può essere eseguita senza dover necessariamente interagire con altri oggetti.==
> 
>> [!example] Ad esempio, un oggetto **Contatto** potrebbe avere un metodo per verificare se il numero di telefono è valido. 
>
>Questo metodo ==può essere eseguito **indipendentemente** dagli altri oggetti del sistema, perché la logica è contenuta all'interno dell'oggetto stesso.==
>
>3. **Risoluzione autonoma**
>
>Quando si dice che un oggetto "si risolve indipendentemente", si intende che:
>
>- **Non dipende strettamente da altri oggetti**: 
>  ==un oggetto può esistere e funzionare anche senza dover conoscere o interagire con altri oggetti.== 
>
> >[!example] Ad esempio, un oggetto **Contatto** può esistere anche senza sapere nulla degli altri contatti o dei gruppi a cui potrebbe appartenere.
>    
>- **È autosufficiente**: 
>  ==l'oggetto contiene al suo interno tutte le informazioni e le operazioni necessarie per svolgere i suoi compiti.==
>   
>>[!example] Ad esempio, un oggetto **ContoCorrente** potrebbe avere un metodo per calcolare il saldo, che non richiede di conoscere altri oggetti come transazioni o clienti.
>
>> [!example] **Esempio Pratico**
>> Immagina un sistema bancario con due oggetti: `ContoCorrente` e `Transazione`.
>> - L'oggetto **ContoCorrente** ha attributi come numero di conto e saldo, e metodi come `deposita()` e `preleva()`.
 >>   
>>- L'oggetto **Transazione** ha attributi come importo, data e tipo (deposito/prelievo).
>>  
>>  In questo caso:
>>  - `ContoCorrente` può esistere e funzionare indipendentemente dalle **Transazioni**. Ad esempio, il metodo `deposita()` può essere eseguito senza dover conoscere le transazioni precedenti.
 >>   
>>- `Transazione`, invece, potrebbe dipendere da `ContoCorrente` per sapere su quale conto è stata effettuata, ma `ContoCorrente` non dipende da **Transazione** per esistere o funzionare.
>
> In sintesi
>
>Dire che un oggetto "si risolve indipendentemente dagli altri oggetti" significa che:
>
>- Ha una sua **identità univoca**.
>    
>- Contiene al suo interno la **logica** necessaria per svolgere i suoi compiti.
 >   
>- Non dipende strettamente da altri oggetti per esistere o funzionare.
>    
>Questo approccio rende il sistema più **modulare**, **manutenibile** e **scalabile**, perché ogni oggetto è un'unità autonoma che può essere modificata o migliorata senza influenzare direttamente gli altri oggetti.

Ad esempio un telefono all'interno del sistema può essere capito ed interpretato indipendentemente dagli altri telefoni e le sue informazioni nel tempo possono risolversi (cioè evolversi o cambiare). 

> [!example]- **Spiegazione dell'esempio del telefono**
> Immagina un sistema che gestisce una rubrica telefonica. In questo sistema, ogni **telefono** è modellato come un oggetto con attributi come:
>
>- Numero di telefono
  >  
>- Modello
  >  
>- Proprietario
  >  
>- Stato (attivo/non attivo)
  >  
>
>Ogni telefono è un oggetto **indipendente** perché:
>
>1. **Può essere interpretato e compreso da solo**:
  >  
  >  - Un telefono ha un significato intrinseco: 
  >    ==rappresenta un dispositivo con un numero univoco, un modello e un proprietario==. Queste informazioni sono sufficienti per capire cosa rappresenta l'oggetto, senza bisogno di conoscere altri telefoni nel sistema.
  >      
   > - Ad esempio, se guardi un telefono con numero `123456789`, modello `iPhone 12` e proprietario `Mario Rossi`, puoi capire cosa rappresenta senza dover sapere nulla degli altri telefoni nella rubrica.
 >       
>2. **Le sue informazioni possono evolversi e cambiare nel tempo**:
  >  
 >   - ==Il telefono può cambiare stato (da attivo a non attivo), può cambiare proprietario o può essere aggiornato con un nuovo modello==. 
 >     Questi cambiamenti avvengono **indipendentemente** dagli altri telefoni nel sistema.
 >       
   > - Ad esempio, se il telefono di Mario Rossi viene disattivato, questo non influisce sul telefono di Luca Bianchi, che rimane attivo e con le sue informazioni intatte.
>        
>3. **Non dipende da altri oggetti**:
>    
  >  - ==Un telefono non ha bisogno di conoscere gli altri telefoni nel sistema per esistere o funzionare==. La sua logica (ad esempio, verificare se è attivo o no) è contenuta all'interno dell'oggetto stesso.

- ==È identificato univocamente mediante l'identificatore di oggetto== 
- Un oggetto in UML è un istanza di classe (la cosiddetta classe più specifica; vedremo che, in determinate
circostanze, un oggetto è istanza di più classi, ma in ogni caso, tra le classi di cui un oggetto è
istanza, esiste sempre la classe più specifica).


![[Oggetto in UML.pdf.png|center]]
Prendendo questa immagine come riferimento possiamo notare:
- **div_comm:** 
  ==è l'identificatore dell'oggetto== (scelto
dall’analista per potersi riferire all’oggetto nello
schema concettuale)
- **Libro:**
  è la classe più specifica di cui l'oggetto è istanza 
- **La sottolineatura**

Due oggetti rappresentano due cose distinte nel mondo.
La classe sono insieme di oggetti  omogenee (tutti gli oggetti hanno qualcosa in comune): hanno in comune gli attributi (il valore viene attribuito all'oggetto) e le dinamiche (operazioni, le vedremo in seguito).
Ogni classe è descritta da:
- **nome**
- **Insieme di proprietà:** 
  ==astrazioni delle proprietà comuni degli oggetti che sono istanze delle classi.== 
![[1 esempio.png]]

Abbiamo la classe `Libro`, che possiede un attributo `titolo` di tipo `Stringa`. Questo significa che ogni oggetto creato a partire dalla classe `Libro` dovrà avere un valore per l'attributo `titolo`, e questo valore dovrà essere una stringa.

Nel diagramma vediamo due istanze della classe `Libro`:

- L'istanza `div_comm`, che ha come valore per l'attributo `titolo` la stringa `"La Divina Commedia"`.
- L'istanza `bio`, che ha come valore per l'attributo `titolo` la stringa `"La mia grandiosa vita"`.

Le frecce tratteggiate indicano che `div_comm` e `bio` sono **istanze** della classe `Libro`, ovvero oggetti concreti che seguono la struttura definita dalla classe. Questo significa che ogni istanza della classe `Libro` deve rispettare il vincolo imposto dal diagramma: deve possedere l'attributo `titolo` e questo attributo deve contenere esattamente un valore di tipo stringa.

Questo schema assicura che tutti gli oggetti della classe `Libro` siano strutturati in modo coerente, garantendo che l'attributo `titolo` sia sempre presente e contenga una stringa.
Nel diagramma sono evidenziati due livelli fondamentali:

- **Livello intensionale**: 
 
  ==rappresenta la definizione astratta delle classi, ovvero il modello che descrive le proprietà e il comportamento degli oggetti che ne derivano. Definisce quali attributi e metodi devono avere le istanze della classe.==               
  In altre parole descrive cosa una classe è e cosa può fare, ma non si occupa delle istanze concrete.           ^inLevel
 


- **Livello estensionale**: 
  ==rappresenta le istanze concrete (oggetti) che derivano dalle classi e che esistono nel sistema. Ogni istanza è un'entità specifica che segue la struttura definita dalla classe a cui appartiene.==
  In altre parole è l'insieme delle istanze concrete (oggetti) che derivano dalla classe. 
  Questi oggetti seguono la struttura definita a livello intensionale, ma hanno valori specifici per gli attributi. ^exLevel

Applicando questa distinzione al diagramma:

- Il **livello intensionale** è rappresentato dalla classe `Libro`, che definisce l'attributo `titolo` di tipo `Stringa`. Questo stabilisce che ogni istanza della classe `Libro` dovrà necessariamente avere un attributo `titolo` con un valore di tipo stringa.
- Il **livello estensionale** è costituito dalle istanze `div_comm` e `bio`, che sono oggetti concreti della classe `Libro`. Questi oggetti possiedono valori specifici per l'attributo `titolo`: `"La Divina Commedia"` per `div_comm` e `"La mia grandiosa vita"` per `bio`.
In altre parole, il livello intensionale riguarda **la progettazione** (definizione delle classi), mentre il livello estensionale riguarda **l'implementazione concreta** (gli oggetti creati nel sistema).

### Identità degli oggetti o delle istanze 
È possibile avere due oggetti distinti che però condividono lo stesso valore per un determinato attributo.
![[le istanze diverse con lo stesso attributo.png]]

L'immagine mostra due livelli:

1. **[[#^inLevel|Livello delle classi (intensionale)]]:** 
    - Qui si definisce la classe `Libro`, che ha un attributo `titolo: Stringa`.
    - La classe specifica la struttura e le proprietà generali di un oggetto.
2. **[[#^exLevel|Livello degli oggetti (estensionale)]]:**  
    - Vengono rappresentate due **istanze** (oggetti) della classe `Libro`.
    - Entrambi gli oggetti (`div_comm` e `div_comm_2`) hanno lo stesso valore per l'attributo `titolo = "La divina commedia"`.
    - Ogni istanza è un'entità separata, anche se ha gli stessi dati.


==Non è il valore degli attributi a determinare l'unicità di un oggetto, ma il suo identificatore.== 
Ad esempio, possiamo avere due oggetti `Persona` con lo stesso nome e cognome? **Sì**, ma devono avere identificatori diversi. ==Se l'identificatore non è diverso, non è possibile distinguere i due oggetti.== 


> [!deep]- **La macro area dell'identità degli oggetti**
> Il concetto di **identità degli oggetti** o **identità delle istanze** in programmazione e modellazione concettuale racchiude e integra i tre concetti fondamentali:
> 
> 
> 1. **Identità dell'oggetto (Object Identity - OID)**:  
   > ==Questo concetto si riferisce al fatto che un oggetto è distinto dagli altri non in base ai suoi attributi, ma grazie a un identificatore univoco.== 
   > ==Anche se due oggetti hanno gli stessi valori di attributo, rimangono entità separate.== 
   > Questo è un aspetto fondamentale dell'identità degli oggetti.    ^OID
   > 
   > 
>    
>2. **Estensione e intensionalità delle classi**:
 >   
 >   - **Intensionalità**: 
 >     ==rappresenta la definizione della classe, ovvero la sua struttura (attributi) e comportamento (metodi).==
>        
  >  - **Estensione**: 
  >    ==rappresenta le istanze (oggetti) della classe, che possono avere gli stessi valori per alcuni attributi ma rimanere entità distinte grazie alla loro identità univoca.==  
   >     Questo concetto è strettamente legato all'identità degli oggetti, poiché l'identità è ciò che distingue le istanze anche quando condividono gli stessi attributi.
  >      
>3. **Principio di uguaglianza vs. identità**:
  >  
 >   - **Uguaglianza (Equality)**: 
 >     ==due oggetti sono considerati uguali se hanno gli stessi valori negli attributi rilevanti.==
 >       
 >   - **Identità (Identity)**: 
 >     ==due oggetti sono distinti se hanno identificatori diversi, anche se hanno gli stessi attributi.==  
  >      Questo principio è centrale nel concetto di identità degli oggetti, poiché sottolinea la differenza tra l'uguaglianza basata sui valori e l'identità basata sull'unicità dell'oggetto.

### Link e associazioni: come classi e oggetti interagiscono

Il secondo elemento fondamentale da comprendere è come le classi e gli oggetti interagiscono tra loro. Per questo, parliamo di **[[#Cosa sono i link?|link]]** e **[[#Cosa sono le associazioni?|associazioni]]**.
Sia i link che le associazioni rientrano nel concetto di identità degli oggetti, anche se in modo indiretto.

![[Link e associazioni.png]]

L'immagine qui riportata rappresenta il concetto di associazioni e link nella modellazione concettuale.
Riprendiamo la distinzione tra **[[#^inLevel|livello intensionale (classi e associazioni)]]** e [[#^exLevel|livello estensionale (istanze e link)]] per comprendere meglio il rapporto tra gli oggetti in un sistema. 
Nel livello intensionale possiamo notare 2 classi: 
- La classe **Libro** con l'attributo `titolo:Stringa` 
- La classe **Persona** con l'attributo `nome: Stringa` e `cognome: Stringa`. 
  Tra queste due classi esiste un'**[[#^associationsDef|associazione]]** chiamata autore: 
  ==essa rappresenta la relazione tra un libro e la persona che lo ha scritto.==   
- L'associazione è direzionata: la freccia indica "il verso di lettura del nome" (facoltativo)
Nel livello Estensivo possiamo vedere istanze le specifiche delle classi:
- **<u>div_comm</u>**:
  è un oggetto della classe `libro`, con il titolo `"La divina commedia"`
- **<u>dante</u>:** 
  è un oggetto della classe `Persona`, con nome `"Dante"` e cognome `"Alighieri"`.
Tra questi due oggetti esiste un **[[#^instanceDef|link]]**(istanza della relazione autore), che collega `div_comm` con `dante`. 
==Questo link non ha un identificatore proprio, poiché è determinato univocamente dagli oggetti che collega.== 
#### Cosa sono le associazioni?
Nella modellazione concettuale (ad esempio, in UML) un'associazione rappresenta una relazione tra due o più classi.
anche qui l'identità degli oggetti gioca un ruolo importante:
- Le associazioni collegano istanze specifiche (oggetti) di classe diverse, e queste istanze sono identificate in modo univoco. 
- L'identità degli oggetti permette di distinguere tra due istanze che potrebbero avere gli stessi attributi ma partecipano a relazioni diverse.
Quindi possiamo definire un'associazione come: 
==Un'**associazione** rappresenta la **possibilità** che due oggetti siano o meno in relazione tra loro.==   ^associationsDef

> [!example] **Esempio: Sistema di gestione di una biblioteca**
> In un sistema di gestione di una biblioteca, due libri potrebbero avere lo stesso titolo e autore (attributi uguali), ma sono istanze distinte con identità diverse. Un'associazione tra un libro e un prestito si baserà sull'identità univoca del libro, non solo sui suoi attributi.


[[Link e associazioni.png|Riprendendo l'immagine sopra]], l'associazione `autore` modella il legame tra le classi `Libro` e `Persona`. Se il nome di una `Persona` è correlato a un `Libro`, allora quella persona è l'autore del libro.

In altre parole:

- ==Un'associazione è una **relazione tra due classi**==.
- ==Le istanze di un'associazione tra due classi si chiamano **link**.==


#### Cosa sono i link?
==Un link (o riferimento) è un modo per accedere a un oggetto specifico attraverso un puntatore o un identificatore.== 
In altre parole:
==Un link è una relazione concreta tra due istanze di classi diverse.==   ^instanceDef

Questo è strettamente legato all'identità degli oggetti perché:
- Un link punta a un oggetto specifico, identificato in modo univoco (ad esempio, tramite il suo **[[#^OID|Object Identity(OID)]]**).
- Anche se due oggetti hanno gli stessi attributi, i riferimenti a essi saranno distinti perché puntano a istanze diverse. 
  
> [!example] Prendi ad esempio le [[Le Classi#^instanceCode|istanze di una classe in Python]]


Quindi se un'associazione lega due classi (ad esempio, `C1` e `C2`),
 ==un **link** collega un oggetto della classe `C1` a un oggetto della classe `C2`==.

Ad esempio, [[Link e associazioni.png|nella figura sopra]], c'è un link che lega <u>`div_comm`</u> (un oggetto della classe `Libro`) a `Dante` (un oggetto della classe `Persona`).

#### Perché i link non hanno un identificatore?

In UML, i link non hanno un identificatore esplicito perché:

1. ==Non possono esistere due link che collegano la stessa coppia di oggetti.==  
    Ad esempio, se `div_comm` e `Dante` sono legati da un link nell'associazione `Libro-autore`, non ha senso avere un altro link che li collega di nuovo. La risposta alla domanda "sono legati?" è già implicita: o sono legati o non lo sono.
    
2. ==Il link è implicitamente identificato dalla coppia di oggetti che rappresenta.== 

> [!example] Riepilogo
> - **Associazione**: 
>   relazione tra due classi (es. `Libro` e `Persona`).
>     
> - **Link**: 
>   istanza di un'associazione, che collega due oggetti specifici (es. `div_comm` e `Dante`).
>     
> - I link non hanno un identificatore esplicito perché sono univoci per la coppia di oggetti che collegano.


> [!faq]- **Quando i link e le associazioni non rientrano nell'identità degli oggetti**
> In alcuni contesti, i link e le associazioni possono essere utilizzati in modo astratto, senza fare esplicito riferimento all'identità degli oggetti. Ad esempio:
>
>- In un database relazionale, le associazioni sono spesso rappresentate tramite chiavi esterne, che si basano su valori (non necessariamente su identità univoche).
  >  
>- In alcuni linguaggi di programmazione, i riferimenti possono essere utilizzati per condividere lo stesso oggetto (ad esempio, in Python, due variabili possono puntare allo stesso oggetto).
  >  
>
>Tuttavia, anche in questi casi, l'identità degli oggetti è implicita, poiché è ciò che permette di distinguere tra oggetti condivisi e oggetti distinti.

In sintesi, i **link** e le **associazioni** sono strettamente legati all'identità degli oggetti, poiché si basano sull'unicità delle istanze per funzionare correttamente. Tuttavia, il loro utilizzo può variare a seconda del contesto (programmazione, modellazione, database), ma il concetto di identità rimane fondamentale per garantire che gli oggetti siano gestiti e distinti in modo appropriato.


---

## Esempio Pratico:  Gestione delle Prenotazioni in un Albergo
Per comprendere meglio il concetto di **associazioni e link**, consideriamo il caso di un sistema di prenotazioni alberghiere.
### Modello concettuale
![[livello intensionale prenotazioni.png]] 
Nel nostro modello, abbiamo due classi principali: 
- **Hotel:** 
  con l'attributo `nome:Stringa`, che rappresenta il nome dell'hotel.
- **Persona:**
  con gli attributi `nome:Stringa` e `cognome:Stringa`, che rappresentano il cliente.

Queste due classi sono collegate da un'**[[#^associationsDef|associazione]]** chiamata **Prenota**, che rappresenta la possibilità che una persona possa prenotare un hotel.
Questa immagine rappresenta il **[[#^inLevel|livello intensionale]],** cioè il livello delle classi e delle loro associazioni. Questo significa che **non stiamo ancora parlando di istanza specifiche,** ma solo della struttura concettuale del sistema.  
#### Significato dell'associazione "Prenota "
L'associazione **prenota** indica una relazione tra oggetti della classe `Persona` e oggetti della classe `Hotel`. 
In altre parole: 
==definisce il fatto che una persona può prenotare un hotel==.

- **Senza l'associazione "prenota"**, i==l modello non potrebbe rappresentare il concetto di prenotazione, perché le classi `Persona` e `Hotel` sarebbero entità indipendenti senza alcun legame==.
    
- **Con l'associazione "prenota"**, ==esplicitiamo che esiste una connessione tra queste due entità, rendendo possibile modellare il concetto di prenotazione==.
Questo per quanto riguarda nel [[#^inLevel|livello intensionale]].
#### Livello Estensionale: Istanza della Prenotazione 
Dopo aver definito il **livello intensionale**, in cui abbiamo individuato le classi `Hotel` e `Persona` e l'associazione `prenota`, passiamo ora al **[[#^exLevel|livello estensionale]]**, che rappresenta le istanze concrete di queste classi e i loro collegamenti effettivi.
Quindi, ==mentre nel livello intensionale si definisce **la struttura concettuale del sistema**, nel livello estensionale si osservano **casi specifici e reali**==.
![[Livello estensionale prenotazioni.png|448x189]]

L'immagine mostra due istanze delle classi:

- **h1:Hotel**, un'istanza della classe `Hotel`, che rappresenta un hotel reale chiamato `"La Pergola"`.
    
- **alice:Persona**, un'istanza della classe `Persona`, che rappresenta una persona specifica di nome `"Alice Bianchi"`.
    

Queste istanze sono collegate da un **link prenota**, che indica che **Alice Bianchi ha prenotato l'hotel "La Pergola"**.

#### Dal modello Concettuale ai Dati Reali
Possiamo vedere che ogni elemento del livello intensionale ha una controparte nel livello estensionale:

1. **La classe `Hotel`** → istanza `h1:Hotel` con nome `"La Pergola"`.
    
2. **La classe `Persona`** → istanza `alice:Persona` con nome `"Alice"` e cognome `"Bianchi"`.
    
3. **L'associazione `prenota`** → link effettivo tra `h1` e `alice`, che rappresenta una prenotazione concreta.
Mentre modellizziamo questo sistema dobbiamo porci la seguente domanda:  "A quale domanda risponde l'instanza di quel link prenota?" 
In generale Il **livello estensionale** risponde alla domanda:  
**"Quale persona specifica ha prenotato quale hotel specifico?"**

Nel nostro esempio, la risposta è:  
**"Alice Bianchi ha prenotato l'hotel 'La Pergola'."**

Tuttavia  se io volessi rappresentare una seconda prenotazione di 'alice' presso h1? 
Nel modello attuale, c'è un problema: non possiamo rappresentare più prenotazioni della stessa persona presso lo stesso hotel. 
Questo perché, in UML, un **link** tra due oggetti (in questo caso, `alice:Persona` e `h1:Hotel`) può esistere solo una volta. 
Quindi, se Alice prenota "La Pergola" due volte, il modello attuale non è in grado di catturare questa informazione.
Questo perché il modello attuale risponde solo all domanda: **"Quale persona ha prenotato quale hotel ?"**, 
ma non può rispondere a una domanda più specifica come:
**"Quante volte Alice ha prenotato l'hotel 'La Pergola'? "**
==Questo limite nasce dal fatto che l'associazione `prenota` collega direttamente `Persona` e `Hotel`, senza tenere traccia delle singole prenotazioni.== 
Per risolvere questo problema, dobbiamo introdurre una **classe aggiuntiva** che rappresenti la prenotazione stessa.
Quindi come si può sistemare questo diagramma, cosa gli manca? La classe `prenotazione`, per vedere quante volte 'alice' ha prenotato questo Hotel.
Questa classe quindi ci consente di gestire più prenotazioni della stessa persona presso lo stesso Hotel, perché agirà come "punto di collegamento " tra `Persona` e `Hotel`, permettendo di rappresentare più prenotazioni. 
#### Come funziona la classe `Prenotazione`
1. **La classe `Prenotazione`:**
	-  Rappresenta una singola prenotazione.
	- È collegata alla classe `Persona` attraverso un'associazione (es. `effettua`)
	- È collegata alla classe `Hotel` attraverso un'altra associazione (es. `riguarda`).
2. **Istanze di `Prenotazione`:**
   - Ogni istanza di `Prenotazione` rappresenta una prenotazione specifica 

> [!example] Esempio
>    e Alice prenota "La Pergola" due volte, avremo due istanze di `Prenotazione`, entrambe collegate a `alice:Persona` e `h1:Hotel`.

Quindi nel modello aggiornato:
![[La classe prenotazione.png]]
- `Prenotazione` è una classe che collega `Persona` e `Hotel`.
- Ogni prenotazione è un'istanza di questa classe, che tiene traccia di quante volte una persona ha prenotato un hotel.

> [!example] **Riassumendo:**
> La classe `Prenotazione` risolve il problema iniziale perché:
> 1. **Permette più prenotazioni**:  
  >  Ora possiamo rappresentare più prenotazioni della stessa persona presso lo stesso hotel, creando più istanze di `Prenotazione`.
 >   
>2. **Risponde a domande più specifiche**:  
  >  Il modello può ora rispondere a domande come:
  >  
  >  - "Quante volte Alice ha prenotato 'La Pergola'?"
  >      
 >   - "Quali sono le date delle prenotazioni di Alice?" (se aggiungiamo attributi come `data` alla classe `Prenotazione`).
 >       
>3. **Migliora la flessibilità del modello**:  
  >  La classe `Prenotazione` può essere estesa per includere ulteriori dettagli, come la data della prenotazione, il numero di ospiti, ecc.

Questo esempio ci mostra che:
A volte il costrutto di associazione è sufficiente :
In casi semplici (come l'associazione `autore` tra `Libro` e `Persona` ), un'associazione diretta tra due classi è sufficiente.
Altre volte serve una classe aggiuntiva:
In situazioni più complesse (come le prenotazioni multiple), è necessario introdurre una classe intermedia (es. `Prenotazione`) per modellare correttamente la realtà.

## Aggiungere più associazioni tra le classi 
==Nella modellazione concettuale, è possibile definire **più associazioni tra le stesse classi**, purché queste associazioni rappresentino relazioni di natura diversa.== 
Questo ci permette di modellare situazioni più complesse in cui due classi possono interagire in modi differenti.
![[aggiungere le associazioni tra le classi.png]]
Prendendo in riferimento l'immagine qui sopra, abbiamo 2 classi principali:
- **Libro**: con l'attributo `titolo: stringa`.

- **Persona**: con gli attributi `nome: Stringa` e `cognome: Stringa`.

Tra queste due classi, possiamo definire **due associazioni distinte**:
1. **`autore`**: 
   ==rappresenta il legame tra un libro e il suo autore.==

2. **`editore`**: 
   ==rappresenta il legame tra un libro e il suo editore.==

Queste due associazioni modellano relazioni diverse:
- L'associazione `autore` indica **chi ha scritto il libro**.

- L'associazione `editore` indica **chi ha pubblicato il libro**.

Nel [[#^inLevel|livello intensionale]] (livello delle classi e delle associazioni), definiamo la struttura del sistema:

- **Classi**:
    
    - `Libro`: 
      ==rappresenta un libro con un titolo.==
        
    - `Persona`: 
      ==rappresenta una persona con nome e cognome.==
        
- **Associazioni**:
    
    - `autore`: 
      ==collega un `Libro` a una `Persona` (l'autore del libro).==
        
    - `editore`: 
      ==collega un `Libro` a una `Persona` (l'editore del libro).== 
Mentre nel livello estensionale (livello degli oggetti e dei link), vediamo come queste classi e associazioni si concretizzano in istanze specifiche. Ecco alcuni esempi:

1. **Libri**:
    - `div_comm: Libro`: 
      ==un'istanza della classe `Libro` con titolo `"La divina commedia"`.==
        
    - `bio: Libro`: 
      ==un'istanza della classe `Libro` con titolo `"La mia grandiosa vita"`.==
2. **Persone**:
    
    - `dante: Persona`: 
      ==un'istanza della classe `Persona` con nome `"Dante"` e cognome `"Alighieri"`.==
        
    - `feltr: Persona`: 
      ==un'istanza della classe `Persona` con nome `"Faustino"` e cognome `"Feltrinelli"`.==
        
    - `modestino: Persona`: 
      ==un'istanza della classe `Persona` con nome `"Modestino"` e cognome `"Rossi"`.==
        
3. **Link**:
    - Il libro `div_comm` è collegato a `dante` attraverso l'associazione `autore` (Dante è l'autore della Divina Commedia).
        
    - Il libro `div_comm` è collegato a `feltr` attraverso l'associazione `editore` (Feltrinelli è l'editore della Divina Commedia).
        
    - Il libro `bio` è collegato a `modestino` attraverso l'associazione `autore` (Modestino è l'autore di "La mia grandiosa vita").

Questo sistema di definire più associazioni tra le stessi classi ci permette di:
1. **Modellare relazioni diverse**:  
    Ad esempio, una persona può essere sia un autore che un editore, ma queste sono due relazioni distinte che devono essere rappresentate separatamente.
    
2. **Rispondere a domande specifiche**:
    
    - "Chi è l'autore di questo libro?" → Risposta: Dante Alighieri.
        
    - "Chi è l'editore di questo libro?" → Risposta: Faustino Feltrinelli.
        
3. **Mantenere la chiarezza del modello**:  
    Separare le associazioni in base al loro significato rende il modello più comprensibile e facile da gestire.