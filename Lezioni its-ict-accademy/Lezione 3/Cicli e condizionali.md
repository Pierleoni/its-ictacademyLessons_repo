# Control Statements 
## if Statements
Per scrivere i cicli e le condizioni in python.
Python ci mette a disposizione delle strutture per tradurre i diagrammi a blocchi.
La sintassi è 
```python
if condizione: #premere tab 
	print (10)
```
==detto ciò si consiglia di usare le parentesi tonde per indicare la condizione.== 

```python
(a <3 or b>10 and (c!=20))
```
Python ci mette a disposizione alte 2 cose oltre l'`if`:
1. `elif`:
   sta per **else if** ed esprime un altra condizione dopo la condizione uno (cioè l'`if`); quindi,  se la condizione 1 è vera fai altro se non è vera fai quello che ti dice `elif`. 
   Posso usare quanti `elif` voglio.
```python
if condizione: #premere tab 
	print (10)
elif condizione 2 : 
	print()
elif condizione 3:
elif condizione 4:
...
else
```
Se io scrivo:
```python 
	if a>o: print(10)
		else:
```
questa condizione dice che se è vera per qualsiasi cosa stampa 10 ma se mettiamo `else` implichiamo che se non è vero fa qualcos'altro.
Diverso  se mettiamo `elif`.
```python
if condizione: #premere tab 
	print (10)
elif -10<a<0: 
	print("a is true")
```
- La prima condizione (`if condizione`) viene verificata. 
	Se è vera, viene eseguito il blocco sotto di essa: il `print(10)`. 
	Se la condizione dell' `if` è falsa salta il `print` sotto l'`if`, e il flusso passa al successivo blocco `elif` (se presente). 
La seconda condizione viene verificata solo quando la condizione dell'`if` è falso:
1. Se la condizione dell'`elif` è vera allora viene eseguito il blocco sotto l'`elif`; cioè `print("a is true")` 
2. Se la condizione dell'`elif` non è vera  il flusso va avanti, e passa al blocco  `else`(se presente)
In questo caso non è presente nessun `else` perciò non verrà stampato nulla in output se entrambe le condizioni sono false

> [!example] Comportamento con `else` 
> Se a questo blocco di codice si aggiungesse l'`else`, il programma eseguirà l'azione definita sotto l'`else` solo quando tutte le condizioni precedenti (`if` e `elif`) sono false. 
> Es:
> ```python
> if condizione:
>	   print(10)
>elif -10 < a < 0:
>    print("Il valore di a è tra -10 e 0")
>else:
>    print("Nessuna condizione soddisfatta")
> ```
> Quindi se entrambi i blocchi `if` e `elif` sono falsi, il programma eseguirà il blocco sotto l'`else` cioè `print("Nessuna condizione soddisfatta")`.
> In conclusione possiamo dire che:
> 1. senza `else` il programma non esegue nulla se nessuna delle condizioni è vera
> 2. **Con `else`**, il programma esegue il blocco sotto l'`else` quando nessuna delle condizioni `if` o `elif` è vera.


> [!attention]- `elif` non va in solitaria 
> `elif` da solo non ha senso.
>
>> [!error]  
> > ```
> > elif -10 < a < 0: print("Il valore di a è tra -10 e 0")
>> ``` 



### Annidare gli `If` 

È possibile inserire un `if` dentro un altro `if`. Questa pratica viene chiamata annidamento(o nested if):
==viene utilizzata per creare logiche condizionali più complesse, dove una condizione dipende dal risultato di un'altra.==
In parole povere, puoi mettere un `if` dentro un altro `if` per eseguire un controllo più dettagliato solo se la condizione esterna è vera.
```python
if cond1:
	if cond1:
	else: #riferito al if interno non esterno
else: #riferito all'if esterno
```



> [!faq]- "Il modo per fare debugging in questo caso è usare il debugger" Debugging?
> si riferisce all'uso di strumenti di debug per analizzare l'esecuzione del codice e individuare eventuali errori o problemi. In particolare, l'uso di un **debugger** aiuta a monitorare l'andamento del programma durante la sua esecuzione, in modo da capire perché una determinata condizione è vera o falsa e come il flusso del programma si sviluppa attraverso i vari blocchi `if`, `elif`, `else` annidati.
>  **Cosa significa "debugging"?** 
>==Il **debugging** è il processo di identificazione, diagnostica e correzione degli errori nel codice.== 
>Un **debugger** è uno strumento che permette di:
>- Esaminare il flusso di esecuzione di un programma riga per riga.
>- Monitorare i valori delle variabili in tempo reale.
>- Capire quale parte del codice sta causando un errore o un comportamento imprevisto.
>
>**Relazione con il codice poco sopra**
>```
>if cond1:
 >   if cond1:
  >      # codice
  >  else:
  >      # codice riferito al secondo if interno
>else:
>    # codice riferito al primo if esterno
>
>```
>Immagina che `cond1` sia una variabile booleana che può essere vera o falsa. Potresti non essere sicuro di come il flusso del programma stia seguendo questa logica a causa di un errore nelle condizioni. Il debugger ti permette di:
>
>1. **Eseguire il programma passo per passo**: Puoi eseguire il codice riga per riga per vedere se le condizioni `if` sono valutate correttamente.
>2. **Monitorare il valore delle variabili**: Durante l'esecuzione del programma, puoi osservare come il valore di `cond1` cambia e come viene trattato nelle varie condizioni annidate.
>3. **Verificare il flusso di esecuzione**: Puoi verificare se il flusso entra nel primo `if`, nel secondo `if`, o nell'`else`, e se le azioni vengono eseguite come previsto.
>
>> [!example] Per Ricapitolare
> >   - **Analizzare il flusso di esecuzione** per capire quale parte del codice venga eseguita.
>>- **Controllare i valori delle variabili** (`cond1` in questo caso) per vedere se la condizione che ti aspetti venga soddisfatta.
>>- **Verificare l'annidamento**: assicurarti che l'`else` associato al secondo `if` venga eseguito solo se la condizione del secondo `if` è falsa e quella del primo `if` è vera.

#### Struttura di un if annidato 
==Per `if` annidato, come abbiamo già detto poco fa, è quando metti un blocco `if` all'interno del corpo di un altro `if`.== 
Ogni livello di indentazione in Python indica un livello di annidamento.
Per fare un esempio:
```python
if cond1:
    if cond2:
        # codice eseguito se entrambe cond1 e cond2 sono vere
    else:
        # codice eseguito se cond1 è vera e cond2 è falsa
else:
    # codice eseguito se cond1 è falsa
```

### L'importanza dell'indentazione
==L'indentazione è fondamentale in Python perché indica il livello di annidamento del codice.== 
Se non viene rispettata l'indentazione corretta, Python restituirà un errore di sintassi. Ad esempio:
```python
if cond1:
if cond2:  # Questo non è corretto
    print("Entrambe le condizioni sono vere.")
```
In questo caso, Python si aspetta che il secondo `if` sia indentato sotto il primo `if`, per indicare che è un blocco annidato. Se non indenti correttamente, otterrai un errore.


> [!example] Per Ricapitolare
> - Un **`if` annidato** è semplicemente un `if` dentro un altro `if`. Serve a creare condizioni più complesse, dove una dipende dal risultato dell'altra.
>- L'indentazione è fondamentale per mantenere il flusso logico del programma.
>- Ogni `else` si riferisce all'`if` immediatamente precedente al quale è associato.


2. `else`: 
   ==va a catturare tutto quello che sfugge alla prima condizione e va a chiudere lo  statements; è lo statement di chiusura.== 
Es:
```python
x=10
if x>5:
	print("x is greater than 5")
elif x == 5:
	print ("x is equal to 5")
else:
	print ("x is less than 5")
```


---


## Loops
Fare i cicli in python.
I `for` in python è utile quando abbiamo a che fare con le collections, in particolare quando dobbiamo scorrere liste o dizionari.
### Sintassi
```python
for + variabile in sequence(lista, dizionario, tupla):

```

Scorrere una lista:
```python
lista_1 =[i for in range(10)]
for numero in lista_1 #numero è la variabile in cui va a finire l'ennesimo valore all'interno della lista
print(numero)
```
In questo caso gli ho detto di stampare i numeri da 1 a 10, il `for` in python lo fa da solo, python prende il primo elemento al primo indice, il secondo al secondo e cosi via.
Cosi facendo ho la semplicità di non dover scorrere gli indici:
```python
lista_2 =["a","b","c" ]
for lettera in lista_2
	print(lettera)
```
Il for legge `lista_2` e prende il primo elemento della lista e lo mette dentro  la variabile `lettera`, di conseguenza quando prendiamo la prima iterazione (cioè l'iterazione 0) stiamo stampando `a`.
Dopodiché, non avendo più istruzioni da eseguire e passa a `b`, ora l'iterazione 1 contiene `b` quindi quando faccio il `print` stampa `b`. 
Dopo aver fatto ciò, non ho più istruzioni da eseguire e passo a `c`, ora `lettera` contiene `c`, quindi l'iterazione 2 contiene `c`. 
Quando raggiunge la fine della lista esce dalla lista e il flusso continua con il altre righe di codice.
### Annidare i for
Possiamo annidare i for:
```python
lista_1 = [1,2,3]
lista_2 =["a","b","c" ]
for lettera in lista_2:
	for numero in lista_1:
		print(lettera,numero)


```
Per comprendere esattamente cosa fa un `for` e come processa le iterazioni, analizziamo passo dopo passo:
1. **Inizio del ciclo:**
- Il ciclo esterno inizia con la variabile `lettera` che assume il valore del primo elemento di `lista_2`, ovvero `"a"`.
- Il ciclo interno prende il primo elemento di `lista_1`, che è `1`, e stampa: `a,1`.
2. **Iterazioni successive del ciclo interno**:
 - La variabile `lettera` rimane `"a"`, mentre il ciclo interno procede con il successivo elemento di `lista_1`, ovvero `2`. Stampa: `a,2`.    
 - Il ciclo esterno ritorna alla variabile `lettera` che rimane `"a"`, e il ciclo interno prosegue con il successivo elemento di `lista_1`, ovvero `3`. Stampa: `a,3`.
torno al for perché ho ancora elementi da numerare dentro la lista.
3. **Fine del ciclo interno**:
- Dopo aver iterato su tutti gli elementi di `lista_1`, il ciclo interno termina.
  
Non avendo da eseguire altri elementi il secondo `for` (`for numero in lista_1:`) torna al `for` principale (`for lettera in lista_2:`) che esegue `b` e si torna al secondo `for` che ricomincia la lista.

4. **Ritorno al ciclo esterno**:
  - Il ciclo esterno avanza, assegnando a `lettera` il valore successivo di `lista_2`, ovvero `"b"`. Il ciclo interno si resetta e riparte con `1`.
  - Stampa i valori: `b 1`, `b 2`, `b 3`.
  - 
Finito quest'altro ciclo il secondo `for` torna un'altra volta al `for` principale che esegue l'ultima iterazione, cioè `c`, e si torna al secondo `for` che ricomincia la lista. 

5. **Ultima iterazione del ciclo esterno**:
- La variabile `lettera` assume l'ultimo valore di `lista_2`, ovvero `"c"`. Il ciclo interno riparte nuovamente, iterando su tutti gli elementi di `lista_1`.        
- Stampa i valori: `c 1`, `c 2`, `c 3`.
Una volta finite le liste continua a lavorare altro codice 
In totale vengono printate 9 righe, cioè 3 elementi in `lista_1` moltiplicati per 3 elementi in `lista_2` (3^2=9). 
L'output è:
```python
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
```


> [!NOTE] Nota
> Ogni iterazione del ciclo interno si completa completamente prima che il ciclo esterno avanzi al successivo elemento. 
> Questo comportamento è fondamentale per comprendere l'esecuzione dei cicli annidati in Python.


Immaginiamo che tutto questo sia una matrice:

|     Iterazione     | indici | Colonna 1 | Colonna 2 | Colonna 3 |
|:------------------:|:------:|:---------:|:---------:|:---------:|
|  prima iterazione  |   0    |    a1     |    a2     |    a3     |
| seconda iterazione |   1    |    b1     |    b2     |    b3     |
|  terza iterazione  |   2    |    c1     |    c2     |    c3     |

Mettiamo caso ho una lista di liste e voglio estrare gli elementi singoli all'interno, ad esempio `b2`.
Io posso accedere ai valori di una lista di liste tramite indici, per fare ciò:
Dichiarare la lista `L`:
```python
L=[[(a1), (a,2), (a,3)], 
[(b,1), (b,2), (b,3)];
[(c,1),(c,2), (c,3)]] 
#Questa lista di liste che contiene tuple fa riferimento alla tabella di matrice che si trova poco sopra 
```

```python
l[1][1] #Accede all'elemento b2
```
possiamo anche usare anche i cicli `for` per accedere agli elementi:
```python
for i in range: (len(lista_2))
#for i che varia nel range che va d 0 fino alla lunghezza della lista 2
	for j in range:(len(lista_1))
	#j varia nel range da 0 fino alla lunghezza della lista_1
	print (L[i][j])
	
```
Alla prima iterazione:
- `i = 0`, `j = 0` → stampa `a1`
    
- `i = 0`, `j = 1` → stampa `a2`
    
- `i = 0`, `j = 2` → stampa `a3`

Dopo aver terminato il ciclo interno:
- Torniamo al ciclo esterno: `i = 1`
- Il ciclo interno si resetta:
    - `j = 0` → stampa `b1`
        
    - `j = 1` → stampa `b2`
        
    - `j = 2` → stampa `b3`
        

Infine:
- Torniamo al ciclo esterno: `i = 2`
- Il ciclo interno si resetta di nuovo:
    - `j = 0` → stampa `c1`
        
    - `j = 1` → stampa `c2`
        
    - `j = 2` → stampa `c3`

> [!NOTE] Nota
> Si consiglia di usare lettere singole quando si a che fare con indici (la convenzione prevede i e j)

### Collegamento con l'esempio iniziale
 `i in range` va da 0 a 3 stessa cosa per `j in range`.
 Se io ho una lista del genere e voglio accedere a tutti gli elementi, posso usare gli indici come visto sopra, io uso allora i `for` perché io voglio crearmi le coordinate (`i` e `j`) per prendermi tutti gli elementi, cioè sto facendo una enumerazione: 
 ==cioè generare, in questo caso, tutte le combinazioni della matrice==. 
 ``` python
L = [[("a", 1), ("a", 2), ("a", 3)],
     [("b", 1), ("b", 2), ("b", 3)],
     [("c", 1), ("c", 2), ("c", 3)]]
 
```
 Per prendere tutti gli elementi al suo interno uso il `for`:
 ```python
 for i in range (3):
>	for j in range(3):
 ```
Abbiamo messo come argomento dei due `in range()` `3,3` perché so che questa lista contiene 3 sotto-liste con 3 elementi.
 la funzione `range`: 
 ==ritorna un range di una lista di interi che va da 0 a 2 che sono esattamente gli indici==.
 Adesso stampiamo quanto fatto finora 
 ```python
 `for i in range (3)`:
 	for j in range(3):
 print(L[i][j])
 
 ```
 prima iterazione `i=0` `j=0` quindi `a,1`
 seconda iterazione `i=0` `j=1` quindi `a,2` 
 terza iterazione del ciclo interno `i=0` `j=2` quindi `a,3`
 Torno al `for` principale(`for j in range(3)`)
  `i=1`
 torno al secondo `for`(`for j in range(3)`)
 `j=0` quindi si resetta e si ri-esegue da capo
 prima iterazione `i=1` `j=0`: `b,1`
 seconda iterazione `i=1` `j=1`: `b,2`
 terza iterazione `i=1` `j=2`: `b,3`
 torno al `for` principale
 `i=2` 
 torno al for secondario che si resetta
 Prima iterazione `i=2` `j=0`: `c,1` 
 seconda iterazione `i=2` `j=1`: `c,2`
 terza iterazione `i=2` `j=2`: `c,3`
 Quindi l'output  stampato sarà:
 ```python
("a", 1)
("a", 2)
("a", 3)
("b", 1)
("b", 2)
("b", 3)
("c", 1)
("c", 2)
("c", 3)
```
Il ciclo `for` crea le coordinate (`i`, `j`) necessarie per accedere a tutti gli elementi, generando tutte le combinazioni possibili degli indici. 
Questo approccio è utile per scansionare matrici o strutture annidate in Python.

### Filtrare elementi specifici con cicli annidati
Supponiamo di voler stampare solo gli elementi delle tuple che contengono numeri pari:
```python
for i in range (3)
	for j in range(3)
		if(L[i][j][1]%2)==0: #controlla se il numero è pari
		print(L[i][j])
 
```
#### Spiegazione

1. **Condizione** `L[i][j][1] % 2 == 0`:
    
    - `L[i][j]` accede alla tupla nella posizione `i, j` della matrice.
        
    - `[1]` accede al secondo elemento della tupla (il numero accanto alla lettera).
        
    - Il modulo `% 2` verifica se il numero è divisibile per 2 (pari).
        
2. **Esempio di iterazione**:
    
    - Alla prima iterazione, `i = 0`, `j = 0`, la tupla è `("a", 1)`. Il numero `1` non è pari, quindi non viene stampato.
        
    - Alla seconda iterazione, `i = 0`, `j = 1`, la tupla è `("a", 2)`. Il numero `2` è pari, quindi viene stampato.
        
    - Questo processo si ripete, stampando solo le tuple con numeri pari: `("a", 2)`, `("b", 2)`, `("c", 2)`.

L'output quindi sarà: 
```python
("a", 2)
("b", 2)
("c", 2)
```

### ### Filtrare numeri pari in una singola lista
Per stampare solo i numeri pari in una lista:
**Soluzione con indice**
```python
lista_1 = [1,2,3]
for num in range (len(lista_1)):
	if lista_1[num]/2==0 
		print (lista_1[num])
```
**Soluzione più semplice**
```python
for num lista_1:
	if num /2==0
	print(num)
```
La seconda soluzione è più concisa e preferibile quando non è necessario accedere agli indici direttamente. 
In entrambi i casi, l'output sarà:
```python
2
```

> [!attention] Attenzione!
> ==Se usiamo la funzione range mi restituisce solo gli indici==

### La funzione `range`
E come se restituisce una sequenza di numeri interi
```python
range[3] #restituisce una lista che va da 0 a 2, cioè va dall indice 0 all'indice 2
```
Possiamo specificare i parametri di inizio (`start`), fine (`end`) e passo (`step`)
```python
range[10] #
range[5,10]#quindi va dal quinto indice al nono
range[1(start),10(end), 2(steps)] #che fa? Stampa tutti i dispari e saltando un solo numero 
#possiamo far variare i numeri come ci pare 
```
Nel primo caso(`range[10]`): stampa tutti gli indici della lista
Nel secondo caso(`range[5,10]`): va dal quinto indice al nono indice
Nel terzo caso(`range[1(start),10(end), 2(steps)]`):  Genera 1, 3, 5, 7, 9

###  List comprehension
 La **list comprehension** è una sintassi compatta e più efficiente di Python per creare liste: 
 ==invece di usare un ciclo `for` tradizionale per aggiungere elementi a una lista, la list comprehension ti permette di fare tutto in una sola riga di codice, rendendo il processo più conciso e leggibile.== 
#### Sintassi 
La sintassi di base della list comprehension è:
```python
[espressione for elemento in iterabile]

```
- **`espressione`**: 
  ==è l'operazione o il valore che vuoi inserire nella lista.==
- **`elemento`**: 
  ==è ogni singolo elemento dell'iterabile (come una lista o un range) su cui stai iterando.==
- **`iterabile`**: 
  ==è l'oggetto su cui iteri (ad esempio, un `range`, una lista, un dizionario, ecc.).==

###### **Creazione di una lista con valori interi ordinati**
Abbiamo bisogno di creare una lista con un insieme di interi ordinati:
```python
lista_1=[i for i in range(10)]
print(lista_1) 
```

L'output sarà:
```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

###### **Creazione rapida di dizionari** 
Si posso applicare pure per creare i dizionari:
```python
dict_1={i: i for i in range(10)}
print(dict_1)
```

L'output sarà:
```python
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
```

###### Esempio con passo specifico nel range
Anche qui, come per il range, possiamo specificare un passo:
```python
lista_1={i: i for i in range (0,10,2)}
print(lista_2)
```

L'output sarà:
```python
[0, 2, 4, 6, 8]
```



> [!example ]+ **Per Ricapitolare le caratteristiche della List Comprehension**
> 1. **Funziona sia su liste ordinate che disordinate.**
>2. È utile per semplificare la creazione di liste o dizionari.
>
> Esempio: creazione di una lista con un ciclo tradizionale
>
>Vediamo ora come creare una lista con un ciclo for tradizionale:
>```
>length = 5  
>numbers = []  
>for i in range(1, length + 1):  # Range parte da 1 e include length (grazie a `+1`)
 >   numbers.append(i)
>print(numbers)  # Output: [1, 2, 3, 4, 5]
>
>```
>Spiegazione passo per passo:
>- **Inizializzazione:** La lista `numbers` è vuota all’inizio.
>- **Iterazione:**
  >  - Al primo ciclo, `i = 1`. Viene aggiunto `1` alla lista, che diventa `[1]`.
 >   - Al secondo ciclo, `i = 2`. Ora la lista diventa `[1, 2]`.
  >  - Questo processo si ripete fino a che `i` raggiunge `length + 1`.
>- **Risultato finale:** La lista `numbers` contiene tutti i numeri da `1` a `5`.




List compresion: 
funziona sia su liste disordinate o ordinate 
Mettiamo caso
```python
lenght =5 
numbers[]
for i in range(1, lenght +1) #se metto solo lenght mi da i numeri da uno fino a 4 cosi gli devo dire di aumentarli di 1 
numbers.append(i)
#il primo valore che assume i è i=1 la i è una lista vuota e con l'append io sto aggiungendo una lista vuota che adesso i è diventanto 1.
#tornando al for adesso i=2 e così numbers diventa numbers[1,2].
#torno al for la i=3
#numbers[1,2,3]
#e cosi via fino al che si è inserito sul terminale.
#Cosi posso crearmi 
```

