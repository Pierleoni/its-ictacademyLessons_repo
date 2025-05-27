# Cos'è uno script 
Uno script è una serie di comandi di shell scritti in un file di testo.
Sono stati introdotti alcuni costrutti di controllo tipici di un vero linguaggio di programmazione per rendere gli script di shell più potenti.
Perché usare gli script di shell?
-  Per creare nuovi comandi personalizzati
-  Per risparmiare tempo (esecuzione di uno scipt, invece di molti comandi in sequenza)
-  Per automatizzare dei task che devono essere eseguiti frequentemente
-  Per facilitare i compiti dell’amministratore di sistema.
Come scrivere uno script?
Si può utilizzare un qualunque editor di testo (per esempio nano).

## Scrivere uno script
Si provi a scrivere lo script `hello_world.sh`
Per fare ciò:
```
$ mkdir scripts 
```

Si crea la directory in cui verranno salvati i nostri script

```
$ cd ./scripts
```

Per spostarci nella directory *scripts* appena creata

```
$ nano hello_world.sh
```

Viene aperto l'editor di testo e si crea un file `hello_world.sh`


### Shell di esecuzione 
La prima riga di uno script può essere utilizzata per indicare quale shell intrepreta lo script:

```
#! /bin/bash
```

Cosi viene indicato uno script per la shell bash.

Per conoscere quale shell si sta utilizzando, si utilizza il comando:
```
$ echo $SHELL
```

#### I commenti
I commenti vengono indicati con il simbolo `#`, e vengono ignorati dal interprete.


> [!attention] Attenzione
> `#!` e `#` sono differenti, in quanto:
>- `#!` è una sequenza di caratteri speciale ed indica al sistema operativo quale interprete utilizzare per eseguire
>lo script e deve essere inserito nella prima riga di uno script per poter essere riconosciuto correttamente
>- `#` è un simbolo utilizzato per indicare un commento all’interno di uno script. I commenti vengono ignorati dall’interprete dello script. Questo simbolo può essere usato in qualsiasi riga dello script per aggiungere notazioni o spiegazioni.

### Esecuzione di uno script 
Per eseguire uno script, è possibile utilizzare:
1. `$ bash < nome_script.sh`:
   re-direzione dello standard di input sullo script
2. `$ bash nome_script.sh`
3. `$ ./nome_script.sh`

La shell riconosce che il file di input è uno script e determina quale shell deve essere utilizzata per eseguirlo.
- La shell che esegue lo script, lo esegue leggendo i comandi come se fossero digitati direttamente nella shell stessa.
![[Esecuzione di uno script.png]]

