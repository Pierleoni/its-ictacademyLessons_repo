
# Introduzione
Abbiamo finito di parlare dei dati (informazioni forniti nel sistema), adesso introduciamo le funzionalità.
Oltre al diagramma delle classi in UML che fornisce i tipi di dati e operazioni che il sistema deve usare, viene redatto anche un ulteriore diagramma chiamato diagramma UML degli use case: 
questo tipo di diagramma modella le funzionalità che il sistema deve realizzare, in termini di use-case (cioè scenari di utilizzo).

## Use-case
==Il diagramma UML degli use-case **cattura un insieme omogeneo di funzionalità** accedute da un gruppo omogeneo di utenti.== 
Tipicamente coinvolge concetti rappresentati da più classi e associazioni del diagramma delle classi.
In sostanza risponde al quesito:
**Come utilizzo questo sistema (scenari di utilizzo) e chi può utilizzare questo sistema?** 
Quindi questo tipo di diagramma modella ==gli utenti esterni (o attori) che possono essere umani o sistemi esterni che utilizzeranno il sistema che stiamo progettando==.

### Cos è un attore
==Un attore è un ruolo che può esser giocato da un essere umano o da un sistema.== 
Da notare come l'utente può ricoprire i diversi ruoli (es: i ruoli all'interno di un sistema informativo di una università possono essere amministrativo(visualizzare i voti di tutti), docenti, studenti, etc.)
==Il ruolo attore può essere interpretato da diversi utenti, ma la persona può avere diversi ruoli==. 

### Diagramma UML degli Use-case
Più specificatamente un diagramma UML degli use case é un grafo:
Un grafo è una struttura molto comune in informatica, rappresenta una **rete** di elementi (detti **nodi**), che sono collegati a coppie da **archi**.
Un esempio molto comune di grafo è una mappa della rete metropolitana:
![[Rete metropolitana.png]]
Come possiamo vedere in questa immagine un nodo è la fermata metro di una linea poichè collega più linee della metro tra loro, mentre l'arco è la linea della metro in se che collega le diverse fermate tra loro.
Infatti questa logica è usata anche nei diagrammi UML degli use-case;
- un **nodo rappresenta:**
	- attori e use case
- **Gli archi rappresentano:**
	- la possibilità per un attore di invocare uno use-case
	- la possibilità per uno use-case di invocare un altro use-case
	- la generalizzazione tra attori e tra use-case

Quindi, in sostanza, gli archi di un diagramma degli use case sono le associazioni

