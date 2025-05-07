Iniziando con un totale corrente, Gauss cominciò ad aggiungere numeri uno alla volta (1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10 e così via). Tutti gli studenti, tranne Gauss, seguirono questo approccio. Lui notò un modello nel problema: 1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101 e così via, fino a 50 + 51 = 101. Questo modello mostrava che quei 100 numeri potevano essere raggruppati in 50 coppie, ognuna delle quali somma 101. Invece di eseguire 100 somme, Gauss doveva solo eseguire una moltiplicazione (50 × 101) per ottenere lo stesso risultato.

**Figura 6.2 Sezione trasversale di una trappola**  
Muro di scarico  
Ventilazione  
Flusso d'acqua  
Flusso d'acqua  
Flusso d'acqua

L'idea del matematico è forse la più vicina all'idea di un informatico. Se un programmatore dovesse codificare queste due soluzioni per un computer, apparirebbero più o meno così:

**Soluzione ovvia:**

- Impostare il totale = 0;
    
- Per ogni numero, n, compreso tra 1 e 100:
    
    - Impostare il totale = totale + n.
        

**Soluzione più elegante di Gauss:**

- Impostare il totale = 50 × 101.
    

La soluzione di Gauss ottiene lo stesso risultato della soluzione ovvia, ma lo fa usando meno spazio (una sola variabile anziché due) e meno tempo (un solo passaggio invece di circa 100). In termini di complessità, se dovessi scrivere versioni generiche di entrambe le soluzioni per calcolare la somma dei primi N numeri, la soluzione ovvia sarebbe O(N), mentre la soluzione di Gauss sarebbe molto più efficiente, O(1).

**Semplice può essere più difficile di complesso:**  
Devi lavorare duramente per semplificare il tuo pensiero fino a renderlo semplice. (Jobs, 1998)

**VALUTARE UNA SOLUZIONE**  
Potrebbe sembrare paradossale, ma è più difficile essere semplici che complicati. Trovare soluzioni eleganti richiede tempo e sforzo. Richiede di arrivare all'essenza del problema e vedere i modelli al suo interno. Richiede anche di applicare un pensiero fuori dagli schemi. Ma è uno sforzo che può essere molto gratificante, perché i vantaggi di un risultato elegante possono essere enormi.

Lo svantaggio principale di una soluzione non ovvia è proprio questo: non è ovvia. Se qualcun altro dovesse lavorare sulla tua soluzione, avrà bisogno di capire come funziona. Chiunque guardi la soluzione ovvia qui sopra può facilmente capire che sta sommando i numeri da 1 a 100. Tuttavia, guardando la soluzione elegante di Gauss in isolamento, non è immediatamente chiaro cosa stia cercando di ottenere. L'autore potrebbe capirla, ma gli altri? Pertanto, dovresti sempre assicurarti che le parti non ovvie della tua soluzione siano accompagnate da spiegazioni chiare.

Quando parlo di altre persone che devono capire la tua soluzione, parlo anche di te! Potresti capire le complessità oggi, ma le capirai ancora dopo aver lasciato la tua soluzione e ripreso il lavoro su di essa tra alcune settimane o mesi? C'è una buona probabilità che tu abbia dimenticato come funziona. Fai un favore a te stesso: scrivi sempre spiegazioni chiare su come funziona la tua soluzione, soprattutto le parti complesse.

Quando trovi soluzioni eleganti, fai attenzione alla furbizia per la propria soddisfazione. Sii sempre pronto a giustificare perché non stai prendendo l'approccio ovvio. Se non ci sono vantaggi tangibili nel tuo modo non ovvio, potresti rendere la soluzione più complessa senza motivo.

**È USABILE?**  
Alla fine, gli utenti della tua soluzione saranno persone. La tua soluzione deve quindi adattarsi agli esseri umani e ai loro modi particolari. In altre parole, deve essere usabile e dovrebbe offrire agli utenti un'esperienza positiva.

Criteri come correttezza, efficienza ed eleganza descrivono una soluzione in termini propri. Tuttavia, l'usabilità misura quanto sia facile per le persone usare una soluzione per raggiungere i propri obiettivi. Gli esseri umani portano con sé altri fattori. Non siamo macchine, abbiamo desideri ed emozioni. Commettiamo errori e abbiamo pazienza limitata. Le persone vogliono soluzioni facili da imparare, semplici da usare, che perdonano i nostri errori, e meno fatica per noi significa meglio.

