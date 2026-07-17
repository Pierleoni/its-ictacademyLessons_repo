# Multi-Tenancy nei Microservizi

Finora abbiamo esplorato come strutturare un'applicazione a microservizi dal punto di vista **architetturale e operativo**: abbiamo visto [[Lezione 1 - Applicazioni cloud a microservizi#Cos'è un'Applicazione a Microservizi|come si organizzano i microservizi]], [[Lezione 2 - Architetture dei microservizi#Le Due Architetture dei Microservizi|come comunicano tra loro]], [[Lezione 3 - Progettazione_Dei__Microservizi#Esempio Pratico Food Delivery|come si progettano i confini tra servizi]].

Ma abbiamo fatto un'assunzione implicita che non sempre è vera: ==**abbiamo supposto che il sistema serva un'unica organizzazione, con un unico set di dati e un unico contesto di business.**==

Nella realtà commerciale però, soprattutto nel modello **SaaS** (Software as a Service), un'unica applicazione può servire **decine, centinaia, o addirittura migliaia di clienti diversi**. Amazon non gestisce ordini solo per se stesso — li gestisce per milioni di venditori. Slack non serve una sola azienda — serve centinaia di migliaia di workspace. Glovo non ha un unico ristorante — ne coordina decine di migliaia in decine di Paesi.

In questi scenari emerge un nuovo problema architetturale: **come garantiamo che i dati del cliente A rimangono completamente isolati dai dati del cliente B, anche se entrambi usano la stessa applicazione?**

Questa è la sfida della **Multi-Tenancy** — e come vedremo, ha implicazioni profonde su come progettiamo e implementiamo i nostri microservizi.

## Cos'è un Tenant?

Partiamo dalla definizione più semplice:

> ==**Un tenant è un'istanza logica della tua applicazione che appartiene a un cliente/organizzazione distinto.**==

Nel contesto di un'applicazione multi-tenant:

- **Tenant = Cliente/Organizzazione** — un'entità commerciale che usa il tuo sistema
- **Ogni tenant ha i suoi dati completamente segregati** — utenti, configurazioni, ruoli, permessi, cronologia, tutto
- ==**Dal punto di vista del tenant, sembra di avere un'istanza privata dell'applicazione** — anche se in realtà è condivisa con altri tenant==

### Analogia Pratica: Hotel

Immagina un hotel con 100 stanze. L'hotel è la tua applicazione. 
- Ogni stanza è un **tenant** — ha i suoi letti, i suoi asciugamani, la sua cassaforte con i soldi del cliente
- Ogni stanza è **isolata logicamente** dalle altre — l'ospite della stanza 201 non sa chi abita nella 305, e non può accedere ai suoi effetti personali
- ==L'hotel gestisce infrastrutture condivise (riscaldamento, acqua, elettricità) — ma ogni stanza rimane privata==

Allo stesso modo:
- La tua applicazione multi-tenant gestisce **infrastrutture condivise** (server, database, microservizi)
- Ma **ogni tenant ha i suoi dati completamente privati** — l'utente del tenant A non vede i dati del tenant B

## Il Problema della Multi-Tenancy

Senza un disegno deliberato della multi-tenancy, emergono rischi critici:

### 1. **Data Leakage — Fuga di Dati**

Immagina un bug nel codice dove una query dimentica il filtro `WHERE tenant_id = X`. 

```sql
-- SBAGLIATO: dimentica il filtro del tenant
SELECT * FROM orders;

-- Corretto
SELECT * FROM orders WHERE tenant_id = ?
```

==Il primo caso restituisce gli ordini di TUTTI i tenant — un disastro di sicurezza.==

In un sistema mono-tenant questo bug non existe nemmeno — non c'è nulla da filtrare. In un sistema multi-tenant è un pericolo costante.

### 2. **Performance Degradation — Degradazione delle Performance**

Se un tenant è molto attivo — millioni di query al secondo — può congestionare le risorse condivise e far rallentare gli altri tenant.

