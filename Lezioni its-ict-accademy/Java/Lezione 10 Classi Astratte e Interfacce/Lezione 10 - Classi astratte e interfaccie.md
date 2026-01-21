## Classi astratte 
Come in [[Classi astratte|Python]] Le **classi astratte** sono utilizzate per modellare concetti molto **generici** all’interno di un’architettura software. 
Proprio perché rappresentano entità incomplete o concettuali, **non possono essere istanziate direttamente:** 
- ==cioè non è possibile creare oggetti a partire da una classe astratta.==

==Una classe che contiene **uno o più metodi astratti** deve essere obbligatoriamente dichiarata `abstract`.== 
Tuttavia, ==anche una classe che **non contiene metodi astratti** può essere dichiarata astratta, se si desidera impedirne l’istanziazione e utilizzarla solo come classe base.==
Come nell' esercizio Cartole ria la classe Articola l'avevamo resa abrtact perché non volevamo istanziare un oggetto della classe Prodotto che è una classe generica, mentre le sottoclassi come Penna e Gomma erano concrete 

Il metodo astratto è un metodo **privo di implementazione**, che definisce solo la firma. L’implementazione concreta viene demandata alle sottoclassi. 
Per questo motivo, per poter creare oggetti, è necessario definire una **sottoclasse concreta** che estenda la classe astratta e fornisca l’implementazione di tutti i metodi astratti. Solo a partire da questa sottoclasse sarà possibile istanziare oggetti.

È importante notare che, pur non potendo creare istanze di una classe astratta, **è possibile dichiarare variabili del suo tipo**. Questo consente di sfruttare il polimorfismo, permettendo a tali variabili di riferirsi a oggetti di qualsiasi sottoclasse concreta.

Una classe astratta può contenere **attributi**, **metodi concreti** e **costruttori**. In particolare, una classe astratta **ha sempre almeno un costruttore**, utilizzato per inizializzare lo stato comune alle sottoclassi.

##### Esempio: classe `Message`
```java
public abstract class Message {
    private String sender;

    public Message(String from) {
        sender = from;
    }

    public abstract void send(); // metodo astratto

    public String getSender() {
        return sender;
    }
}
```

In questo esempio, la classe `Message` rappresenta un messaggio in forma astratta. Essa definisce un attributo comune (`sender`), un costruttore per inizializzarlo e un metodo concreto (`getSender`). Il metodo `send()` è invece astratto, poiché il modo in cui un messaggio viene inviato dipende dal tipo specifico di messaggio e dovrà essere definito nelle sottoclassi.
Vediamo nel dettaglio: 
1. Dichiarazione della classe
```java
public abstract class Message {
```


- La classe `Message` è dichiarata `abstract` perché rappresenta un concetto **generico** di messaggio. 
- Non descrive un messaggio concreto (email, SMS, notifica, ecc.), ma solo le caratteristiche comuni a tutti i messaggi.  
- Di conseguenza, **non è possibile creare oggetti direttamente di tipo `Message`**.
2. **Attributo della classe**
```java
private String sender;
```

- L’attributo `sender` rappresenta il **mittente del messaggio**.  
- È dichiarato `private` per rispettare il principio di **incapsulamento**, impedendo l’accesso diretto dall’esterno della classe. 
- Il valore potrà essere letto solo tramite un metodo pubblico.
3. **Costruttore**
```java
public Message(String from) {
    sender = from;
}
```

- Anche se la classe è astratta, **può e deve avere un costruttore**.  
- Questo costruttore serve a inizializzare lo stato comune a tutte le sottoclassi, in questo caso il mittente del messaggio.
- Il costruttore verrà chiamato **implicitamente** quando si istanzierà una sottoclasse concreta di `Message`.
4. **Metodo astratto**
```java
public abstract void send();
```

- Il metodo `send()` è dichiarato `abstract` perché la classe `Message` **non conosce il modo concreto in cui il messaggio verrà inviato**.  
- L’invio può variare a seconda del tipo di messaggio (email, SMS, push notification, ecc.).

- Questo implica che:

	- il metodo **non ha un corpo**
    
	- ogni sottoclasse concreta **è obbligata a fornire un’implementazione** di `send()`


