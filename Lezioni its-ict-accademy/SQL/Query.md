
### Interrogazioni su tabella singola
prendo tutte le ennuple sulla tabella che soddisfano quella condizione
```postgresql
set timezone to "Europe/Rome"
select * from attivitaprogetto
where giorno >current_date - interval '5 year';

select current_timestamp + interval '18 minute 14 second 3 millenium';
```

Tutte le operazioni cioè le interoggazioni si fanno nel blocco select, quindi se si vuole un operazione tra dati che stanno nel DB o nella query queste operazioni stanno nel select.

Voglio sapere tutti le persone che stanno in assenza:
Se interrogo solo la tabella assenza mi reistutuisce l'id della persona, quindi devo fare una query che coinvolgono più tabelle.

![[Screenshot 2025-07-11 at 13-04-14 Meet - bmb-xnne-ahh.png|500x243]]

Il primo passo di quando si implementa un interrogazione e cercare dove stanno i dati e si fa cosi:
```
select Officina.indirizzo
from Officina 
where Officina.nome ='FixIt'
```

Facciamolo su Persona 
```postgresql
select *
from persona, assenza
```
Crea una tabella fusa ma come? 
Fa il prodotto cartesiano, ovvero l'insieme di tutte le coppie.

Esempio:
La tabella A ha la colonna x,y dove in x ci sono i valori a,b,c e la colonna y ha i valori d,e,f.
La tabella B ha i campi j e k che contengono rispettivamernte i valori g,i,m e h,l,n
In questo caso il prodotto cartesiano tra queste due tabelle, ovvero crea un nuova tabella con utte le possibile coppie tra ennuple: la prima coppia di ennupla della prima * la seconda coppia della seconda tabella 
![[Screenshot 2025-07-11 at 13-11-26 Meet - bmb-xnne-ahh.png|500x257]]In questo caso associa ogni perosna con ogni assenza, ma ad esempio accopia l'assenza 0 della persona 10 ad anna bianchi il cui id è 0.
Noi volgimao avere solo ennuple tra persona e assenza dove l'assenza corrisponde alla perosna:
```postgresql
select *
from persona, assenza
where persona.id = assenza.persona
```

Quindi adesso nella tabella l'id della persona corrisponde all'id dell'assenza. 
senza la condizione where come abbiamo visto l'assenza venti è associata alla persona 10.

QUante ennuple ha questa tabella? QUesta tabella ha tante ennuple quante sono l'assenza, ovvero ci possono essere tante assenze ma sono legate alla stessa persona
```
select assenza.id, tipo.giorno, persona.nome, persona.cognome
from persona,assenza
where persona.id = assenza.id
```

E se voglio i nomi e i cognomi delle persone che hanno fatto le assenze
```postgresql
select persona.nome, persona.cognome
from persona,assenza
where persona.id = assenza.id
```

E se una persona ha fatto più assenze o almeno una e voglio vedere solo il suo nome una sola volta?
```postgresql
select distinct persona.nome, persona.cognome
from persona,assenza
where persona.id = assenza.id
```

Nel primo caso una ennupla su unidici non ha senso, il flusso è:
prima viene eseguita la from che fa il prod cartesiano, poi viene eseguita la `where` e vengono sclete solo le ennuple che rispettano il `where` e dopo viene eseguito il `select` e per ultimo viene eseguito il `distinct`.

Se la tabella Persona contiene un miliarod di ennuple e la tabella video un miliardo di ennupla quant'è il prodotto? ovviamente sql e il DBSM non fa questo tabellone, ma noi ragionaimo come se facesse esattamente questo poi ovviamente il DBMS ottimizza.


Anziche scrivere tutto si possono dare degli alias:
```
select o.indirizzo
from 
```


### Occorenze multiple di una tabella 
Esercizio:
restituire una tabella si nomi e cognomi delle persone che hanno fatto almeno due assenze.
Ad esempio:


![[Screenshot 2025-07-11 at 13-30-05 Meet - bmb-xnne-ahh.png|500x176]]

Come faccio a dire che andrea verona ha fatto almeno due assenze? Dovrei avere due righe, ma la cond where è una cond sulla singola ennupla.

Una soluzione è :
```postgresql
select persona.nome, persona.cognome 
from persona, assenza
where persona.id = assenza.persona
group by persona.id, persona.nome, persona.cognome
having count(*)>1
```

un altra è:
```
--select * 
---select p.nome, p.cognome 
select distinct p.nome, p.cognome 
from persona p, assenza a, assenza b
where p.id = a.persona and p.id = b.persona and a.id <> b.id
```




## Funzioni aggregate

Cos'è? 
Prende una tabella e calcola un solo valore,
Calcola un singolo valore a partire da tutte le ennuple, il risultato è una tabella con una sola ennupla.
Esempio:
Restituire l'elenco che hanno riparato il veicolo 'HK 243 BW'
```
select officina
from riparazione
where veicolo = 'HK 243 BW'
```
Con le funzioni aggregate:
```postgresql
select count ( ∗ )
from Riparazione
where veicolo = ’HK 243 BW’
```

Se voglio prende 

`count(*)`: conta il numero di ennuple
`count( attributo )`: numero di valori non `NULL` per l’attributo (con
duplicati)
`count( distinct attributo )`: numero di valori non `NULL` e distinti
per l’attributo

Esempio :

```
select * 
from arrpart 
where comp = 'MagicFly'

select count(*)
from arrpart
where comp = 'Apitalia'
-- Output: count 5
```

Se volgio sapere quante compagnia hanno un volo che parte da FCO?
```
select count (distinct comp)
from arrpart
where partenza = 'FCO';

```

