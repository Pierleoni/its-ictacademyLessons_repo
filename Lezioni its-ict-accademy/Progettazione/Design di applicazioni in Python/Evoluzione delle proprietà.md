
# Introduzione 
 [[Design di applicazioni in Python|Nella scorsa lezione]] abbiamo visto come definire i tipi di dato, nel diagramma delle classi, per i tipi di dato  base di python o definiti da noi. 
Ora dobbiamo capire come evolvere le proprietà di un oggetto UML:
in generale, per proprietà di un oggetto si intende i suoi [[Analisi dei requisiti mediante UML#^proprietaDellaClasse|attributi]] e [[Analisi dei requisiti mediante UML#Cosa sono i link?|link]] i quali evolvono in maniera arbitraria durante i suo ciclo di vita.
## Evoluzione delle proprietà
Tuttavia esistono casi particolari che vanno presi in considerazione in fase di design:
1. Innanzitutto dobbiamo chiederci: quella/e proprietà rimangono statiche o mutano nel tempo?
   Per rispondere a questa domanda dobbiamo differenziare le proprietà mutabili e immutabili:
	- **Mutabile:** 
	  ==una proprietà di un oggetto si dice mutabile se il suo valore può mutare arbitrariamente durante il ciclo di vita dell'oggetto.==
	  In altre parole la/e proprietà dell'oggetto si evolve/evolvono nel tempo se quell'oggetto è in vita.
	- **Immutabili:** 
	  ==una proprietà dell'oggetto si dice immutabile se, una volta specificata, il suo valore resta invariato per tutto il ciclo di vita dell'oggetto.==
	  In altre parole una volta che è stato specificato il valore di quella proprietà, il suo valore resta invariato per tutto il ciclo di vita dell'oggetto.
	- **Mutabile ad evoluzione non vincolata:**
	  ==Una proprietà  si definisce mutabile ad evoluzione non vincolata se il suo valore non può mutare arbitrariamente (ad esempio il valore può solo crescere.).== 
2. Un altra domanda da porci è: la proprietà dell'oggetto può essere conosciuta oppure no al momento della sua nascita?
   (Ad esempio quando nasce l'oggetto di persona si conosce sicuramente il suo codice fiscale ma non il suo numero di matricola.)
   Per rispondere anche a questa domanda dobbiamo conoscere la differenza tra questi tre diversi tipi:
   - **Certamente nota alla nascita:** 
     ==se la  proprietà deve essere conosciuta nel momento in cui nasce l'oggetto.==
   - **Possibilmente non nota alla nascita:** 
     ==se la proprietà può essere sconosciuta nel momento in cui nasce l'oggetto (deve avere un vincolo di molteplicità `[0..1]`).==
   - **Certamente non nota alla nascita:** 
     ==se la proprietà è certamente sconosciuta nel momento in cui nasce l'oggetto (deve avere un vincolo di molteplicità `[0..1]`).==


### Esempio pratico
 Ad esempio, in un diagramma UML delle classi viene creata la classe `Corso` e una classe `Studente`:
 ![[Esempio diagramma delle classi Ristrutturato.png]]
  
  Innanzitutto in  un corso il numero di studenti che l'ha passato non lo si  conosce  appena creato l'oggetto di corso mentre il numero di matricola è certamente una proprietà immutabile dell'oggetto `studente`.
Quindi, come possiamo notare,  una dimensione sono se le proprietà di un oggetto sono immutabili, mutabili o mutabili ad evoluzione vincolata e un'altra dimensione sono  certamente nota alla nascita, possibilmente non nota alla nascita, certamente non nota alla nascita.

Infatti le proprietà di questo diagramma evolvono così:
![[Esempio diagramma delle classi ristrutturato_2.png]]

Per quanto riguardano le proprietà  della classe `Studente`:
- `indirizzo` è **mutabile** ma **possibilmente non noto alla nascita** perché uno studente può non avere un indirizzo (vedi il vincolo di molteplicità `[0..1]` sull'attributo).
-  `matricola` è **immutabile** ed è **un valore certamente noto alla nascita dell'oggetto studente**.
- `nome`: è **mutabile**(il nome di uno studente può cambiare) ed è **noto alla nascita.**
- `genere`: **mutabile,** e **noto alla nascita.** 

Mentre gli attributi della associazione di classe `esame`:
`data` e `voto` sono entrambi **immutabili** e **noti alla nascita** (questo perché la data e il voto di un esame non cambiano nel tempo e appena uno studente sostiene un esame entrambe le proprietà dell'oggetto esame si conoscono alla nascita dell'oggetto stesso).  

### Evoluzione delle proprietà: assunzioni di default
Sappiamo però che quando si parla di proprietà si parla anche di [[Analisi dei requisiti mediante UML#Cosa sono le associazioni?|associazioni]]: 
 
quando nasce studente non si hanno link verso esame, e mettiamo lo 0..* perché cosi stiamo dicendo che quando nasce l'oggetto studente non è certamente noto il corso superato.
Distinguiamo tra proprietà singole: attriutti o associazioni o meglio ruoli con molteplicità 1..1. Quindi tutte le propeità singole sono note alla nascita, tutte le proprietà 1..*
Mentre le molteplicità con lo 0 possono essere poss non note alla nascita 

Visibilità 
Nei ling di prog come anche UML esiste il concetto di visi delle prorpietà : se ho un oggetto qual'è sono le prorpeita sono visibili e quali no. In UML la visibilità si sudd in:
pubblico(`+`): quella prop è accessibile a tutti
prottetto(`#`): la prop è accessibile solo nella clase/assoc dove è definita e nelle sue sottoclassi e/o sotto-associazioni
privato(`-`): le prop sono accessibili solo nella classe/assoc dove è definita.


Prendiamo azienda 1:
creiamo un modello della class diagram 

> [!info] I nomi delle proprietà della classe e i nomi delle associazioni non vanno cambiati nel diagramma del modello delle classi


Questo ci aiuta per facilitarci l'implementazione in Python

