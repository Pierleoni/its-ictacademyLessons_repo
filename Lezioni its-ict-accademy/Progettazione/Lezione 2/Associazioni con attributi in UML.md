
# Introduzione
Come abbiamo detto sulla lezione [[Analisi dei requisiti mediante UML]], le associazioni descrivono relazioni tra classi. 
In alcuni casi, però, la relazione stessa possiede proprietà specifiche che non appartengono alle singole classi coinvolte, ma alla loro **_istanza di collegamento_**. Per rappresentare questa situazione, si utilizza un’**associazione con attributo**: 
==un attributo legato direttamente al nesso tra le classi, anziché a una di esse.== 

## Associazioni con attributi
Si vuole progettare un sistema che gestisce gli esiti voti in trentesimi dei test superati dagli studenti di un corso.
Il corso è diviso in moduli e uno studente può superare il test di ogni modulo al più una volta.
![|523x141](https://i.imgur.com/zFS1lTS.jpeg)
Quindi abbiamo due classi:
- `Studente`
	- con l'attributo `nome` di tipo `Stringa`
- `Modulo`
	- con l'attributo `nome` di tipo `Stringa`
e vi sono anche due [[Vincoli di molteplicità sulle associazioni e sugli attributi#Semantica dei vincoli di molteplicità sui ruoli delle associazioni|vincoli di molteplicità ]] `0..*`, perché:
 uno studente può superare tanti moduli e i moduli possono essere passati da tanti studenti. 
 Tuttavia come possiamo notare l'attributo `voto` non può essere associato né alla classe `Studente` é alla classe `Modulo`: poiché un voto non è una proprietà locale di uno studente, né di un modulo, ma è una proprietà del legame tra uno studente e un modulo, quindi è una **proprietà dell'[[Analisi dei requisiti mediante UML#^associationsDef|associazione]]**.  

![](https://i.imgur.com/53nyHiL.jpeg)
 
 metto un associazione con attributi (da notare che ha la stessa forma della classe ma la prima lettera è minuscola). Quindi adesso non è più il modulo studente o modulo ad avere l'attributo voto 
ma è il link ad avere questo attributo.
Tuttavia non esistono  link distinti con gli stessi oggetti coinvolti. 
Quindi anna → Py non è una quadrupla ma una coppia per questo non è ammesso.
Un link è identificato dagli oggetti che vi partecipano, e i valori degli attributi di un link non contribuiscono a identificare un link 
quindi scrivero 
SI --> (alice,py),<27,3/5/2025>:test superato
      (alice,py), <25,7/8/2025>: test superato é lo stesso link ma non può esistere.
NO --> (alice,py,27,3/5/2025):test superato

Se devosi modellare questa realtà dovtei intrudurre il concetto di sostenatmento dell'esame, cioè uno studente può sostenere lo stesso esame più volte.

L'associone della classe può avere un'associazione con un altra classe ad esempio Professore che ha somministrato e verbalizzato l'esame.
Comunque non cambia la natura dell'associazione perché non posso avere due link che legano Anna a py. 