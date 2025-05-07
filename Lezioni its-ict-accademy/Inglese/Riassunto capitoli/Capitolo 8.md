# Costruzioni efficaci
**1. Il comando `continue`:**  
Il comando `continue` permette al ciclo di saltare l'iterazione corrente e di passare immediatamente alla successiva. È utile quando certe condizioni sono soddisfatte e non è necessario completare il resto del corpo del ciclo.  
**Esempio:**

```run-python
numeri = [3, 8, 1, 9, 5]
numero_da_testare = 5
for n in numeri:
    if numero_da_testare > n:
        print('Maggiore di')
        continue
    if numero_da_testare < n:
        print('Minore di')
        continue
    if numero_da_testare == n:
        print('Uguale a')

```

In questo caso, se una delle prime due condizioni è vera, il ciclo salta il resto dei confronti e passa al numero successivo.

**2. Il comando `break`:**  
Il comando `break` viene utilizzato per uscire immediatamente dal ciclo quando viene soddisfatta una condizione. Questo è utile in scenari come un gioco di indovinare il numero, dove il ciclo dovrebbe fermarsi appena viene indovinato il numero corretto.  
**Esempio:**
```run-python
numero_computer = 9
indovinato = False
for tentativi in range(1, 6):
    numero_giocatore = input('Inserisci il tuo indovinello> ')
    if numero_computer == numero_giocatore:
        indovinato = True
        break  # Esce dal ciclo se l'indovinello è corretto
messaggio = 'Hai vinto!' se indovinato else 'Hai perso!'
print(messaggio)
```

In questo caso, il ciclo si fermerà non appena verrà indovinato il numero corretto.

**3. Stato del programma e variabili:**  
Lo stato del programma si riferisce ai valori correnti di tutte le variabili usate in un programma. Le variabili rappresentano lo stato e possono cambiare nel tempo. Gestire questi cambiamenti con attenzione è fondamentale per garantire il corretto comportamento del programma.

**Esempio di cambiamento dei valori delle variabili:**

```run-python
x = 42
print(x)  # Stampa 42
x = x + 1
print(x)  # Stampa 43
x = x * 2
print(x)  # Stampa 86
```

In questo esempio, la variabile `x` cambia mentre il programma viene eseguito.

**4. Assegnazione di variabili:**  
In Python, assegnare un valore a una variabile è come etichettare un valore in memoria. Quando una variabile viene riassegnata, essa punta semplicemente a una nuova posizione in memoria.  
**Esempio:**
```run-python
x = 42
nome = 'Arturo'
x = x + 1
```
Dopo l'esecuzione del codice sopra, lo stato del programma in memoria cambia, con `x` che ora punta a un nuovo valore.

**5. Mutabilità:**  
Le variabili in Python possono essere mutabili o immutabili. Gli oggetti immutabili (come numeri e stringhe) non possono essere modificati in loco, mentre gli oggetti mutabili (come le liste) possono esserlo.  
Per esempio, riassegnare una variabile come `x = 99` non cambia il valore di un'altra variabile `y` se `y` era stata assegnata al valore di `x` precedentemente:

```run-python
x = 42
y = x
x = 99
print(y)  # Stampa 42
```
**Oggetti mutabili vs immutabili:**

- **Oggetti immutabili:** Una volta creati, non possono essere modificati (es. interi, stringhe).
    
- **Oggetti mutabili:** Possono essere modificati in loco (es. liste).
**Esempio di mutazione di lista:**
```run-python
nomi = ['Tom', 'Dick']
nomi.append('Harry')
print(nomi)
```

Questo cambia la lista in loco senza creare una nuova copia di essa.

**6. Effetti collaterali con oggetti mutabili:**  
Quando si lavora con oggetti mutabili, i cambiamenti apportati a una variabile possono influire su altre variabili che puntano alla stessa posizione di memoria. Per esempio, quando si assegna una lista a un'altra, entrambe le variabili fanno riferimento alla stessa lista in memoria.

**Esempio:**

```run-python
note_1 = ['Do', 'Re', 'Mi']
note_2 = note_1
note_1.append('Fa')
print(note_2)  # Stampa ['Do', 'Re', 'Mi', 'Fa']
```
Qui, `note_2` viene influenzata dai cambiamenti fatti su `note_1` perché entrambe puntano alla stessa lista.

