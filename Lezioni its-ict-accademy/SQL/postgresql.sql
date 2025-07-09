-- definizione delle tabella

-- +----------+                            +------------+
-- |Studente  | --0..* -----esame---- 0..* |Corso       |
-- +----------+               |            +------------+
--                            |
--                            

create table Corso(
	codice integer not null,
	nome character varying (100) not null, //dice che questa è una sequenza di 100 caratteri, standrd sql
	aula character varying (10) not null,
	primary key (codice)
);


create table studente(
	matricola integer not null,
	 
	nome varchar not null,
	
	primary key(matricola)
);


create table esame (
	studente integer not null,
	corso varchar not null,
	data date not null,
	-- voto con vincolo di dominio
	voto integer not null
		check (voto>=18 and voto <=30)
	-- if lode = true then voto =30
	lode boolean not null,
		-- vincolo di ennupla:
		-- if lode = true then voto=30
		check (lode = false or voto = 30),
		
		foreign key(studente)
			references studente(matricola)
		foreign key(corso)
			references corso(nome),
		
		primary key(studente, corso)
);