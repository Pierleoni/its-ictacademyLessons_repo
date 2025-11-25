Apriamo accedmia e facciamo 
```
select * from persona
```
e dopo: 
```
select * from assenza 
```

Per trovare tutte le possbile coppie di ennupla di persona e di assenza che hanno l'id della persona che corrisponde al campo persona in assenza
```
select *
from assenza a, persona p 
where p.id = a.persona 
```

Ma se io volgio tutte le persona che hanno fatto almento una assenza metto il distinct 
```sql 
select distinct p.id, a.persona 
from assenza a, persona p
where p.id = a.persona 
```

Mentre se volgio contare quante ennuple ci sono in ogni gruppo. 
```
select persona, count(*)
from assenza
group by persona
```

Prendi la tab persona, fai tanti gruppi di ennuple dove due ennuple vanno nello stesso gruppo se hanno valori simili per ciascun gruppo.

Adesso volgiamo filtrare via tutti i gruppu che hanno il count <=1: 
```postgresql 
select persona, count(*)
from assenza 
group by persona 
having count (*)>1 
```


> [!NOTE] Title
> select seleziona le ennupla del campo persona 
> from assenza: dalla tabella assenza
> gruop by: fa i gruppi
> `having count(*)>1`: è la condzione è sul gruppo, difatti sto contando il gruppo che almeno una ennupla 

Adesso raggrupimao per tipo in assenza 
```
select tipo, count(*)
from assenza 
group by tipo
```

Se volgi tutti i tipi di assenza che sono stati fatti almeno 3 volte 
```
select tipo
from assenza 
group by tipo
having count(*)>=3 
```

```postgresql
select *
from persona p, assenza a 
where p.id = a.persona 
```

```
select p.posizione, count(*)
from assenza a, persona p 
where a.persona = p.id 
group by p.posizione; 
```

E se volgio le posizioni che hanno almeno 3 persone che hanno fatto un assenza
```postgresql
select p.posizione, count(*)
from assenza a, persona p
where a.persona = p.id 
group by p.posizione 
having count(*)>2
```



> [!NOTE] Title
> where si applica ad ogni singola ennupla


ad esempio:
```
select p.posizione, count(*)
from assenza a, persona p
where a.persona = p.id and count(*)
```