> [!abstract] **Significato complessivo dell’esempio**
> La classe `Message` definisce:
>
>- **uno stato comune** (il mittente)
>    
>- **un comportamento comune** (il metodo `getSender`)
 >   
>- **un comportamento astratto** (`send`) che deve essere specializzato
 >   
>
>In questo modo, `Message` funge da **classe base astratta**, utile per modellare una gerarchia di classi di messaggi diversi, mantenendo una struttura coerente e favorendo il **polimorfismo**.

## Le interfacce
Oltre alle classi astratte, in Java esistono le **interfacce**, che permettono di definire un **contratto** tra più entità che non sono direttamente collegate da una relazione di ereditarietà.

Un’interfaccia consente a classi diverse, anche appartenenti a gerarchie differenti, di **interagire attraverso un insieme comune di metodi**, senza conoscere i dettagli della loro implementazione. 
In questo senso, l’interfaccia funge da **collegamento** tra:

- ==una o più classi che **utilizzano** i metodi definiti dall’interfaccia;==
    
- ==una o più classi che **implementano** tali metodi.==
    

In pratica, l’interfaccia stabilisce _cosa_ deve essere fatto, mentre le classi che la implementano decidono _come_ farlo. Questo favorisce un forte **disaccoppiamento** tra le parti del sistema e rende il codice più flessibile e manutenibile.

Di solito, si ha:

- una classe (o più classi) che lavora **in termini di interfaccia**, cioè utilizza i metodi dichiarati nell’interfaccia;
    
- una o più classi concrete che **implementano l’interfaccia**, fornendo l’implementazione effettiva dei metodi.


> [!Example] Analogie
> Un’analogia efficace è quella delle **certificazioni professionali**:  
la certificazione rappresenta un insieme di competenze standardizzate. Il datore di lavoro non ha bisogno di sapere _come_ il lavoratore ha acquisito quelle competenze, ma solo che possiede la certificazione. Allo stesso modo, una classe che utilizza un’interfaccia non ha bisogno di conoscere la classe concreta che la implementa, ma solo che rispetti il contratto definito dall’interfaccia.
>
>Un’altra metafora è quella delle **due sponde di un fiume**:  
le sponde rappresentano entità indipendenti, mentre l’interfaccia è il **ponte** che permette la comunicazione tra di esse senza fonderle in un’unica struttura.

###  Caratteristiche principali delle interfacce in Java

In Java, un’interfaccia:

1. rappresenta una **categoria completamente astratta**;
    
2. **dichiara solo metodi astratti** 

> [!info]
> nelle versioni più recenti del linguaggio possono esistere anche metodi `default` e `static`, ma il principio generale resta quello del contratto);

    
3. non può essere istanziata;
    
4. viene **implementata** da una o più classi tramite la parola chiave `implements`.
5. **non possiede attributi di istanza** (può contenere solo costanti `public static final`);
6. **non ha costruttori**, nemmeno quello di default(definito nel `.class`), poiché non può essere utilizzata per creare oggetti.
#### Esempio di caso d’uso: quando scegliere tra classe astratta e interfaccia

Supponiamo di dover modellare una classe generica in Java e di dover scegliere se utilizzare una **classe astratta** oppure un’**interfaccia**.  
La scelta dipende principalmente dalle caratteristiche che vogliamo definire.

- Se la classe deve **condividere attributi comuni** e **fornire metodi concreti** (cioè con implementazione) alle sottoclassi, allora la scelta più appropriata è una **classe astratta**.
    
- Se invece la classe deve solo **definire un insieme di comportamenti**, senza attributi comuni e senza implementazioni concrete, allora la scelta ricade su un’**interfaccia**.
    

In sintesi:

- ==la **classe astratta** è adatta quando esiste uno stato condiviso e una base di codice comune;==
    
- ==l’**interfaccia** è preferibile quando si vuole imporre un contratto uniforme a classi anche molto diverse tra loro, favorendo il disaccoppiamento e il polimorfismo.==

