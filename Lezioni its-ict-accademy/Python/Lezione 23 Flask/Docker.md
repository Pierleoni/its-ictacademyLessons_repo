# Virtual Machine
Le virtual machines (Vms) sono create attraverso un processo chiamata virtualizzazione:
è una tecnologia che peremette di creare ambienti multpli simulati(es:server, storage o network) su una singola macchina fisica. 
In sostanza prendiamo un pezzo del nostro sistema operativo e la utilizziamo per la macchina virtuale.
Le VMs virtualizzano l hardware. Questo semplificazione significa che una VM prende un sinoglo pezzo di hardware, o un server, e crea versioni virtuali di altri server per fa correre il proprio sistema operativo. Fisicamente è un piccolo pezzo di un hardware. 
Logicamente, più macchine virtuali possono essere eseguite su un singolo hardware.
**In pratica, si tratta di uno o più computer in esecuzione all'interno di un altro computer,**  come mostrato di seguito.
![[Screenshot 2025-04-15 at 12-12-19 Docker_v3 - Docker.pdf.png]]

## Container
**Un container è un pacchetto software leggero, autonomo ed eseguibile che include tutto il necessario per eseguire un'applicazione,**  
**compreso il codice, il runtime, gli strumenti di sistema e le librerie.**

I container sono progettati per isolare le applicazioni e le loro dipendenze, 
**garantendo che possano funzionare in modo coerente in ambienti diversi.**

Che l'applicazione venga eseguita dal tuo computer o nel cloud,**  il suo comportamento rimane identico.


### VM vs Container
**Virtualizzazione con VM (Macchine Virtuali):**

- **VM** (Macchine Virtuali)
    
- **Hypervisor** (Software di virtualizzazione)
    
- **Hardware e OS host** (la macchina fisica utilizzata per creare le VM)
    

Ogni VM ha:

- **Un proprio sistema operativo (OS)**
    
- **Librerie**
    
- **Applicazioni**
    

Tutto è eseguito **su un unico hardware fisico**.
![[Screenshot 2025-04-15 at 12-13-09 Docker_v3 - Docker.pdf.png]]
**Container:**

- **Ogni container** utilizza **un unico sistema operativo** per eseguire un'applicazione virtuale e le relative librerie.
    
- **Motore di container** (es: Docker) che virtualizza il sistema operativo.
    
- **Condivisione** dell'hardware e del sistema operativo forniti dal sistema host.
![[Screenshot 2025-04-15 at 12-14-24 Docker_v3 - Docker.pdf.png|342x208]]

Quindi in sostanza le differenze sono 

**Macchine Virtuali (VM)**

- **Portabilità**:  
    Le VM sono generalmente **meno portabili** a causa delle differenze tra i sistemi operativi sottostanti.  
    Lo spostamento di VM tra hypervisor o provider cloud diversi può risultare **più complesso**.
    
- **Efficienza**:  
    Le VM hanno **un maggior consumo di risorse**, poiché ogni VM richiede un'istanza completa di sistema operativo.  
    Ciò comporta:
    
    - Maggiore utilizzo di memoria e storage
        
    - Potenziale impatto negativo su **prestazioni e tempi di avvio**
        


**Container**

- **Portabilità**:  
    I container sono progettati per essere **indipendenti dalla piattaforma**.  
    Possono essere eseguiti su qualsiasi sistema che supporti il runtime dei container (es: Docker), **indipendentemente dal sistema operativo sottostante**.  
    Questo semplifica lo spostamento di applicazioni tra ambienti diversi (es: da locale a cloud).
    
- **Efficienza**:  
    I container **condividono il sistema operativo dell'host**, riducendo il sovraccarico tipico delle VM.  
    Vantaggi:
    
    - Utilizzo più efficiente delle risorse (CPU, memoria)
        
    - Maggiore densità di applicazioni eseguibili sullo stesso host
        



| Caratteristica  | VM                               | Container                           |
| --------------- | -------------------------------- | ----------------------------------- |
| **Portabilità** | Limitata (dipende dall'OS guest) | Alta (grazie al runtime universale) |
| **Overhead**    | Alto (OS completo per ogni VM)   | Basso (condivisione kernel host)    |
| **Densità**     | Bassa (risorse dedicate)         | Alta (più container per host)       |
##### **Perché è importante?**

- Le VM sono ideali per carichi di lavoro **isolati e eterogenei** (es: Windows/Linux sullo stesso hardware).
    
- I container sono ottimi per **microservizi e scalabilità** (es: applicazioni cloud-native).

### Container: benefit addizionali 
1. **Uniformità (Consistency)**

I container includono tutto il necessario per l'esecuzione dell'applicazione:

- Codice
    
- Runtime
    
- Librerie
    
- Dipendenze
    

in un **unico pacchetto autonomo**.  
Questo elimina il classico problema _"sul mio computer funziona"_ e garantisce un comportamento **identico** in tutti gli ambienti, dallo sviluppo alla produzione.



2. ** Isolamento**

I container creano un **ambiente isolato e leggero** per ogni applicazione:

- Ogni container "incapsula" l'applicazione e le sue dipendenze
    
- Previene conflitti tra applicazioni diverse
    
- Assicura un comportamento coerente, indipendentemente dall'ambiente
    

_Esempio:_ Due container con versioni diverse della stessa libreria possono coesistere senza problemi.

---

3.  ** Deployment Rapido**

- **Avvio in pochi secondi** (vs minuti delle VM)
    
- Ideale per applicazioni che richiedono:
    
    - **Scalabilità immediata** (espansione/riduzione in base alla domanda)
        
    - **Rollback veloci** in caso di problemi
        

_Caso d'uso:_ Un e-commerce durante il Black Friday può aggiungere istanze di container in tempo reale per gestire il picco di traffico.


| Vantaggio      | Descrizione               | Beneficio                                |
| -------------- | ------------------------- | ---------------------------------------- |
| **Uniformità** | Pacchetto autosufficiente | Niente più "funziona solo in sviluppo"   |
| **Isolamento** | Ambiente separato per app | No conflitti, maggiore stabilità         |
| **Velocità**   | Avvio in secondi          | Scalabilità agile e risparmio di risorse |


## Docker

Docker è uno strumento progettato per **creare e gestire container** in modo efficiente.  
Si basa su due concetti fondamentali:

1.  **. Dockerfile**

- **Insieme di istruzioni** per costruire un'_immagine Docker_.
    
- Definisce:
    
    - Ambiente di runtime
        
    - Dipendenze
        
    - Configurazioni
        
    - Comandi per l’esecuzione dell’applicazione
        


2. ** Immagine Docker (Docker Image)**

- **Template** per creare container.
    
- Contiene tutto il necessario per eseguire un’applicazione:
    
    - Codice
        
    - Runtime (es: Python, Node.js)
        
    - Strumenti di sistema
        
    - Librerie
        
    - Configurazioni

#### **Perché è utile?**

- **Portabilità:** Un’immagine funziona ovunque (PC, cloud, server).
    
- **Riproducibilità:** Niente più _"sul mio computer funziona"_.
    
- **Isolamento:** Ogni container è autonomo e sicuro.
    

Strumenti correlati:

- **Docker Hub** (repository di immagini pronte all’uso).
    
- **Kubernetes** (orchestrazione di container in produzione).


### Docker comandi basici
`$docker ps`: fa vedere tutti i container aperti 
