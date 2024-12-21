# Python  

==Python è un **linguaggio di programmazione di alto livello, interpretato e orientato** agli oggetti,== noto per la sua semplicità e leggibilità.  
Per queste ragioni, Python è un linguaggio di programmazione ideale sia per principianti che per sviluppatori esperti.

**Linguaggio di alto livello**: I linguaggi di alto livello sono simili all'inglese e facili da apprendere e utilizzare.  
Le istruzioni in un linguaggio di programmazione di alto livello sono chiamate _istruzioni_ (statements).

Ecco, ad esempio, un'istruzione in un linguaggio di alto livello che calcola l'area di un cerchio:  
`area = 5 * 5 * 3.1415`.  

**Linguaggio interpretato**:   
==Un linguaggio interpretato utilizza un programma chiamato interprete, che traduce un linguaggio di alto livello una istruzione alla volta in linguaggio macchina e poi esegue il programma.==  
==L'interprete individuerà diversi tipi di errori e interromperà l'esecuzione del programma quando ne viene rilevato uno.==

**Linguaggio macchina**:   
==Le istruzioni sono sotto forma di codice binario.== Ad esempio, per sommare due numeri, potresti dover scrivere un'istruzione in codice binario, come questa:  
`1101101010011010`.  
**La Programmazione Orientata agli Oggetti (OOP):**   
==è un paradigma di programmazione che organizza il codice in oggetti, che sono entità che combinano dati (chiamati attributi) e comportamenti (chiamati metodi), semplificando l'organizzazione del codice e rendendolo più modulare e riutilizzabile.==  
**Le principali caratteristiche di Python includono:** 
- **Sintassi semplice e intuitiva:**   
 facilita lo sviluppo rapido del codice. 
-  Supporto per i paradigmi di programmazione imperativa, funzionale e orientata agli oggetti. 
- **Ampie librerie standard:**   
che offrono moduli e funzioni per operazioni comuni, come la gestione dei file, la rete, l'elaborazione dei dati e molto altro.   
Grazie alla sua versatilità, Python è utilizzato in vari settori, tra cui lo sviluppo web, l'analisi dei dati, l'intelligenza artificiale, la cybersecurity, la scienza computazionale e l'automazione.

---

## Programmare in Python

==Un codice è una serie di istruzioni che i programmatori scrivono. Il processo di scrivere un programma è chiamato anche codifica.==

Ora creeremo il nostro primo codice in Python: Crea un file chiamato helloWorld.py. Usa un editor per scrivere le istruzioni e salvale nel file helloWorld.py.  
`My first Python code`  
`print ("Hello World")`  
`"This program displays the message: Hello World!"`  
### I commenti  
==I commenti aiutano i programmatori a comunicare e comprendere un programma. Non sono istruzioni di programmazione e quindi vengono ignorati dall'interprete.==

