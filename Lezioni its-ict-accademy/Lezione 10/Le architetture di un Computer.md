# I dati grezzi 

==I dati si riferiscono a fatti grezzi, non elaborati, che vengono raccolti da diverse fonti. Questi fatti possono essere numeri, simboli, caratteri o anche osservazioni.==  
==I dati da soli non hanno alcun significato o contesto fino a quando non vengono elaborati o interpretati.==  
Esempi di "dati" includono:

- un valore (ad esempio, 35),
- una serie di misurazioni,
- un nome,
- un colore,  
    … e così via.

Punto chiave:  
I dati sono disorganizzati e non hanno significato diretto da soli.


--- 



# Informazione e conoscenza  

==L'informazione è ciò che ottieni quando i dati vengono elaborati e organizzati, dando un contesto ai dati.==  
Esempio di "informazione":

- un valore associato ai gradi Celsius (ad esempio, 35°C) rappresenta un valore di temperatura.

==La conoscenza è la comprensione e l'intuizione acquisita dall'interpretazione delle informazioni, rendendole utili per prendere decisioni. La conoscenza risponde a domande come "cosa," "chi," "quando" e "quanto."==  
Esempio di "conoscenza":

- un valore di temperatura come 35°C diventa conoscenza quando viene interpretato come un ambiente caldo.  

---

## La gestione dell'informazione: 
### il Codice Binario 

Qualsiasi informazione memorizzata o recuperata da un dispositivo (come computer desktop, laptop o smartphone) deve essere rappresentata in un linguaggio che il dispositivo possa comprendere. Questo linguaggio è noto come Codice Binario.  
Il Codice Binario è definito come un sistema di codifica che utilizza le cifre binarie 0 e 1 per rappresentare lettere, cifre o altri caratteri in un computer o in altri dispositivi elettronici, come smartphone e tablet.

Più specificamente, un BIT (cifra binaria) è l'unità di base di informazione utilizzata dai dispositivi per gestire tutti i tipi di dati. Un singolo BIT può esistere in uno dei due stati: 0 o 1.
> [!NOTE] NOTA
> Con un singolo BIT, possono essere rappresentati solo due elementi.  
Ad esempio:  
>```
1 = "A"  
0 = "B"
>```

#### Bit e Combinazioni: 
- Un bit può avere 2 stati: 0 o 1.  
- Con N bit possiamo creare 2^N combinazioni distinte.

Esempi:  
o 1 bit: 2^1 = 2 combinazioni (0, 1)  
o 2 bit: 2^2 = 4 combinazioni (00, 01, 10, 11)  
o 3 bit: 2^3 = 8 combinazioni (000, 001, 010, 011, 100, 101, 110, 111)

#### Intervallo di Valori:  
Con N bit, i valori rappresentabili vanno da 0 a 2^N − 1.

Esempi:  
o 1 bit: 2^1 − 1 = 1, valori rappresentabili nell'intervallo `[0,1]`  
o 2 bit: 2^2 − 1 = 3, valori rappresentabili nell'intervallo `[0,3]`  
o 3 bit: 2^3 − 1 = 7, valori rappresentabili nell'intervallo `[0,7]`.

==All'interno del dispositivo, tutto è rappresentato da un insieme di cifre binarie.== Più specificamente:  
- Qualsiasi Sistema Operativo (ad esempio, Windows, Android, Mac OS, Linux)  
- Qualsiasi Programma/Applicazione (ad esempio, Word, Excel, Skype, Firefox)  
- Qualsiasi Comando/Interazione (ad esempio, Tastiera, Mouse, Touchpad).  

## ASCII Code

Il Codice Standard Americano per la Codifica delle Informazioni (ASCII) utilizza tipicamente 7 bit per rappresentare ogni carattere, il che consente di avere 128 codici di caratteri unici.  
**ASCII Esteso**: ASCII a volte viene esteso a 8 bit, il che permette di aggiungere 128 caratteri in più, portando il totale a 256. Questa estensione non è standardizzata allo stesso modo dell'originale ASCII a 7 bit, e ci sono vari set di ASCII esteso, come ISO 8859-1 o Windows-1252, che includono caratteri per lingue specifiche o simboli grafici.

