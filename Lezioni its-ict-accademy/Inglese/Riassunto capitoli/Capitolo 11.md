Nel Capitolo 11, l'attenzione è posta sui principi e sulle tecniche per una modellazione software efficace. I concetti chiave trattati sono la modellazione statica e dinamica, nonché i diversi tipi di diagrammi UML utilizzati per rappresentare il comportamento e la struttura del sistema.

**Concetti Chiave:**

1. **Modellazione Statica**: Questa riguarda la rappresentazione degli aspetti fissi di un sistema, come oggetti, attributi e relazioni. Un esempio di scacchiera illustra come un modello possa essere implementato utilizzando classi in Python, dove una classe `Square` rappresenta i singoli quadrati e una classe `Chessboard` li organizza in una scacchiera. Questo evidenzia il ruolo dell'aggregazione e della composizione nella modellazione, con la distinzione tra le due che è meno significativa in linguaggi come Python, che gestiscono automaticamente la creazione e la distruzione degli oggetti.
    
2. **Cambiamenti di Stato**: Nella modellazione dinamica, il capitolo discute come alcuni componenti di un sistema subiscano cambiamenti di stato nel tempo. Questo è particolarmente importante per prevedere il comportamento del sistema e garantire che i sistemi non entrino in stati non desiderati. I diagrammi delle macchine a stati (ad esempio, per modellare un tornello) sono utilizzati per rappresentare queste transizioni di stato, con elementi come stati iniziali, transizioni, stati e stati finali.
    
3. **Condizioni di Guardia e Attività**: Una macchina a stati più dettagliata può incorporare elementi aggiuntivi come attività `entry/`, `exit/`, e `do/` per modellare il comportamento del sistema mentre entra, esce o opera all'interno di un dato stato. L'esempio di un tornello a moneta mostra come queste attività vengano attivate e come le condizioni di guardia (dichiarazioni di verità) determinano le transizioni.
    
4. **Flussi di Lavoro e Diagrammi di Attività**: A differenza dei diagrammi delle macchine a stati, che si concentrano sullo stato di una singola entità, i diagrammi di attività sono utilizzati per modellare il flusso di controllo attraverso un sistema. Questi diagrammi enfatizzano decisioni, azioni e attività concorrenti in un processo. I diagrammi di attività forniscono una visione più globale, mentre i diagrammi delle macchine a stati si concentrano sul comportamento degli oggetti individuali.
    
