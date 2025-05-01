Fiora abbiamo smepre è solo utilizzato gli attributi, le classi modellano oggetti del mondo che hanno proprietà in comune. 
Queste proprietà per ora sono rimaste statiche mentre una prorpiretà dinamica:
 i valori vengono calcolati ogni volta che servono, a partire dai valori di altre
proprietà.

Una operazione della classe C indica che su ogni
oggetto (istanza) della classe C si può eseguire un
calcolo per:
• calcolare un valore a partire da altri dati e operazioni
• effettuare cambiamenti di stato dell’oggetto (cioè per
modificare le sue proprietà), dei link in cui è coinvolto
e/o degli oggetti a questo collegati.
L'operazione di classe significa che su goni ogetto Studente si può fare un calcolo, ciò significa che il clacolo può fare due cose:
• calcolare un valore a partire da altri dati e operazioni
• effettuare cambiamenti di stato dell’oggetto (cioè per
modificare le sue proprietà), dei link in cui è coinvolto
e/o degli oggetti a questo collegati.

Su tutti gli oggetti studente si può invocare il calcolo `n_esami_fino_a(d:Data):Intero>=0`
Ogni qual volta chiedo il valore di questa prorpietà viene calcolato il valore di questa prorpietà.

La signatura dell'operazione:
nome_operazione(argomenti) : tipo_ritorno
dove:
• “argomenti” è una lista di elementi della forma:
nome_argomento : tipo_argomento
• “tipo_ritorno” è il tipo del valore restituito
dall’operazione
• I tipi degli argomenti e del valore di ritorno
possono essere tipi di dato concettuali oppure
classi del diagramma
• Una operazione di classe può essere invocata
solo su un oggetto della classe, che è un ulteriore
argomento (non indicato nella segnatura).

Il diagramma a destra a sia il livello estensionale che intenzionale 

voto medio è un operazione della classe corso: vuol dire che tutti gli oggetti della classe corso rispondono all'operazione voto_medio() ma questa operazione ritornerà un reale compreso tra 18 e 30.
L'ereditarietà come funziona sugli attributi funziona anche per le operazioni:
ad esempio se la classe 

Dove si scirve questo vlaore restituito, si scrive in un documento a parte schiamato documento di specifica 
se un op non rstituisce niente non si scrive nulla dopo i due punti 


## Specializzazione degli attributi di associazioni ed operazioni

Se ereditiamo l'attributo di una superclasse i vlaori dell'attributo della sottoclasse hanno i propri vlaori, ad esempio studneti starnieri nel numero di matricola hanno due 0 seguuti da un numero, lo posos fare

Ad esempio devo vendere delgi atticolo, pero alcuni articoli nuovi hanno una garanzia che sia un intero>=2 rispetto agli articoli che hanno la garanzia Intero>=0
![[img/Screenshot 2025-04-29 at 12-21-36 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]

Il relae per anni di garanzia non è più ammesso perchè il tipo reale e meno stringente rispetto ad intero, perché permette più vlaori rispetto a quelli di intero>=0, per cui l'attributo della sottoclasse non può avwere un tipo specializzato che supera il vlaore specializzato della superclasse.
QUando specializzo un attributo il tipo ella sottoclasse deve essere rispetto a quello della superclasse ma comunque compatibile con lo stesso tipo di dato specificato nella superclasse.
Ad esempio qui potrei avere nella superclasse un valore per anni_garanzia reale e nella sotto classe sempre un intero>=2, questo è ammesso perché 

Specializzazione di associzioni
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

Un altor esempio di articolo fuorviante
![[Screenshot 2025-04-29 at 12-55-12 Slide A.1 - Analisi dei requisiti mediante UML - BD2 - Slide A.1 - Analisi dei requisiti mediante UML - BD2.pdf.png]]

Il vincolo 1..* è fuorviante. In realtà diagramma implica che ogni articolo nuovo è venduto da un solo venditore professionale!
Implica chel'eticolo nuovo è venduto da un solo vendiotre professionale
Questo è anche peggio perché dice che un articolo nuovo può essere messo in vendita da 2 venditori professionali ma può essere messo in vnedita da almeno un utente, quindi se metto creo un oggetto aritcolo nuovo si rompre tutto.

Si posso specializzare anche le operazioni di classe:
![[Screenshot 2025-04-29 at 12-59-19 Meet - bmb-xnne-ahh.png]]

Nella classe Articolo c'è un operazione prezzo che applica un numero intero maggiore di 0 
