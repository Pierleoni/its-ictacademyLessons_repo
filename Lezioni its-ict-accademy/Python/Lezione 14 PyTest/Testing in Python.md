Fare i test in Python è molto importante ed è una parte essenziale nel software development: ci assicura che il codice fa quello che devo fare e ci permette di rispamiare tempo e denaro. Di solito si ha poco tempo a disposizione per stare dietro agli errori, quindi appena si sviluppa un pezzo di codice si passa alla fase di test per assicurarci che nel caso si trovino degli errori questi possono venire fixati subito, anche perché se troppi errori si accumulano può diventare un problema.
Quindi in sostanza bisogna scrivere piccoli pezzi di codice di test anche detti unità di test (test unity), quindi permettono di assicurarci che quel blocco di codice lavori come ci aspettiamo.
Per fare i test python presetna due framework: Pytest e unitest
Per fare i test dobibamo capire coem funziona assert:
comando built-in che consente di asserire/ affermare che una certa condizione è vera. 
Se poi la condizione che noi asseriamo essere vera è falsa allora viene sollevarto un `assertionError`.
In un file chiamato `prova.py`, scriviamo:
```python
assert 1>0
```

Se facciamo runnare il programma non succede nulla, se si modifica l'asserzione:
```python
assert 1 < 0
```

Se si runna il codice viene sollevato un AssertionError questo perché si sta spacciando una codizione flasa come vera e quindi la condition assertemtn faliscie.
SI può customizzare i messagi con l'assert:
```python
assert 1 < 0, 'The Condition is False’
```
QUando si runna il progrmamma viene sollevato l'errore di assertion e viene visualizzato cosi:
```shell
Traceback (most recent call last):
  File "c:\Users\Project Lead\Desktop\Esercizi Programazzione ITS\Progetti_Py\Lezione 14 pytest\prova.py", line 1, in <module>
    assert 1 < 0, "The Condition is False"
           ^^^^^
AssertionError: The Condition is False
```

### La sintassi
La sisntassi delgi assert è:
```python
assert <condizione che deve essere testata>, <messaggio di errore che deve essere visualizzata>
```

### Pytest
Cancelliamo il file `prova.py`.
Andiamo sul termianlee di Vs Code per installare PyTest:
```shell
pip install -U pytest
```

Dopodiché controllare se l'installazione è avvenuta con successo:
```shell
pytest --version
pytest <numeroVersione>
```

### Convenzioni per l'organizzazione dei test con Pytest

Quando si scrivono test automatici in Python utilizzando **Pytest**, è fondamentale seguire alcune convenzioni che facilitano:

- Il riconoscimento automatico dei test da parte del framework.
    
- Una struttura ordinata del progetto.
    
- L'evitamento di conflitti di importazione.
    

#### 📁 Struttura consigliata del progetto

Si raccomanda l’uso di una struttura a cartelle coerente. In particolare:

- Creare una directory dedicata ai test, denominata `tests/`.
    
- All’interno della directory `tests/`, è possibile creare sottocartelle organizzate per modulo o funzionalità.
    
- Ogni file contenente test deve iniziare con il prefisso `test_`.
    

#### ❌ Evitare il nome `test` per la directory

È **fortemente sconsigliato** denominare la directory dei test con il nome `test`, poiché:

- `test` è un modulo della libreria standard di Python.
    
- L'utilizzo di tale nome potrebbe generare **conflitti nei nomi dei moduli**, problemi di importazione o malfunzionamenti durante l'esecuzione dei test.
    

✅ **Usare sempre la forma plurale**: `tests`.

Esempio di struttura corretta
```css
project_root/
│
├── src/
│   └── frazioni.py
│
├── tests/
│   ├── __init__.py
│   └── test_frazioni.py
│
└── requirements.txt

```

###### Convenzioni nei nomi dei file e delle funzioni

- **File di test**: devono iniziare con `test_` → es. `test_frazioni.py`.
    
- **Funzioni di test**: devono anch’esse iniziare con `test_` → es. `test_valore_frazione()`.

#### Il primo test di pytest
onsiderimao la struttura dei file nella cartella lezione 14:
```css
my_project/
├── weather.py
└── tests/
	└── test_weather.py
```

Nel file `weather.py` troviamo scritto il seguente codice:
```python
def check_weather(temperature: float) -> str:
	if temperature > 20:
		return "hot"
	elif 10 < temperature <= 20:
		return "average"
	else:
		return "cold"
```