#### Perché usare il costrutto `interface` anziché abstract
- ==Un interfaccia definisce comportamenti (metodi) generici che verrano implementati nelle sottoclassi figlie.== 
- Mentre una classe astratta non definisce solo i comportamenti(metodi) ma anche gli attributi dell'istanza 
### Sintassi - Java 7
Si possono dichiarare solo: 
- metodi pubblici e astratti `public abstract`
- costanti di classe `public static final`
Inoltre per dichiarare un interfaccia si dichiara `interface` al posto di `class`
Esempio: 
```java
public interface OggettoPrezzabile
{
	public void setPrezzo(double prezzo); 
	public double getPrezzo();
}
```

Da notare come `abstract` sia sottointeso in un interfaccia, scriverlo non è un errore, la JVM non darà un errore e il codice a runtime verrà compilato ma è comunque una buona pratica non definirla. 
`static`: crea gli attributi di classe 
`final`: comparabile con il `const` di JS ovvero non muta 
Se ci dimenticassimo di scrivere questi due statement vengo assegnati di defualt ma è una best practise dichiarali sempre. 


#### Perché le interfacce 
Le **interfacce** rappresentano uno strumento avanzato di **progettazione e sviluppo software**, ma si fondano comunque sui concetti fondamentali della **programmazione a oggetti**, in particolare **ereditarietà** e **polimorfismo**.

Esse permettono di superare alcune limitazioni del linguaggio, offrendo maggiore flessibilità nella progettazione dei sistemi. In particolare, le interfacce consentono di:

- **aggirare l’assenza dell’ereditarietà multipla** tra classi in Java, permettendo a una classe di implementare più interfacce;
    
- **definire tipi astratti e generici** che descrivono un comportamento, rimandando l’implementazione concreta alle classi che li realizzeranno.
##### Quindi a che servono 
Le interfacce hanno lo scopo di **definire schemi di comportamento** che le classi sono obbligate a rispettare. In questo modo, esse stabiliscono un contratto che garantisce uniformità e coerenza tra classi diverse.

Un aspetto fondamentale è che, utilizzando **variabili dichiarate come tipo interfaccia**, è possibile invocare i metodi definiti dall’interfaccia **senza conoscere a priori la classe concreta dell’oggetto** a cui la variabile fa riferimento.

Grazie al **polimorfismo**, sarà il sistema, **a runtime**, a determinare quale implementazione concreta del metodo debba essere eseguita, in base alla reale natura dell’oggetto. Questo meccanismo consente di scrivere codice più flessibile, estendibile e meno dipendente dalle singole implementazioni.

Per ereditarietà multiplia si intende: una classe in Java può avere uno e un solo padre da cui eredita, se il padre non viene definito allora sarà la classe `Object`.
Le interfaccie rappresentato tutte le categorie a cui volgiamo appartenere per imparare a fare quelle cose: volgio diventare un programmatore Java e quindi frequento un corso e quindi io ed i miei colleghi di corso avremo in comune questo tipo di parentela come programmatori java, detta parentela debole.
La parentela debole è un tipo di parentela in cui un oggetto non ha un legame vero con una vera classe padre: io se sono un programmatore Java ho una parentela con i miei colleghi ma non siamo una famiglia in senso stretto.

In UML viene rappresentata con la linea tratteggiata
[![Screenshot-2026-01-20-at-12-28-37-Microsoft-Power-Point-Java-10-Interfacce-Compatibility-Mode-Jav.png](https://i.postimg.cc/v8nM268G/Screenshot-2026-01-20-at-12-28-37-Microsoft-Power-Point-Java-10-Interfacce-Compatibility-Mode-Jav.png)](https://postimg.cc/BtJdXb1z)

In questo caso `Libro` ha una relazione is-a  con media, e ha altre due relazioni is-a debole con `OggettoPrezzabile`, `OggettoSfogliabile` 

[![Screenshot-2026-01-20-at-12-33-43-Microsoft-Power-Point-Java-10-Interfacce-Compatibility-Mode-Jav.png](https://i.postimg.cc/7L5fQYQY/Screenshot-2026-01-20-at-12-33-43-Microsoft-Power-Point-Java-10-Interfacce-Compatibility-Mode-Jav.png)](https://postimg.cc/CZVhRYgW)


