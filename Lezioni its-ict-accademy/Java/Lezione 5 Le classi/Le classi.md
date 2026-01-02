Una classe può essere definita con la seguente forma; 
```java
public class NomeClasse
{
	[dichiarazione attributi]
	[definizione metodi]
}
```
Si possono anche scrivere 2 o più classi nello stesso file, ma solo una classe è public (quella che da il nome al file).
Le altre sono visibili nel pacchetto 

In Ecplise se creaimo una classe nella finestra per creare una classe sotto al campo Name ci sono public e package
### Definizione di pacchetto 
Un pacchetto è una directory che ha lo scopo di organizzare i file .class che compongono una libreria 
I veri pacchetti sono i .class, sono organizzatti nelle gemellle di quelle che vediamo nella sorgente.
2 apsetti diversi: 
- Organizzazione logica dei nomi: 
	- ogni package è uno spazio di nomi (namespace) distinto 
- Organizzazione fisica dei file: ogni package è una cartella distinta del disco.
IL pachheyyo java è costituita da solo sotto paccheyti : 
`java.utils`
Il nome di un pacchetto 
- viene esplicitato nella classe (file `.java`) con l'istruzione `package myPackage`
Il nome deve essere univoco: `it.nomePacchetto.nomeClasse`
- deve essere la prima istruzione della classe 
- Il nome deve essere il più possibile uniico 
### Uso dei pacchetti 
Per usare una classe di un pacchetto si usa l'istruzione 
```java
import myPackage.MyClass; 
import java.util.Date
```
Se si crea una classe senza pacchetto su Eclipse viene creato un pacchetto chiamato `(default package)` ma nel file system questo pacchetto non esiste cioè non esiste la directory. La conseguenza è che nessuno può importare la classe senza pacchetto perché ci vuole il percorso completo (es: `java.utils`).
Questo acceade per classi che non sono dentro il pachetto di default 

Regola di java 
- Tutte le classi devono 

#### Attributi di una classe 
Gli attributi si dichiarano: 
```
tipo1 nomeVariabile1; 
tipo2 nomeVariabile2;
```

I tipi possono essere primitivi, cklassi di libreria, classi proprie

Per usare le classi bisonga importalre (salvo se nel default). 
```
import package1.Class1
import package2.*; 

```
Possono essere richiamati utilizzando la notazione 
`nomeOggetto.attributo;`
Ma questo dipende dove lo fai e che visibilità si è messa.
Sebbene questo è possibile per le regole di sint

### Metodi di una classe
I metodi normali sono detti metodi di istanza (come python). 
Possono ricevere da zero a n parametri
Possono ritornare uno o nessun valore: 
- nel primo caso devono dichiarare il tipo di ritorno
- nel secondo dichiaro void
Hanno la seguente forma generale
```java
public/private tipoRitornato nomeMetodo(elenco parametriRicevuti)
{
	dichiarazioni di variabili locali; 
	istruzioni; 
	..................; 
	(return valore); 
}
```

Possono essere richiamati utilizzando la notazione `nomeOggetto.metodo([parametri])`.


## Costruttori e modificatori
Esempio classe Impiegato
2 propieta formali: 
1. Il nome è sempre uguale al nome della classe 
2. Non si specifica il tipo di ritorno (è sempre della classe in costruzione)
3. Ha il compito di valorizzare tutti gli attributi della classe 
```java
public Impiegato (String n, double s, Date d){
	nome = n; 
	salario = s; 
	dataAss = d; 
}
```

Il costruttore come in Python e JS, inizializza gli attributi di una classe, ma in Java se mi scordo di vlorizzare un attributo viene valorizzato di default (come gli array). 
Quindi posso dichiarare un attributo ma non lo inzializzo dentro il costruttore gli viene asseganto un valore di defualt. 
Il `this` qui non vien messo perché i nomi degli attributi inizializzati sono diversi da quelli dichiariati 

### La keyword this 
La keyword this si usa nei metodi per riferirsi all'oggetto chiamante. 
Java consente di chiamare i parametri di un metodo come gli attributi → shadowing, in questo caso è necessario utilizzare this per distinguere gli attributi dell'oggetto dalle variaibli locali al metodo. 
```
public Impiegato(String nome, double salario, Date dataAss){
	this.nome = nome;
}
```

Se nel costruttore non si valorizza un attributo, il compilatore assegna di defualt 
- null per gli oggetti(String compreso)
- false
- \u0000 carattere nullo per i char
- 0 per i numeri
Se non viene scritto nessun costruttore, il compilatore aggiunge un costruttore di defualt : 
- con zero parametri 
- tutti gli attributi settati con i valori di defualt , salvo assegnazioni esplicite 
Il csotruttore di defalut (detto anche di emergenza/disperazione) viene aggiunto al .class quindi non verrà visto dal programmatore nel file della classe ma esiste

### Overloading
In java esiste la possibilità di scrivere metodi con lo stesso nome ma lista di argomenti diversa, questa caratteristica si chiama overloading dei metodi 
Esempio: questi metodi sono validi overloading 
1. `String metodo (int i, Date d)`
2. `String metodo (Date d)`
3. `String metodo (Date d, int i)`
Un metodo di una classe può avere diversi overloading

> [!NOTE] N.B: 
> Nell'overloading il tipo di ritorna non conta → può cambiare, ma è necessario pero cambiare la lista argomenti `double metodo (Date d, int i)` non compila se gia esiste il metodo 3.