**7. Alternative immutabili:**  
Per evitare modifiche indesiderate alle variabili, considera l'uso di tipi di dati immutabili come le tuple. Questo garantisce che i dati originali vengano preservati.  
**Esempio:**
```run-python
numeri = (1, 2, 3)
print(numeri)  # Stampa (1, 2, 3)
```

Questo impedisce qualsiasi modifica alla tupla `numeri`.

**8. Buone pratiche:**

- Evita di alterare oggetti mutabili all'interno di funzioni, specialmente se i loro valori vengono passati come parametri. Un approccio più sicuro è creare una copia o usare una nuova collezione per memorizzare i valori modificati.  
**Esempio di approccio più sicuro:**

```run-python
def stampa_quadrati(nums):
    nuovi_nums = []
    for n in nums:
        nuovi_nums.append(n**2)
    print(nuovi_nums)

numeri = (1, 2, 3)
stampa_quadrati(numeri)  # Stampa [1, 4, 9] - Atteso

```

Questo evita di alterare la lista originale.

Un oggetto dovrebbe essere immutabile, a meno che tu non abbia una buona ragione per renderlo mutabile.  
In alternativa, usa tipi di dati immutabili equivalenti come le tuple (che impediscono modifiche in loco). Assicurati di sapere quali tipi di dati in Python sono mutabili e quali sono immutabili. L'Appendice A contiene un elenco dei tipi più comuni.

**Ordinamento delle Istruzioni**  
Oltre ai valori che cambiano, lo stato del programma richiede anche attenzione nell'ordinamento delle istruzioni. Possono sorgere problemi quando le operazioni vengono eseguite nell'ordine sbagliato. Ad esempio, ecco due modi di ottenere la lista dei numeri raddoppiati:
```run-python
def get_doubles_wrong(singles):
    doubles = []
    for n in singles:
        doubles.append(n)
        n = n * 2
    return doubles

def get_doubles_right(singles):
    doubles = []
    for n in singles:
        n = n * 2
        doubles.append(n)
    return doubles

print(get_doubles_wrong([1, 2, 3])) # Stampa [1, 2, 3]
print(get_doubles_right([1, 2, 3])) # Stampa [2, 4, 6]
```

La funzione "sbagliata" non funziona correttamente perché i numeri in Python sono immutabili. Quando raddoppi `n`, viene creato un nuovo valore a cui viene assegnato l'etichetta `n`. Il valore a cui `n` era associato inizialmente rimane invariato nella lista `doubles`. La funzione "giusta" funziona correttamente perché aggiorna il valore dell'oggetto prima di aggiungerlo alla lista.

Python fornisce i mezzi per evitare gli errori causati dall'ordinamento delle istruzioni e dalla gestione esplicita dello stato. Permette di riscrivere ciò che sarebbe stato un blocco di più righe come istruzioni singole e atomiche, ottenendo gli stessi risultati. Ad esempio, riscriviamo l'esempio precedente utilizzando una comprensione della lista:
```run-python
def get_doubles(singles):
    return [n * 2 for n in singles]

print(get_doubles([1, 2, 3])) # Stampa [2, 4, 6]

```

Questa versione ridotta di `get_doubles` è solo una riga di codice invece di cinque. Come scritto, la comprensione della lista può essere letta da sinistra a destra come "crea una nuova lista in cui ogni elemento, `n`, è moltiplicato per 2, prendendo gli elementi da un'altra lista chiamata `singles`." Una comprensione della lista gestisce la creazione della lista per noi. Dice solo come dovrebbe essere la lista risultante, senza spiegare come crearla.

**Costrutti più Avanzati**  
Questa sezione esplora costrutti più avanzati che ci permettono di evitare le difficoltà presentate dall'ordinamento delle istruzioni e dalla necessità di aggiornare continuamente i valori (discusso nella sezione precedente). Tuttavia, richiede la conoscenza dello stile di programmazione dichiarativo, che discuteremo ora.

