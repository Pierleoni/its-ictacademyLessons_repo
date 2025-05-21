Abbiamo visto nel completo il [[Analisi dei requisiti mediante UML|diagramma delle classi in UML]] e [[Diagramma use-case|il diagramma degli use-case]], esiste un terzo documento chiamato documento di specifica.
Siccome il i primi due diagrammi hanno dei rispettivi limiti:
1. Il diagramma delle classi non definisce nel dettaglio cosa calcolano le operazioni di classe, né se e come modificano gli oggetti esistenti (i dati).
2. Il diagramma UML degli use- case non definisce quali sono le operazioni di ogni use-case, né cosa calcolano, né se e come modificano gli oggetti esistenti (i dati).

Di conseguenza lo schema va corredato di un ulteriore documento di specifica **separato da accludere allo schema concettuale,** questo documento si suddivide in 4 tipi diversi:
- **Specifica di dato:**
	==Definisce tutti i tipi di dato non standard utilizzati nello schema concettuale.==  
	^specificaDato
	
- **Specifica di classe**:
	==definisce quali sono le operazioni di classe e cosa calcolano e se modificano gli oggetti/link esistenti.== 
	 ^specificaClasse
	
- **Specifica degli use-case:**
	==Definisce l’insieme delle operazioni di uno use-case.== 
	==Per ogni operazione, definisce cosa calcola e se e come modifica gli oggetti/link esistenti (i dati).==  
	 ^specUse-case
	
- **Specifica dei vincoli esterni:**
	==Definisce ulteriori vincoli (non esprimibili nel diagramma della classi, di qui il nome “esterni”) che gli oggetti/link devono soddisfare.==  ^specificaVincoliEx

### [[#^specificaDato|Specifica dei tipi di dato]] 
![[Specifica dei tipi di dato.png]]

### [[#^specificaClasse|Specifica di classe]] 

Come si da la specifica di un operazione:
![[Specifica operazione nella specifica delle classi.png]]

SI deve riportare la signatura delle operazioni e si devono definire le pre-condizioni e le post-condizioni: 
- pre-condizioni:
Le condizioni che devono essere vere per poter invocare quella operazione, in altre ==parole le condizioni che devono sussistere affinché l'invocazione abbia luogo.== 
queste condizioni vanno indicate per 
	- oggetto di invocazione
	- valori degli argomenti
	-  altri oggetti del sistema
Senza le precondizioni possiamo avere comportamenti inaspettati o bugging. 
- post-condizioni: 
  e quello che deve essere vero dopo quella operazioni
	1. se si modificano i dati come si modificano
	2. spiega come è calcolato il risultato

#### Esempio pratico
Nel diagramma nell'[[Specifica operazione nella specifica delle classi.png|immagine sopra]] la classe `Studente` ha l'operazione di classe `media_fino_a(d:Data): reale in 18..30`.
Di questa operazione bisogna specificare questo:
![[Specifica della classe Studente.png]]

Bisogna chiedersi quali possono essere dei  casi in cui non è possibile calcolare il tipo di ritorno? 
Se lo studente non ha svolto nessun esame, allora  non è possibile restirure un reale tra 18 e 30, 
per risolvere questo problema si potrebbe applicare il vincolo `[0..1]`, però non essendoci devo avere una pre-condizione in cui mi dice che lo studente deve aver fatto almeno un esame. 
Devo dire, l'oggetto di invocazione(self in python) detto `"this"` deve essere coinvolto in almeno un link dell'associazione esame che ha abbia un valore per l'attributo data non successivo al valore `d` precedente a quella presa in input dall'operazione.
Se vedo che lo studente ha sostenuto un esame prima della data d posso clacolare il voto dell'esame.
Dico come è fatto il risultato non come calcolarlo perché è dichiarativa concettuale. 
Questa operazione modifica i dati? No perchè non crea nuovi dati nel sistema quindi non modifica il livello estensionale.
Sia E l'insieme dei link di assoc. "esame" che coinvolgono this
 tali da avere un valore per l'attributo "data" non successivo al vlaore d
 Sia S la somma dei valori dell'attributo "voto" di tutti i link nell'insieme E
 Sia N la cardinalità (ovverro il numero di elementi) di E
 result = S/N ("il vlaore di S diviso per il valore di N).
 Non stiamo dicendo come fare la media dei voti ma dice cosa viene restituito
 L'operazione della classe associata a Studente, ovvero l'operazione `voto_medio():Reale in 18..30` 
 ![[Screenshot 2025-05-05 at 16-58-55 Meet - bmb-xnne-ahh.png]]
Dobbiamo specificare cosa fa questa operazione.

Questi sono uguali a questo:
![[Screenshot 2025-05-05 at 17-04-04 Meet - bmb-xnne-ahh.png]]
Questa cosa si chiama offuscamento: ho offuscato i nomi e il mondo di interesse ma riesco a dire cosa fare in questo caso. 

### [[#^specUse-case|Specifica degli use case ]]
È sempre un documento separato da accludere allo schema concettuale.
![[Specifica di use-case.png]]


### Specifica di use-case
### Specifica dei vincoli esterni
Posso specificare dei vincoli esterni.
I direttori devono:
1. afferire al dipartimento che dirigono, e
2. devono farlo da almeno 5 anni
Ora il primo requisito posso modellarlo in UML cosi: 

![[image.png|463x463]]

Tuttavia pero il secondo punto non posso modellarlo in UML per questo si usa in un documento "SPecifica dei vincoli estenri":
• Un identificatore univoco (per riferirsi al vincolo da altre parti dello schema concettuale, da documentazione
prodotta nelle fasi successive, e dal codice)
• Aziende diverse utilizzano standard diversi per gli identificatori.
Noi useremo `[V.classi_a_cui_il_vincolo_si_applica.nome_vincolo]`
• Una asserzione (in matematica/logica o, in questo corso, in italiano/inglese) che definisce quali sono le
condizioni che devono essere soddisfatte dagli oggetti/link affinché siano in una configurazione legale per il
vincolo.

Quindi seguendo questo esempio posso scrivere 
`[v.Dipartimento.direttore_anni_afferenza]`
In qursto caso sto dicendo che
Per ogni oggetto dip:Dipartimento, sia dir:Impiegato il direttore di dip, ovvero tale che (dip, dir):dirige.
(Grazie alla generalizzazione, è anche vero che (dip, dir):afferenza)
Deve essere: (dir, dip).inizio <= adesso - 5 anni.
Il progettista deve fare in modo che il sistema non deve MAI violare questo statement, per fare cio anziche fare un documento solo enorme posso specificare i vincoli esterni li posso mettre nella Specifica delle classi. 