> [!fail] Da non vedere come  le [[Analisi dei requisiti mediante UML#Cosa sono le associazioni?|associazioni]] del diagramma delle classi.


### Diagramma degli use-case: associazioni
In questo diagramma le associazioni o archi:
==modellano la possibilità di accesso, da parte di un attore, alle funzionalità di uno use-case==.

![[Dimostrazione di un diagramma use-case.png]]
In questa immagine, infatti, possiamo vedere come l'arco o associazione `utilizza` modella la possibilità di acceso da parte di un attore, `utente`, nel modello use case, quindi può accedere a tutte le possibilità degli use-case; ovvero a `Strumenti venditore`.

Da notare come Il diagramma degli  use-case è molto vago o ad alto modello, rispetto al diagramma delle classi.

> [!danger] ==Il fatto che esiste l'attore utente non è detto che nel diagramma delle classi esiste la classe utente, viceversa se esiste la classe `Utente`, nel diagramma delle classi, non è detto che esista l'attore `utente` nel diagramma degli use-case==. 

Quindi le classi e gli attori non hanno nulla a che vedere tra loro, in questo diagramma interessa di sapere chi usa il sistema.

#### Esempio

Il sistema deve permettere agli studenti di iscriversi, via web, ai corsi offerti. 
La segreteria deve poter assegnare i docenti ai singoli corsi. 
I docenti devono poter inserire i risultati dei test degli studenti: tali test sono somministrati agli studenti utilizzando il sistema.
![[Esempio di un diagramma degli use-case.png]]
Come mostra questa immagine:
- Abbiamo l'attore `Studente` che accede all'use-case `Gestione iscrizioni`:  
	  è l'insieme di funzionalità che permettono l'iscrizione web da parte degli studenti, ovvero singole operazioni racchiuse in un use case omogeneo.
- Inoltre l'attore uno `Studente`, e l'attore `Docente` possono entrambi accedere all'use-case `Gestione test`:
  è l'insieme di funzionalità che permettono la creazione, la somministrazione e la valutazione dei test, cioè singole operazioni racchiuse in un use case omogeneo.
-  Abbiamo l'attore `Segreteria` che accede all' use -case `Gestione docenti`:
	è l'insieme di funzionalità  che permettono l'assegnazione dei docenti ai corsi, etc. Singole operazioni racchiuse in un use case omogeneo

Tuttavia questo diagramma è comunque troppo vago, per una serie di motivi:
1. **Granularità troppo elevata (troppo generico):**
	   Gli use-case come `Gestione iscrizioni` o `Gestione test` **racchiudono molte operazioni distinte** (es: compilazione modulo, invio richiesta, ricezione conferma, valutazione, creazione domande, ecc.) ma queste **non sono esplicitate** nel diagramma.
	   Quindi questo diagramma non chiarisce quali sono le singole funzionalità disponibili all'interno di uno use-case.

2. **Assenza di relazioni tra use-case:** 
	   In questo diagramma manca completamente l'uso di [[#^93c45c|inclusioni]] ed [[#^extend|estensioni]]: 
		  -  ==Nel diagramma non è chiaro se certe operazioni **dipendano da altre** (es: “valutare un test” può avvenire solo **dopo** la “somministrazione” )==.
		 -   In più non è modellata la **riusabilità** tra use-case (es: "Autenticazione" potrebbe essere comune a più operazioni ma non è visibile).
	Quindi il diagramma ha come limite quella della **modularità** e la possibilità di **riutilizzo** del comportamento comune tra più use-case.

3. **Accesso indiscriminato da parte degli attori:**
	Come evidenziato nel riquadro viola dell'immagine, sia **studenti** che **docenti** hanno accesso completo all'use-case `Gestione test`, senza distinzioni.
	 ==Il diagramma **non distingue i comportamenti specifici** di ogni attore. In realtà, lo studente effettua il test, mentre il docente lo **valuta** o lo **crea**. Sarebbe più corretto scomporre l'use-case “Gestione test” in operazioni distinte con relazioni specifiche per ogni attore.== 

In conclusione serve un diagramma più dettagliato, per ovviare a questo problema si usano due costrutti:
- `<<include>>`: 
	  ==per **includere obbligatoriamente** un use-case in un altro, quando un comportamento è condiviso o ripetuto.==   
     ^93c45c
- `<<extend>>`: 
	  ==per **aggiungere opzionalmente** un comportamento a un use-case, attivato solo in certe condizioni.==  
	  ^extend


### Introduzione a `<<include>>` e `<<extend>>`
Quindi per specificare come gli utente (o attori) usano nel dettaglio i vari use-case (ovvero se sono operazioni **obbligatorie,** **riutilizzabili,** o **opzionali**), e come accedono **allo stesso use-case** vengono usati `<<include>>` ed `<<extend>>` per migliorare la precisione, permettendo così di rappresentare in modo più modulare e dettagliato il comportamento del sistema.
#### L'inclusione
In sintesi il costrutto `<<include>>` si applica quando:
==alcune funzionalità del case A può hanno bisogno di accedere ad alcune funzionalità  del case B.==
![[Esempio del costrutto include.png]]

In questo esempio sia i case `Somministrazione Test` che il case `Creazione` e valutazione test possono **usare** le funzionalità del case `Gestione Test`. 

> [!example] Analogia con Python
> Possiamo pensare al costrutto `<<include>>` come all’istruzione `import` in Python:
> ==Quando uno use-case ha bisogno di accedere alle funzionalità di un altro, lo “include”, proprio come in Python si usa `import` per accedere alle funzioni o classi definite in un altro modulo.==
>Questa inclusione rappresenta una **dipendenza obbligatoria**:  
> se A include B, **A non può funzionare senza B**.  
>Allo stesso modo, se in Python una funzione usa elementi da un modulo esterno, l’`import` è **necessario** per farla funzionare correttamente.

 
#### L'estensione
Se `<<include>>` è come  `import` in Python, possiamo vedere [[#^extend|`<<extend>>` ]] come un **plugin o un modulo opzionale:**
==Serve per aggiungere un comportamento **facoltativo**, attivabile solo in determinate condizioni.==
Viene applicata quando: 
==lo use-case A estende lo use-case B, in alcuni casi particolari, in cui alcune funzionalità di A sono migliorate, estese anche a B.==
La direzione della dipendenza:
Lo use-case **esteso** (A) **non dipende** direttamente dallo use-case che lo estende (B), ma è quest'ultimo ad "agganciarsi" a A se necessario.
Quindi il verso della dipendenza:
==va dallo use-case B (che estende) ad A (che è esteso).==


![[Esempio di extend.png]]
In questo esempio:
1. ==Gli studenti possono iscriversi a corsi==.
2. ==Durante il processo di iscrizione, gli studenti possono optare per il pagamento online==.
Il pagamento online non è obbligatorio ma è un opzione che estende il comportamento di `Iscrizione`. 


> [!example] Analogia con l'accesso a Gmail
> Possiamo pensare a `<<extende>>` come al comportamento dell'accesso all'account personale di Gmail:
>  Lo use-case principale è "**Accesso all'account Gmail**" (con email e password).
>  In **certi casi** l'utente può:
> - usare l’**accesso con impronta digitale**,
  >  
>- ricevere un **codice sul telefono**,
  >  
>- usare il **login automatico da dispositivo riconosciuto**.
>Queste opzioni di accesso aggiuntive non sono obbligatorie, ma estendono il comportamento dell'accesso classico, solo se disponibili o attivate.
> In sostanza `Accesso Gmail` è lo use-case **esteso** (base), mentre `Accesso con impronta`, `Accesso da dispositivo riconosciuto` sono use-case **che estendono** lo use-case base.


### Generalizzazione tra use case
Nei diagrammi UML degli use-case possiamo generalizzare tra i diversi use-case nei casi in cui:
==alcune funzionalità dello use-case A, solo in alcuni casi particolari, sono rimpiazzate con le funzionalità dello use-case B.== 
![[Generalizzazione tra use-case.png]]


In questo esempio:
le funzionalità del case `Identificazione`, in alcuni casi, vengono sostitute dal case `Controllo password` o in alcuni casi dal case `Accesso biometrico a varco`. 
Detto in altre parole:
1. Gli studenti devono potersi identificare
2. L’identificazione online avviene tramite password
3. La registrazione delle presenze ai corsi avviene tramite impronta digitale/iride
scansionata dal lettore del tornello.

> [!NOTE] Nota: nei diagrammi degli use-case non si possono usare generalizzazioni uniche che coinvolgono più sotto-usecase, né tantomeno vincoli [[Generalizzazioni#Vincoli sulle generalizzazioni `{disjoint}` e `{complete}`|`{disjoint}`]] e [[Generalizzazioni#Vincoli sulle generalizzazioni `{disjoint}` e `{complete}`|`{complete}`]].
> 


### Generalizzazione tra attori
Si possono usare anche le generalizzazioni tra i diversi attori, nel caso in cui:
l'attore B può fare le veci dell'attore A, e ne eredita tutte le associazioni.
Ad esempio:
![[Generalizzazione tra attori.png]]
L'attore `Manager`, che accede allo use-case `Analisi economiche` può fare le veci dell'attore `Segreteria` e quindi accedere a tutti gli use-case accessibili dalla Segreteria.
Quindi in sostanza:
 ==se B è A (se Manager è segreteria), tutti gli attori B possono sostituire gli attori A==. 


> [!caution] Il diagramma non implica che esistano le classi Segreteria e Manager nel diagramma delle classi, né tantomeno che la classe Manager sia una sottoclasse di Segreteria


### Specifica dello use-case
Il diagramma degli use-case è molto semplice, e dà solo una visione di alto livello di:
-  quali attori possono usare il sistema
-  quali macro-funzionalità sono accessibili ai diversi attori
-  Definisce inoltre come le diverse macro-funzionalità vadano modularizzate
-  Si tratta di un diagramma facilmente comprensibile anche al committente
-  Il diagramma non definisce le singole operazioni all’interno di ogni use-case
-  Ogni use-case del diagramma andrà affiancato da un [[Documenti di specifica|documento di specifica]] che entra nel dettaglio 