**Stili di Programmazione: Dichiarativo vs Imperativo**  
Le ricerche mostrano che i programmatori esprimono istintivamente diverse parti delle loro soluzioni utilizzando stili diversi (Pane et al., 2001). Due stili di programmazione sono particolarmente evidenti nei risultati: dichiarativo e imperativo.

**Stile Dichiarativo**  
Questo stile enfatizza la dichiarazione di ciò che è e non è vero in una soluzione. Utilizza dichiarazioni logiche per articolare i fatti iniziali e i comportamenti della soluzione, nonché gli obiettivi della soluzione. In altre parole, dice cosa fa la soluzione, piuttosto che come lo fa. Esempi in un gioco di Noughts and Crosses (tris) includono:

- L'area di gioco è una matrice 3x3.
    
- 'Punteggio alto' è il punteggio più alto nella lista di tutti i punteggi.
    

Un esempio popolare dello stile dichiarativo è la programmazione funzionale, che enfatizza la scrittura di programmi composti da funzioni in stile matematico che spiegano cosa fa una funzione piuttosto che come lo fa. Inoltre, incoraggia a evitare l'uso dello stato mutabile (cioè variabili che cambiano nel tempo).

**Stile Imperativo**  
Lo stile imperativo è in contrasto con l'approccio dichiarativo. Si concentra sulla risoluzione di un problema esplicitando ogni passaggio nell'algoritmo. Ad esempio:

- Riproduci suono introduttivo. Mostra "Player 1 Get Ready".
    
- Mostra il simbolo del giocatore. Rimuovi la freccia che punta su "Player 1". Aggiungi la freccia che punta su "Player 2". Messaggio = "Player 2's turn". Mostra il messaggio. Aspetta 5 secondi. Rimuovi il messaggio.
    

**Confronto tra gli Stili**  
Diversi stili sono più adatti a determinati tipi di obiettivi:

- Lo stile dichiarativo funziona bene per impostare lo scenario della soluzione e delineare i vincoli.
    
- Lo stile imperativo viene utilizzato quando un programmatore ha bisogno di un controllo rigoroso sull'esecuzione dei passaggi, in particolare quando l'efficienza o l'ordinamento delle istruzioni è critico.
    

Potrebbe risultare una sorpresa poco piacevole scoprire che i linguaggi di programmazione spesso supportano principalmente solo uno stile. La maggior parte dei linguaggi popolari (come Java, C++, Ruby e JavaScript) sono principalmente imperativi. Tuttavia, ciò non significa che l'uso di un linguaggio imperativo ti limiti a uno stile 100% imperativo. I confini tra gli stili sono recentemente diventati più sfocati e alcuni linguaggi ora supportano in modo limitato anche altri stili. Python sta principalmente nel campo imperativo, ma supporta anche alcuni elementi di altri stili.

Come dimostrazione, consideriamo un programma che filtra una lista di numeri per rimuovere tutti i numeri dispari. Una soluzione imperativa potrebbe apparire così:

```run-python
old_list = [1, 2, 3, 4, 5]
new_list = []
for number in old_list:
    if (number % 2) == 0:
        new_list.append(number)
print(new_list)
```

Mentre una soluzione dichiarativa potrebbe apparire così:
```run-python
def is_even(n):
    return (n % 2) == 0
new_list = list(filter(is_even, [1, 2, 3, 4, 5]))
print(new_list)
```

Entrambe le soluzioni producono esattamente gli stessi risultati, ma i loro stili differiscono. Invece di dire al computer come fare il filtro (come fa la prima soluzione), la seconda soluzione chiede semplicemente alla funzione incorporata `filter` di farlo per noi.

**Vantaggi dello Stile Dichiarativo**  
Usare uno stile dichiarativo porta alcuni vantaggi. In primo luogo, il programmatore raramente deve utilizzare lo stato per controllare il flusso del programma, riducendo la quantità di stato da tenere traccia. In secondo luogo, gli oggetti immutabili sono tipicamente la norma. In terzo luogo, i blocchi di codice multi-riga possono essere ridotti a pochissime (a volte una sola) righe di codice, rendendo più facile capire un programma.

