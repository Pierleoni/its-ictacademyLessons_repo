# Introduzione
Abbiamo visto come funzionano le [[Funzioni in Python|funzioni in Python]] e quali sono i [[Funzioni in Python#Le funzioni|vantaggi]] nell'implementarle nel codice.
Esiste una particolare uso delle funzioni chiamate **funzioni ricorsive**
## Le funzioni ricorsive
==Sono funzioni che chiamano sé stesse durante la loro esecuzione. ==
Questo approccio è particolarmente utile ==per risolvere problemi che possono essere scomposti in sotto-problemi più piccoli dello stesso tipo,== come ad esempio il calcolo del fattoriale, la sequenza di Fibonacci o la costruzione e la navigazione interna di strutture dati gerarchiche (es: alberi). 
### Caratteristiche principali
La logica delle funzioni ricorsive prevede 3 caratteristiche principali:
1. **Caso base:**
   ==Ogni funzione ricorsiva deve avere almeno un caso base che interrompe la ricorsione.==  
   ^casoBase
   
2. **Caso Ricorsivo:**
   ==La parte della funzione che chiama sé stessa con un input più semplice.==
   ^casoRicorsivo
   
3. **Avvicinamento al caso base:**
   ==Ogni chiamata ricorsiva deve avvicinarsi al caso base.==
   ^avvicinamento-casoBase

Prendiamo ad esempio il calcolo del fattoriale:
```run-python
def fattoriale(n:int)->int:
	#caso base
	if n == 0 or n<1:
		 raise ValueError("Il numero deve essere maggiore di zero")
	elif n == 1:
		return 1
	#caso ricorsivo
	else:
		return n * fattoriale(n-1)

print(fattoriale(5))
```

Analizziamo questo codice:
1. **[[#^casoBase|Caso base]]:**
   - `if n == 0 or n < 1`: 
    Restituisce un messaggio d'errore se `n` non è positivo.
   - `elif n == 1`: 
    Restituisce `1`, terminando la ricorsione.
2. [[#^casoRicorsivo|Caso Ricorsivo]]: 
     - `else: return n * fattoriale(n-1)`
3. [[#^avvicinamento-casoBase|Avvicinamento al caso base]]: 
   - `n-1`: 
     - Ogni chiamata ricorsiva passa `n-1` invece di `n`, riducendo progressivamente il problema.
       Infatti  nel `print()` si va a chiamare la funzione `fattoriale()` e viene passato il valore `5` come argomento, viene calcolato il fattoriale di `5!` (cioè `5*4*3*2*1 = 120` ) e quando viene raggiunto il caso base (`n == 1`) la ricorsione si ferma.



Difatti senza la diminuzione progressiva di `n` non ci si avvicinerebbe al caso base, tuttavia, benché la diminuzione progressiva sia importante, non è sufficiente: 
serve prima di tutto un caso base affinché venga raggiunto e lo stack di chiamate si interrompa.
Per essere più precisi: 
```run-python
def fattoriale(n: int) -> int:
    if n == 0 or n < 1:
        return f"Il numero inserito deve essere maggiore di zero e 1"
    return n * fattoriale(n - 1)  # Caso ricorsivo senza fermarsi mai

print(fattoriale(5))

```
In questo caso la funzione continua a chiamarsi all'infinito (`fattoriale(0)`, poi `fattoriale(-1)`, `fattoriale(-2)`, etc.) fino a che Python non dà errore di ricorsione perché lo stack di chiamate si riempie troppo.
###### Esempio di esecuzione per `fattoriale(5)`:
1. `fattoriale(5)` → `5 * fattoriale(4)`
    
2. `fattoriale(4)` → `4 * fattoriale(3)`
    
3. `fattoriale(3)` → `3 * fattoriale(2)`
    
4. `fattoriale(2)` → `2 * fattoriale(1)`
    
5. `fattoriale(1)` → **caso base**, ritorna `1`
    

Ora, i valori si moltiplicano risalendo la catena:  
`2 * 1 = 2`, `3 * 2 = 6`, `4 * 6 = 24`, `5 * 24 = 120`.



### Esercizio con funzione ricorsiva: Countdown
Scrivi una funzione Python chiamata `countdown` che accetti un numero intero positivo `n` come input e stampi un conto alla rovescia da `n` a zero.  
Se il numero di input è negativo, visualizza un messaggio di errore.  
Per implementare la funzione, devi usare esclusivamente un ciclo `while` e il parametro `n` passato come input alla funzione.  
Non è consentito dichiarare variabili aggiuntive all'interno della funzione.  
Successivamente, chiama la funzione con `n = -5` e `n = 5`.
Expected Output:
Error! Inserted number is negative!

-------------------------------------------------
5
4
3
2
1
0


Normalmente per risolvere questo esercizio si usa un `while` loop:
```run-python
def countdown(n: int) -> None:
    # n is positive (n >= 0)
    if n >= 0:
        # print the countdown, while n >= 0
        while n >= 0:
            print(n)
            n = n - 1
    # n is negative (n < 0)
    else:
        print("Error! Inserted number is negative!")

# calling function countdown for n = -5
countdown(-5)
# calling function countdown for n = 5
countdown(5)

```
#### Passaggi della funzione `countdown(n)`
- **Controllo del valore di `n`**
    
    - Se `n` è **positivo o zero** (`n >= 0`), esegue un **ciclo `while`** che stampa `n` e lo decrementa di 1 fino ad arrivare a `0`.
        
    - Se `n` è **negativo** (`n < 0`), entra nell'**`else`** e stampa un messaggio di errore.
        
- **Uso del ciclo `while`**
    
    - Il ciclo `while n >= 0:` continua a eseguire il corpo del ciclo finché `n` non diventa inferiore a `0`.
        
    - Ad ogni iterazione, `n` viene decrementato di `1` (`n = n - 1`).
        
    - Quando `n` diventa `-1`, la condizione `n >= 0` diventa falsa e il ciclo si interrompe.
**Il flusso di esecuzione quindi sarà:**
1. **Prima chiamata (`countdown(-5)`)**:
    
    - Poiché `-5 < 0`, esegue il blocco `else`
        
    - Stampa: "Error! Inserted number is negative!"
        
2. **Seconda chiamata (`countdown(5)`)**:
    
    - Poiché `5 >= 0`, entra nel blocco `if`
        
    - Esegue il ciclo `while`:
        
        - Stampa: 5
            
        - Decrementa: n = 4
            
        - Stampa: 4
            
        - Decrementa: n = 3
            
        - ... continua finché n >= 0
            
        - Stampa finale: 0
            
        - Esce dal ciclo quando n diventa -1


Se usassimo la funzione ricorsiva al posto del ciclo while:
Expected Output:
 `Error! Inserted number is negative!`
-------------------------------------------------
5
4
3
2
1
0


Qui abbiamo la `def` della funzione:
```python
def countdown(n:int):
	#n è negativo
	if n<0:
		print(error)
```

L'if, in questo caso, impedisce che la funzione richiami se stessa all'infinito quindi prima di fare una chiamata ricorsiva dobbiamo costruire il codice che a monte ci sia una condizione per cui il codice si stoppa; ovvero il [[#^casoBase|caso base]].

```python
	elif n==0:
		print(0)
```

L' `elif` è un'altra condizione di terminazioni delle ricorsioni(o [[#^casoBase|caso base]]):
Quindi la chiamata deve terminare quando n è uguale a 0 o minore di 0, 
Il  [[#^casoRicorsivo|caso ricorsivo]] lo mettiamo nell'else:

```python
	else:
		print(n-1)
```
Anche qui `n-1` è l' [[#^avvicinamento-casoBase|avvicinamento al caso base]].

Quindi il codice completo è:
```run-python
def countdown(n:int) -> None:
	# n is negative
	if n < 0 :
		print("Error! Inserted number is negative!")
	# n = 0 must stop the recursive process
	elif n == 0:
		print(0)
	# other cases
	else:
		print(n)
		countdown(n-1)

countdown(0)
print("-------")
countdown(5)
print("--------------")
countdown(20)
```

#### Passaggi logici del codice

###### Struttura della Funzione

1. **Caso base 1 (n < 0)**:
    
    - Gestione dell'errore per input negativi
        
    - Stampa un messaggio di errore e termina
        
2. **Caso base 2 (n == 0)**:
    
    - Condizione di terminazione della ricorsione
        
    - Stampa 0 e termina la catena ricorsiva
        
3. **Caso ricorsivo (n > 0)**:
    
    - Stampa il valore corrente di n
        
    - Chiama se stessa con `n-1` ([[#^avvicinamento-casoBase|avvicinamento al caso base]]).

###### Flusso di esecuzione
#### Chiamata `countdown(0)`

```python
0
```

- Entra nel caso `elif n == 0`
    
- Stampa 0 e termina (nessuna ricorsione)
    

#### 2. Chiamata `countdown(5)`

```python
5
4
3
2
1
0
```


- Sequenza ricorsiva:
    
    1. Stampa 5 → chiama `countdown(4)`
        
    2. Stampa 4 → chiama `countdown(3)`
        
    3. Stampa 3 → chiama `countdown(2)`
        
    4. Stampa 2 → chiama `countdown(1)`
        
    5. Stampa 1 → chiama `countdown(0)`
        
    6. Stampa 0 → termina (caso base raggiunto)
        

#### 3. Chiamata `countdown(20)`

- Stampa i numeri da 20 a 0 in ordine decrescente
    
- Segue lo stesso pattern di `countdown(5)` ma con più passaggi

##### Differenza Rispetto alla versione iterativa 
1. **Assenza di cicli**: Tutta la logica è gestita dalle chiamate ricorsive
    
2. **Stack di chiamate**: Ogni chiamata viene messa nello stack fino al raggiungimento del [[#^casoBase|caso base]] 
    
3. **Terminazione naturale**: La ricorsione si interrompe automaticamente quando n raggiunge 0


> [!attention] **Punti critici da notare**
> 1. **Gestione degli errori**: L'input negativo non blocca l'esecuzione, solo stampa un messaggio
 >   
>2. **Ordine di stampa**: La stampa avviene prima della chiamata ricorsiva (approccio "head recursion")
  >  
>3. **Profondità ricorsiva**: Per `n = 20` funziona, ma per `n = 1000` potrebbe causare stack overflow(ovvero lo stack delle chiamate si riempie e Python restituisce un errore di ricorsione (`RecursionError`)


> [!hint] **Trick & Tips**
> Il trucco delle funzioni ricorsive è mettere il [[#^casoRicorsivo|caso ricorsivo]] nel blocco`else`, mentre gli altri blocchi (`if` ed `elif`) gestiscono i casi di terminazione.
> Questo perché quando vado a mettere un numero positivo come argomento della chiamata della funzione o un valore che faccia risultare i primi due blocchi falsi, il flusso del codice passa all'`else` e fa correre l'istruzione che vi è contenuta al suo interno.
> Essendo che l'`else` è la parte finale della catena di `if`-`elif`-`else` non si ha il rischio di avere output indesiderati.
> Se si togliesse il blocco `else`, il codice continuerebbe a funzionare, ma dopo aver stampato `0`, analizzerebbe il primo [[#^casoBase|caso base]] (`n<0`) e stamperebbe il messaggio di errore.
> Questo succede perché quando `n==0`, il codice entra nell'`elif` e stampa `0` e in teoria la funzione termina senza chiamare sé stessa. 
> Tuttavia se la chiamata non si trova dentro il blocco `else`, Python continuerà a verificare le altre condizioni anche dopo la terminazione della ricorsione.
>```
>def countdown(n: int) -> None:
  >  if n < 0:
  >      print("Error! Inserted number is negative!")
 >   if n == 0:  # Caso base
 >       print(0)
 >   print(n)  # Viene eseguito anche per n == 0
  >  countdown(n - 1)  # La chiamata ricorsiva avviene sempre, anche dopo lo 0
>
>countdown(3)
>```
> >[!example] **Regola generale:**
> >- **Blocchi `if`/`elif` → Definiscono i casi base (terminazione della ricorsione).**  
>>- **Blocco `else` → Contiene la chiamata ricorsiva per continuare il processo.**
>
>Un ultimo consiglio è quello di usare sempre è solo il `return` e mai il `print()` all'interno della catena dei [[Cicli e condizionali#Conditional Statements|conditional statements]]



### Metodo ricorsivo vs. metodo iterativo

Questo problema può essere risolto sia attraverso il metodo iterativo che con le funzioni ricorsive:
![](https://i.imgur.com/WPSMTgk.jpeg)
Come possiamo vedere dall'immagine nel **metodo ricorsivo** a sinistra:
- La funzione `countdown(n)` chiama sé stessa con un valore ridotto (`countdown(n-1)`) finché `n` non diventa `0`.
    
- Ogni chiamata genera un nuovo livello nella pila di esecuzione, che viene poi risolto tornando indietro.
    
- Struttura visiva: 
  una serie di chiamate annidate che vanno da `countdown(5)` fino a `countdown(0)`, poi si risolvono tornando indietro.
Nel metodo iterativo a destra:
- Utilizza un ciclo che **decrementa `n` ad ogni iterazione** fino a raggiungere `0`.
    
- Non vengono create nuove istanze della funzione, quindi consuma meno memoria rispetto alla versione ricorsiva.
    
- Ogni iterazione è numerata (Iter1, Iter2, etc.), mostrando il valore di `n` a ogni passo.
Ovviamente con il metodo ricorsivo scrivere questo codice risulta più veloce da scrivere, più leggibile e più intuitivo. Tuttavia come abbiamo già accennato prima la ricorsione è un buon modo per costruire strutture gerarchiche ad albero ed esplorarle ma se l'albero è troppo profondo si rischia di aumentare il calcolo computazionale e di rallentare la macchina, infatti questo tipo di funzioni vengono usate in alcuni casi specifici quando servono.  


### Esercizio 2: Somma ricorsiva

Scrivi una funzione chiamata sum che prende un numero intero in input e ritorna da 0 a n.
Se l'input n è negativo, visualizza un messaggio di errore e la funzione deve ritornare 0. 
Per implementare la funzione sum, devi esclusivamente usare un while loop e il parametro n passato in input nella funzione.

Expected Output:
```
Error! Inserted number is negative!

0

-----
15
```
1. Caso con il `while` loop:
```run-python
def sum(n:int) -> int:
	# n is negative
	if n < 0:
		print("Error! Inserted number is negative!")
		return 0
	# n is positive
	else:
		# define a sum
		sum:int = 0
		# compute sum until n >= 0
		while n>=0:
			sum = sum + n
			n = n-1
		# return sum as int
		return int(sum)
print(sum(-5))
print("-----------")
print(sum(5))
```

Analizziamo questo codice:
 1. Gestione dell'input negativo
```python
if n < 0:
    print("Error! Inserted number is negative!")
    return 0
```
- **Logica**: Se `n` è negativo:
    
    - Stampa un messaggio di errore
        
    - Restituisce 0 (come specificato nei requisiti)
2.  Calcolo della somma per input positivo:
```python
else:
    sum: int = 0
    while n >= 0:
        sum = sum + n
        n = n - 1
    return int(sum)
```
- **Inizializzazione**:
    
    - `sum = 0` - Variabile accumulatore per la somma
        
- **Ciclo while**:
    
    - Condizione: `n >= 0` (continua finché `n` non diventa negativo)
        
    - Ad ogni iterazione:
        
        - Aggiunge il valore corrente di `n` a `sum`
            
        - Decrementa `n` di 1
            
- **Ritorno del risultato**:
    
    - `return int(sum)` - Restituisce la somma convertita in intero (la conversione è ridondante poiché `sum` è già intero)


> [!example]- **Esempio di esecuzione**
> ### Caso 1: Input negativo (`sum(-5)`)
>
>1. Verifica `n < 0` → True
 >   
>2. Stampa: "Error! Inserted number is negative!"
  >  
>3. Restituisce: 0
  >  
>4. Output:
  >  
  >  
  >  
>```
 >   Error! Inserted number is negative!
 >   0
>```
 >   
>Caso 2: Input positivo (`sum(5)`)
>
>
>
>1. Inizializza `sum = 0`
  >  
>2. Esegue il ciclo:
>    
  >  - Iterazione 1: n=5 → sum=0+5=5, n=4
 >       
  >  - Iterazione 2: n=4 → sum=5+4=9, n=3
 >       
  >  - Iterazione 3: n=3 → sum=9+3=12, n=2
 >       
  >  - Iterazione 4: n=2 → sum=12+2=14, n=1
 >       
  >  - Iterazione 5: n=1 → sum=14+1=15, n=0
 >       
  >  - Iterazione 6: n=0 → sum=15+0=15, n=-1
 >       
>1. Esce dal ciclo quando n=-1
>    
>2. Restituisce: 15
 >   

Il ciclo `while` termina sempre perché `n` viene decrementato ad ogni iterazione

Ora anziché il `while` usiamo la funzione ricorsiva:
```run-python
def recursiveSum(n:int) -> int:
	# n is negative
	if n < 0:
		print("Error! Inserted number is negative!")
		return None
	# if n = 0 recursive process must be stopped
	elif n == 0:
		return 0
```

la rappresentazione grafica è:
![](https://i.imgur.com/0o9iyhc.jpeg)

Osservando questa immagine possiamo vedere come funziona la funzione ricorsiva:
ho il numero intero `5`, ché è maggiore e diverso da zero
devo fare `5` + (`n-1`), cioè:
- `5 + (5-1)`, 4 è maggiore e diverso da zero? Si
- `4+(4-1=3)`, 3 è maggiore e diverso da zero ? Si
- `3+(3-1=2)`, 2 e maggiore e diverso da zero ? Si
- `2+(2-1= 1)`, 1 è maggiore e diverso da zero ? Si
- `1+(1-1= 0)`, 0 è maggiore e diverso da zero ? No, qui la ricorsione si stoppa.
Volendo possiamo anche vedere il flusso della funzione dal basso verso l'alto, cioè partendo da `0`.
![](https://i.imgur.com/BaNOeT0.jpeg)
Il procedimento è lo stesso solo che è inverso
Possiamo adesso scrivere la nostra funzione ricorsiva
```run-python
def recursiveSum(n:int) -> None:
	# n is negative
	if n < 0:
		print("Error! Inserted number is negative!")
		return None
	# if n = 0 recursive process must be stopped
	elif n == 0:
		return 0
	# if n is positive, compute recursive sum
	else:
		return int(n + recursiveSum(n-1))

print(recursiveSum(5))
```

Guarda immagine pag.34.

### Esempio 3: Sum in range
Scrivi una funzione `sumInRange` che calcola la somma di tutti i numeri interi compresi tra `a` e `b`, inclusi, dove `a` e `b` vengono passati come input alla funzione.

Per risolvere l'esercizio, è obbligatorio utilizzare un ciclo `while`, e si assume che il valore di `b` sia sempre maggiore di `a`. Pertanto, se `a > b`, è necessario scambiare i valori per assicurarsi che `a` sia il più piccolo dei due.

Infine, è consentito dichiarare solo una variabile, oltre ai parametri della funzione, per memorizzare la somma.

Infine, chiama la funzione `sumInRange` per `a = 5, b = 10` e per `a = 10, b = 5`.

Expected Output:
```
45

---
45
```
Quindi l'esercizio è:
```run-python
def sumInRange(a:int, b:int) -> int:
	# if a > b, swap values of a and b
	if a > b:
	# define a temporary variable called temp, containing value of a
		temp:int = a
		# swap values of a and b
		a = b
		b = temp # now b = a
	# define a sum
	sum:int = 0
	# compute sum until b = a
	while b>=a:
		sum = sum + b
		b = b -1
	# return sum
	return int(sum)
```
Analizziamo il codice:
1. **Gestione dell'ordine degli estremi**
```python
if a > b:
    temp: int = a
    a = b
    b = temp
```
- **Logica**: Se `a` è maggiore di `b`, scambia i valori delle due variabili
    
- **Meccanismo**:
    - Usa una variabile temporanea `temp` per conservare il valore di `a`
        
    - Assegna a `a` il valore di `b`
        
    - Assegna a `b` il valore originale di `a` (conservato in `temp`).

2. **Calcolo della somma**
```python
sum: int = 0
while b >= a:
    sum = sum + b
    b = b - 1
return int(sum)
```

- **Inizializzazione**:
    
    - `sum = 0` - Variabile accumulatore per la somma
        
- **Ciclo while**:
    
    - Condizione: `b >= a` (continua finché `b` non diventa minore di `a`)
        
    - Ad ogni iterazione:
        
        - Aggiunge il valore corrente di `b` a `sum`
            
        - Decrementa `b` di 1
            
- **Ritorno del risultato**:
    
    - `return int(sum)` - Restituisce la somma (la conversione è ridondante poiché `sum` è già intero)


> [!example] **Esempio di esecuzione**
> Caso 1: Input ordinato (`sumInRange(2, 5)`)
>
>1. Non entra nell'`if` (2 < 5)
 >   
>2. Esegue il ciclo:
  >  
  >  - Iterazione 1: b=5 → sum=0+5=5, b=4
  >      
  >  - Iterazione 2: b=4 → sum=5+4=9, b=3
  >      
  >  - Iterazione 3: b=3 → sum=9+3=12, b=2
  >      
  >  - Iterazione 4: b=2 → sum=12+2=14, b=1
  >      
>3. Esce dal ciclo quando b=1
  >  
>4. Restituisce: 14 (5+4+3+2)
>
>
>
>
>
>Caso 2: Input non ordinato (`sumInRange(5, 2)`)
>
>
>5. Entra nell'`if` (5 > 2) e scambia i valori:
  >  
>  - a diventa 2
 >       
 >  - b diventa 5
 >      
>1. Esegue lo stesso calcolo del Caso 1
  >  
>2. Restituisce: 14 (stesso risultato)

Implementato con la funzione ricorsiva è:

```run-python
def recursiveSumInRange(a:int, b:int) -> int:
	# if a > b, swap values of a and b
	if a > b:
	# define a temporary variable called temp, containing value of a
		temp:int = a
		# swap values of a and b
		a = b
		b = temp # now b = a
```

Nel caso in cui a e b siano uguali ritorno uno dei due valori:

```run-python
def recursive_sum_Range(a:int, b:int) -> int:
	# if a > b, swap values of a and b
	if a > b:
	# define a temporary variable called temp, containing value of a
		temp:int = a
		# swap values of a and b
		a = b
	b = temp # now b = a
	# if b = a, the recursive process must be stopped
	if b == a:
		return int(a)
	# otherwise, compute the sum recursively
	else:
		return int(b + recursive_sum_range(a, b-1))

print(recurisive_sum_range(5,10))
```

Analizziamo il codice:
1. **Gestione dell'ordine degli estremi:**
```python
if a > b:
    temp: int = a
    a = b
    b = temp
```
- **Scambio intelligente**: Garantisce che `a` sia sempre ≤ `b` prima del calcolo
    
- **Effetto**: `range(a, b)` sarà sempre valido
2. **Caso base:**
```python
if b == a:
    return int(a)
```
- **Terminazione**: Quando gli estremi coincidono, restituisce il valore stesso
    
- **Esempio**: `recursiveSumInRange(3, 3)` → 3
3. **Caso Ricorsivo:**
```python
else:
    return int(b + recursiveSumInRange(a, b-1))
```

- **Logica ricorsiva**:
    
    - Somma il valore corrente `b`
        
    - Richiama la funzione con intervallo ridotto `(a, b-1)`
        
- **Esempio**:
    
    - `recursiveSumInRange(2, 4)` → `4 + recursiveSumInRange(2, 3)`
        
    - → `4 + (3 + recursiveSumInRange(2, 2))`
        
    - → `4 + 3 + 2` = 9


> [!example] **Esempio di esecuzione**
> **Input**: `recursiveSumInRange(3, 5)`
>
>1. Non scambia (3 < 5)
  >  
>2. `5 + recursiveSumInRange(3, 4)`
  >  
 >   - `4 + recursiveSumInRange(3, 3)`
 >       
 >       - Caso base: 3
 >           
 >   - `4 + 3 = 7`
 >       
>3.  `5 + 7 = 12`
  >  
>4. **Output**: 12 (3+4+5)
>
>**Input con scambio**: `recursiveSumInRange(5, 3)`
>
>5. Scambia: a=3, b=5
  >  
>6. Segue lo stesso processo dell'esempio precedente

Guardando questa immagine possiamo capire come la funzione ricorsiva torni:
![](https://i.imgur.com/6dmi3K8.jpeg)

Partendo dal basso si ha l'intero `5`:
- `6+5=11`
- `11+7=18`
- `18+8=26`
- `26+9=35`
- `35+10=45`

## Fibonacci
La sequenza di Fibonacci è una sequenza di numeri interi dove ogni numero è la somma dei numeri che lo precedono e alla fine si va a creare quest' albero. 

![](https://i.imgur.com/1Vs9r19.png)

Per ogni funzione devo eseguire questa formula finché non raggiungo 0 o uno.
Per capire meglio Fibonacci, usiamo questa immagine:
![](https://i.imgur.com/zdNVofH.png)
Per implementare ciò in Python:
```run-python
def fibonacci(n:int) -> int:
	# n is negative or 0
	if n <= 0:
		return 0
	# n = 1
	elif n == 1:
		return 1
	# otherwise, compute Fibonacci series applying its formula
	else:
		return int(fibonacci(n-1) + fibonacci(n-2))
```

