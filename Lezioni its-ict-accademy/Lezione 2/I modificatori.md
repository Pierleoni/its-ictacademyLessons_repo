# Modificare i dati
Editor online di [[Introduzione a Python#|python]], [clicca qui](https://www.online-python.com/) 
per usare una [[Introduzione a Python#Strings|stringa]]:  
```python 
name:str = "marco"
age:int = "29"
```
Per stampare un messaggio si può fare in 2 modi 
1. concatenazione di stringhe: 
```python
Print ("ciao io sono " + name + "!Ho" + age + "anni")
```
E mi da un errore alla linea 5 perché posso cocatenare valori di stringhe non numeri e a python non piace, quindi uso: 
```python
   Print ("ciao io sono " + name + "!Ho" + str(age) + "anni")
```
Python definisce automaticamente definisce la variabile age e la variabile age come intero e la variabile name come stringa, in alcuni linguaggi di programmazione ciò non si può fare perché devi definire di che tipo è la variabile. 
Se io cambio nome alla variabile name me lo stampa comunque in output.
Voglio stampare in output che tipo di valore è associato alla variabile age
```python
 print(type(age))
 print (type(str(age)))
 print(type(age))
```
verrà fuori che age è un intero perché cosi facendo non ho sovrascritto il valore di age, diverso è se avessi fatto questo 
```python
age=str(age)
print(type(age))
```
In questo modo ho sovrascritto il valore di age come stringa e quindi l'output me lo farà visualizzare
![[Recording 20241217120107.webm]]
 come tale. 
QUESTO È IL PRIMO MODO. 
Tuttavia questo modo porta a fare un sacco di errori, perciò si ha la possibilità di formattare l'output
```python
#output formattato
print(f"Ciao! Io sono {name}! Ho {age} anni")
```
Se mando in output ottengo lo stesso risultato:
la `f` serve per formattare l'output in questo modo (se non si mette la f all'inizio python darà errore), tra le parentesi graffe renderizza il valore name e age in output e lo stampa in output.
Se io analogalmente cambio il valore di age o name cambia i  valori in output.

---
## Numeri in virgola mobile
Scrivo il numero di pi greco
```python
pi:float = 3.14159265359
print(f"Pi Greco vale: {pi}")
```
Ottengo il valore di pi greco e se ho scritto tutte le cifre deciamli dopo la virgola me li stampa anche quelli.
```python
#scriviamo pi greco con 2 cifre decimali
print(f"Pi Greco vale:{pi:.2f}")
```
Questo serve per trimmare i numeri dopo la virgola se sono troppi
```python
#Pi greco con 3 n. dec.
print(f"Pi Greco vale: {pi:.3f}")
```
Consideriamo le prime 4 cifre deciamli del pi greco:
prendiamo il primo caso 3.14 questo significa che dopo il 4 c'è l'1 allora arrotodna per difetto (si arrotonda per difetto se tutti i nuemri che seguono l'ultimo numero vanno da 1 a 4).
Nel secondo caso 3.142 il pi greco è arrotondanto per eccesso perché il numero dopo l 1 è il 5 (si arrontodna per eccesso se tutti i numeri che seguono dopo l'ultimo numero vanno da 5 a 9).


---

## I caratteri di Escape 

Sono caratteri particolari, vengono usati quando si lavora con le stringhe.
Mettiamo che voglio stampare in output una stringa `Ciao! io sono Marco
`ho 27 anni`
```python
#Output carratteri di escape
print(f"Ciao! Io sono {name}\nHo {age} anni!")
```
`\n` sta per new line perché consente di stampare l'output accapo, quindi su una nuova riga(new line). 

Inserire le `""` nel output

```python
print("sei \"bellissimo!\"")
```

Immagiano di avere la necessità di salvare un path sul pc
```python
print("C:Documents\\Folder01\\img01.png")
```
Il doppio slash serve per generare lo slash singolo. 
Su alcuni editor funziona su alcuni editor anche un solo slash in questo caso ma in altri no.

```python
print("Ciao\t blablablablabla")
```

![[Recording 20241217113337.webm]]

---




