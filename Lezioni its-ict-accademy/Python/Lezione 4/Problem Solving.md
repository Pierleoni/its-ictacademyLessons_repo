# Tipi di Errore
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


Quando si programma, un modo efficiente di risolvere i problemi è scomporre il problema in problemi più piccoli:
prendiamo l'esercizio 9 quello sulla serie del pi greco.
![[Ex9_pi_greco.py]] 

Partendo da questo esercizio:
- **Leggere e comprendere il testo dell’esercizio**
    
    - Identificare cosa il programma deve fare.
    - Individuare eventuali formule o regole matematiche da applicare (nel caso della serie di Pi Greco, la formula di Leibniz).
- **Identificare i sotto-problemi**
    - **Definire una funzione** per calcolare l'approssimazione di π.
    - **Capire la struttura del ciclo**:
        - Come generare i termini della serie.
        - Come alternare i segni (+ e -).
    - **Definire la condizione di uscita**:
        - Decidere se iterare per un numero fisso di termini o fino a un errore accettabile.
- **Scrivere un piano logico prima di programmare**
    - Creare una bozza dell’algoritmo in pseudocodice o con un diagramma di flusso.
    - Definire chiaramente i passaggi necessari per costruire la soluzione.
- **Implementare il codice a piccoli passi**
    - Testare ogni parte separatamente per evitare errori complessi.
    - Usare **stampa di debug** (`print()`) per controllare che ogni passaggio funzioni come previsto.
- **Verificare l’accuratezza della soluzione**
    - Confrontare i risultati ottenuti con il valore reale di π.
    - Analizzare il numero di iterazioni necessarie per ottenere una buona approssimazione.
- **Ottimizzare il codice**
    - Eliminare istruzioni ridondanti.
    - Valutare se esistono metodi più efficienti per migliorare la velocità di convergenza della serie.
- **Documentare il codice**
    - Aggiungere commenti per spiegare le parti più importanti.
    - Rendere il codice leggibile e ben organizzato per future revisioni.