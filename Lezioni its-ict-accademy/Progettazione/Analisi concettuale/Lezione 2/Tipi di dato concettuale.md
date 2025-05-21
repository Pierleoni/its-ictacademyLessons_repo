# Introduzione
Finora abbiamo usati i tipi di dato  per definire ogni tipo di attributo, di classe e di associazione.
In analisi bisogna ricordare che non si effettuano scelte tecnologiche(come ad esempio sul linguaggio di programmazione), quindi si preferisce utilizzare tipi di dato concettuali, come:
- `Stringa`
    
- `Intero`
    
- `Booleano`
    
- `Data`
    
- `Ora`
    
- `DataOra`


### **Cosa si intende per tipo di dato concettuale?**
Prendiamo ad esempio il **tipo di dato "Data":**
- Esso **rappresenta il concetto di data (ad esempio: 2/05/2025),** 
- ==Definisce **un istante di tempo**, ma **non specifica il formato di memorizzazione o di visualizzazione** (che dipenderà dalla tecnologia utilizzata).==
Tuttavia, a volte abbiamo bisogno di rappresentare i dati in modo più accurato, introducendo dei **tipi di dato specializzati**.

## Tipi di dato specializzati
Esaminiamo un caso pratico.
Riprendendo l'esempio fatto sulla lezione sull'[[Associazioni con attributi in UML|associazioni con attributi in UML]]: consideriamo un sistema che gestisce gli esiti voti, in trentesimi, dei test superati dagli studenti di un corso.
Il corso è suddiviso in moduli e uno studente può superare il test di ogni modulo una sola volta:
![](https://i.imgur.com/E6e5V9v.png)
Questo diagramma è corretto, ma presenta un piccolo problema: **il valore `-5` nell'attributo `voto` di `test_superato` nel livello estensionale**.

- Nella realtà, un voto negativo **non esiste** (o, quantomeno, non ha senso in un contesto accademico).
    
- Tuttavia, nel **livello intensionale**, il tipo di `voto` è semplicemente un `Intero`, quindi il valore `-5` **sarebbe comunque lecito nel modello UML**.
    

Ora, il sistema deve rispettare queste regole:

1. I voti sono **espressi in trentesimi**.
    
2. Il punteggio minimo per superare un test è **18**.
    
3. Il massimo punteggio ottenibile è **30**.
    

Quindi, per **evitare l’inserimento di voti non validi**, dobbiamo **specializzare il tipo di dato** di `voto`, definendolo con un **range valido**.
![](https://i.imgur.com/MEnDwEU.png)
Ora che si è andato a definire il range `18..30` per `voto` nel [[Analisi dei requisiti mediante UML#^inLevel|livello intensionale]], il valore `-5` **non è più lecito nel modello UML**.

> [!example] **Altri esempi di specializzazione dei tipi di dato**
>
>- **Numero reale tra 0 e 1:**
  >  
  >  - Tipo di dato → `Reale 0..1`
  >      
  >  - Esempio: `0.45` è valido, mentre `1.5` no.
  >    
>  
>- **Stringa con esattamente 4 caratteri alfabetici maiuscoli:**
  >  
 >   - Tipo di dato → `Stringa[4]`
  >      
  >  - Esempi validi: `"ABCD"`, `"XZYT"`
 >       
> - Esempi non validi: `"abc"` (solo 3 caratteri), `"ABCDE"` (5 caratteri)
>  
>      
>- **Codice Fiscale italiano (16 caratteri alfanumerici):**
  >  
 >   - Tipo di dato → `Stringa[16]`
 >       
>    - Esempi validi: `"RSSMRA85M01H501Z"`
 > 
>      
>- **Partita IVA italiana (11 caratteri numerici):**
>    
  > 	 - Tipo di dato → `Stringa[11]` (solo cifre)
 >       
 > 	  - Esempio valido: `"01234567890"`


### Tipi di dato enumerativo
A volte, un attributo può assumere **soltanto un insieme ristretto e predefinito di valori**.  
Ad esempio, riprendendo l’esempio precedente, supponiamo di voler aggiungere un attributo `genere` alla classe `Studente`, assegnandogli **due possibili valori**:

- `maschio`
    
- `femmina`
    

In questi casi, si utilizza un **tipo di dato enumerativo**, che:
 ==Definisce esplicitamente e completamente l’insieme dei valori possibili per un attributo.==  

Ecco come possiamo rappresentarlo nel livello intensionale:

![](https://i.imgur.com/f9jis63.png)
Nel [[Analisi dei requisiti mediante UML#^inLevel|livello intensionale]] all'attributo `genere` iene assegnato il tipo di dato **enumerativo** `genere: {maschio, femmina}`. 
Questo perché il genere assume **un numero fisso e immutabile di valori**. 
Infatti, nel [[Analisi dei requisiti mediante UML#^exLevel|livello estensionale]] vediamo che per l'oggetto `anna` l’attributo `genere` ha il valore `femmina`

> [!NOTE] Da notare come il valore dell’attributo `nome` (`"Anna"`) è racchiuso tra virgolette, mentre `femmina` no.  
>Questo perché `"Anna"` è un valore di tipo **Stringa**, mentre `femmina` è un valore **enumerativo**.

#### Esempio con più valori 
Un altro esempio di **tipo di dato enumerativo** è l’attributo `continente`.
In questo caso, l’insieme dei valori è **completo e immutabile**, quindi dovremo **elencare tutti i continenti della Terra**: `continente:{Africa, America, Antardide, Asia, Europa,Oceania}`.

> [!hint] Quando si usa un tipo di dato enumerativo bisogna elencare per forza tutti gli insiemi di valori, non si può scrivere `ecc.`/`etc`/`...`


> [!info] Per ora per definire questi tipi di dati specializzati si può usare le note di Visual Paradigm, anche se si deve fare un diagramma a parte
> 


> [!danger] **Regola Generale**
> Se non conosci **tutti** i possibili valori di un attributo, **non devi usare un tipo enumerativo**, ma un altro tipo di dato più flessibile, come una **Stringa**.



### Tipi di dato composti(record)

UML consente all’analista di **definire tipi di dato composti** da più campi.  
Questi sono chiamati **tipi record** e ==consentono di **strutturare più informazioni all'interno di un singolo attributo**.== 

![](https://i.imgur.com/PLVktVD.png)
**Esempio di tipo composto:**
`Tipo indirizzo = (via: Stringa, civico:intero >0, cap: Intero>0) .`
Qui abbiamo un **tipo di dato composto (record)** con i seguenti campi:

- `tipo`: `(via, piazza, contrada, viale, corso)`
    
>[!danger] **Attenzione!**
>Come per il [[#Tipi di dato enumerativo|tipo di dato enumerativo]] anche qui non si può scrivere `etc.`! Bisogna **elencare tutte le possibilità**.
    
- `denominazione`: `Stringa`
    
- `civico`: `Intero`
    
- `CAP`: `Stringa numerica di 5 caratteri`
    


## Vincoli di molteplicità sugli attributi

In UML, è possibile applicare **vincoli di molteplicità** anche agli **attributi** di una classe.

![](https://i.imgur.com/qRpWENC.png)
Nell’immagine vediamo **due vincoli di molteplicità** definiti nel [[Analisi dei requisiti mediante UML#^inLevel|livello intensionale]]:
abbiamo 4 attributi
1. - `nome`: di tipo `Stringa`
    
2. `genere`: di tipo `Genere` (enumerativo)
    
3. `email`: di tipo `Stringa`, con un **vincolo di molteplicità** `1..*`
    
4. `indirizzo`: di tipo `Indirizzo`, con un **vincolo di molteplicità** `0..1`

In questo caso io non sto definendo il tipo di dato; ad esempio non sto dicendo che il valore dell'attributo email è una stringa che parte da un carattere e arriva fino a infinito, semmai sto dichiarando che:
- **`email: 1..*`** → Ogni oggetto `Studente` **deve avere almeno un’email**, ma può averne anche più di una.  
-  **`indirizzo: 0..1`** → Ogni `Studente` **può avere al massimo un indirizzo**, ma non è obbligato ad averne uno.

Nella pratica, questi vincoli si traducono così nel **livello estensionale**:
![](https://i.imgur.com/XG5maIz.png) 

#### **Esempio di tipo di dato composto**

Un altro esempio di vincolo applicato ai **tipi composti** è la definizione di un tipo **Denaro**, che comprende un importo e una valuta:

```
Tipo Denaro: tipo composto con i seguenti campi  
- Importo: Reale ≥ 0  
- Valuta: Stringa di 3 caratteri alfabetici maiuscoli  

```

**In questo caso**:

- L’attributo `Importo` è un numero reale che **non può mai essere negativo**.
    
- L’attributo `Valuta` deve essere una **stringa di esattamente 3 caratteri alfabetici maiuscoli** (es. `EUR`, `USD`, `JPY`).


## Vincoli di identificazioni di classe
 In alcuni casi, per modellare correttamente il dominio applicativo, è necessario imporre alcuni ulteriori vincoli oltre a quelli naturalmente imposti dal diagramma delle classi.
- Vincolo (di integrità): 
  ==una asserzione che impone restrizioni all’insieme dei livelli estensionali ammessi (ovvero agli insiemi di oggetti e link che possono coesistere) ulteriori a quelle strutturali che provengono dal diagramma delle classi==.
Abbiamo già visto i [[Vincoli di molteplicità sulle associazioni e sugli attributi|vincoli di molteplicità sulle associazioni]].

Ci sono però  un ulteriore tipologia di vincolo:
**vincolo di identificazione di classe**
-  ==Impone che non possono coesistere oggetti di una classe che coincidono nel valore di un insieme di attributi e/o sono collegati tramite link agli stessi oggetti di altre classi.==
![[vincoli di identificazione di una classe.png]]
Se guardiamo a questo esempio nella classe `Persona` stiamo dicendo che:
Non possono esistere due persone con lo stesso codice fiscale (“{id1}”) e non possono esistere persone con, simultaneamente, lo stesso nome, cognome e data di nascita (“{id2}”)

### Vincoli di identificazioni di classe nei ruoli di una classe 
Un vincolo di identificazione di classe può coinvolgere anche ruoli della classe.
![[vincoli sui ruoli di una classe.png]]
In questo esempio possiamo vedere:
- 2 classi:
  1. `Studente`;
     3 attributi
	  - `matr:Stringa{id}`
	  - `nome:Stringa`
	  - `cognome:Stringa`
  2. `Università` ;
	  1 attributo:
	   - `nome:Stringa`
- un associazione `iscritto`:
	2 vincoli;
	 - **`0..*`** (lato `Studente`): 
	   ==Una **università** può avere **zero o più studenti iscritti**==
	 - `1..1` (lato `Università`): 
	   ==Uno **studente** è iscritto a **una e una sola università**.==
Il vincolo di identificazione sull'attributo stringa ci dice che non possono esistere due studenti con lo stesso numero di matricola, quel `{id}` **non è un vincolo sul ruolo**, significa che **l’identificatore dell’associazione "iscritto" include l'identificatore della classe Università**.
In altre parole per **identificare un'istanza dell'associazione `iscritto`**, è sufficiente l'ID dello studente (**`matr`**), perché ogni studente è iscritto **a una sola università**.
Quindi si può dire che: 
==Il `{id}` sul ruolo `1..1` indica che **per ogni studente l’università a cui è iscritto è unica**, e quindi **l’identificatore dell'associazione è lo stesso dell'oggetto Studente**.==


> [!danger] un vincolo di identificazione di classe può coinvolgere solo attributi a molteplicità [1..1] e/o ruoli della classe a molteplicità 1..1
> 

Quindi riprendendo l'esercitazioni [[Ordini e fatture 1]]: se devo dire che non esistono due dipartimenti con lo stesso nome devo mettere accanto al valore dell'attributo `nome` nella classe Dipartimento:
`nome:Stringa{id}`

Per capire i vincoli delle associazioni delle classi, guardiamo le classi, se io ho 3 classi che sono associati tramite associazioni ed ho applicato il vincolo id all 'attributo' e sull vincolo di molteplicità associato a quella classe il vicnolo di classe è uno solo perché riguarda la stessa classe