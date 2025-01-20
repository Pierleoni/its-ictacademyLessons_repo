## Computer Archittectures
L'importante è un  modello astrato su cui si basano tutti i dispositivi elettronici moderni, e devono avere una 
1. CPU
2. Una RAM 
3. e dei dispositivi I/O
4. infine il bus di sistema:
   -bus dati: su questo bus viaggiano i dati 
   bus di controllo: 
   bus indirizzi: viaggiano gli indirizzi di memoria cioè contiene le locazioni dove vengono presi i dati 

### CPU
Central Processing Unit è la memoria centrale del dispositivi, è vista come il cervello del dispositivo 
Al suo interno è suddiviso 
1. PU (Processing Unit):
2. CU (Control Unit):
   è l'unita del controllo della CPU ed è suddivisa in 

L'alu si occuppa dei calcoli logico-aritmetici, mentre il TEMP sono registir temporanei e sono di supporto perche sono dati su cui il PU deve lavorare o risultati dell'elaborazione di quei dati 

CU:
PC (Program Counter):
contiene l'indirizzo di memoria dove trovi della successiva istruzione da seguire 
IR(Instruction Register):
contiene l'istruzione in esecuzione in quel momento

### Ciclo di vita dell'istruzione 
Si suddivide in 3 step che si ripetono di continuo: 
Fetch: 
di recupero dell'istruzione, si va all'indirizzo di memoria che si trova nel PC 
Decode: 
l'istruzione che si trova nell'IR 
Execute: 
L'istruzione viene eseguita e verrà prodotto il risultato die calcoli, dopo l'esecuzione si ripartirà da capo. 


### RAM 
Random access memory, memoria casuale ad acesso rapido e volatile cioè una volta che viene spento il device la RAM viene svuotata. 
Sulla memoria possiamo compiere 2 esecuzioni:
1. Fetch:
2. Store: operazione della scrittura in memoria 

La memoria è composta da una serie di celle contigue, e ognuna di queste celle ha un valore e un indirizzo e vengono rappresentati in sequenze di bit(codice binario).
2 registri importanti:
1. MDR:
   è un registro che contiene i dati che sono stati recuparti dalla memoria o che devono andare in memoria, quindi che vanno dalla CPU alla RAM e viceversa
2. MAR:
   contiene gli inidrizzi di memoria dove i dati devono essere scritti o recuperati 
fisicamente si trovano nella CPU ma permettono l'interazione tra la RAM e la CPU, sono gli indirizzi dove vengono eseguiti le operazioni di fetch (MDR) e lo store (MAR). 

### Device I/O 
cioè le periferiche che ci permettono di interagire con il dispositivo: danno un input al dispositvio e ci fonriscono un feedback o output dal dispositivo.
