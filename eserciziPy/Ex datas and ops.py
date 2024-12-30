# Primo esercizio

x:float = 3.17
y = 1.0/x
product = x*y
print(x, y)
print(product)
sott = x - product
print(sott)



# Secondo esercizio

x:float = -5.70
y = x%20 
print(x)
print(y)


# Terzo Esercizio

a:int=2
b:int=2
c:int=5
somm = a + c + b 
med = somm/3 
print(med) 

# Quarto esercizio 

numero = int(input("Inserisci un numero intero di quattro cifre: 1998"))
cifre = str(numero)
for cifra in cifre:
    print(cifra)
    




# Quinto esercizio
gradiFahrenheit:int= 80
gradiCelsius=5*(gradiFahrenheit-32)/9
print(f"25 gradi Fahrenheit corrispondono a: {round(gradiCelsius, 1)} gradi Celsius")


# Sesto Esercizio
bakeryMenu:dict= {
"Pizza":9.00, 
"pasta": 10.50, 
"zuppa": 7.00, 
"hamburger": 15.50, 
"Cotoletta": 10.00, 
"salmone": 20.20, 
"patatine fritte":5.50, 
"Verdura del giorno": 7.00, 
"Cheesecake": 6.00, 
"Tiramisù": 6.00,
"Focaccia con Nutella": 6.00,
"Coca Cola": 3.50,
"Acqua": 1.50, 
"Vino": 5.00  
}

ordine:dict={
"primo": {"Pizza":9.00},
"secondo": { "Cotoletta": 10.00},
"contorno": { "patatine fritte": 5.50},
"bevanda": {"Acqua":1.50},
"dolce": {"Tiramisù": 6.00}
}

tot = ordine["primo"] ["Pizza"] + ordine["secondo"] ["Cotoletta"] + ordine["contorno"] ["patatine fritte"] + ordine["bevanda"] ["Acqua"] + ordine["dolce"] ["Tiramisù"]
print(f"Il conto totale è: {tot}" )



a:int= 1
b:int=2
c:int=4
d:int=7
f:int=9 
posNum= a+b+c+d
if posNum<=0:
    

