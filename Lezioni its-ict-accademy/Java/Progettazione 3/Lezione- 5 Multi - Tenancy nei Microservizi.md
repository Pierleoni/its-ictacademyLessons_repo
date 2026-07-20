# Multi-Tenancy nei Microservizi

Finora abbiamo esplorato come strutturare un'applicazione a microservizi dal punto di vista **architetturale e operativo**: abbiamo visto [[Lezione 1 - Applicazioni cloud a microservizi#Cos'è un'Applicazione a Microservizi|come si organizzano i microservizi]], [[Lezione 2 - Architetture dei microservizi#Le Due Architetture dei Microservizi|come comunicano tra loro]], [[Lezione 3 - Progettazione Dei  Microservizi#Esempio Pratico Food Delivery (come Glovo)|come si progettano i confini tra servizi]].

Ma abbiamo fatto un'assunzione implicita che non sempre è vera: ==**abbiamo supposto che il sistema serva un'unica organizzazione, con un unico set di dati e un unico contesto di business.**==

Nella realtà commerciale però, soprattutto nel modello **[[Lezione 4 - Modelli dei servizi di cloud#SaaS – Software as a Service (Software come Servizio)|SaaS]]** (Software as a Service), un'unica applicazione può servire **decine, centinaia, o addirittura migliaia di clienti diversi**. Amazon non gestisce ordini solo per se stesso — li gestisce per milioni di venditori. Slack non serve una sola azienda — serve centinaia di migliaia di workspace. Glovo non ha un unico ristorante — ne coordina decine di migliaia in decine di Paesi.

In questi scenari emerge un nuovo problema architetturale: **come garantiamo che i dati del cliente A rimangono completamente isolati dai dati del cliente B, anche se entrambi usano la stessa applicazione?**

Questa è la sfida della **Multi-Tenancy** — e come vedremo, ha implicazioni profonde su come progettiamo e implementiamo i nostri microservizi.

## Cos'è un Tenant?

Partiamo dalla definizione più semplice:

> ==**Un tenant è un'istanza logica della tua applicazione che appartiene a un cliente/organizzazione distinto.**==

Suona astratto, vero? Scomposizione punto per punto.
#### Cosa Significa "Istanza Logica" (non Fisica)?

Finora abbiamo sempre pensato a un'applicazione così:
```css
┌─────────────────────┐
│  Applicazione       │
│  (un'istanza)       │
│  (un server)        │
│  (un database)      │
└─────────────────────┘
     ↓ serve ↓
   UN CLIENTE
```
==**Una sola applicazione, un solo cliente, tutto insieme.**==

Ma una SaaS multi-tenant fa così:
```css
┌──────────────────────────────────────┐
│  Applicazione (un'istanza sola)      │
│                                      │
│  Logicamente divisa in:              │
│  ├─ Tenant A (Cliente 1)             │
│  ├─ Tenant B (Cliente 2)             │
│  ├─ Tenant C (Cliente 3)             │
│  └─ ...                              │
│                                      │
│  Database (uno solo, fisicamente)    │
│  Ma organizzato per tenant (logicamente) │
└──────────────────────────────────────┘
     ↓ serve ↓
   TANTI CLIENTI
```

>**"Istanza logica" significa: ==un'applicazione fisica unica, ma organizzata in modo da presentare tanti "mondi" separati.**==

Slack è l'esempio perfetto:

- ==**Fisicamente**: uno Slack, un server, un database==
- ==**Logicamente**: migliaia di workspace, ognuno isolato dagli altri==

#### I Tre Pilastri di un Tenant

Nel contesto di un'applicazione multi-tenant, un tenant ha **sempre** tre caratteristiche:

##### 1. Tenant = Cliente/Organizzazione

Un tenant non è un utente. ==**È un contenitore di utenti.**==

Ad esempio:

- In Slack: il workspace "Acme Corp" è un tenant (contiene 500 utenti)
- In Shopify: il negozio "Mario's Shop" è un tenant (contiene 1 proprietario, migliaia di clienti)
- In iam-mo: l'azienda "EuroTech" è un tenant (contiene 100 dipendenti)

> [!info] **Differenza cruciale:**
> 
> - **Utente** = Mario (dipendente di Acme)
> - **Tenant** = Acme Corp (l'organizzazione che contiene Mario)

##### 2. Ogni Tenant Ha i Suoi Dati Completamente Segregati

Dentro il database, **ogni tabella** ha una colonna che identifica il proprietario:
```
users
├─ id: 1, tenant_id: acme-corp, name: Mario
├─ id: 2, tenant_id: acme-corp, name: Luigi
├─ id: 3, tenant_id: beta-inc, name: Anna
```

Quando Mario (tenant A) chiede "chi sono i miei colleghi?", il backend filtra:
```sql
SELECT * FROM users WHERE tenant_id = 'acme-corp';
```
Mario vede 2 persone. Non sa che Anna esiste.

==**Questo vale per OGNI dato:**==

- Utenti
- Ordini
- Configurazioni
- Messaggi
- Cronologia
- Log di audit

Tutto ha la colonna `tenant_id` e tutto viene filtrato automaticamente.

##### 3. Dall'Esterno Sembra Privato (Ma Non Lo È)

Questo è il trucco elegante della multi-tenancy.

Quando Mario entra in iam-mo, vede:

- 100 colleghi (SOLO i suoi)
- 50 ruoli definiti (SOLO i suoi)
- 1000 ordini elaborati (SOLO i suoi)
- Configurazioni personalizzate (SOLO le sue)

==**Sembra di avere un'istanza privata e dedicata.**==

In realtà:

- ==**Fisicamente**: condivide l'app con Beta Inc, Google, Microsoft, e altri 1000 tenant==
- ==**Ma i dati sono segregati così bene che non lo sa**==

È come una illusione architettonica — perfettamente sicura, ma invisibile.
#### Analogia Pratica: Hotel

Il modo più veloce di spiegare a qualcuno cos'è un tenant:

Immagina un grande hotel internazionale con 100 stanze.
```
HOTEL HILTON ROMA (Istanza fisica unica)
│
├─ Stanza 201 (Tenant A)
│  ├─ 2 ospiti: Mario, Luigi
│  ├─ Effetti personali privati
│  ├─ Cassaforte con soldi
│  └─ Non sa che la 202 esiste
│
├─ Stanza 202 (Tenant B)
│  ├─ 1 ospite: Anna
│  ├─ Effetti personali privati
│  └─ Non sa che la 201 esiste
│
├─ ... altre stanze ...
```

==**L'hotel è l'applicazione.**== ==**Ogni stanza è un tenant.**==

**Cosa è condiviso (infrastruttura)?**

- Riscaldamento centrale
- Acqua calda
- Ascensore
- Reception
- Piscina

**Cosa è privato (dati)?**

- Il contenuto della stanza (soldi, documenti, effetti personali)
- Il numero di telefono della stanza
- Le preferenze (non disturbare, sveglia alle 7)

L'ospite della 201 non scende in ascensore e pensa "chissà cosa c'è nelle altre stanze". ==**Sa che l'hotel è condiviso, ma i suoi spazi rimangono privati.**==

Allo stesso modo in iam-mo:

- ==**Condiviso**: server, rete, database fisico==
- ==**Privato**: i dati di ogni tenant (utenti, ruoli, permessi)==

##### Perché Non È Triviale

Potrebbe sembrare semplice — aggiungi una colonna `tenant_id` e filtri sempre. Ma ci sono **insidie** che rendono la multi-tenancy un'architettura delicata:

**Insidia 1: Dimenticare il Filtro**

```java
// ❌ SBAGLIATO
public List<User> getUsers() {
    return repository.findAll();
}

// Restituisce TUTTI gli utenti di TUTTI i tenant!
// Mario vedrebbe i dati di Anna (VIOLAZIONE!)
```

**Insidia 2: Caching Incrociato:**
```java
// ❌ SBAGLIATO
@Cacheable("users")
public List<User> getUsers() { ... }

// Restituisce lo stesso cache per tutti i tenant!
// Mario vede gli utenti di Beta Inc nel suo cache.
```

**Insidia 3: Bug nel Context**  
Se non propagi correttamente il tenant ID tra microservizi, il servizio B potrebbe processare i dati con il tenant sbagliato.

> [!warning] **Per questo la multi-tenancy deve essere architettuale**  
> Non è qualcosa che aggiungi dopo. Deve essere disegnata da subito, perché:
> 
> - Ogni query assume il filtro tenant
> - Ogni cache è isolato per tenant
> - Ogni microservizio propaga il tenant ID
> - Ogni test verifica l'isolamento

> [!example] **Riepilogo**
> 
> 
> Un **tenant** è:
> 
> - ✅ Un cliente/organizzazione dentro la tua applicazione
> - ✅ Ha i suoi dati completamente segregati da altri tenant
> - ✅ Vede l'app come se fosse privata (ma non lo è)
> - ✅ Condivide l'infrastruttura con altri tenant
> - ⚠️ L'isolamento è garantito da filtri `tenant_id` su OGNI query

Quando capisci questo, capisci tutto della multi-tenancy. Il resto è implementazione.
### Il Problema della Multi-Tenancy

Ora che abbiamo capito cosa sia un tenant, emerge una domanda: ==**perché abbiamo bisogno di disegnare la multi-tenancy con cura?**==

La risposta è semplice: ==**perché senza attenzione, le cose possono andare terribilmente male.**==

Quando Slack, Shopify, etc. servono milioni di utenti in contemporanea, ogni scelta architetturale ha conseguenze enormi. Ci sono tre categorie di problemi che emergono:

#### 1. **Data Leakage — Fuga di Dati**
Immagina questo scenario: uno sviluppatore  sta scrivendo una feature per recuperare la lista degli ordini di un tenant. Scrive:
```java
public List<Order> getOrders() {
    return repository.findAll();  // ❌ SBAGLIATO
}
```
Una query innocente. Innocente perché dimentica il filtro del tenant.

Cosa succede? Quando Mario di Acme Corp chiede la lista dei suoi ordini, il backend:

```sql
SELECT * FROM orders;  -- ❌ Non c'è il WHERE tenant_id!
```

Restituisce **TUTTI gli ordini di TUTTI i tenant**. Mario vedrebbe gli ordini segreti di Beta Inc. Beta Inc vedrebbe gli ordini di Google. Google vedrebbe gli ordini di Microsoft.

> [!warning] **Questo non è un bug minore**  
> È una **violazione di privacy totale**. È il tipo di bug che:
> 
> - Finisce nelle notizie ("App di gestione utenti espone dati di migliaia di aziende")
> - Viola leggi come il GDPR (fino a 20 milioni di euro di multa)
> - Distrugge la reputazione dell'azienda

La cosa insidiosa? ==**Questo bug è facile da fare.**== Se scrivi 100 query, e 99 hanno il filtro corretto ma una no, quella una query diventa una bomba di sicurezza.

In un ==**sistema mono-tenant questo problema semplicemente non esiste**==. Se l'app serve solo Acme Corp, allora `SELECT * FROM orders` è perfettamente logico — gli ordini sono sempre di Acme.

Ma in un sistema multi-tenant, ==**il filtro `WHERE tenant_id = ?` non è opzionale, è obbligatorio.**==

> [!example] **Analogia:**  
> È come guidare in una strada dove ci sono 1000 case mescolate insieme. Se non guidi con attenzione e colpisci la casa sbagliata, caos totale. In una strada con una sola casa, non c'è problema.
#### 2. **Performance Degradation — Degradazione delle Performance**

Facciamo un altro scenario. Immagina che iam-mo abbia due tenant:

- **Acme Corp**: 500 utenti, attività normale
- **MegaTech**: 50.000 utenti, società che cresce velocemente

Tutto è bello finché non arriva il giorno in cui MegaTech deve importare la nómina di 50.000 dipendenti nel sistema. Nel giro di 10 minuti, MegaTech genera:

- 50.000 query per creare utenti
- 50.000 query per assegnare ruoli
- 50.000 query per aggiungere al gruppo default
- Centinaia di migliaia di operazioni di logging e audit

==**Le risorse del database sono congestionate.**== Gli altri tenant — Acme Corp, Beta Inc, tutti gli altri — vedono le loro query rallentare drammaticamente.

Cosa vede l'utente di Acme Corp?

- Prima: carica la lista degli utenti in 100ms
- Dopo: carica la lista degli utenti in 5 secondi

Non sa che MegaTech sta facendo un import massivo. Per lui, l'app semplicemente è diventata lentissima.

> [!info] **Il problema del "noisy neighbor"**  
> È esattamente come avere coinquilini che fanno rumore di notte.  
> Tu vuoi dormire (eseguire query veloce), ma il tuo vicino sta facendo musica alta (eseguire un import massiccio).  
> Entrambi condividete le stesse risorse (le pareti dell'appartamento, il database), e il comportamento dell'uno impatta l'altro.

In un'architettura multi-tenant con una singola istanza di database, ==**non puoi isolare le risorse di un tenant dagli altri**==. Se Acme ha il 10% del carico ma occupa il 90% del CPU del database, gli altri ne soffrono.

Questo non succede nei sistemi mono-tenant — ogni cliente ha il suo server dedicato, quindi i rallentamenti di uno non impattano gli altri.

> [!example] **Come si risolve:**  
> Ci sono tecniche avanzate — rate limiting per tenant, isolamento delle risorse con Kubernetes, load balancing intelligente — ma tutte richiedono disegno deliberato. Non è automatico.
#### 3. **Compliance e Residenza Dati**

Ora consideriamo un aspetto legale che spesso viene sottovalutato.

Immagina che iam-mo voglia espandersi in Europa, in Russia e in Cina. Tre clienti:

- **EuroTech** (Italia) — ha il diritto che i dati rimangano in Europa (GDPR)
- **RussiaCorp** (Russia) — le leggi richiedono che i dati rimangano in Russia
- **ChinaTech** (Cina) — le leggi richiedono che i dati rimangano in Cina

Se iam-mo usa un ==**database unico in una sola region (ad esempio, AWS us-east-1)**==, allora:
```txt
Database unico (AWS Virginia, USA)
├─ EuroTech (dati in USA, non in Europa) ❌ VIOLA GDPR
├─ RussiaCorp (dati in USA, non in Russia) ❌ VIOLA legge russa
├─ ChinaTech (dati in USA, non in Cina) ❌ VIOLA legge cinese
```

Tecnicamente, il backend filtra correttamente — EuroTech non vede i dati di RussiaCorp. Ma ==**fisicamente, i dati sono tutti nello stesso posto (USA)**==, il che viola le leggi sulla sovranità dati di questi paesi.

> [!warning] **Le conseguenze legali sono serie:**
> 
> - GDPR (Europa): fino a 20 milioni di euro di multa
> - Leggi sulla sovranità (Russia, Cina): blocco del servizio, sanzioni commerciali
> - Clienti che se ne vanno: se un cliente scopre che i suoi dati non sono nel suo paese, cambia fornitore

**La soluzione?** Devi avere ==**database in regioni diverse**, segregati per tenant== — così EuroTech ha i dati in Europa, RussiaCorp in Russia, ecc.

Ma questo introduce complessità operativa enorme: come sincronizzi i dati? Come gestisci il backup? Come monitorizzi la salute di 100 database in 50 paesi diversi?

> [!example] **Chi ha questo problema nella realtà:**
> 
> - Slack: ha datacenter in US, EU, e Asia
> - Microsoft 365: ha dati replicati in diverse regioni
> - Google Cloud: offre servizi multi-region proprio per questo

### Le Tre Strategie di Isolamento dei Dati

Ora che sappiamo cosa sia un tenant e quali siano i rischi, emerge una domanda fondamentale:

> ==**Dove e come organizziamo fisicamente i dati dei tenant?**==

Questa decisione è ==**la più importante che farai nella progettazione**== perché ha conseguenze enormi su sicurezza, costo, compliance e operazioni.

Esistono tre approcci, e ognuno rappresenta un diverso equilibrio tra isolamento e complessità.

#### Opzione 1: **Database per Tenant — Massimo Isolamento**

**Immagina questa architettura:**
```txt
Tenant A (Acme Corp) ──→ Database A (postgres-acme)
Tenant B (Beta Inc)  ──→ Database B (postgres-beta)
Tenant C (Google)    ──→ Database C (postgres-google)
```

- ==Ogni tenant ha un **database completamente separato** — non condivide nulla con gli altri==
- ==Quando un nuovo tenant si registra, viene creato un nuovo database dedicato==
**Come funziona il backend?**
```java
// Quando Mario di Acme Corp fa login
String tenant = "acme-corp";

// Il backend sa: "Acme Corp usa il database postgres-acme"
String dbUrl = registry.getDatabase(tenant);
// jdbc:mysql://db-acme.internal/iam_mo

DataSource ds = connectionPool.get(dbUrl);
// Si connette al database di Acme

// La query
repository.findUsers(ds);  // Legge dal database di Acme
```

Mario vede solo i dati nel database di Acme. Anna di Beta Inc legge dal database di Beta. I due database non comunicheranno mai.

**Cosa Rende Questo Approccio Forte?**

> [!done] **Sicurezza Assoluta**
> 
> Anche se uno sviluppatore scrive `SELECT * FROM users;` senza filtro tenant, ==**il risultato è sempre isolato**== perché Mario è connesso al database di Acme e non può leggere da Beta.
> 
> Non c'è modo di fare data leakage tra tenant, perché fisicamente i dati non condividono nemmeno il database.

> [!done] **Compliance Totale**
> 
> Se la legge dice "i dati di EuroTech devono stare in Europa", metti semplicemente il database di EuroTech in AWS Europa. I dati di ChinaTech in AWS Asia. Semplice.

> [!done] **Nessun Noisy Neighbor**
> 
> Se MegaTech importa 50.000 utenti e intasa il database, ==**impatta solo il database di MegaTech.**== Acme Corp continua a funzionare normalmente nel suo database.

**Cosa Rende Questo Approccio Difficile?**

> [!failure] **Complessità Operativa Massima**
> 
> Immagina che SiliconDev ha 1000 tenant. Significa gestire 1000 database diversi:
> 
> - Monitorare la salute di 1000 database
> - Fare backup di 1000 database
> - Aggiornare lo schema SQL su 1000 database contemporaneamente
> - Trovare i bug in 1000 database diversi

> [!failure] **Costo Elevato**
> 
> Ogni database ha overhead — memoria, CPU, storage dedicati. Moltiplicato per 1000 tenant = costo gigantesco.

> [!failure] **Migrazioni Complesse**
> 
> Se scopri un bug nel schema (es. "ho dimenticato un indice"), devi aggiornaare 1000 database. Se sbagli, 1000 tenant sono offline.

> [!info] **Quando Ha Senso Usarla?**
> 
> - ==Clienti enterprise (banche, ospedali, assicurazioni)==
> - ==Pochi tenant (decine, al massimo centinaia)==
> - ==Quando la compliance vale più dell'operazione (e lo è, per una banca)==

#### Opzione 2: **Schema per Tenant — Isolamento Intermedio**

**Architettura:**
```css
┌─────────────────────────────────────┐
│  Database Unico (postgres-shared)   │
│                                     │
│  ├─ Schema acme_corp                │
│  │  └─ tables: users, orders, ...   │
│  │                                  │
│  ├─ Schema beta_inc                 │
│  │  └─ tables: users, orders, ...   │
│  │                                  │
│  └─ Schema google                   │
│     └─ tables: users, orders, ...   │
└─────────────────────────────────────┘
```

- Unico **database condiviso**, ma **uno [[Introduzione a SQL e il DDL#Gli schemi|schema SQL]] per ogni tenant**
- ==Quando un nuovo tenant si registra, viene creato un nuovo schema nello stesso database==


```sql
-- Database: ecommerce_platform

-- Schema per tenant Apple Inc.
CREATE SCHEMA tenant_apple;
CREATE TABLE tenant_apple.orders (id, amount, ...);

-- Schema per tenant Microsoft Corp
CREATE SCHEMA tenant_microsoft;
CREATE TABLE tenant_microsoft.orders (id, amount, ...);
```

==**Un database, ma logicamente diviso in schemi SQL.**== Uno schema per tenant.

Quando Mario fa login:
```java
String tenant = "acme-corp";

// Il backend sa: "Acme usa lo schema acme_corp nel database shared"
String schema = registry.getSchema(tenant);
// "acme_corp"

// La query sa quale schema usare
repository.findUsers(schema);
// SELECT * FROM acme_corp.users
```
nna di Beta Inc, nello stesso momento, legge da `beta_inc.users`. Stesso database fisicamente, ma schemi SQL diversi.

**Cosa Rende Questo Approccio Interessante?**

> [!done] **Isolamento Buono**
> 
> Uno schema offre una barriera logica forte. Se uno sviluppatore dimentica di specificare lo schema, di solito riceve un errore — ==**non legge silenziosamente dall'altro tenant**.==

> [!done] **Costo Moderato**
> 
> Un solo database da gestire. Monitoraggio unificato. Backup unificato. Costi infrastrutturali molto più bassi.

> [!done] **Operazioni Semplificate**
> 
> Aggiungi un nuovo tenant? Crea uno schema nuovo. Aggiorna lo schema? Una singola migrazione SQL su un database, ma eseguita su tutti gli schemi.

**Cosa Rende Questo Approccio Rischioso?**

> [!failure] **Isolamento Non Totale**
> 
> Un amministratore del database potrebbe accidentalmente connettersi al database e vedere tutti gli schemi. I dati rimangono logicamente segregati, ma non fisicamente.

> [!failure] **Noisy Neighbor Ancora Presente**
> 
> Se MegaTech importa 50.000 utenti nello schema `megatech`, congestionano il CPU e memoria del database condiviso. Gli altri tenant ne soffrono.

> [!failure] **Compliance Parziale**
> 
> Se la legge richiede che i dati italiani stiano in Italia, ma il tuo database shared è in USA... non puoi garantirlo. Tutti gli schemi condividono la stessa localizzazione.

> [!info] **Quando Ha Senso Usarla?**
> 
> - ==SaaS con centinaia di tenant (non migliaia)==
> - ==Quando compliance non richiede isolamento totale==
> - ==Buon equilibrio tra operazioni e sicurezza==


#### 3. **Row-Level Multi-Tenancy — Isolamento Minimo**

**Architettura:**
```css
┌──────────────────────────────────┐
│  Database Unico                  │
│  ├─ Tabella users                │
│  │  ├─ id: 1, tenant_id: acme,... │
│  │  ├─ id: 2, tenant_id: acme,... │
│  │  ├─ id: 3, tenant_id: beta,... │
│  │  └─ id: 4, tenant_id: beta,... │
│  │                               │
│  ├─ Tabella orders               │
│  │  ├─ id: 1, tenant_id: acme,... │
│  │  ├─ id: 2, tenant_id: beta,... │
│  │  └─ id: 3, tenant_id: google...│
└──────────────────────────────────┘
```

- ==**Una sola tabella per tutti i tenant**, con una colonna `tenant_id` che distingue i proprietari.==

```sql
-- Una sola tabella per TUTTI i tenant
CREATE TABLE orders (
  id INT,
  tenant_id STRING,  -- <-- Questo identifica il proprietario
  amount DECIMAL,
  ...
);

-- Dati di Apple
INSERT INTO orders (id, tenant_id, amount) VALUES (1, 'apple', 100);

-- Dati di Microsoft
INSERT INTO orders (id, tenant_id, amount) VALUES (2, 'microsoft', 200);
```

Quando Mario chiede gli utenti di Acme:
```sql
SELECT * FROM users WHERE tenant_id = 'acme-corp';
```

Quando Anna chiede gli utenti di Beta:
```sql
SELECT * FROM users WHERE tenant_id = 'beta-inc';
```
Stesso database, stessa tabella, ma filtrato per tenant.

**Cosa Rende Questo Approccio Attraente?**

> [!done] **Semplicità Operativa Massima**
> 
> Un database. Una tabella per ogni entità. Monitoraggio semplice. Backup semplice. Aggiungere un nuovo tenant richiede solo un INSERT, non la creazione di infrastruttura.

> [!done] **Costo Minimo**
> 
> Una sola istanza di database, dimensionata per il carico totale. Scalabilità orizzontale: aggiungi tenant senza aggiungere infrastruttura.

> [!done] **Analytics Unificato**
> 
> Una singola query può analizzare tutti i dati di tutti i tenant:
> 
> sql
> 
> ```sql
> SELECT tenant_id, COUNT(*) FROM users GROUP BY tenant_id;
> ```

**Cosa Rende Questo Approccio Pericoloso?**

> [!failure] **Il Filtro È Obbligatorio, Sempre**
> 
> Ogni query deve includere `WHERE tenant_id = ?`. Non c'è eccezione, non c'è default. ==**Se uno sviluppatore dimentica, la data leakage è garantita.**==

> [!failure] **Rischio Di Leakage Massimo**
> 
> Una sola query sbagliata e Mario vede i dati di Beta Inc:
> 
> sql
> 
> ```sql
> -- ❌ SBAGLIATO
> SELECT * FROM users;  -- Restituisce TUTTI gli utenti
> ```

> [!failure] **Niente Isolamento Infrastrutturale**
> 
> Se uno hacker accede al database, vede tutto. Non c'è niente che lo blocca. Con database per tenant, potrebbe leggere solo un database.

> [!failure] **Performance Degrade Col Tempo**
> 
> Con milioni di righe nella tabella, persino con indici su `tenant_id`, le query diventano più lente. Devi pagare il costo di filtrare milioni di righe ogni volta.

> [!info] **Quando Ha Senso Usarla?**
> 
> - ==SaaS in fase early-stage (pochi tenant)==
> - ==Sistemi interni che servono dipartimenti diversi della stessa azienda==
> - ==Quando il rischio di security è accettabile==

> [!example] **Le Tre Strategie a Confronto**
> 
> 
>
>
> | Aspetto                | Database per Tenant | Schema per Tenant   | Row-Level        |
> |------------------------|-------------------|-------------------|------------------|
> | **Isolamento Dati**    | Massimo ✅✅✅       | Buono ✅✅          | Fragile ⚠️       |
> | **Compliance**         | Ottima ✅✅✅        | Buona ✅✅          | Difficile ⚠️      |
> | **Costo Operativo**    | Alto ❌❌❌          | Medio ✅            | Basso ✅✅✅      |
> | **Numero Tenant**      | Decine             | Centinaia          | Migliaia         |
> | **Facilità Migrazione**| Difficile          | Media              | Facile ✅✅✅      |
> | **Performance**        | Ottima ✅✅✅        | Buona ✅✅          | Degrade con vol. |
> 

---

## La Multi-Tenancy nei Microservizi

Finora abbiamo parlato di multi-tenancy come se fosse **un'applicazione monolitica** — un backend unico che gestisce le richieste.

Ma ricordi [[Lezione 2 - Architetture dei microservizi#Architettura Interna|l'architettura dei microservizi]]? Non c'è una sola applicazione — ce ne sono decine, ognuna autonoma, ognuna con il proprio database.

Adesso aggiungiamo la multi-tenancy a questo quadro.

La domanda diventa: ==**come garantiamo che il tenant ID sia rispettato quando le richieste passano da un microservizio all'altro?**==

#### Cosa Cambia nei Microservizi?

In un'architettura monolitica la multi-tenancy è **localizzata**:

```
[Client] ──→ [App Monolitica] ──→ [Database]
            (estrae tenant, filtra, finito)
```

In un'architettura a microservizi, è **distribuita**:**
```
[Client] ──→ [Gateway] ──→ [Service A] ──→ [Database A]
                              ↓
                         [Service B] ──→ [Database B]
                              ↓
                         [Service C] ──→ [Database C]
```


Ogni servizio:

- Riceve una richiesta (che deve sapere a quale tenant appartiene)
- Deve filtrare i dati per quel tenant
- Se chiama un altro servizio, deve passargli l'informazione del tenant
- Il prossimo servizio deve fare lo stesso

==**Il tenant ID non rimane nello stesso processo — deve viaggiare attraverso la rete.**==

#### Il Flusso Concreto

Facciamo un esempio pratico. Immagina un e-commerce multi-tenant con tre servizi:

- **Servizio Ordini** — crea e gestisce gli ordini
- **Servizio Catalogo** — recupera i dettagli dei prodotti
- **Servizio Pagamenti** — elabora i pagamenti

Mario di Apple vuole creare un ordine.
Step 1: Mario Si Loga
```
Mario apre l'app e inserisce credenziali
┌─────────────────────────────┐
│ Username: mario             │
│ Password: ***               │
│ Tenant: apple (ricordato)   │
└─────────────────────────────┘
```
Il backend verifica Mario nel database di Apple (o nello schema apple, o con filtro `WHERE tenant_id = 'apple'` — dipende dalla strategia scelta).

Il backend crea un [[JWT - JSON Web Token#Cosa sono i JWT|JWT token]] che contiene:
```json
{
  "user_id": 1,
  "username": "mario",
  "tenant_id": "apple",     // ← QUI! Il tenant è nel token
  "exp": 1234567890
}
```

Mario riceve il token e lo salva nel suo dispositivo.
Step 2: Mario Crea un Ordine
```
Mario apre il carrello e clicca "Paga"

[App] invia:
POST /api/orders
Authorization: Bearer eyJ0ZW5hbnRfaWQ6ImFwcGxlIiwi...
Body: { items: [123, 456] }
```

La richiesta arriva al **[[Lezione 6 - API#API (Application Programming Interface)|API]] [[Lezione 2 - Architetture dei microservizi#Il Gateway|Gateway]]**.
Step 3: Il Gateway Estrae il Tenant dal Token
```java
@Component
public class TenantMiddleware {
    @Before
    public void intercept(HttpRequest request) {
        // Estrae il token
        String token = request.getHeader("Authorization");
        
        // Estrae il tenant dal token (perché è dentro, firmato)
        String tenantId = parseToken(token).getTenantId();  // "apple"
        
        // Lo mette in un context che è disponibile a TUTTI i servizi
        TenantContext.set(tenantId);  // ← Disponibile ovunque da qui in poi
    }
}
```

==**Da questo momento, il tenant ID è disponibile in tutto lo stack.**==

Step 4: Il Servizio Ordini Riceve la Richiesta

```java
@RestController
public class OrdersController {
    @PostMapping("/orders")
    public Order createOrder(@RequestBody CreateOrderRequest request) {
        // Non ha bisogno di passare tenantId come parametro!
        String tenantId = TenantContext.get();  // "apple"
        
        return orderService.createOrder(request, tenantId);
    }
}

@Service
public class OrderService {
    public Order createOrder(CreateOrderRequest request, String tenantId) {
        // Crea l'ordine con il tenant ID
        Order order = new Order(tenantId, request.getItems());
        
        // Chiama il servizio Catalogo per i dettagli
        for (Integer productId : request.getItems()) {
            Product product = catalogService.getProduct(productId);
            // ← Il servizio Catalogo deve sapere il tenant!
        }
        
        return repository.save(order);
    }
}
```

Step 5: Il Servizio Catalogo Riceve la Richiesta (da Ordini)
```java
// Nel servizio Ordini
Product product = catalogService.getProduct(productId);

// In realtà, dietro le quinte:
Product product = restClient.get(
    "http://catalog-service/api/products/" + productId
);
```

Il servizio Catalogo riceve la richiesta e... ==**deve sapere che è un ordine di Apple, non di Microsoft.**==

Come lo sa? Il context viene propagato automaticamente! Se usi Spring Cloud o framework moderni per microservizi, il `TenantContext` viene automaticamente passato nella richiesta (come header nascosto).
```java
@RestController
public class CatalogController {
    @GetMapping("/products/{id}")
    public Product getProduct(@PathVariable Integer id) {
        String tenantId = TenantContext.get();  // "apple" (automaticamente!)
        
        // Filtra per tenant
        return repository.findByIdAndTenantId(id, tenantId);
    }
}
```

**Step 6: Il Servizio Pagamenti Elabora il Pagamento**

Quando Ordini chiama Pagamenti:
```java
// Nel servizio Ordini
paymentService.processPayment(order, paymentInfo);

// Nel servizio Pagamenti
@Service
public class PaymentService {
    public void processPayment(Order order, PaymentInfo info) {
        String tenantId = TenantContext.get();  // "apple" (propagato!)
        
        // Registra il pagamento filtrando per tenant
        Payment payment = new Payment(
            tenantId,
            order.getId(),
            info.getAmount()
        );
        
        repository.save(payment);
    }
}
```

Il diagramma completo:
```css
┌─ Client (Mario) 
│  invia JWT con tenant_id="apple"
│
├─→ API Gateway
│   estrae tenant dal token
│   lo mette in TenantContext
│
├─→ Servizio Ordini
│   legge TenantContext.get() = "apple"
│   crea ordine con tenant_id = "apple"
│   chiama Servizio Catalogo
│
├─→ Servizio Catalogo
│   riceve la richiesta (il context è propagato!)
│   legge TenantContext.get() = "apple"
│   restituisce prodotti di Apple
│
└─→ Servizio Pagamenti
   riceve la richiesta
   legge TenantContext.get() = "apple"
   processa pagamento per Apple
```


#### I Tre Pilastri dell'Architettura Multi-Tenant

Ora che vedi il flusso, emerge che ci sono tre cose critiche che devono funzionare insieme:

##### Pilastro 1: Identificazione Iniziale del Tenant

Il sistema deve capire "questa richiesta è di Apple, non di Microsoft" **prima** che [[Lezione 2 - Architetture dei microservizi#Il Gateway|il Gateway]] inoltri la richiesta.

==**La scelta più sicura è il [[JWT - JSON Web Token#Cosa sono i JWT|JWT]].**==

Perché? Perché il tenant ID è **firmato dentro il token**. Mario non può mentire e dire "sono Apple" se non ha un token valido di Apple.

```
Opzione A: Header casuale (RISCHIOSA)
GET /api/orders
X-Tenant-ID: apple  ← Mario potrebbe cambiarla!

Opzione B: JWT (SICURA)
GET /api/orders
Authorization: Bearer eyJ0ZW5hbnRfaWQ6ImFwcGxlIiwiYWxnIjoiSFMyNTYi...
                      ↑
                   Firmato con chiave segreta!
                   Mario non può falsificarla
```

Nel secondo caso, il server verifica la firma del token. Se Mario prova a falsificarlo, il token non è valido e viene rifiutato.

##### Pilastro 2: Propagazione Automatica

Una volta che il tenant ID è nel context del Gateway, ==**deve rimanere disponibile in TUTTI i servizi che lo usano**==, senza che lo debbano passare manualmente ogni volta.

Tecnologie come **Spring Cloud** o **OpenTelemetry** fanno esattamente questo — propagano il context automaticamente attraverso le richieste HTTP tra servizi.

Se non fosse automatico, ogni servizio dovrebbe fare:
```java
// ❌ TEDIOSO E FRAGILE
paymentService.process(order, tenantId);  // Lo passo manualmente
catalogService.getProduct(id, tenantId);  // Lo passo manualmente
deliveryService.ship(id, tenantId);       // Lo passo manualmente
// ... e se ne dimentico uno? Data leakage!
```

Con la propagazione automatica:

```java
// ✅ AUTOMATICO E SICURO
String tenantId = TenantContext.get();  // Lo leggo dovunque
// Niente parametri aggiuntivi, il sistema se ne occupa
```

##### Pilastro 3: Filtraggio Coerente

Ogni microservizio deve applicare la strategia di isolamento scelto (database per tenant, schema, o row-level) **nello stesso modo**.

Se Ordini usa row-level (un database, colonna `tenant_id`), allora Catalogo deve usare lo stesso. Altrimenti uno servizio filtra correttamente e l'altro no.
```java
// Tutti i servizi DEVONO fare così
String tenantId = TenantContext.get();
return repository.findByTenantId(tenantId);  // Sempre presente
```

Se uno servizio dimenticasse il filtro:
```java
// ❌ SBAGLIATO
return repository.findAll();  // Restituisce TUTTI i dati
```

Allora Mario vedrebbe i prodotti di Microsoft, i pagamenti di Google, tutto.

#### Riepilogo

La multi-tenancy nei microservizi richiede **tre cose che devono funzionare insieme**:

1. ✅ ==**Identificazione sicura**: il tenant ID nel JWT, firmato==
2. ✅ ==**Propagazione automatica**: il context disponibile ovunque==
3. ✅ ==**Filtraggio coerente**: ogni servizio applica lo stesso schema di isolamento==

Se una di queste manca, il sistema fallisce.

Se tutte e tre funzionano, allora Mario di Apple vede solo i dati di Apple, Anna di Microsoft vede solo quelli di Microsoft, e nessuno sa che stanno usando la stessa applicazione.