Quante tratte distinte ci sono da fiumicino?
```
select count (distinct (partenza, arrivo))
from arrpart 
where partenza = 'FCO';
-- Output: count 2
```

Voglio sapere quati aeroeporti ci sono a ROMa?
```
select count (*)
from luogoareoporto
where citta = 'Roma';
```

Una query con un semplice aggregato restituisce un valore, il valore è una tabella con una colonna count e con una ennupla con il valore.
E per forza una sola riga perchè l'aggregato prende tutte le righe e le colassa in una sola.


```
select  * 
from compagnia 
where annoFond is null;

select *
from compagnia
where annoFond is null
```

Le altre funzioni aggregate
sum(): prende le ennuple ma vuole un attributo, somma su domini numerici o tempi 
posso sommare intervalli, dati e numeri 
```
select interval '1 year' + interval '3 day';
```

Ma non posso fare la concatenazione delle stringhe con il sum

AVG(attributo); media artimetica

min e max funzionano su tutti i domini che hanno un numero ordianto pure sulle stringhe:
```
select sum (annofondaz), avg(annoFondaz)
from compagnia;
```

I null li ignora
Avg restituusce un numero reale per abbelirlo:
```
select sum (annofondaz), round(avg(annoFondaz),2)
from compagnia;
```

Posso fare anche il min e il max dell 'anno di fondazione e il nome della comapginia
```postgresql
select sum (annofondaz), round(avg(annoFondaz),2), min (annoFond), max(annoFond), min(nome)
from compagnia;
```

I vlaori null vengono sempre ifgnorati delle funzioni aggregate

Vediamo su accademia:
Voglio fare lo stipendio medio dei ricercatori:
Facico la tabella dei ricercatori e dopo faccio la media degli stipendi
```
select * 
from persona
where posizione = 'Ricercatore'

select avg(stipendio)
from persona
where posizione = 'Ricercatore'

-- oppure

select sum(stipendio/count(*))
from persona
where possizione = 'Ricercatore'
```

Il secondo metodo pero ha un problema: da la divisione per zero 
esempio:
```
select avg(stipendio)
from persona
where posizione = 'Ricertaore'
```

SI possono mettere insieme ma ogni funzione aggregata calcola il suo valore.

Questa query:
```
select nome, round(avg(stipendio))
from persona
where posizione = 'Ricercatore'
```

COme si comporta, ricodridiamo che le tabelle sono rettangoli, ma questa tabella non è un rettangolo perche deve mettere tanti nomi con un solo valore.
Inoltre nella target list (select) non possono apparire agreggati insieme a non aggregati.
Gli operatori aggregati per ora appiono solo nella select.

Quindi la regola è che la target list deve essere sempre omogenea, quindi una query con solo attributi va bene e una query con solo aggregsati va bene 

Esercizio: 
Quanti sono i voli che partono dalla città 'Roma' e durano almeno 180 minuti?
Ragioniamo di trovare i voli che partono da Roma e che durano almeno 180 minuti:
Mi serve `volo`, `arrpart` e `LuogoAeroporto`
```
select *
from volo v, arrpart a,  LuogoAeroporto l;
```

Le ultime tre colonne sono di luogoaeroporto e devo dire che il luogo aeroporto deve stare a Roma:
```
l.città = 'Roma'
```

Ma non ho risulto nulla, quando associo un volo e un luogoaeroporto il luogo deve essere l'areoporto di partenza del volo:
```
select *
from volo v, arrpart a,  LuogoAeroporto l
where l.città = 'Roma'
and v.durata_minuti >= 180
and a.partenza = l.codiceIATA
```

Una nennupla deve parlare di un volo
```
select *
from volo v, arrpart a,  LuogoAeroporto l
where l.città = 'Roma'
and v.durata_minuti >= 180
and a.partenza = l.codiceIATA
and v.codice = a.codice and v.comp = a.comp
```

Questa è la tabella arrpart, ma accanto a ogni volo in arrpart da un lato ho messo le info sulla tabella volo e dall'altro le info sull'aereporto di partenza.
Volgio anche mettere le info sull aereoporto di arivo?
```
select *
from volo v, arrpart a,  LuogoAeroporto l
where l.città = 'Roma'
and v.durata_minuti >= 180
and a.partenza = l.codiceIATA
and v.codice = a.codice and v.comp = a.comp

```

Adesso che ho la tabella metto il count:
```
select count(*)
from volo v, arrpart a,  LuogoAeroporto l
where l.città = 'Roma'
and v.durata_minuti >= 180
and a.partenza = l.codiceIATA
and v.codice = a.codice and v.comp = a.comp
```



```postgresql
select count(*) 
from volo, LuogoAeroporto, arrpart
where volo.durata_minuti >= 180
and LuogoAeroporto.città = 'Roma' and luogoaeroporto.codiceIATA = arrpart.partenza
and volo.codice_volo = arrpart.codice;
```

In questo caso non va usato l'operatore `IN` poichè adesso gli Aereoporti a Roma sono FCO e CIA ma se venisse costruito un nuovo aereoporto a Roma dovrei cambiare la query, mentre invece le query devono rimanenre corrette sempre.

Qual'è la durata media dei voli della compagnia 'Apitalia'?

```
select *
from volo
```

Mi servono le ennuple di Apitalia 
```postgresql
select *
from volo
where comp = 'Apitalia'
```

Dopodiché mi serve la media della durata dei minuti
```postgresql
select avg(volo.durata_minuti)
from volo
where comp = 'Apitalia'
```

