Abbiamo visti i modificatori di accesso: 
ovvero quelli che permettono la visibilita delle classi e dei loro attributi: 
- private : per gli attributi privati 
- public : per le classi e sui metodi di classe 
- protrected: 
- e l'impostazione predefinita 
Questi ultimi due metodi sono poco utilizzati per chi fa applicazioni commericiali eccetto per chi sviluppa livbrerie Java. 

Altri due modificatori aggiuntivi sono: 
1. Static 
2. Final 
Possono essere usati entrambi, separati o nessuno dei due. 
### Esempio: classe Impiegato 
Vogliamo rappresetnate un impiegato che deve avere i seguenti attributi: 
nome : String
salario: double
dataAssunzione: Date

Nel [[Analisi dei requisiti mediante UML|diagramma UML]] verra visualizzato cosi: 
![[ImpiegatoJava.png]]


Il modificatore final consente di dire che un modificatore(attributo) non cambia nel tempo. 
L'ultimo metodo, `incrSalario: void` aumenta il salario.
Quindi nel costruttore 

### Teorema delle classi 
Tutte le classi hanno ALMENO un costruttore
Se non viene scritto nessun costruttore, viene aggiunto quello di default 
Quindi una classe può avere più di un



### Note sui costruttori 
Java permette una sola chiamata a un cosruttore al momenti della referenzazione dell'oggetto 

```java
public Impiegato (String nome, double salario, Date data){
	this.nome = nome; 
	this.salario = salario; 
	this.dataAss = data; 
}

// costruttore di Impiegato con data Odierna 
public Impiegato (String nome, double salario){
	this (nome, salario, new Date())
}
```

Il `this` del secondo costruttore interno della classe sta richiamando il primo costruttore all'interno della stessa classe (diverso dal super che eredita dalla superclasse). 

### Modificatori 
I modificatori descrivono le proprietà di un entità (classe/metodo/attributo) relativamente a: 
- visibilità: 
	- private 

modificabilità: 
- final: specifica che l'entità non può essere modificata 
- Il suo vlaore non può cambiare nel costruttore
- Ad esempio l'attributo nome di impiegato se è final il nome non può cambiare; non evolve. 
- La finezza di aggiungere final è che final è una protezione: appena si mette final il compilatore capisce che per quel'attributo non possono essere implementati i getter e i setter dell'attributo 

Appartenanza ad una classe: 
- static: specifica l'appartenenza alla classe e non agli oggetti 

### Static
Si puo mettere sulla classe, sull'attributo e sul metodo.
Static va sulle classi se sono inner class
I meotdi statici sono: 
prendiamo ad esempio `Math.pow(2,3)`, questo metodo prende 2 parametri e ne ritorna uno. 
IL metodo statico è un metodo che non ha bisogno di un oggetto per essere invocato (stessa cosa per gli i metodi JS come `Math.floor()`, `Math.random()`).
Questo ovviamente ha senso per metodi matematici, MAth ha tutti meotdi statici con un costruttore privato. 
Nella libreria di Java ci sono alcuni metodi statici(sono un 10%).

La viaribile statica: se dichiaro unattributo static nella classe vuol dire che c'è un solo attributo uguale per tutti gli oggetti della classe. 
Quindi la variabile statica c'è ne una sola ed è condivisa con tutti gli oggetti.
Esempio pratico: 
Ad esempio in un corso ci sono delle sedie per tutti gli studenti, ma la stanza dove si tengono le lezoni è condivisa tra gli  alunni compreso il professore.
QUindi l'oggetto stanza c'è ne una sola condivisa tra tutti gli oggetti alunni, quindi la variaible condivisa se viene modificata anche da una solo oggetto la variaible verrà modificata per tutti gli oggetti che la condividono. 
La varuabile statica viene creata quando si crea anche l'oggetto. 
Un esempio di variabile static e final insieme è la variabile  pi greco 