> ==**È il problema del "noisy neighbor"** — un vicino rumoroso che disturba chi gli sta accanto.==

### 3. **Compliance e Residenza Dati**

In molti Paesi (GDPR in Europa, leggi sulla sovranità dati in Russia/Cina), i dati di un cliente devono rimanere **fisicamente in una specifica regione geografica**.

Se i dati di tutti i tenant sono mischiati in un unico database in una sola region, ==non puoi garantire che il cliente italiano abbia i dati in Italia.==

### Le Tre Strategie di Isolamento dei Dati

Quando progettiamo la multi-tenancy, la decisione più importante è: **come isoliamo i dati tra tenant?**

Esistono tre approcci principali, ognuno con trade-off distinti:

#### 1. **Database per Tenant — Massimo Isolamento**

**Architettura:**
- ==Ogni tenant ha un **database completamente separato** — non condivide nulla con gli altri==
- ==Quando un nuovo tenant si registra, viene creato un nuovo database dedicato==

> [!done] **Vantaggi:**
> 
> - ✅ ==Isolamento totale — impossibile leakage di dati (anche con bug)==
> - ✅ ==Compliance massima — puoi mettere database in region diverse a seconda delle normative==
> - ✅ ==Performance: ogni tenant ha le proprie risorse dedicate, nessun noisy neighbor==
> - ✅ ==Backup selettivo — puoi fare backup di un singolo tenant senza toccare gli altri==

> [!failure] **Svantaggi:**
> 
> - ❌ ==Complessità operativa massima — devi gestire e monitorare migliaia di database==
> - ❌ ==Costo elevato — ogni database ha overhead di infrastruttura==
> - ❌ ==Migrazioni difficili — aggiornare uno schema su N database è complesso==
> - ❌ ==Monitoraggio difficile — è complicato avere una visione unificata della salute del sistema==

> [!info]  **Quando usarla:**
>
> - ==Clienti enterprise con altissimi requisiti di privacy/compliance (banche, ospedali)==
> - ==Numeri bassi di tenant (decine, al massimo centinaia)==
> - ==Quando il costo della non-compliance supera il costo operativo==
> 

#### 2. **Schema per Tenant — Isolamento Intermedio**

**Architettura:**
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

> [!done] **Vantaggi:**
> 
> - ✅ ==Isolamento buono — gli schemi SQL offrono una barriera logica==
> - ✅ ==Operazioni unificate — una singola query può operare su schemi diversi==
> - ✅ ==Migrazioni semi-semplificate — puoi migrare uno schema alla volta==
> - ✅ ==Costo moderato — una sola istanza di database per molti tenant==
> 

> [!failure]  **Svantaggi:**
>
> - ❌ ==Isolamento non totale — un admin database potrebbe vedere tutto accidentalmente==
> - ❌ ==Compliance parziale — i dati sono comunque nella stessa regione==
> - ❌ ==Condivisione risorse — il carico di un tenant continua a impattare gli altri==
> 

> [!info] **Quando usarla:**
> 
> - ==Applicazioni SaaS con volumi medi di tenant (centinaia)==
> - ==Quando compliance non richiede isolamento totale==
> - ==Buon equilibrio tra semplicità operativa e isolamento==
> 

#### 3. **Row-Level Multi-Tenancy — Isolamento Minimo**

**Architettura:**
- ==Unico database, **un'unica tabella per tutti i tenant**, con una colonna `tenant_id` che identifica il proprietario==

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

> [!done] **Vantaggi:**
> 
> - ✅ ==Semplicità operativa massima — un solo database da gestire==
> - ✅ ==Costo minimo — infrastruttura al minimo==
> - ✅ ==Scalabilità dei dati — aggiungi tenant senza creare nuove strutture==
> - ✅ ==Facilità di analytics — una query unificata vede tutti i dati==
> 

