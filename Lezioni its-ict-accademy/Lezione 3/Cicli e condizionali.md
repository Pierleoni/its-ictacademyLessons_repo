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
Sintassi:
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
il for legge `lista_2` e prende il primo elemento della lista e lo mette dentro  la variabile `lettera`, di conseguenza quando prendiamo la prima iterazione (cioè l'iterazione 0) stiamo stampando `a`.
Dopodiché, non avendo più istruzioni da eseguire e passa a `b`, ora l'iterazione 1 contiene `b` quindi quando faccio il `print` stampa `b`. 
Dopo aver fatto ciò, non ho più istruzioni da eseguire e passo a `c`, ora `lettera` contiene `c`, quindi l'iterazione 2 contiene `c`. 
Quando raggiunge la fine della lista esce dalla lista e il flusso continua con il altre righe di codice.
### Annidare i for
Possiamo annidare i for:
```python
lista_1 = [1,2,3]
lista_2 =["a","b","c" ]
for lettera in lista_2
	for numero in lista_1
		print(lettera,numero)
#il primo print sara a,1.
#torno al for perché ho ancora elemtni da numerare dentro la lista.
#Lettera è ancora a ma il numero lo devo fare diventare 2 perché deve\ #eseguire la seconda iterazione,
#il secondo print sarà a,3
#stessa cosa per a,3
#Non avendo da eseguire altri elementi il secondo for si torna al for #pricipale che esgue b e si torna al secondo for che ricomincia la lista,
#quindi il print sarà b,1 
#Di ocnseguenza sara 
#b,2
#b,3
#Avendo altri elementi stampa 
#c,1
#c,2
#c,3
#Una volta finite le liste continua a lavorare altro codice 
#Ho printato 9 volte, cioè 3^2 

```
immagniamo che sia una matrice 

| a1  | a2  | a3  | 0   |
| --- | --- | --- | --- |
| b1  | b2  | b3  | 1   |
| c1  | c2  | c3  | 2   |

Mettiamo caso ho una lista di liste e voglio estrare gli elementi singoli all'intenro, ad esempio voglio estrare b2.
Io posso accedere ai valori di una lista di liste tramite indici, per fare ciò:
```python
l[0][1]
```
posso usare anche i for
```python
for i in range: (len(lista_2))
#for i che varia nel range che da 0 fino alla lunghezza della lista 2
	for j in range:(len(lista_1))
	#in questo modo qualsiais la lunghezza della lista lui mi metta 
	il primo eleemento fino alla lunghezza della lista
	print (L[i][j])
	alla prima iterazione i=0 e j=0 quindi a1 e cosi via 
```
si consiglia di usare lettere singole quando si a che fare con indici (la convenzione prevede i e j)
i in range va da 0 a 3 stessa cosa per `j in range`.
Ora mettiamo caso io abbia diciharato la lista L:
```python
L=[[(a1), (a,2), (a,3)], 
[(b,1), (b,2), (b,3)];
[(c,1),(c,2), (c,3)]] 
Questa lista di liste che contiene tuple fa riferimento alla matrice a tabella sopra 
```
Se io ho una lista del genere e voglio accedere a tutti gli elementi, posso usare gli indici come visto sopra, io uso allora i for perché io voglio crearimi le coordinate (i e j) per prendermi tutti gli elementi, cioe sto facendo una enumerazione: cioè generare, in questo caso, tutte le combinazioni della matrice. 
Per prendere tutti gli eleemnti al suo intenro uso il for:
```python
for i in range (3):
	for j in range(3):
```
io ho messo 3,3 perche so che questa lista contiene 3 sottoliste con 3 elementi.
la funzione `range`: ritorna un range di una lista di intenri che va da 0 a 2 che sono esattemente gli indici.
Io poi mi volgio stampare 
```python
for i in range (3):
	for j in range(3):
print(L[i][j])
#prima iterazione i=0 j=0 quindi a,1
#seconda iterazione i=0 j=1 quindi a,2 
#terza iterazione del ciclo interno i=0 j=2 quindi a,3
#Torno al for principale
# i=1
#torno al secondo for
#j=0 quindi si risetta e si ri-esegue da capo
#prima iterazione i=1 j=0 b,1
#seconda iterazionwe i=1 j=1 b,2
#terza iterazione i=1 j=2 b,3
#torno al for principale
#i=2 
#torno al for secondario che si risetta
#Prima iterazione i=2 j=0 c,1 
#seconda iterazione i=2 j=1 c,2
#terza iterazione i=2 j=2 c,3
```
Se io volessi stmapare tutti gli elementi che ho nella tupla in pari:
```python
for i in range (3)
	for j in range(3)
		if(L[i][j][1]%2)==0
```
Questo stmapa elementi della tupla che sono pari:
Sappaimo che abbiamo tuple e che possono essere indicizzate
l'1 rappresenta il numero accanto alla lettera perché prende la prima colonna e del contentuto della prima riga e colonna mi prende il numero 1, se dovessi prendere la lettera dovre mettere 0 nella parentesi quadra dove è posto l'1.
Prende quell numero e calcola il modulo 2, e 1%2=1 perché è dispari e quindi da 1 e 1 non è uguale 0 quindi vado oltre.
Selezione la tupla a2 e la stampa perché 2/2 da 0.
Passando alla prossima colona c'è a3 ma non me lo stampa perché 3/2 = 1.
Quindi insitesi l'operazione modulo è vera solo quando stmapa a,2 b,2 c,2
Voglio stmapare solo i numeri pari di una lista:
```python
lista_1 = [1,2,3]
for num in range (len(lista_1)):
	if lista_1[num]/2==0 
		print (lista_1[num])
```
Posso anche usare un altra soluzione: 
```
for num lista_1:
	if num /2==0
	print(num)
```
Questo metodo è più veloce,

> [!attention]
> Se usiamo la funzione range mi restituisce solo gli indici

### La funzione `range`
E come se restiuisse una lista, quindi se io scrivo 
```python
range[3] #restituisce una lista che va da 0 a 2
```
Io in questo caso ho pero ho
```python
range[10] #il range va da 0 a 10
range[5,10]#quindi va dal quinto indice al nono
range[1(start),10(end), 2(steps)] #che fa? Stampa tutti i dispari e salta un solo numero 
#possiamo far variare i numeri come ci pare 
```


> [!NOTE] Title
> Contents
List comprenesion: se abbiamo una lista e la vogliamo riepire con un inseme di intenri orndinati
>```python
lista_1=[i for i in range(10)]
>```
>utile per riempire una lista in maniera rapida, lo posso utilizzare pure per i dizionari
>```python
dict_1={i: i for i in range(10)}
print(lista_1)
>```
>Anche qui il range funziona in questo caso
>```python
>lista_1={i: i for i in range (0,10,2)}
>```

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