Mentre nel file `test_weather.py`:
```python
from my_project.weather import check_weather
# passed
def test_check_weather():
	assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
	must be considered as hot'
```

Per runnare questo file bisogna andare sul terminale di vs code, andare sul nome del file, click destro sul nome del file e cliccare alla voce `Open in integrated terminal` dopodiche nel terminale scrivere :
```shell
pytest my_projects/tests/test_weather.py
```

L'output sarà: 
![[Output pytest.png]]

Analizziamo questa immagine: 
`collected 1 item`: pytest trova 1 test per runnare il file `test_weather.py`.

Il punto verde dopo `pytest my_projects/tests/test_weather.py` significa che il test è stato passato con successo. Ongi punto rappresenta un test passato.

`100%`: si riferisce all'avanzamento complessivo dell'esecuzione di tutti i casi di test.

`1 passed in 0.03s==================================`: Tutti i test (1 su 1) sono stati eseguiti con successo in 0,03 secondi.

### Caso inverso se il test fallisce 

Nel file `test_weather.py`:
```python
from my_project.weather import check_weather
# failed
def test_check_weather():
assert check_weather(5.00) == “average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'
```

Per runnare il file `test_weather.py`:
```shell
pytest my_projects/tests/test_weather.py
```

![[Output pytest fail.png]]

La f rossa che segue `my_project\tests\test_weather.py ` significa che il test è fallito
`test_chekc_weather`: è il nome del test che la sezione di errore mostra il nome del test che è fallito.
- `- average`: (-) il valore aspettato.
- `+ cold`: (+) il valore attuale.

`\===========short test summary info\=============`:
Questo è una versione compatta del report di fallimento; dice esattamente quali test sono falliti e quali tipi di errore si è verificato (in questo caso `AssertionError`).

`1 failed in 0.30s`: la conslusione del test; pytest runna 1 test fallito e l'intera esecuzione prende 0.26 secondi.

Ora continuamo a scirvere altri `test_check_weather` nel file `test_weather.py`: 

```python
from my_project.weather import check_weather
#passed
def test_check_weather1():
	assert check_weather(21.00) == "hot", "temperatures greater than 20 degree must be considered as hot"

#failed
def test_check_weather2():
	assert check_weather(5.00) == "avarege", "temperatures between 10 and 20 degree must be considered as average temperature"

#passed
def test_check_weather3():
	assert check_weather(5.00) == "cold", "temperatures lowe than 10 degree must be considered as cold"

#passed
def test_check_weather1():
	assert check_weather(13.00) == "average", "temperatures between 10 and 20 degree must be considered as average temperature"
```

L'uotput in questo caso sarà:
![[Output pytest2.png]]

Ogni  funzione `test_check_weather` definita è considerata da pytest come un singolo test che viene eseguito.
Infatti l'output mostra 4 test eseguiti: 1 fallito e 3 passati.

Tutti i nomi dei metodi devono iniziare cone la parola `test`, questa è una convenzione che utilizziamo affinché **pytest** possa identificare i test che deve eseguire, se ad esempio scriviamo:
```python
from my_project.weather import check_weather
#passed
def not_test_check_weather1():
	assert check_weather(21.00) == "hot", "temperatures greater than 20 degree must be considered as hot"

#failed
def test_check_weather2():
	assert check_weather(5.00) == "avarege", "temperatures between 10 and 20 degree must be considered as average temperature"

#passed
def test_check_weather3():
	assert check_weather(5.00) == "cold", "temperatures lowe than 10 degree must be considered as cold"

#passed
def test_check_weather4():
	assert check_weather(13.00) == "average", "temperatures between 10 and 20 degree must be considered as average temperature"
```

L'output sarà:
![[Output pytest3.png]]
Py test trova solo 3 delle 4 funzioni che abbimao scritto, questo perché la prima funziona non usa il prefisso `test` nel nome quindi viene skippata.

