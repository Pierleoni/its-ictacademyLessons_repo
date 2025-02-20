# Caratteristiche di Python 
### 1. **Sintassi semplice e leggibile**

- ==La sintassi di Python è chiara e minimalista, simile al linguaggio naturale, il che lo rende facile da apprendere per i principianti.==
- ==La sua leggibilità favorisce la manutenzione del codice e la collaborazione tra sviluppatori.==

### 2. **Versatilità**

- ==Python è un linguaggio multi-paradigma: supporta la programmazione procedurale, orientata agli oggetti e funzionale.==
- ==È utilizzato in molti ambiti, come sviluppo web, analisi dei dati, intelligenza artificiale, machine learning, automazione, sviluppo di applicazioni desktop e molto altro.==

### 3. **Ampia libreria standard**

- ==La libreria standard di Python offre moduli e funzioni pronti all'uso per compiti comuni, come la manipolazione di file, la gestione delle date, il networking e altro.==

### 4. **Ricca ecosistema di librerie e framework**

- ==Python dispone di un vasto ecosistema di librerie e framework specifici per ogni campo:==
    - **Machine Learning/AI**: TensorFlow, PyTorch, Scikit-learn.
    - **Analisi dei dati**: Pandas, NumPy, Matplotlib, Seaborn.
    - **Sviluppo web**: Django, Flask, FastAPI.
    - **Automazione**: Selenium, PyAutoGUI.
    - **Elaborazione di immagini**: OpenCV, PIL (Pillow).

### 5. **Community attiva e supporto**

- Python ha una delle community più grandi e attive al mondo. Questo si traduce in:
    - U==na grande quantità di documentazione e tutorial.==
    - ==Forum e gruppi di discussione dove trovare supporto.==
    - ==Molti pacchetti open-source sviluppati e mantenuti dalla community.==

### 6. **Portabilità**

- ==Python è multipiattaforma: il codice scritto in Python funziona su Windows, macOS e Linux senza bisogno di modifiche significative.==

### 7. **Interprete e sviluppo rapido**

- ==Essendo un linguaggio interpretato, Python permette di eseguire il codice direttamente senza doverlo compilare, accelerando il ciclo di sviluppo.==
- ==È ideale per prototipazione e sviluppo rapido di applicazioni.==

### 8. **Supporto per il testing**

- ==Python include strumenti e framework per il testing come `unittest`, `pytest` e `nose`, rendendo più facile lo sviluppo di codice robusto e affidabile.==

### 9. **Integrazione con altri linguaggi**

- ==Python può integrarsi facilmente con altri linguaggi come C, C++ (con strumenti come Cython o SWIG), e Java (tramite Jython), permettendo di ottimizzare parti critiche di un'applicazione.== 

### 10. **Adatto a diversi livelli di competenza**

- ==È adatto sia ai principianti, grazie alla sua semplicità, sia agli sviluppatori esperti, grazie alla sua flessibilità e alle sue potenzialità avanzate.==


# PEP (Python Enhancement Proposal)

**PEP** è l'abbreviazione di **Python Enhancement Proposal**. 
Un PEP è un documento di progettazione che informa la comunità Python o descrive una nuova funzionalità per Python, i suoi processi o il suo ambiente. 
Il PEP ==deve fornire una breve descrizione tecnica della funzione e il suo ragionamento==. I PEP sono intesi come i meccanismi primari per proporre nuove importanti funzionalità, raccogliere input dalla comunità su un problema e documentare le decisioni di progettazione di Python.

L'autore del PEP è responsabile della costruzione del consenso all'interno della comunità e della documentazione delle opinioni opposte (dissenzienti).

Poiché i PEP vengono memorizzati come file di testo in un repository con versione, la cronologia delle revisioni funge da record storico della proposta di funzionalità. È possibile accedere a questo record storico utilizzando i comandi git standard per ottenere le versioni precedenti e può anche essere sfogliato su GitHub.

Le PEP vengono suddivise in tre categorie:
1. **PEP Standards Track (PEP 484):**
    - ==Definiscono nuove funzionalità o implementazioni per Python.==
    - ==Possono specificare anche standard di interoperabilità che verranno supportati esternamente alla libreria standard, almeno fino a quando un futuro PEP non introdurrà il supporto direttamente nella libreria standard.== 
- **PEP Informativi(PEP 8):**
    - ==Forniscono linee guida generali, risolvono problemi di progettazione o offrono informazioni utili alla comunità Python.==
    - ==Non propongono nuove funzionalità e non rappresentano necessariamente il consenso della comunità. Gli utenti possono scegliere liberamente se seguirli o ignorarli.== 
    - Esempio: linee guida per lo stile del codice.
- **PEP di Processo (PEP 13):**
    - ==Descrivono processi legati a Python o propongono modifiche a tali processi.==
    - ==Non riguardano il codice sorgente di Python, ma possono suggerire modifiche a procedure, linee guida o strumenti usati nello sviluppo.==
    - ==A differenza dei PEP informativi, i PEP di processo richiedono il consenso della comunità e non possono essere ignorati.==
    - ==Esempi: modifiche al processo decisionale o introduzione di nuove regole per la gestione del linguaggio.==
    - ==Nota: qualsiasi "meta-PEP" rientra in questa categoria.==



