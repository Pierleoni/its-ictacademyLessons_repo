# Interfacce Funzionali e espressioni Lambda
Java sotricamente nasce come linguaggio OOP in contrapposizione con il paradigma del tempo(funzionale).
La programmazione ad oggetti pone al centro dell'attenzione l'oggetto come dato condiviso e mutabile.
Elementi come metodi o classi sono consdierati accessari necessari alla manipolazione degli oggetti, cioè elementi secondari.
Ci sono delle situazioni in cui si è costretti ad usare una logica ad oggetti più vicina alla logica funzioanle, l'esempio è il `TreeSet`.
Il TreeSet è una collection ordinabile di elementi(a differenza del HashSet dove l'ordinamento è intrinseco e il programmatore non può deciderlo).
Il TreeSet ricodriamo che ha due costruttori: 
`TreeSet<E>()`
e 
`TreeSet<E>(Comparator)`.
Ricodriamo che comparator è un interfaccia quindi per istanziare un comparator dobbiamo istanziare una sottoclasse es; `MarcaComparator`.
Quindi dobbiamo istanzare il MarcaComparator: 
```java
TreeSet<Prodotto>t = new TreeSet<>(new MarcaComparator());
```

La lambda expression semplifica questo giro perché permette di dire l'essenziale.
Una lambda expression è come un operatore ternario: l'operatore ternario è un if-else compatto stessa cosa le lambda expression sono delle funzioni anonime che come in Python e in JS (le arrow function) permettono di scrivere funzioni anonime e compatte
### Esempio
Supponimao di voler scrivere un metodo che filtra su una collezione in base a un certo criterio: vogliamo filtrare mele in base al colore ed anche in base al loro peso.
Si dovrebbero scrivere in 2 metodi speratai: 
```java
public static List<Mela>filtraMelePerColore(List<Mela> cassetta){
	List<Mela> listaFiltrata = new ArrayList<Mela>();
	for (Mela m:cassetta){
		if(m.getColore().equals("verde")){
			listaFiltrata.add(m);
			
		}
		return listaFiltata;
		
	}
}
```

```java
public static List<Mela> filtraMelePerPeso(List<Mela> cassetta){
	List<Mela> listaFiltrata = new ArrayList<Mela>();
	for (Mela m:cassetta){
		if (m.getPeso()>150){
			listaFiltrata.add(m);
			
		}
		return listaFiltata;
	}
}
```


### Predicato
Il `Predicate` è un interfaccia che fa lo stsso lavoro della nostra interfaccia Criterio. 
Tuttavia il nome è fuorviante ma fa lo stesso lavoro.
```java
public static List<Mela> filtraMele(List<Mela> cassetta, Predicate<Mela> p){
	...
}
```
Ora con le lambda expression può essere invocata seconda 


### Elementi chiave 
3 elementi chisve: 
1. Functional Interface → un interfaccia che contienen un solo metodo astratto (per esempio potrebbero essere un predicato `Predicate<T>` di Oracle oppure un altra interfaccia personalizzata)
2. Behavior parameterization → metodo che accetta come argomento un comportamento.
3. Lambda Expression → nuova sintassi (per l'invocazione) che passa una funzione in alternativa all'oggetto che implementa l'interfaccia
```java
piblic interface Predicate<T>{
	...
}
```

```java
public static void esegui(String obj, Predicate<String> p){
	System.out.println(p.test(obj));
}
```

```java
esegui("ciao",(String s)→ s.length()>3);
```

Il predicate restituisce un booleano.



### Interfacce funzionali nelle collection
Da java 8 sono disponibili nel framework delle Collection alcuni metodi di defualt (già concretamente implementati), che utilizzano le interfacce funzionali.
I metodi sono cosi assegnati: 
- Iterable → forEach(Consumer)
- Collection → removeIf(Predicate)
- List → 
	- replaceAll(UnaryOperation)
	- sort(BiFunction)
	- 