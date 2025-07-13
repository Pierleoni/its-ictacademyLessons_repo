
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