Ora aggiungimao un altra funzione:
```python
from my_project.weather import check_weather
#passed
def test_check_weather1():
	assert check_weather(21.00) == "hot", "temperatures greater than 20 degree must be considered as hot"

#failed
def test_check_weather2():
	assert check_weather(5.00) == "avarege", "temperatures between 10 and 20 degree must be considered as average temperature"

#passed
def test_check_weather3():
	assert check_weather(5.00) == "cold", "temperatures lower than 10 degree must be considered as cold"

#passed
def test_check_weather4():
	assert check_weather(13.00) == "average", "temperatures between 10 and 20 degree must be considered as average temperature"

# failed because every def test_function() is considered as single test
def test_check_weather5():
	assert check_weather(30.00) == "hot", "temperatures greater than 20 degree must be considered as hot"
	assert check_weather(11.00) == "cold", "temperatures lower than 10 degree must be considered as cold"
```

L'ioutput sarà:
![[Output pytest4.png]]

L'output mostra 5 test eseguiti con 2 falliti e 3 passati.
Questo accade perché, anche se la funzione `test_check_weather5` contiene due istruzioni `assert`, essa viene comunque eseguita come un **singolo test**.  
Pertanto, **ogni funzione** definita nel file di test viene eseguita come un **test unico**. 

### Pytest: test multiplici
Quando si desidera testare una funzione con molte combinazioni di input e output, **senza scrivere molte funzioni di test separate**, il decoratore `@pytest.mark.parametrize` risulta particolarmente utile.

`@pytest.mark.parametrize` è un **decoratore fornito da Pytest** che permette di eseguire **lo stesso test più volte con dati differenti**.



### Perché utilizzarlo?

- ✅ **Riduce la ripetizione del codice**
    
- ✅ **Rende i test più leggibili e manutenibili**
    
- ✅ **Facilita l’identificazione dei casi specifici che passano o falliscono**
    

> [!NOTE] Nota:
> Per utilizzare `@pytest.mark.parametrize`, è necessario **importare il modulo `pytest`**.

Ma cosa fa `@pytest.mark.parametrize`?
Esegue la funzione `test_check_weather` più volte, passando ogni volta una coppia di valori dalla lista fornita.  
Questi valori sono:

- **`temperature`**: il valore di temperatura in ingresso (input)
    
- **`expected`**: il valore di output atteso (expected output)

QUindi nel file `test_weather.py`:
```python
from my_project.weather import check_weather
import pytest
@pytest.mark.parametrize("temperature, expected", [
	(21.00, "hot"),
	(13.00, "average"),
	(0.00, "cold"),
	(15.00, "cold")
])
def test_check_weather(temperature, expected):
	assert check_weather(temperature) == expected
```

`@pytest.mark.parametrize` esegue la funzione `test_check_weather` **4 volte**:

- La prima volta viene eseguita l’istruzione `assert check_weather(21.00) == "hot"`.
    
- La seconda volta viene eseguita l’istruzione `assert check_weather(13.00) == "average"`.
    
- La terza volta viene eseguita l’istruzione `assert check_weather(00.00) == "cold"`.
    
- La quarta volta viene eseguita l’istruzione `assert check_weather(15.00) == "cold"`.

Quindi l'uotput sarà:
![[Output pytest5.png]]

Pytest esegue 4 test: 3 superano con successo e 1 fallisce, perché la quarta condizione verificata risulta falsa.  
Grazie al decoratore `@pytest.mark.parametrize`, testare la funzione `check_weather()` diventa più **dinamico** e **meno ripetitivo**.

Inoltre si può anche assegnare un **messaggio personalizzato di `AssertionError`** se un test eseguito con `@pytest.mark.parametrize` fallisce.  
Questo aiuta a **comprendere meglio il contesto dell'errore** durante il debug.

```python
from my_project.weather import check_weather
import pytest
@pytest.mark.parametrize("temperature, expected", [
	(21.00, "hot"),
	(13.00, "average"),
	(0.00, "cold"),
	(15.00, "cold")
])
def test_check_weather(temperature, expected):
	ae:str = ""
	if temperature >20:
		ae = "temperatures greater than 20 degree must be considered as hot"
	elif 10 <temperature <=20:
		ae = "temperature within 10 and 20 degree must be considered as averege temperature"
	else:
		ae = "temperatures lower than 10 degree must be considered as cold"
	assert check_weather(temperature) == expected, ae
```

Andiamo a scrivere la classe `Calculatore` in Python nel file `calculator.py`

