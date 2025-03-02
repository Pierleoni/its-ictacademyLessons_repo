# Il modello di Von Neumann
 È un  modello astrato su cui si basano tutti i dispositivi elettronici moderni. 
 Questo modello si basava principalmente su una 4 dispositivi che stanno dentro all'elaboratore: 
1. [[#CPU (Central Processing Unit)|CPU]] 
2. [[#RAM|RAM]] 
3. Dispositivi I/O
4. Bus di sistema:
   ==connette la CPU, RAM e le periferiche di I/O a gli altri componenti del sistema.== 
   Permette di: 
   - ==trasferire i dati== 
   - ==Trasferire le istruzioni== 
   - ==Trasferire i segnali di controllo tra i componenti, permettendo di interagire tra loro e collaborare.==
A sua volta il bus di sistema è suddiviso i **3 categorie:**
 1. **Bus Dati:** 
    ==è utilizzato per il trasferimento dei dati tra i vari componenti del sistema, come CPU, memoria e dispositivi di I/O.== 
    ==La sua larghezza (es. 8, 16, 32, 64 bit) determina la quantità di dati che possono essere trasferiti contemporaneamente.== 
  1.  **Bus di controllo:** 
     ==trasporta segnali di controllo e sincronizzazione tra i componenti, come i segnali di lettura/scrittura, conferme di trasferimento dati, o segnali di interrupt. Gestisce il coordinamento delle operazioni.==

   1. **Bus di Indirizzi:** 
      ==serve per specificare l'indirizzo di memoria o di I/O a cui la CPU vuole accedere. La sua larghezza determina il numero massimo di locazioni indirizzabili (es. un bus di indirizzo a 32 bit può indirizzare fino a 2^{32} locazioni di memoria).==

### CPU (Central Processing Unit)
==**Central Processing Unit o CPU** è la memoria centrale del dispositivo, in parole povere è vista come il "cervello del dispositivo stesso."== 
Al suo interno sono presenti due moduli, cioè 
1. **[[#Processing Unit (PU)|PU (Processing Unit):]]** 
   ==L'unità di elaborazione è una parte centrale della CPU responsabile dell'esecuzione delle istruzioni e della gestione delle attività di elaborazione dei dati.== 
   ==Include diversi componenti chiave che lavorano insieme per eseguire operazioni aritmetiche e logiche, controllare il flusso di istruzioni e memorizzare i risultati intermedi.== 
2. **[[#Control Unit (CU)|CU (Control Unit)]]:** 
   L'unità di controllo è una parte cruciale della CPU che dirige il funzionamento del processore. 
   ==Interpreta le istruzioni del programma, genera segnali di controllo e coordina le attività degli altri componenti della CPU, assicurando che le istruzioni vengano eseguite nella sequenza e nel tempo corretti.== 
![[Inside The CPU.png]]


### Processing Unit (PU)
Come possiamo vedere dall'immagine sopra, la PU è a sua volta suddivisa in altri 2 unità: 
1. **ALU (Arithmetic Logic Unit):**
	==L'ALU è un componente critico della CPU che esegue operazioni aritmetiche (come addizione, sottrazione, moltiplicazione e divisione) e operazioni logiche (come AND, OR, NOT e XOR).== 
	==È essenziale per eseguire calcoli e prendere decisioni basate su confronti logici.==
	
2. TEMP (**Temporary** **Register**):
	 ==I registri temporanei (TEMP) sono posizioni di archiviazione piccole e veloci all'interno della CPU utilizzate per contenere dati e risultati intermedi durante l'esecuzione delle istruzioni.== 
	 ==Forniscono un accesso rapido ai valori utilizzati di frequente e aiutano a ottimizzare la velocità di elaborazione riducendo la necessità di accedere alla memoria principale più lenta.==  
	  ^319a5c
### Control Unit (CU):
Come per la PU, anche la CU è suddivisa in altre 2 unità: 
1. **PC (Program Counter):**
	==Il Program Counter (PC) è un registro all'interno dell'unità di controllo che contiene l'indirizzo dell'istruzione successiva da eseguire.== 
	Incrementa dopo che ogni istruzione è stata recuperata, garantendo un flusso sequenziale di esecuzione del programma, a meno che un'istruzione di salto o di ramo non alteri il flusso.   ^PC-register
	
	
2. **IR(Instruction Register):**
	==Il registro delle istruzioni (IR) è un componente dell'unità di controllo che contiene temporaneamente l'istruzione corrente in esecuzione.==    
	Memorizza l'istruzione recuperata dalla memoria, consentendo all'unità di controllo di decodificarla ed elaborarla, indirizzando le azioni necessarie ad altre parti della CPU.   ^IR-register

### Ciclo di vita dell'istruzione 
Si suddivide in 3 step che si ripetono di continuo: 
1. Fetch: 
==La CPU recupera l'istruzione successiva dalla memoria, come indicato da==
==il Program Counter (PC).==
L'istruzione viene caricata nel Instruction Register (IR).
2. Decode: 
==La CU interpreta l'istruzione recuperata nell'IR.==
Determina l'operazione da eseguire e identifica gli operandi necessari.
3. Execute: 
==La CPU esegue l'operazione specificata dall'istruzione.== 
Ciò può comportare operazioni aritmetiche o logiche eseguite dal ALU, trasferimento di dati o operazioni di controllo.
![[Instruction Cycle.pdf.png]]



## RAM 
Random Access Memory (RAM): 
==memoria casuale ad accesso rapido, è volatile cioè una volta che viene spento il computer la RAM viene svuotata.== 
Nell'architettura di Von Neumann, la memoria è tipicamente Riferita alla RAM (Random Access Memory), che è un componente critico che ==memorizza temporaneamente sia i dati che le istruzioni del programma mentre il computer è in esecuzione.== 
Quando un dispositivo è operativo, sia i programmi (Es: Word) che i dati associati (il documento di Word che stai scrivendo) sono archiviati in memoria. 
Sulla memoria possiamo compiere 2 esecuzioni:
1. Fetch: 
	Operazione di **lettura**, in cui la CPU recupera un'istruzione o un dato dalla RAM per elaborarlo.

2. Store: 
	Operazione di **scrittura**, in cui la CPU memorizza un dato nella RAM per un uso futuro.

Queste operazioni avvengono attraverso un sistema di indirizzamento chiamato **memory addressing**, che consente alla CPU di individuare e gestire le informazioni nella RAM.
![[Memory Addresses.png]]
==La memoria è organizzata come una sequenza di **celle**, ciascuna composta da un singolo byte (8 bit).==  
Ogni **cella** di memoria è caratterizzata da:

- **Un valore**, che rappresenta il contenuto della cella (espresso come numero binario).
- **Un indirizzo**, che identifica in modo univoco la posizione della cella nella memoria (espresso come numero binario).
### MDR e il MAR Register 
Altri 2 registri importanti sono il MDR (Memory Data Register) e il MAR (Memory Address Register). 
Sono anch'essi componenti fondamentali nell'architettura di un computer e fanno parte dell' Unità di Controllo (CU). 

3. MDR:
   è un registro che contiene i dati che sono stati recuperati dalla memoria o che devono andare in memoria, quindi che vanno dalla CPU alla RAM e viceversa.
   Quando i dati vengono letti dalla memoria, vengono prima caricati nell'MDR prima di essere elaborati dalla CPU. Allo stesso modo, quando i dati vengono scritti in memoria, vengono inseriti nell'MDR prima di essere memorizzati nella posizione di memoria specificata. 
   Il MDR agisce come un buffer, facilitando il trasferimento regolare dei dati tra CPU e memoria
4. MAR:
   contiene gli indirizzi di memoria dove i dati devono essere scritti o recuperati fisicamente, si trova nella CPU ma permettono l'interazione tra la RAM e la CPU.
   Il Memory Address Register (MAR) è un registro all'interno della CPU che contiene l'indirizzo della posizione di memoria a cui accedere successivamente. 
   Durante la fase di recupero ([[#^fetch|fetch]]) del ciclo di istruzioni, il MAR contiene l'indirizzo dell'istruzione da recuperare (fetched).
   Durante le operazioni sui dati, il MAR conserva l'indirizzo dei dati da leggere o scrivere in memoria. 
   Il MAR garantisce l'accesso alla corretta posizione di memoria, consentendo il recupero e l'archiviazione precisi dei dati.
Entrambi questi registri sono gli indirizzi dove vengono eseguiti le operazioni di fetch (MDR) e lo store (MAR). 
### Le operazioni di fetch e store
Il funzionamento del modulo di memoria prevede i seguenti due passaggi:  
**Operazione [[#^fetch|FETCH]] / Per leggere da una posizione (A):**  
• Scrivere l'indirizzo (A) nel MAR.  
• Inviare un segnale di "lettura" alla memoria.  
• Leggere i dati dall'MDR.  
**Operazione [[#^store|STORE ]]/ Per scrivere un valore (X) in una posizione (A)**:  
• Scrivere i dati (X) nell'MDR.  
• Scrivere l'indirizzo (A) nel MAR.  
• Inviare un segnale di "scrittura" alla memoria.
### Device I/O 
Le operazioni di input e output (I/O) sono fondamentali per consentire a un sistema informatico di interagire con l'ambiente esterno e i dispositivi periferici.
- Input:
	- Scopo: Raccogliere dati da fonti esterne e fornirli al computer per l'elaborazione.
	- Dispositivi: i dispositivi di input più comuni includono tastiere, mouse, scanner, microfoni e fotocamere.
	- Processo: i dispositivi di input convertono le azioni dell'utente o i dati esterni in segnali digitali che il computer può elaborare.
- Output:
	- Scopo: Presentare i dati elaborati dal computer all'ambiente esterno.
	- Dispositivi: i dispositivi di output più comuni includono monitor, stampanti, altoparlanti e proiettori.
	- Processo: i dispositivi di output convertono i segnali digitali dal computer in una forma leggibile o percepibile dall'uomo, come testo, immagini, suoni o output fisico.
