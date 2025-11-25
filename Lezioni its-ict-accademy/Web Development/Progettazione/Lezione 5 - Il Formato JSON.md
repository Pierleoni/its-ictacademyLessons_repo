# **Introduzione: dal protocollo HTTP allo scambio dei dati**

Nella [[Lezione 4 - Protocollo HTTP 2 parte|lezione precedente]] abbiamo visto come funziona la comunicazione tra _[[Lezione 4 - Protocollo HTTP 2 parte#^client|client]]_ e _[[Lezione 4 - Protocollo HTTP 2 parte#^server|server]]_ tramite il protocollo HTTP: ogni richiesta e risposta contiene un **[[Lezione 4 - Protocollo HTTP 2 parte#^header|header]]**, che trasporta metadati, e un **[[Lezione 4 - Protocollo HTTP 2 parte#^body|body]]**, che contiene l’eventuale contenuto vero e proprio.

Il body può trasportare informazioni in molti formati. Storicamente si è utilizzato spesso l’**XML**, un formato strutturato ma relativamente pesante. Con l’evoluzione delle architetture web, in particolare con l’affermazione delle API REST, è emersa la necessità di un formato:

- più leggero,
    
- più veloce da trasmettere,
    
- semplice da leggere e scrivere,
    
- facilmente gestibile nelle applicazioni JavaScript (ma non solo).
    

Per soddisfare queste esigenze si è affermato **JSON (JavaScript Object Notation)**, che oggi rappresenta il formato standard per lo scambio dei dati tramite HTTP in ambito web e REST.

## Cos’è il JSON e perché viene utilizzato
JSON è:
- ==un formato testuale utilizzato per rappresentare oggetti e strutture dati in modo semplice e compatto.== 
Pur essendo nato come derivazione della sintassi di JavaScript, è oggi indipendente dal linguaggio ed è supportato da qualunque tecnologia server-side e client-side.

I principali vantaggi sono:

- ==struttura leggibile e intuitiva;==
    
- ==peso ridotto rispetto all’XML;==
    
- ==perfetta compatibilità con JavaScript e framework frontend moderni;==
    
- ==facilità nell’essere serializzato e deserializzato dai principali linguaggi (Python, Java, PHP, ecc.).==

### **Struttura di un documento JSON**

Un oggetto JSON è racchiuso tra parentesi graffe `{ … }`.  
Al suo interno contiene **proprietà** espresse con la sintassi:

```json
"nome": valore
```

Le proprietà sono separate da virgole.

#### **Tipologie di valore accettate**

Un valore JSON può essere:

- un numero
    
- una stringa (sempre tra doppi apici `" "`)
    
- un valore booleano (`true` / `false`)
    
- `null`
    
- un **oggetto** JSON annidato
    
- un **array** (`[ ... ]`) contenente elementi dello stesso tipo o misti

###### Esempio di formato JSON 
```json
{
  "nome": "Mario",
  "eta": 25,
  "attivo": true,
  "indirizzo": {
    "via": "Roma 10",
    "citta": "Roma"
  },
  "interessi": ["musica", "programmazione", "sport"]
}
```

### JSON nelle richieste e risposte HTTP
Sia il _client_ sia il _server_ possono inviare e ricevere dati in formato JSON.  
Affinché la comunicazione sia corretta, è necessario dichiarare esplicitamente questo formato nell’header HTTP.

#### Dichiarare il formato JSON quando si inviano dati
Chi invia una richiesta o una risposta che contiene JSON **deve** dichiarare il `Content-Type`:

```json
Content-Type: application/json
```

==In questo modo l’interlocutore sa come interpretare il contenuto del body.==

#### Richiedere una risposta in formato JSON
Se il client desidera ricevere dal server una risposta in JSON, deve usare l’header:
```JSON
Accept: application/json
```
==Questo header indica quali formati di dato il client accetta come risposta.==  
==Il server, se supporta quel formato, restituirà i dati in JSON.==

#### Negoziazione del formato
Se il client specifica più formati (per esempio JSON, XML, HTML) e il server è in grado di gestirne più di uno, il server può scegliere liberamente quale restituire tra quelli accettati.


### Ruolo del JSON nello sviluppo moderno
JSON è oggi lo standard nelle API REST grazie ai suoi punti di forza:

- ==Consente trasferimenti più efficienti.==
    
- ==È semplice da generare lato server.==
    
- ==È immediatamente utilizzabile lato frontend.==
    
- ==Riduce l’overhead della comunicazione, migliorando la performance.==
    

Per questo motivo è considerato il formato ideale per lo scambio di dati strutturati nelle applicazioni web moderne, nei servizi mobili e nei microservizi.