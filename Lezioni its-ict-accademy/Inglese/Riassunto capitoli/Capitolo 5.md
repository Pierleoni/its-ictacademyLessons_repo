# **PENSIERO COMPUTAZIONALE**  
È meglio assumere che l'utente inserisca input errati a un certo punto. Pensa a tutte le possibilità in cui un input potrebbe essere sbagliato:

- Se la tua soluzione si aspetta un numero, controlla che sia effettivamente un numero prima di fare qualsiasi cosa con esso. Inserire ‘9O’ invece di ‘90’ è un errore abbastanza facile da fare.
    
- Allo stesso modo, se la tua soluzione richiede un input in un certo intervallo, controllalo dopo che è stato inserito. Assicurarsi che un numero di conto sia lungo esattamente otto cifre è veloce e semplice. Basta contare il numero di cifre nell'input e assicurarsi che sia corretto.
    
- Formati errati: numeri di telefono, URL di siti web, indirizzi email, date e orari sono tutti esempi di dati che devono rispettare un formato specifico.
    

Essere proattivi e proteggersi da comportamenti indesiderati è essenziale. Tuttavia, alcuni bug si insinueranno nonostante i tuoi sforzi.

**TESTING**  
Questa sezione descrive il testing, un metodo per individuare bug nascosti in un sistema completamente o parzialmente funzionante.

**Obiettivo**  
Lo scopo del testing è usare il sistema che hai prodotto per verificare se funziona come previsto e identificare aree specifiche in cui fallisce. Pertanto, il testing deve aspettare che la tua soluzione abbia raggiunto uno stato di lavoro. Potrebbe essere completamente funzionante, il che ti permette di testare l'intero sistema, oppure potrebbe essere parzialmente funzionante, consentendoti di testare singole parti.  
Per testare efficacemente, è necessario sapere esattamente cosa la soluzione si prefigge di fare. Questo rende fondamentale il consiglio del Capitolo 3: definire chiaramente l'obiettivo della tua soluzione. Verificare che un sistema funzioni come previsto quando le aspettative sono vaghe porta a poco. L'obiettivo della soluzione serve come guida per il testing.

**Approccio**  
Nel testing è molto importante essere sistematici. Il testing ad hoc, senza un approccio particolare, è facile da fare, ma l'unica cosa che probabilmente scoprirai è che qualcosa non va da qualche parte. Essere sistematici ti aiuterà a localizzare il problema e scoprire esattamente cosa non va e dove.  
Puoi scegliere tra due approcci al testing, a seconda di ciò che vuoi ottenere. Il primo è il testing "top-down", in cui testi la soluzione nel suo complesso per assicurarti che funzioni. Questo è particolarmente utile per trovare difetti nel design e verificare che il sistema sia ben integrato. Il secondo approccio è "bottom-up", che richiede di iniziare testando le singole parti della soluzione. Questo permette di verificare che ciascuna parte adempia correttamente ai suoi compiti all'interno del sistema e mostra che la soluzione è costruita su basi solide

**Tabella 5.1: Vantaggi e svantaggi del testing top-down e bottom-up**

| Vantaggi      | Svantaggi                                                                            |
| ------------- | ------------------------------------------------------------------------------------ |
| **Top-down**  | Efficace per trovare difetti di design.                                              |
|               | Può essere incoraggiante testare un sistema completo, anche se incompleto o con bug. |
|               |                                                                                      |
| **Bottom-up** | Facile da applicare nelle prime fasi dello sviluppo.                                 |
|               | Efficace per localizzare problemi.                                                   |



Se possibile, dovresti combinare questi approcci durante il testing, ottenendo il meglio di entrambi i mondi. Quando inizi a implementare la tua soluzione, puoi cominciare mettendo insieme una struttura scheletrica con segnaposti. Questo dovrebbe essere eseguibile, anche se potrebbe non fare nulla di utile per ora. Successivamente, puoi iniziare a implementare i singoli pezzi, sostituendo ogni segnaposto con una parte funzionante che puoi testare immediatamente in isolamento (questo è il testing bottom-up). Allo stesso tempo, poiché hai una struttura scheletrica funzionante, puoi testare l'intero sistema per assicurarti che funzioni ancora come previsto (testing top-down).

**Testare singole parti**  
Se hai seguito i consigli dei Capitoli 3 e 4, in modo che la tua soluzione esista in pezzi relativamente indipendenti, il testing sarà più semplice. Testando solo piccole parti della soluzione alla volta, sarà più facile localizzare il problema. I test che esercitano solo singole parti sono chiamati unit test. Tuttavia, testare le singole parti può essere complicato e merita qualche spiegazione. La difficoltà nasce dal fatto che le singole parti della tua soluzione normalmente operano come parte di un sistema più grande e quindi presumono che il resto del sistema sia presente e corretto. Questo non è il caso quando vengono testate in isolamento, quindi dovrai simulare tutto ciò di cui la parte dipende.

