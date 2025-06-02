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
Quando si definisce una **classe** in UML, non basta elencare attributi e operazioni: per ogni **operazione significativa**, bisogna anche fornire una **specifica formale**
Come si da la specifica di un operazione:
![[Specifica operazione nella specifica delle classi.png]]

SI deve riportare la signatura delle operazioni e si devono definire le pre-condizioni e le post-condizioni: 
1. **pre-condizioni:**
	Le condizioni che devono essere vere per poter invocare quella operazione, in altre ==parole le condizioni che devono sussistere affinché l'invocazione abbia luogo.== 
	Quindi sono condizioni che devono essere vere prima dell'invocazione dell'operazione.
	
	Quindi le pre-condizioni indicano:

	- ==Le condizioni sull’**oggetto di invocazione** (es. lo Studente esiste).==
    
	- ==I **valori degli argomenti** (es. `d` deve essere una Data valida).==
    
	- ==L'eventuale **stato di altri oggetti del sistema** (es. esami registrati prima della data `d`).==
Tutte queste condizioni devono essere soddisfatte affinché l'operazione possa essere invocata con successo. 

> [!caution] Se non si rispettano le pre-condizioni, il comportamento dell’operazione è **non definito** (potrebbero verificarsi bug o comportamenti imprevisti).


2. **post-condizioni:** 
  ==Sono le condizioni che devono essere vere dopo l'invocazione.==
  Va tenuto conto di:
	-  se si modificano i dati come si modificano
	-  spiega come è calcolato il risultato.

Quindi queste condizioni specificano:
1) ==**Cosa restituisce** l’operazione (es. il valore medio dei voti)==.
    
2) ==**Come vengono modificati** i dati interni della classe (se ci sono effetti collaterali).==
    
3) **Eventuali effetti collaterali sul sistema**:
    
    - ==creazione/eliminazione di oggetti,==
        
    - ==aggiornamento di link (relazioni),==
        
    - ==modifiche allo stato dell’oggetto o di altri oggetti collegati.==


> [!abstract] **Riassumendo**
> 1. Le pre-condizioni: 
> 	==Sono le **condizioni che devono essere vere (True)** **prima** di invocare un'operazione.==
> Servono, quindi, a garantire che l'operazione venga chiamata in un contesto valido.
> Indicano:
> 	- Lo stato dell'oggetto chiamante (in questo caso uno studente deve avere degli esami )
> 	-  La validità dei parametri (in questo caso una pre-condizione garantisce che il valore del parametro `d` sia una data passata valida).
> 	- I vincoli su altri oggetti del sistema (in questo caso indica che esiste almeno un esame prima di una certa data).  ^pre-condizioni
>> [!danger] Se le pre-condizioni non sono soddisfatte, il comportamento dell'operazione non è garantito, e questo può portare a errori, bug o risultati inaspettati
>
>2. Post-condizioni:
> 	==Sono le **condizioni che devono essere vere dopo l’invocazione** dell’operazione.==
> Specificano:
>	- ==Cosa restituisce l'operazione==;
> 		- Il tipo di ritorno (es: `int>0`, `reale in 18..30`, etc.).
> 		- Il valore calcolato in base ai dati dello stato interno o dei parametri. 
> 		  
> 	- **Cosa cambia nello stato interno della classe:**
> 		- Se vengono modificati gli attributi.
> 		   
> 		- Se l'oggetto modifica il suo livello estensionale:
> 			- Vengono creati nuovi oggetti. 
>			- Vengono eliminati oggetti o relazioni.
>			- Vengono mutate collezioni (es. una lista di esami, email, ecc.).
>  ^post-condizioni



#### Esempio pratico
Nel diagramma nell'[[Specifica operazione nella specifica delle classi.png|immagine sopra]] la classe `Studente` ha l'operazione di classe `media_fino_a(d:Data): reale in 18..30`.
Di questa operazione bisogna specificare questo:
![[Specifica della classe Studente.png]] 

1. Per impostare la precondizione di questa operazione, bisogna chiedersi: 
	**Quali possono essere dei  casi in cui non è possibile calcolare il tipo di ritorno?** 
		Se lo studente non ha svolto nessun esame entro la data `d`, allora  non è possibile restituire un reale tra `18..30`. 
		Per risolvere questo problema si potrebbe applicare il vincolo `[0..1]`, però non essendoci si deve avere una pre-condizione in cui si dice che lo studente deve aver fatto almeno un esame.

Quindi bisogna indicare che: 
- l'oggetto di invocazione(`self` in python) detto `"this"` deve essere coinvolto in almeno un link dell'associazione `esame`, che ha abbia un valore per l'attributo data non successivo al valore `d` precedente a quella presa in input dall'operazione.
  ==In altre parole: `"this"` deve essere coinvolto in **almeno un link** dell’associazione `esame` tale che il valore dell’attributo `data` sia **`≤ d`**.== 