> [!failure] **Svantaggi**
> 
> - ❌ ==Isolamento fragile — il filtro `WHERE tenant_id = ?` deve essere messo **su ogni query**==
> - ❌ ==Rischio di leakage altissimo — un bug o uno sviluppatore distratto espone tutto==
> - ❌ ==Compliance difficile — non puoi garantire l'isolamento a livello infrastrutturale==
> - ❌ ==Performance degrade con volumi grandi — una tabella con miliardi di righe diventa lenta==
> 

> [!info]  **Quando usarla:**
>
> - ==Applicazioni SaaS in fase early-stage, con numero limitato di tenant==
> - ==Quando il rischio di security è accettabile==
> - ==Sistemi interni che servono diversi dipartimenti (non clienti esterni)==
> 


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

Nel contesto di un'architettura a microservizi, la multi-tenancy introduce complessità aggiuntive. 

Ricordi che in un'architettura a microservizi:
- ==**Ogni microservizio ha il proprio database dedicato**==
- ==**I microservizi comunicano tra loro tramite API o messaggi**==

Ora aggiungiamo la multi-tenancy:
- ==**Ogni tenant ha i propri dati segregati**==
- ==**Ogni microservizio deve rispettare questa segregazione**==

### Il Flusso di una Richiesta Multi-Tenant

Immagina un'applicazione di e-commerce con microservizi per catalogo, ordini e pagamenti. Un utente del tenant Apple vuole fare un ordine:

```
1. Client Apple invia richiesta al Gateway
   GET /api/orders
   Header: X-Tenant-ID: apple

2. Gateway riceve la richiesta
   - Estrae il tenant ID dall'header (apple)
   - Lo aggiunge al contesto della richiesta
   - Inoltra al microservizio Ordini

3. Microservizio Ordini riceve la richiesta
   - Legge il tenant ID dal contesto (apple)
   - Filtra AUTOMATICAMENTE: SELECT * FROM orders WHERE tenant_id = 'apple'
   - Restituisce solo gli ordini di Apple

4. Se il servizio Ordini deve chiamare il servizio Pagamenti:
   - DEVE propagare il tenant ID
   - Chiama: GET /api/payments?tenant_id=apple
   - Il servizio Pagamenti filtra di nuovo: WHERE tenant_id = 'apple'
```

==**Il concetto chiave: il tenant ID viene propagato attraverso TUTTA la catena di microservizi.**==

### I Tre Problemi Architetturali

#### Problema 1: Identificazione del Tenant

Come sa il sistema quale tenant sta facendo la richiesta? 

**Tre strategie:**

**a) Via Header HTTP**
```http
GET /api/orders
X-Tenant-ID: apple
```

>[!done] ✅ Semplice e chiaro

>[!failure] ❌ Il client deve mandarla sempre

>[!failure] ❌ Rischio di spoofing (un utente tenta di impersonare un altro tenant)

