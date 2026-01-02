
# Introduzione 

Flask è un micro web framework scritto in [[Introduzione a Python|Python]], sviluppato da [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher) e una parte del Pallets project.
Permette di svillupare applicazione web in maniera semplice.

## Model View Controller (MVC)
Prima di affrontare Flask dobbiamo capire cos'è l'architettura MVC, per capire bene come Flask lavora. 

![[MVC.png]]

 L’**architettura MVC** suddivide un’applicazione in tre componenti principali, con l’obiettivo di separare la logica di presentazione da quella di business e di gestione dei dati.

#### **1. View (Vista)**

- **Ruolo:** rappresenta l’interfaccia utente (UI).
    
- **Tecnologie tipiche:** HTML, CSS, JavaScript.
    
- **Funzione:** mostra i dati all’utente e riceve le sue azioni (input, click, form, ecc.), che vengono poi inviate al **Controller**.
    

#### **2. Controller**

- **Ruolo:** gestisce la logica applicativa e coordina il flusso di comunicazione tra **View** e **Model**.
    
- **Tecnologie tipiche:** linguaggi lato server come Python (Flask, Django), Java, PHP, Ruby, ecc.
    
- **Funzione:** riceve le richieste dell’utente dalla View, elabora i dati (eventualmente interagendo con il Model) e restituisce la risposta appropriata alla View.
    

#### **3. Model**

- **Ruolo:** rappresenta la struttura dei dati e la logica di accesso al database.
    
- **Tecnologie tipiche:** SQL, ORM (Object-Relational Mapping), query al database.
    
- **Funzione:** gestisce la memorizzazione, l’aggiornamento e il recupero delle informazioni.
    

#### Flusso di interazione

1. **L’utente** compie un’azione nella **View** (es. clicca un bottone).
    
2. La **View** invia la richiesta al **Controller**.
    
3. Il **Controller** elabora la richiesta e, se necessario, interagisce con il **Model** per leggere o modificare i dati.
    
4. Il **Model** aggiorna o fornisce i dati richiesti.
    
5. Il **Controller** riceve i risultati e aggiorna la **View**.
    
6. La **View** mostra i nuovi dati all’utente.
### Cos è Flask
Flask è un **micro-framework** per Python, chiamato così perché **non include nativamente un livello di gestione del database né funzionalità avanzate di validazione dei form**, e richiede quindi poche librerie esterne.  
Il suo compito è gestire la **comunicazione tra il client (frontend)** e il **server (backend)**.
Quindi Flask offre al programmatore la **flessibilità di scegliere il database** con cui integrarsi e di utilizzare le librerie che preferisce per la validazione dei form.  

> [!abstract] **Cos è la validazione dei form**
>La validazione dei form consiste nel **controllare e verificare i dati inseriti dall’utente** prima di inviarli al database, per garantire che siano corretti e sicuri, evitando errori o l’iniezione di codice arbitrario.
### Framework per costruire le web app in Python
Osservando lo schema:

![[Framework per costruire le web app in Python.png]]

Possiamo descrivere il processo passo per passo:

1. **Client (es. il browser)**  
    L’utente digita un indirizzo web, ad esempio `http://mywebsite.com`, e invia una **richiesta HTTP GET** al server per ottenere la homepage.
    
2. **Backend (Flask + Python)**  
    L’app Flask riceve la richiesta, la elabora e individua quale funzione (detta _view function_) deve essere eseguita per rispondere alla route richiesta (`/` in questo caso).  
    Questa funzione restituisce una **risposta HTTP**, che può essere:
    
    - una pagina HTML generata dinamicamente, oppure
        
    - dati in formato JSON (nel caso di un’API), ecc.
        
3. **Server (Web Server o WSGI Server)**  
    Il server riceve la risposta da Flask e la invia al client.  
    In ambiente di sviluppo, Flask include un piccolo server integrato; in produzione, invece, si usa solitamente un server WSGI come _Gunicorn_ o _uWSGI_.
    
4. **Client (Frontend)**  
    Il browser riceve la risposta e la interpreta: se è HTML, renderizza la pagina visibile all’utente (es. “Hello, world!”).



> [!example] **Esempio Pratico:**
>```python
> from flask import Flask
>
>app = Flask(__name__)
>
>@app.route('/')
>def home():
 >   return "<h3>Hello, world!</h3>"
>
>if __name__ == '__main__':
 >   app.run(debug=True)
>```
>**Flusso di esecuzione:**
>
>1. Il browser invia `GET /` → `http://127.0.0.1:5000/`
 >   
