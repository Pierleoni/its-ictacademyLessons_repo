
# Introduzione
Per modellare accuratamente il mondo, vediamo l'esempio di [[Università 1]]: 
![[Università1.png|700x345]]

Questo diagramma delle classi è particolarmente inadeguato
1. I professori non possono essere studenti
2. I professori e studenti hanno attributi simili 
Tutto questo è artificioso perché sono casi particolari della stessa natura, cioè che fanno parte di un'unica classe: `Persona`.
Un altra cosa: questo diagramma ci dice che non possono esserci due prof con lo stesso codice fiscale cosi come due studenti con lo stesso codice fiscale ma ciò permette che un prof abbiamo il codice fiscale uguale a uno studente.
Per migliorare il diagramma si può creare una classe `Persona`, cambiare i nomi della classi da `Facoltà` a Corsi di Laurea (`CdL`), da `Corso`  a `Insegnamento`.
Nella classe `Persona` metto attributo `cf:CodiceFiscale` e un attributo `tipo:(prof, stud)` cosi si deve mettere un associazione `studente_iscritto` che va a `CdL` e si mette un vincolo di molteplicità `0..1` accanto a `CdL`: questo permette che un professore possa iscriversi a un corso di laurea. 
Per la legge è giusto, quindi questo diagramma com'era fatto prima era sbagliato perché per legge un professore può iscriversi a un corso di laurea. Tuttavia questo può essere un problema all'interno del sistema, quindi devo trovare un modo per evitare questo scenario. 
## Il concetto di generalizzazione
Quindi in molte situazioni voglio rappresentare il fatto che tra due classi sussista una relazione di sotto-insieme. 
I diagrammi delle classi permettono di definire il concetto di **relazione [[#^is-aDef|is-a]] tra le classi.** 

![[concetto di generalizzazione.png|340x300]]

Guardiamo questo esempio: mettendo questa freccia stiamo imponendo una relazione **is-a("è anche un"):** 
==**ogni**  istanza della classe sotto-classe (`Studente`) è (concettualmente!) **anche** un'istanza della classe super-classe(`Persona`).==    ^is-aDef


Detta in altri termini: un'istanza della classe `Studente` è anch'essa stessa un' istanza della classe `Persona`.

Quindi tutte le istanze della sottoclasse `Studente` sono anch'esse istanze della super-classe(**[[#^is-aDef|is-a]]**) `Persona`. 
Come si può intuire nel concetto di generalizzazione o relazione [[#^is-aDef|is-a]] è presente anche il concetto di ereditarietà: 
==tutti gli attributi della sottoclasse (`Studente`) ereditano gli attributi della super-classe(`Persona`).== 
Ovviamente ciò non vale per l'inverso: 
==cioè non tutte le istanze di `Persona` devono per forza essere anche istanze di `Studente`== .   ^ereditarieta

Infatti poniamoci la seguente domanda: gli studenti hanno anche il numero di matricola e tutte le persone hanno numero di matricola? No

### Classi più specifiche di un oggetto
![[Classi più specifiche di un oggetto.png|361x289]]

In questo diagramma vediamo un esempio di **gerarchia tra classi** tramite generalizzazione.

- `Persona` è la **superclasse** con attributi comuni (es. `nome`, `genere`)
- `Studente` e `Lavoratore` sono **sottoclassi** di `Persona` e ne ereditano le caratteristiche
- `anna` è un **oggetto (istanza)** che può appartenere a una o più di queste classi``

Possiamo quindi descrivere **quattro possibili scenari** per l'oggetto `anna`:

1. `anna` **non è né** studentessa né lavoratrice, ma è comunque una `Persona`
2. `anna` **è sia** studentessa **che** lavoratrice, quindi è anche una `Persona`
3. `anna` **è solo** lavoratrice, quindi è anche una `Persona`
4. `anna` **è solo** studentessa, quindi è anche una `Persona`


È necessario per il sistema che Anna è una lavoratrice, una studentessa e persona? No, perché Il sistema può dedurre che anna è una persona: 
==le classi più specifiche (le più specifiche perché sono quelle più in basso nell'albero **[[#^is-aDef|is-a]]**) sono collegate tramite generalizzazione alla classe padre (o super-classe) `Persona`, di conseguenza se anna è una studentessa o una lavoratrice il sistema può dedure che anna è anche una persona.== 

> [!abstract]  [[#^ereditarieta|Anna è una studentessa, tutti gli studenti sono una persona, quindi Anna è anche una persona]].  ^sillogismoAristotelico
> 

##### Cosa sono le classi specifiche
Le classi più specifiche(anche dette _"foglie"_ nell'albero [[#^is-aDef|`is-a`]]): 
==sono `Studente` e `Lavoratore`, e rappresentano le "nature" più concrete di Anna. La classe `Persona` invece è più generale e viene ereditata.==
In altre parole le sottoclassi (o classi figlie) `Studente` e `Lavoratore`, rappresentano i suoi **tipi più concreti.**


### Relazione is-a tra classi: ereditarietà 
Tornando al meccanismo dell'[[#^ereditarieta|ereditarietà]]:
fino ad ora abbiamo implicitamente assunto  che classi diverse non hanno istanze in comune, tuttavia in molte situazioni torna utile rappresentare il fatto che tra due classi sussista una relazione di sottoinsieme.
Infatti i diagrammi delle classi permettono di definire il concetto di **[[#^is-aDef|relazione `is-a`]]** .

> [!caution] In presenza di relazioni [[#^is-aDef|is-a]], vige il [[#^ereditarieta|meccanismo dell'ereditarietà]]: per assimilare meglio questo concetto bisogna ricordare il **[[Ereditarietà delle classi#^sillogismoAristotelico-Def|sillogismo aristotelico]]** 
> 

Prendiamo ad esempio un sistema in cui di tutte le persone di interesse vogliamo rappresentare nome, cognome, genere e città di nascita; mentre di tutti gli studenti vogliamo rappresentare il numero di matricola e l'eventuale tutor.
Ora, può esistere una `Persona` senza città di nascita o con due nomi, come può esistere uno `Studente` con due nomi o senza e con due citta di nascita? No.
Quindi in questo caso  la sottoclasse `Studente` eredità gli attributi, le associazioni e i vincoli di molteplicità della classe `Persona`. 
![[Relazioni is-a tra classi_ereditarietà.png]]
Quindi, in questo caso studente eredita  un nome, un genere, una città di nascità, un genere e acquisisce un numero di matricola e si associa a un tutor tramite il link dell'associazione `tutor_stud`.
Questo perché tutti gli studenti sono persone ([[#^is-aDef|relazione is-a]]):
Di conseguenza, ==di tutti gli studenti  si sta rappresentando anche nome, genere e città di nascita (con le loro molteplicità `1..1`)==.

#### Relazioni tra classi: ereditarietà delle relazioni is-a a più livelli
Ovviamente possiamo avere **relazioni [[#^is-aDef|`is-a`]] a più livelli: la transitività**
Prendiamo ad esempio il diagramma con la relazione [[#^is-aDef|is-a]], `Persona`→`Studente`:
abbiamo detto che 
- di tutte le persone di interesse volgiamo rappresentare nome, cognome, genere e città di nascita.
- di tutti gli studenti volgiamo rappresentare la matricola e l'eventuale tutor.
Adesso aggiungiamo un ulteriore sottoclasse `StudenteStraniero`:
- di tutti gli studenti stranieri volgiamo rappresentare la nazione di provenienza.
![[transitività.png]]
In questo esempio abbiamo una relazione is-a a più livelli:
**Primo livello:**
- Tutti gli studenti sono persone (relazione [[#^is-aDef|`is-a`]]):
	- di conseguenza, di tutti gli studenti stiamo rappresentando anche nome, genere e città di nascita (con le loro molteplicità)
	- inoltre si associano alla classe `Tutor` tramite il link della associazione `tutor_stud`
**Secondo livello:**
- Tutti gli studenti stranieri sono studenti (relazione [[#^is-aDef|is-a]]): 
	- di conseguenza, degli studenti stranieri stiamo rappresentando anche nome, genere di matricola, città di nascita e la possibilità di avere o meno un tutor(quindi stiamo rappresentando le loro molteplicità per la città di nascita(`1..1`) e per i tutor(`0..1`))
	- Inoltre si associano anche alla classe `Nazione` tramite il link dell'associazione `naz_stud`. 

### Generalizzazione 
Tornando al concetto di generalizzazione tra le classi:
I diagrammi delle classi UML offrono un costrutto più complesso della relazione [[#^is-aDef|is-a]]: il costrutto della generalizzazione
- **==Permette di definire che le istanze di una classe possono essere istanze di più classi figlie secondo uno stesso criterio concettuale==**

![[Generalizzazione_1.png]]
Il significato di questa immagine è:
• Studente **[[#^is-aDef|is-a]](è anche un)** Persona
• Lavoratore **[[#^is-aDef|is-a]](è anche un)** Persona
Il criterio secondo il quale le Persone sono considerate studenti e/o lavoratori è lo
stesso: quello dell’enfasi concettuale chiamata “occupazione”
Quindi è ancora possibile per un oggetto essere istanza sia di `Studente` che di `Lavoratore`.


Inoltre la stessa classe può essere superclasse di generalizzazioni distinte(cioè con criteri diversi).
![[generalizzazioni distinte.png|396x277]]
Il significato dell'immagine è la seguente:
- Secondo il criterio del genere, le Persone sono considerate uomini e/o donne
- Secondo il criterio (indipendente!) dell’occupazione, le persone sono considerate studenti e/o lavoratori

Per capire meglio questo concetto guardiamo questo diagramma e poniamoci le seguenti domande,  
1. Una istanza di persona può essere un'istanza di un uomo? Sì
    
2.  Una istanza di persona può essere un'istanza di una donna? Sì
    
3.  Una istanza di persona può essere un'istanza sia di uomo che di donna? Sì
    
4.  Una istanza di persona può essere un'istanza di studente? Sì
    
5.  Una istanza di persona può essere un'istanza di lavoratore? Sì
    
6.  Una istanza di persona può essere un'istanza di uomo e studente? Sì
    
7.  Una istanza di persona può essere un'istanza di donna e studente? Sì
    
8.  Una istanza di persona può essere un'istanza di uomo e lavoratore? Sì
    
9. Una istanza di persona può essere un'istanza di donna e lavoratore? Sì
    
10. Una istanza di persona può essere un'istanza di uomo, di studente e di lavoratore? Sì
    
11. Una istanza di persona può essere un'istanza di donna, di studente e di lavoratore? Sì
    
12.  Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di studente e di lavoratore? Sì
    
13. Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di studente ma non di lavoratore? Sì
    
14. Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di lavoratore ma non di studente? Sì
    
15. Una istanza di persona può essere solo lavoratore, senza essere né uomo, né donna, né studente? Sì
    
16. Una istanza di persona può non essere né uomo, né donna, né studente, né lavoratore? Sì



> [!abstract]- **Visualizzazione in codice binario di queste domande** 
>| #   | Uomo | Donna | Studente | Lavoratore | Descrizione breve                  | Domanda                                                                                                                                       |
| --- | ---- | ----- | -------- | ---------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 1    | 0     | 0        | 0          | Solo uomo                          | 1. Una istanza di persona può essere un'istanza di un uomo? **Sì**                                                                            |
| 2   | 0    | 1     | 0        | 0          | Solo donna                         | 2. Una istanza di persona può essere un'istanza di una donna? **Sì**                                                                          |
| 3   | 1    | 1     | 0        | 0          | Uomo e donna                       | 3. Una istanza di persona può essere un'istanza sia di uomo che di donna? **Sì**                                                              |
| 4   | 0    | 0     | 1        | 0          | Solo studente                      | 4. Una istanza di persona può essere un'istanza di studente? **Sì**                                                                           |
| 5   | 0    | 0     | 0        | 1          | Solo lavoratore                    | 5. Una istanza di persona può essere un'istanza di lavoratore? **Sì**                                                                         |
| 6   | 1    | 0     | 1        | 0          | Uomo e studente                    | 6. Una istanza di persona può essere un'istanza di uomo e studente? **Sì**                                                                    |
| 7   | 0    | 1     | 1        | 0          | Donna e studente                   | 7. Una istanza di persona può essere un'istanza di donna e studente? **Sì**                                                                   |
| 8   | 1    | 0     | 0        | 1          | Uomo e lavoratore                  | 8. Una istanza di persona può essere un'istanza di uomo e lavoratore? **Sì**                                                                  |
| 9   | 0    | 1     | 0        | 1          | Donna e lavoratore                 | 9. Una istanza di persona può essere un'istanza di donna e lavoratore? **Sì**                                                                 |
| 10  | 1    | 0     | 1        | 1          | Uomo, studente e lavoratore        | 10. Una istanza di persona può essere un'istanza di uomo, di studente e di lavoratore? **Sì**                                                 |
| 11  | 0    | 1     | 1        | 1          | Donna, studente e lavoratore       | 11. Una istanza di persona può essere un'istanza di donna, di studente e di lavoratore? **Sì**                                                |
| 12  | 1    | 1     | 1        | 1          | Uomo, donna, studente e lavoratore | 12. Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di studente e di lavoratore? **Sì**      |
| 13  | 1    | 1     | 1        | 0          | Uomo, donna e studente             | 13. Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di studente ma non di lavoratore? **Sì** |
| 14  | 1    | 1     | 0        | 1          | Uomo, donna e lavoratore           | 14. Una istanza di persona può essere sia un'istanza di donna che di uomo ed essere anche un'istanza di lavoratore ma non di studente? **Sì** |
| 15  | 0    | 0     | 0        | 1          | Solo lavoratore                    | 15. Una istanza di persona può essere solo lavoratore, senza essere né uomo, né donna, né studente? **Sì**                                    |
| 16  | 0    | 0     | 0        | 0          | Nessuna categoria                  | 16. Una istanza di persona può non essere né uomo, né donna, né studente, né lavoratore? **Sì**                                               |

Quindi,  in questo diagramma si sta modellando $2^4=16$ combinazioni.
### Vincoli sulle generalizzazioni: `{disjoint}` e `{complete}` 
Il costrutto della generalizzazione delle classi  li posso vincolare:
spesso, nell'ottica di modellare accuratamente i requisiti si mettono dei vincoli sulle generalizzazioni.
il primo di questi vincoli è 
1. `{disjoint}`: 
	==significa che ho disgiunte le sottoclassi fra loro, in questo caso ho disgiunto la sottoclasse `Uomo` e `Donna` e sto dicendo che non hanno nulla in comune.== 

![[{disjoint}.png]]

Quindi il significato di questa immagine è:
- ==la generalizzazione sul genere è disgiunta; una istanza di `Uomo` non può essere anche istanza di `Donna`.== 
  In altre parole, ==una persona può avere solo ed esclusivamente un genere tra uomo o donna==
- La generalizzazione sull'occupazione rimane non disgiunta: quindi una istanza di `Studente` può essere anche istanza di `Lavoratore`.
- Quindi alla domanda se un istanza di `Persona` può essere sia un istanza di `Uomo` che un istanza di `Donna`? **Non più.**
  Una istanza di Persona può essere sia istanza di `Uomo` che di `Studente`? Si
  Una istanza di `Persona` può essere istanza né di `Uomo` che di `Donna`? Si
  
> [!caution] **`{disjoint}` impone che ogni istanza di `Persona` possa appartenere **al massimo** a una sola tra `Uomo` e `Donna`, ma può anche non appartenere a nessuna**.
> 

2. `{complete}`: 
   ==Le due sottoclassi rappresentano l'insieme completo delle istanze della superclasse. 
   Se, ad esempio, prendo le istanze di `Uomo` e `Donna`, queste coprono tutte le istanze della classe `Persona`. Quindi, ogni persona deve appartenere ad almeno una di queste due sottoclassi. Una persona può avere un solo genere oppure entrambi, se non è presente il vincolo `{disjoint}`.== 
![[{complete}.png]]
Il significato dell'immagine è la seguente: 
- La generalizzazione sul genere è completa: ogni istanza di `Persona` deve essere anche istanza di almeno una sottoclasse tra `Uomo` e `Donna` e/o di entrambi. 
- La generalizzazione sull’occupazione non è completa: possono esistere istanze di `Persona` che non sono né istanze di `Studente` né istanze di `Lavoratore`.

Nulla vieta che posso mettere entrambi questi vincoli:
mettendoli insieme sto dicendo facendo una partizione:
==un partizione è un insieme di insiemi sia disgiunti che completi.==
In questo modo si hanno solo 4 nature per ogni genere e occupazione.

![[{disjoint,complete}.png]]
Il significato di questa immagine è il seguente:
- ogni istanza di `Persona` deve essere anche istanza di esattamente una sottoclasse tra `Uomo` e `Donna`.
-  ogni istanza di `Persona` deve essere anche istanza di esattamente una sottoclasse tra `Studente` e `Lavoratore`
- Una istanza di Persona può essere sia istanza di Uomo che di Studente? Sì
  Una istanza di Persona può essere istanza né di Uomo né di Donna? **Non più**
  Una istanza di Persona può essere istanza sia di Uomo che di Donna? **Non più**
Questo perché: 
Abbiamo detto che con il vincolo **`{complete}`**:
> ==_tutte_ le istanze della superclasse devono appartenere a **una o più** delle sottoclassi coinvolte.==

Mentre con **`{disjoint}`**:
> ==le sottoclassi **non si sovrappongono**, quindi un'istanza può appartenere a **una sola** sottoclasse tra quelle o a nessuna.== 

Quando questi due vincoli si combinano (`{disjoint, complete}`), il significato diventa:
> ==tutte le istanze della superclasse devono appartenere a **una sola** delle sottoclassi coinvolte.==

Nel nostro esempio:

- ==Per la generalizzazione su **genere**, ogni istanza di `Persona` deve essere **o `Uomo` o `Donna`**, ma **non entrambe**==.
    
- ==Lo stesso vale per la generalizzazione su **occupazione**: ogni `Persona` deve essere **o `Studente` o `Lavoratore`**, ma **non entrambe**==.

Per capire meglio questi vincoli prendiamo ad esempio i diagrammi di Ven: 
Come possiamo vedere da questa immagine guardandola da sinistra verso destra;
1. nella prima immagine non si hanno vincoli sulla generalizzazione quindi tutte le istanze della classe padre C appartengono anche alle classi figlie A e B che a loro volta si sovrappongono tra loro, questo perché A [[#^is-aDef|is-a]] C e B [[#^is-aDef|is-a]] C.
2. Nella seconda immagine: viene applicato il vincolo `{disjoint}`, infatti come possiamo vedere le sottoclassi A e B sono disgiunte tra loro andando a formare due diagrammi separati ma comunque contenuti in C, questo perché ogni istanza della superclasse può appartenere a una sola istanza della sottoclasse o nessuna
3. Nella terza immagine: viene applicato il vincolo `{complete}` difatti A e B adesso si sovrappongono tra loro andando ad a occupare e completare il diagramma C, questo perché ogni istanza **deve appartenere ad almeno una** delle sottoclassi.
4. Nella quarta immagine: viene applicato il vincolo `{disjoint,complete}`, infatti adesso sia A che B si uniscono ma rimangono comunque separati tra loro.

![[diagramma di Ven.png]]

> [!example] **In Sintesi: Differenza tra `{disjoint}`, `{complete}`, `{disjoint,complete}`**
> 
> **1. `{disjoint}` **(solo disgiunzione)**:
>
>- **Ogni istanza può appartenere a una sola sottoclasse tra quelle indicate.**
 >   
>-  ==**Non obbliga** che appartenga ad **almeno una**.==
  >  
>-  **Limitante**: ==potresti avere istanze di `Persona` che non sono né `Uomo` né `Donna`==.
 >   
>
>2. **`{complete}` **(solo completezza)**:
>
>- ==Ogni istanza **deve appartenere ad almeno una** delle sottoclassi.==
>    
>-  ==Può appartenere anche **a più di una** contemporaneamente.==
>    
>-  **Flessibile**, ==ma può **complicare il modello** con combinazioni inaspettate o incoerenti (es. `Uomo` e `Donna` insieme, se non vuoi che sia possibile).==
  >  
>
> 3.`{disjoint, complete}` **(insieme)**:
>
>- ==Ogni istanza **deve appartenere ad una sola** delle sottoclassi coinvolte.==
  >  
>-  ==Nessuna sovrapposizione **e**  nessuna istanza "orfana" (cioè senza sottoclasse).==
 >   
>-  ==È il vincolo più **rigido**, ma anche **chiaro e sicuro** nei casi in cui le categorie siano **mutuamente esclusive ed esaustive** (es. `Uomo`/`Donna` in un certo contesto, `Studente`/`Lavoratore`).==