**b) Via [[JWT - JSON Web Token#Cosa sono i JWT|Token JWT]]**
```http
GET /api/orders
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInRlbmFudF9pZCI6ImFwcGxlIn0...
```
>[!done] ✅ Sicuro — il tenant ID è firmato nel token

>[!done] ✅ Il server lo estrae automaticamente

>[!failure] ❌ Complessità di autenticazione

**c) Via URL/Subdomain**
```http
apple.ecommerce.com/api/orders
microsoft.ecommerce.com/api/orders
```
> [!done] ✅ Sicuro e elegante

>[!failure] ❌ Devi gestire DNS per ogni tenant (complesso a scala)

>[!note] **In un'architettura a microservizi moderna, la scelta comune è il [[JWT - JSON Web Token#JSON Web Token|JWT]]** — ==il tenant ID viene incluso nel token di autenticazione e ogni microservizio lo estrae automaticamente.==

#### Problema 2: Propagazione Automatica del Tenant ID

Quando un microservizio chiama un altro microservizio, **il tenant ID deve essere propagato** — altrimenti il microservizio downstream non sa a quale tenant applicare i filtri.

**Soluzione: Context Propagation**

In linguaggi come [[Lezione 1 - Introduzione a Java|Java]], usi **AsyncLocalStorage** o **ThreadLocal** per mantenere il tenant ID disponibile in tutto lo stack:

```java
// Middleware del Gateway
@Component
public class TenantMiddleware {
    public void intercept(HttpRequest request) {
        String tenantId = extractTenantFromToken(request);
        TenantContext.set(tenantId);  // <-- Salva nel context
    }
}

// In qualsiasi microservizio, in qualsiasi profondità
public class OrderService {
    public List<Order> getOrders() {
        String tenantId = TenantContext.get();  // <-- Lo legge automaticamente
        return repository.findByTenantId(tenantId);  // <-- Lo usa per filtrare
    }
}

// Quando chiama un altro microservizio
public void createOrder(Order order) {
    String tenantId = TenantContext.get();
    // Passa il tenant ID al servizio Pagamenti
    paymentService.process(order, tenantId);
}
```

==**Il vantaggio: il filtro `WHERE tenant_id = X` diventa automatico, non opzionale.**==

#### Problema 3: Isolamento del Database

Una volta decisa la **strategia di isolamento** ([[#1. **Database per Tenant — Massimo Isolamento**|database per tenant]], [[#2. **Schema per Tenant — Isolamento Intermedio**|schema]], o [[#3. **Row-Level Multi-Tenancy — Isolamento Minimo**|row-level]]), **ogni microservizio deve implementarla coerentemente**.

Se usi **database per tenant** e il tenant Apple ha un database separato:

```java
// Al momento della connessione
String tenant = TenantContext.get();  // "apple"
String dbUrl = tenantRegistry.getDatabase(tenant);
// "jdbc:mysql://db-apple.internal/ecommerce"

DataSource ds = getDataSource(dbUrl);
// Dalla connessione al database di Apple
```

Se usi **row-level multi-tenancy**:

```java
// Tutte le query aggiungono automaticamente il filtro
public List<Order> getOrders() {
    String tenantId = TenantContext.get();
    return repository.findByTenantId(tenantId);  // Filtro obbligatorio
}
```

---

## Esempio Concreto: iam-mo e dashboard-mo in Multi-Tenant

Torniamo al contesto specifico di **iam-mo** (mobile IAM app) e **dashboard-mo** (dashboard).

Supponiamo che SiliconDev voglia vendere queste applicazioni come **SaaS** a varie aziende. Ogni azienda (cliente) è un **tenant**.

### Scenario

- **Tenant A: Acme Corp** — 500 utenti, con i loro ruoli e permessi
- **Tenant B: Beta Inc** — 200 utenti, con ruoli e permessi diversi
- ==**Entrambi usano la stessa istanza di iam-mo e dashboard-mo**==

### Architettura Multi-Tenant Proposta

**Identificazione del Tenant:**
- Quando un utente di Acme Corp si logga in iam-mo, riceve un JWT con `tenant_id: acme-corp`
- Il token viene allegato a ogni richiesta API

**Nel Backend:**
```
[Client iam-mo] ---- JWT(tenant: acme-corp) ----> [API Gateway]
                                                        |
                                                   [Estrae tenant dal JWT]
                                                   [Aggiunge al context]
                                                        |
                      ┌─────────────────────────────────┼─────────────────────────────────┐
                      |                                  |                                  |
              [Users Service]                  [Roles Service]                  [Groups Service]
              WHERE tenant_id = ?              WHERE tenant_id = ?              WHERE tenant_id = ?
```

**Isolamento Dati:**
- Usa **row-level multi-tenancy** con colonna `tenant_id` su tutte le tabelle (users, roles, groups, sites)
- Ogni query aggiunge `WHERE tenant_id = <current_tenant>`

```sql
-- Tabella Users
CREATE TABLE users (
  id INT,
  tenant_id STRING,  -- Acme Corp vs Beta Inc
  username STRING,
  email STRING,
  ...
);

-- Una query del servizio Users
SELECT * FROM users WHERE tenant_id = 'acme-corp' AND username = 'mario';
```

**Nel Frontend (iam-mo):**
- La schermata degli utenti mostra solo gli utenti del tenant corrente
- Il JWT contiene il tenant ID, quindi non serve richiederlo da UI

```typescript
// Nel servizio che chiama l'API
const headers = {
  'Authorization': `Bearer ${jwtToken}`,  // <-- Il JWT contiene tenant_id
};

// Il backend estrae il tenant dal JWT automaticamente
const response = await fetch('/api/users', { headers });
```

**Nel Dashboard (dashboard-mo):**
- L'admin del tenant vede i dati solo del suo tenant
- Stesso meccanismo — JWT + context propagation

---

## Considerazioni Implementative

### 1. **Sempre Filtrare**

==**La regola d'oro: TUTTI i filtri devono includere il tenant ID — non è opzionale.**==

Non scrivere mai:
```java
// ❌ SBAGLIATO
repository.findByUsername("mario");
```

Scrivi sempre:
```java
// ✅ CORRETTO
repository.findByTenantIdAndUsername(tenantId, "mario");
```

Considera di ==**forzare il filtro a livello di database**== con trigger o policy:

```sql
-- Trigger che forza il tenant_id
CREATE TRIGGER enforce_tenant
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  IF NEW.tenant_id IS NULL THEN
    RAISE ERROR 'tenant_id is required';
  END IF;
END;
```

### 2. **Testare il Fallimento**

I bug di multi-tenancy sono sottili — una query senza filtro passa inosservata fino a che non causa una data leakage.

==**Aggiungi test che verificano l'isolamento:**==

```java
@Test
public void shouldNotSeeTenantBDataFromTenantA() {
    // Crea ordini per Tenant A
    Order orderA = createOrder(tenantA, "order-1");
    
    // Crea ordini per Tenant B
    Order orderB = createOrder(tenantB, "order-2");
    
    // Quando Tenant A fa query
    TenantContext.set("tenant-a");
    List<Order> results = orderService.getOrders();
    
    // Dovrebbe vedere solo order-1
    assertEquals(1, results.size());
    assertEquals("order-1", results.get(0).getId());
}
```

### 3. **Monitoring e Observability**

==**Includi il tenant ID in tutti i log e nelle metriche.**==

```java
// Negli NDC (Nested Diagnostic Context) di logging
MDC.put("tenant", TenantContext.get());
logger.info("Order created");  // Il log conterrà il tenant ID

// Nelle metriche Prometheus
counter.labels(TenantContext.get(), "created").inc();
```

Questo permette di:
- Debuggare bug specifici a un tenant
- Monitorare il carico per tenant
- Rilevare anomalie (es. un tenant che improvvisamente genera 10x il traffico)

---

## Conclusione

La multi-tenancy è uno dei pattern più importanti nelle applicazioni SaaS moderne. 

Nel contesto di un'architettura a microservizi:
- ==**Il tenant ID deve permeare l'intero sistema** — dal Gateway fino al database==
- ==**L'isolamento dei dati non è facoltativo — deve essere forzato a livello architetturale**==
- ==**La scelta della strategia di isolamento (database vs schema vs row-level) ha implicazioni profonde su costo, compliance e operazioni**==

Per **iam-mo** e **dashboard-mo**, un approccio basato su **row-level multi-tenancy** con **JWT e context propagation** è una scelta razionale — bilancia semplicità, costo e isolamento adeguato per la maggior parte dei casi di SaaS.

Ma ricorda: ==**il costo della semplicità è la vigilanza costante sui filtri.**== Una singola query senza `WHERE tenant_id = ?` può diventare un disastro di security.