>2. Flask intercetta la richiesta e chiama `home()`
  >  
>3. `home()` restituisce una risposta HTML
 >   
>4. Flask invia la risposta al browser, che mostra “Hello, world!”

### Installare flask 
Per utilizzare Flask bisogna avere python installato maggiore alla versione 3.9
Di norma si installa tramite riga di comando (su windows e linux)
```shell
pip install flask
```

> [!warning]
> Se non funzionasse si puo eseguire con il comando (solo linux): 
> ```shell
> apt install flask 
> ```
> 




### Scrivere la prima applicazione in Flask
Per usare flask su Python bisogna importare il framework `Flask` dal modulo `flask`.

```python
from flask import Flask
```
Ecco il codice minimo per creare e avviare una semplice applicazione Flask:
```python
from flask import Flask

# Creiamo un'istanza dell'app Flask
app = Flask(__name__)

# Avviamo il server di sviluppo
# debug=True attiva il debug mode (utile solo in fase di sviluppo)
# host='127.0.0.1' indica che il server sarà accessibile solo dal computer locale
# port=5000 specifica la porta su cui il server ascolta
app.run(debug=True, host='127.0.0.1', port=5000)
# In produzione, impostare debug=False

```

#### Spiegazione passo-passo

1. Importazione della classe Flask: 
	`from flask import Flask` 
	-  Questa riga importa la classe `Flask`, che serve per creare l’applicazione web.
2. Creazione dell’istanza dell’applicazione: `app = Flask(__name__)`
- `__name__` indica il nome del modulo corrente.
    
- Flask lo usa per capire dove cercare **template**, **file statici** e altre risorse.
    
- In pratica, dice a Flask “questa è la mia applicazione principale”.

1. Avvio del server di sviluppo: `app.run(debug=True, host='127.0.0.1', port=5000)`
   
	- `debug=True` abilita:
    
	    - il **debug interattivo** (per rilevare errori e vedere dettagli nel browser);
        
	    - il **reload automatico** quando modifichi il codice;
        
	    - la **configurazione di sviluppo**, con logging dettagliato.
        
	- `host='127.0.0.1'` limita l’accesso al solo computer locale.
    
	- `port=5000` specifica la porta su cui il server ascolta.
In produzione la modalità debug deve essere settata a False perché permette di eseguire codice arbitrario

### Eseguire l'applicazione flask

Per eseguire il codice su terminale 
```shell
python3 nomeFile.py
```

Il codice viene eseguito e viene creato l'oggetto flask con valore `__name__` 

#### Definire le route statiche 

