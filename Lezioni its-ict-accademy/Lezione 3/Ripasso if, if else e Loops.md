Nei diagrammi a blocchi la condizione veniva scritta con un rombo dal quale partivano due rami:
1. Un ramo true 
2. Un ramo false
Da d'ora in poi vengono definite nelle istruzioni if, if else, else
```python
n:int= int(input("Digitare un numero:")) #La funzione int ti converte tutto quello che si trova nell'argomento come un numero integer
if n ==5:
	print(f"{n} è uguale a 5") #il print è stata indentata perché fa parte del blocco if e quindi viene eseguita se il blocco if risulta vero
else: 
	if n%2==0:
		print(f"{n} non è uguale a 5 ma è pari")
'''
questo blocco di codice posso anche scriverlo cosi:
'''
if n == 5:
	print(f"{n} è uguale a 5")
elif n%2==0:
	print(f"{n} non è uguale a 5 ma è pari")
else: 
	print(f"{n} non è uguale a 5 ma è dispari")
#Quindi prima vado a valutare la mia condizione if se è vera mi printa il primo print, se è falsa vado a valutare la condizione elif; se questa condizione è vera mi esegue le istruzioni previste per questa condizione. 
#Se questa condizione è falsa valuto l'else che va a chiudere lo statement condizionale.
#Al posto dell'elif posso annidare anche diversi if, è la stessa cosa.



```

I cicli ci permettono di ripetere in maniera automatica elle istruzioni che si ripetono, in python abbiamo 2 tipologie:
1. While 
	C'è una condizione che detemrina la riupetizione del ciclo fin tanto che la condizione sia vera, ma posso anche non entrare nel ciclo se la condizione non è stata verificata 
```python
print("While")
#Per lavorare con un while ho bisogno di definire un contatore
i:int=1
while i<=5:
	print("Hello World")
	i=i+1

print("FOR")
for i in range(5): 
	print("Hello World")
```

Da notare come ho utilizzato lo stesso contatore: tuttavia nel while il contatore nasce e cresce nel ciclo mentre con il for invece 

IL while è utile quando non so quante iterazioni devo fare, mentre se so quante iterazioni devo fare utilizzo il ciclo for:
questo ciclo vuole 3 regole 
1. un valore di inizio
2. un valore finale 
3. un'intervallo di valori(range) per incrementare il contatore
	Di fatti la funzione in range mi restituisce in output il numero delle iterazioni che ho messo in arogmento 
```python
for i in range (1,11): #mi stampa in output tutti i valori da 1 a 10 perche mi esclude l'ulitmi numero 
	print(i)

for i in range(1,11,2): #Quest'ultimo valore mi dice quante unita devo implementare il contatore
	print(i)
```

Il ciclo for viene usato per lavorare con le liste: 
mettiamo ho una lista vuota e posso riempirla con un ciclo, o posso aumentare gli elementi della lista o modificarli:
```python
lista:list = [1,2,3,4,5]

#1 modo
print("modo 1")
for i in range(len(lista)): #la funzione len mi restituisce la lunghezza della lista 
	print(lista[i]) #èrendo il valore che assume i e lo uso per accedere alle posizioni degli elementi della lista 

#2 modo
for item in lista:
	print(item)
#In questo caso item diventa un elemento della lista, perche in questo caso vado a chiedere il valore stesso e quindi per ogni elemento della mia lista lo stampo in output 

```

Le istruzioni break e continue:
```python
for i in range(1,11):
	if i%2==0:
		continue #mi interrompe l'iterazione corrente e mi skippa all'iterazione dopo
	print(i)
	#in questo caso mi stampo solo i numeri dispari perché mi skippa l'if 
for i in range(1,11):
	x:int=int(input("digita un numero"))
	if x%2==0
	break #Interrompe il ciclo e ti fa finire il ciclo quindi in questo caso per ogni numero dispari in questo caso il ciclo si interromperà  

print("DAJE")
```


