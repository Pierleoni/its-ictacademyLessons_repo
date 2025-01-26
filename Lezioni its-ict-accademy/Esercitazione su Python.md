[[Introduzione a Python#Variabili|Variabili]]

```python
num:int = 10
num2:float = 3.14
string:str = 'Brumotti'
string2:str = 'infame'
sum = num + num2 
string_sum = string + string2 
print(f"se 10 + 3.14 fa {sum}, → {string_sum}")
```

### Funzione di [[Introduzione a Python#^typeFun-def|type]] 
```python
num:int = 10 
num2:float = 3.14 
string:str = 'Brumotti' 
string2:str = 'infame'
sum = num + num2 
string_sum = string + string2
tipo = type(sum)
tipo1 = type(string_sum)
print(tipo, tipo1)
```
---


# [[Gli Operatori]] 
### [[Gli Operatori#Gli operatori aritmetici|Gli operatori aritmetici]] 

```python
a = 10 
b = 39 
c = 5 
d = 9 

sum = a + b
sott = d - c 
div = b/d 
molt = a * c 
floor = 10//5
perc = a%c 
pot = a**c 
print(f"Somma:{sum}")
print(f"Sottrazione:{sott}")
print(f"Divisione:{div}")
print(f"Moltiplicazione: {molt}")
print(f"Floor Division: {floor}")
print(f"Percentuale: {perc}")
print(f"Potenza: {pot}")
```

### [[Gli Operatori#Lista operatori di confronto|Operatori di Confronto]] 

```python
a = 10 
b = 39 
c = 5 
d = 9 
e = 9
f = 33

print(f"{a} è uguale a {b}? {a==b}")
print(f"{c} è diverso da {d}? {c!=d}")
print(f" {b} è maggiore di {c}? {b>c}")
print(f"{d} è minore di {b}? {d<b}")
print(f"{d} è minore o uguale a {e}? {d<=e}")
print(f"{b} è maggiore o uguale a {f}? {b>=f}")
print(f"{d} è uguale a {e}? {d==e}")
print(f"{e} è diverso da {d}? {e!=d}")
print(f"{c} è maggiore di {f}? {c>f}")
```

### [[Gli Operatori#Gli operatori logici|Gli Operatori Logici]]

```python
bln = True
bln2= False
bln3 = True 
bln4= False

print(f"con l'operatore AND se il primo operatore è: {bln}, mentre il secondo operatore è {bln3}: ergo → {bln and bln3}")

print(f"con l'operatore OR, se il primo operatore è {bln3}, e il secondo operatore è {bln4}: ergo →  {bln3 or bln4}")
print(f"con l'operatore OR, se il primo operatore è {bln2}, e il secondo operatore è {bln4}: ergo → {bln2 or bln4}")

print(f"Con l'operatore NOT se l'operatore è {bln}, allora viene valutata come {not bln} ")
print(f"Con l'operatore NOT se l'operatore è {bln2}, allora viene valutata come {not bln2} ")
```


### [[Gli Operatori#Gli operatori di assegnazione|Gli operatori di assegnazione]] 
```python
string = "Con l'operatore"
a = 10 
b = 39 
c = 5 
d = 9 
e = 43
f = 33
g = 20
h= 6
i = 3
l= 2

i+=c
b-=d 
c*=d
e/=d
g//=a
f%=e
l**=h
print(f"{string} = allora 'a' punta a {a}" )
print(f"{string} += incremento il valore della variabile: equiparabile al segno '+'. \nEs: {i}" )
print(f"{string} -= decremento il valore della vairiabile: equiparabile al segno '-'. \nEs:{b}")
print(f"{string} *= moltiplico il valore della variabile: equiparabile al segno '*'. \nEs:{c}")
print(f"{string} /= divido il valore della variabile: equiparabile al segno '/'. \nEs: {e}")
print(f"{string} //== divide i numeri e restituisce solo la parte intera (integer).: equiparabile al segno '//'. \nEs: {g}")
print(f"{string} %= restituisce il resto della divisione: equiparabile al segno '%'. \nEs: {f}")
print(f"{string} **= calcola la potenza di un numero elevato al secondo numero posto a destra: equiparabile al segno '**'. \nEs:{l}")
```
---

## [[Collections]]

### [[Collections#Le liste|Liste]]
```python
my_list = [1, "formaggio",2,"ciao", 55]
my_list2 = [66, 70, 99]
my_list3 = ["AO", 9, 7, 10]
my_list4=[88, 'A', "B", 50]
print(my_list)
print(my_list2)
print(my_list3)
print(*my_list4)
print(my_list[0])
my_list3[2]= "boh"
print(my_list4[-3])
print(my_list3)
```

### L'operatore [[Collections#^inOp|In]] 
```python
spesa_lista:list = ["Ciliega", "Banana", "Pomodori", "Tofu", "Zucchine" ]
if "Zucchine" in spesa_lista:
	print("Check!")
else:
	print("God Damn!")

if "pera" not in spesa_lista:
	print("Dio Bestia!")
else:
	print("Check!")
```

### [[Collections#Le funzioni di una lista|Le Funzioni di una lista]] 
#### [[Collections#**Funzione `.append(element)`**|Funzione .append()]] 
```python
spesa_lista:list = ["Ciliega", "Banana", "Pomodori", "Tofu", "Zucchine" ]
if "Zucchine" in spesa_lista:
	print("Check!")
else:
	print("God Damn!")

if "pera" not in spesa_lista:
	print("Dio Bestia!")
else:
	print("Check!")

spesa_lista.append("pera")
print(spesa_lista)
```

#### [[Collections#**Funzione `.insert`**|Funzione Insert]]
```python
spesa_lista:list = ["Ciliega", "Banana", "Pomodori", "Tofu", "Zucchine" ]
if "Zucchine" in spesa_lista:
	print("Check!")
else:
	print("God Damn!")

if "pera" not in spesa_lista:
	print("Dio Bestia!")
else:
	print("Check!")

spesa_lista.append("pera")
print(spesa_lista)
spesa_lista.insert(6, "Il budello di tu ma'")
print(spesa_lista)
spesa_lista.insert(1, "Cioccolato")
print(spesa_lista)
```

#### [[Collections#funzione `remove`|Funzione .remove()]] 
```python
spesa_lista:list = ["Ciliegia", "Banana", "Pomodori", "Tofu", "Zucchine" ]
if "Zucchine" in spesa_lista:
	print("Check!")
else:
	print("God Damn!")

if "pera" not in spesa_lista:
	print("Dio Bestia!")
else:
	print("Check!")

spesa_lista.remove("Ciliegia")
print(spesa_lista)
```

#### [[Collections#Funzione `pop()`|Funzione .pop()]]
```python
spesa_lista:list = ["Ciliegia", "Banana", "Pomodori", "Tofu", "Zucchine" ] 
if "Zucchine" in spesa_lista: 
	print("Check!") 
else: 
	print("God Damn!") 

if "pera" not in spesa_lista: 
	print("Dio Bestia!") 
else: 
	print("Check!")

spesa_lista.pop(3)
print(spesa_lista)
```

#### [[Collections#Le funzioni di una lista#La funzione `Extend`|Funzione .extend()]] 
```python
spesa_lista:list = ["Ciliegia", "Banana", "Pomodori", "Tofu", "Zucchine" ] 
if "Zucchine" in spesa_lista: 
	print("Check!") 
else: 
	print("God Damn!") 
if "pera" not in spesa_lista: 
	print("Dio Bestia!") 
else: 
	print("Check!")

print(spesa_lista)

spesa_lista.extend(["Dio can de Dio", "Credere, obbedire, penzolare a testa in giù", "California Uber Alles"])
print(spesa_lista)
```

#### [[Collections#Le funzioni di una lista#Funzione `.del`|Funzione .del()]] 
```python
spesa_lista:list = ["Ciliegia", "Banana", "Pomodori", "Tofu", "Zucchine" ] 
if "Zucchine" in spesa_lista: 
	print("Check!") 
else: 
	print("God Damn!") 
if "pera" not in spesa_lista: 
	print("Dio Bestia!") 
else: 
	print("Check!") 

print(spesa_lista)

mlist = [1,2,3,4, "Ciao"]

print(mlist)
mlist.del
print(mlist)
```



## [[Collections#I set|I Set]]
```python
my_set:set ={"Ciao", 1,1,0,0, "Boh","Ciao"}
print(my_set)
print(my_set[1])
```
Per indicizzare un set:
```python
my_set:set ={"Ciao", 1,1,0,0, "Boh","Ciao"}
m_list = list(my_set)
print(m_list)
```

### [[Collections#Funzioni dei set|Funzioni dei set]]

#### [[Collections#Funzioni dei set#1. la funzione `.add()`|Funzione .add()]]
