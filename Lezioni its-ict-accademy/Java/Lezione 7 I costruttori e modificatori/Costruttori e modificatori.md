
# Introduzione 
Nel corso delle lezioni precedenti sono stati introdotti i **[[Oggetti e Classi|concetti fondamentali della programmazione orientata agli oggetti in Java]]**, analizzando il ruolo delle [[Oggetti e Classi#^classe|classi]], degli [[Oggetti e Classi#^715e05|oggetti]], dei [[Oggetti e Classi#Costruzione delgi oggetti|costruttori]] e dei metodi. 
Abbiamo approfondito l’uso della [[Java/Lezione 5 Le classi/Le classi#La  keyword `this`|keyword `this`]], il meccanismo di **[[Java/Lezione 5 Le classi/Le classi#Overloading dei metodi|overloading]]** e **[[Java/Lezione 5 Le classi/Le classi#Overriding dei metodi|overriding]]**, e studiato in dettaglio la classe [[Le stringhe#Le stringhe in Java|`String`]], mettendone in evidenza le caratteristiche principali come l’immutabilità, i metodi di lettura, ricerca, confronto e parsing, oltre alle differenze con [[Le stringhe#La classe `StringBuffer`|`StringBuffer`]] e [[Le stringhe#La classe `StringBuilder`|`StringBuilder`]]. 
Successivamente sono stati introdotti i **[[Java/Lezione 5 Le classi/Le classi#Introduzione ai modificatori di accesso|modificatori di accesso]]**, che regolano la visibilità di classi e membri, evidenziando le differenze tra [[Java/Lezione 5 Le classi/Le classi#`public`|`public`]], [[Java/Lezione 5 Le classi/Le classi#`private`|`private`]], [[Java/Lezione 5 Le classi/Le classi#`protected`|`protected`]] e [[Java/Lezione 5 Le classi/Le classi#Introduzione ai modificatori di accesso#Accesso _default_ (nessun modificatore)|visibilità di default]].  
A partire da queste basi, la lezione attuale introduce nuovi concetti chiave per la progettazione delle classi: 
i **modificatori `static` e `final`**, il loro significato e il loro impatto sul comportamento di attributi, metodi e costruttori. 
Questi elementi permettono un controllo più preciso sul ciclo di vita degli oggetti e sulla struttura delle classi, risultando fondamentali per scrivere codice robusto, chiaro e manutenibile.


## I modificatori
Abbiamo visto che in Java esistono i **modificatori di accesso**, cioè quelle parole chiave che regolano la **visibilità** delle classi, degli attributi e dei metodi.

I principali sono:

- **`private`**  
    - ==Utilizzato soprattutto per gli **attributi**==. 
    - ==Un membro `private` è accessibile **solo all’interno della classe** in cui è dichiarato.==  
    - ==È il modificatore più usato nella programmazione orientata agli oggetti perché favorisce l’**[[Java/Lezione 5 Le classi/Le classi#Incapsulamento|incapsulamento]]**.==
    
- **`public`**  
    - ==Può essere applicato a **classi, metodi e attributi**==. 
    - ==Un membro `public` è accessibile **da qualsiasi altra classe**==.  
    - In genere:
    
	    - ==le classi principali sono `public`==
        
	    - ==i metodi che definiscono il comportamento pubblico di un oggetto sono `public`==
        
- **`protected`**  
    Rende visibile un membro:
    
    - ==alle classi dello **stesso [[Oggetti e Classi#Definizione di pacchetto|package]]**==
        
    - ==alle **sottoclassi**, anche se si trovano in package diversi==  
        - È meno usato nelle applicazioni comuni ed è più frequente nello sviluppo di **framework o librerie**.
        
- **visibilità di default (package-private)**  
    - ==Se non viene specificato alcun modificatore, il membro è visibile **solo all’interno dello stesso package**.==  
    - Anche questa modalità è poco usata nelle applicazioni commerciali, ma può essere utile nella progettazione di librerie.

In pratica, nello sviluppo di applicazioni “classiche”, i modificatori più usati sono **`private`** e **`public`**, mentre `protected` e il default hanno un ruolo più di nicchia.

Oltre ai modificatori di accesso, Java mette a disposizione **altri due modificatori fondamentali**, che non riguardano la visibilità ma il **comportamento** delle classi e dei membri:

1. **`static`**
    
2. **`final`**
    

Questi modificatori:

- ==possono essere usati **insieme**==
    
- ==possono essere usati **separatamente**==
    
- ==oppure **non essere usati affatto**==
    

Possono essere applicati a:

- ==attributi==
    
- ==metodi==
    
- ==(in alcuni casi) classi==

### Esempio: classe Impiegato 
Vogliamo rappresentare un **impiegato** che possiede i seguenti attributi:

- `nome : String`
    
- `salario : double`
    
- `dataAssunzione : Date`

Nel [[Analisi dei requisiti mediante UML|diagramma UML]] la classe viene rappresentata con: 
- **attributi privati**
    
- **metodi pubblici**
    
- un **costruttore**
    
- un metodo per **modificare il salario**
![[ImpiegatoJava.png]]

#### Uso dei modificatori nella classe `Impiegato`

Gli attributi vengono dichiarati `private` per rispettare il principio di **[[Java/Lezione 5 Le classi/Le classi#Incapsulamento|incapsulamento]]**:
```java
public class Impiegato {

    private final String nome;
    private double salario;
    private Date dataAssunzione;
```

#### Il modificatore `final`

Il modificatore `final` viene utilizzato per indicare che: 
- ==**un attributo, una volta inizializzato, non può più essere modificato** durante la vita dell’oggetto.==

Nel caso degli **attributi di istanza**, `final` significa che:

- ==il valore **può essere assegnato una sola volta**==
    
- ==dopo l’inizializzazione **non è più possibile riassegnarlo**==
    

In altre parole, l’attributo fa parte dello **stato “immutabile”** dell’oggetto.

Nel nostro esempio, l’attributo `nome` è dichiarato `final` perché:

- ==viene deciso **al momento della creazione dell’oggetto**==
    
- ==rappresenta un’informazione **stabile**, che non deve cambiare nel tempo==
    
- ==eventuali tentativi di modifica genererebbero un errore di compilazione==
    

> [!NOTE]  
> Il modificatore `final` **non rende l’attributo una costante a compile-time** (come accade per `static final`),  
> ma impedisce semplicemente che venga riassegnato dopo l’inizializzazione.

##### Inizializzazione di un attributo `final`

Proprio perché un attributo `final` **non può rimanere non inizializzato**, Java impone una regola precisa:

- un attributo `final` **deve essere inizializzato obbligatoriamente**
    
    - ==**nella dichiarazione**==
        
    - ==**oppure all’interno del costruttore**==
        

Non è possibile rimandare l’assegnazione a un metodo successivo.
#### Ruolo del costruttore

Il costruttore ha il compito di: 
- ==**inizializzare completamente lo stato dell’oggetto**, e questo è particolarmente importante quando sono presenti attributi `final`.==
```java
public Impiegato(String nome, double salario, Date dataAssunzione) {
    this.nome = nome;
    this.salario = salario;
    this.dataAssunzione = dataAssunzione;
}
```
In questo costruttore:

- `this.nome = nome` è **obbligatorio**, perché `nome` è `final`
    
- gli altri attributi vengono inizializzati normalmente
    
- l’uso della keyword `this`:
    
    - ==distingue gli attributi di istanza dai parametri del costruttore==
        
    - ==risolve il problema dello **shadowing**==
        

Se `this.nome` **non venisse inizializzato**, il codice **non compilerebbe**, perché Java garantisce che ogni oggetto venga creato in uno stato valido e completo.


> [!abstract]  Idea chiave
>
>
>- `final` serve a **fissare parti dello stato dell’oggetto**
  >  
>- il costruttore è il **luogo naturale** in cui inizializzare questi valori
  >  
>- in questo modo si ottengono oggetti:
>    
 >   - più sicuri
 >       
  >  - più prevedibili
 >      
  >  - più facili da mantenere


##### Metodo `incrSalario`

L’ultimo metodo, `incrSalario`, serve a **modificare il salario** dell’impiegato:
```java
public void incrSalario(double incremento) {
    salario += incremento;
}
```
Questo metodo:

- è `public` perché fa parte dell’**interfaccia pubblica** della classe
    
- **non ritorna nulla** (`void`)
    
- modifica lo stato interno dell’oggetto in modo **controllato**
    

> [!NOTE]  
> Anche se `salario` è `private`, può essere modificato dai metodi della classe stessa.

### Teorema delle classi 
In Java vale una regola fondamentale, spesso chiamata **teorema delle classi**:

- ==**tutte le classi hanno almeno un costruttore**==
    

Questo significa che **non può esistere una classe senza costruttore**.

#### Costruttore di default

Se **il programmatore non scrive alcun costruttore**, il compilatore:

- ==**aggiunge automaticamente un costruttore di default**==
    
- il costruttore di default:
    
    - ==**non ha parametri**==
        
    - ==inizializza tutti gli attributi ai **valori di default**==
        
        - `0` per i numeri
            
        - `false` per i boolean
            
        - `'\u0000'` per i `char`
            
        - `null` per i riferimenti a oggetti
            

Questo costruttore **non è visibile nel codice sorgente**, ma viene inserito nel file `.class`.
>[!NOTE]  
>Il costruttore di default è spesso chiamato anche costruttore di _emergenza_ o _disperazione_.

#### Più costruttori nella stessa classe
==Una classe **può avere più di un costruttore**, purché abbiano **liste di parametri diverse**==  
([[Java/Lezione 5 Le classi/Le classi#Overloading dei metodi|overloading]] dei costruttori).
Esempio:
```java
public class Impiegato {

    private String nome;
    private double salario;

    public Impiegato() {
        nome = "sconosciuto";
        salario = 0;
    }

    public Impiegato(String nome) {
        this.nome = nome;
        salario = 0;
    }

    public Impiegato(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }
}
```
In questo caso:

- ==**esistono tre costruttori**==
    
- ==il compilatore **non aggiunge** il costruttore di default==
    
- ==il programmatore controlla esplicitamente **come nasce l’oggetto**==


> [!faq] **Perché mettere più costruttori nella stessa classe**
>L’idea chiave è che **non tutti gli oggetti devono essere creati nello stesso modo**, perché spesso le informazioni disponibili al momento della creazione sono **diverse**.  
>In altre parole, un oggetto della classe che vogliamo rappresentare nel [[Analisi dei requisiti mediante UML#^0241e6|dominio]] può nascere in modi differenti, e sta a noi decidere **come modellarlo e inizializzarlo**.
>Prendiamo l'esempio della classe `Impiegato`: 
>```java
>public class Impiegato {
>
  >  private String nome;
   > private double salario;
>
  >  public Impiegato() {
  >      nome = "sconosciuto";
  >      salario = 0;
  >  }
>
  >  public Impiegato(String nome) {
 >       this.nome = nome;
  >      salario = 0;
  >  }
>
 >   public Impiegato(String nome, double salario) {
  >      this.nome = nome;
  >      this.salario = salario;
 >   }
>}
>
>```
>Qui abbiamo tre modi diversi di creare un impiegato:
>
>1. **Senza alcuna informazione** (`Impiegato()`):  
>    ==Utile se non conosci ancora nulla dell’impiegato. Viene creato un oggetto “di default” con valori iniziali sicuri==.
>    
>2. **Con solo il nome** (`Impiegato(String nome)`):  
> 	   - ==Utile se hai almeno il nome, ma non il salario==. 
> 	   - ==L’oggetto viene inizializzato in uno stato valido senza dover inserire dati inesistenti==.
>    
>3. **Con nome e salario** (`Impiegato(String nome, double salario)`):  
> 	  -  ==Utile quando hai tutte le informazioni fin dall’inizio.==
>> [!done] **Vantaggi Principali**
>> - **Oggetti sempre in uno stato valido:** 
>> 	  - ==il costruttore obbliga a inizializzare gli attributi secondo le regole della classe.==
 >>   
>>- **Flessibilità:** 
>> 	 - ==puoi creare un oggetto con informazioni parziali o complete senza scrivere codice duplicato==.
  >>  
>>- **Overloading:** 
>>	- ==tutti i costruttori hanno lo **stesso nome della classe**, ma parametri diversi → il compilatore sa quale chiamare==.
 >>   
>>- **Leggibilità:** 
>>	- ==chi legge il codice capisce subito quali dati servono per creare un certo oggetto.==

### Note sui costruttori 
Come abbiamo già visto nella lezione sulle [[Java/Lezione 5 Le classi/Le classi#Costruttori e modificatori|classi in Java]], in Java **ogni oggetto viene inizializzato tramite un solo costruttore al momento della creazione**.  
Tuttavia, è possibile richiamare **un altro costruttore della stessa classe** usando la [[Java/Lezione 5 Le classi/Le classi#La keyword `this`|keyword `this`]].  
==In questo modo possiamo **riutilizzare il codice** e evitare duplicazioni quando vogliamo costruire oggetti con valori predefiniti o parziali==.

```java
public class Impiegato {

    private String nome;
    private double salario;
    private Date dataAss;

    // Costruttore principale
    public Impiegato(String nome, double salario, Date data) {
        this.nome = nome;
        this.salario = salario;
        this.dataAss = data;
    }

    // Costruttore che usa la data odierna
    public Impiegato(String nome, double salario) {
        this(nome, salario, new Date());
    }
}
```

Qui:

- ==Il **primo costruttore** inizializza tutti gli attributi, incluso `dataAss`.==
    
- ==Il **secondo costruttore** accetta solo nome e salario e **richiama il primo costruttore** tramite `this`, impostando automaticamente la data odierna senza doverla passare manualmente.==
    

> [!important] **Importante:**
> 
> - `this(...)` ==deve essere **la prima istruzione** all’interno del costruttore.==
>     
> - ==È diverso da `super(...)`, che richiama invece un costruttore della superclasse.==
>

Questo approccio rende i costruttori più **modulari e leggibili**, evitando di duplicare codice quando vogliamo fornire valori predefiniti o calcolati automaticamente.

### Modificatori 
==I **modificatori** servono a descrivere le proprietà di un’entità in Java, che può essere una **classe**, un **metodo** o un **attributo**==.  
Si riferiscono principalmente a tre aspetti: **visibilità**, **modificabilità** e **appartenenza alla classe**.

#### 1. Visibilità

- `private`  
    - ==Indica che l’entità è accessibile **solo all’interno della classe** in cui è dichiarata.==  
    - Questo è fondamentale per applicare il **[[Java/Lezione 5 Le classi/Le classi#Incapsulamento|principio di incapsulamento]]**, proteggendo lo stato interno dell’oggetto e obbligando a usare **metodi controllati** (getter e setter) per accedere agli attributi.
    

#### 2. Modificabilità

- `final`  
    Specifica che l’entità **non può essere modificata dopo l’inizializzazione**.
    
    - Per un attributo, significa che il suo **valore rimane costante** una volta assegnato.
        
    - Ad esempio, se l’attributo `nome` di un `Impiegato` è `final`, il nome **non potrà mai cambiare** dopo la creazione dell’oggetto.
        
    - In pratica, `final` **impedisce l’implementazione di setter** per quell’attributo, mentre i getter rimangono possibili per leggerne il valore.
        
    - Il compilatore utilizza `final` anche come protezione: segnala immediatamente eventuali tentativi di modifica non consentiti.
        

#### 3. Appartenenza alla classe

- `static`  
    Indica che l’entità **appartiene alla classe stessa**, e non agli oggetti creati da quella classe.
    
    - Un attributo `static` è condiviso da **tutti gli oggetti** della classe.
        
    - Un metodo `static` può essere invocato **senza creare un’istanza** della classe, semplicemente usando `NomeClasse.metodo()`.

### `Static`
Il modificatore `static` indica che: 
- ==un’entità **appartiene alla classe stessa** e non agli oggetti creati da quella classe.== 
Può essere applicato a:

- ==**Classi interne (inner class)**==
    
- ==**Attributi**==
    
- ==**Metodi**==
    

#### Metodi statici

==Un **metodo statico** può essere invocato **senza creare un oggetto** della classe==.  
Un esempio classico è `Math.pow(2, 3)`:
```java
double risultato = Math.pow(2, 3); // ritorna 8
```
==Non serve istanziare `Math` perché tutti i metodi della classe sono statici, e il costruttore di `Math` è privato.==  
In Java, i metodi statici sono spesso usati per operazioni **matematiche o di utilità**, come in JS `Math.floor()` o `Math.random()`.

#### Variabili statiche

Se dichiari un attributo `static`, significa che: 
- ==**c’è un solo valore condiviso tra tutti gli oggetti della classe**.==  
Ad esempio, immagina una **stanza in un corso**: tutti gli studenti e il professore condividono la stessa stanza.
```java
public class Corso {
    static String aula = "Aula 101";
}
```

- ==Tutti gli oggetti `Corso` puntano alla stessa variabile `aula`.==
    
- ==Se un oggetto cambia `aula`, il cambiamento è visibile a tutti gli altri oggetti.==
    
- La variabile statica viene **creata insieme alla classe**, non all’oggetto.
#### Combinazione `static` + `final`

Spesso si usa `static` insieme a `final` per creare **costanti condivise**:
```java
public class Matematica {
    public static final double PI = 3.1415926535;
}
```

- ==`PI` appartiene alla classe `Matematica` e **non può essere modificata**==.
    
- ==È un esempio classico di variabile **condivisa e immutabile**.==

### Modificatori `final` e `static` in Java
Quindi per comprendere al meglio questi due modificatori in Java, riassumiamo quanto detto finora: 
#### Il modificatore `final`

==Il modificatore `final` indica che un elemento **non può evolvere nel tempo==.**
Può essere assegnato sia agli attributi che ai metodi di una classe con le seguenti caratteristiche:

- **Attributi:** 
	- ==una volta inizializzati (direttamente nella dichiarazione o nel costruttore), il loro valore **non può più cambiare**==.  
    - Ad esempio, se dichiariamo il `nome` di un `Impiegato` come `final`, una volta assegnato nel costruttore, non sarà più modificabile.
    
- **Metodi:** 
	- ==non possono essere **sovrascritti** dalle sottoclassi, garantendo che il comportamento originale resti invariato==.
    

> [!ticket] **In pratica, `final` è uno strumento di protezione**:
> -  ==il compilatore impedirà ogni tentativo di modifica successiva, rendendo più sicuro e prevedibile il comportamento dell’oggetto==.

> [!NOTE] **Nota:**
> -  ==un attributo `final` **può avere solo un getter**, perché non ha senso fornire un setter per qualcosa che non deve cambiare==
##### Esempio `final` su attributi e metodi
```java
public class Impiegato {

    // Attributo final: non può cambiare dopo l'inizializzazione
    private final String nome;

    public Impiegato(String nome) {
        this.nome = nome;
    }

    // Metodo final: non può essere sovrascritto in una sottoclasse
    public final void stampaNome() {
        System.out.println("Nome: " + nome);
    }

    // Non possiamo fare:
    // this.nome = "Altro";  --> ERRORE!
}
```

**Spiegazione:**

- ==`nome` è `final`, quindi il costruttore deve assegnargli un valore e poi non potrà più cambiare==.
    
- ==`stampaNome()` è `final`, quindi eventuali sottoclassi non possono modificare questo metodo.==

#### Il modificatore `static`

Il modificatore `static` indica invece che: 
- ==un elemento **appartiene alla classe e non alle singole istanze**==


- ==Non serve creare un oggetto per utilizzarlo; lo si può richiamare direttamente con `Classe.attributo` o `Classe.metodo()`==.
    
- ==Tutte le istanze della classe **condividono la stessa variabile o metodo**.== Se un oggetto modifica una variabile statica, la modifica è visibile da tutti gli altri oggetti della classe.
    
- I metodi statici sono utili quando il comportamento **non dipende dai dati specifici dell’oggetto**, come ad esempio i metodi matematici (`Math.pow()`, `Math.random()`).

##### Esempio `static` su attributi e metodi
```java
public class Contatore {

    // Attributo statico condiviso da tutte le istanze
    public static int totaleOggetti = 0;

    public Contatore() {
        totaleOggetti++; // ogni volta che creo un oggetto, aumento il contatore
    }

    // Metodo statico: non serve un oggetto per invocarlo
    public static void stampaTotale() {
        System.out.println("Totale oggetti: " + totaleOggetti);
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        new Contatore();
        new Contatore();
        Contatore.stampaTotale(); // Output: Totale oggetti: 2
    }
}
```
- `totaleOggetti` è condiviso tra tutte le istanze.
    
- `stampaTotale()` è un metodo di classe, quindi può essere chiamato direttamente con `Contatore.stampaTotale()` senza creare oggetti.
#### `static` + `final`

Combinando i due modificatori otteniamo elementi che sono **condivisi da tutte le istanze** e **immutabili**:

- Tipico esempio: una costante matematica
```java
public static final double PI = 3.14159;
```

- Significa che **c’è un solo valore condiviso** per tutti gli oggetti e **non può cambiare** nel tempo.
    

In altre parole:

- `final` → “non cambiare mai”
    
- `static` → “c’è uno solo per tutti”
    
- `static final` → “c’è uno solo per tutti e non può cambiare mai”

##### Combinazione `static final` (costanti)
```java
public class Matematica {

    // Costante: unica per tutti e immutabile
    public static final double PI = 3.14159;

    public static void main(String[] args) {
        System.out.println("Il valore di PI è: " + PI);

        // Non possiamo fare:
        // PI = 3.14;  --> ERRORE!
    }
}
```
**Spiegazione:**

- `PI` è un valore **immutabile** (`final`) e **condiviso da tutte le istanze della classe** (`static`).
    
- È il tipico caso di costante in Java, molto simile alle `const` in altri linguaggi.