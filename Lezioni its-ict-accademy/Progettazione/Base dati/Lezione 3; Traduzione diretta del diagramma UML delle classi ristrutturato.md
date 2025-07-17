
# Introduzione
Nella [[Lezione 2; La fase di progettazione|scorsa lezione]] abbiamo visto come ristrutturare il diagramma concettuale in un diagramma applicabile in PostgreSQL, in questa lezione affrontiamo come applicare la traduzione diretta del diagramma ristrutturato. 

### Metodologia da seguire

-  Ogni classe del diagramma si traduce in una tabella relazionale. 
- Ogni associazione si possono tradurre in altre tabelle relazionali, più vincoli di [[Lezione 1; Introduzione e modello relazionale#I vincoli foreign key (integrità referenziale)|foreign key]], oppure possono essere accorpate nella tabella che traduce una delle classi coinvolte nell'associazione.
- I vincoli di molteplicità dei ruoli di associazione si traducono in vincoli di chiave, foreign key, o in vincoli esterni (tipicamente, vincoli di inclusione più generale).

---

### Tradurre le classi dal diagramma UML delle classi ristrutturate
Per tradurre le classi in tabelle relazionali prendiamo ad esempio questa figura:


![[Traduzione diretta delle classi.png]]
1. La classe `Studente`:
	- con attributi: 
		  - `matricola:integer {id1}`(la sua chiave primaria)
		  - `nome:varchar`
		  - `genere: Genere`(tipo di dato enumerativo)
2. La classe `Corso`
	- con attributi:
		- `nome:varchar {id1}` (la sua chiave primaria)
		- `modalita:Modalita [0..1]` (tipo di dato enumerativo con un vincolo che indica che può esserci una modalità o può non esserci; ==in altre parole questo attributo può assumere valori `NULL`==).


Quindi, come già ampiamente visto, bisogna sostituire i tipi di dato con tipi di dato compatibili in PostgreSQL.
Dopodiché definire gli [[Lezione 2; La fase di progettazione#Identificatori di classe|identificatori artificiali]] nelle classi se sono sprovviste di attributi identificativi di classe e [[Lezione 2; La fase di progettazione#Le generalizzazioni|ristrutturare anche le generalizzazioni]].
Dopodiché si passa alla fase di  traduzione diretta in tabelle:

```postgresql
create table Studente (
	matricola integer not null,
	nome varchar not null,
	genere Genere not null,
	primary key (matricola)
);

create table Corso(
	nome varchar not null
	modialita Modalita --anche null
	primary key(nome)
)
```


### Tradurre le associazioni dal diagramma UML delle classi ristrutturate
Ci sono vari modi per tradurre le associazioni in PostgreSQL a seconda anche dei vincoli di molteplicità presenti nel diagramma UML ristrutturato.

#### Caso 1: traduzione diretta delle associazioni con vincoli `0..*` su entrambi i lati
Supponiamo ora che nel diagramma venga aggiunta un’associazione tra le classi `Studente` e `Corso`, e che su questa associazione sia definita una association class `esame` con attributo `voto:Voto`:

![[Traduzione diretta delle associazioni.png]]

Anche in questo caso è necessario creare una **tabella relazionale** per rappresentare l’associazione, poiché i **vincoli di molteplicità** sull'associazione `Esame` sono `0..*` su entrambi i lati (cioè un'associazione molti-a-molti):
```postgresql
create table esame(
studente integer not null,
corso varchar not null,
Foreign Key (studente) references Studente(matricola),
Foreign Key (corso) references Corso(nome),
primary key(studente, corso),
);
```
###### **Spiegazione:** 
La tabella `Esame` prende come **chiavi esterne** i riferimenti alle entità `Studente` e `Corso`, utilizzando il tipo di dato corrispondente alle rispettive chiavi primarie:

- `studente: INTEGER` → corrisponde a `matricola` in `Studente`
    
- `corso: VARCHAR` → corrisponde a `nome` in `Corso`.

##### Foreign Key e vincoli di molteplicità 
Le due **foreign key** permettono di rispettare i **vincoli di molteplicità `0..*`** presenti su entrambi i lati dell'associazione `esame`:

1. `FOREIGN KEY (studente) REFERENCES Studente(matricola)`  
    Il campo `studente` nella tabella `Esame` fa riferimento al campo `matricola` della tabella `Studente`.  
    Ciò è perfettamente coerente con la semantica del modello, poiché attraverso il numero di matricola (che rappresenta la chiave primaria dello studente) è possibile risalire agli altri attributi dello studente, come `nome` e `genere`.  
    Questo vincolo garantisce che ogni valore presente nella colonna `studente` di `Esame` **debba necessariamente comparire nella colonna `matricola` di `Studente`**, assicurando l’integrità referenziale.
    In altre parole: **non si possono registrare esami per studenti inesistenti**.
2. `FOREIGN KEY (corso) REFERENCES Corso(nome)`  
    Analogamente, il campo `corso` nella tabella `Esame` fa riferimento al campo `nome` della tabella `Corso`.  
    Anche in questo caso, la foreign key assicura che ogni valore di `corso` nella tabella `Esame` sia presente come chiave primaria nella tabella `Corso`, mantenendo la coerenza tra le due entità.
    In altre parole:**non si possono registrare esami per corsi non presenti in `Corso`**.

Poiché un’associazione `Studente-Corso` può essere registrata **al massimo una volta** (ossia, non è ammessa la ripetizione di esami per la stessa coppia `studente-corso`), la **primary key** in questo caso è la coppia `studente, corso`: ==perché **non può ripetersi un'ennupla con lo stesso studente associato allo stesso corso**.==

La **foreign key** invece garantisce che:
==per ogni valore `studente` presente nella tabella `esame`, debba esistere **una corrispondente riga** nella tabella `Studente` con lo stesso valore in `matricola`.==
==E per ogni valore di `corso` in `esame`, debba esistere una riga corrispondente nella tabella `Corso` con lo stesso valore in `nome`==
 
> [!NOTE] **Nota:**
> **Quindi la primary key:** 
> ==impedisce la duplicazione di righe con la stessa coppia `studente, corso`==
> **La foreign key:** 
> ==assicura che lo studente coinvolto sia effettivamente presente nella tabella `Studente`.==
> ==Assicura che il corso coinvolto sia effettivamente presente nella tabella `Corso`==

#### Caso 2: Vincoli di molteplicità massima `1`
Supponiamo di avere un altro diagramma con un vincolo `0..1`:

![[Vincolo di molte max 1.png]]





E se dicessi ora che dal lato studente cambiamo il vincolo da `0..*` a `1..*`?
Per ogni corso deve esserci uno studente che abbia passato l'esame.
Quindi ogni valore della colonna Nome in corso non è più una fk, si mette un vincolo di inclusione che è più debole di una fk, mentre con questo vincolo dico che il nome del corso appare almeno una volta dentro la tabella esame:
```
v. incl (nome) occore in esame (corso)
```

Un vincolo di inclusione è: 
la fk è implementata nel DBMS, mentre questi vincoli non sono implementati vedremo come fare in seguito.
Questo vincolo di inclusione modella il `1..*` dal lato `Studente` e permette di far apparire almeno una volta nel campo nome in esame.
Se mettessimo `1..*` anche accanto a Corso si deve fare la stessa cosa:
```
v. incl (matricola) occore in esame (studente)
```

Adessom concetrimaoci su Docente e Corso
```postgresql
create table Docente(
	cf CodiceFiscale primary key,
	nascita not null
);

-- Questa tabella è l'associazione tra docente e corso
create table insegna(
	docente CF not null,
	corso varchar not null
	FK(docente) ref Docente(cf),
	FK (corso) ref Corso(nome),
	primary key(docente, corso) --in relate è superflua perchè è unico sia il DOcente che il corso perché appare almeno una volta in corso, stessa cosa per corso che appare almeno un volta in questa associazione. Quindi in relate devo fare:
	unique(docente)
	--unique(corso)
	--Quindi non è la coppia a riptersi ma ogni colonna deve avere valori unici. Si potrebbe fare anche:
	--unique (docente)
	primary key (corso)--: questo perché una chiave primaria deve per forza esserci
	--o
	--primary key(docente)
	--unique (corso)
);
```

E se fosse che accanto a studente ci sia un vincolo `0..1` anziché `1..*`? 
In questo caso non può ripetersi il corso, dove c'è un uno massimo come vincolo ignifica che è una chiave:
```postgresql
create table esame(
studente integer not null,
corso varchar not null,
FK (Studente) ref Studente(matricola),
FK (Corso) ref. Corso(nome),
primary key(corso),
);
```

Quindi il vincolo di inclusione sarà:
```plain
v. incl occorre in esame(Studente)
```

E se accanto a Studente mettiamo il vincolo `1..1`, in questo caos non è una chiave perche il massimo dice 1 ma il minimo pure e va letta come una inclusione.
QUindi il vincolo di incl saà:
```
v. incl (nome) occorre in esame(corso)
```

Ma ora noto che corso è una chiave di esame, quindi questo vincolo di inclusione ma è una fk, quindi:
```
FK (nome) ref. esame (corso)
```
Gli 1 minimo diventnato delle fk mentre gli 1 massimo diventano delle chiavi (o unique o primary key).

Adesso mettiamo di avere una classe con attributo `nome:varchar {id1}`

e un classe Studente con attributo `mat:integer {id1}` e `nome:varchar`
Assoc. `iscritto`:
Università → Studente: `Università 1..1{id1}`, `STudente 0..*`.
L'unico modo per includere la primary key sull'assoc iscritto è fare così:
```
create table Studente(
	mat integer not null,
	nome varchar not null,
	università varchar not null,
	primary key (mat, università),
	FK (università) ref Univeristà(nome)
)
```

Ora riprendiamo gli esempi dei vincoli `1..1{id1}`: in questo modo sono obbligato ad accoprpare l'assoc. dentro Studente, quindi è un ereditarietà. 
Se avessimo una diagramma del genere
![[Screenshot 2025-07-14 at 18-38-08 Meet - bmb-xnne-ahh.png]]

In questo modo possiamo identificare uno studente tramite il codice fiscale o il nmero di matricola.

### Accorpamenti

È possibile procedere ad accorpamenti ogni volta che un assoc ha un ruolo a molt. `1..1` o `0..1`.
![[Screenshot 2025-07-14 at 18-39-50 Meet - bmb-xnne-ahh.png]]

In questo caso sono obbligato nella tabella esame nell'accorpare la tabella Studente:
```
create table esame(
studente integer not null,
corso varchar not null,
FK (Studente) ref Studente(matricola),
FK (Corso) ref. Corso(nome),
primary key(corso),
foreign key (Studente, università) ref. Studente(mat,università)
);
```
Un alternativa può essere accorpare esmae in corso:
```postgresql
create table Corso(
	nome varchar primary key,
	studente integer not null,
	univeristà varchar not null,
	FK (studente, univeristà) ref Studente(matricola, università)
	voto Voto -- perchè un corso può non essere associato a uno Studente
		check ((stud is null) = (università is null) = (voto is null))
);
```

Queste due soluizioni sono equivalenti, c'è lo dice lap rpimay key: nella tabella esmae la chiave primaria è corso e viceversa in Corso.
Quindi è più smeplice fare l'accorpamento anziché fare un altra tabella a parte 