In Python, i commenti sono preceduti da:  
- un simbolo cancelletto (#) su una riga (chiamato line comment):  
`#My first Python code`  
- Oppure racchiusi tra tre apici singoli consecutivi (''') su una o più righe (chiamato paragraph comment):   
`'''this program displays the message: Hello World!''`.   


## Data types

### Cosa sono i data types
Quando ci approciamo a un qualsiasi ling di prog ci approcciamo a dei dati primitivi 
Un programma deve rappresentare diversi tipi di valori con cui lavorare. Iniziamo con i più semplici: i tipi primitivi.  
Ce ne sono di diversi tipi:  
- **Intero (int):**  
==Numeri senza decimali. Possono essere positivi o negativi.==  
- **Flottante (float):**  
==Numeri con decimali. Possono essere positivi o negativi.==  
- **Stringa (str):**  
==Dati testuali, ma in realtà possono essere qualsiasi simbolo purché siano racchiusi tra virgolette (“ ” o ‘ ’).==  
- **Booleano (bool):**  
==Valore restituito dalle operazioni logiche. Può essere solo True o False (attenzione alla sensibilità delle maiuscole!).== 

![[Data types.png]]

I numeri possono avere qualsiasi valore come le stringhe, i valori booleani posso avere 2 valori `True` o `false`
### Variabili
Una volta compreso i dati devi sapperli usare, le variabili sono dei modi per slavare questi valori di dati e li puoi richiamare richiamando la variabile a cui hai assegnato quel valore (dato).
A una[[Spiegazione esercizi Lezione 1 Python#Introduzione a Python Variabili| variabile]] posso dargli qualsiasi nome e valore, i nomi devono descrivere al meglio il tipo di dato che state usando (es: name, age). 
Consideriamo prima il semplice problema di calcolare l'area di un cerchio.  
Come scriviamo un programma per risolvere questo problema?  
Scrivere un programma implica progettare algoritmi e poi tradurli in istruzioni di programmazione, ovvero codice.  
Un algoritmo descrive come un problema viene risolto elencando le azioni che devono essere intraprese e l'ordine in cui devono essere eseguite.  
L'algoritmo per calcolare l'area di un cerchio può essere descritto come segue:

1. Ottieni il raggio del cerchio dall'utente.
2. Calcola l'area applicando la seguente formula:  
    area = raggio * raggio * pi
3. Visualizza il risultato.  
In questo problema, il programma deve ottenere il valore del raggio.  
Il valore del raggio può essere memorizzato nella memoria del computer. Per accedervi, il programma deve usare una variabile.  
Una variabile è un nome che fa riferimento a un valore memorizzato nella memoria del computer.  
==**Invece di usare x e y come nomi di variabili, è meglio scegliere nomi descrittivi**==:  
In questo caso, ad esempio, puoi usare il nome "raggio" per la variabile che fa riferimento al valore del raggio del cerchio e "area" per la variabile che fa riferimento al valore dell'area del cerchio.  
Quindi possiamo scrivere nel nostro programma computeArea.py 
```python
#Assign a value to radius
radius=20
#compute area
area= radius * radius * 3.14
#display result
print(area)
```

Vogliamo rappresentare nel nostro programma quanto siamo vecchi:    
Es:
```python
 gianpino = 27
 print (gianpino)
```

Supponiamo che ci sia un altra persona con un'età differente con lo stesso nome, basterà solo assegnare un nuovo valore alla variabile `gianpino`. 
```python
gianpino = 30 
print(gianpino)
```

Possiamo anche modificare il data type alla nostra variabile:  
```python
type (gianpino)
>>> <class `int`>
```

Mentre se vogliamo assegnargli un valore con la virgola:  
```python
gianpino = 27.5
type (gianpino)
>>> <class `float`> 
```

### Overwriting delle variabili

> [!warning] Overwriting: Fate attenzione!
> L'overwriting è semplice, ma proprio per questo è anche semplice commettere errori. 
> ```python
> age =30 
> name = "Bob"
> ...
> name = 31 ←  Qui ad esempio volevamo aggiornare l'età ma abbiamo accidentalmente codificato il nome. In questo caso Python non genera nessun errore! Altri linguaggi, come Java o C++ sono tipizzati: per ogni variabile, devi predefinire il suo tipo di dato.
> ```

In Python, quando una variabile viene dichiarata, il suo tipo viene determinato automaticamente in base al valore che le viene assegnato.  
Una variabile può avere una sequenza di caratteri come valore:  
```python
#stringa  
stringa = "Questa è una stringa"  
print(stringa)  
print(type(stringa))

```

Una variabile può avere un valore booleano:  
```python
#booleano  
bln = True  
print(bln)  
print(type(bln))
```

==In Python, quando una variabile viene dichiarata, il suo tipo viene determinato automaticamente in base al valore che le viene assegnato.==
```python
a = 2.3  
print(a)  
print(type(a))

b = 10  
print(b)  
print(type(b))

c = 'io sono una stringa'  
print(c)  
print(type(c))


c1 = "io sono anche una stringa"  
print(c1)  
print(type(c1))
```


## Convenzioni di denominazione 

Quando nomini le tue variabili, ci sono alcune cose che non puoi fare.  
Ad esempio: gli spazi bianchi.  
**"alices age"** non è una variabile valida! Invece, ad esempio: **alices_age** o **alicesAge**.

In generale:  
-  ==Un nome di variabile deve iniziare con una lettera o il carattere di underscore (_)==.  
-  ==Un nome di variabile non può iniziare con un numero.==  
-  ==Un nome di variabile può contenere solo caratteri alfanumerici e underscore (A-z, 0-9, e _).==  
- ==I nomi delle variabili sono sensibili al maiuscolo/minuscolo (ad esempio, **age**, **Age** e **AGE** sono tre variabili diverse).==  
- ==Un nome di variabile non può essere una delle parole chiave di Python (come **if**, **else**, **import**, **return**, ecc.).==  
---


## Strings 
Una stringa è una sequenza di caratteri, quindi è possibile accedere a ogni carattere della stringa utilizzando un indice che indica la posizione di quel carattere all'interno della stringa data.
```python
Strings
#single line string
strA="Hello World«
#multiple line strings
straB="This is too \
bif to fit \
on a single line so \
you multi-lined it«
'''a string is a sequence of characters, so each character of the string can be accessed
using an index
that indicates the position of that character within the given string.‘‘’
name="John Fitz«
print(name[0]) #display character at position 0 of string.
len(name) #return string lenght
print(len(name))
print(name.lower()) # Lowercase
print(name.upper()) # Uppercase
print(name.title()) # Title case
```

---


