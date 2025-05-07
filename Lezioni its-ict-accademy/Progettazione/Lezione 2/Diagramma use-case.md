Abbiamo finito di parlare dei dati (info forniti nel sistema), adesso parlaimo di funzioanlità:

Come utilizzo questo sitema (scenari di utilizzo) e cghi utilizza questo sistema.
Negli use case è un inseme eterogeno di funzionalità che sono accedute da un insieme di utenti.
modella gli utenti esterni (attori) che possono essere umani o sistemi esterni che utilizzerano il sistema.
Un attore è un ruolo che può esser giocato da un essere umano o da un sistema. 
Da notare come l'utente può ricorire i diversi ruoli (es: i ruoli possono essere amministrativo(visualizzare i voti di tutti), docenti, studenti, etc.)
Il ruolo attore può essere interpretato da diversi utenti, ma la persona può avere diveris ruoli. 

### Diagramma Uml degli Use-case
é un grafo:
i nodi rappresetnato attori e use case
gli archi sono le associazioni(da non vedere le associazioni del diagramma delle classi).
![[Screenshot 2025-05-05 at 15-54-13 Meet - bmb-xnne-ahh.png]]
La linea moella la possibilità di acceso da parte di un attore nel modello use case, quindi può accedere a tutte le possibilità degli use-case. 
Il diagramma use-case è molto vago o ad alto modello.
Il fatto che esite l'attore utente non è detto che nel diagramma delle classi esiste la classe utente, stesa cosa se esiste la classe utente non è detto che esiste la classe utente. Quindi le classi e gli attori non hanno nulla a che vedere tra loro, qui ci interesa di sapere chi lo usa.
Esempio:
Il sistema deve permettere agli studenti di iscriversi, via web, ai corsi offerti. La segreteria deve poter
assegnare i docenti ai singoli corsi. I docenti devono poter inserire i risultati dei test degli studenti: tali
test sono somministrati agli studenti utilizzando il sistema.
C'è l'attore studente che accede all'use case Gestione iscrizioni che è l'insieme di funzionalità che permettono l'iscrizione web da parte degli studenti, singole operazioni raccchiuse in un use case omogeneo.
Inoltre uno studente può accedere all'use-case Gestione test che può essere accesso anche dall'attore Docente.
Dopodichè c'è l'attore segreteria che accede alla gestione docenti. 
Questo diagramma è comunque troppo vago.
### Inclusione
Esiste un cotstrutto detto inclusione: 
nel nostro caso alcune funzionalità del case A può ha bisogno di accedere ad alcune funzonalità del case B: 
sia i case Somminitrazione Test che il case Creazione e valutazione test possono **usare** le funzionalità del case Gestione Test. 
L'inclusione viene indicata tramite il costrutto `<<include>>`
l'inclusione è come l'import in Python. gestione test sono un insmee di operazioni e somministrazione test ne può usare alcune.
I nomi sui case sono opzionali.
![[Screenshot 2025-05-05 at 16-06-24 Meet - bmb-xnne-ahh.png]]

### Estensione
mentre l'iclusione a che fare con alcune funzione di tipo import, l'estensione è come un plugin: Lo uso case A estende lo use case B (il verso va dal case che estende a quello che è esteso), in alcuni casi particolari, in cui alcune funzionalità di A sono migliorate, estese anche a B 
Pensiamo ad esempio che uno studente può accedere al case iscrizione, in più iscrizione viene esteso al case pagamento online il quale aggiunge più funzioni al case pagamento online.


Questo documento va associato ma non incluso nello schema concettuale delle classi:

### Generalizzazione tra use case
Alcune funzionalità dello use-case A, solo in alcuni casi particolari, sono rimpiazzate con le funzionalità dello use-case B. QUindi alcune funzionalita dell' use case A, in alcuni casi particolari, vengono ripmipazzate dalle funzionalità dello case B.
Ad esempio le funzionalità del case idnetificazioni in alcuni casi vengono sostootute dal case Cotnrollo password o in alcuni casi Accesso biometrico a varco.
Essite anche la generalizzazione tra attori: se B è A (se Manager è segreteria), tutti gli attori B possono sostituire gli attori A.
Questo diagramma serve:
a capire chi puo usare il sistmea(umano o sistema esterno)
e quali macro funzionalità possono essere accesse dagli attori.
Serve al commitente, senza che quest'ultimo abbia per forza una conoscenze tecnica della materia. 
Il diagramma no deifnisce le singole operazioni. 

### Specifica dello use-case 
La specifica degli use-case deve essere un documento separato da accludere allo schema concettuale.
