
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

#### Caso 2: Vincoli di molteplicità massima `1` in un'associazione
Supponiamo di avere un altro diagramma con un vincolo `0..1` solo da un lato dell'associazione:

![[Vincolo di molte max 1.png]]

l’associazione `insegna` collega le entità `Docente` e `Corso`, con vincoli di molteplicità:

- `Docente` → `0..*`
    
- `Corso` → `0..1`
    

#### ➤ Interpretazione:

- **Un docente può insegnare a un corso o nessuno.**
    
- **Un corso può essere insegnato da più docenti o da nessuno.**
    

Poiché sul lato `Corso` la molteplicità massima è **1**, ciò significa che **non si possono avere due tuple con lo stesso `corso` nella tabella `insegna`**.  
==Ne segue che `corso` è **chiave** (univoco) nella tabella `insegna`.==
```postgresql
CREATE TABLE insegna(
	docente integer primary key, 
	corso varchar, 
	da Date,
	foreign key docente references Docente(matricola)
	foreign key corso references Corso(nome)
);
```
Quindi in questo caso la chiave primaria sarà solo `docente` poiché è coinvolta nel link di associazione `insegna` con molteplicità massima pari a `1` (`0..1`).
##### Variante: Molteplicità massima `1` da entrambi i lati 
Ipotizziamo invece una variante di questo caso ovvero: 
Il vincolo di molteplicità `0..1` viene messo su entrambi i lati  
![[Variante caso 2.png]]

 **Interpretazione:**

- **Un docente può insegnare al più un corso.**
    
- **Un corso può essere insegnato da al più un docente.**

Ora sia `Docente` che `Corso` partecipano ai link di associazione `insegna` con i vincoli di molteplicità massima pari a `1`.
Allora si può scegliere **uno dei due campi** (`docente` o `corso`) come chiave primaria, e sull’altro definire una **UNIQUE constraint** per garantire l’univocità:
```postgresql
-- tabella insegna con chiave primaria corso
CREATE TABLE insegna(
	corso varchar primary key, 
	docente integer,
	unique (docente),
	foreign key docente references Docente(matricola),
	foreign key corso references Corso(nome)
	
);

-- tabella insegna con chiave primaria il campo docente
CREATE TABLE insegna (
	docente integer primary key,
	corso varchar,
	unique (corso),
	foreign key docente references Docente(matricola),
	foreign key corso references Corso(nome)
)
```

Entrambe le implementazioni **riflettono correttamente il vincolo UML**, e sono **equivalenti dal punto di vista semantico**.


> [!info] **Nota:**
> Quando in un’associazione la **molteplicità massima è 1**, ==ciò implica **un vincolo di univocità** che si riflette nella **definizione della chiave primaria o di una chiave alternativa** nella tabella di associazione.==


#### Caso 3: Vincolo di molteplicità minima `1` in un'associazione (`1..*`)
Ipotizziamo di avere un diagramma dove su un lato dell'associazione vi sia un vincolo di molteplicità uno a molti (`1..*`):
![[Vincolo di molteplicità minima 1.png]]
Nel seguente schema:

l’associazione `insegna` collega le entità `Docente` e `Corso` con vincoli di molteplicità:

- `Docente`: `0..*`
    
- `Corso`: `1..*`
Interpretazione:
- Un corso può essere insegnato da almeno un docente o da più docenti (`1..*`)
- Un docente può insegnare a più corsi o a nessun corso (`0..*`).
==l vincolo `1..*` dal lato `Corso` implica che **ogni corso deve comparire almeno una volta nella relazione `insegna`**, ossia **deve essere insegnato almeno da un docente**.==

