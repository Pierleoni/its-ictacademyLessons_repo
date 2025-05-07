Nello schema concettuale è fatto da:
diagramma delle classi
use case
documenti di specifica: specifica di dato, la specifica di classe(definisce qualis sono le operazioni di classe e cosa clacola e se modicia i dati), specifica degli use case(dice cosa fa ogni operazione), specidica dei vincoli esterni.

### Specifica dei tipi di dato

### Specifica di classe
Finora abbiamo visto la signatura.
Come la si da la specifica di un operazione:
riportiamo la signatura e definire le pre-condizioni e le post-condizioni: 
- pre-condizioni:
condizioni che devono essere vere per poter invocare quella operazione.
Le condizioni che devono sussistere affinché l'invocazione abbia luogo.
Senza le precondizioni possiamo avere comportamenti inaspettati o bugging. 
- post-condizioni: e quello che deve essere vero dopo quella operazioni
	1. se si modificano i dati come si modificano
	2. spiega come è calcolato il risultato

Per esempio `media_fino_a`:

![[Screenshot 2025-05-05 at 16-47-32 Meet - bmb-xnne-ahh.png]]

Ci chiediamo dei casi in cui non è possibile calcolare il tipo di ritorno? 
Se non ha svolto nessun esame non posso restirure un reale tra 18 e 30, 
potrei mettere il vincolo \[0..1] ma non esendoci devo avere una pre-condizione in cui mi dice che lo studente deve aver fatto almeno un esame. 
Devo dire, l'oggetto di invocazione(self in python) detto this deve essere coinvolto in almerno un link dell'associazione esame che ha abbia un vlaore per l'attributo data non successivo al vlaore `d` precedente a quella presa in input dall'operazione.
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