**Tipi di Caratteri**:  
• **Caratteri Alfanumerici**: Comprende tutte le lettere maiuscole e minuscole dell'alfabeto inglese e i numeri (0-9).  
• **Simboli**: ASCII include un insieme di simboli di punteggiatura comuni e altri simboli vari come @, #, $, ecc.  
• **Caratteri di Controllo**: Questi sono caratteri non stampabili che controllano il flusso del testo o il suo processo in qualche modo. Esempi includono TAB (tabulazione orizzontale), LF (line feed), CR (ritorno a capo) e BEL (campanello/avviso).    

---
## Comprendere le Dimensioni dei Dati Digitali

Questa tabella fornisce un confronto tra le dimensioni dei dati utilizzando diversi prefissi, le loro dimensioni decimali, le approssimazioni binarie e gli esempi pratici.  
• Un gruppo di 8 bit è chiamato Byte;  
![[Tab bit.png]] 

All'interno di ogni dispositivo, le informazioni sono rappresentate da un insieme fisso di byte:  
• 16 bit (2 byte)  
• 32 bit (4 byte)  
• 64 bit (8 byte)

Il numero di byte indica la "potenza" di un dispositivo. Maggiore è il numero di byte:  
• Maggiore è la capacità del dispositivo di eseguire calcoli complessi  
• Maggiore è la capacità del dispositivo di gestire grandi quantità di informazioni  
• Maggiore è la capacità del dispositivo di elaborare istruzioni complesse.

---

## Le proprietà del Codice Binario

Come ogni sistema numerico, il codice binario ha le sue proprietà intrinseche. Una proprietà chiave, condivisa con altri sistemi posizionali, è la capacità di convertire numeri da una base numerica a un'altra.  
Inoltre, il sistema binario supporta le quattro operazioni di base:

- Addizione;
- Sottrazione;
- Moltiplicazione;
- Divisione.

>[!note] NOTA:  
>Un numero rappresentato con due cifre è chiamato numero binario (base due).  
>Un numero rappresentato con dieci cifre è chiamato numero decimale (base dieci).

---

## Calcoli aritmetici con il codice binario 

### Conversione decimale in Binario 

Per convertire un numero decimale (base 10) in un numero binario (base 2), segui questi passaggi:

1. Dividi il numero per 2.
2. Annota il resto (0 o 1). Questo sarà il bit meno significativo (LSB).
3. Continua a dividere il quoziente ottenuto nel passaggio precedente per 2, annotando i resti.
4. Ripeti fino a quando il quoziente non è 0.
5. Scrivi i resti in ordine inverso: dal più recente al primo ottenuto.  
   Questo rappresenta il numero in binario.

**Conversione da Decimale a Binario**  
Convertiamo **13** in binario:  
13 ÷ 2 = 6, resto = 1  
6 ÷ 2 = 3, resto = 0  
3 ÷ 2 = 1, resto = 1  
1 ÷ 2 = 0, resto = 1  
Risultato in binario: **1101₂**.

> [!NOTE] NOTA
> Si parte dal basso verso l'alto per leggere il numero binario, difatti il risultato è 1101
 
### Conversione Binario in decimale 

Per convertire un numero binario (base 2) in un numero decimale (base 10), segui questi passaggi:

1. Scrivi il numero binario.
2. Elenca le potenze di 2 da destra a sinistra, iniziando con 2^0 sotto il bit più a destra.
3. Moltiplica ogni bit per la corrispondente potenza di 2.
4. Somma i risultati per ottenere il numero decimale.

**Conversione da Binario a Decimale**  
Convertiamo **1101₂** in decimale:  
1101 = 1 ∙ 2^3 + 1 ∙ 2^2 + 0 ∙ 2^1 + 1 ∙ 2^0  
= 8 + 4 + 0 + 1 = 13  
Risultato in decimale: **13₁₀**.  

### L'addizione binaria

Prendi i due numeri binari che vuoi sommare.  
>[!note] NOTA: Assicurati che entrambi i numeri abbiano la stessa lunghezza.
>  Se non lo sono, aggiungi zeri iniziali al numero più corto fino a che non abbiano la stessa lunghezza.

2. Inizia a sommare i bit dalla parte destra (bit meno significativo) dei due numeri binari, seguendo queste regole:  

![[Bin add.png]]

3. Continua sommando i bit successivi e considerando eventuali riporto dalle colonne precedenti. Se dopo aver sommato l'ultimo bit rimane un riporto, scrivilo nella colonna più a sinistra del risultato.  
Esempio dell'addizione binaria:  
```
Binary Addition/2
Example 1 (1011 + 1101):
1011
+ 1101
-----------
11000 (Result: carry applied)
```

