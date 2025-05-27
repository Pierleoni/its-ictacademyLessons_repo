
# Introduzione 
 [[Design di applicazioni in Python|Nella scorsa lezione]] abbiamo visto come definire i tipi di dato, nel diagramma delle classi, per i tipi di dato  base di python o definiti da noi. 
Ora dobbiamo capire come evolvere le proprietà di un oggetto UML:
==in generale, per proprietà di un oggetto si intende i suoi [[Analisi dei requisiti mediante UML#^proprietaDellaClasse|attributi]] e [[Analisi dei requisiti mediante UML#Cosa sono i link?|link]] i quali evolvono in maniera arbitraria durante i suo ciclo di vita==.  ^propDiClasse
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
Sappiamo però che quando si parla di proprietà si parla anche di [[Analisi dei requisiti mediante UML#Cosa sono le associazioni?|associazioni]] tra classi.
Per mantenere il diagramma delle classi ristrutturato leggibile e velocizzare la fase di design, adottiamo le seguenti assunzioni di default:
Innanzitutto quando nasce l'oggetto della classe `Studente` esso non ha link verso l'oggetto della classe `Esame`, mettendo il vincolo di molteplicità `0..*` diciamo che quando nasce l'oggetto studente non è certamente noto il corso superato.
Di conseguenza dobbiamo distinguere tra 
- **proprietà singole:** 
attributi (di classe o di associazioni) e associazioni (o meglio ruoli) con molteplicità `1..1`. 
- **proprietà con molteplicità minima pari a zero:**
  attributi (di classe o di associazioni) e associazioni (o meglio ruoli) con molteplicità `0..1`, `0..*`, `0..2`, etc.
Detto ciò le nostre assunzioni di default, ovvero che valgono in assenza di ulteriori elementi, sono:
- Tutte le proprietà sono mutabili
- Le proprietà singole (`1..1` ) o quelle con molteplicità minima pari a 1 (come ad esempio `1..*`) sono note alla nascita (questo per via della molteplicità `1..1`).
- Le proprietà con molteplicità minima pari a 0 sono possibilmente non note alla nascita 

I valori diversi dai default vengono contrassegnati nel diagramma con la dicitura `<<immutable>>` o nota UML ([[Esempio diagramma delle classi ristrutturato_2.png|vedi l'immagine sopra]]).


---
# Visibilità delle proprietà 
Come abbiamo visto per Python nelle rispettive lezioni [[Ereditarietà delle classi]], alla paragrafo [[Ereditarietà delle classi#Gli attributi protetti|Gli attributi protetti]], e nella lezione [[Public, Private and Class Attibutes, Class and Static Methods]], la visibilità degli attributi di una classe può variare in base a cosa si vuole rendere pubblico, privato o protetto.
Questa scelta va fatta proprio in fase di design, 

### Visibilità 
Nei linguaggi di programmazione, come anche UML, esiste il concetto di visibilità delle proprietà (o attributi) : se ho un oggetto quale sono le proprietà  visibili e quali no. 
In UML la visibilità si suddivide in:
- **pubblico(`+`):** 
  ==La proprietà è accessibile anche dal di fuori della classe/associazione dove è definita.==  
  In altre parole quella proprietà è accessibile a tutti. ^attrUMLpubblici
- **protetto(`#`):** 
  ==la proprietà è accessibile solo nella classe/associazione dove è definita e nelle sue sottoclassi e/o sotto-associazioni.==  ^attrUMLprotetto
- **privato(`-`):** 
  ==le proprietà sono accessibili solo nella classe/associazione dove è definita.==   ^attrUMLprivato


Prendiamo [[Esercitazione Azienda 1]]:
Dopo aver fatto il diagramma delle classi andiamo a ristrutturarlo.
![[img/Progettazione IMG/Class Diagram Design.png]]

Da questa immagine come si può vedere da questo diagramma:
tutti i tipi di dati sono stati riscritti in tipi di dati immutabili di Python (ad esempio `str`), mentre i valori di `stipendio` e `budget`, i cui valori erano `float > 0` sono stati specializzati in Python tramite una classe chiamata `RealGEZ`. 
Inoltre sono state usate le note per identificare le [[#Evoluzione delle proprietà assunzioni di default|assunzioni di defualt]]: 
infatti come possiamo vedere i vincoli di molteplicità sulle associazioni con con molteplicità minima pari a 0 sono tutti "certamente non noto alla nascita". 
Fatta eccezione per il vincolo dell'attributo `indirizzo`, che è "certamente noto alla nascita": questo perché quando nasce l'oggetto `dipartimento`, nasce sicuramente con un indirizzo che potrebbe essergli levato in seguito (il vincolo `[0..1]` sull'attributo, bisogna ricordare, che sta indicare che il valore di quell'attributo è opzionale).
Come ultimo dettaglio, da notare come è in fase di design che si decide se gli attributi devono essere privati (`-`), protetti(`#`) o pubblici (`+`), in questo caso si è deciso che gli attributi devono essere pubblici.

> [!info] I nomi delle proprietà della classe e i nomi delle associazioni non vanno cambiati nel diagramma del modello delle classi