> [!faq] Gli esempi delle PEP
> **PEP 484: Type Hints**
>- Introduce il supporto per l'annotazione dei tipi in Python, permettendo di specificare il tipo di variabili, parametri e valori di ritorno nelle funzioni.
>- Ha migliorato il supporto per gli strumenti di verifica statica dei tipi come MyPy.
>
>**PEP 8: Style Guide for Python Code**
>- Fornisce linee guida per scrivere codice Python leggibile e coerente.
>- Copre aspetti come spaziature, lunghezza delle righe, nomi delle variabili, e uso degli import.
>- Non è obbligatoria, ma è ampiamente seguita come standard de facto.
>
>**PEP 13: Python Language Governance Proposal**
>- Descrive il processo per governare lo sviluppo del linguaggio Python dopo che Guido van Rossum ha lasciato il ruolo di Benevolent Dictator For Life (BDFL).
>- Stabilisce un modello basato su un comitato direttivo elettivo (Steering Council).



# Equality checking 
### **Perché seguire le pratiche consigliate?**

- **Leggibilità**: Le pratiche nella sezione "Yes" sono idiomatiche e leggibili da altri sviluppatori Python.
- **Chiarezza semantica**: L'uso di `is` per `None` e di semplici controlli per valori "truthy" o "falsy" chiarisce le intenzioni del codice.
- **Robustezza**: Evita ambiguità e comportamenti indesiderati quando si lavora con oggetti personalizzati che sovrascrivono gli operatori di uguaglianza (\=\=). 


# Differenza tra Automazione e Scripting in Python

1. **Automazione**
    
    - ==L'automazione si riferisce all'uso di script per eseguire compiti ripetitivi o complessi in modo automatico, senza richiedere l'intervento dell'utente.==
    - ==È spesso utilizzata per ridurre gli errori umani, risparmiare tempo e migliorare l'efficienza dei processi.==
    - Esempi:
        - Inviare email in blocco.
        - Rinomina automatica di file.
        - Automazione di processi aziendali o test software.
2. **Scripting**
    
    - ==Lo scripting si riferisce alla scrittura di piccoli programmi, chiamati "script", per eseguire compiti specifici.==
    - ==Gli script sono generalmente progettati per essere semplici e risolvere un problema immediato.==
    - ==Sebbene spesso usati per l'automazione, gli script possono essere anche utili in altre situazioni che non necessariamente richiedono automazione.== 
    - Esempi:
        - Creare uno script per analizzare file CSV.
        - Uno script che estrae dati da una pagina web.
        - Generare report o output specifici.

---

### Differenza fondamentale

- ==**Automazione** è il **risultato** o l'obiettivo: rende i processi ripetitivi automatici e autonomi.==
- ==**Scripting** è il **mezzo**: il processo di scrivere codice (script) per raggiungere l'obiettivo, che può includere l'automazione o altro.==

In breve, ==**l'automazione spesso utilizza gli script, ma non tutti gli script sono pensati per l'automazione**.== 


### Vantaggi e Svantaggi nell'Automazione e Scripting con Python

|**Vantaggi**|**Svantaggi**|
|---|---|
|**Semplicità e leggibilità del codice**|Prestazioni inferiori rispetto ad altri linguaggi|
|**Supporto per attività di automazione comuni**|Problemi con l’uso intensivo della CPU e della memoria|
|**Elevata produttività e rapidità nello sviluppo**|Gestione dei thread|
|**Automazione di operazioni su sistemi operativi differenti**|Distribuzione e creazione di eseguibili stand-alone|
|**Facilità di integrazione con altre tecnologie e API**|Gestione delle dipendenze|
|**Gestione dei task schedulati e periodici**|Compilazione e ottimizzazione limitate|
|**Documentazione e supporto della community**||

### Dettagli

- **Vantaggi**:
    
    - **Semplicità**: 
      Python ha una sintassi intuitiva che riduce il tempo necessario per impararlo e usarlo.
    - **Automazione multipiattaforma**: 
      Grazie ai moduli standard come `os`, `subprocess`, e `shutil`, Python consente di automatizzare operazioni su Windows, macOS e Linux.
    - **Elevata produttività**: 
      La vasta gamma di librerie e il supporto della community rendono rapido lo sviluppo di script complessi.
    - **Integrazione**: 
      Python si integra facilmente con API, database, sistemi di logging, e altre tecnologie.
    - **Community**: 
      La documentazione ufficiale, insieme a forum e risorse online, fornisce un valido aiuto per risolvere problemi.
- **Svantaggi**:
    
    - **Prestazioni**: 
      Python, essendo un linguaggio interpretato, è più lento rispetto a linguaggi compilati come C++ o Go.
    - **Uso della memoria**: 
      Non è ottimizzato per applicazioni che richiedono un uso intensivo della memoria o della CPU.
    - **Distribuzione**: 
      Creare eseguibili stand-alone può richiedere strumenti aggiuntivi come `PyInstaller` o `cx_Freeze`, che possono complicare il processo.
    - **Threading**: 
      Il GIL (Global Interpreter Lock) di Python limita le prestazioni in applicazioni multi-threaded pesanti.
    - **Gestione delle dipendenze**: 
      La risoluzione delle dipendenze in progetti più complessi può essere una sfida, anche con strumenti come `pip` o `poetry`.