```python
class Calculator:
	def __init__(self, a:int, b:int):
		self.a = a
		self.b = b
	def addition(self)->int:
		return int(self.a + self.b)
	def subtraction(self) ->int:
		return int(self.a - self.b)
	def multiplication (self)->int:
		return int(self.a * self.b)
	def division(self)->float|None:
		if self.b == 0:
			raise ValueError("Errore")
		return round(self.a/self.b)
```

Ora nel file `test_calculator` scriviamo una serie test per la  classe:
```python
from my_project.calculator import Calculator
def test_addition():
	calculation:Calculator = Calculator (10,5)
	assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction():
	calculation = Calculator(10,5)
	assert calculation.multiplication()== 50, "The multiplication is wrong"

def test_division():
	calculation = Calculator(10,5)
	assert calculation.division()==2.00, "The quotient is wrong"
	
```

L'output sarà:
![[Output pytest6.png]]

4 test eseguiti: 1 fallito e 3 passati
`test_addiction` è fallito.
### Il decoratore `@pytest.fixture`
Probabilmente hai notato che, all'interno di ogni test, abbiamo inizializzato un oggetto della classe `Calculations`, che sarà testato.  
Possiamo evitare questo passaggio utilizzando il decoratore `@pytest.fixture`.

#### Cos'è `@pytest.fixture`

`@pytest.fixture` è un **decoratore** che ti permette di creare **oggetti o risorse riutilizzabili** da utilizzare nei tuoi test.

Invece di creare un oggetto della classe `Calculator` (o simili) in ogni singolo test, questo oggetto viene creato **una sola volta** prima dell’esecuzione dei test, e poi **riutilizzato** in più test.
Serve a **preparare automaticamente** dati, oggetti, connessioni, file, ambienti, ecc. **prima che un test venga eseguito**, aiutandoti ad **evitare ripetizioni di codice**.

#### Quando usare `@pytest.fixture`?

Usalo quando:

- Hai bisogno di un oggetto (ad esempio un’istanza di classe, un dizionario, un file, ecc.) **in più test**
    
- Vuoi **separare** la configurazione/preparazione dalla logica del test
    
- Vuoi scrivere test **più chiari e facili da mantenere**

#### Esempio pratico di `@pytest.fixture`

```python
from my_project.calculator import Calculator
import pytest
@pytest.fixture
def calculation():
	#Crea una nuova istanza della classe Calculator prima di ciascun test.
	return Calculator(10,5)

def test_addition(calculation):
	assert calculation.addition()==13, "The sum is wrong"

def test_subtraction(calculation):
	assert calculation.subtraction()==5, "The subtraction is wrong"

def test_multiplication(calculation):
	assert calculation.multiplication()==50, "The multiplication is wrong"

def test_division(calculation):
	assert calculation.division()==2.00, "The quotient is wrong"
```

L'output sarà:
![[Output pytest7.png]]

Spiegazione:
	4 test eseguiti: 1 fallito e 3 passati
	`test_addiction` è fallito


### Il comando `Pytest`
Per runnare tutti i test in una directory dobbiamo usare il comando `pytest` da terminale.
Questo comando permette:
-  Cerca automaticamente tutti i file che **iniziano con `test`** oppure **terminano con `_test.py`**
    
- Esegue tutte le funzioni che **iniziano con `test_`**
    
- Supporta i test scritti con **pytest**

#### Il comando `pytest -v`
Il comando **`pytest -v`** viene utilizzato per eseguire i test in modalità **"verbosa"** con il framework **Pytest**.  
Ovvero:

- Mostra l’elenco completo dei test eseguiti
    
- Visualizza anche i **parametri**, se si utilizza `@pytest.mark.parametrize`
    
- Per ogni test, mostra:
    
    - Il **nome del file**
        
    - Il **nome della funzione di test**
        
    - Il **risultato**: `FAILED`, `PASSED`, ecc.

Inoltre possiamo specificare un singolo test dentro una cartella e runnarlo usando il comando
```shell
pytest -v my_project/test/test_calculator.py
```

Oppure possiamo fare lo stesso con un singolo test di una funzione dentro un file di test:
```shell
pytest -v my_project/test/test/test_calculator.py::test_addition
```

L'output:
```shell
collected 1 item

my_project/test/test_calculator.py::test_addition FAILED
```


> [!NOTE] Nota
> Nel comando **`pytest`**, i **due due punti** vengono utilizzati per **navigare all'interno di un file Python** e **specificare una particolare funzione di test da eseguire**.


