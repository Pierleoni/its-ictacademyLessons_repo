====# Tipi di Errore
Quando si scrive un programma, è difficile che venga eseguito correttamente al primo tentativo.  
Un errore può essere definito come una **deviazione dal comportamento previsto di un programma**.  
Gli errori possono verificarsi in diverse fasi del ciclo di vita del programma, dalla scrittura del codice fino all'esecuzione.

Gli errori in programmazione si suddividono in **3 principali categorie**:

1. **Syntax error (il più semplice):** 
   Questi errori sono tra i più comuni e facili da individuare, poiché riguardano la **sintassi del linguaggio di programmazione**.
   Quindi fanno riferimento al sintassi del linguaggio di programmazione, se la sintassi non viene rispettata l'interprete fa un check prima di runnarlo, se la sintassi è sbagliata viene restituito un errore di sintassi. 
Alcuni esempi di errore di sintassi: indentazione sbagliata, parentesi mancanti, parole chiave scritte male etc.
Nella maggior parte dei casi gli errori di sintassi, Vs Code rileva subito gli errori di sintassi perché  dispone di strumenti integrati per individuare e segnalare gli errori di sintassi **ancor prima che il codice venga eseguito**.

 **Ecco come fa VS Code a individuare questi errori:**

1. **Linting e Intellisense**:
    - Grazie a estensioni come **Pylance** e **Python Linter**, VS Code analizza il codice in tempo reale e sottolinea eventuali errori sintattici con una linea rossa ondulata.
2. **Diagnostica automatica**:
    - VS Code suggerisce possibili correzioni quando si passa il mouse sopra l'errore.
3. **Terminale interattivo**:
    - Se un errore viene rilevato durante l'esecuzione, l'output nel terminale fornisce **messaggi chiari e dettagliati**, indicando la riga esatta in cui si trova il problema.

Gli errori di sintassi sono tra i più semplici da individuare grazie ai controlli automatici dell'interprete Python e agli strumenti offerti dagli editor di codice come **VS Code**.  
Utilizzando il **linting** e l'**Intellisense**, è possibile correggere molte di queste problematiche **ancor prima di eseguire il codice**, migliorando così la produttività e riducendo il rischio di bug.

2. **Runtime Errors:** 
questa tipologia è particolare perché fanno crashare il programma in maniera inaspettata. 
Si verificano durante l'esecuzione del codice.
Vengono  causati da input non validi o da altri problemi che non possono essere
rilevati dall'interprete Python.
Ad esempio se abbiamo un vettore e proviamo aa accedere ad un elemento che non esiste restituisce un errore di runtime. In un programma lungo  se l'errore si trova in mezzo al programma l'esecuzione non arriverà mai alla fine del codice.
Esempi comuni di errori di runtime:
divisione per zero, l'accesso a un indice che non esiste in
un elenco e il tentativo di aprire un file inesistente.
[Per approfondire i runtime errors su python](https://docs.python.org/3/library/exceptions.html)
Si possono implementare gli errori di runtime quando si scrive una nuova libreria. 
Il `try except` per gestire le eccezioni, evita il crash.

3. **Logical Errors:** 
   sono i più complicati perché il programma funziona ma il risultato non è coretto.
   Sono causati da un errore nella logica del codice. 
   Esempi comuni di errori logici sono: 
   l'uso della formula sbagliata in un calcolo, l'uso della variabile sbagliata in un ciclo e l'uso della condizione sbagliata in un'istruzione if
Bisogna capire dove sta e perché accade, perché python non controlla la correttezza dell'output.

## Dividi e conquista
Quando si programma, un modo efficiente di risolvere i problemi è scomporre il problema in problemi più piccoli:
prendiamo l'esercizio 9 quello sulla serie del pi greco.
![[Ex9_pi_greco.py]] 



 dato un probelma suddividere il problema in tanti sotto-problemi più piccoli, e inizio a risolvere un sotto problema alla volta e una volta risolti li ricombino per risolvere il problema principale.

Nel caso di questo esercizio lo scriviamo usando le funzioni:
Per fare ciò dobbiamo definire una chiamata 
```python
def computePI(approximation_value, decimal_digits):
	
```

Questa strategia del divide et impera, ci fa dividere il probmela in sotto problemi più piccoli, per fare ciò suddividiamo in 3 passaggi:
1. Generalizza la formula, quindi trovare una formula che conesnte di generalizzare la serie infinta di pi greco
2. Scrive la funzione computePI()
3. Usare la funzione 

### Step 1: trovare la formula generale della serie
Se guardiamo questa serie, ogni temrine di questa serie è una frazione e il denominatore cambia seguendo un criterio:

1.1) Determinare come il denomitarore cambia per ogni iterazione 
1.2) Determinare come il segno si alterna per ogni terminwe della serie in ogni iterazione
#### Sub-Step 1.1 
Detrminare come il denomi atore cambia.
- il primo termine della serie è `4`
- The first term of the series is 4.
• The second term of the series is 4/3.
• The third term of the series is 4/5.
• The fourth term of the series is 4/7.
• The fifth term of the series is 4/9.
• The sixth term of the series is 4/11, and so on.

