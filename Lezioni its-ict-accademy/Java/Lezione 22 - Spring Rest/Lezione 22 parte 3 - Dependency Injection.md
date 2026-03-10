## Inversione di Controllo e Dependency Injection

Fino ad ora abbiamo usato Spring in modo quasi "ingenuo": 
- ==abbiamo annotato le classi con [[Lezione 22 parte 2 - Spring framework#^cc5395|`@RestController`]] e [[Lezione 22 parte 2 - Spring framework#^e0d891|`@Service`]], e Spring le ha istanziate e gestite automaticamente.== 
Ma non abbiamo mai spiegato il **meccanismo** che sta dietro a tutto questo. È arrivato il momento di farlo.

Guardando il codice dell'esercizio sugli utenti, noti qualcosa di strano: nel Controller istanziamo il Service così:

java

```java
private UtenteService service = new UtenteService();
```

E nel Service istanziamo il DAO così:

java

```java
private DAOUtenteMappa dao = new DAOUtenteMappa();
```

Stiamo usando `new` — stiamo creando noi gli oggetti. 
Questo funziona, ma è il modo sbagliato di farlo con Spring. 
Il problema è che stiamo creando dipendenze esplicite tra i layer: 
- ==il Controller sa che esiste `UtenteService`, il Service sa che esiste `DAOUtenteMappa`.== 
- Se un domani volessimo cambiare il DAO con uno che usa un database reale, dovremmo modificare il Service. 
==Questo viola il disaccoppiamento che abbiamo costruito con tanta cura.==

La soluzione è affidarsi a due principi fondamentali di Spring: 
1. **Inversione di Controllo**  
2. **Dependency Injection**.
### Inversione di controllo 

Una delle caratteristiche più famose di Spring è la sua implementazione del principio **IoC** (Inversion of Control). 
==È un pattern per cui un componente di livello applicativo **riceve** il controllo da un componente appartenente a una libreria riusabile — solitamente un framework.== 

Per capirlo vale la pena confrontare i tre livelli di "attività":

1. **La libreria** (es. `ArrayList`): 
	- ==è **passiva** rispetto alla nostra applicazione — siamo noi ad importarla, istanziarla e chiamarne i metodi quando vogliamo==
- **La nostra classe** è **passiva** rispetto al framework: 
	- ==non parte finché Spring non la invoca==
- **Il framework** (Spring) è la parte **attiva:**
	- ==è lui che decide quando istanziare le nostre classi e quando invocare i loro metodi==
Questo è esattamente ciò che abbiamo fatto finora: 
- abbiamo annotato il Controller con [[Lezione 22 parte 2 - Spring framework#^cc5395|`@RestController`]] e Spring lo ha istanziato e invocato automaticamente quando arrivava una richiesta HTTP. Noi non abbiamo mai scritto `new UtenteController()`.

> [!info] **Il principio di Hollywood:** 
> Lo IoC viene anche chiamato "principio di Hollywood" — _"Don't call us, we'll call you"_. 
> ==Non sei tu a chiamare il framework, è il framework a chiamare te.==

> [!example]  **Esempi di IoC che abbiamo già visto**
>
>**`ArrayList` vs Spring:**
>-  quando usi un [[Lezione 12 - Collection#Classe `ArrayList`|`ArrayList`]] sei tu l'attore attivo: 
>	- ==importi la libreria e chiami i suoi metodi.== 
>	- ==Con Spring invece è il contrario: sei tu a diventare passivo e Spring a chiamare il tuo codice.==
>
>**[[Lezione 18 - MultiThreading|I Thread:]]**
>-  ==il metodo [[Lezione 18 - MultiThreading#Creare un thread|`run()`]] non va mai chiamato direttamente perché non attiverebbe il multithreading.== 
>- ==Va chiamato [[Lezione 18 - MultiThreading#Avviare un Thread|`start()`]], che è il framework della [[Lezione 1 - Introduzione a Java#La JVM e l’indipendenza dalla piattaforma|JVM]] a invocare `run()` nel momento giusto.== 
>- È un esempio di IoC: non sei tu a decidere quando parte `run()`, è la JVM.

> [!NOTE] **Nota pratica:** 
> ==Per funzionare correttamente, le classi gestite da Spring devono trovarsi nel **pacchetto base** del progetto o in un suo sottopacchetto.== 
> Se il Controller si trova fuori da questo perimetro, Spring non lo trova e non lo istanzia.

Per comprendere meglio il IoC, facciamo riferimento all'immagine:

[![Screenshot-2026-03-10-at-12-24-46-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png](https://i.postimg.cc/DzyjJtL5/Screenshot-2026-03-10-at-12-24-46-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png)](https://postimg.cc/cv2MPkD8)
Il protagonista di questo esempio è il componente `MyApplicationComponent`: 
- Nel caso classico usato fino ad ora con java base(escludendo il multi-threading) è la nostra applicazione (ad esempio la classe con il `main`) a chiamare le librerie di Java(JSE Library).
Quando dovevamo utilizzare i componenti come [[Lezione 12 - Collection#Classe `ArrayList`|`ArrayList`]], [[Lezione 13 - Le map in Java#Classe `HashMap<K,V>`|`Hashmap`]], [[Lezione 12 parte 2 - L'interfaccia Set#La classe `TreeSet`|`TreeSet`]], [[Le stringhe|`String`]], etc. importavamo la libreria, istanziavamo esplicitamente un oggetto di queste classi e tramite dot notation usavamo i loro metodi. 
Questo è l'esempio classico di controllo: 
- ==è la nostra applicazione ad essere la parte **attiva** che chiama la libreria — che rimane **passiva**.== 
Con Spring invece: 
- ==è la nostra applicazione a diventare **passiva**, mentre il framework diventa la parte **attiva** che la chiama.==
Quindi nel caso di Spring invece, ma più in generale di qualsiasi framework di qualsiasi linguaggio(Flask o React), è la nostra applicazione a diventare la parte passiva perché è il framework a chiamarla usando le sue clausole e regole. 
Tornando agli esempi fatti nelle lezioni precedenti di Spring dove nella classe Controller o Service usavamo le annotazioni [[Lezione 22 parte 2 - Spring framework#^cc5395|`@RestController`]] o [[Lezione 22 parte 2 - Spring framework#^e0d891|`@Service`]] sopra la firma di queste due classi, notiamo che è Spring a istanziare implicitamente in modo automatico l'oggetto di queste due classi. 
Non siamo noi a farlo, a differenza di quanto fatto finora nelle classi [[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]] o [[Lezione 22 parte 2 - Spring framework#Il Service|Service]] dove, tramite [[Lezione 8 - L'incapsulamento#Incapsulamento e consistenza degli oggetti|incapsulamento]], rispettivamente istanziavamo esplicitamente gli oggetti  delle [[Lezione 22 parte 2 - Spring framework#DTO vs Entity|Entity]] o dei [[Lezione 22 parte 2 - Spring framework#Il DTO — Data Transfer Object|DTO]]. 
Mentre con le annotazioni [[Lezione 22 parte 2 - Spring framework#^cc5395|`@RestController`]] o [[Lezione 22 parte 2 - Spring framework#^e0d891|`@Service`]] non ci è mai servito istanziare esplicitamente gli oggetti della Controller o della Service per poter utilizzare i metodi di queste due classi, questo perché: 
- ==queste due annotazioni dicono a spring di istanziare implicitamente  queste due classi come una Controller o come una Service allo startup dell'applicazione.== 
Quindi è la nostra applicazione ad aspettare che il framework la chiami, la istanzi e usi i suoi metodi.



### Dependency Injection
La **Dependency Injection** è una forma specifica di IoC: 
- ==Consiste nella capacità di un framework — detto **Container** — di creare oggetti in inversione di controllo, occupandosi anche di creare e iniettare automaticamente gli oggetti di cui sono composti, detti **dipendenze**.==

#### L'esempio del Musicista

Supponiamo di avere una classe `Player` che ha una dipendenza da `Instrument` e di voler decidere il tipo di strumento **dinamicamente** — senza sapere a compile time se il Player suonerà una chitarra, un violino o una batteria.

Il problema è lo stesso che abbiamo visto nell'esercizio degli utenti: 
- ==se `Player` istanzia esplicitamente `new Guitar()`, è accoppiato a `Guitar` — non è più flessibile.== 
La soluzione è:

1. ==Creare un'**interfaccia** `Instrument` con un metodo `play()`==
2. ==Creare le classi concrete `Guitar`, `Violin`, `Drum` che la implementano==
3. ==Chiedere a **Spring** di creare il `Player` e di iniettargli dinamicamente lo strumento corretto==

In questo modo `Player` non sa e non gli importa quale strumento suonerà — lavora solo con l'interfaccia `Instrument`. È Spring a decidere quale implementazione concreta iniettare.

> [!link] **Il Collegamento con la Cartoleria:**
>  
> 
> Questo concetto lo abbiamo già visto in Java base con l'esercizio della cartoleria: 
> la classe `Magazzino` non nominava mai esplicitamente `Gomma` o `Penna` — lavorava con la classe padre `Articolo`. 
> ==Grazie al **[[Ereditarietà e polimorfismo#Binding dinamico in Java|binding dinamico]]** e al **[[Ereditarietà e polimorfismo#Polimorfismo|polimorfismo]]**, era in grado di gestire entrambi i prodotti senza dipendere esplicitamente da nessuno dei due.==
> 
> La Dependency Injection porta questo concetto al livello successivo: 
> - ==non sei tu a creare l'oggetto concreto e passarlo alla classe che ne ha bisogno — è il **Container** di Spring a farlo automaticamente, leggendo le annotazioni e costruendo il grafo delle dipendenze.==
> 
> > [!info] **In pratica:** 
> > ==se si danno al Controller le giuste coordinate tramite le annotazioni, Spring è in grado di creare da solo il [[Lezione 22 parte 2 - Spring framework#Il Service|Service]], il [[Lezione 22 parte 2 - Spring framework#Il DAO nel contesto Spring|DAO]], i [[Lezione 22 parte 2 - Spring framework#Il DTO — Data Transfer Object|DTO]] e le Entity== — senza che tu scriva mai un `new`. 
> >>[!ticket] **Ogni componente dichiara solo di cosa ha bisogno, e Spring pensa a procurarglielo.**
> 

### Diagramma delle classi delle esempio player
Il diagramma delle classi dell'esempio del musicista è strutturato così:
[![Screenshot-2026-03-10-at-13-08-44-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png](https://i.postimg.cc/pXqbGbRF/Screenshot-2026-03-10-at-13-08-44-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png)](https://postimg.cc/vcgNTK1Y)
- **`Instrument`** — è un'interfaccia con un metodo astratto `play()`, che verrà implementato dalle sottoclassi concrete
- **`Guitar`**, **`Violin`**, **`Drum`** — sono le classi concrete che implementano `Instrument` e forniscono ognuna la propria implementazione di `play()`
- **`Player`** — è la classe principale, che ha un attributo di tipo `Instrument` e un metodo `playInstrument()`

Il punto chiave è che `Player` dichiara l'attributo come riferimento all'**interfaccia** `Instrument` — non a una classe concreta:


```java
private Instrument instrument;
```

Questo permette di fare **chiamate polimorfiche** al metodo `play()`: a runtime, a seconda di quale oggetto concreto (`Guitar`, `Violin` o `Drum`) viene iniettato da Spring nell'attributo `instrument`, verrà eseguita l'implementazione corrispondente. `Player` non sa e non gli importa quale strumento suonerà — sa solo che l'oggetto che riceve implementa l'interfaccia `Instrument` e quindi ha un metodo `play()`.

Una volta create le classi, basterà configurarle tramite le annotazioni di Spring affinché il Container possa:

1. **Creare** l'oggetto `Player`
2. **Creare** lo strumento che vogliamo fargli suonare
3. **Iniettare** lo strumento nel `Player` automaticamente

> [!NOTE] **Nota — Pattern Strategy:**
>  Questo esempio è un'applicazione diretta del **[[Lezione 19 - Design Pattern#Pattern Strategy|pattern Strategy]]** che abbiamo visto [[Lezione 19 - Design Pattern|nella lezione sui Design Pattern]]. 
>  `Instrument` è la strategia astratta, `Guitar`, `Violin` e `Drum` sono le strategie concrete intercambiabili, e `Player` è il contesto che le usa senza sapere quale implementazione concreta sta ricevendo. 
>  La Dependency Injection di Spring potenzia questo pattern: 
>  - ==invece di essere tu a passare manualmente la strategia concreta al contesto, è Spring a iniettarla dinamicamente a runtime — rendendo il sistema ancora più disaccoppiato e flessibile.== 
>  Non è da confondere con il pattern **Adapter** che abbiamo visto con JDBC — lì si trattava di far comunicare due interfacce incompatibili, qui si tratta di rendere intercambiabili diverse implementazioni della stessa interfaccia.



### `@Component` e `@Autowired`
Spring, al fine di implementare la IoC e la Dependency Injection, usa le cosiddette **annotazioni**. Come abbiamo già visto con [[Lezione 22 parte 2 - Spring framework#^cc5395|`@RestController`]] e [[Lezione 22 parte 2 - Spring framework#^e0d891|`@Service`]], le annotation servono a Spring per due scopi principali:

1. **Indicare il ruolo** del componente nella struttura del progetto — Controller, Service, DAO, ecc.
2. **Configurare come gestirlo** — ad esempio ==quando istanziarlo, quali dipendenze iniettargli e con quale priorità sceglierlo tra più implementazioni disponibili.==

In tutti i casi il principio è lo stesso: 
- ==non sei tu a scrivere `new` — è Spring a leggere le annotation allo startup e a costruire e collegare automaticamente tutti i componenti.==


> [!NOTE] **Nota — `@Annotation` Spring vs Decorator Python:** 
> Le annotation di Spring e i [[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#**Utilizzo dei Decoratori** `@property` **per Getter e Setter**|decorator Python]] sono concettualmente simili: 
> ==entrambi usano la sintassi `@` per **aggiungere comportamento a una classe senza modificarne il codice**.== 
> La differenza principale è nel funzionamento sottostante:
>
>- I **decorator Python:**
>	- ==wrappano la funzione originale ed eseguono codice aggiuntivo a runtime==
>- Le **annotation Java** sono **metadati** che Spring ==legge allo startup per capire come gestire le classi:== 
>	- ==non modificano il comportamento della classe direttamente, ma dicono al Container come istanziarla e collegarla alle altre==
>
>In entrambi i casi però l'obiettivo è lo stesso: 
>**configurare il comportamento senza toccare il codice della classe**.



Ovviamente non esistono solo queste due annotazioni ma c'è ne sono molte altre e le principali sono: 

#### 1. `@Component`

`@Component` è: 
- ==l'annotazione base che si pone su una classe per dire a Spring di **istanziarla e gestirla automaticamente** tramite il Container IoC.== 
Una classe annotata con `@Component` viene detta **bean** di Spring.

> [!NOTE] **Nota — Container Spring vs Docker:** 
> Il termine "Container" in Spring non ha nulla a che fare con i container Docker. Il **Container di Spring** è il componente interno — chiamato `ApplicationContext`: 
>-  ==si occupa di creare, gestire e collegare tutti i bean annotati con `@Component`.== 
> È essenzialmente il "gestore" degli oggetti dell'applicazione. 
> Docker invece è un ambiente isolato per eseguire applicazioni — due concetti completamente diversi che condividono solo il nome.



Per funzionare correttamente con Spring, un Component dovrebbe essere un **JavaBean**, ovvero avere:

- **Costruttore a zero argomenti** — ==necessario per la deserializzazione e per l'istanziazione da parte di Spring==
- **Getter e setter per le proprietà** — ==necessari per accedere e modificare i campi dell'oggetto==

### 2. `@Autowired`

Se un Component ha una proprietà di tipo oggetto — quindi non primitiva (`int`, `double`, ecc.) né `String` — ==è possibile chiedere a Spring di **crearla e iniettarla automaticamente** usando l'annotazione `@Autowired` sulla proprietà.==

==Per funzionare, la classe della proprietà da iniettare deve essere a sua volta annotata con `@Component` — altrimenti Spring non sa come crearla.==

```java
@Component
public class Player {

    @Autowired
    private Instruments inst; // Spring creerà e inietterà automaticamente l'implementazione corretta

    public Player() { }

    public void playInstruments() {
        this.inst.play();
    }
}
```

**In questo esempio:**

- `@Component`: 
	- ==su `Player` dice a Spring di istanziare il `Player` come un Component==
- **`@Autowired` su `inst` dice a Spring di:** 
	- ==cercare un Component che implementi `Instruments` e di iniettarlo automaticamente nel campo `inst`==

> [!link] **Nota il collegamento con la [[#Dependency Injection|Dependency Injection]]:**
>  non siamo noi a scrivere `this.inst = new Guitar()`: 
>  - ==è Spring a decidere quale implementazione concreta di `Instruments` iniettare.== 
>  - ==`Player` non sa e non gli importa quale strumento riceverà.==

#### 3.  `@Primary`

Ma cosa succede se esistono **più Component** che implementano la stessa interfaccia? 
Ad esempio se sia `Guitar` che `Drums` sono annotate con `@Component`, Spring non sa quale delle due iniettare nel `Player` e lancerebbe un errore.

La soluzione è `@Primary`: 
- ==si aggiunge sotto `@Component` sulla classe che si vuole venga scelta **prioritariamente** rispetto alle altre.==
```java
@Component
@Primary
public class Drums implements Instruments {
    @Override
    public void play() {
        System.out.println("I'm playing drum");
    }
}
```

In questo modo quando Spring deve iniettare un `Instruments` nel `Player`, sceglierà `Drums` perché è marcata come primaria.
### Il Problema delle Dipendenze Ambigue

[![Screenshot-2026-03-10-at-16-06-00-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png](https://i.postimg.cc/L5gHrjFw/Screenshot-2026-03-10-at-16-06-00-Microsoft-Power-Point-Spring-e-Servizi-REST-Spring-e-Servizi-RE.png)](https://postimg.cc/y3B4Rgdy)

Guardando l'immagine, vediamo il `Player` con `@Autowired` sull'attributo `Instrument`. 
Spring deve iniettare un'implementazione concreta di `Instrument` — ma nel progetto ne esistono due: `Violin` e `Drums`, entrambe annotate con `@Component`.

Questo crea un problema: 
- ==Spring non sa quale delle due scegliere e **va in errore**.== 
- È un errore di **dipendenza ambigua** — ==Spring trova più candidati validi per l'iniezione e non può decidere autonomamente quale usare.==

```java
NoUniqueBeanDefinitionException: expected single matching bean but found 2: violin, drums
```

La soluzione che abbiamo già visto è `@Primary`: 
- ==si annota con `@Primary` la classe che si vuole venga scelta prioritariamente, e Spring la userà come implementazione di default quando trova più candidati dello stesso tipo.==

```java
@Component
@Primary
public class Drums implements Instruments {
    @Override
    public void play() {
        System.out.println("I'm playing drum");
    }
}
```

> Nota il parallelismo con il pattern **Strategy** che abbiamo visto prima: `@Primary` è il meccanismo con cui diciamo a Spring quale strategia concreta usare di default — senza che `Player` debba sapere nulla di questa scelta.




## Spring Core — L'`ApplicationContext`

Il **Spring Core** è: 
- ==il modulo fondamentale di Spring che fornisce il **Container IoC**.== 
È lui il vero protagonista di tutto ciò che abbiamo visto finora: è il componente responsabile di:

- ==**Creare** i bean annotati con `@Component`==
- ==**Iniettare** le dipendenze tramite `@Autowired`==
- ==**Gestire** il ciclo di vita di tutti gli oggetti dell'applicazione==

Il Container IoC di Spring è implementato dalla classe `org.springframework.context.ApplicationContext` — ==è questa la classe che abbiamo chiamato "Container" fino ad ora.==

#### Come si usa l'`ApplicationContext`

Una volta create e annotate le classi, si usa l'`ApplicationContext` per ottenere i bean gestiti da Spring:
```java
ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

// chiedo al Container di darmi il bean Player
// Spring lo crea, gli inietta lo strumento corretto tramite @Autowired e me lo restituisce
Player player = context.getBean(Player.class);

// chiamo il metodo — Spring ha già iniettato lo strumento @Primary
player.playInstruments(); // stampa: "I'm playing guitar"
```

> [!NOTE] **Nota:** 
> non scriviamo mai `new Player()` — chiediamo al Container di darcelo tramite `getBean()`. 
> È [[#Inversione di controllo|l'inversione di controllo in azione]]: 
> - ==non siamo noi a costruire l'oggetto e le sue dipendenze, è Spring a farlo per noi secondo le configurazioni che abbiamo dichiarato tramite le annotation.==


####  L'`ApplicationContext` nel Progetto Spring Boot

In un progetto Spring Boot non è necessario creare manualmente l'`ApplicationContext` — lo si ottiene direttamente come valore di ritorno del metodo di avvio di Spring nella **classe starter**, quella generata automaticamente da Eclipse alla creazione del progetto:
```java
@SpringBootApplication
public class SpringWebServicesUtenteApplication {
    public static void main(String[] args) {
        // SpringApplication.run() avvia Spring e restituisce l'ApplicationContext
        ApplicationContext context = SpringApplication.run(SpringWebServicesUtenteApplication.class, args);

        // chiedo al Container il bean Player
        Player player = context.getBean(Player.class);

        // Spring ha già iniettato lo strumento @Primary
        player.playInstruments();
    }
}
```

Se `Guitar` è configurata come `@Primary`, Spring inietta automaticamente `Guitar` nel `Player` — e `player.playInstruments()` stamperà:
```shell
I'm playing guitar
```

Se invece si cambia `@Primary` da `Guitar` a `Drums`, senza toccare nessun'altra riga di codice, `player.playInstruments()` stamperà:
```shell
I'm playing drum
```

Questo è il valore concreto della Dependency Injection: 
- ==cambiare il comportamento dell'applicazione modificando **solo la configurazione** — senza toccare il codice della classe che usa la dipendenza.== 
- `Player` non sa e non gli importa quale strumento suona — è Spring a decidere.