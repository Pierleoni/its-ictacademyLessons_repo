
La fase di design è quella criciale tra l'analisi e l'implementazione 
L'analisi segue metodologie
Il desgin invece non segue un inquardamento canonico
- Introduce elementi e oggetti 
- Definisce e responsabilità 
- Usa concetti come indipendenza, flessivililità, riuso...
Cosa si intende dunque per un buon design? 
Il bravo programmatore è colui che ne capisce di analisi e programmazione del software. 
Ma quindi come si fa a dire che un diagramma UML  sia ben fatto o meno? In realta non c'è una metrica su cui passarsi a differenza del livello di Implementazione dove si capisce molte volte a occhio di errori etc.
Quindi il lavoro del progettista non è smeplice perché non essendoci una metrica di giudizio o paragone eventuali a errori non saltano subito all'occhio ma spesso escono fuori durante l'implementazione. 
### Le metriche 
Affrontare un problema, in generala siginifica risolverolo 

#### Un processo induttivo
Per risolvere i "problemi" della vita, il nostro cervello utilizza da smepre la deduzione logica e i modelli
Quello che fa la differenza è l'esperienza, "allenamento"!!
Il cervello umano infatti identifica in modo incoscio le strutture simili. gli schemi(pattern) ricorrenti

Il principio è : 
una situazione "gia vissuta"
- se riconosciuta
- può essere gestita grazie all'espereinze maturata 
I desgin pattern sono modelli/approcci di progettazione consolidati negli anni.
In questo modo si hanno dei punti di riferimento. 
Pensiamo ad esempio quando si usano algoritmi che non implementiamo noi, ad esempio il bubble sort che fa da punto di riferimento per tutti i programmatori che devono ordinare elementi all'interno di una lista. 
Quindi il progettista deve riconoscere la situazione per sapere quale pattern usare.
Difatto i pattern quindi non hanno la pretesa di invientare nulla!
Sono solo le pratiche di buon senso frutto dell'esperienza. 

Processo induttivo
1. Identifico una famiglia di probelmi simili 
2. Trovo una soluzione "comune"
3. Opero un'analisi e astraggo la soluzione dal contesto
Con il temrine pattern


### Ruolo dei pattern 
Dal punto di vista delle archittetture a software, i design pattern
- diminuiscono i rischi 
- incrementa la produttiva 
- aumentano la standaridizzazione 
- favoriscono un più alto livello di qualità 
### Alexander: un archittetto 
Christopher Alexander fu 


### Desgin pattern (in archittetura)
Un pattern descrive il nucleo di una soluzione relativa un problema che compare frequentemente in un dato contesto 
Il modello della solzione deve essere strutturato in modo che "si posso usare tale soluzione un milione di volte, senza mai farlo allo stesso modo"

### Gamma: un progettista 
Erich Gamma è un informatico svizzero è noto come co-autore del libro Design Pattern: Elementi per il riuso di sfotware ad oggetti 

Nel 1981 consegue un dottorato a Zurigo su Design Pattern 
Nel 1995 guadagna vasta fama nell'ambiente della Programmazzione OO (publicazione del libro Design Pattern insieme alla **GoF**)
Ha dato un importante.

#### Un design Pattern(Gamma)
Un pattern software è : 
una soluzione provata ed ampiamente applicabile ad una particolare problema di progettazione descritta in una forma standard che possa essere facilmente riusata 
"Descrizione di classi e oggetti "


#### Il Libro del GoF
Il libro "Design Patterns": 
è considerata la "bibbia" sui pattern

Primo libro che: 
- Applica concetti di design pattern all'OOP
- individua i principali pattern 
È catalogo di 23 pattern, descritti per: 
- Nome 
- Problema 
- Soluzione 
- Conseguenze 


### Tipi di pattern
Le principali categorie di pattern sono 
- Archittetturali 
- progettuali (micro-architetture)→ GoF
- Idiomi (basso livello, legati al linguaggio)
#### Pattern progettuali 
Sono quelli comunemente 


#### Idiomi
Sono pattern di basso livello.
Sono specifici per un linguaggio 




## Pattern structural 
### Adapter 
Problema: 
Convertire l'interfaccia di una data classe in una interfaccia nota al Client(non inteso come Client nell'archittetura Client -  Server).
Supponiamo di avere una classe `Impiegato` che volgiamo ri-adattare che si trova in un certo progetto chiamato `PRJ1`. Ma adesso abbiamo un altro progetto `PRJ2` e volgio riadattare la classe `Impiegato` per questo progetto, ovviamente senza riscriverla o fare il copia-incolla 
QUindi la solluzione è scrivere un adattatore che adatta la classe `Impiegato` di `PRJ1` con l'interfaccia di `PRJ2` che concettualemente ha una relazione is-a con la classe 
`Impiegato`. 

Una analogia che possiamo usare è l'adattotore di corrente.

#### Diagramma Adapter versione Object


#### 1) Adapter 
Conseguenze: 
- Riutilizzo di classi esistenti 
- Mascheramenteo di dettagli implementativi al client 
- Alta responsabilità dell'adattore concernente creazione e gestione 


#### 2 ) Pattern Strategy
Problema 
- un programma deve fornire più varianti di un algoritmo, di un comportamento, di un criterio
- I diversi comportamenti devono restare indipendenti dalle classi che li utilizzano. 
Soluzione: 
- Definire l'interfaccia Strategy e poi realizzare classi concrete che incapsulano la logica degli algoritmi 
- Prevedere meccanismi dinamici di scelta e configurazione degli algoritmi da parte della classe di contesto (utilizzatrice delle strategie).
Un caso d'uso e quando utilizzando un `TreeSet` che stora oggetti della classe `Prodotto`, si definisce una classe `ProdComp<Prod>` in cui si implementa il metodo `compare(Pr,Pr)` poichè questa classe implementava l'interfaccia funzionale `Comparator`.
Poi quando nasce il `TreeSet` tramite costruttore si passa il `Comparator` 
Anche i metodi delle Stringhe ricalcoano il pattern Strategy. 

