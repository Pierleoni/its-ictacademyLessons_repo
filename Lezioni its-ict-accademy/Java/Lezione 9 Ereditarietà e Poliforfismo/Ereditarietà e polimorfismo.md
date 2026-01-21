## Concetto di ereditarietà
È uno dei punti di forza di Java e dell'OOP 
Infatti consente di: 
1. Massimizzare il riutilizzo del codice 
	- divide gli aspetti da quelli specifici 
	- Quindi se una Persona ha competenza sul proprio dominio riesce a classificare questi elementi in classi e sottoclassi 
Quindi quando faccio le classi e le relative sottoclassi stiamo suddividendo gli elementi del dominio in un elemento generico in sotto elementi più specifici. 
2. Predisporsi facilmente ad evolutive
	- Aggiunge funzionalità, non comporta modifiche al codice preesistente
### Definizione 
L'ereditarietà consente di creare nuove classi che riutilizzano, estendono e modificano(overriding) il comportamento definito di altre classi. 
Le classi i cui membri vengono ereditati è denominanta classe base (o classe padre), mentre la classe che eredita i membri è denominata classe derivata (o classe figlia). 
Si dice super classe perchè nei diagrammi si disegna sopra alla sotto classe. 
Questa gerarchia di delle classi padre-filgie si estende alla classe figlie che a loro volta possono diventare genitori, 

### Esempio 1 : dividere apsetti generali e specifici 

Volendo ottimizare il diagramma si può creare una classe Persona più generale che conterra struttura 


### Esempio 2: 
Abbiamo una classe Impiegato che modella il dipendente di una azienda 
In seguito nasce l'esigenza di modellare i manager: 
- dispongono di una segretaria e prevedono una implementazione del metodo `incrementaSalario`. 
Quindi per implementare questa cosa ci sono 3 metodi: 
1. Fare un copia incolla da Impiegato a mangere
2. Fondere le due classi , aggiungendo un primitivo(stringa, booleano) o un enumerativo
3. Implementare la nuova classe `Manager` verrà allora creata come evoluzione di classe Impiegato: 
	- Erediterà i memebri dell'Impiegato
	- Aggiungera i nuovi membri 
	- Evolvera il metodo incrementaSalario; 
		- Ovvero la classe Manager deve sovrascrivere il metodo del padre per "aggiustarla" per le necessita del figlio 

> [!NOTE] La segreteria potrebbe essere una classe figlia di Impiegato, ma per comodità la segretaria è un attributo di Manager di tipo stringa. 


Immaginaimo l'ovverriding dei metodi come fare l'aggiornamento di un applicativo su SO: cancelliamo la vecchia realese sovrascrivendola con la nuova realese. 


### Sottocategorie
La relazione tra classi e sottoclassi è la relazione `is-a` e induce a vedere insieme e sotto insiemi di oggetti. 
Esempio: 
Se un Cane e Gatto sono sottoclassi di Animale, allora un cane (e ovviamente anche un gatto) sono particolari animali
Se smonto una delle sottoclassi il padre non se ne accorge e il fratello non sa neanche che esiste la classe siblings, viceversa se smontiamo il padre dobbiamo smontare anche le sotto classi.

## Sintassi 
Per definire una sottoclasse si utilizza la seguente sintassi: 
```java
public class SottoClasse extends SuperClass(...)
```

La parola riservata extends indica che la nupva classe perfeziona - specializza - estende un altra gia esistente

### Il costruttore 
I costruttori della superclasse non si ereditano nel eseno stretto del temrine: perché la sottoclasse eredita tutti gli attributi e i metodi del padre esculso il costruttore. 
Quindi i costruttori della superclasse DEVONO essere richiamati nel costruttore dellla sottoclasse con la sintassi 
```java
super([lista di parametri])
```

La chiamata a super deve essere la prima istruzione del costruttore della sottoclasse (poi ci sono le istruzioni specifiche). 
Esempio: 
Se il manager ha un sttributo secretaryName allora scriviamo 
```java
private String secretaryName; 
public Manager (String n, double, s, Date, d, String ns)
{
	super (n, s,d); //prima istruzione
	secretaryName = ns; //istruzione specifiche
}
```

Il figlio quanti costruttori devi avere? Dipende da quello che deve fare il figlio. 

Se non scrive alcun costruttore, il compilatore aggiunge quello di defualt con la chiamata a
```java
super(); // zero parametri
```

Nell'esempio del Manager sarebbe: 
```
public Manager()
{
	super(); 
	secretaryName = null; 
}
```

Se la superclasse: 
- ha il costruttore a zero parametri, questo viene invocato 

```java
public class Manager extends Impiegato{
	private String segretaria; 
	public Manager (String nome, Date dataAssunzione, double salario, String segreataria){
		super (nome, dataAssunzione, salario)
		this.segretaria = segretaria
	}
}
```


### Overriding dei metodi 
Si realizza quando la sottoclasse sovrascrive, quindi modifica /evolve, un metodo ereditato dalla superclasse 
La sottoclasse quindi sostiuisce la "vecchia" versione del metodo (della superclasse) con una nuova versione 


#### Gerarchia dell'ereditarietà 
Tutte le classi ereditno per deafualt dalla classe Object
tutte tranne Object stessa. 
La classe `java.lang.Object`:
- radice di tutte le classi 
- superclasse di tutte le classi 

### Virtual Method invocation 
La virtual method invocation è azione della macchina virtuale Java(JVM)
Consiste nell’invocazione della versione corretta di un metodo sovrascritto, tenendo in considerazione la natura dell’oggetto chiamante e non la sua reference