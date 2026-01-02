Per implementare le classi UML in class Python, la metodologia consiste fare una class Python per ogni classe UML e per ogni tipi di dato non base (codice fiscale, etc.).
Quindi dobbiamo scrivere un programma python che sia al 100% compatibile con il diagramma delle classi.
Quindi bisogna scrivere la class elencando gli attributi, **che devono essere sempre protetti mai pubblici.** 
==L'idea dietro a questa metodologia è che la modifica e la gestione dei valori degli attributi sia responsabilità della classe in modo interno==. 
Quindi abbiamo visto nella lezione [[Evoluzione delle proprietà e visibilità delle proprietà]] come [[Evoluzione delle proprietà e visibilità delle proprietà#^propDiClasse|evolvere le proprietà di una classe]] e la differenza tra un attributi [[Evoluzione delle proprietà e visibilità delle proprietà#^attrUMLpubblici|pubblico]], [[Evoluzione delle proprietà e visibilità delle proprietà#^attrUMLprivato|privato]] o [[Evoluzione delle proprietà e visibilità delle proprietà#^attrUMLprotetto|protetto]].  

## Implementare le classi del diagramma UML in Python
Prendiamo ad esempio la classe `Studente`:

![[Screenshot 2025-05-23 at 18-48-03 Meet - bmb-xnne-ahh.png]]


Per le proprietà `telefono` e `email` si sceglie di utilizzare un set perché  le collection di dati  essendo uniche per ogni oggetto della classe, quindi non si accettano ripetizioni e perché gli elementi devono essere immutabili:
``` run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
```

### I metodi getter 
Per gli attributi [[Evoluzione delle proprietà e visibilità delle proprietà#^attrUMLpubblici|pubblici]] dobbiamo usare i [[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#**Gestione degli Attributi con Getter e Setter**|getter]]:
come abbiamo già detto nelle lezioni di Python [[Ereditarietà delle classi#Gli attributi protetti|Ereditarietà delle classi]] e nei paragrafi [[Public, Private and Class Attibutes, Class and Static Methods#Gli attributi pubblici|Gli attributi pubblici]] e [[Public, Private and Class Attibutes, Class and Static Methods#Attributi privati|Gli attributi privati]], non esiste il concetto in Python di "pubblico" o "privato" impostato dal linguaggio (come in altri linguaggi tipo Java o C++), ma si usa la convenzione di rendere tutti gli attributi protetti (con il simbolo del singolo underscore `_`) e si gestisce l'acceso solo tramite i [[Public, Private and Class Attibutes, Class and Static Methods#Accesso agli attributi Privati Getter e Setter|metodi getter e, eventualmente,  i setter ]]. 
```run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
	def matricola(self)->int:
		return self._matricola
	def nome(self)->str:
		return self._nome
	def genere(self)->Genere:
		return self._genere
	def telefono(self)->set[Telefono]:
		return set(self._telefono) # una copia immutabile!
	def email(self)->set[Email]:
		return set(self._email) # una copia immutabile!
```
 In questo esempio:
 - `_matricola`: un attributo immutabile(perché il numero di matricola di uno studente è univoco per ogni studente) e noto alla nascita dell'oggetto `studente`
 - `_nome`: attributo mutabile (il nome di uno studente può cambiare da studente a studente) e noto alla nascita dell'oggetto `studente`.
 - `_genere`: attributo con valore di tipi specializzato (enum) noto alla nascita dell'oggetto `studente`.
 - `_telefono`: un attributo di tipo `set`, noto alla nascita dell'oggetto studente.
 - `_email`: un attributo noto alla nascita dell'oggetto studente.
 Tutti le funzioni in questo caso le funzioni sono dei getter:
```python
 def telefono(self) -> set[Telefono]:
    return set(self._telefono)  # restituisce una copia!
```
 



La variabile `s` contiene un riferimento in memoria all'oggetto `{1,2,3}` ,
qujdi quando s si assegna a una collection set viene creato prima l'oggetto set in memoria e la variabile conterrà un riferimento a qusto oggetto in memoria.
Se si faccesse:
```
s = {1,2,3}
t = s
print(t)
```
In questo caso t punta al riferimento in memoria dove punta s, ma se si facesse:
``` run-python
s = {1,2,3}
t = s
print(t)
t.add(4)
print(t)
print(s)
```
Ma se si scirvesse:
```
s = {1,2,3}
t = s
print(t)
t.add(4)
print(t)
print(s)
 s = {4,5,6}
 print(s)
```
Viene creato un nuovo oggetto set in memoria e s punta al riferimento in memoria dove si trova quell'oggetto. 
Ma se si scrivesse:
```
s = {4,5,6}
s = {4,5,6}
print(s)
```
Ora l'ultimo oggetto `{4,5,6}` ha come riferimento `s` il primo non ha più rifertimento è diventa una garbage collections e viene cancellato.
Quindi dentor una variabile assegnata a un oggetto c'è un riferiemtno in memoria di quell'oggetto 
> [!NOTE]
> In python c'è differenza se si scrive:
> ```
> x = 1
> s = {1,2,3}
> ```
> Se si lancia il tipo di dato di vlaore primitivo cioè l'1 della x sono unici, non essitono due vlaori primitivi differenti:
> ```run-python
> x = 1
> y = 1
> s = {1,2,3}
> print(id(x))
> print(id(y))
> 
> ```
> Come possiamo vedere l'hash è sempre lo stesso quindi se si facesse: 
> ```run-python
> x = 1
> y = x 
> x = 2
> print(y)
> 
> ```
>  y rimane sempre 1.
>  Qui se x è 1 e y = x allora 1 viene copiato, la variabile non punta a un oggetto in memoria 

Ora se chiamassi i getter di telefoni ed email e usassimo aggiungessimo elementi tramite il metodo `.add()`, Python non lo impedisce perché il getter di telefoni e email tornano un inieme di elementi che si possono modificare. Per ovviare a questo problema restituiamo un frozenset:
il forzenst di un ineisem crea una copia non modificavbile di quell'insieme:
```run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
	def matricola(self)->int:
		return self._matricola
	def nome(self)->str:
		return self._nome
	def genere(self)->Genere:
		return self._genere
	def telefono(self)->frozenset[Telefono]:
		return frozenset(self._telefono) # una copia immutabile!
	def email(self)->frozenset[Email]:
		return frozenset(self._email) # una copia immutabile!

s = Studente()
s._telefono = {Telefono("3334445566")}
telefoni = s.telefono
```

QUindi quando diamo il campo di un oggetto non possiamo dare il campo di quell'oggetto modificabile, bisogna restituirlo immutabile.
Ora per i setter, entra in cmapo l'immutabilità, se un'attributo è immatubile la class che implementa matricola non darà un set ma invece sicocme nome è mutabile implemterà un setter:
```run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
	def matricola(self)->int:
		return self._matricola
	def nome(self)->str:
		return self._nome
	def genere(self)->Genere:
		return self._genere
	def telefono(self)->frozenset[Telefono]:
		return frozenset(self._telefono) # una copia immutabile!
	def email(self)->frozenset[Email]:
		return frozenset(self._email) # una copia immutabile!
	# def set_matricola(…) <— no, è <<imm>> e noto alla nascita
	def set_nome(self, n:str)->None:
		self._nome:str = n
	def set_genere(self, g:Genere)->None:
		self._genere:Genere = g
	# nota: g è immutabile

s = Studente()
s._telefono = {Telefono("3334445566")}
telefoni = s.telefono
```

Per gli attributi multi vlaori e mutabili i metodi che devo implementare sono add() e remove():
```run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
	def matricola(self)->int:
		return self._matricola
	def nome(self)->str:
		return self._nome
	def genere(self)->Genere:
		return self._genere
	def telefono(self)->frozenset[Telefono]:
		return frozenset(self._telefono) # una copia immutabile!
	def email(self)->frozenset[Email]:
		return frozenset(self._email) # una copia immutabile!
	# def set_matricola(…) <— no, è <<imm>> e noto alla nascita
	def set_nome(self, n:str)->None:
		self._nome:str = n
	def set_genere(self, g:Genere)->None:
		self._genere:Genere = g
	# nota: g è immutabile
	def add_telefono(self, t:Telefono)->None:
		self._telefono.add(t)
	def remove_telefono(self, t:Telefono)->None:
		if len(self.telefono()) > 1:
			self._telefono.remove(t)
		raise RuntimeError ("Uno studente deve avere almeno un numero di telefono")
	def add_email(self, e:Email)->None:
		self._email.add(e)
	def remove_email(self, e:Email)->None:
		self._email.remove(e)

s = Studente()
s._telefono = {Telefono("3334445566")}
telefoni = s.telefono
```

Il costruttore `__init__()` in questo caso lo si usa per gli attributi noti alla nascita:

```run-python
class Studente:
# campi dati:
	_matricola: int #<<imm>>, noto alla nascita
	_nome: str # noto alla nascita
	_genere: Genere # noto alla nascita
	_telefono: set[Telefono] # noto alla nascita
	_email: set[Email] # non noto alla nascita
	def matricola(self)->int:
		return self._matricola
	def nome(self)->str:
		return self._nome
	def genere(self)->Genere:
		return self._genere
	def telefono(self)->frozenset[Telefono]:
		return frozenset(self._telefono) # una copia immutabile!
	def email(self)->frozenset[Email]:
		return frozenset(self._email) # una copia immutabile!
	# def set_matricola(…) <— no, è <<imm>> e noto alla nascita
	def set_nome(self, n:str)->None:
		self._nome:str = n
	def set_genere(self, g:Genere)->None:
		self._genere:Genere = g
	# nota: g è immutabile
	def add_telefono(self, t:Telefono)->None:
		self._telefono.add(t)
	def remove_telefono(self, t:Telefono)->None:
		if len(self.telefono()) > 1:
			self._telefono.remove(t)
		raise RuntimeError ("Uno studente deve avere almeno un numero di telefono")
	def add_email(self, e:Email)->None:
		self._email.add(e)
	def remove_email(self, e:Email)->None:
		self._email.remove(e)
	def __init__(self, mat:int, nome:str, g:Genere, t:Telefono):
		self._telefono = set()
		self._email = set()
		# mat è <<imm>> e noto alla nascita, quindi non ha metodo setter:
		# mettiamo il codice qui (unico punto dove può essere eseguito)
		self._matricola:int = mat
		self.set_nome(nome)
		self.set_genere(g)
		self.add_telefono(t)

s = Studente()
s._telefono = {Telefono("3334445566")}
telefoni = s.telefono
```