Devo quindi scrivere un loop che mi stampa i primi 6 termini della serie sullo schermo:
inizializzo un contatore `i=0` e definire pi=0 
Ora devo trovare come il contatore i è legato al denominatore; dato il denominatore:
 i = 0
pi = 4 = 4/1 = 4 / (0 + 1)
• i = 1
pi = 4/3 = 4 / (1 + 1 + 1)
• i = 2
pi = 4/5 = 4 / (2 + 2 + 1)
• i = 3
pi = 4/7 = 4 / (3 + 3 + 1)
Thus, we found that 4/7 can be written as
4 / (3 + 3 + 1) = 4 / (2 * 3 + 1),
and since i = 3,
we get 4 / (2 * i + 1)

Pertanto ho trovato una regola generale in modo che il denominatore cambi in funzione di i.
Faccio il test:
i = 0
pi = 4 = 4/1 = 4 / (2 * 0 + 1)

• i = 1
pi = 4/3 = 4 / (2 * 1 + 1)

• i = 2
pi = 4/5 = 4 / (2 * 2 + 1)

• i = 3
pi = 4/7 = 4 / (2 * 3 + 1)

• i = 4
pi = 4/9 = 4 / (2 * 4 + 1)

• i = 5
pi = 4/11 = 4 / (2 * 5 + 1)

Quindi il programma possiamo riscriverlo così:
```python
# define a counter for while loop
i:int = 0
# define a term for pi for each iteration
pi:float = 0.00
while i <=5 :
# print each term of the series
print(f"4 / {2*i + 1}")
# incrementing i by 1
i +=1
```

#### Sub-step 1.2
Adesso devo capire come alternare il segno, per fare ciò devo usare lo stesso ragionamento:
If i = 0, the term of the series has a positive sign (+4)
• If i = 1, the term of the series has a negative sign (-4/3)
• If i = 2, the term of the series has a positive sign (+4/5)
• If i = 3, the term of the series has a negative sign (-4/7)
• If i = 4, the term of the series has a positive sign (+4/9)
• If i = 5, the term of the series has a negative sign (-4/11)
• If i = 6, the term of the series has a positive sign (+4/13)

Se i assume valore pari il termine della serie assume il valore positivo, contrariamente se i assume un valore dispari il termine della serie assume un segno negativo.
Quindi posso scrivere il codice così:
```python
# define a counter for while loop
i:int = 0
# define a term for pi for each iteration
pi:float = 0.00
while i <=6 :
# if i is even, the term of the pi series is positive
if i%2==0 :
print(f"+ 4 / {2*i + 1}")
# if i is odd, the term of the pi series is negative
else:
print(f"- 4 / {2*i + 1}")
# incrementing i by 1
i += 1
```

Abbiamo trovato una formula che consete di generalizzare la formula del pi greco 
### Step 2 
Scrivo la funzione `computePI(appromaxition_value, decimal_digits)` per computare l'approssimazione del pi greco. 
![[Conquest.png]]

### Step 3 
Usare la funzione per calcolare le 4 differenti approssimazioni di pi greco. 
```python
# calling computePI function to determine how many terms are needed to obtain 3.14 ( 152 terms)
print(f"{computePI(3.14, 2)} terms are needed to compute a value of pi approximated to 3.14!")

# calling computePI function to determine how many terms are needed to obtain 3.141 ( 916 terms)
print(f"{computePI(3.141, 3)} terms are needed to compute a value of pi approximated to 3.141!")

# calling computePI function to determine how many terms are needed to obtain 3.145 ( 7010 terms)
print(f"{computePI(3.1415, 4)} terms are needed to compute a value of pi approximated to 3.1415!")

# calling computePI function to determine how many terms are needed to obtain 3.1459 ( 130'658 terms)
print(f"{computePI(3.14159, 5)} terms are needed to compute a value of pi approximated to 3.14159!"
```

![[Probelm solving ex9.png]]


| Dividi | Conquista | Combina |
| ------ | --------- | ------- |
|        |           |         |