Anche se Python è principalmente nell'ambito imperativo, si presenteranno occasioni in cui utilizzare un approccio dichiarativo (come sostituire i cicli multi-riga con espressioni su una sola riga). È una buona idea perseguirle perché un approccio dichiarativo incoraggia a suddividere il programma in piccole funzioni riutilizzabili, prive di effetti collaterali. Di conseguenza:

- Il programma sarà complessivamente più piccolo.
    
- Sarà più facile ragionare sul comportamento del programma perché le sue parti sono piccole e autonome.
    
- Diventa più facile testare e fare debug.
    
- Alcune funzioni che crei saranno generiche, permettendoti di riutilizzarle ed esplorare i modelli nella tua soluzione.
    

**Comprehension**  
I programmi lavorano spesso con collezioni—oggetti che raggruppano più elementi. L'approccio usuale per gestire le collezioni in uno stile imperativo è usare un ciclo, ma come abbiamo visto, ciò può aggiungere complicazioni. Più importante, i cicli possono risultare non intuitivi per i principianti della programmazione.

In realtà, le persone scoprono che l'approccio più naturale per creare una collezione è semplicemente definirla—cioè dichiarare cosa dovrebbe sembrare, piuttosto che come dovrebbe essere creata. Confronta questa dichiarazione dichiarativa:

"Creare una lista di tutti i numeri pari tra 1 e 15."

Con la sua equivalente imperativa:

"Creare una nuova lista, `l`. Passare attraverso ogni numero, `n`, da 1 a 15. Per ogni `n`, se `n` è pari, aggiungerlo a `l`."

Python fornisce un modo per applicare l'approccio più intuitivo sotto forma di _comprehension_. Una comprehension è semplicemente un modo conciso di creare nuove collezioni a partire da quelle esistenti. Ecco un esempio che crea una lista di numeri quadrati da una lista di numeri:

```run-python
numbers = [1, 2, 3, 4, 5]
# 'n ** 2' = n elevato alla potenza di 2
squares = [n ** 2 for n in numbers]
print(squares) # Stampa [1, 4, 9, 16, 25]
```

Puoi anche filtrare gli elementi indesiderati dalla lista originale aggiungendo una clausola `if`. Il prossimo esempio include nella nuova lista solo i nomi di quattro lettere dalla lista originale e si assicura che i nomi siano correttamente capitalizzati:

```run-python
forenames = {'graham', 'john', 'eric', 'terry', 'michael'}
four_letter_pythons = {name.capitalize() for name in forenames if len(name) == 4}
print(four_letter_pythons) # Stampa {'Eric', 'John'}
```

**Funzioni di Ordine Superiore**  
Nel Capitolo 2, abbiamo fatto un'analogia tra gli algoritmi e le ricette. Entrambi descrivono una serie di passaggi che manipolano oggetti in vari modi. Le funzioni possono anche diventare parametri di altre funzioni. Ad esempio:
```run-python
def is_even(n):
    return n % 2 == 0
def is_positive(n):
    return n > 0
def test_numbers(test_function, numbers):
    return [test_function(n) for n in numbers]
evens = test_numbers(is_even, [1, 2, 3, 4])
positives = test_numbers(is_positive, [-2, -1, 0, 1, 2])
print(evens) # Stampa [False, True, False, True]
print(positives) # Stampa [False, False, False, True, True]
```

**Primitivi Funzionali**  
Quando si utilizzano funzioni di ordine superiore, ci sono tre operazioni in particolare che vengono eseguite così frequentemente da essere state assegnate a dei nomi propri. Insieme formano il nucleo di un approccio di programmazione funzionale e a volte sono chiamati _primitivi funzionali_:

- **Map**: Applica una funzione a tutti gli elementi di una collezione e mette i risultati in una nuova collezione.
    
- **Filter**: Crea una nuova collezione, includendo solo gli elementi che restituiscono `True` quando viene applicata loro una funzione di test.
    
- **Reduce**: Esegue un'operazione su ogni elemento di una collezione e produce un risultato singolo.
    

Python fornisce i primitivi funzionali incorporati. Ecco un esempio che usa `map` e `filter` insieme:

