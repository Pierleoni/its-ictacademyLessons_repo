
# Introduzione
Dopo aver analizzato **dove** viene eseguito il cloud ([[Lezione 3 - Modelli di deployment del cloud#Cloud Pubblico|pubblico]], [[Lezione 3 - Modelli di deployment del cloud#Cloud Privato|privato]], [[Lezione 3 - Modelli di deployment del cloud#Cloud Ibrido|ibrido]], [[Lezione 3 - Modelli di deployment del cloud#Multi-Cloud|multi-cloud]]) è necessario introdurre un secondo asse fondamentale: **chi è responsabile di cosa**.

I **modelli di deployment** descrivono: 
- _la posizione dell’infrastruttura_ e _come viene distribuita_,  
mentre i **modelli di servizio** (IaaS, PaaS, SaaS) descrivono: 
- **come vengono suddivise le responsabilità operative** tra:

- il **cloud provider** (AWS, Azure, Google Cloud);
    
- l’**azienda o lo sviluppatore** che utilizza il servizio.
    

Questa suddivisione è spesso rappresentata come una **piramide della responsabilità**:  
- ==scendendo verso la base aumenta il controllo, ma aumentano anche le attività di gestione;==  
- ==salendo verso l’alto diminuisce il carico tecnico, ma anche la libertà di configurazione.==

## Piramide delle responsabilità 
Nel cloud non esiste una soluzione unica valida per tutti:  
- ogni progetto può scegliere **quanto lavoro tecnico svolgere in prima persona** e **quanto delegare al provider**.

Un’analogia efficace è quella della **pizza**:

- **IaaS (Infrastructure as a Service)**  
    - ==Prepari la pizza partendo dagli ingredienti grezzi (farina, lievito, pomodoro, mozzarella).==  
    - ==Hai il massimo controllo sul risultato finale, ma devi occuparti di ogni singolo passaggio.==
    
- **PaaS (Platform as a Service)**  
    - ==Parti da un impasto già pronto e aggiungi solo i condimenti.==  
    - ==La base è gestita da altri, tu ti concentri sulla personalizzazione.==
    
- **SaaS (Software as a Service)**  
    - ==Ordini la pizza già pronta a domicilio.==  
    - ==Non ti occupi di nulla: la usi e basta.==
    

Allo stesso modo:

- **più sei in basso nella piramide (IaaS)** →  
    - ==più **controllo**, **flessibilità** e **responsabilità** hai;==
    
- **più sali verso PaaS e SaaS** →  
    - più il provider gestisce infrastruttura, sistema operativo, aggiornamenti e sicurezza,  permettendoti di concentrarti solo sul tuo obiettivo principale:
    
	    - sviluppare codice,
        
	    - gestire un servizio,
        
	    - oppure semplicemente usare un’applicazione.
        

La piramide della responsabilità aiuta quindi a capire **non solo cosa offre il cloud**, ma soprattutto ==**come cambia il ruolo dello sviluppatore e dell’azienda** a seconda del modello scelto.== 


### IaaS – Infrastructure as a Service (Infrastruttura come Servizio)

Nel modello **IaaS:**
- ==il cloud provider si limita a fornire **l’infrastruttura IT di base**, mentre **tutta la parte software rimane sotto la piena responsabilità dell’utente**.==

In altre parole, il provider mette a disposizione:

- **potenza di calcolo** (computer virtuali);
    
- **spazio di archiviazione**;
    
- **rete e sicurezza di base**.
    

Tutto ciò che si colloca _al di sopra_ dell’infrastruttura — sistema operativo, applicazioni, configurazioni, aggiornamenti e manutenzione — **deve essere installato, configurato e gestito direttamente dall’utente**.

> [!example] **Analogia: l’appartamento vuoto**  
Il modello IaaS è paragonabile all’affitto di **un appartamento completamente vuoto**:
>
>- il provider fornisce la struttura (mura, pavimenti, impianti);
  >  
>- l’utente deve arredarlo, mantenerlo e gestirlo nel tempo.
  >  
>
>L’infrastruttura è pronta, ma tutto il resto è responsabilità tua.

#### Cosa fornisce il cloud provider
Nel modello IaaS (ad esempio su AWS), il provider si occupa esclusivamente della **base infrastrutturale**, fornendo:

- **Server virtuali**
    
    - [[Docker#Le macchine virtuali (VM)|Macchine virtuali]] astratte su cui è possibile installare qualsiasi sistema operativo.
        
- **Storage (spazio disco virtuale)**
    
    - Dischi virtuali collegabili ai server per ospitare sistemi, applicazioni e dati.
        
- **Rete virtuale**
    
    - Infrastruttura di rete software-defined: subnet, indirizzi IP, routing e collegamenti tra risorse.
        
- **Firewall virtuali**
    
    - Regole di sicurezza per controllare e filtrare il traffico in ingresso e in uscita.
        

Questi componenti costituiscono l’**infrastruttura di base:**
- ==fisicamente gestita dal provider ma logicamente controllabile dall’utente.==
#### Cosa devi gestire l'utente
Nel modello IaaS, la responsabilità operativa ricade in gran parte sull’utente, che deve occuparsi di:

- installare e configurare il **sistema operativo** (Linux, Windows);
    
- installare e gestire i **software applicativi** (web server, database, servizi);
    
- configurare correttamente **rete e sicurezza a livello software**;
    
- applicare **aggiornamenti e patch**;
    
- garantire la **sicurezza del sistema operativo e delle applicazioni**;
    
- pianificare ed eseguire **backup e strategie di ripristino**.
    

> [!ticket] **Sintesi chiave**  
> Con IaaS ottieni **il massimo controllo**, ma anche **la massima responsabilità operativa**.
#### Esempi di servizi IaaS su AWS

##### EC2 – Elastic Compute Cloud

EC2 rappresenta il cuore del modello IaaS su AWS.

- **[[Lezione 1 - Introduzione al Cloud Computing#1. Compute – Potenza di Calcolo Virtuale|Compute]]**: 
	- ==potenza di calcolo ([[Il modello di Von Neumann#CPU (Central Processing Unit)|CPU]] e [[Il modello di Von Neumann#RAM|RAM]]);==
    
- **Elastic**: 
	- ==le risorse possono crescere o ridursi;==
    
- **Cloud**: 
	- ==le macchine sono virtuali, non fisiche.==
    

**Esempio operativo**:

> “Crea un server virtuale con 4 vCPU e 16 GB di RAM”.


##### VPC – Virtual Private Cloud

Il VPC permette di creare una **rete privata virtuale**, isolata e sicura.

- **Virtual**: non esiste fisicamente;
    
- **Private**: isolata dagli altri clienti;
    
- **Cloud**: gestita nel cloud provider.
    

**Esempio**:

> “Crea una rete privata dove solo i miei server possono comunicare tra loro”.

##### EBS – Elastic Block Storage

EBS fornisce **dischi virtuali** collegabili alle macchine EC2.

- funziona come un **hard disk virtuale**;
    
- può essere ridimensionato;
    
- è usato per sistemi operativi, database e dati persistenti.
    


> [!done]  **Vantaggi del modello IaaS**
>
>Il modello IaaS è ideale quando serve **massima libertà tecnica**.
>
>- **Controllo totale**  
> 	 - ==Possibilità di installare e configurare qualsiasi software.==
 >   
>- **Flessibilità massima**  
>	- ==Nessun vincolo su database, linguaggi o architetture.==
>    
>- **Conveniente per profili esperti**  
>	- ==Se il team ha competenze sistemistiche, si paga solo l’infrastruttura base.==


> [!FAILURE] **Svantaggi del modello IaaS**
>
>Il prezzo del controllo è la complessità.
>
>- **Richiede competenze tecniche avanzate**  
>	- Sistemi operativi, sicurezza, networking, patching.
>    
>- **Carico operativo elevato**  
>	- Tutta la manutenzione è a carico dell’utente.
>    
>- **Tempi di configurazione più lunghi**  
>	- Preparare un ambiente completo può richiedere giorni o settimane.

