# Organizzare il codice
### Concetti principali:

1. **Funzioni per il Rendering di Immagini**: Viene creato un esempio di faccia neutra tramite funzioni come `create_oval()` e `create_line()` di Tkinter. Le forme geometriche vengono disegnate per formare occhi, pupille e bocca.
    
2. **Separazione delle Preoccupazioni**: Si esamina come separare le diverse preoccupazioni in funzioni distinte, come il rendering della faccia neutra e quella sorridente, ciascuna con una propria funzione. Questo aumenta la flessibilità e la riusabilità del codice.
    
3. **Vantaggi della Separazione**:
    
    - Ogni funzione si occupa di un solo compito, migliorando la chiarezza e la testabilità.
        
    - Permette di utilizzare soluzioni più modulari, facilitando l'aggiunta di nuove funzionalità.
        
4. **Problematiche nell'uso di Variabili Globali**: Viene mostrato come l'uso di variabili globali può causare problemi di gestione dello stato, specialmente quando modificato in più punti del programma. Ad esempio, la variabile `colour` mantiene il valore precedente di 'black' quando non viene resettata, portando a risultati indesiderati.
    
5. **Evita le Variabili Globali**: Si consiglia di evitare l'uso di variabili globali, preferendo invece di passare le informazioni tramite parametri tra funzioni. Ciò consente di tenere sotto controllo lo stato delle variabili e ridurre gli errori.
    
6. **Scope delle Variabili**:
    
    - _Scope globale_: Variabili definite all'inizio del programma e accessibili da tutte le funzioni.
        
    - _Scope locale_: Variabili definite all'interno di una funzione e accessibili solo dentro quella funzione.
        
    - L'importanza di limitare lo scope delle variabili per evitare conflitti o cambiamenti indesiderati nello stato del programma.
        
7. **Scoping e Buone Pratiche**:
    
    - Si suggerisce di utilizzare variabili locali e passare valori tramite parametri, evitando variabili globali per migliorare la chiarezza e la sicurezza del codice.
        
    - Si evidenzia come la definizione dei parametri all'interno delle funzioni consenta di creare soluzioni più modulari e facili da testare.
        

### Esempio di codice:

Il codice finale utilizza funzioni con variabili locali e passaggio di parametri per rendere una faccia neutra o sorridente. Ogni funzione si concentra su un singolo compito, come disegnare un ovale o una linea, migliorando la gestione del codice.

```run-python
def draw_oval(x1, y1, x2, y2, colour=None):
    if colour == None:
        c.create_oval(x1, y1, x2, y2)
    else:
        c.create_oval(x1, y1, x2, y2, fill=colour)

def draw_line(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2)

def draw_arc(x1, y1, x2, y2, s, e):
    c.create_arc(x1, y1, x2, y2, start=s, extent=e)

def render_neutral_face():
    draw_oval(50, 50, 120, 120)
    draw_oval(60, 60, 80, 80)
    draw_oval(65, 65, 75, 75, 'black')
    draw_oval(90, 60, 110, 80)
    draw_oval(95, 65, 105, 75, 'black')
    draw_line(70, 110, 100, 110)

def render_smiley_face():
    draw_oval(50, 50, 120, 120)
    draw_oval(60, 60, 80, 80)
    draw_oval(65, 65, 75, 75, 'black')
    draw_oval(90, 60, 110, 80)
    draw_oval(95, 65, 105, 75, 'black')
    draw_arc(60, 110, 110, 80, 0, -180)

```

Il modulo "wildcard" importa tutto automaticamente da un modulo. Questo dovrebbe essere evitato perché può inquinare il modulo cliente con nomi non necessari.

**Moduli riutilizzabili:**  
Molti moduli forniscono funzionalità per altri moduli (moduli di libreria). Un modulo riutilizzabile deve:

- Avere funzioni piccole, focalizzate su un'unica preoccupazione e con uno scopo chiaro.
    
- Il nome e la firma della funzione devono indicare chiaramente lo scopo.
    
- Non usare variabili globali, preferendo variabili locali.
    
- Fornire i dati necessari come parametri.
    
- Comportarsi sempre allo stesso modo per gli stessi input.
    

**Modulo eseguibile:**  
Alcuni moduli sono progettati per essere eseguiti come script standalone, non dovrebbero essere importati in altri moduli perché l'importazione dovrebbe non avere effetti visibili. Un modulo può essere reso sia una libreria che uno script, verificando il contesto di esecuzione con `if __name__ == '__main__':`.

**Esempio di uso di moduli:**  
Un esempio di script che richiede un input da parte dell'utente viene utilizzato solo come script, ma se importato come modulo, causerebbe l'esecuzione immediata del codice a livello superiore.

**Moduli come interfacce:**  
L'interfaccia di un modulo descrive le funzioni che espone, senza che il cliente debba conoscere i dettagli interni. Questo approccio consente di cambiare l'implementazione interna senza modificare il comportamento esterno del modulo. I vantaggi sono:

- Aggiornamenti più facili senza errori.
    
- Rischi ridotti di effetti indesiderati.
    
- Maggiore riusabilità e testabilità.
    

**Nascondere le informazioni nei moduli:**  
Il concetto di _information hiding_ implica nascondere i dettagli interni di un modulo, permettendo modifiche interne senza che il modulo cliente ne risenta. Un esempio concreto è quello di cambiare la libreria di disegno senza alterare il comportamento del programma, poiché il modulo cliente interagisce solo con l'interfaccia.

