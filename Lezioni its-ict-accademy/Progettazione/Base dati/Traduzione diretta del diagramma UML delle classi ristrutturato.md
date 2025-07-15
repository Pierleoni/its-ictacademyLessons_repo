La metodologia vuole che goni classe del diagramma sia una tabella, le associazioni possono essere altre tabelle o accorpate ad altre tabelle, i vincoli di molte diventano foreign key, chiavi etc.

### Le classi

Partiamo da `Studente` 
![[Screenshot 2025-07-14 at 17-56-22 Meet - bmb-xnne-ahh.png]]

Quindi sostituire i tipi di dato con tipi di dato compatibili in PostgreSQL.
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

Ora mettiamo che nel diagramma tra l'associoziazione tra `Studente` e `Corso` ci sia una association class `esame` con attributo `voto:Voto`, anche qui dobbiamo fare una tabella
```postgresql
create table esame(
studente integer not null,
corso varchar not null,
FK (Studente) ref Studente(matricola),
FK (Corso) ref. Corso(nome),
primary key(studente, corso),
);
```

La primary key in questo caso è la coppia `studente, corso` perché non può ripetersi un ennupla con lo stesso studente associato allo stesso corso.
La fk dice che Per ogni valore studente in esame deve apparire nella colonna matricola in `Studente`(non possono esistere due righe con la stessa coppia di valori).
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