Quindi se lo studente ha sostenuto un esame prima della data (`d`) si può calcolare il voto dell'esame.
Come accennato poco fa in questa nelle pre-condizioni si specifica  come è fatto il risultato non come calcolarlo poiché è dichiarativa concettuale. 

2. Per impostare la post-condizione di questa operazione, bisogna chiedersi: 
	 Questa operazione modifica i dati? 
		   In questo caso no, perché non crea nuovi dati nel sistema, quindi non modifica il livello estensionale.
	Cosa restituisce esattamente ? 
		Un valore medio calcolato concettualmente.
Quindi il livello estensionale rimane invariato (nessuna modifica a oggetti o relazioni),
inoltre va definito il valore del risultato (`result`) dell'operazione:
 - Sia `E` l'insieme dei link di associazione `"esame"` che coinvolgono "`this`" tali da avere un valore per l'attributo `"data"` non successivo al valore `d` (`data` ≤ `d` ) 
 - Sia `S` la somma dei valori dell'attributo `"voto"` di tutti i link nell'insieme `E`
 - Sia `N` la cardinalità (ovvero il numero di elementi) di `E`
 - `result = S/N` ("il valore di S diviso per il valore di N).
 
 L’operazione è **dichiarativa e concettuale**: non  dice _come_ calcolare, ma _che cosa_ rappresenta il risultato.
 
 Ora pure per la classe `Corso`, si deve specificare l'operazione `voto_medio():Reale in 18..30`:
 ![[Screenshot 2025-05-05 at 16-58-55 Meet - bmb-xnne-ahh.png]]
Di base si riscrivono le stesse cose ma con una differenza: 
nell'operazione della classe `Studente` si deve calcolare la media dei voti di uno studente fino a una specifica data (ovvero quella relativa all'esame del corso), mentre nell'operazione `voto_medio():Reale in 18..30` si deve calcolare il voto medio degli esame relativo a quel corso. 


Un altro modo per redigere il diagramma delle classi e i documenti di specifica è l'uso dell'offuscamento dei nomi e del mondo di interesse: 
![[Screenshot 2025-05-05 at 17-04-04 Meet - bmb-xnne-ahh.png]]
Si offuscano i nomi e il mondo di interesse tuttavia bisogna notare come le il comportamento di questo diagramma UML delle classi rimanga invariato. 
L'offuscamento si usa tendenzialmente per evitare la pedanteria nei nomi delle classi, attributi, associazioni e operazioni; ma anche per mantenere il segreto aziendale.


### [[#^specUse-case|Specifica degli use case ]]
È sempre un documento separato da accludere allo schema concettuale.
![[Specifica di use-case.png]]