```
Step-by-step addition with carry:
1 + 1 = 0 (carry 1)
1 + 0 + 1 (carry) = 0 (carry 1)
0 + 1 + 1 (carry) = 0 (carry 1)
1 + 1 + 1 (carry) = 1 (carry 1 to a new
column)
```

```
Example 2 (1011 + 101):
1011
+ 0101
-----------
10000 (Result: carry applied)
```

```
Step-by-step addition with carry:
1 + 1 = 0 (carry 1)
1 + 0 + 1 (carry) = 0 (carry 1)
0 + 1 + 1 (carry) = 0 (carry 1)
1 + 0 + 1 (carry) = 0 (carry 1 to a new
column
```

### Sottrazione Binaria  

Prendi i due numeri binari che vuoi sottrarre.  
> [!note] NOTA: Assicurati che entrambi i numeri abbiano la stessa lunghezza.  
>Se non lo sono, aggiungi zeri iniziali al numero più corto fino a che non abbiano la stessa lunghezza.

2. Inizia a sottrarre i bit dalla parte destra (bit meno significativo) dei due numeri binari, seguendo queste regole:  

![[Bin sub.png]]
3. Continua sottraendo i bit successivi e considerando eventuali prestiti dalle colonne precedenti. Se dopo aver sottratto l'ultimo bit rimane un prestito, scrivilo nella colonna più a sinistra del risultato.  
```
Example 1 (1110 – 1001):
1110
- 1001
---------
0101 (Result: borrow applied)
```

```

Step-by-step subtraction with borrow:
0 - 1 = 1 (borrow 1)
1 - 0 - 1 (borrow) = 0
1 - 0 = 1
1 - 1 = 0
```

```
Example 2 (1011 - 101):
1011
- 0101
-----------
0110 (Result: borrow applied)
```

```
Step-by-step subtraction with borrow:
1 – 1 = 0
1 – 0 = 1
0 - 1 = 1 (borrow 1)
1 - 0 - 1 (borrow) = 0
```

---

# L'algebra Booleana 

==L'Algebra Booleana è un ramo dell'algebra che si occupa di valori veri o falsi, tipicamente denotati come `1` e `0`, rispettivamente.== 
È fondamentale nel campo dell'informatica e dell'elettronica digitale perché viene utilizzata per progettare e analizzare il comportamento di circuiti digitali e porte logiche.
> [!info] Concetti chiave:  ^keyConc-alBool
>  1. Variabili binarie:   
>  Rappresentate come 1 (vero) e 0 (falso).
>   2.  Operazioni logiche:  
>  - [[Ripasso Python#L'operatore Le architetture di un Computer L'algebra Booleana AND|AND]] (\*): 
>  Restituisce vero se entrambi gli operandi sono veri (1 \* 1 = 1).  ^andOp-Def
> - [[Ripasso Python#^de8a18|OR]] (+): 
>  Restituisce vero se almeno uno degli operandi è vero (1 + 0 = 1).  ^orOp-Def
>  - [[Ripasso Python#^notOp-Py|NOT]] (¬): 
>    Restituisce l'inverso dell'operando (¬1 = 0) (è il segno meno). ^notOp-Def

### Tabelle di verità 
 
|  A  |  B  | A  AND  B |
| :-: | :-: | :-------: |
|  0  |  0  |     0     |
|  0  |  1  |     0     |
|  1  |  0  |     0     |
|  1  |  1  |     1     |

|  A  |  B  | A OR B |
|:---:|:---:|:------:|
|  0  |  0  |   0    |
|  0  |  1  |   1    |
|  1  |  0  |   1    |
|  1  |  1  |   1    |

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

• Commutative:
A OR B = B OR A
A AND B = B AND A
• Distributive:
A OR (B AND C) = (A OR B) AND (A OR C)
A AND (B OR C) = (A AND B) OR (A AND C)
• De Morgan’s Law:
NOT (A AND B) = (NOT A) OR (NOT B)
NOT (A OR B) = (NOT A) AND (NOT B)


> [!attention] Le regole di precedenza
> 1. NOT ha la precedenza più alta su tutti gli altri operatori
>  2. Segue AND  
> 
>3. Per ultimo c'è OR
>Per alternare la precedenza si usano le parentesi, ovvero l'operatore dentro la parentesi ha la precedenza su tutti gli altri.





