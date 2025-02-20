
La differenza tra linguaggi **tipizzati staticamente** (statically-typed) e **tipizzati dinamicamente** (dynamically-typed) riguarda il momento in cui il tipo di una variabile viene determinato e come viene gestito durante l'esecuzione del programma.
# Statically-typed (Tipizzazione statica)
### Definizione:
La tipizzazione statica significa che ==il tipo delle variabili è determinato al momento della compilazione: cioè prima che il programma venga eseguito.== 
Ogni variabile deve avere un tipo dichiarato esplicitamente o inferito dal compilatore dal compilatore. 
==Una volta che una variabile è stata dichiarata con un certo tipo, non può contenere valori di tipo diverso.== 

### Caratteristiche
- **Tipo determinato al momento della compilazione**: 
  ==In un linguaggio tipizzato staticamente, il tipo di una variabile è noto prima che il programma venga eseguito==. 
  Questo tipo viene dichiarato esplicitamente dal programmatore (ad esempio, con la sintassi `int` in C o `String` in Java), oppure può essere dedotto dal compilatore.
- **Controllo dei tipi a compile-time**: 
  ==Poiché i tipi sono noti prima dell'esecuzione, il compilatore verifica la correttezza dei tipi, riducendo la possibilità di errori relativi ai tipi durante l'esecuzione del programma.==
- **Sicurezza sui tipi**: 
  ==Gli errori relativi ai tipi (come cercare di sommare una stringa con un numero) vengono catturati durante la compilazione, prima che il programma venga eseguito.==
- **Esempi di linguaggi**: 
  C, C++, Java, C#, Rust, Swift, etc.

#### Esempio in C:
```c
#include <stdio.h>

int main() {
    int x = 5;  // La variabile x è dichiarata come intero
    x = "Hello";  // ERRORE: non puoi assegnare una stringa a una variabile di tipo int
    return 0;
}
```

In questo esempio: 
- La variabile `x` è dichiarata come un intero (`int`).
- Quando tentiamo di assegnare una stringa a `x`, il compilatore segnala un errore, perché `x` è di tipo `int` e non può contenere una stringa.

### Tabella dei vantaggi e svantaggi dei linguaggi tipizzati staticamente

| Vantaggi                                                                             | Svantaggi                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Maggiore sicurezza sui tipi                                                          | Maggiore verbosità e necessita di dichiarazioni esplicite          |
| Rilevamento precoce degli errori durante la compilazione                             | Maggiore rigidità nel tipo di dati che una variabile può contenere |
| Maggiore ottimizzazione delle prestazioni, poiché i tipi sono conosciuti in anticipo |                                                                    |

# Tipizzazione Dinamica (Dynamically-Typed)

### Definizione 
==La tipizzazione dinamica significa che il tipo di una variabile viene determinato **durante l'esecuzione del programma**, non al momento della compilazione.== 
Le variabili non hanno bisogno di una dichiarazione esplicita del tipo. 
==Il tipo della variabile può cambiare mentre il programma è in esecuzione.==

### Caratteristiche 
- **Tipo determinato a runtime**: 
  ==In un linguaggio tipizzato dinamicamente, il tipo di una variabile viene determinato durante l'esecuzione del programma, non prima.== 
  Le variabili non devono essere dichiarate con un tipo esplicito.
- **Controllo dei tipi a runtime**: 
  ==Il tipo di variabile viene verificato mentre il programma è in esecuzione.== 
  Ciò significa che è possibile assegnare valori di tipo diverso alla stessa variabile in momenti diversi.
- **Maggiore flessibilità**: 
  ==Le variabili possono cambiare tipo durante l'esecuzione, il che offre una maggiore flessibilità, ma aumenta anche il rischio di errori (ad esempio, cercare di usare una stringa come un numero).== 
- **Esempi di linguaggi**: 
  Python, JavaScript, Ruby, PHP, Perl.

### Tabella dei vantaggi e svantaggi dei linguaggi tipizzati dinamicamente 

| Vantaggi                                                                  | Svantaggi                                                                                                                              |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Maggiore flessibilità                                                     | Maggiore possibilità di errori durante l'esecuzione (i controlli sui tipi vengono effettuati solo mentre il programma è in esecuzione) |
| Scrittura di codice più conciso senza necessità di dichiarazioni del tipo | Più difficile per il compilatore (o l'interprete) ottimizzare il codice, poiché i tipi sono sconosciuti in anticipo.                   |


### Sintesi delle differenze
> [!example]+ Tabella di sintesi delle Differenze 
> 
>| Caratteristiche         | Tipizzazione Statica                                                | Tipizzazione Dinamica                                                     |
>| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------- |
>| Determinazione del tipo | Il tipo è determinato **prima dell'esecuzione** (a compilazione).   | Il tipo è determinato **durante l'esecuzione** (a runtime).               |
| Dichiarazione del tipo  | Richiede una dichiarazione esplicita o inferenza dei tipi.          | Non richiede dichiarazione del tipo. Il tipo è determinato dinamicamente. |
| Controllo dei tipi      | Controllo dei tipi **durante la compilazione**.                     | Controllo dei tipi **durante l'esecuzione**.                              |
| Flessibilità            | Meno flessibile, più rigido                                         | Maggiore flessibilità, più dinamico.                                      |
| Sicurezza sui tipi      | Maggiore sicurezza (errori di tipo rilevati prima dell'esecuzione). | Meno sicurezza (errori di tipo possono verificarsi a runtime).            |
>


> [!example] Per Ricapitolare
> 1. **Tipizzazione statica**: 
>    Garantisce maggiore sicurezza e stabilità del codice, poiché gli errori sui tipi vengono catturati dal compilatore prima che il programma venga eseguito
> 2. **Tipizzazione dinamica**: 
>    Offre maggiore flessibilità, permettendo di scrivere codice più conciso e di adattarsi rapidamente ai cambiamenti, ma comporta il rischio di errori che emergono solo durante l'esecuzione.


## Elenco dei vari tipi di linguaggio 

### Linguaggi tipizzati staticamente 
1. **C**
2. **C++**
3. **Java**
4. **C#**
5. **Rust**
6. **Go**
7. **Swift**
8. **Kotlin**
9. **Scala**
10. **Haskell**

### Linguaggi Tipizzati dinamicamente
1. **Python**
2. **JavaScript**
3. **Ruby**
4. **PHP**
5. **Perl**
6. **Lua**
7. **R**
8. **MATLAB**
9. **Bash (e shell scripting in generale)**
10. **Smalltalk**