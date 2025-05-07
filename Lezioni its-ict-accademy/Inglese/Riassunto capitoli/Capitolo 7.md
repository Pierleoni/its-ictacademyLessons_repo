
### **Tutorial per principianti di Python**

**Obiettivi:**

- Imparare a usare il Prompt dell'interprete.
    
- Introdurre i tipi di base come numeri, stringhe, valori booleani e liste.
    
- Spiegare gli operatori aritmetici di base, l'assegnazione e i confronti.
    
- Mostrare come aggiungere commenti al codice.
    
- Spiegare come Python usa l'indentazione per definire la struttura.
    
- Dimostrare cosa è una funzione a un livello base.
    

**Introduzione a Python:**

- Il capitolo copre le basi di Python necessarie per comprendere gli esempi in Part II del libro.
    
- Python 3 è la versione utilizzata in questo tutorial.
    
- È possibile eseguire Python direttamente dal prompt dei comandi o tramite file di testo.
    

**Primi Passi:**

- Per eseguire Python, apri il terminale e digita `python` per entrare nel Prompt dell'interprete.
    
- Puoi inserire le istruzioni Python una alla volta, che verranno eseguite immediatamente.
    
- Puoi anche scrivere il codice in un file `.py` e eseguirlo tutto insieme.
    

**Tipi di Dati di Base:**

- **Numeri**: es. 7, 42, 3.14.
    
- **Stringhe**: sequenze di caratteri, racchiuse tra virgolette singole o doppie.
    
- **Booleani**: True o False.
    
- **Liste**: sequenze di elementi come `[1, 2, 3]`.
    

I valori possono essere assegnati a variabili (es. `the_number = 3`). Le variabili consentono di eseguire operazioni su set di dati diversi.

**Operazioni di Base:**

- Aritmetiche: somma (`+`), sottrazione (`-`), moltiplicazione (`*`), divisione (`/`), esponenziazione (`**`), e modulo (`%`).
    
- Confronti: uguaglianza (\==\), maggiore di (`<`), minore di (`>`).
    

Esempi di operazioni: `x = 3`, `print(x == 3)` mostrerà True, mentre `print(9 < 4)` mostrerà False.

**Funzioni:**

- Una funzione è una sequenza di istruzioni racchiuse in un blocco, che può essere chiamata quando necessario.
    
- In Python, una funzione è definita con la parola chiave `def` e può restituire valori usando `return`.
    

Esempio di funzione che stampa "Hello, World!":
```python
def output_hello():
    print('Hello, World!')
```

Le funzioni possono prendere parametri per lavorare con dati esterni, come nel caso di `output_message(msg)` e `multiply(x, y)`.

**Commenti:**

- I commenti iniziano con il simbolo `#`. Python li ignora durante l'esecuzione del codice.
```python
# Questo è un commento. Python lo ignora.
```
**Riassunto:**

- Dopo aver letto questo capitolo, dovresti essere in grado di scrivere programmi base in Python, sia tramite il Prompt dell'interprete che in un file di codice.


---
# Traduzione in inglese

### **Python Beginners' Tutorial**

**Objectives:**

- Learn how to use the Interpreter Prompt.
    
- Introduce basic types like numbers, strings, booleans, and lists.
    
- Explain basic arithmetic operators, assignment, and comparisons.
    
- Show how to add comments to code.
    
- Explain how Python uses indentation to denote structure.
    
- Demonstrate what a function is, at a basic level.
    

**Introducing Python:**

- The chapter covers the basic Python knowledge needed to understand the examples used in Part II of the book.
    
- Python 3 is the version used in this tutorial.
    
- You can run Python directly from the command prompt or through a text file.
    

**First Steps:**

- To run Python, open the terminal and type `python` to enter the Interpreter Prompt.
    
- You can enter Python instructions one at a time, and they will be executed immediately.
    
- Alternatively, you can write your code in a `.py` file and run it all at once.
    

**Basic Data Types:**

- **Numbers**: e.g., 7, 42, 3.14.
    
- **Strings**: Sequences of characters, enclosed in either single or double quotes.
    
- **Booleans**: True or False.
    
- **Lists**: Sequences of items like `[1, 2, 3]`.
    

Values can be assigned to variables (e.g., `the_number = 3`). Variables allow you to perform operations on different sets of data.

**Basic Operations:**

- Arithmetic: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), exponentiation (`**`), and modulo (`%`).
    
- Comparisons: equality (\==\), greater than (`<`), less than (`>`).
    

Examples of operations: `x = 3`, `print(x == 3)` will display True, while `print(9 < 4)` will display False.

**Functions:**

- A function is a sequence of instructions packaged as a block, which can be called when needed.
    
- In Python, a function is defined with the keyword `def` and can return values using `return`.
    

Example of a function that prints "Hello, World!":

```python
def output_hello():
    print('Hello, World!')
```

Functions can take parameters to work with external data, like in the case of `output_message(msg)` and `multiply(x, y)`.

**Comments:**

- Comments start with the `#` symbol. Python ignores them during code execution.
    

Example of a comment:

```python
# This is a comment. Python will ignore it.
```

**Summary:**

- After reading this chapter, you should be able to write basic Python programs, either through the Interpreter Prompt or in a source file.