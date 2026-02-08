Abbiamo esaminato le collection ora nadimao a vedere le map.
Le map sono un interfaccia non è collegato all'interfaccia collection, quindi è un inerfaccia a se, questo perchè map ha il doppio generics: <k, v>.
Questo fa intendere che come per i dizionari di Python le map sono strutture dati composte da coppie chiave-valori.
Ricordiamoci che i generics sono comunque oggetti quindi devo specificare i wrapper come Integer per usare un int o un Character per un char. 
Per aggiungere elementi ci sta il metodo `put`: 
- Il primo parametro il tipo della  chiave e il valore 
`put(k,v)`.
Se aggiungessimo un nuovo valore con put con una chiave già esistente entrmabi vengono sovrascritti, per evitare ciò si fa un controllo preventivo tramite `get(k):v`: 
- questo metodo restituisce il valore associato a quella chiave.
La put torna il vecchio valore usente se lo sto sovrascrivendo oppure null.
Un altro metodo `contains(key): boolean`:
- torna un booleano se la chiave è contenuta nel map
un metodo simile è `contains(value):boolean`:
- torna un booleano se il valore è contenuto nel map 
Le map si possono iterare con il for each? No perché map non è parente dell'interfaccia Iterable. 
Ma c'è un metodo che dalla mappa ti tira fuori le collection chiave-valore: `entrySet()`
Torna un set costituito da Entry e l'Entry è costituito dalle coppie chiave-valore.

> [!NOTE]
> Un elemento di una mappa si dice Entry ed è modellato co un oggetto di tipo `Map.Entry<k,v>`.
> Esso rappresenta la coppia Key, Value


Per fare un paragone con SQL, le map in java e i loro metodi estraggo i valori a partire da una chiave (come un `select * from tabella where condizione`).
### Map.Entry
È un in


Un mappa può essere riguardata come: 
- un set di chiavi 
- Collection di valori 
- Set di oggetti chiave-valore
£ viste e 3 metodi: 
Set KeySet(); Collection Values(); Set EntrySet();

Sintassi vecchia: 
```java
Set entries = personale.entrySet();
Iterator iter = entries.iterator();
while (iter.hasNext()){
	Map.Entry entry = (Map.Entry)iter.next
	Object key = entry.getKey();
	Object value = entry.getValue(); 
}
```

Quindi la mappa non è iterabile a meno che non si estrae l'insieme delle Entry.

### Implementazioni
Le classi concrete filgie di map sono: 
- HashMap<K,V>
- TreeMap<K,V>

Un HashMap è per la gestione di Map non ordinati, utilizza Hash Table.
Le chiavi relative agli oggetti della mappa dovrebbero ridefineire il metodo hashCode in modo che: 
- 2 oggetti uguali per equals devono produrre lo stesso hashCode e il metodo equals, per distinguere le chiavi doppie
Per ottimizzare le oparazioni, la struttura dato che lo rappresrnta è un array i cui elemento sono liste, ciascuna lista è un bucket 
Il numero di elementi (buckets) e il dattore 


### Il treemap
È utilizzato per la gestione di MAp ordinati e utilizza una struttura ad albero. 
Le 

