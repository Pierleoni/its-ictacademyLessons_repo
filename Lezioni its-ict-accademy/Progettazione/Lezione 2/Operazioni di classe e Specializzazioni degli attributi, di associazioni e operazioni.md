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
Da notare come il questa operazione non abbia il parametro (o il tipo di ritorno) in input, questo perché: 
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
   ==restringendo il tipo, il dominio di valori o i vincoli==
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

3. Operazioni:
   ==ridefinendo il comportamento, restringendo i parametri o il tipo di ritorno, o aggiungendo vincoli.== 
   Quindi un operazione specializzata può:
- **ridefinire** l’implementazione nella sottoclasse (override).
    
- **restringere il tipo di ritorno** (covarianza).
    
- **aggiungere vincoli** più forti sui parametri o sulla semantica.

> [!example] Esempio
> Nella superclasse `Conto`: `calcolo_tot():Reale>0`
> Nella sottoclasse `ContoRisparmio`: `calcolo_interessi():Reale>0.5`


### Specializzazione di attributi: Esempio pratico
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
quindi l'oggetto a può essere venduto da esattamente solo vp1, tuttavia se ci fosse l'istanza vp2, quindi può esserci un nuovo link tra questa istanza e l'istanza di articolonuovo? 
SI, perchè il vincolo 1..1 dice che articolo nuovo partecipa esatemmente a un link venditore nuovo ma articolo nuovo può particapera ad lameno un link venditore e quando partecuipa al link vendiotore il venditore può essere un utente e basta o un vendiotre, quindi è ammesso.
Quindi se vend_nuovo lo scrivo come venditorepreferito volgio dire che un articolo viene venduto da un venditore preferito ma può essere venduto da latri utenti/venditori.
![[Screenshot 2025-04-29 at 12-49-33 Meet - bmb-xnne-ahh.png]]
Esiste articolo a:ArticoloNuovo, 
creaimo 4 utenti:
u1:Utente
u2:Utente
v1:VendProf
v2:VendProf
ho questi 5 oggetti, quali link posso creare?
Succede solo esattamente solo un vendiotre professionale può essere il venditore preferito, quindi può essereci il link (a,v1): vend_preferito, ma non può esserci il link (a, v2):vend_preferito, ma v2 può essere un venditore perché è un vendiotre.
Ma mettiamo che u1 metta in vendita l'articolo a, quindi pùò esserci il link (a, u1): venditore
(a,u2):venditore 


Un altor esempio di articolo fuorviante
![[Screenshot 2025-04-29 at 12-55-12 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]

Il vincolo 1..* è fuorviante. In realtà diagramma implica che ogni articolo nuovo è venduto da un solo venditore professionale! Quindi è 1..1
Implica chel'eticolo nuovo è venduto da un solo vendiotre professionale
Questo è anche peggio perché dice che un articolo nuovo può essere messo in vendita da 2 venditori professionali ma può essere messo in vnedita da almeno un utente, quindi se metto creo un oggetto aritcolo nuovo si rompre tutto.
Mentre se dico che articolo nuovo partecipa ad almeno 2 venditore professionale che è una sottoclasse di utente quindi il vincolo accanto a utente(1..1) non è più vlaida ma diventerebbe il vincolo 0..*

Si posso specializzare anche le operazioni di classe:
![[Screenshot 2025-04-29 at 12-59-19 Meet - bmb-xnne-ahh.png]]

Nella classe Articolo c'è un operazione prezzo che applica un numero intero maggiore di 0.
Ignoriamo l'ultima la riga dell'operazione, noi sapremmo comunque che possiamo invocare comqunue l'operazione prezzo su articolo in offerta, ma riscirivendola nella sottoclasse abbiamo riscritto l'operazione prezzo, ma anziché applicare il prezzo normalmente come fa la classe padre nella sottoclasse applica anche lo sconto dato dall'attributo `tasso_sconto`, quindi diventa un operazione specializzata, usa il dato dell'attributo tasso_sconto e lo calcola nell'operazione eredita anche l'attributo `prezzo_unitario` (in sintesi è l'overriding dei metodi di Python).
L'operazione specializzata posteva anche restituire un intero perché gli interi sono anche reali ma non il contrario, i tipi di arogmenti devono essere **esattamente** uguali all'operazione che si trova nella classe padre.