Una volta creata la web app bisogna definire le risorse : si usano i [[#I Le Classi **Utilizzo dei Decoratori** `@property` **per Getter e Setter** decorators in Flask|decorators]] 
ad esempio: 
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home() -> str:
	return "<h3>Hello, world!</h3>"
```


> [!NOTE] `@app.route` è un metodo GET dell'HTTP


Dobbiamo sempre definire la route, quindi deve sempre portare alla homepage.
Levando `app.run` possiamo eseguire il codice nel modo visto prima, levando l'`app.run` si deve essere il comando: 
```shell
flask --app main run
```

In questo modo il server si avvia non in modalità debug.

Supponiamo di avere un `main.py` che contiene la nostra applicazione, finchè c'è l'`app.run()` possiamo avviare l'applicazione tramite riga di comando `python3 main.py`, in questo modo però se cambiamo i valori di defualt dobbiamo sempre salvare e rilanciare l'app.
Eliminare l'`app.run()` abbiamo due modi per lanciare l'app:
```shell
flask --app MAIN run --port 4000
```
In questo modo posso cambiare la porta senza dover cambiare il codice.
L'altro metodo prevede: 
il file main.py deve essere rinominato app.py e quando eseguo il comando 
```shell
flask run
```
l'app viene lanciata e non si deve specificare il nome del file, basta che il nome del file si chiami app.py.
Ovviamente anche con questo comando posso cambiare altri valori come il numero della porta.
```shell
flask run --port 4000
```

Come dicevamo questo è un route statico: ad ogni funzione associamo la route 

#### Route dinamici
Nel mondo reale la maggior parte dei path sono dinamici, come si definisco questi URL dinamici? 
SI utlizzano sempre i decoratori 
```python
@app.route('/user/<string:username>')
def show_user_profile(username: str) -> str:
return f"Profilo di {username}"
@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
return f"Post {post_id}"
```

la variabile nel path diventa l'argomento della funzione che poi viene usato per restituire il messaggio personalizzato a quella richiesta.
Per capire meglio: nel primo esempio sto dicendo "vai alla route user, poi passa alla route degli username degli utenti".
Quindi se passo una il nome `"Marco"` nell'invocazione della funzione mi restiruisce il messaggio `"Profilo di Marco"`

Se nell'input della funzione non specgichiamo il tipo di default è una stringa, altri tipi possibili sono
- int
- float
- path
- uuid
Di base noi creiamo un URL e dentro l'URL gli passo quei dati specifici per darmi quella risposta.
Di base i path che si mettono dentro i decoratori sono i path di un URL quindi se vado nel mio borwser e scrivo : `user/Marco` mi restiuirà il messaggio `Profilo di Marco`.
Le parti dinamiche devono sempre essere previste come arogmenti delle funzioni 
Se aggiungiamo una parametro age e nel bowrser scrivo `user/Marco/age/18`
mi restiruisce il messaggio  `profilo di Marco : 18 anni` 

Quando siamo in `@app.route` senza speicficae nulla stiamo facendo chiamate get:
se sappiamo che c'è un path che viene usato solo per i get posso scrivere: 
`@app.get()` stessa cosa per chiamate post `@app.post`.
route è vantaggioso perchè 


### `url_for()` — Ricostruire dinamicamente gli URL
Nel mondo reale, molti percorsi (URL) sono **dinamici** e quindi non noti a priori.  
La funzione `url_for()` di Flask permette di **ricostruire automaticamente l’URL associato a una determinata funzione di view**, evitando di scriverlo manualmente.


> [!done] **Vantaggi Principali**
>1. **Astrazione dal percorso fisico:** 
> 	  - non è necessario ricordare o riscrivere la route manualmente. 
> 	  - Flask la ricava dal nome della funzione.
 >   
>2. **Manutenzione semplificata:** 
> 	  - se una route cambia nel codice, `url_for()` aggiorna automaticamente tutti i riferimenti.
  >  
>3. **Percorsi sempre assoluti:** 
> 	  - i link generati sono sempre completi (non relativi), riducendo gli errori di navigazione.
  >  
>4. **Gestione automatica dei caratteri speciali:** 
> 	  - gli spazi o simboli vengono convertiti in codifica URL-safe (es. `John Doe` → `John%20Doe`).


##### Esempio Pratico: 
```python
from flask import Flask, url_for
app = Flask(__name__)

# Definisce la route principale (`home`) necessaria come punto di ingresso dell’applicazione.
@app.route('/')
def home():
    return "Homepage"

#Cattura un parametro di tipo stringa, correttamente tipizzato, e lo mostra nella risposta HTML.
@app.route('/user/<string:username>')
def show_user_profile(username):
    return f"Profilo utente: {username}"

#Cattura un parametro numerico (`int`) e lo restituisce nella risposta. 
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post n° {post_id}"

# Utilizzato nel contesto di test (`app.test_request_context()`), è il modo corretto per costruire dinamicamente gli URL delle route definite.  

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('show_post', post_id=42))

```

**Expected Output:**
```shell
/
/user/John%20Doe
/post/42
```

Quindi printa su terminale i diversi percorsi URL permettendoti di costruire dinamicamente i path URL visualizzandoli su terminale

**Interpretazione:**
La funzione `url_for()` costruisce dinamicamente i percorsi:

- `url_for('home')` → restituisce la route `/`
    
- `url_for('show_user_profile', username='John Doe')` → sostituisce il parametro `<username>` con il valore fornito
    
- `url_for('show_post', post_id=42)` → sostituisce il parametro `<post_id>` con `42`



### I [[Python/Lezione 6_ Le Classi_ Gli attributi pubblici,privati, gli attributi di classe e i metodi di classe/Le Classi#**Utilizzo dei Decoratori** `@property` **per Getter e Setter**|decorators]] in Flask
Le funzioni sono **first class objects:** 
- ==una funzione può essere passata come parametro di un altra funzione, non il valore di ritorno della funzione ma la funzione stessa.==
Quindi si può scrivere una cosa del genere: 
```python
def fun1()->str:
	return "Hello"
	
def fun2(fun):
	fun()

fun2(fun1) #Da notare che passo la funzione stessa senza parentesi quello che viene indicato è la zona di memoria dove fun1 si trova
```

L'inteprepte py quando legge le funzioni prima di eseguirle va a leggere lo spazio in memoria dove sono salvate.
In questo caso sto passando il riferimento di memoria, se eseguo fun2 questa funzione richiama qualsiasi funzione gli sto passando in questo caso `fun()`. 
Quindi quando eseguo fun2 questa esegue la funzuone fun che altro non è che la funzione fun1 nell'invocazione di fun2.
In altre parole: 
```python
def ciao()
	return "Hello"

def fun2(fun):
	fun()

fun2(ciao)
```


I decorators fanno qualcosa di simile: è una funzione che prende in input un altra funzione, quella che vogliamo decorare, viene decorato dal decoratore, in questo caso fun2 sarebbe il decoratore mentre ciao è la funzione che ogliamo decorare.

Inner function e outer function
Una funzione può prendere in ingresso un altra funzione ma può anche ritornarla: 
fun2 può prendere in ingresso ciao() ma può anche ritornare ciao().



Differenza tra funzioni estrene ed interne:
Le funzioni possono contenere quello che volgiamo:
```python
def parent():
	print("Printing from parent()")
	
	def first_child():
		print("Printing from first child")
	def second_child():
		print("Printing from second child")
	second_child()
	first_child()
```

QUanda la funzione parent è stata eseguita tutta se non trovo il modo di tirare fuori le funzioni interne non possono essere usate globalmente.
I deocrators vanno ad espandere le funzionalità delle funzioni, l'esempio è il cronometro, usando un decoratrs sulla funzione del cronometro posso, ad esempio vedere il tempo di runnig della inner function cronometro().

Andiamo a vedere come fare un decorator cronometro: 
```python
import time
def cronometro(fun): #è il decorators (@cronometro)
	def wrapper() #avvolge la funzione che si vuole decorare
		start = time.time()
		fun()
		print(time.time()-start)
	return wrapper #non l'ho ritorno con le parentesi ma ritorno il riferimento perché non volgio passare la funzione ma il suo indirizzo di memoria 
```

Una volta definito l'heaer ho bisogno di una inner function.
Ora: 
voglio sapere quanto ci mette questa funzione a runnare, uso quindi il decorator cronometro
```python
@cronometro
def ciao():
	print("hello")
```

Un modo per applicare il decoratore è cosi, quando scrivo la chiocciola sto facendo : 
```python
ciao = cronometro(ciao)
```
QUindi quando assegno ciao al cronometro eseguo wrapper e i riferimeti di ciao si trovano nel corpo di wrapper (`fun()`) quindi la funzione ciao contiene il wrapper del cronometro. 
Quindi se eseguo ciao() sto ritornando la funzione wrapper (), la differenza è che nella funzione wrapper fun() ha come valore ciao().
Questo
```python
ciao = cronometro(ciao)
```

viene definito da
```python
@cronometro
```

È solo sintassi, detto anche zucchero sintattico; se scriviamo `ciao = cronometro(ciao)` è la stessa cosa di `@cronometro`. 

Quindi il decoratore è una funzione che prende in input una funzione e restiruisce la funzione decorata.
Metto `*args` nel decorator perchè devo poter passar qualsiasi arogmento nel wrapper e in fun().
```python
import time

def cronometro(fun):

    def wrapper(*args):

        start = time.time()

        fun(*args)

        print(time.time()- start)

    return wrapper

@cronometro

def ciao():

    print("Hello")

# ciao = cronometro(ciao)

# @cronometro

ciao()
```


Questo è un disegn pattern per risparmiare codice.

### Implementare [[Lezione 4 - Protocollo HTTP 2 parte#^verbiHTTP|i verbi HTTP]] in Flask
Se in Flask scrivessimo 
```Python
@app.route ('/libri', method = 'GET')
	def get_libri():
	#corpo della funzione
```

Automaticamente quando arriva una richiesta [[Lezione 4 - Protocollo HTTP 2 parte#^04d1a5|GET]] al server Flask richiamerà questa funzione
Ora mettiamo che: 
```python
@app.route ('/libri', method = 'GET')
	def get_libri():
		libri = db.get_libri()
		return jsonify(libri), 200
```

In questo modo noi costruimao un dizionario `libri` e restituisce la risposta HTTP, 
Il 200 è lo [[Lezione 4 - Protocollo HTTP 2 parte#Status Code HTTP|status code]].
Il flusso è: 
Il client fa una richiesta, 
la richiesta viene creata automaticamente
la richiesta arriva al codice Flask
Flask manda la richiesta al DB
il DB manda a Flask la risposta 
Flask construisce e rimanda la risposta in forma JSON al client 

Metodo app.route non restituisce niente, se metto `return "Hello Wordl"` flask è abbastanza intelligente da sapere che deve costruire la risposta con quella stringa
```python
@app.route ('/')
	def home():
		return "Hello World"
```

Ora creaimo un server con Flask
```
from Flask 
```