Ad esempio, alcuni componenti si aspettano di ricevere parametri come parte del loro lavoro normale, quindi per testarli dovrai fornire dei dati fittizi che simulano il funzionamento normale. Nel caso ideale, dovresti pensare a ogni valore diverso che potrebbe essere fornito e poi eseguire un test per ciascuno di essi. Se riuscissi a farlo, potresti garantire con certezza che il componente funzioni come previsto. Tuttavia, spesso ciò è irrealizzabile a causa del numero elevato di varianti possibili.

Per illustrare questo, userò l'esempio del gioco FizzBuzz. In questo gioco, i giocatori si alternano a contare in avanti da 1, sostituendo qualsiasi numero divisibile per 3 con la parola "Fizz" e qualsiasi numero divisibile per 5 con "Buzz". I numeri divisibili sia per 3 che per 5 sono sostituiti con "FizzBuzz". Un giocatore perde se dice un numero quando avrebbe dovuto dire una di queste parole. I primi numeri nella sequenza corretta sono:  
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz …

Un gioco FizzBuzz basato su computer richiede una subroutine che calcoli la risposta corretta per un numero dato. Per testare che questa subroutine funzioni, potresti provarla per i primi 20 valori. Questo ti direbbe con certezza se funziona per quei valori. Ma funziona per 21? Tecnicamente, non lo sai con certezza. Il problema è che, indipendentemente da quanto grande sia il set di valori di test, esistono più numeri che potresti includere. Inoltre, più grande è il set di test, più tempo ci vorrà per eseguire tutti i test.

Nonostante ciò, puoi essere sistematico. Un componente in una soluzione di solito stabilisce requisiti riguardo ai dati in ingresso e puoi usare queste informazioni per rendere il tuo testing sistematico. Ogni requisito corrisponde a un insieme distinto di input chiamato classi di equivalenza. La caratteristica che lega tutti gli input di ogni classe è che suscitano lo stesso tipo di risposta dalla soluzione. Di conseguenza, puoi scegliere uno (o più) pezzi di dati di test rappresentativi da ogni gruppo per rappresentare tutti gli altri valori in quella classe. Puoi fare lo stesso con i dati di input che contraddicono ciascun requisito.

Per il gioco FizzBuzz, possiamo dividere tutti gli input in diverse classi di equivalenza, scegliere un valore rappresentativo da ciascuna classe, passarli alla subroutine e poi verificare che in ogni caso venga restituita la risposta corretta. Le classi includono:

- Numeri normali accettabili (ad esempio, 8): rappresenta tutti i numeri accettabili non divisibili né per 3 né per 5. La subroutine dovrebbe restituire lo stesso numero che gli abbiamo dato. Se questo numero funziona, implica che anche tutti gli altri numeri in questa classe funzionano.
    
- Fizzes (ad esempio, 3): rappresenta tutti i numeri divisibili per tre. La subroutine dovrebbe restituire “Fizz”.
    
- Buzzes (ad esempio, 10): rappresenta tutti i numeri divisibili per cinque. La subroutine dovrebbe restituire “Buzz”.
    
- FizzBuzzes (ad esempio, 30): rappresenta tutti i numeri divisibili sia per tre che per cinque. La subroutine dovrebbe restituire “FizzBuzz”.
    
- Numeri inaccettabili (ad esempio, -10): i numeri fuori intervallo dovrebbero essere rifiutati.
    
- Non numeri (ad esempio, VII): solo numeri arabi, per favore. Un computer lo considera come un testo e dovrebbe rifiutarlo.
    

E, poiché "i bug si annidano negli angoli e si radunano sotto le pietre", un altro test fondamentale è quello che verifica che il sistema si comporti come previsto se l'utente immette un valore malformato.
---
# Traduzione in inglese
**COMPUTATIONAL THINKING**

It's important to anticipate that users will eventually enter incorrect input. There are several common ways input can be flawed:

- If your solution expects a number, make sure it really is a number before proceeding. For example, entering '9O' instead of '90' is an easy mistake to make.
    
- Similarly, if your solution requires input within a certain range, check the input after it's entered. For instance, ensuring an account number has exactly eight digits is simple: just count the digits and ensure it matches.
    
- Incorrect formats: data such as phone numbers, URLs, email addresses, dates, and times all require a specific format.
    

