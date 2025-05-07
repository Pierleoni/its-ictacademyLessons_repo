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


L'ereditarietà come funziona sugli attributi funziona anche per le operazioni:
ad esempio se la classe 

Dove si scirve questo vlaore restituito, si scrive in un documento a parte schiamato documento di specifica 
se un op non rstituisce niente non si scrive nulla dopo i due punti 
L'ereditarietà 
Le operazioni manipolano dati nel sistema, non li creano
## Specializzazione degli attributi di associazioni ed operazioni
Si pùò restringere il tipo di attributo quando viene eredito in una sottoclasse
Se ereditiamo l'attributo di una superclasse i vlaori dell'attributo della sottoclasse hanno i propri vlaori, ad esempio studneti starnieri nel numero di matricola hanno due 0 seguuti da un numero, lo posos fare

Ad esempio devo vendere delgi atticolo, pero alcuni articoli nuovi hanno una garanzia che sia un intero>=2 rispetto agli articoli che hanno la garanzia Intero>=0
![[img/Screenshot 2025-04-29 at 12-21-36 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]

Il relae per anni di garanzia non è più ammesso perchè il tipo reale e meno stringente rispetto ad intero, perché permette più vlaori rispetto a quelli di intero>=0, per cui l'attributo della sottoclasse non può avwere un tipo specializzato che supera il vlaore specializzato della superclasse.
QUando specializzo un attributo il tipo ella sottoclasse deve essere rispetto a quello della superclasse ma comunque compatibile con lo stesso tipo di dato specificato nella superclasse.
Ad esempio qui potrei avere nella superclasse un valore per anni_garanzia reale e nella sotto classe sempre un intero>=2, questo è ammesso perché 

Specializzazione di associzioni
Posso specializzare anche le diverse association class, è una relazione is-a anzichè tra oggetti tra link
![[Screenshot 2025-04-29 at 12-27-04 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]
Un aritcolo in vendita è venduta esattamente da un utente (1..1 vicino a utente), ma un articlo in vendita può essere un articolo nuovo come un utente può essere messo in vendita da un venditore professionale.
Tutti i link vend_nuovo sono anche venditore, non è vero il contrario perché se un articolo in vendita non è un articolo nuovo e l'utente non è venditore professionale allora il link nopn è più valido.
Riprendeod l'esempio di azienda1:
![[Screenshot 2025-04-29 at 12-30-13 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]

In questo caso sto dicendo che se un impiegato dirige un dipartiemto allora vi afferisce anche, quindi io posso essere un impiegato che afferisce e basta ma posso essere anche un impieghato che lo dirige e quindi vi afferisce.
QUi un dipartiemento in questo caso quanto impiegati afferiscono?
A sinistra dico che il dipartiemento è afferito da 0 a più impiegati pero c'è almeno un mipiegato che lo dirige e quindi vi afferisce anche.
Quini lo 0 to star diventa fuorviante, infatti in questo caso bisogna stare attenti con i vincoli, infatti a sinistra dovrei mettere 1..* oppure a destra 0..1.
La questione è spinosa:
il diagramma degli articoli dice che:
un articolo nuovo è venduta da quanti utenti viene venduto? 
C'è l'articolo a che è istnaza di nuovo, c'è utente1 che istsnza di utente e utente2 che è istnaza di utente e l'istanza di vpi che è istanza di venditore Professionale, 
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
![[Screenshot 2025-05-05 at 15-17-35 Meet - bmb-xnne-ahh.png]]

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