```run-python
nums = [1, 2, 3, 4, 5, 6, 7]
doubled_evens = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 0, nums)))
print(doubled_evens) # Stampa [4, 8, 12]
```
Questi concetti pongono le basi per le esplorazioni del prossimo capitolo sugli _abstract data types_ (tipi di dati astratti).

---
# Traduzione in inglese
## Effective Building Blocks
**The `continue` Statement:**  
The `continue` statement allows the loop to skip the current iteration and immediately start the next iteration. It’s helpful when certain conditions are met, and you don’t need to complete the rest of the loop body.  
**Example:**

```run-python
numbers = [3, 8, 1, 9, 5]
test_number = 5
for n in numbers:
    if test_number > n:
        print('Greater than')
        continue
    if test_number < n:
        print('Less than')
        continue
    if test_number == n:
        print('Equal to')

```

Here, if either of the first two conditions is true, the loop skips the rest of the comparisons and proceeds to the next number.

**2. The `break` Statement:**  
The `break` statement is used to exit the loop immediately when a condition is met. This is useful in scenarios like a number-guessing game where the loop should stop once the correct number is guessed.  
**Example:**
```run-python
computers_number = 9
guessed_correct = False
for guesses in range(1, 6):
    players_number = input('Enter your guess> ')
    if computers_number == players_number:
        guessed_correct = True
        break  # Exit the loop if the guess is correct
message = 'You win!' if guessed_correct else 'You lose!'
print(message)
```

In this case, the loop will stop as soon as the correct number is guessed.

**3. Program State and Variables:**  
Program state refers to the current values of all the variables used in a program. Variables represent state and can change over time. Managing these changes carefully is crucial for ensuring correct behavior in programs.

**Example of changing variable values:**
```run-python
x = 42
print(x)  # Prints 42
x = x + 1
print(x)  # Prints 43
x = x * 2
print(x)  # Prints 86
```
In this example, the variable `x` changes as the program runs.

**4. Assigning Variables:**  
In Python, assigning a value to a variable is like labeling a value in memory. When a variable is reassigned, it simply points to a new memory location.  
**Example:**
```run-python
x = 42
name = 'Arthur'
x = x + 1
```
After executing the above code, the state of the program in memory changes, with `x` now pointing to a new value.

**5. Mutability:**  
Variables in Python can be mutable or immutable. Immutable objects (like numbers and strings) cannot be modified in place, while mutable objects (like lists) can.  
For example, reassigning a variable like `x = 99` doesn't change the value of another variable `y` if `y` was assigned the value of `x` earlier:

```run-python
x = 42
y = x
x = 99
print(y)  # Prints 42
```
**Mutable vs Immutable Objects:**

- **Immutable Objects:** Once created, they can't be changed (e.g., integers, strings).
    
- **Mutable Objects:** Can be modified in place (e.g., lists).

**List Mutation Example:**
```run-python
names = ['Tom', 'Dick']
names.append('Harry')
print(names)
```
This changes the list in place without creating a new copy of it.


**6. Side Effects with Mutable Objects:**  
When dealing with mutable objects, changes made to one variable can affect others that point to the same memory location. For example, when you assign one list to another, both variables refer to the same list in memory.

**Example:**

```run-python
notes_1 = ['Do', 'Re', 'Me']
notes_2 = notes_1
notes_1.append('Fa')
print(notes_2)  # Prints ['Do', 'Re', 'Me', 'Fa']
```
Here, `notes_2` is affected by changes made to `notes_1` because both point to the same list.

**7. Immutable Alternatives:**  
To avoid unintended changes to variables, consider using immutable data types like tuples. This ensures that the original data is preserved.
**Example:**
```run-python
numbers = (1, 2, 3)
print(numbers)  # Prints (1, 2, 3)
```
This prevents any changes to the tuple `numbers`.


**8. Best Practices:**

- Avoid altering mutable objects inside functions, especially if their values are passed as parameters. A safer approach is to create a copy or use a new collection to store modified values.  
**Example of safer approach:**
```run-python
def print_squares(nums):
    new_nums = []
    for n in nums:
        new_nums.append(n**2)
    print(new_nums) 

numbers = (1, 2, 3)
print_squares(numbers)  # Prints [1, 4, 9] - Expected

```