**Pacchetti:**  
Quando un programma cresce, i moduli vengono organizzati in pacchetti per raggruppare logicamente i moduli. Un pacchetto è una cartella con un file `__init__.py` che permette a Python di trattarlo come un pacchetto importabile. Esempio di struttura di pacchetti per un programma di disegno:

- `emoji/`
    
    - `drawing/`
        
        - `core_draw.py`
            
    - `rendering/`
        
        - `faces.py`
            
        - `weather.py`
            
        - `vehicles.py`
            

**Struttura tipica di un progetto:**  
Un progetto Python può essere strutturato con cartelle per il codice e per la documentazione, come ad esempio:

- `Projectname/`
    
    - `docs/`
        
    - `projectname/`
        
        - `package1/`
            
        - `package2/`
            
    - `README.txt`
        

**Riepilogo finale:**  
Una buona struttura è essenziale per mantenere il codice leggibile e facilmente modificabile. Separare le preoccupazioni, programmare in modo modulare, nascondere i dettagli interni dei moduli e usare pacchetti permette di gestire progetti complessi senza introdurre errori e facilitando la manutenzione del codice.


---

# Traduzione in inglese
This chapter focuses on organizing code by using functions to break tasks into smaller, reusable units. It emphasizes the importance of **separation of concerns**, where each part of the program handles a single responsibility, making the code easier to manage and test.

### Key Concepts:

1. **Functions**: Small, reusable units of code that make tasks more manageable.
    
2. **Separation of Concerns**: Different parts of the program should focus on one task, leading to better reusability and easier maintenance.
    
3. **Single Responsibility**: Functions should do one thing, like drawing the face or rendering specific components.
    
4. **Local Variables**: Avoid using global variables to reduce errors and scope issues. Instead, pass parameters to functions.
    
5. **Abstraction**: Keep the rendering logic separate from the drawing tools (e.g., Tkinter), improving flexibility.
    

The chapter explains the importance of using local variables and breaking tasks into simpler functions, avoiding the pitfalls of global variables, and keeping the code modular and maintainable.

**Reusability of Modules**  
Modules are designed to be reusable components, often provided by libraries like Python’s `datetime` module. To enhance the reusability of your own modules, it is recommended to:

- Provide functions that are small, focused on one task, and have a clear purpose.
    
- Ensure the function’s purpose is clear from its signature and is bolstered with documentation.
    
- Ensure functions are predictable by avoiding global variables and passing data via function parameters.
    
- Clearly document any behavior changes that may occur when the same input produces different results (e.g., depending on time of day).
    

**Executable Modules vs. Library Modules**  
When importing a module, its functions are set up to execute on request. However, some modules contain top-level code that runs immediately upon import. This behavior is undesirable for library modules, which should avoid causing unintended side effects when imported. To ensure proper behavior, use the `if __name__ == "__main__":` construct to prevent immediate execution when a module is imported.

**Example**  
A script that asks for the user’s birthdate and calculates their age could be imported as a library without asking for user input immediately by encapsulating the script's behavior inside the `if __name__ == "__main__":` block.

**Modular Approach and Separation of Concerns**  
The example of drawing faces using the `core_draw` module demonstrates how to separate concerns in code. By isolating drawing functionality in one module and rendering in others, the code becomes easier to maintain. If a drawing function needs to change, only the core module needs to be updated, and the rest of the code remains unaffected.

**Modules as Interfaces**  
A module's interface consists of its function signatures and documentation. It should hide the implementation details, allowing the user to interact with the module without knowing its internals. This approach provides benefits such as easier updates, reduced risk of errors, and better modularity and testability. For instance, changing the internal implementation of a drawing function does not affect client modules if the interface remains the same.

**Information Hiding**  
The principle of information hiding ensures that details about a module’s internal data structures are concealed from the user. This allows the module’s implementation to change without affecting the user. For example, if a drawing module switches from using `tkinter` to another library (`ultra_draw`), the core module's interface remains the same, and the rest of the code continues to work as before.

**Packages**  
As programs grow in complexity, organizing modules into packages becomes necessary. Packages are logical groupings of related modules, allowing for better organization and maintainability. Python packages are represented as directories containing modules and an `__init__.py` file to indicate that the directory is a Python package. Dot notation is used to import modules from packages (e.g., `emoji.drawing.core_draw`).

**Example of Package Structure**  
The emoji example is reorganized into a package with drawing and rendering subpackages, each containing related modules. The directory structure should include the `__init__.py` file in each folder to make it a package that can be imported by other code.

**Typical Package Layout**  
A typical project structure might look like this:

```
- Projectname/
  - docs/
  - install.txt
  - tutorial.txt
  - projectname/
    - package1/
      - __init__.py
      - module1_1.py
      - module1_2.py
    - package2/
      - __init__.py
      - module2_1.py
    - README.txt

```

For the emoji example, this structure would be:
```
- Emoji/
  - docs/
  - install.txt
  - tutorial.txt
  - emoji/
    - __init__.py
    - drawing/
      - __init__.py
      - core_draw.py
    - rendering/
      - __init__.py
      - faces.py
      - weather.py
      - vehicles.py
  - LICENCE.txt
  - README.txt
```

**Summary**  
Proper code structuring is essential for creating maintainable and error-free programs. The chapter introduced several principles, including separation of concerns, modular programming, information hiding, and package organization. By adhering to these principles, developers can build more reliable, reusable, and testable code.