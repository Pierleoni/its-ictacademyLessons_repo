Supponiamo di stare a una festa di simulare il gioco di Mario Kart, dobbiamo fare 3 giri di una pista e finito il terzo giro ogni giocatore finisce il gioco e viene visualizzata la classifica. 
Vogliamo di raccogliere le posizioni finali: se l'utente inserisce la posizione uno il programma la ritorna in posizione cardinale (`1st`) e cosi via.
Considera l'utente inserisca i numeri 1,2,3 e ci deve stampare i numeri cardinali `1st`, `2nd`, `3rd`, dal 4 in poi si usa il `th` 
```python
n = int(input("Inserire un numero:"))

  

if n == 1:

    print(f"{n}st!")

elif n == 2:

    print(f"{n}nd!")

elif n == 3:

    print(f"{n}rd!")

elif n == 4:

    print(f"{n}th!")

else :

    print(f"{n}th!")
```

Partendo da questo esempio introduciamo i Match Statements: Sono stati valutati tutti i valori possibili di n e per ogni valore veniva stampato il messaggio con la nomencaltura cardinale. QUesto ovviamente diventa complicato quando scriviamo righe e righe di codice, in quiesto caso viene in aiuto il match statement: 
è un metodo che migliora la leggibilità del codice e la compresnione e fa parte della bupna pratica di programmazzione
### Funzionamento Match Statement
Si parte da una variabile con un determinato valore, e si prende questa variabile si fanno vari casi e per ogni caso deve eseguire una determinata istruzione. 
Se nessun case è vero allora si passa al case di default. 
Quindi l'esercizio può essere riscritto così:
```python
n = 1
case 1:
	print(f"{n}st!")
n = 2:
case 2:
	print(f"{n}nd!")
n = 3
case 3:
	print (print(f"{n}rd!")
n = 4 
case 4:
	print(f"{n}th!")
#default case
case : 
	print(f"{n}th!")

```

Questo match statement può essere usato in qualsiasi contensto (match annidati, if, elif, else, while e for loop). 

### Match statements e ORD
Supponiamo di avere: 
```
#http status (if/elif/else version)
http_status = 200
if http_status ==200 or http_status ==201:
	print("success")
elif http_status==400:
	print("Bad Request")
elif http_status==500 OR http_status==501
	print()
```
Tradotto nel Match statements:
```
case 200|201:
	print ("Success")
case 400:
	print("Bad Request")
case 404:
	print("Not Found")
case 500|501:
	print("Server Error")
case_:
	print ("Unknown")
```
Da notare come in questo caso l'OR è tradotto con il simbolo `|`, questo perché nel match statement se scrivo `or` Python mi dà errore. 
### Il match statement e le condizioni
Io posso inserire delle condizioni `if` (non `elif` ed `else`):
Ad esempio 
```python
#insert a number
n = int(input("Insert a number"))
match n:
case n if n>0 and n%2==0: #in questo caso l'if diventa sia: "se il caso n sia maggiore di zero e pari"
	print (f"{n} is positive and even")
case n if n>0 and n%2!=0:
	print(f"{n} is postive and odd)
case n if n<0 and n%2==0:
	print(f"{n} is negative and even")
case n if n<0 and n%2==0:
	print(f"{n} is negative and odd")
case_:
	print("The inserted number is 0")
```

Il match si usa solo quando la variabile assume diverse valori e seguendo questi valori devo far eseguire determinate azioni 

### Match Statement e variabili
Mettiamo si abbiano 2 variabili:
```python
g = "f"
age = 5
match (g,age):
	case (f", 5):
		print("Piccola!")
	case (m", 5):
		print("Piccolo!")
	case (f",10):
		print("Grande")
	case ("m", 10):
		print("Gigante")
	case_:
		print("Kinder Sorpresa!")
```

### Match Statement e liste
Mettiamo che la mia variabile sia una lista:
```python
ingredienti = ["Pomodoro", "mozzarella", "basilico"]
match ingredients:
	case ["pomodoro", "mozzarella", "basilico"]:
		print("Puoi fare una Caprese!")
	case ["pomodoro", "mozzarella", *_]: #il simbolo con l'asterisco e underscore significa che dal quel momento in pii deve considerare tutti gli elementi che vengono dopo
		print("Puoi fare la Pasta al pomodoro")
	case ["Pane", "Prosciutto", "Formaggio"]:
		print("Puoi fare un Panino!")
	case_:
		print("Non saprei cosa consigliare...sperimenta!")
```

### Match statement e dizionari
```python
user = ("nome": "Luca", "ruolo": "admin")
match user: 
case("nome": name, "ruolo": "admin"): #la variabile name serve per definire il fatto che volgio concdntrarmi sul valore della chiave ruolo perchè non voglio porre l'attenzione sulla chiave nome. 
	print(f"Benvenuto amministratore {name}")
case ("nome": name, "ruolo": "utente")
	print(f"Bwenvenuto utente {name}")
case _:
	print ("Ruolo non riconosciuto")
```
in questo caso devo usare la variabile `name` perché voglio concentrami sulla variabile ruolo, tuttavia non posso usare questa sintassi:
```python
user = ["nome": "Luca", "ruolo": "admin"]
match user:
	case ("nome": name["Luca"], "ruolo": "admin"): #questo è sbagliato
		print("Admin")
	case ("nome": name, "ruolo": "admin"): #Questo è giusto
		print("admin")
```

### Match statement e tuple
```python
point = (3,5)
match point:
	case (0,0):
		print("Origine")
	case(x, 0):
		print(f"Punto sull'asse x: ((x), 0)")
	case (0, y):
		print(f"Punto sull'asse y: (0,(y)")
	case _:
		print(f"Punto generico: (point)")	
```