In questo caso, sempre partendo da il diagramma UML delle classi visto prima, si ha un diagramma use-case, nel quale è presente l'[[Diagramma use-case#Cos è un attore|attore]] "Docente" e lo use-case "Verbalizzazione"(qui si sta dicendo che l'attore Docente può accedere allo use-case "Verbalizzazione"). 
Si va a redigere quindi il documento di specifica dello use-case definendo anche qui le pre/post-condizioni. 
Come si può vedere l'operazione `verbalizza` prende come parametri `s:Studente`(oggetto della classe `Studente`), `c:Corso` (oggetto della classe `Corso`), `d:Data` (oggetto di una rappresentazione concettuale di una data), `v:18..30`(oggetto di una rappresentazione concettuale di un numero compreso in un range tra 18 e 30)
1. **[[#^post-condizioni|pre-condizioni]]:** 
	Affinché questa operazione possa essere invocata con successo gli oggetti `s`, `c` non devono essere (già) un link di associazioni esame *(cioè `s` non ancora sostenuto/verbalizzato `c`)*.
	Quindi, in sostanza non deve esistere un link dell'associazione `esame` tra gli oggetti `s`, `c`; questo perché si vuole impedire la duplicazione della verbalizzazione di uno stesso esame per lo stesso studente-corso.
2. **[[#^post-condizioni|post-condizione]]:** 
	Dopo l'invocazione di questa operazione viene creato un link (con gli oggetti `s`, `c`) di associazione `"esame"` con valori `"d"` e `"v"` che corrispondo rispettivamente agli attributi `"data"` e `"voto"`.
	In altre parole, dopo l'invocazione, nel modello concettuale esiste:
	- un nuovo link della associazione `esame` tra gli oggetti `s`, `c`.
	- **valori** `data = d` e `voto = v` specificati.

La differenza con il documento di specifica delle classi è che le operazioni di use-case non hanno alcun oggetto di invocazione ("`this`").

#### Un altro esempio di specifica degli use-case:
![[Specifica use-case_2.png]]
In questo esempio abbiamo un attore `Studente` che accede ad uno use-case `Iscrizione` (rappresenta un'operazione di creazioni di oggetti nel modello concettuale). 
Nella specifica di questo use-case l'operazione `iscrizione(mat:intero>0, nome:Stringa):Studente`: prende in input due parametri 
1. il numero di matricola dello studente
2. il nome dello studente 
E restituisce un oggetto `Studente`. 
La pre-condizione: 
	==Affinché questa operazione possa essere invocata con successo, non può esistere nessun oggetto della classe `Studente` con valore `"mat"` per l'attributo `matricola`.== 
	In altre parole: 
	==non esiste alcun oggetto della classe `Studente` tale che `matricola = mat`.==
	Serve per evitare duplicazioni(unicità della chiave primaria `matricola`, che è anche `{id}` nel diagramma UML delle classi a destra).

La post-condizione: 
	Una volta invocata questa operazione, viene creato e restituito un nuovo oggetto `result:Studente` con valori `"mat"` e `"nome"` per, rispettivamente, gli attributi `matricola` e `nome`.  
	In altre parole: ==viene creato e restituito un nuovo oggetto `Studente`, i cui attributi `matricola` e `nome` assumono i valori `mat` e `nome`==.
	


### [[#^specificaVincoliEx|Specifica dei vincoli esterni]]
Come detto per la definizione di specifica dei vincoli esterni: 
==Alcuni requisiti potrebbero implicare vincoli sui dati/oggetti/link che sono non sono esprimibili nel diagramma delle classi.== 
Quindi in sostanza questi vincoli esterni li possiamo definire come:
alcuni dati, oggetti o link che devono rispettare regole che non si possono esprimere con molteplicità, attributi o generalizzazioni.
Ipotizziamo che in un diagramma UML delle classi si debba modellizzare che I direttori devono:
1. afferire al dipartimento che dirigono, e
2. devono farlo da almeno 5 anni
Ora il primo requisito si può modellizzarlo in UML cosi: 
![[Esempio specifica dei vincoli esterni.png]]

Cioè una generalizzazione tra associazioni dirige `is-a` afferenza (quindi: se dirigi un dipartimento, allora ci afferisci anche).
Tuttavia pero il secondo requisiti non lo si riesce modellizzare in UML, **perché include una condizione temporale e quindi serve un vincolo esterno**.  
Per questo ci si serve di un documento "Specifica dei vincoli esterni":
==Si usa un identificatore univoco (per riferirsi al vincolo da altre parti dello schema concettuale, da documentazione prodotta nelle fasi successive, e dal codice)==.

> [!info] Aziende diverse utilizzano standard diversi per gli identificatori.
> Noi useremo `[V.classi_a_cui_il_vincolo_si_applica.nome_vincolo]`

Dopodiché ci si serve di una asserzione (in linguaggio matematico/logico o, **in questo corso, in italiano/inglese**): 
==che definisce quali sono le condizioni che devono essere soddisfatte dagli oggetti/link affinché siano in una configurazione legale per il vincolo.== 
In parole povere: 
==definisce **cosa deve essere vero** affinché la configurazione sia **valida**.== 

Tornado al secondo requisito da modellizzare, si può scrivere: 
`[V.Dipartimento.direttore_anni_afferenza]`.
In questo caso si sta dicendo che: 
==Per ogni oggetto `dip:Dipartimento` (cioè per ogni oggetto `dip` che è un oggetto della classe `Dipartimento`), sia `dir:Impiegato`(cioè per ogni oggetto `dir` che è un oggetto della classe `Impiegato`) il direttore di `dip`, ovvero tale che (`dip`, `dir`)`:dirige`.== 
(Grazie alla generalizzazione, è anche vero che `(dip, dir):afferenza`)
Quindi deve essere: `(dir, dip).inizio <= adesso - 5 anni`.
**Nel caso (frequente) in cui un vincolo esterno si applica naturalmente agli oggetti di una sola classe, è raccomandato definirlo nella specifica di quella classe piuttosto che nella specifica dei vincoli esterni**.
Con questo approccio, il documento “Specifica dei vincoli esterni” conterrà solo la definizione dei vincoli che non sono attribuibili a singole classi.


> [!abstract] **Memotecnica**
> - **Vincolo modellabile in UML?** → Diagramma delle classi.
  >  
>- **Vincolo NON modellabile?** → Vincolo esterno.
>    
>- **Vincolo riferibile a UNA classe?** → Mettilo nella specifica di quella classe.


Per fare un esempio di come vanno scritte le specifiche dei vincoli esterni all'interno della specifica delle classi:

```
Specifica classe Dipartimento
operazione_1(…): …
pre: …
post: …
…
Vincoli esterni:
[V.Dipartimento.direttore_anni_afferenza]
Per ogni oggetto dip:Dipartimento, sia dir:Impiegato il direttore di dip, ovvero tale che (dip, dir):dirige.
(Grazie alla generalizzazione, è anche vero che (dip, dir):afferenza)
Deve essere: (dir, dip).inizio <= adesso - 5 anni
```