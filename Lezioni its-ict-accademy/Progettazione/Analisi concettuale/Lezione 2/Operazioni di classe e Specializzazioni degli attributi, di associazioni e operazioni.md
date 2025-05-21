# Introduzione

Finora abbiamo sempre è solo utilizzato gli attributi, le classi modellano oggetti del mondo che hanno proprietà in comune. 
Queste proprietà per ora sono rimaste statiche (cioè gli attributi e le [[Analisi dei requisiti mediante UML#Cosa sono le associazioni?|associazioni]]) mentre ora introduciamo le proprietà dinamiche:
 ==i valori vengono calcolati ogni volta che servono, a partire dai valori di altre==
==proprietà.==
Ovvero le operazioni di classe in UML.
## Cosa sono le operazioni di classe

Le operazione di classe sono: 
operazione dinamiche, che a differenza delle proprietà statiche che non evolvono automaticamente, queste si evolvono automaticamente e si calcolano in base ad altre proprietà delle classi. 

> [!attention] **Le operazioni di classe non possono stare nell' associazioni con attributi([[Associazioni con attributi in UML#Le association class|association class]]).** 
> Questo perché l'operazione appartiene a una classe e non può essere direttamente associata a una association class.


Una operazione della classe C indica che su ogni oggetto (istanza) della classe C si può eseguire un calcolo per:
• calcolare un valore a partire da altri dati e operazioni
• effettuare cambiamenti di stato dell’oggetto (cioè per modificare le sue proprietà), dei link in cui è coinvolto e/o degli oggetti a questo collegati.

Prendiamo ad esempio questa immagine:
![[operazioni di classe 1.png]]
L'operazione di classe significa che su ogni oggetto `Studente` si può fare un calcolo, ciò significa che il calcolo può fare due cose:
• calcolare un valore a partire da altri dati e operazioni:
    - L'operazione `n_esami_fino_a(d:Data):Intero>=0`, sostanzialmente sta dicendo che il prende in input un parametro di tipo `Data` e restituisce un dato di tipo Intero che deve essere maggiore o uguale a zero. 
	  Detto in parole povere sta calcolando il numero di esami sostenuti dallo studente fino alla data messa in input

• effettuare cambiamenti di stato dell’oggetto (cioè per modificare le sue proprietà), dei link in cui è coinvolto e/o degli oggetti a questo collegati.
Su tutti gli oggetti di quella classe, dove è presente l'operazione, possono invocare questa operazione. 
Quindi Su tutti gli oggetti studente si può invocare il calcolo `n_esami_fino_a(d:Data):Intero>=0`.
Ergo, ==ogni qual volta chiedo il valore di questa proprietà viene calcolato il valore di questa proprietà==.

## Come si scrive
Sul diagramma delle classi  la signatura dell'operazione è :
`nome_operazione(nome_argomenti: tipo_argomento) : tipo_ritorno` 
dove:
• “argomenti” è una lista di elementi della forma:
`nome_argomento : tipo_argomento` 
• “`tipo_ritorno`” è il tipo del valore restituito dall’operazione
• I tipi degli argomenti e del valore di ritorno possono essere tipi di dato concettuali oppure classi del diagramma
• Una operazione di classe può essere invocata solo su un oggetto della classe, che è un ulteriore argomento (non indicato nella segnatura).
Prendiamo ad esempio questa immagine :
![[Operazioni_di_classe Sintassi.png]]

Questo diagramma mostra sia il livello [[Analisi dei requisiti mediante UML#^exLevel|estensionale]] che il livello [[Analisi dei requisiti mediante UML#^inLevel|intensionale]].
Le operazioni di classe, possiamo vederle come dei messaggi, a cui gli oggetti della classe possono rispondere. 
Quindi seguendo l'immagine sopra tutti gli oggetti della classe `Studente` possono invocare il calcolo della media(`media_fino_a(d:Data):Reale in 18..30`).
Infatti nell'immagine vediamo che l'oggetto `s` (istanza della classe `Studente`), oltre ad avere gli attributi `matricola` e `nome`, può invocare l’operazione per il calcolo della media. 
Allo stesso modo, anche gli oggetti della classe `Corso` possono invocare l’operazione: `voto_medio():Reale in 18..30`.
Da notare come il questa operazione non abbia il parametro (o il tipo di argomento) in input, questo perché: 
`voto_medio` calcola la media dei voti degli esami relativi a quel corso, di conseguenza non ha un parametro esterno(o per meglio dire un tipo di argomento) come data o filtro, a differenza di `media_fino_a`, che calcola la media degli esami sostenuti _fino a una certa data_.
In altre parole: `voto_medio()` usa **solo lo stato interno dell’oggetto `Corso`**, cioè la lista degli esami e i relativi voti. Per questo motivo **non ha bisogno di argomenti in input**: è un'operazione che lavora esclusivamente sui dati già contenuti all’interno dell’oggetto.

> ✅ Ogni volta che si chiede il valore restituito da `voto_medio()`, viene effettuato il calcolo in tempo reale sulla base degli esami associati al corso.

#### Quando manca il tipo di ritorno

Abbiamo visto che alcune operazioni di classe possono non richiedere un tipo di **argomento** in input, perché lavorano solo sullo stato interno dell’oggetto. Allo stesso modo, **alcune operazioni possono anche non avere un tipo di ritorno**.
==Un caso tipico è quando l’operazione serve a **modificare direttamente lo stato interno dell’oggetto**, senza restituire alcun valore.==

Ipotizziamo ad esempio un'operazione di classe chiamata `n_bocciature(d:Data)` che, ogni volta che lo studente viene bocciato a un esame entro una certa data, **incrementa un contatore interno**.
Questa operazione non restituisce alcun valore (quindi non ha un tipo di ritorno), ma ha comunque un effetto importante: **modifica uno degli attributi interni dell’oggetto**, aggiornando il numero di bocciature. In casi come questo, non è necessario che l’operazione produca un risultato esterno, perché il suo scopo è solo **modificare lo stato dell’oggetto**.

### L'ereditarietà nelle operazioni di classe 
Abbiamo ampiamente visto nella lezione [[Generalizzazioni]] come funzione [[Generalizzazioni#Relazione is-a tra classi ereditarietà|l'ereditarietà]] tra le classi e sugli attributi delle classi, questa relazione funziona anche per le operazioni di classe:
![[ereditarietà_operazioni_diClasse.png]]
Seguendo questa immagine possiamo vedere innanzitutto che nel livello [[Analisi dei requisiti mediante UML#^inLevel|intensionale]]  la classe `StudenteStraniero` è una sottoclasse di `Studente`, e quindi eredita gli attributi e può invocare l'operazione `media_fino_a(d:Data):Reale in 18..30`. 
Nel livello [[Analisi dei requisiti mediante UML#^exLevel|estensionale]] l'oggetto (istanza di `StudenteStraniero`)  `ss:StudenteStraniero` eredita gli attributi della classe `Studente` (`matricola` e `nome`) è può anche invocare l'operazione `media_fino_a()`. 
Difatti:
![[Esempio_opDiClasse_istanza.png]]
l'oggetto `ss` invoca l'operazione di classe `media_fino_a()`.

Tuttavia il limite del diagramma delle classi è quello che non definisce cosa calcolano le operazioni, né se e come modificano i dati. 
Infatti ogni classe del diagramma con operazioni andrà affiancata da un documento di specifica che entra nel dettaglio (vedi la lezione [[Documenti di specifica]]). 


---

## Specializzazione degli attributi di associazioni ed operazioni
Si può restringere il tipo di dato dell'attributo quando viene eredito in una sottoclasse.
Se ereditiamo l'attributo di una superclasse i valori dell'attributo della sottoclasse hanno i propri valori più ristretti (per meglio dire **Specializzati**).
Ad esempio, riprendiamo l'immagine [[ereditarietà_operazioni_diClasse.png]]: ipotizziamo  che la classe `StudenteStraniero` abbiamo il proprio attributo `matricola`, ma anziché essere un intero maggiore di zero come nella classe padre `Studente`, specializziamo il tipo di dato dell'attributo `matricola` in un Intero che ha due 0 seguiti da un numero.
Quindi possiamo dire che:
==**La specializzazione di attributi, associazioni e operazioni** si verifica quando una **sottoclasse** ridefinisce o raffina un elemento della **superclasse** in modo da renderlo **più specifico**, **più vincolato** o **più dettagliato** rispetto alla definizione originale, mantenendo la compatibilità semantica con essa.== 
Ciò può avvenire tramite:
1. **[[#Specializzazione di attributi Esempio pratico|Attributi]]:** 
   ==restringendo il tipo, il dominio di valori o i vincoli.==  ^445701

Quindi un attributo specializzato in una sottoclasse può; 
- avere un **tipo più specifico** (es. `Intero > 0` invece di `Intero`),
    
- avere **vincoli più stringenti** (es. un range di valori più stretto),
    
- essere **ridefinito** con un significato più preciso nel contesto della sottoclasse.
   
> [!example] Esempio
> 
> Nella superclasse `Persona`: `eta: Intero >=0`
> Nella sottoclasse `StudenteUniversitario`: `età: Intero>=18`

2. **[[#Specializzazione di associazioni Esempio Pratico|Associazioni]]:** 
   ==restringendo la molteplicità, specificando meglio il tipo associato, o rafforzando i vincoli.==
   Quindi una associazione specializzata può:
- restringere la **molteplicità** (es. da `0..*` a `1..2`),
    
- specificare un **tipo più specifico** di classe associata,
    
- aggiungere **vincoli più forti** o ruoli più precisi.

> [!example] Esempio
> Nella superclasse `Lavoratore` è associato a `Azienda` con molteplicità `0..*`
> Nella sottoclasse `Impiegato` è associato alla sottoclasse di `Azienda`, `AziendaPubblica`, con una molteplicità `1..1`

3. **[[#5dbd80 Specializzazioni di Operazioni di classe Esempio Pratico|Operazioni]]**:
   ==ridefinendo il comportamento, restringendo i parametri o il tipo di ritorno, o aggiungendo vincoli.==  ^5dbd80

   Quindi un operazione specializzata può: 
- **ridefinire** l’implementazione nella sottoclasse (override).
    
- **restringere il tipo di ritorno** (covarianza).
    
- **aggiungere vincoli** più forti sui parametri o sulla semantica.

> [!example] Esempio
> Nella superclasse `Conto`: `calcolo_tot():Reale>0`
> Nella sottoclasse `ContoRisparmio`: `calcolo_interessi():Reale>0.5`


### [[#^445701|Specializzazione di attributi]]: Esempio pratico
Immaginiamo un caso in cui si deve progettare un sistema che tenga traccia degli articoli in vendita:
- Degli articoli in vendita vanno rappresentati: nome e numero di anni di garanzia (anche zero)
-  Alcuni articoli sono nuovi
-  Degli articoli nuovi interessa anche il codice EAN
-  Inoltre, per gli articoli nuovi, la garanzia deve essere di almeno due anni
Ad esempio devo vendere delgi atticolo, pero alcuni articoli nuovi hanno una garanzia che sia un intero>=2 rispetto agli articoli che hanno la garanzia Intero>=0
![[Specializzazione_attributi.png]]

Prendendo come riferimento questa immagine vediamo infatti che la sottoclasse `ArticoloNuovo` eredita dalla classe padre `ArticoloInVendita` l'attributo `nome` e `anni_garanzia` ma su quest'attributo restringe il tipo dicendo che il tipo dell'attributo è un `Intero >=2` e non più un `Intero >=0`.
Infatti Il reale per anni di garanzia non è più ammesso, perché il tipo reale è meno stringente rispetto ad intero, perché permette più valori rispetto a quelli di intero>=0, ==per cui l'attributo della sottoclasse non può avere un tipo specializzato che supera il valore specializzato della superclasse==.
==Quando si specializza il tipo dell'attributo della sottoclasse, deve essere **più ristretto** rispetto a quello della superclasse ma comunque compatibile con lo stesso tipo di dato specificato nella superclasse==.
Ad esempio qui potremmo avere nella superclasse un valore per `anni_garanzia:Reale` e nella sotto classe sempre un valore  per `anni_garanzia:Intero>=2`, questo è ammesso perché un numero intero è compreso tra i numeri reali e non viceversa.

### Specializzazione di associazioni: Esempio Pratico 
Si possono specializzare anche le diverse association class: è una relazione [[Generalizzazioni#^is-aDef|is-a]] anziché tra oggetti tra link.
Immaginiamo di dover progettare un sistema informativo che tenga traccia degli articoli venduti e degli utenti e venditori:
- Ogni articolo è venduto da esattamente un utente
- Gli articoli nuovi devono essere venduti da almeno due venditori professionali.
![[Specializzazione_associazioni1.png]]

In questo diagramma stiamo dicendo che: 
Un articolo in vendita è venduto esattamente da un utente (`1..1` vicino a utente), ma un articolo in vendita può essere anche un articolo nuovo, come un utente può essere anche un venditore professionale che a sua volta può vendere da 0 a più articoli nuovi (guarda il vincolo `0..*` ) e un articolo nuovo è venduto esattamente da un venditore professionale (`1..1` vicino a venditore).
Tutti i collegamenti `vend_nuovo` sono anche validi come collegamenti `venditore`, perché coinvolgono istanze di classi figlie (`ArticoloNuovo` ⊆ ([[Generalizzazioni#^is-aDef|is-a]]) `ArticoloInVendita`, `VenditoreProfessionale` ⊆ (is-a) `Utente`). Tuttavia, **non vale il contrario**: non tutti i collegamenti `venditore` sono anche `vend_nuovo`, perché potrebbero coinvolgere un `ArticoloInVendita` che non è un `ArticoloNuovo` o un `Utente` che non è un `VenditoreProfessionale`.
Per spiegare meglio questo concetto riprendiamo  l'esempio di [[Esercitazione Azienda 1|Azienda 1]]:
In quell'esercitazione si è dovuto creare due classi diverse, una `Impiegato` e l'altra `Direttore`, la prima che aveva una associazione di nome `afferisce` con la classe `Dipartimento` e l'altra una associazione di nome `dirige` sempre con la classe `Dipartimento`. 
Questa ridondanza può essere risolta grazie alla specializzazione di associazioni:
![[secondoesempio di specializzazione delle associazioni.png]]

Con questo diagramma stiamo dicendo che:
se un `Impiegato` dirige un dipartimento allora vi afferisce anche, quindi si può essere un impiegato che afferisce a un dipartimento ma non lo dirige, come si può essere anche un impiegato che  dirige il dipartimento e quindi vi afferisce.
In un dipartimento, in questo caso, quanto impiegati afferiscono?
Leggiamo il diagramma da sinistra verso destra:
 il dipartimento può avere da 0 a più impiegati che vi afferiscono (`0..*`) e un impiegato può afferire almeno ad un solo dipartimento (`1..1`), pero c'è almeno un impiegato che  dirige il dipartimento (`0..1`) come il dipartimento può essere diretto da solo un impiegato (`1..1`) che tra l'altro vi afferisce anche.
 Infatti, come per l'esempio sopra, una association class, in quanto classe, può anche essere radice di relazioni is-a e generalizzazioni.
Difatti in questo diagramma lo 0 to star diventa fuorviante perché:
la molteplicità `0..*` suggerisce che un dipartimento può avere anche zero impiegati che vi afferiscono.
Ma..
>==Se un dipartimento è diretto da qualcuno (`dirige` con `1..1` sull'impiegato), e chi dirige **vi afferisce per forza**, allora il dipartimento **ha almeno un impiegato** (ovvero quello che lo dirige).==

Quindi **non è vero che il dipartimento può avere zero impiegati** in generale.
Il vincolo `0..*` non tiene conto della specializzazione, cioè del fatto che **almeno uno (cioè il direttore) deve esserci se il dipartimento è diretto.**
Va da sé che a questo punto bisogna cambiare la molteplicità sul lato della classe `Impiegato`, sulla associazione `afferenza`, che da `0..*` passa a `1..*`, questo significa dire:
> "Ogni dipartimento ha **almeno un impiegato** che vi afferisce" (cioè il direttore)

Questo riflette meglio il fatto che:

- Se **nessuno afferisce**, **nessuno può dirigere** (dato che dirigere è una specializzazione di afferenza)
    
- Quindi un dipartimento diretto → ha **almeno uno** (il direttore) che afferisce

![[Secondo esempio di specializzazione delle associazioni ammesso.png]]


> [!ticket] Se una **sottoclasse di un'associazione implica la presenza nella classe madre**, i vincoli devono riflettere anche quel legame implicito, altrimenti diventano **fuorvianti**.

Ora che abbiamo appreso questa consapevolezza torniamo al [[Specializzazione_associazioni1.png|diagramma della classi degli articoli in vendita]]:

Per risolvere questo problema bisogna porci la domanda: un articolo nuovo è venduta da quanti utenti ? 
Immaginiamo di avere più istanze:
  - `a` a che è istanza di `ArticoloInVendita `.
  - `utente1` e `utente2` che sono istanze di `Utente`.
  -  `v1` e `v2` che sono istanze di `VenditoreProfessionale`.
  ![[Diagramma Articolo_Risolto.png]]
Nel contesto di questo nuovo diagramma abbiamo diverse relazioni:
- Abbiamo una relazione `vend_nuovo` tra `ArticoloNuovo` e `VenditoreProfessionale`.
- Questa relazione è una **specializzazione** della più generale `venditore`, che collega `ArticoloInVendita` a `Utente`.
L'interpretazione semantica è:
- Un istanza di `ArticoloNuovo` è un anche un istanza di `ArticoloInVendita`.
    
- Un istanza di  `VenditoreProfessionale` è anche un istanza di `Utente`.
    
- `vend_nuovo` è una **specializzazione** di `venditore`.

Ciò significa che:  
==**Se un `VenditoreProfessionale` vende un `ArticoloNuovo` tramite `vend_nuovo`, allora vende anche l’articolo tramite la relazione `venditore`**.==

Tuttavia questo diagramma è fuorviante, per via delle molteplicità sulla relazione `venditore`:
- `0..*` lato ArticoloInVendita
    
- `1..1` lato Utente
Quindi **sembra** che un articolo possa essere venduto da **zero utenti**.
Ma questa è **fuorviante**, per lo stesso motivo visto nel caso "impiegato-dipartimento":
==Se un `ArticoloNuovo` è associato a un `VenditoreProfessionale` tramite `vend_nuovo`, allora **per forza** deve anche partecipare a `venditore`.==  
==Dunque l’articolo è venduto da almeno **uno** (il venditore preferito).==
==**Quindi dire che la molteplicità su `venditore` è `0..*` non è del tutto corretto.**== 

Questo problema si può ovviare andando a modificare i vincoli di molteplicità; al fine di essere **semanticamente coerenti** con la specializzazione:
la molteplicità sul lato di `ArticoloInVendita` nella relazione `venditore` dovrebbe essere **`1..*`**.
Questo perché è come dire:
=="Ogni articolo (nuovo o usato) è messo in vendita **da almeno uno o più utenti**”==
Di conseguenza:
==“Se è un articolo nuovo, allora è venduto da almeno un utente, e **uno di questi è anche venditore preferito (cioè un venditore professionale)**.”==
In conclusione, quindi, bisogna ricordare che:
==Quando una **relazione è specializzazione di un’altra**, bisogna ricordare che ogni **istanza della relazione specializzata** **è anche** un’istanza della relazione generale.==  
==Quindi i **vincoli di molteplicità sulla relazione generale devono tener conto anche di quelli impliciti** portati dalla specializzazione.==


> [!ticket] Regola d'oro
> **==Una relazione specializzata rafforza semanticamente la relazione generale: i suoi effetti devono essere riflessi anche nei vincoli.==**



##### Un altro esempio di articolo fuorviante:
![[Un altro esempio di articolo in vendita.png]]
In questo diagramma abbiamo:
- Una **relazione principale** `venditore` tra `ArticoloInVendita` e `Utente`, con classe associativa (con attributo `istante` con valore `DataOra`).
    
- Una **specializzazione** di quella relazione: `vend_nuovo`, tra `ArticoloNuovo` (sottoclasse di `ArticoloInVendita`) e `VenditoreProfessionale` (sottoclasse di `Utente`).
I vincoli di molteplicità sono: 

| Associazioni | Lato Articolo            | Lato Venditore                        |
| ------------ | ------------------------ | ------------------------------------- |
| `venditore`  | `0..*` ArticoloInVendita | `1..1` Utente                         |
| `vend_nuovo` | `0..*` ArticoloNuovo     | `1..*` VenditoreProfessionale<br>(🔴) |
Ora cosa non torna in questo diagramma?
-  **Specializzazione implicita:**
	Poiché l'association class `vend_nuovo` è **specializzazione** della association class `venditore`, ogni coppia 
	`(ArticoloNuovo, VenditoreProfessionale)` in `vend_nuovo` **è anche** una coppia in `venditore`.
	
Quindi è come dire che : 
>ogni `ArticoloNuovo` è anche in relazione con un `Utente` attraverso `venditore` — nello specifico, quel venditore è un `VenditoreProfessionale`.
 
In altre parole ogni articolo nuovo può essere venduto da almeno un venditore professionale o anche più di uno. 
Questa condizione è data dal vincolo di molteplicità `1..*` accanto a `VenditoreProfessionale`, tuttavia:
**ha senso che uno stesso articolo nuovo sia messo in vendita da più venditori professionali?** 
In un sistema e-commerce realistico, **NO**: ogni annuncio/articolo è venduto da **uno solo**.
Quindi il vincolo `1..*` va corretto e cambiato in `1..1 `:
Se si dice che un `ArticoloNuovo` può essere venduto da 2 o più `VenditoriProfessionali`, ma la relazione generale `venditore` ammette **solo un `Utente` (`1..1`) per ogni `ArticoloInVendita`**, allora hai un **conflitto**:

Un articolo ha più venditori professionali → quindi più utenti → ma può avere **solo 1 utente** come venditore?


> [!example] In sintesi
> > Se un `ArticoloNuovo` ha **più venditori professionali** tramite `vend_nuovo`, allora dovrebbe avere anche più utenti tramite `venditore`.
>
>❌ Ma questo **viola** la molteplicità `1..1` nella relazione `venditore` (cioè: ogni `ArticoloInVendita` è venduto da **uno solo** `Utente`).
>
>🔁 Quindi **o cambi la molteplicità di `venditore` in `0..*`**, oppure metti `1..1` anche in `vend_nuovo`.


Quindi, il vincolo `1..*` nella relazione `vend_nuovo` è **fuorviante**, perché sembra suggerire che **un singolo `ArticoloNuovo` possa essere venduto da più `VenditoriProfessionali`**, ma la relazione generale `venditore` (che collega ogni `ArticoloInVendita` a **uno solo** `Utente`) verrebbe **violata** in tal caso.
 ==Per coerenza, dovremmo cambiare la molteplicità di `vend_nuovo` da `1..*` a `1..1`, per dire chiaramente che ogni `ArticoloNuovo` è venduto da **esattamente uno** `VenditoreProfessionale` (che è anche un `Utente`), proprio come ogni `ArticoloInVendita` è venduto da uno solo `Utente`.== 

### [[#^5dbd80|Specializzazioni di Operazioni di classe]]: Esempio Pratico  

Come detto in precedenza si possono  specializzare anche le operazioni di classe:
![[Specializzazioni di operazioni di classe.png]]

In questo diagramma abbiamo:

- `Articolo`:
    
    - Attributi:
        
        - `nome: Stringa`
            
        - `prezzo_unitario: Reale >= 0`
            
    - Operazione:
        
        - `prezzo(num: Intero > 0, naz: Nazione): Reale >= 0`
            
            > Calcola il prezzo come:  
            > `prezzo_unitario * num + costo_spedizione(naz)`
            
- `ArticoloInOfferta` **è una sottoclasse** di `Articolo`
    
    - Attributo aggiuntivo:
        
        - `tasso_sconto: Reale in 0..1`
            
    - **Ridefinisce** l’operazione `prezzo(...)`:
        
        > Applica lo **sconto** sul prezzo calcolato dalla superclasse.


Quindi nella classe `Articolo` è presente un'operazione di classe `prezzo()`: prende come parametri (o tipi di argomento) un numero intero maggiore di 0 e una nazione. 
Come tipo di ritorno restituisce un reale maggiore maggiore o uguale a zero.
In altre parole questa operazione applica un prezzo sull'articolo in vendita prendendo come parametri un intero (che deve essere moltiplicato per l'attributo `prezzo_unitario: Reale >=0`) e calcola anche i costo di spedizione verso quella nazione in cui deve essere consegnato, restituendo un numero con la virgola che deve essere maggiore o uguale a zero.
Nella sottoclasse di `Articolo`, `ArticoloInOfferta`, c'è un attributo aggiuntivo `tasso_sconto:Reale in 0..1`: 
questa classe  eredita  e ridefinisce l'operazione `prezzo()` della classe padre applicando  il tasso di sconto sul prezzo calcolato dalla superclasse.
Proprio per questo l'operazione `prezzo()` viene specializzata: perché nella sottoclasse `ArticoloInOfferta` viene applicato lo sconto dato dall'attributo `tasso_sconto`.

Il concetto chiave dietro a ciò è l'[[Ereditarietà delle classi#L'overriding dei metodi|overriding]] dell'operazione:
La sottoclasse `ArticoloInOfferta` ridefinisce l’operazione `prezzo(...)`, usando la **stessa signatura** (stessi parametri e stesso tipo di ritorno).
Anche se non riscrivessimo `prezzo(...)` nella sottoclasse, potremmo comunque **ereditare** e usare l’operazione della superclasse (`Articolo`). Ma in questo caso **la ridefiniamo per adattarla** al contesto specifico (cioè applicare uno sconto).



> [!warning] Nota sui tipi di argomento
>  Quando si specializza un’operazione, i **tipi degli argomenti** devono essere **esattamente uguali** a quelli definiti nella superclasse.
>Questo garantisce la **compatibilità** e il rispetto del **principio di sostituibilità** (es. principio di Liskov in OOP).
>
> > [!example] **Esempio**:
>>
>>- Se la superclasse ha:  
 > >  `prezzo(num: Intero, naz: Nazione): Reale`  
>>- Allora anche la sottoclasse **deve avere gli stessi tipi** per `num` e `naz`.
 > >  
>>
>> ✅ È accettabile che il tipo restituito sia più **specifico** (es. `Intero` al posto di `Reale`), perché ogni intero è anche un reale.  
>> ❌ Non è accettabile il contrario (es. restituire un `Reale` quando è atteso un `Intero`).