5. **Diagrammi dei Casi d'Uso**: Questi diagrammi forniscono una visione centrata sull'utente di un sistema, mostrando quali azioni gli utenti possono eseguire. Rappresentano diversi tipi di utenti (attori) e le loro interazioni con le funzionalità del sistema (casi d'uso). I diagrammi dei casi d'uso sono particolarmente utili nelle fasi iniziali della progettazione del sistema, aiutando a chiarire i requisiti del sistema senza entrare nei dettagli del funzionamento interno del sistema.
    

**Caratteristiche della Modellazione**:

- **Astrazione**: I modelli semplificano i sistemi complessi concentrandosi sugli aspetti più rilevanti.
    
- **Comprensibilità**: I modelli efficaci sono facili da comprendere e richiedono meno sforzo rispetto al codice equivalente.
    
- **Accuratezza**: I modelli devono rappresentare con precisione il sistema.
    
- **Predittività**: Un buon modello prevede come si comporta un sistema in diverse condizioni.
    
- **Economia**: Creare un modello dovrebbe essere più conveniente rispetto alla costruzione del sistema reale.
    

**Scopo della Modellazione**:  
Lo scopo finale della modellazione è semplificare e comunicare idee complesse. Un modello dovrebbe aiutare a comprendere e progettare i sistemi, rendendo il processo di sviluppo più facile ed efficiente.

**Consigli Generali per la Modellazione**:

- Scegli il tipo di modello in base allo scopo e al pubblico.
    
- Un modello dovrebbe aiutare a chiarire la comprensione e a guidare la progettazione del sistema.
    
- Evita complessità inutili: i modelli dovrebbero essere semplici, chiari ed efficaci nel trasmettere informazioni.
    

**La Modellazione nella Pratica**:  
Sebbene la modellazione sia ampiamente utilizzata nell'industria del software, non è onnipresente. La tensione tra i modelli e il codice sorgente (cioè modellare un codice già esistente) può far sembrare la modellazione un passaggio superfluo. In molti casi, i modelli vengono utilizzati in modo informale, concentrandosi su parti specifiche di un sistema e spesso semplificati per evitare di sopraffare gli stakeholder con dettagli eccessivi.

In sintesi, il Capitolo 11 sottolinea che una modellazione efficace riguarda la creazione di rappresentazioni utili, comprensibili e praticabili di un sistema. L'uso dei diagrammi UML — sia per la modellazione statica che dinamica — aiuta gli sviluppatori a riflettere e comunicare la progettazione dei sistemi. L'obiettivo non è creare modelli troppo dettagliati, ma generare modelli astratti, chiari e predittivi che semplifichino il processo di sviluppo.

---
# Traduzione in inglese
## Effective modelling
In Chapter 11, the focus is on the principles and techniques for effective software modelling. The key concepts discussed are static and dynamic modelling, as well as the different types of UML diagrams used to represent system behaviour and structure.

**Key Concepts:**

1. **Static Modelling**: This involves representing the fixed aspects of a system, such as objects, their attributes, and their relationships. A chessboard example illustrates how a model can be implemented using classes in Python, where a `Square` class represents individual squares, and a `Chessboard` class organizes them into a board. This highlights the role of aggregation and composition in modelling, with the distinction between them being less significant in languages like Python, which handle object creation and destruction automatically.
    
2. **State Changes**: In dynamic modelling, the chapter discusses how certain system components undergo state changes over time. This is particularly important in predicting system behaviour and ensuring systems do not enter unintended states. State machine diagrams (e.g., modelling a turnstile) are used to represent these state transitions, with elements such as initial states, transitions, states, and end states.
    
3. **Guard Conditions and Activities**: A more detailed state machine can incorporate additional elements such as `entry/`, `exit/`, and `do/` activities to model the system’s behaviour as it enters, exits, or operates within a given state. The example of a card-operated turnstile shows how these activities are triggered and how guard conditions (truth statements) determine transitions.
    
4. **Workflows and Activity Diagrams**: Unlike state machine diagrams, which focus on the state of a single entity, activity diagrams are used to model the flow of control through a system. These diagrams emphasize decisions, actions, and concurrent activities in a process. Activity diagrams provide a more global view, whereas state machine diagrams focus on individual objects’ behaviours.
    
5. **Use Case Diagrams**: These diagrams provide a user-centric view of a system, showing what actions users can perform. They represent different types of users (actors) and their interactions with system functionalities (use cases). Use case diagrams are particularly useful in the early stages of system design, helping clarify system requirements without detailing the internal workings of the system.
    

**Modelling Characteristics**:

- **Abstract**: Models simplify complex systems by focusing on the most relevant aspects.
    
- **Understandable**: Effective models are easy to understand and require less effort than equivalent source code.
    
- **Accurate**: Models must accurately represent the system.
    
- **Predictive**: A good model predicts how a system behaves under various conditions.
    
- **Inexpensive**: Creating a model should be more cost-effective than building the actual system.
    

**Purpose of Modelling**:  
The ultimate purpose of modelling is to simplify and communicate complex ideas. A model should help in understanding and designing systems, making the development process easier and more efficient.

**General Modelling Advice**:

- Choose the model type based on the purpose and the audience.
    
- A model should help clarify understanding and guide system design.
    
- Avoid unnecessary complexity—models should be simple, clear, and effective in conveying information.
    

**Modelling in Practice**:  
While modelling is widely used in the software industry, it is not ubiquitous. The tension between models and source code (i.e., modelling an already existing code) can make it feel like an unnecessary extra step. In many cases, models are used informally, focusing on specific parts of a system, and often simplified to avoid overwhelming stakeholders with excessive detail.

In summary, Chapter 11 emphasizes that effective modelling is about creating useful, understandable, and actionable representations of a system. The use of UML diagrams—whether for static or dynamic modelling—helps developers think through and communicate the design of systems. The goal is not to create overly detailed models, but rather to generate abstract, clear, and predictive models that simplify the development process.