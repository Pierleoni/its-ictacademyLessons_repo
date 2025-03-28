 
Le classi in python e quindi anche gli oggetti sono un concetto astratto, ci sono delle differenze tra Python e la progettazione.
in fase di analisi ci concentriamo sulle classi che sugli oggetti:
==gli oggetti servono essenzialmente per descrivere elementi singoli particolarmente significativi==
==oppure per descrivere esempi.== 
È un approccio simile al paradigma della programmazione [[Introduzione a Python#Object-Oriented|objected-oriented]] (es:[[Introduzione a Python|Python]], Java,etc.).
==Quindi un programma si scrive definendo un insieme si classi (o class), non di oggetti poiché questi vengono creati, modificati e distrutti durante l'esecuzione del programma.== 
In UML ci sono tanti costrutti delle classi e degli oggetti ma ne andremmo ad escluderne molti in modo di avere un significato univoco per ogni diagramma. 
## Cos'è un oggetto in UML
Un oggetto (istanza di una classe) in UML modella un elemento del dominio di analisi :

> [!deep]- **Significato di Dominio di analisi**
>  ==è l'insieme degli oggetti di interesse che si trovano nella porzione di mondo che il sistema deve rappresentare==

- un oggetto "ha vita propria": 
  ==cioè  può essere interpretato e compreso indipendentemente dagli altri oggetti del sistema e si risolve indipendentemente dagli altri oggetti.== 
un oggetto in UML è: se prendo un telefono e l'ho metto in uno spazio nero quel telfono ha vita propria perché ha le sue app, il suo orario, etc. e se lo metti in relazione ad altri oggetti simili costituisci una classe.
Una data non è un'oggetto, perché se prendi una data ad esempio 3/05/2025 questa data da sola non dice nulla e quindi va a costituire un tipo di dato, non un oggetto.

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
![Oggetto in UML](file:///C:/Users/Project%20Lead/OneDrive/Documents/Programmazione/Its-ict%20academy/Lezioni%20its-ict-accademy/img/Progettazione%20IMG/Progettazione(Lezione2)_Analisi%20dei%20requisiti%20in%20UML/Oggetto%20in%20UML.pdf.png)

















Prendendo questa immagine come riferimento possiamo notare:
- **div_comm:** 
  ==è l'identificatore dell'oggetto== (scelto
dall’analista per potersi riferire all’oggetto nello
schema concettuale)
- **Libro:**
  è la classe più specifica di cui l'oggetto è istanza 
- **La sottolineatura**

==Due oggetti (istanze) rappresentano due cose distinte nel mondo.==
La classe sono insieme di oggetti  omogenee (tutti gli oggetti hanno qualcosa in comune): hanno in comune gli attributi (il valore viene attribuito all'oggetto) e le dinamiche (operazioni, le vedremo in seguito).
Ogni classe è descritta da:
- **nome:** gli oggetti in Uml per convenzione sono al singolare 
- **Insieme di proprietà:** 
  ==astrazioni delle proprietà comuni degli oggetti che sono istanze delle classi.== 
![Primo esempio|493x158](https://i.imgur.com/uOjGmpA.png)

Abbiamo la classe `Libro`, che possiede un attributo `titolo` di tipo `Stringa`. Questo significa che ogni oggetto creato a partire dalla classe `Libro` dovrà avere un valore (uno solo) per l'attributo `titolo`, e questo valore dovrà essere una stringa.

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

- Il **livello intensionale:** 
  ==è rappresentato dalla classe `Libro`, che definisce l'attributo `titolo` di tipo `Stringa`.== 
  Questo stabilisce che ==ogni istanza della classe `Libro` dovrà necessariamente avere un attributo `titolo` con un valore di tipo stringa.==
- Il **livello estensionale:** 
  ==è costituito dalle istanze `div_comm` e `bio`, che sono oggetti concreti della classe `Libro`.== Questi oggetti possiedono valori specifici per l'attributo `titolo`: `"La Divina Commedia"` per `div_comm` e `"La mia grandiosa vita"` per `bio`.
In altre parole, il livello intensionale riguarda **la progettazione** (definizione delle classi), mentre il livello estensionale riguarda **l'implementazione concreta** (gli oggetti creati nel sistema).

### Identità degli oggetti o delle istanze 
Quando lavoriamo con oggetti in programmazione e modellazione UML, è cruciale comprendere la differenza tra due concetti che spesso vengono confusi:

>Un conto è dire che A e B sono **uguali** un conto e dire che A e B **sono la stessa cosa**.

La frase sopra ci dà un'anteprima di questo concetto, andiamo ad analizzarla meglio:
1. **Essere la stessa cosa (Identità):**
   L'identità di un oggetto è la sua "carta d'identità" univoca nel sistema.
   Due riferimenti che puntano:
    - **Allo stesso oggetto fisico in memoria** vuol dire che **hanno la stessa identità**
2. **Avere gli stessi valori (Uguaglianza):** 
   Due oggetti distinti possono:
	- **Condividere valori identici** per alcuni attributi, il che vuol dire che **sono uguali.** 

Per chiarire meglio i concetti di identità e uguaglianza:

> [!example] Esempio dei gemelli : Identità
> 
>
>Immaginiamo due gemelli omozigoti.  
>Condividono **aspetto fisico, DNA, età, genere e cognome**, eppure sono due entità distinte. La loro **identità** è unica perché:
>
>1. **Hanno nomi diversi**, che fungono da primo identificatore distintivo.
>2. **Occupano spazi fisici separati**: anche se simili, non possono essere lo stesso individuo.
>3. **Sviluppano personalità diverse nel tempo**, rendendo ancora più evidente la loro unicità.
>
>Anche in un sistema informatico, due oggetti possono avere molte caratteristiche in comune, ma la loro **identità è definita da un identificatore univoco**, che permette di distinguerli indipendentemente dagli attributi.


> [!example] **Esempio degli omonimi: Uguaglianza**
>
>Ora consideriamo due persone con lo stesso **nome e data di nascita**.  
>Hanno in comune **il nome, il giorno, il mese e l’anno di nascita**, che sono attributi dell’istanza `Persona`, ma **restano due oggetti distinti** perché:
>
>- **Hanno cognomi diversi**, il che basta per distinguerli.
>- Anche se **avessero lo stesso cognome**, rimarrebbero comunque due persone separate.
>
> **Punto chiave:**  
>L'identità **non si basa solo sugli attributi visibili**, ma su un **identificatore unico** (come un codice fiscale o un ID interno a un database).


È possibile avere due oggetti distinti che però condividono lo stesso valore per un determinato attributo.

![Le istanze diverse con lo stesso attributo ](https://i.imgur.com/MCqQRib.png)


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
- L'associazione è direzionata: la freccia indica "il verso di lettura del nome" (facoltativo).
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

Al contrario degli oggetti, però, i link non hanno identificatori espliciti: ==un link è implicitamente==
==identificato dalla coppia (o in generale dalla ennupla, v. seguito) di oggetti che esso rappresenta.==
Ciò implica, ad esempio, che il seguente diagramma degli oggetti non è ammesso dal diagramma delle classi.
![](https://i.imgur.com/xqYQtO3.png)
Questo diagramma dice che un Libro non puo modellare l'istanza della stessa persona perché non avrebbe senso.
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



---
## Vincoli di molteplicità sulle associazioni e sugli attributi 

I diagrammi delle classi visti finora ci permettono di rappresentare la realtà attraverso entità (classi) e relazioni (associazioni). ==Tuttavia, queste rappresentazioni sono spesso **troppo generiche** e non catturano pienamente i vincoli logici e concettuali che esistono nel mondo reale.==

Ipotizziamo che si deve progettare un sistema che registra la data di nascita di un impiegato in una città, come abbiamo negli esempi riportati nelle immagini sopra i modelli concettuali definiti finora **permettono configurazioni che potrebbero non essere realistiche,** questo perché senza vincoli precisi il modello accetta qualsiasi combinazione che sia formalmente corretta, anche se **non ha senso dal punto di vista logico.** 
Se guardiamo l'immagine riportata qui sotto ad esempio, possiamo vedere che:
![](https://i.imgur.com/PR5bO1D.png)

1. **Livello Intensionale (in alto)**

- Il modello concettuale prevede due classi:
    
    - `Impiegato`, con gli attributi `nome` e `cognome`.
        
    - `Città`, con l’attributo `nome`.
        
- L’associazione `nascita` collega un `Impiegato` a una `Città`, indicando dove è nato l’impiegato.
2. **Livello Estensionale (in basso):**
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
    Solo il **numero di collegamenti** in un'associazione tra classi.  
    Esempio:
     
- Uno studente può essere iscritto a _molti_ corsi (`*`), ma ogni corso deve avere _almeno uno_ studente (`1`).
        
- **Limite**:  
    Non controllano il contenuto degli attributi o altre regole complesse.
    

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
 **==A quanti [TARGET] è collegato un [SOURCE] tramite [ASSOCIAZIONE]?==**.
 
 ##### **Legenda della Frase**
 
 1.**Source (Classe Sorgente):** 
 ==È la classe da cui parte l'associazione (il punto di partenza del "link").==   
Corrisponde alla classe **di cui stiamo analizzando le relazioni** quando formuliamo domande del tipo;
 *A quanti \[target] può essere collegato un \[source].*  
 ^sourceClass
 
 
 2.**Target (Classe di destinazione):** 
 ==È la classe **a cui arriva l'associazione** (il punto di destinazione del "link").==   
Corrisponde alla classe **di cui vogliamo contare gli oggetti collegati** al source.    ^b5cc77

3. **Associazione:** [[#^associationsDef|vedi la definizione]] 

Detto ciò, in questo caso le domande da porci sono: 
 1. **==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite l'associazione `nascita`?==**
    - **[[#^sourceClass|Classe Sorgente]]**:   `Impiegato` (partenza dell'associazione)
    - **[[#^b5cc77|Classe target]]:** `Citta` (destinazione)
    - **[[#^associationsDef|Associazione]]**: `nascita`
	- La risposta è `1..1` perché ogni impiegato **può essere nato in una sola città**.
	- Questo vincolo garantisce che non possano esistere due città diverse associate alla stessa persona tramite l'associazione "nascita".

2. **"A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite il link `nascita`?"** 
	-  **[[#^sourceClass|Classe Sorgente]]**: `Città` (partenza dell'associazione)
	- **[[#^b5cc77|Classe target]]:** `Impiegato` (destinazione)
	- **[[#^associationsDef|Associazione]]**: `nascita`
	-   La risposta è `0..*` perché una città **può avere un numero qualsiasi di impiegati nati al suo interno**.
	- Questo significa che una città potrebbe non avere alcun impiegato associato oppure averne moltissimi.

Prendiamo come esempio anche questa immagine 

![](https://i.imgur.com/dgHnOYY.png)
Nel [[#^inLevel|livello intensionale]] ci sono due classi:
- `Persona`: ha un attributo  `nome` di tipo `stringa`
- `Automobile`: ha un attributo `targa`, presumibilmente di tipo `stringa`
La relazione tra `Persona` e `Automobile` è chiamata **"possiede"** ed è caratterizzata da un vincolo di molteplicità **`0..*`** dal lato di `Automobile`.
Nel [[#^exLevel|livello estensionale]] , difatti, possiamo notare che:
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
1. "==A quanti oggetti della classe `Prenotazione` può essere collegato un oggetto della classe `Hotel` tramite l'associazione `hotel_prenotato`?**=="
	  
	- **[[#^sourceClass|Classe Sorgente (source)]]:** `Hotel`(partenza dell'associazione).
	- **[[#^b5cc77|Classe Target]]:** `Prenotazione` (destinazione).
	- **[[#^associationsDef|Associazione]]:** `hotel_prenotato`. 
	**Ergo:** Un hotel può avere **zero, una o più prenotazioni** nel tempo.  
	**Risposta:** `0..*` (zero o più prenotazioni per ogni hotel).
	
2) . "**==A quanti oggetti della classe `Hotel` può essere collegato un oggetto della classe `Prenotazione` tramite l'associazione `hotel_prenotato`?==**"
	- **[[#^sourceClass|Classe sorgente (source)]]:** `Prenotazione` (partenza dell'associazione)
	- **[[#^b5cc77|Classe Target]]:** `Hotel` (destinazione)
	- **[[#^associationsDef|Associazione]]:** `hotel_prenotato`
    **Ergo:** Una prenotazione è sempre riferita **a un solo hotel**.  
    **Risposta:** `1..1` (ogni prenotazione è associata a un solo hotel).
    

> [!done] **Risultato**
> - `Hotel` → `0..*` `Prenotazioni`
>     
> - `Prenotazione` → `1..1` `Hotel`

Passando alla seconda coppia di classi (associazione `cliente_persona`): 
Qui dobbiamo porci le seguenti domande:
3) "**==A quanti oggetti della classe `Persona` può essere collegato un oggetto della classe `Prenotazione` tramite `cliente_prenotazione`?==**"
	- **[[#^sourceClass|Classe Sorgente (source)]]:** `Prenotazione` 
	- **[[#^b5cc77|Classe Target]]:** `Persona` (destinazione)
	- **[[#^associationsDef|Associazione]]:** `cliente_prenotazione`
	**Ergo:** Una prenotazione può essere effettuata da **una sola persona** (di solito il titolare della prenotazione).  
	- **Risposta:** `1..1` (ogni prenotazione ha un solo cliente associato).
	
4) "**==A quanti oggetti della classe `Prenotazione` può essere collegato un oggetto della classe `Persona` tramite `cliente_prenotazione`?==**"
	 - **[[#^sourceClass|Classe Sorgente (Source)]]:** `Persona`
	 - **[[#^b5cc77|Classe Target]]:** `Prenotazione` (destinazione)
	 - **[[#^associationsDef|Associazione]]:** `cliente_prenotazione`
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
1. "**==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite l'associazione `nascita`?==**"
   - **[[#^sourceClass|Classe sorgente(source)]]:** `Impiegato`(partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Città` (destinazione)
   - **[[#^associationsDef|Associazione]]:** `nascita`. 
   **Ergo:** Una persona può essere nato in una sola città.
   **Risposta:** `1..1` (ogni persona ha solo una città di nascita).
   
2. "**==A quanti oggetti della classe `Città` può essere collegato un oggetto della classe `Impiegato` tramite l'associazione `residenza`?==**"
   - **[[#^sourceClass|Classe sorgente(source)]]:** `Impiegato` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Città`(destinazione)
   - **[[#^associationsDef|Associazione]]:** `residenza`
   **Ergo:** Una persona può risiedere in una sola città.
   **Risposta:**`1..1`(ogni persona ha solo una citta di residenza).
   
3. "**==A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite l'associazione `nascita` ?==**"
   - **[[#^sourceClass|Classe sorgente (source)]]:**`Città` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:**`Impiegato` (destinazione)
   - **[[#^associationsDef|Associazione:]]**`nascita` 
   **Ergo:** Una città può essere la citta di nascita di nessuna o di una o di più persone.
   **Risposta:** `0..*`(ogni città ha nessuna, una o più persone che vi sono nati).
   
4. "**==A quanti oggetti della classe `Impiegato` può essere collegato un oggetto della classe `Città` tramite l'associazione `residenza`?==**"
   - **[[#^sourceClass|Classe sorgente (source)]]:** `Città` (partenza dell'associazione)
   - **[[#^b5cc77|Classe Target]]:** `Impiegato` (destinazione)
   - **[[#^associationsDef|Associazione]]:** `residenza`
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
**Risposta:** ogni oggetto sovrano può partecipa con il **ruolo di** `predecessore` al link della associazione successione da 0 a 1 volta.

![|423x188](https://i.imgur.com/9EY4OaU.png)

Ogni sovrano d quanti sovrano può essere successore?0, se è il primo della dinastia o  1
Ongi sovrano di quanti sovrani è il predecessore? 0 se è il primo della dinastia o 1

Il problema è il sovrano può essere predecessore di se stesso( esempio Napoleone Bonaparte)? Si 

La Riflessività: Padre di me stesso
La simmetria: A padre di B e B padre di C