Being proactive and guarding against unwanted behavior is essential, but some bugs will inevitably slip through despite your efforts.

**TESTING**

This section discusses testing, a method for identifying hidden bugs in a system, whether it is fully or partially working.

- **Goal:** The aim of testing is to verify whether your solution performs as expected and to pinpoint specific areas where it fails. Testing can only occur once your solution has reached a working state, either fully or partially.
    

To test effectively, you need a clear understanding of what the solution is intended to do. This makes the advice from Chapter 3 – clearly defining your solution’s goals – crucial. Testing is far less useful if the expectations for your system are poorly defined.

- **Approach:** In testing, it's vital to be systematic. Ad-hoc testing without a specific strategy can only tell you that something is wrong without identifying the cause. Systematic testing helps you localize the issue and pinpoint exactly what is wrong.
    

There are two main approaches to testing:

1. **Top-down testing:** Testing the entire system to ensure it functions as a whole. This is most effective for identifying design flaws and confirming the system works together.
    
2. **Bottom-up testing:** Testing the individual parts of the solution first. This allows you to verify that each component functions correctly before checking the system as a whole.
    

**Advantages and Disadvantages of Top-Down and Bottom-Up Testing**

|**Top-Down**|**Bottom-Up**|
|---|---|
|Effective for finding design flaws.|Easy to apply in the early stages.|
|Can test the whole system even if incomplete.|Helps localize problems effectively.|
|Difficult to apply when the system is incomplete.|Requires simulation of the controlling parts.|
|Harder to locate bugs when they occur.|Doesn’t reveal design flaws until later.|
Ideally, you should combine both approaches. Start with a basic skeletal structure and test it with placeholders (bottom-up testing). Simultaneously, test the entire system to check that it functions as expected (top-down testing).

- **Testing individual parts:** If your solution is divided into reasonably independent pieces, testing each one individually becomes simpler. Tests that focus on individual components are called unit tests. Testing individual components can be tricky, as these parts often assume the rest of the system is present and functioning correctly.
    

For instance, when testing a component, you may need to simulate input data. In some cases, you might test different values of the input to ensure the component works correctly under all conditions, though this can be infeasible due to the large number of possibilities.

**FizzBuzz Example:**

For the FizzBuzz game, where numbers divisible by 3 are replaced with 'Fizz', by 5 with 'Buzz', and by both 3 and 5 with 'FizzBuzz', testing the subroutine can be done for the first 20 values. However, testing all possible values is unfeasible, so we use equivalence classes to group similar values and test one representative value from each class.

For FizzBuzz, equivalence classes could include:

- **Normal acceptable numbers** (e.g., 8) – Should return the number itself.
    
- **Fizzes** (e.g., 3) – Should return 'Fizz'.
    
- **Buzzes** (e.g., 10) – Should return 'Buzz'.
    
- **FizzBuzzes** (e.g., 30) – Should return 'FizzBuzz'.
    
- **Unacceptable numbers** (e.g., -10) – Should be rejected.
    
- **Non-numbers** (e.g., 'VII') – Should be rejected.
    
- **Boundary numbers** (e.g., 1 or 0) – Should be accepted or rejected accordingly.
    

By testing representative values from each equivalence class, you can verify that the subroutine behaves correctly.

- **Test Plan:** It's important to document all tests in a test plan. This plan should be clear and understandable, and it’s helpful to have a third party review and run the tests. They may uncover issues you missed.
    

**DEBUGGING**

Inevitably, you will encounter errors during testing or real-world use of your solution. These errors can be puzzling, but there's no need to panic. Debugging is a systematic process of identifying and fixing the error. You can follow several strategies to find the problem.

- **Be ruthless with hunches:** If you have a hunch about the cause of the error, test it. If it’s wrong, discard it immediately.
    
- **Respect Occam’s Razor:** When considering possible causes, choose the simplest explanation that requires the fewest assumptions.
    
- **Divide and conquer:** If unsure where the problem lies, use the divide-and-conquer method to isolate the issue by testing smaller parts of the system and eliminating large sections at a time.
    
- **Change one thing at a time:** Apply one change at a time and test it. If it doesn’t work, undo the change and try a different approach.
    
- **Logging:** If your system behaves unexpectedly, add logging instructions to track what’s happening. Logs can help you see which instructions are executed and identify issues.
    
- **Tracing:** For complex problems, sometimes you need to go through each instruction manually, simulating the computer’s behavior to understand what’s going wrong. This can also be done using a debugger.
    
- **Explain the problem aloud:** If you're stuck, try explaining the problem aloud. Walking through the issue step by step often helps uncover a solution.
    


This approach will help ensure that your systems are robust, and your code is free of hidden bugs.