L'usabilità formalizza questi desideri in vari componenti che misurano quanto sia facile e soddisfacente utilizzare una soluzione (Nielsen, 2012). Fortunatamente, nonostante coinvolga gli esseri umani, questi componenti sono in qualche modo misurabili. Sono:

- **Imparabilità:** quanto è facile per gli utenti compiere le attività di base la prima volta che incontrano la soluzione?
    
- **Efficienza:** una volta che gli utenti hanno imparato la soluzione, quanto velocemente possono eseguire le attività?
    
- **Memorabilità:** quando gli utenti tornano alla soluzione dopo un periodo di non utilizzo, quanto facilmente possono riacquisire la competenza?
    
- **Errori:** quanti errori commettono gli utenti, quanto sono gravi e quanto facilmente possono recuperare da essi?
    
- **Soddisfazione:** quanto è piacevole usare il design?
    

**Test di usabilità:**  
La valutazione dell'usabilità riguarda in ultima analisi le reazioni delle persone reali. Alla fine, dovrai coinvolgere le persone nella valutazione. Questo avviene in parte tramite uno studio osservazionale. Persone rappresentative del tuo pubblico dovrebbero essere reclutate come soggetti di prova, che poi usano la soluzione per svolgere una serie di compiti predefiniti (vedi Tabella 6.2). Mentre il soggetto lavora, l'evaluator osserva il loro lavoro, notando dove sono riusciti e dove hanno avuto difficoltà.

**Tabella 6.2 Esempio di elenco di compiti di usabilità**

| N° Compito | Descrizione                                      |
| ---------- | ------------------------------------------------ |
| 1          | Accedere al sistema.                             |
| 2          | Aggiungere un indirizzo email al profilo utente. |
| 3          | Comprare un libro di cucina sotto i 10 £.        |
| 4          | Mostrare un elenco dei tuoi acquisti passati     |

---
# Traduzione in inglese
This passage provides a deep dive into key principles of **computational thinking**, such as evaluating solutions for correctness, efficiency, elegance, usability, and the trade-offs that come with making design choices. Let's break it down:

1. **The Obvious vs. Elegant Solution**:
    
    - The example of Gauss' elegant formula for summing integers highlights how, through recognizing patterns, one can solve a problem with fewer steps and less computational resources. Gauss' formula (50 x 101) is far more efficient (O(1) complexity) compared to the brute force method of adding the numbers one by one (O(N) complexity).
        
    - The main takeaway is that **elegance** can simplify problems, making solutions both space- and time-efficient, but it requires insight into the structure of the problem.
        
2. **Evaluating Solutions**:
    
    - In evaluating solutions, the focus is not only on correctness but on the **complexity** and **usability** of the approach.
        
    - **Correctness** is obvious—it simply means the solution works as expected.
        
    - The passage emphasizes **elegance** as an important factor. However, even elegant solutions must be clear and understandable, particularly for other developers or users interacting with the code. Non-obvious solutions need clear documentation to avoid confusion later.
        
3. **Usability**:
    
    - **Usability** is about making the solution user-friendly. Jakob Nielsen's **usability heuristics** provide guidelines to design solutions that are easy to learn, use efficiently, and forgiving of user mistakes.
        
    - It includes tasks such as making the solution **learnable**, ensuring **efficiency** for experienced users, providing mechanisms for error recovery, and making it **satisfying** for users.
        
4. **Trade-offs in Problem Solving**:
    
    - A solution often involves **trade-offs**, such as balancing **time efficiency** and **space efficiency**. A good example is **image compression**, where data is optimized to save space, but the process of decompressing the data becomes slower.
        
    - Similarly, solutions that are clever and complex might be harder to understand, and **flexibility** may reduce **usability**.
        
    - The key is knowing when and where to prioritize certain factors over others. For instance, in scenarios where data needs to be transmitted over a network, optimizing **storage space** (compression) might be more important than the extra time it takes to decode the data.
        
5. **Conclusion**:
    
    - Solutions to problems involve many factors, and these must be evaluated based on the goals of the solution. The important guiding question is **which aspect should you optimize?** Correctness, efficiency, elegance, usability, or perhaps a mix depending on the context of the problem at hand.
        

This passage provides a broad framework for thinking about how to solve problems effectively and efficiently, and how to make conscious choices in problem-solving that balance different needs and constraints.