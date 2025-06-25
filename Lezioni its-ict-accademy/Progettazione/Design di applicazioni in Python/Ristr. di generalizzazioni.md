Prendiamo ad esempio Go:
In Go un'istazna di partita nasce come oggetto della classe partita e nel tempo può diventare istanza di partita TemPunteggio o di PartitaTemRitiro. 
Ovviamente non può morire come oggetto di Giocatore.
In python quando si crea ad esempio una classe `Persona` e una classe `Studente(Persona)` dopodiche si crea l'istanza
```
mario = Persona()
```

Non si può far diventare questa istanza una istanza di Studente perché senno sarebbe un laltro oggetto.

QUindi il complete in Python non esiste mentre il disjoint si.

Ad esempiose in UML si crea una generalizzazione di Persona tra Studente e Lavoratore, significa che istanza di Persona può essere o un Lavoratore o uno Studente.
In python questa cosa non si può fare quindi bisogna ristrutturare le generalizzazioni:
QUindi si deve ristr. il diagramma concettuale in un diagramma equivalente che non abbia mai generalizzazioni che non siano disgiunte perché in Python due oggetti non possono completarsi a vicenda, quindi deve per forza essere il disjoint.
In più non devono esserci generalizzazioni tra lcassi o assoc le cui istanze (oggetti o link) possono cambiare la loro classe/assoc. più specifica durante la loro vita.
GLi oggetti non hanno bisogno di cambiare la loro classe più specifica.
In questo caso il diagramma :
![[Ristr generalizzazioni.png]]

In questo caso non c'è bisogno di nessuna azione necessaria perchè in Python si traduce così:
```
class Persona:

class Studente(Persona):
```

Ma se c'è il complete:
![[Ristr con complete.png]]
bisogna impl una classe Astratta; ovvero una classe che non ha oggetti propri cioè non ci sono oggetti che sono istanza prorpie di quella classe.
QUindi quando si ritr si ottiene una classe atratta e il complete va via. 

E se non è dijsoint?
Io devo avere persona che sono Studente o Dicenti o nessuno delle due o che uno Stud può diventare Docente.
Come si fa? Si usa la tecnia della fuzione: prendo le n sottoclassi e le fondo nella superclasse:
![[Fusione.png]]

Quindi per capire meglio:
Studente ha il numero di matricola
Persona ha il nome 
e Docente ha la data di nascita 
Tutto questo viene messo nella superclasse Persona perchè deve catturare tutti i casi e diventa una sola classe cioè Persona.
Però non tutte le persona hanno la matricola, quindi si mette l'attributo 
`is_studente` di tipo `bool` e matricola diventa opzionale(`[0..1]`).
Inoltre ogni Stud è iscritto ha un corso di laurea, ma adesso la classe Persona ingloba la classe Studente ma ogni Persona non è iscritto a un corso di Laurea, quindi bisogna scrivere nella specifica dei vincoli esterni p:
Per ogni p:Persona se p.is_studente = True allora :
	-  p.matricola ha un valore
	- p.partecipa ha un link 'iscritto'
	Quindi se patecipa a un link 'iscritto' è uno studente
Di conseguenza si deve inserire anche un attr. `is_docente:bool`
QUindi anche la nascita diventa opzionale e come per l'assoc. iscritto anche il vincolo su afferenza diventa `0..1` perchè non tutte le Persone afferiscono a un Dipartimento.
Una persona può non essere sia DOcente che Stud?Si
Una persona può essere solo Stud? Si
Una perosna può essere solo Docente?Si
Una persona può essere entrabi ? Si

Otteniamo un diagramma nuovo, i vincoli estenri sono importanti perché senza il diagramma è sbalgiato.
Nella fusione i vincoli sono sempre uguali e gli attributi della sotto


Nel complete:
![[Ristr complete.png]]

In questo caso cambia solo il vincolo estenro perchè può essere sia docente che Studente, quindi si aggiunge un vincolo che per ogni p:Persona:
p.is_docente = True oppure p.is_studente = True

Nelle generalizzaioni di assoc.: 
non cambia nulla 
e se invece: 
![[Ristr assoc. con generalizzazioni.png]]
In questo caso ArticoloNuovo si è fuso con ArticoloInVendita, e Utente si è fuso con VenditoreProfessionale.
Inolte ArticoloInVendita ha l'attributo condizione(cond) che è un tipo enumerativo che mi dice che l'articolo e nuovo o usato. Stessa cosa per Utente che ha acqusito l'attributo tipo che mi dice se l'utente e un venditore professionale o un smeplice utente.
Avendo fuso queste due classi si deve fondere anche l'associazione, pero attenzione: dobbiamo mettere nella specifica dei vincoli estenri 
per ogni a:ArticoloInVendita:
	- se a.cond = 'nuovo' allora a.anni_garanzia di tipo IntGE2
	- se a.cond = 'nuovo' allora il link (a,u): venditore nel quale 'a' è coinvolto è tale che u.tipo = 'prof'. 
In questo caso sto dicendo che se la condzione dell'articolo è 'nuovo' allora l'istnaza di venditore che partecipa al link di associazione in cui è è coinvolto è tale che il vlaore dell'attributo tipo di Utente è professionale