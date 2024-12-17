# Complemento a 2 
Il complemento a 2 è un metodo usato nella Computer Science e nell'elettronica per rappresentare numeri interi con segno (sia positivi che negativi) nel [[Le architetture di un Computer#il Codice Binario|sistema binario]].  
È un metodo molto utile per due motivi principali: 
1. ==Permette di utilizzare operazioni binarie (somma e sottrazioni) sia per numeri positivi che negativi==. 
2. ==Elimina la necessità di avere circuiti separati per operazioni aritmetiche con numeri con segno==.
**Concetti di base:**
1. Il **Most Significant Bit (MSB)** viene usato come bit di segno: 
	- ==0:==  
		==indica un numero positivo==. 
	- ==1:==   
		==indica un numero negativo==.  

2. **Intervallo di rappresentazione:**
   - In un sistema binario a N bit, il complemento a 2 consente di rappresentare i numeri da: 
	   - `-2^(N-1)` a `2^(N-1)-1` 

Ad esempio, in **4 bit**, si possono rappresentare i numeri da -8 a +7
```
4-bit: da 1000 (-8) a 0111 (+7)
```

3. **Rappresentazione di zero:**
   - ==Lo zero ha una sola rappresentazione (`0000`), **sia in positivo che in negativo**, per evitare ambiguità e evita il problema del doppio zero presente in altri sistemi (Es: il complemento a 1).==

### Come calcolare il complemento a 2 

I numeri negativi sono rappresentati calcolando il complemento a due dei loro valori positivi corrispondenti, mentre i numeri positivi sono rappresentanti dal calcolo del complemento a due dei loro valori negativi corrispondenti, in parole povere:
==Il complemento a 2 di un numero è il **modo per rappresentare un numero negativo** a partire dalla sua controparte positiva==  
Es:  
+3 in 4 bit binari equivale a 0 011→ numero positivo.
-3 in 4 bit binari equivale a 1 101 → numero negativo.

Per trovare il complemento a 2 dei numeri binari:
1. Invertire tutti i bit del numero binario ( complemento a uno).
2. Aggiungere 1 al risultato del numero precedente 


> [!tip] Positivo → Negativo
> Assumendo di stare usando 4 bit
> Rappresentazione di +3:   
> - il numero binario è : 0011 (4 bit) 
> 
> Rappresentazione di -3:  
> - Invertire i bit di +3 (0011): il risultato diventa 1100 (complemento a uno)
> - Aggiungere 1 (cioè: 0001) a 1100  
> 1100 + 
> 0001  = 1101 → -3 4 (bit  in binario)

Per fare l'addizione in binario la regola è sempre la stessa:  
1. Invertire tutti i bit del numero binario (complemento a uno)  
2. Aggiungere 1 al risultato dello step precedente

> [!tip] Negativo → Positivo
>Assumendo di stare usando 4 bit
>Rappresentazione di -3:
> - La rappresentazione in binario è: 1101 (4 bit)
> 
> Rappresentazione di +3:
> - Invertire i bit di -3 (1101): il risultato è 0010 (complemento a uno)
> - Aggiungere 1 (cioè: 0001) a 0010
>   0010 + 0001 = 0011 → + 3  (4 bit in binario)

### **Perché è utile il complemento a 2?**
1. **Semplifica le operazioni aritmetiche:**  
- La sottrazione viene trasformata in somma.  
- Ad esempio, per calcolare `5 - 3` in binario, possiamo sommare `5` e `-3`:
  
  +5 → 0101
  -3 → 1101

0101+ 1101 = 0010 → +2 (risultato corretto)
  

2. **Un'unica logica per somma e sottrazione:**  
Non servono circuiti distinti per le due operazioni.
### **Intervallo di rappresentazione:**
- Per un sistema binario con **N bit**, i numeri rappresentabili sono:
Da -2^(N-1) a 2^(N-1) - 1
 **Esempi:**
- **4 bit**: da `-8` (`1000`) a `+7` (`0111`).
- **8 bit**: da `-128` (`10000000`) a `+127` (`01111111`).

---

### **Conclusione**
Il complemento a 2 è un metodo efficace per rappresentare numeri con segno in binario, semplificando le operazioni aritmetiche. Seguendo le regole di inversione dei bit e somma di 1, possiamo facilmente calcolare la rappresentazione binaria di numeri positivi e negativi.

---

# Computer networks

### Introduzione
1. Evoluzione dei dispositivi di rete:
• **Da mainframe a personal computer:** 
dall'affidamento precoce su sistemi centralizzati di grandi dimensioni all'onnipresente
dispositivi informatici personali.
• **L'ascesa della tecnologia mobile:** 
transizione dai desktop statici agli smartphone e ai tablet mobili
Connettività sempre e ovunque
2. Proliferazione dei servizi Internet:
• **Espansione dei servizi di streaming:** 
impatto di Internet ad alta velocità sull'intrattenimento; dal tradizionale
trasmissione su piattaforme di streaming on-demand come Netflix e YouTube.
• **Social Media Networks:** 
evoluzione da strumenti di comunicazione di base a piattaforme complesse che guidano i social
Interazioni, business e diffusione di notizie.
3. Impact sulla società:
• **Inclusione digitale e villaggio globale:**
il ruolo del networking avanzato nel colmare le esigenze geografiche e
divari socioeconomici.
• **Sfide:** 
affrontare le minacce alla sicurezza informatica e i problemi di privacy in un mondo sempre più interconnesso.

