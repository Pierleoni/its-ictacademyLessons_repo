 
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

È possibile che esistono due oggetti distinti che pero hanno lo stresso valore dell'attributo 
![[Screenshot 2025-03-20 at 12-33-20 Meet - bmb-xnne-ahh.png]]

Non è il fatto di avere le stresse prorprietà che mi dice che l'oggetto è lo stessso ma dipende dall'identificatore.
Possiamo avere due oggetti perosona con lo stesso nome e cognome ?SI, pero l'identificativo deve essere diverso, se l'identificativo è diverso non posso farlo. 

Il secondo elemento che ci serve è cpaire come le classi e gli oggetti interagiscono tra loro, quindi parliamo di link e correlazzioni.
![[Screenshot 2025-03-20 at 12-36-05 Meet - bmb-xnne-ahh.png]]

Un associazione è la possibilita che due oggetti siano o meno in relazione uno con l'altro, ad esempio l'associazione autore modella il fatto che il legame tra libro e persona mi dice che se il nome della Persona è correllata al libro allora quella persona è l'autore. 
L'associazione è una relazione tra due classi, le istanze delle associazioni tra due classi si chiamano link. 
Se l'associazione lega la classe C1 e C2 il link invece collega un oggetto della classe C1 a un oggetto della classe C2.
Infatti quello sotto è un link che lega div_comm con dante. 
Non si immette un identificatore in un link perché in UML, non possono esistere due link che legano la stessa coppia di oggetti:
Ad esempio div_comm e Dante sono legati con un link tra l'associazione Libro o autore o non sono legati perché non ha senso rispondere di "si" alla stessa domanda, questo è anche il motivo del perché il link non ha un identificatore perché è implicitamente identificato dalla coppia di oggetti che rappresenta. 

Si vuole progettare che permetta ai clienti di prenotare hotel via web:
le classi qui sono `hotel`, `clienti` e come moddeliamo il fatto che il clienti prenoti l'hotel, con un link:
 ![[Screenshot 2025-03-20 at 12-47-02 Meet - bmb-xnne-ahh.png]]
Cosa modella l'associazione prenota? Modella la possibilità che un oggetto della classe Persona e della Classe Hotel siano in relazione.
Questo è il livello intensionale.
A livello estensionael 
![[Screenshot 2025-03-20 at 12-48-28 Meet - bmb-xnne-ahh.png]]

A quale domanda risponde l'estensa di quel link prenota? 
E se io volessi rappresentare una seocnda prenotazione di 'alice' presso h1? Non si può fare, quei due link prenota non può essere fatto in UML, ma io volgio che la persona possa prenotare due volte lo stesso hotel. 
In questo caso il diagramma è inadatto anche perché io volevo riposnedere alla doamnda "Quantwe volte alice ha prenotato questo Hotel?".
Ora come si può sistemare questo diagramma, cosa gli manca? La classe `prenotazione` per vedere qunate volte alice ha prenotato questo hotel. 
Quindi in partenza non abbiamo individuato la classe prenotazione:
![[Screenshot 2025-03-20 at 12-54-22 Meet - bmb-xnne-ahh.png]]
Nel livello sotto abbiamo 
Abbiamo imparato che alcune volte il costrutto di associazione basta (come nell'esempio libro), ma certe volte il costrutto da solo n basta e serve la classe(come in questo caso la classe `prenotazione`). 

Tra le stessi classi possono essere definte più associazioni, che modelllano legami di natura diversa.

![[Screenshot 2025-03-20 at 13-02-42 Meet - bmb-xnne-ahh.png]]


