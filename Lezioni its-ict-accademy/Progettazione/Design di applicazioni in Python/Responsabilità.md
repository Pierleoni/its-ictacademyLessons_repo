Ogni volta che dobbiamo implementare le associazioni dobbiamo alle responsabilità: prendiamo Azienda 1, è utile conoscere il progetto in cui è conviolto l'impiegato? Si
È utile sapere qual'è impiegato dirige il dipartimento? Si
Oppure un imoiegato deve consocere i dip in cui afferisce perche deve assicurarsi che il vincolo `0..1` deve essere vlaido
Resp:
Per ogni assoc dobbiamo decidere quali delel 2 classi conivlt ne hanno la responabilità.
Cio significa conoscere una classe 

In quali casi serve la reps?
Serve se c'è un op di classe o un usecase e si ha bisogno in qualce modo che un oggetto della classe possa accedere ai link in qualche modo.
![[Operazioni di classe_Responsabilità.png]]
Se c'è un op di classe numero_impiegati su dip vuol dire che il dip deve conoscere il numero di impiegati e quindi un oggetto dip deve avere la responabilità di percorrere il numero di impiegati che vi aff.
Un altro caos è quando il vincolo non è `0..*`, perché la classe eve assicur. che il suo vincolo sia soddisfatto, quindi ad esempio al vincolo 0..1 l'impiegato ha la resp sull'assoc afferenza perchè un ipiegato si deve assicurare ch quel vincolo sia rispettato e quindi almeno un impegato deve afferire a quel dip.

Potrebbe anche essere che lo studente ha resp su corso di laurea ma da un corso di laurea non ci interessa sapere gli studenti iscritti:
in questo caso se la resp è singola, cioè di una sola freccia ovvero si da un verso di navigabilità.
Facciamo una modifica al diagramma aggiungendo la classe Città: 
immg che da un dip di conoscere la sua citta, ma dall'altra parte non chiedermoo a una citta di sapere i suoi dip, perche al dip serve conoscere il suo link verso citta ma non viceversa:

![[Responsabilità.png]]

Deve assic che il vincolo di moltepl 1..1 deve essere risp e perchè dobbiamo immaginare che nel sys ci sia un operazione che dato un dip bisogna conoscere la sua citta, ma data una città non serve conoscere i dipartienti che stanno in quella città. 
Quando succede questo, che la resp è singola e l'assoc non ha attr. si cihama aggregazione e si fa con il rombo: questo significa che la città è una proprietà di dip come quasi se fosse un attrib. 
L'agreg modella la relazione has-a: tipo da uno studnete si ha una riferimento diretto a un corso di laurea.
COme si implementano le aggregazioni?
Diventa una class Python specifica, ad esempio 
```

```

Da notare come le aggreg funzionano anhe con lo `0..*` ad esempio una persona ha visitato una città, la resp è singola quindi persona ha un aggregazione verso città 