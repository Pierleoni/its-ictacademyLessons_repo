
## Concetto di ereditarietà
L’**ereditarietà** è uno dei punti di forza principali di Java e, più in generale, della programmazione orientata agli oggetti (OOP).

Essa permette di creare **nuove classi** partendo da classi già esistenti, riutilizzando codice e strutturando meglio il dominio dell’applicazione. In pratica, una classe **figlia** eredita attributi e metodi dalla classe **padre**, e può aggiungerne di nuovi o ridefinirne alcuni.

I principali vantaggi dell’ereditarietà sono:

1. **Massimizzare il riutilizzo del codice**
    
    - Separando gli aspetti generici da quelli specifici, possiamo definire classi base con funzionalità comuni (es. `Persona`) e poi creare sottoclassi più specializzate (es. `Studente` o `Docente`).
        
    - Questo approccio ci permette di organizzare gli elementi del dominio in maniera logica: **gli elementi generici in classi base, gli aspetti specifici nelle sottoclassi**.
        
    - In questo modo, ogni classe si concentra sul proprio ambito di responsabilità.
        
2. **Facilità di evoluzione e manutenzione**
    
    - L’aggiunta di nuove funzionalità avviene **estendendo le classi esistenti**, senza modificare il codice già testato.
        
    - Questo riduce i rischi di introdurre errori e rende il software più **manutenibile e scalabile**.
### Definizione di ereditarietà

L’**ereditarietà** permette di creare nuove classi che **riutilizzano**, **estendono** e, se necessario, **modificano** (tramite [[Java/Lezione 5 Le classi/Le classi#Overriding dei metodi|overriding]]) il comportamento di altre classi già esistenti.

- La classe i cui membri (attributi e metodi) vengono ereditati è detta **classe base** o **classe padre**.
    
- La classe che eredita questi membri è detta **classe derivata** o **classe figlia**.
    

Si parla di **superclasse** perché nei [[Generalizzazioni#Il concetto di generalizzazione|diagrammi UML]] viene rappresentata **sopra** alla sottoclasse.

Questa gerarchia può estendersi ulteriormente:

- una **classe figlia** può a sua volta diventare **classe padre** per altre classi, creando una **catena di ereditarietà**.
    
- In questo modo, possiamo costruire strutture a più livelli, dove ogni livello aggiunge funzionalità specifiche senza duplicare il codice comune.

### Esempio 1 : dividere apsetti generali e specifici 

Supponiamo di voler modellare alcune entità del **dominio universitario**, come **studenti** e **professori**:

- **In comune** hanno: `nome` e `cognome`.
    
- **Specifico per lo studente**: `matricola` e `corso di laurea`.
    
- **Specifico per il professore**: `materia insegnata`.
    
[![Screenshot-2026-02-09-at-12-56-01-Microsoft-Power-Point-Java-09-Ereditarieta-Compatibility-Mode-J.png](https://i.postimg.cc/wvyhMRGj/Screenshot-2026-02-09-at-12-56-01-Microsoft-Power-Point-Java-09-Ereditarieta-Compatibility-Mode-J.png)](https://postimg.cc/47GKFyGD)

Se creassimo le due classi separatamente, copiando e incollando tutti i campi comuni, avremmo **ridondanza di dati**.

> [!fail] Il copia-incolla **non è riuso del codice**: aumenta il rischio di errori e rende difficile la manutenzione.
> 

Per ottimizzare, possiamo creare una **classe più generale**, chiamata `Persona`, che contenga **attributi e metodi comuni**.  
Le classi `Studente` e `Professore` diventeranno **sottoclassi** di `Persona`:

[![Screenshot-2026-02-09-at-12-58-00-Microsoft-Power-Point-Java-09-Ereditarieta-Compatibility-Mode-J.png](https://i.postimg.cc/2yYVYqpP/Screenshot-2026-02-09-at-12-58-00-Microsoft-Power-Point-Java-09-Ereditarieta-Compatibility-Mode-J.png)](https://postimg.cc/FdP9gHHZ)
- **Ereditano** attributi e metodi della superclasse (`nome`, `cognome`, eventuali metodi comuni).
    
- **Aggiungono** attributi e comportamenti specifici (`matricola`, `corso di laurea`, `materia`).
    
- **Possono modificare** (override) comportamenti ereditati se necessario.
    

> [!done] In questo modo:
> 
> 
> - Si riduce la **ridondanza**.
>     
> - Si favorisce il **riuso del codice**.
>     
> - Si ottiene una struttura più **chiara e manutenibile**.

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