Lo stile rest prevede una serie di vincoli: 
1. Stateless: non deve essere necessario l'uso della sessione 
2. Altro importante vincolo è quello che ogni richiesta venga processato al fine di produrre una risorse che il programma client userà: non mettere i verbi nella risorsa, ma mettere i sostantivi.
	- Quindi da un punto di vista della funzionalità non cambia nulla mettere i verbi al posto dei sostantivi nella URL, ma non rispetta lo stile Rest. 

Livelli di rest: 
il livello 0 è il livello è l'anarchia 
il livello 1 e 2 vanno in coppia
il livello 3 aggiunge link ipermediali per guidare l'utente (non smepre viene implementato). 
Il livello 3 impatta sulla sostanza: come scrivere i servizi. 
Difatti essendo il più impegantivo non viene sempre integrato nei progetti. 


Il livello 1 impone di mettere l'identificativo sulla URL della risorsa che vuoi ottenere
Il livello 2 aggiunge i verbi http
Il livello 3 usa link ipermediali che guidano il client per estendere la risorsa. 
(Librearia HATEOAS di Java).



idempotenza → **se si fa più di una volta una chiamata al database lo stato  del db(Server) non cambia.** (es: DELETE).

Queste cose servono per l'appunto nei microservizi: finora abbiamo fatto progetti a servizi, ma quando le applicazioni sono spezzate a microservizi; questi servizi si parlano di continuo e hanno sempre più di una istanza che possono vivere e morire di continuo, quindi se una richiesta fallisce si può rifarla a cuor leggero a patto che la richiesta sia idempotente. 


