## Gestione degli Errori
Le eccezioni sono situazioni anomalie che possiamo ad andare a gestire durante l'esecuzione di un programma.
Quando si verifica un eccezzione, un programma può terminare la sua esecuzione 
La **gestione degli errori** è il meccanismo che consente di **interrompere il normale flusso di esecuzione** quando si verifica un problema e di trasferire il controllo a un **gestore degli errori** capace di affrontare la situazione.
[![Gli Errori in Java](https://i.postimg.cc/yxPBGc8c/Screenshot-2026-01-29-at-14-57-31-Microsoft-Power-Point-Java-11-Eccezioni-Compatibility-Mode-Java.png)](https://postimg.cc/bSsKDGbw)
Supponiamo di avere un metodo che calcola la suddivisione tra due Interi, se il divisore è 0 l'esecuzione del programma si interrompe generando la seguente eccezzione:
```
Exception 
```

### Classificazione delle eccezioni 
Le eccezioni possono essere di 2 tipi:
- Eccezioni controllate : dovute eventi che si verificano esternamente al software 
	- Si chiamano controllate in quanto il compilatore verifica che vengano indicate e intercettate nel nostro software. Se non Vengono indicate, avremo degli errori di compilazione. 
```java
public String readFile(BufferedReader br) throws java.io.IOException{
	...
}
```

Nell'esempio precedente, se non inseriamo il costruttore `throws` avremo un errore in fase di compilazione.
Quindi l'app non parte.
- Eccezzioni non controllate: 
	- sono docutre al codice scritto nel nostro programma ed in linea teroiaca potrebbero essere evitate 
	- Rappresentano i famosi bug software 
	- QUeste eccezzioni non vengono verificate dal compilatore e si possono verificare solo durante l'esecuzioni del programma.
```java
public String contaCarretteri(String testo){
	return.testo.length();
}
```
Nell'esempio precedente, se la variabile testo è null, riceveremo un eccezione.
Il compilatore pero in fase di compilazione non rileva questa possibile eccezione (ecco perché si dice unchecked).

### I meccanismi di gestione delle eccezzioni
Java consente di gestire le eccezioni in mmodo flessibile ed elegante, in quanto le eccezzioni sono oggetti di classi particolari.
Cosa accade quando si verifica un eccezione?
- Quando si verifica un eccezione 
È possibile catturare l'eccezzioni

Le eccezzioni in Java sono sottoclassi delle classi java.lang.Throwable, grazie all'ereditarietà è possible definire gerarchie di eccezzioni. 
La classi Thorwable 


### Tipi di errori comuni

1. **Errori di input dell’utente**  
    Esempio: l’utente inserisce un valore non valido in un modulo.
    
2. **Errori dei dispositivi**  
    Esempio: impossibilità di leggere da un file o da una periferica.
    
3. **Errori di codice**  
    Esempio: divisione per zero, accesso a un indice inesistente di un array.
    
4. **Restrizioni fisiche**  
    Esempio: esaurimento memoria o limiti hardware.

### Tecniche di gestione degli errori

#### Metodo classico

- Il metodo dove si verifica l’errore **restituisce un codice speciale** (ad esempio `-1` o `null`).
    
- Il **metodo chiamante** deve controllare questo valore e gestire l’errore.
    
- Svantaggio: il codice diventa spesso difficile da leggere e da mantenere, perché la gestione degli errori si mescola con la logica principale.
    

### Java e le eccezioni

- Java permette di **uscire dal metodo con un percorso alternativo** senza dover restituire il valore normale previsto.
    
- Questo percorso alternativo è rappresentato da **oggetti che modellano l’errore**, chiamati **eccezioni** (`Exception`).
    
- Le eccezioni consentono di separare la **logica normale** dalla **gestione degli errori**, rendendo il codice più leggibile e modulare.
    



### Come funziona la gestione delle eccezioni

1. Quando si verifica un errore, Java **cerca un gestore** dell’errore (`catch`) in grado di risolvere la situazione.
    
2. Il gestore può **interagire con le entità coinvolte** per tentare di risolvere il problema (ad esempio, ripetere un’operazione, mostrare un messaggio all’utente, registrare l’errore).
    
3. Se nessun gestore è presente, l’eccezione viene propagata lungo la catena di chiamate fino a che non viene trovata una soluzione, altrimenti il programma termina.
    

**Nota:** tutte le eccezioni gestibili in Java derivano dalla classe base `Exception`.