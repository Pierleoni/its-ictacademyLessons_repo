# Esercitazione [[Algoritmi e Diagrammi a blocchi|diagramma a blocchi]] 

### Esercizio 1: Calcolare il cateto di un triangolo rettangolo
![[Esercizio 1.svg]]

### Esercizio 2: Trovare il massimo tra 4 numeri 


![[esercizio 2.svg]]

Soluzione alternativa:
![[Soluzione Alt Ex 2.svg]]




## Speigazione Esercizi a blocchi 

per fare i diagrammi a blocchi:

1.Expected output: leggendo la traccia cerchiamo di capire pezzo per pezzo l'output che aspettiamo di avere (es:  

1. user-number 1: 15.  ^first-ite

2. user-number 2: 4.    ^second-ite

3. user-number 3: 17.  ^third-ite

4. use-number 4: 13.   ^fourth-ite

5. user-number 5: 38.  ^fifth-ite

6. user-number 6: 10) .  ^sixth-ite

Dopo aver impostato i 6 numeri, impostare la somma:  
sommaPari= 4+38+10 = 52  
  
2. Quali strutture devo usare?   
- Condizioni?
- cicli?
- variabili?  
- Collections?   
Fatto ciò devo tornare a leggere la traccia, per 6 volte nell'expected output ho inserito per 6 volte il numero, quindi se devo svolgere una azione e la devo ripetere tante volte (in questo caso 6 volte) devo usare un ciclo perché così inserisco le iterazioni in modo automatico.   
Il ciclo porta con sé automaticamente una dichiarazione di una variabile, perché il ciclo per essere dichiarato e ripetuto devo impastare una condizione e per creare una condizione devo impostare una variabile. (es: questa condizione deve essere un contatore che mi conta le ripetizioni del ciclo, dette anche iterazioni).   
Altro suggerimento, nella traccia c'è scritto "in input": in questo caso devo mettere un altra variabili perché se l'utente digita da tastiera questi valori devo salvarli da qualche parte.

3. Di quante variabili ho bisogno? 
- Nella traccia c'è scritto "input": 
    Quindi ho bisogno di 1 variabile per salvare il numero 'n' dato in input dall'utente. 
- 1 variabile da usare come contatore per il ciclo 
- 1 variabile per la somma 

4. Impostare il ragionamento
Abbozzarlo in maniera brutta, ma mi serve per capire cosa devo fare e come impostare il mio diagramma blocchi per poi scrivere il mio codice. 
Per ogni iterazione: 
- inserire il numero `n`

> [!hint] il valore di `n` cambia per ogni iterazione del ciclo, quindi se devo fare operazioni con il valore di `n`, devo farla prima di inizializzare il ciclo

Poiché sto salvando il valore inserito dall'utente, in una variabile `n`, il valore che `n` assume esiste solo ed esclusivamente nella iterazione corrente del ciclo (cioè quella attuale), per esempio 
se `i = 2`, `n=4`
se `i=3`, `n=17`. 
- Inserisco numero `n`, faccio il check per vedere se `n` è pari 
  Di conseguenza se n è pari → faccio una freccia sotto(true) e scrivo "aggiorno". → se n è dispari (freccia sotto "False"), non faccio nulla. 
- Alla fine di tutto, devo aggiornare il contatore
  Cercare di aggiornare il contantore coe ultima cosa del nostro cilco, questo perché:
  Se l'aggiorniamo all'inizio sbaglieremo perché se la vairiabile n varia di valore e aggiorno il contatore mi darà dei valori sballati in output. 

5. Fare il diagramma 

![[Demo diagramma a blocchi.svg]] 

6. Fare il check del diagramma 
Questo check mi aiuta molto ad impostare le condizioni:
i = 1 
somma = 0 

---
Adesso sono nel ciclo: 
1. [[#^first-ite|Prima iterazione]] 
`i<=6` 
`i = 1` 
`n= 15`
Adesso 15 è pari, ovviamente non pari quindi:
`somma = 0` 

2. [[#^second-ite|Seconda iterazione]] 
quindi adesso: 
`i = 1 +1 = 2` 
`n + 4` 
4 è pari, per cui: 
`somma = somma + n = 0 + 4 = 4`  

3. [[#^third-ite|Terza Iterazione]] 
Torno al ciclo e aggiorno i
`i = 3` 
3 è minore di 6, per ciò 
`n = 17` 
17 è pari, no quindi non aggiorno la somma che rimane 
`somma = 4` 

4. [[#^fourth-ite|Quarta iterazione]] 
`i = 4` 
Torno sopra: 4 è minore di 6, quindi passo a leggere un altro numero; i alla 4 iterazione è 
`i = 4` 
`n = 13`
13 è dispari per cui: 
`somma = 4` 
Torno giù e aggiorno il mio contatore 
5. [[#^fifth-ite|Quinta Iterazione]] 
`i = 5` 
`n = 38`  
38 è pari per cui: 
`somma = 4 + 38 = 42` 

6. [[#^sixth-ite|sesta iterazione]] 
Torno al ciclo: 
`i = 6` 
`n = 6` 
10 è pari, per cui 
`somma = 42 +10 =52` 

7. Settima Iterazione 
aggiorno la i
`i= 7` 
7 è maggiore di 6 per cui esco dal ciclo e vado all'output che mi stampa  52, e siccome ottengo lo stesso valore della somma dell'expetced output allora vuol dire che il mio algoritmo funziona bene. 

### Esercizio 5


![[Diagram Ex 5.svg]]


### Esercizio 7
![[Diagram Ex 7.svg]]



### Esercizio 10 
![[DiagramEx 10.svg]]