Per fare degli esempi concreti:
1. `$ bash < nome_script.sh`
   ![[Esempio modo 1 per l'esecuzione di uno script.png]]
2. `$ bash nome_script.sh`
![[Esempio modo 2 per l'esecuzione di uno script.png]]

3. `$ ./nome_script.sh`
   Se scriviamo `./hello_world.sh`, l'output sarà: *Permission denied*, questo perché bisogna definire i permessi:
```
$ chmod u+x hello_world.sh
```
In questo modo si sta assegnando all'utente il permesso di esecuzione dello script `hello_world.sh`


### Variabili di shell
Come per i linguaggi di programmazione una variabile è:
==un nome simbolico al quale è associato un valore.== 
==Sono utilizzate per memorizzare dati che possono essere utilizzati all'interno di script e sessioni di shell==. 

La shell permette di definire 2 tipi di variabili:
1. **[[#Variabili locali|variabili locali]]**
2. **[[#Variabili di ambiente|variabili di ambiente]]** 

#### Variabili locali
==Le variabili locali non richiedono alcun comando speciale per essere create==, sono semplicemente definite con un'assegnazione di valore.
==Inoltre hanno una validità limitata all’ambito della shell stessa, in quanto sono visibili ed esistono solo all'interno e durante l’esecuzione del contesto in cui sono state definite, come una funzione o uno script==.
Il nome di una variabile può contenere lettere, cifre e underscore, **ma il primo carattere non può essere un numero**.
La creazione di una variabile e l’assegnazione di un valore si ottengono con una dichiarazione del tipo:
`nome_variabile=valore (senza spazi)`.

L'assegnazione dei valori per queste variabili seguono le seguenti regole:
- ==Se non viene fornito il valore da assegnare, si intende che la variabile è uguale ad una stringa vuota==
- ==Se la variabile non esiste, allora viene creata con il valore specificato==.
- ==Se la variabile esiste, il suo valore precedente viene sovrascritto==.

##### Il comando `unset` e il comando `$`
Il comando `unset` permette di cancellare una variabile locale.
```
$ unset nome_variabile
```

Mentre il simbolo `$`: ==permette di accedere al valore di una variabile==.
```
$ $nome_variabile
```

#### Esempi di casi d'uso
```bash
$ a=ciao
```

Crea la variabile locale con valore `ciao`

```bash
$ echo $a
```

Visualizza/accede al valore della variabile `a`

```
$ $a
```

```bash
$ b=who
```

Definisce la variabile locale `b` con valore il comando [[Linux#Il comando `$ who`|`who`]] 

```bash
$ echo $b 
```

Visualizza/accede al valore della variabile `b`

```bash
$ $b
```

esegue il comando [[Linux#Il comando `$ who`|`$ who`]]

#### Variabili di ambiente
==Le variabili di ambiente sono visibili a tutti i processi figli della shell==. 
==Questo significa che quando un processo viene eseguito dalla shell, erediterà le variabili di ambiente definite nella shell genitore==.
==Le variabili di ambiente persistono e sono accessibili ai processi figli finché la shell genitore è attiva o la variabile non viene esplicitamente eliminata==.
Esiste un insieme di variabili di ambiente predefinite, che contengono informazioni utili sull’ambiente di esecuzione. Ad esempio:
- $HOME: ==path della home directory==.
- $PATH: ==path delle directory dove la shell, dopo l’inserimento di un comando, cerca il programma da eseguire==.
- $MAIL: ==path della mailbox dell’utente==.

- $USER: ==username dell’utente==.

- $SHELL: ==path della shell di login==.
- $TERM: ==specifica il tipo di terminale utilizzato==.


### Il comando `read`
legge dallo standard input ed assegna alla prima variabile specificata la prima parola digitata, alla seconda variabile specificata la seconda parola digitata e così via.
```bash
echo "Scrivi il tuo nome e cognome"
#usa il comando read per assegnare alle variabili name e surname i valori di nome e cognome digitati
read name surname
echo "Ciao, $name $surname"
```

il comando `$bash` serve per eseguire i file:
`$ bash read_script.sh`: esegue lo script `read_script.sh`


---
## Operazioni aritmetiche
In linux è possibile eseguire operazioni aritmetiche tramite i seguenti operatori:
+ `+`: somma
- `-`: sottrazione
* `*`:prodotto
- `/`: divisione intera
- `%`: resto

Mentre gli operatori relazionali comuni sono:

| Operatore positivo | Significato           | Operatore negativo | Significato         |
| ------------------ | --------------------- | ------------------ | ------------------- |
| `>`                | **maggiore**          | `<`                | **minore**          |
| `>=`               | **maggiore o uguale** | `<=`               | **minore o uguale** |
| `=`                | **uguale**            | `!=`               | **diverso**         |
| `&&`               | **AND Logico**        | \|\|               | `OR logico`         |
### Il comando `$ expr`
Sta per *\<espressioni aritmetiche>*, permette di usare variabili numeriche e di eseguire calcoli semplici.
```
$ expr 1 + 2 #attenzione agli spazi
```
In questo caso effettua la somma tra 1 e 2

```
$ a = 9 b=3 #definisce due variabili numeriche
$expr $a - $b #effetua la sottrazione tra a e b

```

Si possono anche usare le parentesi tonde e quadre per rappresentare le espressioni aritmetiche:
```
$ a = 9 b=3 #definisce due variabili numeriche
$ echo $($a+$b)
```

Oppure: 
```
$ a = 9 b=3 #definisce due variabili numeriche
$ echo $[$a-$b]
```

### Strutture di controllo 
In ambiente Linux (come anche in programmazione) per compiere una determinata azione si usano delle strutture di controllo.

Le principali strutture di controllo sono:
- if
- case
- for 
- while
#### Struttura dell' if 
Come per python la struttura dell'if è la seguente:
```
if <condizione>:
	
then <condizione>:  #o elif in python
	
else <condizione>:
	
```

Se la prima condizione ha successo oppure è verificata viene eseguita la seconda condizione, o, se questa non è verificata, viene eseguita la condizione dell'`else`. 


