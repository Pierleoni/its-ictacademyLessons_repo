
![[Ripasso.png]]
4) Cosa distingue un'operazione di classe da un'operazione di Use-Case?
	Uno use case è un insieme omogeneo di funzioni, quindi un insieme omogeneo di funzionalità.
	Uno case può essere usato da un attore: 
	gli attori nel diagramma non sono gli utenti, è un ruolo con cui un utente umano o un sistema esterno può usare il sistema. QUindi l'attore Marco può usare il sistema con diversi ruoli, ad esempio su moodle un docente può utilizzare il sistema con il ruolo di studente o docente, quindi con ruoli diversi.
	I diversi ruoli possono dare diverse features.
	Se devo dire che il manager può usare il sistema come il privato si utilizza la generalizzazione: stiamo dicendo che il manager può utilizzare il sistema come lo utilizza l'attore privato

L'operazione di classe è: 
	una proprietà degli oggetti di quella classe, come gli attributi che sono statici, mentre le operazioni lo calcolano quando viene richiesto quindi sono dinamici.
	Poi quando la classe UML diventerà una class Python quell'operazione di classe diventa un metodo.
Una differenza:
l'operazione di classe è dentro il sistema, ciè nella classe mentre uno Use case è modo di gestire il sistema di fuori.
Chi invoca un operazione di classe? Un vincolo, un altra operazione di classe
Quindi un operazione di classe sono invocati gli oggetti quindi si avrà il this mentre nello use case essendo più generico non ha il this.

6) Cos'è un attributo multi-valore e come si indica in UML? è un attributo che può avere più valori come `email:Email[1..*]` o `email:Email[0..*]`.
   Un attributo opzionale è un attributo che come vincoli `[0..1]` e `[0..2]`, anche lo zero to star può essere un attributo opzionale.
   