### Computer network (o rete di computer)
Una rete di computer è un insieme di sistemi informatici interconnessi e altri dispositivi informatici che
Comunicare tra loro per condividere risorse e informazioni. Consente a più utenti di scambiare dati, accedere
applicazioni condivise e utilizzare hardware comune come stampanti e server.
Le reti possono variare da semplici connessioni tra due computer a vaste reti globali come Internet.
In genere utilizzano varie tecnologie, protocolli e infrastrutture fisiche per facilitare la fluidità
comunicazione e trasferimento di dati tra dispositivi collegati.

### Uso della rete di computer
#### Applicazioni aziendali:
• **Condivisione delle risorse:** 
le reti di computer consentono l'uso condiviso di dispositivi essenziali su diversi computer all'interno di una rete. Ciò include stampanti, scanner e fax, consentendo a più utenti di utilizzare lo stesso risorse fisiche in modo efficiente, riducendo i costi e migliorando la produttività.
• **Condivisione delle informazioni:** 
le reti facilitano lo scambio continuo di informazioni tra gli individui,
organizzazioni e tecnologie. Questa capacità è fondamentale per la collaborazione e il processo decisionale, in quanto garantisce che i dati rilevanti siano accessibili e utilizzati da più posizioni e piattaforme.
• **Mezzo di comunicazione:** 
le reti fungono da canali di comunicazione vitali. Supportano vari
strumenti di comunicazione come e-mail, videoconferenze e messaggistica istantanea, che sono essenziali per i moderni operazioni aziendali. Questi strumenti aiutano a mantenere una comunicazione efficace tra dipendenti, clienti e
indipendentemente dalla loro ubicazione fisica.
• **E-commerce:** 
le reti sono fondamentali per le attività di e-commerce. Consentono transazioni come online pagamenti, trasferimenti elettronici di fondi e gestione di mercati digitali. Questa infrastruttura digitale è fondamentale condurre affari nel mercato globale, fornendo una piattaforma per l'acquisto e la vendita di prodotti e servizi
in linea.

#### Applicazioni domestiche:
• **Accesso remoto alle informazioni:** 
Le reti informatiche consentono l'accesso remoto a contatti personali e professionali
informazioni praticamente da qualsiasi luogo, compresa la propria casa. Questa flessibilità consente alle persone di lavorare da ovunque, accedendo a file di lavoro, database e applicazioni tramite connessioni sicure come VPN,
produttività ed equilibrio tra lavoro e vita privata.
• **Comunicazione da persona a persona:** 
le reti sono fondamentali per facilitare la comunicazione diretta tra individui che utilizzano vari metodi come telefonate, chat di testo e videochiamate. Questi strumenti aiutano a mantenere relazioni personali e collaborazioni professionali a distanza, riducendo la necessità di spostamenti fisici e consentendo una comunicazione più dinamica e immediata.
• Intrattenimento interattivo: 
le reti informatiche svolgono un ruolo fondamentale nel regno dell'intrattenimento, collegandosi utenti con una vasta gamma di contenuti interattivi. Ciò include i siti di social networking che consentono la condivisione e comunicazione tra gli utenti, piattaforme di gioco online che consentono esperienze di gioco multiplayer, e
Servizi di streaming che forniscono accesso in tempo reale a film, musica e programmi televisivi. Queste piattaforme non solo servono per intrattenere ma anche creare comunità e riunire persone con interessi simili.

#### Applicazioni mobili:
• **M-commerce:** 
questa forma di commercio consente l'acquisto e la vendita di beni e servizi attraverso dispositivi portatili wireless, come smartphone e tablet. L'm-commerce utilizza le reti mobili per fornire transazioni convenienti e veloci da qualsiasi luogo, consentendo ai consumatori di fare acquisti, gestire le finanze e accedere ai servizi in movimento.
Ciò include i pagamenti mobili, le operazioni bancarie e gli acquisti tramite app dedicate e siti Web ottimizzati per i dispositivi mobili, migliorando così la comodità dell'utente e ampliando la portata del mercato per le aziende.
• Sistema di navigazione GPS: i sistemi di navigazione utilizzano la tecnologia di rete per fornire informazioni sulla posizione e sull'ora in tutte le condizioni atmosferiche e ovunque. Questi sistemi offrono istruzioni di navigazione turn-by-turn per aiutare gli utenti a raggiungere le loro destinazioni in modo efficiente. Sono integrati nei dispositivi mobili e nei veicoli per facilitare la pianificazione del percorso, il monitoraggio del traffico e il rilevamento della posizione, migliorando la sicurezza e la comodità del viaggio.
• **Messaggistica istantanea:** 
le reti supportano una varietà di servizi di messaggistica istantanea che consentono agli utenti di inviare e ricevere messaggi in tempo reale. Questi servizi vanno oltre i messaggi di testo per includere le chiamate vocali e la condivisione di file multimediali, come immagini e documenti. La messaggistica istantanea ha rivoluzionato la comunicazione,
offrendo un metodo rapido, economico e versatile per rimanere in contatto personale e professionale in tutto il mondo.

---


### Comunicazioni delle reti di computer

Ci sono 2 tipi di comunicazioni delle reti di computer:
1. **Point-to point:**
   Si intende un link diretto tra due devices 
![[Point to point.png]]
Questo network è strutturato attraverso una serie di link e nodi. 
Un nodo può essere un device, come ad esempio; uno switch o un router.
Switch:
serve a connettere un device
