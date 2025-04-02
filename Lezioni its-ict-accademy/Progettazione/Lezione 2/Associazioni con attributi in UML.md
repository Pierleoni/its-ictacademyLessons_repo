
# Introduzione
Come abbiamo detto sulla lezione [[Analisi dei requisiti mediante UML]], le associazioni descrivono relazioni tra classi. 
Tuttavia, in alcuni casi, la relazione stessa possiede proprietà specifiche che non appartengono alle singole classi coinvolte, ma alla loro **_istanza di collegamento_**. Per rappresentare questa situazione, si utilizza un’**associazione con attributo**: 
==un attributo legato direttamente al nesso tra le classi, anziché a una di esse.== 

## Associazioni con attributi
Consideriamo un sistema che gestisce gli esiti voti, in trentesimi, dei test superati dagli studenti di un corso.
Il corso è suddiviso in moduli e uno studente può superare il test di ogni modulo una sola volta.
![|523x141](https://i.imgur.com/zFS1lTS.jpeg)
Quindi abbiamo due classi:
- `Studente`
	- con l'attributo `nome` di tipo `Stringa`
- `Modulo`
	- con l'attributo `nome` di tipo `Stringa`
La relazione tra `Studente` e `Modulo` ha due  [[Vincoli di molteplicità sulle associazioni e sugli attributi#Semantica dei vincoli di molteplicità sui ruoli delle associazioni|vincoli di molteplicità ]] `0..*`, perché:
 - uno studente può superare più moduli 
 - i moduli possono essere passati più studenti. 
 Tuttavia come possiamo notare l'attributo `voto` non può essere associato né alla classe `Studente` é alla classe `Modulo`: poiché un voto non è una proprietà locale di uno studente, né di un modulo, ma è una proprietà del legame tra uno studente e un modulo, quindi è una **proprietà dell'[[Analisi dei requisiti mediante UML#^associationsDef|associazione]]**.  

Quindi il voto non è un attributo né della classe `Studente` perché:
l'attributo `voto` andrebbe a significare che tutti gli studenti hanno quel voto in comune 
né della classe `Modulo`, perché:
l'attributo `voto` andrebbe a significare che tutti i moduli hanno quell'unico voto.
Quindi:
il `voto` (insieme alla `data` del test) diventa un **attributo dell'associazione**, che chiamiamo `test_superato`.
![](https://i.imgur.com/53nyHiL.jpeg)

L'associazione `test_superato` viene modellata come una classe con attributi (`voto` e `data`).

> [!NOTE] **Da notare che ha la stessa forma della classe ma la prima lettera è minuscola**
>

Questa associazione è collegata a `Studente` e `Modulo` mediante una **linea tratteggiata,** ==indicando che non è una classe indipendente, ma un **oggetto che esiste solo all'interno della relazione.**== 
In altre parole non è più la classe `Studente` o la classe `Modulo` ad avere l'attributo `voto`, ma è il link stesso ad avere questo attributo.

### L'importanza dell'unicità dei link 
Come abbiamo visto nella [[Analisi dei requisiti mediante UML|prima lezione]] un **[[Analisi dei requisiti mediante UML#Cosa sono i link?|link]],** in UML, **[[Analisi dei requisiti mediante UML#Perché i link non hanno un identificatore?|è un istanza concreta di un associazione tra oggetti]].**
Questo significa che un link è **==identificato esclusivamente dagli oggetti che collega:==**
I link sono identificati dagli oggetti che partecipano alla relazione, pertanto ==**non possono esistere due link distinti tra la stessa coppia di oggetti**, indipendentemente dagli attributi associati.==

![](https://i.imgur.com/0UiIX06.jpeg)

Da questa immagine possiamo notare che:
l'oggetto della `anna:Studente` della classe `Persona` ha due link con l'oggetto `py:Modulo`. 
Questo **non è ammesso** perché, secondo UML, un link in un'associazione (come quella tra `Studente` e `Modulo`) binaria ==è determinato solo dagli **oggetti coinvolti** e non dagli attributi dell'associazione==.
L'errore nel modello si manifesta con la seguente rappresentazione:
```UML
(Anna, Python, 27, 3/5/2023)  
(Anna, Python, 25, 7/9/2022)  
```
Poiché in UML un'associazione binaria è definita da **due soli elementi** (Studente e Modulo), questi esempi rappresentano una **quadrupla** (Studente, Modulo, Voto, Data), violando il principio che un link sia univoco per una coppia di oggetti.
In altre parole:
Nell'immagine vediamo un **modello UML con un'associazione con attributi**, dove il legame tra `Studente` e `Modulo` è rappresentato dall'entità `test_superato`. Quest'ultima contiene due attributi:

- `voto` (punteggio ottenuto dallo studente)
    
- `data` (data dell'esame).
Nella parte [[Analisi dei requisiti mediante UML#^exLevel|estensionale]] (cioè l'implementazione concreta con istanze degli oggetti), vediamo che lo **stesso studente (`anna:Studente`) ha superato lo stesso modulo (`py:Modulo`) due volte con voti e date diverse**.
UML definisce un'associazione come un **collegamento tra due oggetti,** quindi un **==link è identificato solamente dagli oggetti coinvolti, non dagli attributi dell'associazione==:**
- Ciò significa che non posso avere due istanze di `test_superato` che collegano gli stessi due oggetti (`anna` e `py`), anche se i valori degli attributi sono diversi.
    
- L'associazione `test_superato` esiste **una sola volta** per ogni coppia (`Studente`, `Modulo`).

> [!example]- Sintetizzando
> | `Studente` | `Modulo` | `voto` | `data`   | Ammesso                                |
| ---------- | -------- | ------ | -------- | -------------------------------------- |
| Anna       | Python   | 27     | 3/5/2023 | Si!                                    |
| Anna       | Python   | 25     | 7/9/2022 | No! <br>((duplicato dello stesso link) |
> 
> 
> 

Questo problema nasce perché l'associazione **non è modellata come un'entità autonoma**. Per consentire che uno studente possa superare più volte lo stesso modulo, dovremmo ridefinire il modello e introdurre una nuova classe, ad esempio `EsameSostenuto`, che può avere attributi come `voto`, `data_esame` e magari un attributo `id` che deve essere univoco. 
Questa classe ci permette di gestire più tentativi (esattamente come per l'esempio [[Analisi dei requisiti mediante UML#Esempio Pratico Gestione delle Prenotazioni in un Albergo|della gestione delle prenotazioni in un albergo]]) al che possiamo avere più istanze di `Esame` per la stessa coppia (`Studente`, `Modulo`).


> [!example] **In conclusione**
> In UML, un link in un'associazione binaria è **identificato solo dagli oggetti coinvolti**. Se vogliamo registrare più informazioni su ogni connessione, dobbiamo trattarla come un'entità autonoma, introducendo una classe separata (ad esempio: `EsameSostenuto`).  
>Questo ci permette di gestire più tentativi senza violare le regole dell'unicità dei link.


### Le association class
In UML, un'associazione con attributi è anche chiamata **association class,** in quanto può essere a sua volta terminale di ulteriori associazioni.
![](https://i.imgur.com/tZw191t.png)

In questa immagine possiamo notare che: 
1. **[[Analisi dei requisiti mediante UML#^inLevel|Livello Intensionale:]]:**
   La classe `Studente` e la classe `Modulo` sono collegati dalla association class `test_superato`, che ha due attributi:
   - `voto`: il punteggio ottenuto
   - `data`: data dell'esame
L'association class a sua volta è collegata, tramite all'associazione `docente_test`, alla classe `Docente`, che indica chi ha somministrato l'esame.

> [!abstract]- **Vincoli nel livello intensionale**
>Nel livello intensionale dell'immagine (parte superiore), vediamo:
>
>1. **Molteplicità dell'associazione `test_superato`**
  >  
 >   - `0..*` tra `Studente` e `test_superato`: uno studente può sostenere più test.
 >       
 >   - `0..*` tra `Modulo` e `test_superato`: un modulo può essere superato più volte.
  >      
>2. **Associazione con `Docente`** (`docente_test`)
 >   
>    - `1..*` su `Docente`: ogni `test_superato` è associato almeno a un docente.
>        
 >   - `0..*` su `test_superato`: un docente può supervisionare più esami.
 >       
>3. **Problema dell'unicità del link**
 >   
  >  - UML **non consente** due link distinti tra gli stessi oggetti (`Studente` e `Modulo`), anche se gli attributi dell'associazione sono diversi.
  >      
  >  - Questo perché UML identifica un link solo in base agli **oggetti coinvolti**, e non in base agli attributi dell'associazione.
  >      
>
>> [!deep] **Conseguenze di questi vincoli** 
> >- Nel livello estensionale (parte inferiore), `anna:Studente` e `py:Modulo` sono collegati due volte da `test_superato`, ma UML li considera un solo link → **errore concettuale!**
>>    
>>- L'introduzione della relazione con `Docente` (`docente_test`) non risolve il problema, perché l’associazione tra `Studente` e `Modulo` resta comunque **binaria** e identificata solo dai due oggetti coinvolti.
> 
> Come possiamo vedere nel livello intensionale del diagramma, i vincoli di molteplicità non sono più direttamente tra `Studente` e `Modulo`, ma tra `Studente` e l'associazione `test_superato`, e tra `Modulo` e `test_superato`.
>
 >**Cosa significa questo?**
>
>- `0..*` accanto a `Studente` → uno **studente** può avere **più** associazioni `test_superato` (può sostenere più test).
  >  
>- `0..*` accanto a `Modulo` → un **modulo** può essere associato a **più** `test_superato` (può essere superato da più studenti).
  >  
>- Quindi, **non c’è più un’associazione diretta tra `Studente` e `Modulo`**, ma il legame avviene attraverso `test_superato`.
  >  
 >**Perché è importante?**
>
>- Se l'associazione fosse **diretta** tra `Studente` e `Modulo` con una molteplicità `0..*`, avremmo **solo un link per coppia (`Studente`, `Modulo`)**, e non potremmo registrare più tentativi di esame.
>    
>- Invece, con l'associazione `test_superato`, ogni tentativo è un'istanza separata, permettendo di gestire più esami per lo stesso studente e lo stesso modulo.
  >  
 >In altre parole, il **target** della molteplicità è ora `test_superato`, che funge da entità intermediaria tra `Studente` e `Modulo`


2. **[[Analisi dei requisiti mediante UML#^exLevel|Livello estensionale]]:**
    - vediamo che `anna:Studente` ha sostenuto l’esame di `py:Modulo` due volte, con due voti e date diverse.
    
	- **Problema**: UML identifica i link solo dagli oggetti che collega, quindi entrambi i `test_superato` sono considerati lo stesso link.
    
	- Questo è **"Non Ammesso"** in UML, perché i link devono essere univoci.
Anche qui il problema nasce dal fatto che `test_superato` è un'associazione con attributi, ma non è trattata come una vera classe. 
Quindi per permettere più tentativi dello stesso esame:
- **Trasformiamo `test_superato` in una vera classe (`EsameSostenuto`)**, separandola dall'associazione diretta tra `Studente` e `Modulo`.  
-  Questo permette di creare più istanze di `EsameSostenuto`, ognuna con attributi unici (`voto`, `data`, `docente`).  
- Così, ogni tentativo d'esame diventa un oggetto distinto e possiamo gestire più tentativi senza violare le regole UML.

