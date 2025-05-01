
# Firmware 
Il **firmware** è un tipo di software integrato all'interno di componenti hardware del dispositivo; come ad esempio: processori, schede grafiche, schede audio, schede di rete e dispositivi periferici (come stampanti e monitor). 
La sua **funzione principale** è quella di **iniziallizzare il componente** e facilitare la sua comunicazione con gli altri componenti all'interno del dispositivo. 
In sostanza, il firmware fornisce al componente un insieme di interfacce di comunicazione e protocolli, permettendo ai vari componenti di **"parlare" tra di loro**, utilizzando un linguaggio comune (che comprende sitnassi e semantica).
![[Firmware.png]]

Il firmware è un tipo di software **proprietario:** 
e non può essere facilmente modificato dall'utente, funge da **ponte tra hardware e software**, consentendo così all'hardware di **comunicare e funzionare secondo le istruzioni software**. 
Viene memorizzato in **memorie non volatili** ([[#ROM (memoria non volatile)|ROM]]), in modo che i dati non vengano persi quando si spegne il dispositivo.

Un esempio noto di firmware è il **[[#Bios|BIOS]]**  (Basic Input/Output System), che è un tipo di firmware più vecchio e **fondamentale per avviare il computer**. Il BIOS risiede sulla **scheda madre** e gestisce il processo iniziale di avvio del computer, inclusa l'inizializzazione dell'hardware e il caricamento del sistema operativo.

Anche dispositivi diversi, come **PC desktop, laptop, computer di bordo di auto o aeroplani**, contengono componenti simili, come le **schede madri**, che eseguono funzioni analoghe.
## ROM (memoria non volatile)
I tipi più comuni di una memoria non volatile per archiviare il firmware sono:
- **ROM (memoria non volatile):**
==memoria non volatili la più famosa è la ROM:==
==una volta scritta non può più essere modificata, adesso si utilizzano le evoluzioni== 
- **EPROM:**
==è una memoria che può essere cancellata e modificata utilizzando l'UV==
- **EEPROM:**
==è come la EPROM ma anzichè usare l'UV utilizza l'elettricità.==

Questi tipi di memoria sono integrati nel dispositivo, garantendo che il firmware sia facilmente accessibile per inizializzare e controllare i componenti del dispositivo quando viene acceso. 
In tutte queste ROM la scrittura avviene bit per bit
LE flash memory sono un tipo di EEPROM ma hanno una capienza più grande utilizzate oggi per la memorizzazione di firmware perché possono essere memorizzate a blocchi quindi sono più veloci ed efficiente di fatto sono utilizzate anche nei SSD.


### Motherboard 
![[Motherboard.png]] 
La **scheda madre** è una delle componenti più importanti all'interno di un dispositivo elettronico (non solo del computer). 
È una **scheda a circuito stampato** (PCB) che ospita e consente la comunicazione tra i componenti elettronici fondamentali del dispositivo. Funziona come un **hub centrale**, unendo tutte le parti del computer e permettendo loro di comunicare e lavorare insieme.

Sulla scheda madre si trovano diversi elementi cruciali:
- **Firmware**: 
  Come il BIOS o l'UEFI, che forniscono le istruzioni per l'avvio del sistema e l'inizializzazione dell'hardware.  ^firmware
  
- **Slot per la memoria**: 
  Qui vengono installati i moduli di RAM, che consentono al computer di immagazzinare e accedere rapidamente ai dati.
- **Slot di espansione**: 
  Permettono l'aggiunta di carte aggiuntive, come schede grafiche, audio, di rete e altre periferiche.
- **Socket CPU**: 
  Un connettore che ospita il processore centrale (CPU).
- **Connettori di memorizzazione**: 
  Per dispositivi di archiviazione come dischi rigidi o SSD.
- **Connettori di alimentazione**: 
  Permettono di fornire corrente alla scheda madre e ai suoi componenti tramite l'unità di alimentazione (PSU).
- **Connettori periferici**: 
  Inclusi quelli per dispositivi USB, prese audio, connessioni di rete, e display (HDMI, DisplayPort).

In sintesi, la **scheda madre** è la spina dorsale di un computer, integrando tutti i componenti critici e garantendo che possano comunicare e funzionare insieme in modo efficace.


## [[#^firmware|Bios]] (Basic Input/Output System)
Il **BIOS** è un insieme di routine software che forniscono la struttura di base che permette al sistema operativo di interfacciarsi con l'hardware del dispositivo. Il BIOS è memorizzato in un chip di memoria non volatile, il che significa che mantiene i dati anche senza alimentazione. Oggi, il BIOS è tipicamente memorizzato in memoria **FLASH** o **EEPROM** saldata direttamente sulla scheda madre, e può essere riscritto tramite una procedura di aggiornamento appropriata.

#### Processo di Bootstrap

Quando un dispositivo viene avviato, prima che il sistema operativo venga caricato, il BIOS esegue diverse operazioni fondamentali:

- **Schermo di avvio**: Mostra una schermata che consente all'utente di configurare e gestire alcune impostazioni di base del BIOS.
- **Avvio della routine di boot**: Il BIOS avvia la routine di avvio per caricare il sistema operativo. Il processo di avvio è incrementale, caricando le parti essenziali del sistema operativo dal settore di avvio per portare il sistema a uno stato operativo stabile.
- **Gestione dell'hardware**: Il BIOS esegue vari test, tra cui il **POST** (Power On Self Test), per verificare il corretto funzionamento dei vari componenti, come la scheda madre, il processore, la memoria, e altri.
- **Configurazione delle impostazioni hardware**: Se non vengono rilevati errori gravi durante la fase POST, il BIOS configura le impostazioni hardware, preparando il sistema affinché il sistema operativo possa prenderne il controllo.

#### Localizzazione dell'MBR (Master Boot Record)

Dopo aver eseguito le routine di base, la prima istruzione del BIOS è localizzare il punto di avvio del disco rigido (o di un altro media di archiviazione di massa) dove è memorizzato il sistema operativo. In questo punto si trova il **Master Boot Record** (MBR).

- Il BIOS legge il contenuto dell'MBR e trasferisce il controllo al sistema operativo. Da questo momento in poi, la gestione del dispositivo è completamente affidata al sistema operativo.
- L'MBR contiene informazioni sulla posizione del **BOOT SECTOR** sul disco rigido (o altro media di archiviazione) dove è memorizzato il sistema operativo. Il **BOOT SECTOR** è il punto di ingresso per l'avvio del sistema operativo.

Se la tabella MBR è danneggiata, il disco potrebbe non avviarsi correttamente, impedendo al computer di accendersi.

### UEFI
fa le stesse cose del BIOS ma essendo aggiornato ha maggiori features ed
ha una interfaccia grafica
ha un boot manager integrato, differentemente con il BIOS, che era un software che doveva essere installato.
Supporto dei driver: con il BIOS prima si accendevano i componenti hardware e poi Il BIOS accendeva i driver, mentre con l'UEFI questo processo avviene in parallelo.
Con l'UEFI possiamo gestire la sicurezza: ad esempio possiamo decidere quali SO si avviano prima. 
E facilemente estendibile e aggiungere nuovi aggiornamenti. 
Il UEFI non utilizza il master boot record ma ha il GPT che è una tabella che descrive le partizione presenti sul SSD ed è più siuro perche questa tabella ha per ogni partizioni descrive queste partizioni ed ha un header secondaria di backup e lo rende più sicuro del MAster boot record perché se si danneggia c'è un backup. 


### Drivers 
I Drivers sono programmi software che permettono al SO e altri software di comunicare con i device hardware. 
Ad esempio e grazie al driver grafico che un vidoegioco possa correre e comunicare con l'hardware. 
Il driver quindi funge da intermediario perché va a tradurre le istruzioni ad alto livello (es: python) in istruzioni a basso livello che l'hardware possa comprendere.


### Diferenza tra firmware e driver
- **La posizione:** 
Al firmware non possiamo accedervi ne modificarlo mentre con il driver posso accedervi e modificarli 
- **Le funzionalità:** 
il firmware ha il compito di avviare il componente mentre il driver è un ponte tra hardware e software
- **La frequenza di aggiornamento:** 
I drivers vengono aggiornati molto frequentemente, il firmware è aggiornato molto poco frequentemente e richiedono una procedura particolare.


## Sistema Operativo

Il sistema operativo (SO) è il software più importante di un dispositivo, in quanto gestisce l'intera operatività della macchina. 
==Si colloca tra l'hardware (compreso il firmware) e il software applicativo, astrando la complessità del computer per gli utenti e i programmi.== 

### Funzioni principali del sistema operativo

Il S.O. si occupa di quattro compiti fondamentali:

1. **Gestione dei componenti hardware**:
    coordina CPU, memoria e dispositivi di I/O.
2. **Esecuzione di applicazioni, programmi e servizi:** permette agli utenti di utilizzare il dispositivo.
3. **Interfacciamento con le periferiche:** 
   come tastiera, mouse, stampanti e dispositivi di archiviazione.
4. **Facilitazione dell'interazione con l'utente:**
    offre un'interfaccia grafica o a riga di comando.

### Ruolo del sistema operativo

Il sistema operativo definisce due aspetti chiave di un dispositivo:

- **Modalità operativa**, determinando lo scopo e il funzionamento del dispositivo.
- **Interazione con l'utente**, specificando come l'utente può gestire e controllare la macchina.

Il SO è presente in tutti i dispositivi elettronici, inclusi computer, smartphone e sistemi embedded. In alcuni casi, il sistema operativo non prevede un'interfaccia diretta con l'utente, come accade nei dispositivi industriali o nei sistemi embedded.

### Classificazione dei sistemi operativi

I sistemi operativi possono essere classificati in base alla gestione dell'elaborazione dei dati:

- **Batch Operating System**: Non c'è interazione diretta con l'utente. L'utente fornisce l'input, il sistema elabora i dati e restituisce l'output senza interventi intermedi.
- **Interactive Time-Sharing Operating System**: Esegue più applicazioni contemporaneamente in runtime, condividendo le risorse tra i processi attivi.
- **Real-Time Operating System (RTOS)**: Utilizzati in ambito industriale e nella robotica, devono operare con tempistiche rigide senza ritardi. Hanno un timing predefinito e non possono subire variazioni nei tempi di esecuzione.
- **Embedded Operating System**: Integrati direttamente nell'hardware, spesso senza interfaccia grafica. Sono utilizzati in dispositivi come aerei, automobili e sistemi di controllo industriale.
- **Hypervisor Operating System**: Permettono la gestione di macchine virtuali, distribuendo le risorse hardware tra i vari sistemi operativi installati.

### Esempi di sistemi operativi

I principali sistemi operativi in uso includono:

- **Microsoft Windows**
- **GNU/Linux**
- **macOS**
- **Android**
- **iOS**
- **Altri sistemi specifici per ambienti embedded e industriali**
### Caratteristiche funzionali
Mono-Task Operating Systems: 
eseguono un solo programma alla volta 

Multi-Task Operating Systems: 
permette di eseguire più programmi alla volta.  ^multi-task-OS

 
Multi-Threading Operating Systems: lo stesso programma che viene suddiviso in altri piccoli progrmami 
Mono-User: un solo utente può interagire con il sistema 

Multi-User: più utenti possono interagire con il sistema.(Windows, [[Linux]], etc. Sono multi-user ma sono usate come Mono-User).   ^multi-user-OS


### Struttura del SO 
Un sistema operativo può essere strutturato come segue: 
1. Management of Programs and User Interface
2. Management of Protection and Security
3. Management of Secondary Memory
4. Management of Peripheral Units
5. Management of the File System
6. Management of Main Memory
7. Management of Processes (Scheduler)


### Kernel
è il cuore del SO ed è il ponte tra l'Hardware e le applicazioni. 
3 tipi di kernel: 
Monolitico: 
tutte le funzioanlità essenziali stanno nel kenrel space mentre libreria etc. stanno nello user space, ma se c'è un bug nel kernel space crolla il sistema operativo ma è veloce
Micro-kernel: 
la differenza è che nel Kernel troviamo l'essenziale mentre tutte le altre operazioni sono stati spostati nello user space è sono suddiviso come moduli, ma spostnado tutto nello spazio utente risulta più lento del monolitico 

Hubryd Kernel:
va ad unire i due per prendere i vantaggi;
abbiamo le funzion imodulari che vengono presi dallo user allo kernel ma sono comunque dei moduli e permette di aggiuungere funzioanlità al kernel ed è più efficiente e veloce 