Poiché questo tipo di vincolo **non è garantibile mediante i meccanismi standard di chiave esterna (foreign key)**, si ricorre a una **specifica logica dichiarativa**, detta **vincolo di inclusione**.
==Il vincolo di inclusione è una generalizzazione di vincolo di foreign key, ma gli attributi della tabella di destinazione non formano una chiave.==
```postgresql
-- v. inclusione: Corso(nome) occorre in insegna(corso)
```
Difatti il vincolo di inclusione è più debole di una foreign key ==ma permette di dire che il campo `nome` in `Corso` appare (occorre) almeno una volta nel campo `corso` in `insegna`.== 
Questo **non è un vincolo di foreign key** (che impone un'inclusione inversa), bensì la sua **generalizzazione**, ==e serve a **garantire la partecipazione obbligatoria** all'associazione.== 

Poiché il DBMS **non supporta nativamente questo vincolo**, lo si **documenta** nella definizione della tabella, come segue:

```postgresql
CREATE TABLE Corso(
	nome varchar primary key,
	modalita ENUM, 
	-- v. inclusione: Corso(nome) occorre in insegna(corso)
);

CREATE TABLE insegna(
	docente integer,
	corso varchar,
	primary key (docente, corso)
	foreign key docente references Docente(matricola),
	foreign key corso references Corso(nome)
);
```


> [!abstract] **Osservazione semantica**
> Il vincolo di inclusione **è concettualmente più debole di una foreign key**>
> esso garantisce solo che **ogni valore in `Corso(nome)` compaia almeno una volta in `insegna(corso)`**, ma **non viceversa** (cioè in `insegna(corso)` possono apparire anche corsi non più presenti in `Corso` — a meno che non vi sia anche una foreign key, come in questo caso).

##### Variante con vincoli di molteplicità minima `1`
Ipotizziamo una variante in questo caso, ovvero il vincolo `1..*` viene posto a entrambi i lati dell'associazione:
![[Variante vinc. di molt. min. 1.png]]

Nel seguente schema:

l’associazione `insegna` collega le entità `Docente` e `Corso` con vincoli di molteplicità:

- `Docente`: `1..*`
    
- `Corso`: `1..*`

**Interpretazione:**
- Un docente può insegnare ad almeno a un corso.
- Un corso può essere insegnato da almeno un docente

In tal modo, **l’associazione `insegna` non è facoltativa per nessuna delle due entità**: ciò impone che **i valori di `Docente.matricola` e `Corso.nome` debbano sempre comparire almeno una volta nella tabella `insegna`**.

Per rappresentare questa obbligatorietà nella **traduzione relazionale**, dobbiamo specificare due **vincoli di inclusione**:
- ==`Docente(matricola)` **deve apparire almeno una volta** in `insegna(docente)`==
    
- ==`Corso(nome)` **deve apparire almeno una volta** in `insegna(corso)`.==

Come già detto in precedenza, questi vincoli, tuttavia, **non possono essere implementati direttamente dal DBMS** tramite costrutti standard. Devono pertanto essere **documentati** come commenti strutturali nel codice SQL.
```postgresql
CREATE TABLE Docente (
	matricola integer primary key, 
	nome varchar not null,
	genere Genere not null
	-- v. inclusione: Docente(matricola) occorre in insegna(docente
);

CREATE TABLE Corso(
	nome varchar primary key,
	modalità Modalità not null
	-- v. inclusione: Corso(nome) occorre in insegna(corso)
);


CREATE TABLE insegna(
	docente integer,
	corso varchar,
	primary key(docente, corso),
	foreign key docente references Docente(matricola),
	foreign key corso references Corso(nome)
);
```



In questo caso per far rispettare il vincolo `1..*` sia sul lato

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

#### Caso 4: caso speciale di vincoli di molteplicità `1..1` in una associazione
Si consideri il caso in cui, in un’associazione binaria, sia presente un **vincolo di molteplicità `1..1`** su uno dei due lati:
![[Vincoli di molt. 1..1.png]]

Nel seguente schema:

l’associazione `insegna` collega le entità `Docente` e `Corso` con i seguenti vincoli di molteplicità:

- `Docente`: `0..*`
    
- `Corso`: `1..1`

**Interpretazione:**
- **Un docente può insegnare anche più corsi** o nessuno.
    
- **Un corso deve essere insegnato obbligatoriamente da un solo docente**.
In questo caso, l’associazione è **funzionale da `Corso` a `Docente`**, ovvero **ogni corso è assegnato a un solo docente**, ma **un docente può insegnare più corsi**.
Questa situazione si traduce **non con una tabella dell’associazione**, ma integrando l'associazione direttamente in una delle due tabelle, ossia **portando la chiave dell'entità `Docente` (lato `0..*`) come chiave esterna nella tabella `Corso`** (lato `1..1`):
```postgresql
CREATE TABLE Docente (
    matricola INTEGER PRIMARY KEY,
    nome      VARCHAR NOT NULL,
    genere    Genere NOT NULL
);

CREATE TABLE Corso (
    nome     VARCHAR PRIMARY KEY,
    modalità Modalità NOT NULL,
    docente  INTEGER NOT NULL,
    FOREIGN KEY (docente) REFERENCES Docente(matricola)
);
```


> [!remember] **Riflessione sui vincoli**
> 1. Vincolo di molteplicità minima `1`:
> Se accanto a `Corso`  poniamo il vincolo `1..1`, ==il minimo `1` comporta che il valore **debba comparire** nell’associazione (in questo caso tradotta nella tabella).==
> Questo si traduce in un vincolo di inclusione:
>
>```postgresql
>-- Il docente associato a un corso deve esistere
>FOREIGN KEY (docente) REFERENCES Docente(matricola)
>```
>2. Vincolo di molteplicità massima `1`:
>==Il massimo `1` comporta che il valore non possa essere ripetuto più volte nell’associazione.==
>
> In questo esempio, poiché `corso.nome` è **la chiave primaria**, ogni corso compare una sola volta, e dunque **la funzione da corso a docente è automaticamente garantita**.
> 
>Se invece il caso fosse invertito (cioè il docente fosse sul lato `1..1`), avremmo dovuto usare un vincolo `UNIQUE` per garantire l’unicità.
>> [!example] **In sostanza**
>> Integrare i vincoli di molteplicità minima e massima nella progettazione relazionale è fondamentale per **preservare la semantica del modello concettuale**. In particolare:
>>
>>- ==Il **minimo `1`** si traduce in una **foreign key not null**==.
  >>  
>>- ==Il **massimo `1`** si traduce in una **unicità**, talvolta una **primary key**, a seconda dei casi.==



> [!ticket] **Quando in un’associazione UML compare il vincolo di molteplicità `1..1` su un lato**, la **metodologia di traduzione nel modello relazionale** prevede di **non trattarlo come vincolo di inclusione separato**, ma piuttosto di **implementarlo direttamente come vincolo di integrità referenziale (foreign key)**, **nella tabella corrispondente alla classe concettuale che porta il vincolo `1..1`**.

### Accorpamenti

Adesso mettiamo di avere una classe con attributo `nome:varchar {id1}`

e un classe Studente con attributo `mat:integer {id1}` e `nome:varchar`
Assoc. `iscritto`:
Università → Studente: `Università 1..1{id1}`, `STudente 0..*`.
L'unico modo per includere la primary key sull'assoc iscritto è fare così:
```sql
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