This avoids altering the original list.

An object should be immutable unless you have a good reason for it to be mutable.  
Alternatively, use equivalent immutable data types like tuples (which forbid changes being made in-place). Make sure you know which data types in Python are mutable and which are immutable. Appendix A contains a list of the most common types.

**Statement Ordering**  
In addition to ever-changing values, program state also requires you to be mindful of instruction ordering. Problems can arise when things are done in the wrong order. For example, this shows two ways of getting your list of numbers doubled:

```run-python
def get_doubles_wrong(singles):
    doubles = []
    for n in singles:
        doubles.append(n)
        n = n * 2
    return doubles

def get_doubles_right(singles):
    doubles = []
    for n in singles:
        n = n * 2
        doubles.append(n)
    return doubles

print(get_doubles_wrong([1, 2, 3])) # Prints [1, 2, 3]
print(get_doubles_right([1, 2, 3])) # Prints [2, 4, 6]

```

The 'wrong' function works incorrectly because numbers in Python are immutable. When you double `n`, a new value is created that gets the `n` label. The value that `n` used to be attached to remains inside the `doubles` list unchanged. The 'right' function succeeds because it updates the object’s value before adding the resultant value to the list.

Python provides the means for avoiding the kinds of errors caused by statement ordering and explicit management of state. It allows you to rewrite what would be multi-lined blocks as single, atomic statements that yield the exact same results. For example, let’s rewrite the previous example using a list comprehension:

```run-python
def get_doubles(singles):
    return [n * 2 for n in singles]

print(get_doubles([1, 2, 3])) # Prints [2, 4, 6]
```
This reduced version of `get_doubles` is just one line in length instead of five. As written, the list comprehension can be read from left to right as "create a new list where each item, `n`, is multiplied by 2, sourcing the items from another list called `singles`." A list comprehension manages the creation of the list for us. It says only what the resultant list should look like; it says nothing about how to create it.

**More Advanced Constructs**  
This section explores more advanced constructs that allow us to avoid the difficulties presented by statement ordering and the need to continually update values (discussed in the previous section). However, it requires knowledge of the declarative programming style, which we’ll discuss next.

**Programming Styles: Declarative vs Imperative**  
Research shows that programmers instinctively express different parts of their solutions using different styles (Pane et al., 2001). Two styles of programming feature heavily in the results: declarative and imperative.

**Declarative Style**  
This style emphasizes declaring what is and isn’t the case in a solution. It uses logical statements to articulate the initial facts and behaviors, as well as the solution’s goals. In other words, it states what the solution does rather than how it does it. Examples in a Noughts and Crosses game include:

- The playing area is a 3 x 3 square.
    
- ‘High-score’ is the greatest score in the list of all scores.
    

A popular example of the declarative style is functional programming, which emphasizes writing programs made up of mathematical-style functions that explain what a function does instead of how it does it. It also encourages you to avoid using changeable (i.e. mutable) state.

**Imperative Style**  
The imperative style contrasts with the declarative approach. It focuses on solving a problem by explicitly spelling out each step in the algorithm. For example:

- Play intro sound. Display ‘Player 1 Get Ready.’
    
- Display player’s symbol. Remove arrow pointing at ‘Player 1’. Add arrow pointing at ‘Player 2’. Message = ‘Player 2’s turn.’ Display Message. Wait 5 seconds. Remove Message.
    

**Comparing the Styles**  
Different styles are better suited to certain types of goals:

- The declarative style works well in setting up the solution scenario and laying out the constraints.
    
- The imperative style is used when a programmer needs tight control over the execution of steps, particularly when efficiency or the ordering of instructions is critical.
    

It might come as an unpleasant surprise to learn that programming languages often primarily support only one style. Most popular languages (like Java, C++, Ruby, and JavaScript) are mainly imperative. However, this doesn’t mean using an imperative language restricts you to a 100% imperative style. Boundaries between styles have recently begun to blur, and some languages now include limited support for other styles. Python stands mainly in the imperative camp but also supports some elements of other styles.

As a demonstration, let’s consider a program that filters a list of numbers to remove all the odd ones. An imperative solution would look something like this:

