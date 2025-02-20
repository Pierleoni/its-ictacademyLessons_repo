
# Firmware 
Il firmware è un software che integrato all'interno di componenti hardware del computer, è molto importante perché permette di avviare il computer e di comunicare con gli altri componente del pc. 
Il firmware è un software proprietario di fatto l'utente non può essere modificato ed è il ponte tra l'hardware e il software. 
Il BIOS è un tipo di firmware più vecchio ed avviava il pc, il firmware è memorizzato su memorie non volatili (ROM) perché è necessario che non vada perso quando si spegne il computer.
### ROM
memoria non volatili la più famosa è la ROM:
una volta scritta non può più essere modificata, adesso si utilizzano le evoluzioni 
EPROM:
è una memoria che può essere cancellata e modificata utilizzando l'UV
EEPROM:
è come la EPROM ma anzichè usare l'UV utilizza l'elettricità.
In tutte queste ROM la scrittura avviene bit per bit
LE flash memory sono un tipo di EEPROM ma hanno una capienza più grande utilizzate oggi per la memorizzazione di firmware perché possono essere memorizzate a blocchi quindi sono più veloci ed efficiente di fatto sono utilizzate anche nei SSD 


### Motherboard 
E un chip stampato più importante all'interno del device elettronico (non solo il computer) perché è quel circuito su cui si trovano tutte le componenti elettronici e riescono a comunicare tra loro. 
Sulla scheda madre troviamo 
Il firmware
gli slot di memoria 
slot di espansione
CPU socket
I conntettori di memorizzazione (SSD)
conntettori di corrente: ciò che da l'elttricità alla macchina 
I connettori periferici(USB, Firmware, etc.)


### Bios
Il BIOS è il firmware più vecchio è una insieme di software che permette l'avvio delle componenti hardware del computer e si trova all'intnero del 
#### Processo di bosstrap
Tramite questo processo il BIOS avvia una serie di Test, una tra questi è il POST: avvia ogni vomponente e si assicura che funzioni. 
Una volta fatto ciò vengo avviate tutte le altre componenti, 
Boot routine: Il caricamento del SO.
Si andava a trovare la prima istruzione a quel punto veniva lanciata, il controllo passava al SO e l'SO lanciava l'accensione.
Se il boot record veniva danneggiato il pc non si accendeva 

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
La posizione: 
Al firmware non possiamo accedervi ne modificarlo mentre con il dirver posso accedervi e modificarli 
Le funzionalità: il firmware ha il compito di avviare il componente mentre il driver è un ponte tra hardware e software
La frequenza di aggiornamento: i driver vengono aggiornati molto frequentemente, il firmware è aggiornato molto poco frequentemente e richiedono una procedura particolare.


### Sistema operativo 
Il sitema operativo è il software più importante del dispositivo: gestisce l'interazione con l'utente, gestice gli applicativi, interfacciamento con le periferiche e la gestione con l'interazione con l'utente. 
Il SO definisce come deve lavorare con il dispositivo e definisce come l'utente può agire sulla macchina.
Il SO è presenye in tutti i device elettronici, in alcuni casi non hanno un'interazione con i dispositivi elettronici. 

Il SO puo essere clasifficato in base all'elavborazione dei dati. 
Batch Operating system: non c'è interazione con l'utente anche se quest'ultimo fornisce l'input e la macchina fornisce l'output
Interactive Time-Sharing Operatign System: fanno correre in runtime diversi applicativi e condidono le risorse. 
Real-Time Operating Systems:
SO che devono lavorare in real time, è sono utilizzato nell'industria o nella robotica, qui il tempo è fisso e quindi non posso ritardare; hanno un timing ben predefiniti. 
Embedded operating system: sono integrati nell'hardware e non hanno interfaccia grafica, sono utilizzati nell'aeroplano. 
Hypervisor Operating System: SO che permette di installare diverse macchine virtuali e permette di condividere le risorse alla diverse macchine virtuali 
### Caratteristiche funzionali
Mono-Task Operating Systems: 
esegunono un solo programma alla volta 
Multi-Task Operating Systems: permette di eseguire più programmi alla volta 
Multi-Threading Operating Systems: lo stesso programma che viene suddiviso in altri piccoli progrmami 
Mono-User: un solo utente può interagire con il sistema 
Multi-User: più utenti possono interagire con il sistema (Windows, etc. Sono multi-user ma sono usate come Mono-User).


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

