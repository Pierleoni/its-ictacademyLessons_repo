# Introduzione

In [[Introduzione a Python|Python]], gli **errori** che si verificano durante l'esecuzione del programma sono chiamati **eccezioni**. Se non gestite, possono causare l'interruzione del programma.
Per gestire gli errori si usa il blocco `try - except`. 
## Struttura base del `try - except`
La struttura per usare questo particolare blocco è: 
1. Nel blocco `try`:  
   ==ci si mette il codice che può generare un'eccezione.== 
2. mentre nell'`except`: 
   ==si mette il codice eseguito se si verifica l'eccezione.==
```python
try:
    # Codice che potrebbe generare un'eccezione
except NomeEccezione:
    # Codice eseguito se si verifica l'eccezione

```

**Esempio:**
```python
try:
    linux_interaction()
except RuntimeError as error:
    print(error)
```

> [!NOTE] **Il try ed except è un blocco di codice all'interno del nostro programma e viene scritto quando si è consapevoli che quel particolare tipo di blocco di codice causerà degli errori o eccezioni**
> 
### Keyword aggiuntive
A parte il `try` e l' `except` , in Python vi sono altre keyword. 
- `else`: 
 ==in questo blocco il codice viene eseguito **solo se non si verifica nessuna eccezione**.== 

Esempio:
```python
try:
	linux_interaction()
except RuntimeError as error:
	print(error)
else:
	print("Doing even more Linux things")
```



2. `finally`: ==viene eseguito **sempre**, sia se si verifica un’eccezione che no. Utile per chiudere file, liberare risorse, ripristinare variabili.==
Esempio:
```python
try:
	linux_interaction()
except RuntimeError as error:
	print(error)
else:
	try:
		with open("file.log") as file:
		read_data = file.read()
	except FileNotFoundError as fnf_error:
		print(fnf_error)
finally:
	print("Cleaning up, irrespective of any exceptions")
```
#### `BasicException` e gerarchia delle eccezioni
In Python esistono molte eccezioni([Qui per avere la lista completa](https://docs.python.org/3/library/exceptions.html)), quelle più usate sono
1. `BasicException`: 
   ==è la classe madre di tutte le eccezioni di Python.== 
2. `except Exception`: 
   ==è  una sottoclasse di `BaseException` e serve per usare eccezioni generiche come `ValueError`, `TypeError`, `FileNotFoundError`, etc.==

> [!faq]- **Differenza tra `Basic Exception` e `except Exception`** 
> 1.`Basic Exception`
>- ==È la **vera classe madre** di _tutte_ le eccezioni in Python.==
  >  
>- È **superclasse anche di eccezioni speciali** come:
  >  
 >   - ==`SystemExit` (quando il programma sta per chiudersi)==
   >     
 >   ==- `KeyboardInterrupt` (quando premi `Ctrl+C`)==
 >       
 >   ==- `GeneratorExit`== 
 >       
>
>2. `Exception`
>
>- ==È una **sottoclasse** di `BaseException`.==
  >  
>- ==È la **classe madre della maggior parte delle eccezioni “normali”**, come `ValueError`, `TypeError`, `FileNotFoundError`, ecc==.
 >   
>- Non include eccezioni “di sistema” come `KeyboardInterrupt`.
>  
>**Perche allora si usa `except Exception`?**
>Perché è più sicuro:
>```python
>except Exception:
>
>```
>Ciò significa:
>**==Gestisco solo gli errori 'normali' del programma, ma lascio passare eccezioni critiche come un `Ctrl+C` o l'uscita del programma.==**
>
>Mentre se uso `except BaseException`:
>```python
>except BaseException:
>```
>Ciò significa:
>**==Catturo qualsiasi cosa, anche un'interruzione da tastiera o un'uscita del sistema.==**
>Ovviamente è molto rischioso perché:
>- Si impedisce la chiusura ordinata del programma 
>- Blocca comandi da tastiera rendendo difficile interrompere manualmente lo script.
> Di conseguenza `BaseException` è utile solo in **casi rari**(es. logging avanzato, cleanup critico, debugger, ecc)



### Creazione di eccezioni personalizzate

Python da la possibilità di creare eccezioni personalizzate: supponiamo di star scrivendo programma e vogliamo creare delle eccezioni custom.
Per fare ciò bisogna creare  una classe che eredità da `Exception`. 
Questo passaggio è molto importante perché:  se non si eredita da `Exception`, Python vedrà quella classe come una classe qualunque, mentre se si eredità da `Exception` quella classe diventa una classe di eccezione.
```python
class PlatformException(Exception):
	"Incompatible platform"
```


### La keyword `raise` 
 Finora abbiamo visto come in Python se si verificano errori viene sollevata un errore ma può essere che in un nostro contesto quello che non è un errore per altri, per noi lo è e quindi torna utile sollevare un errore e per fare ciò si usa la keyword `raise`:
 ==Serve a **sollevare un'eccezione manualmente**.== 
 È utile quando una condizione che _non è tecnicamente un errore_ lo diventa nel tuo contesto specifico. 
```run-python
number=10
if number >5:
	raise Exception (f"The number should not excedd 5. ({number=})")
print(number)
```

Questo ti blocca il programma.