```run-python
old_list = [1, 2, 3, 4, 5]
new_list = []
for number in old_list:
    if (number % 2) == 0:
        new_list.append(number)
print(new_list)
```
Whereas a declarative solution would look like this:
```run-python
def is_even(n):
    return (n % 2) == 0
new_list = list(filter(is_even, [1, 2, 3, 4, 5]))
print(new_list)
```

Both solutions have the exact same outcomes, but their styles differ. Instead of telling the computer how to do the filtering (as the former solution does), the latter solution simply asks the in-built `filter` function to do it for us.

**Benefits of the Declarative Style**  
Using a declarative style brings certain benefits. First, the programmer rarely has to use state to control the program flow, reducing the amount of state you need to track. Second, immutable objects are typically the norm. Third, multi-line code blocks can be reduced to very few (sometimes a single) lines of code, making it easier to understand a program.

Even though Python stands mainly in the imperative camp, opportunities to use a declarative approach (like replacing multi-line loops with single-line expressions) will present themselves throughout your programming. It’s a good idea to pursue them because a declarative approach encourages you to break your program into small, reusable functions possessing no side effects. As a consequence:

- The program will be smaller overall.
    
- It will be easier to reason about the program’s behavior because its parts are small and self-contained.
    
- Testing and debugging become easier.
    
- Some functions you create will be generic, allowing you to reuse them and exploit the patterns in your solution.
    

**Comprehensions**  
Programs often work with collections—objects that group together multiple items. The usual approach to handling collections in an imperative style is to use a loop, but as we've seen, this can add complications. More importantly, loops can be unintuitive to programming novices.

In reality, people find that the most natural approach to creating a collection is simply to define them into existence—i.e., to describe what they should look like, rather than how they should be created. Contrast this declarative statement:

"Create a list of all even numbers between 1 and 15."

With its imperative equivalent:

"Create a new list, `l`. Go through each number, `n`, from 1 to 15. For each `n`, if `n` is even, add it to `l`."

Python provides a means to apply the more intuitive approach in the form of comprehensions. A comprehension is just a concise way of creating new collections from existing ones. Here's an example creating a list of square numbers from a list of numbers:
```run-python
numbers = [1, 2, 3, 4, 5]
# 'n ** 2' = n to the power of 2
squares = [n ** 2 for n in numbers]
print(squares) # Prints [1, 4, 9, 16, 25]
```

You can also filter out unwanted items from the original list by adding an `if` clause. The next example includes in a new list only four-letter names from the old one and ensures the names are properly capitalized:
```run-python
forenames = {'graham', 'john', 'eric', 'terry', 'michael'}
four_letter_pythons = {name.capitalize() for name in forenames if len(name) == 4}
print(four_letter_pythons) # Prints {'Eric', 'John'}
```


**Higher-Order Functions**  
In Chapter 2, we drew an analogy between algorithms and recipes. Both describe a series of steps that manipulate objects in various ways. Functions can also become parameters to other functions. For instance:
```run-python
def is_even(n):
    return n % 2 == 0
def is_positive(n):
    return n > 0
def test_numbers(test_function, numbers):
    return [test_function(n) for n in numbers]
evens = test_numbers(is_even, [1, 2, 3, 4])
positives = test_numbers(is_positive, [-2, -1, 0, 1, 2])
print(evens) # Prints [False, True, False, True]
print(positives) # Prints [False, False, False, True, True]
```

**Functional Primitives**  
When using higher-order functions, three operations in particular are carried out so often that they’ve been given their own names. Together they form the core of a functional programming approach and are sometimes called functional primitives:

- **Map**: Applies a function to all items in a collection and puts the results in a new collection.
    
- **Filter**: Creates a new collection, including only the items that return True when a testing function is applied to them.
    
- **Reduce**: Performs an operation on each item in a collection and produces a single result.
    

Python provides the functional primitives built-in. Here's an example using `map` and `filter` together:
```run-python
nums = [1, 2, 3, 4, 5, 6, 7]
doubled_evens = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 0, nums)))
print(doubled_evens) # Prints [4, 8, 12]
```

These concepts set the foundation for the next chapter's explorations on abstract data types.