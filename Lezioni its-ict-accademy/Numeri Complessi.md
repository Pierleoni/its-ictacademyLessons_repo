# Numeri reali e immaginari

In matematica i numeri complessi vengono scritti nella forma :
$$
a + bj
$$
dove: 
- ***a***: 
  è la parte reale (cioè un numero che esiste nella "realtà" come ad esempio 5,7.3,-2, etc.)
- ***bi*** : 
  è la parte immaginaria (dove i è l'unità immaginaria, tale che: $$i^2 = -1$$)

## Cos'è un numero immaginario 
Un **numero immaginario** è un numero che non può essere rappresentato sulla retta dei numeri reali. Viene definito come un numero che, se elevato al quadrato, dà un risultato negativo. Questo è possibile solo se introduciamo una nuova "unità" che rappresenta la radice quadrata di `-1`.

Questa unità è denotata con la lettera **i** (o [[Spiegazione esercizi Lezione 1 Python#^numero-complesso| **j** in Python]]), ed è definita come:

$$
i = √-1 
$$
Perfetto, approfondiamo il concetto di numeri complessi e l'uso della parte immaginaria!
1. Cos'è un numero immaginario?

Un numero immaginario è un numero che non può essere rappresentato sulla retta dei numeri reali. Viene definito come un numero che, se elevato al quadrato, dà un risultato negativo. Questo è possibile solo se introduciamo una nuova "unità" che rappresenta la radice quadrata di -1.

Questa unità è denotata con la lettera i (o j in Python), ed è definita come:
i=−1
i=−1
​
### L'origine dei numeri complessi

Nel contesto storico, i matematici si sono imbattuti in problemi dove non c'erano soluzioni tra i numeri reali. Ad esempio:

- La radice quadrata di un numero negativo non ha senso tra i numeri reali, poiché il quadrato di un numero reale (positivo o negativo) è sempre positivo.
- Per risolvere queste equazioni, si è introdotta l'idea di numeri immaginari, che sono numeri che, elevati al quadrato, danno un risultato negativo.

Ad esempio:
$$x^2=−1  ⟹  x=±i$$


In altre parole: $$i2=−1.$$
### ### Costruzione di numeri complessi

Un **numero complesso** è costituito da una **parte reale** e una **parte immaginaria**. I numeri complessi sono scritti nella forma: $$z=a+bi$$

Dove:

- ***a*** è la **parte reale** del numero complesso.
- ***b*** è il **coefficiente della parte immaginaria**.

In In Python, la parte immaginaria è rappresentata dalla lettera `j`, quindi un numero complesso potrebbe essere:
```python
z = 3 + 4j
```
In questo esempio:
- La parte **reale** è **3**.
- La parte **immaginaria** è **4j**.
I numeri complessi possono essere usati in molte operazioni matematiche, come somma, sottrazione, moltiplicazione, divisione e radici. Ad esempio:

#### Somma:

$$(3+4i)+(1−2i)=(3 + 4i) + (1 - 2i)  = 4 + 2i$$

#### Moltiplicazione:

$$(3+4i)×(1−2i)=(3×1)+(3×−2i)+(4i×1)+(4i×−2i) = 3 - 6i + 4i -8i^2$$
Poiché $$i^2=−1$$, il termine $$−8i^2$$ diventa positivo, quindi:$$=3−6i+4i+8=11−2i$$

In Python, il risultato della moltiplicazione sarebbe:

```python
z1 = 3 + 4j
z2 = 1 - 2j
result = z1 * z2
print(result)  # Output: (11 - 2j)

```

### Spiegazione dell'esempio 
#### 1. Espansione del prodotto

Per moltiplicare i due numeri complessi, dobbiamo applicare la **distribuzione** (simile alla moltiplicazione di polinomi): $$(3+4i)×(1−2i)$$
Distribuiamo ogni termine del primo numero complesso con ogni termine del secondo numero complesso. In altre parole:  $$(3+4i)×(1−2i) =(3×1)+(3×−2i)+(4i×1)+(4i×−2i)$$
#### 2. Calcolare ogni prodotto

Ora calcoliamo ciascun termine separatamente:

- ***3×1=3***(Questo è il prodotto tra le parti reali di entrambi i numeri.)
- ***3×−2i=−6i*** (Questo è il prodotto tra la parte reale del primo numero e la parte immaginaria del secondo numero.)
- ***4i×1=4i*** (Questo è il prodotto tra la parte immaginaria del primo numero e la parte reale del secondo numero.)
- ***4i×−2i=−8i^2*** (Questo è il prodotto tra due parti immaginarie, quindi dobbiamo ricordare che ***i^2=−1***)

Quindi il risultato finora è:$$=3−6i+4i−8i^2$$
### 3. Semplificare

Ora vediamo come semplificare il risultato:

- **Sommiamo i termini immaginari**: $$−6i+4i=−2i$$

- ***Sostituiamo i^2=−1*** nel termine ***−8i^2***:$$−8i2=−8×(−1)=8$$


Ora il risultato diventa:$$3−2i+8$$


### 4. Risultato finale

Infine, sommiamo i termini reali ***3+8***:$$3+8=11$$


Quindi il risultato finale della moltiplicazione è:$$11−2i$$

> [!example] Riepilogo passaggi
> 1. Distribuiamo i termini: $$(3+4i)×(1−2i)=3+(−6i)+4i+(−8i^2)$$
>1. Sommiamo i termini immaginari: $$−6i+4i=−2i$$
>2. Sostituiamo $$i^2=−1$$ diventa $$−8i^2=8$$
>3. Sommiamo i termini reali: $$3+8=11$$
>Il risultato finale è:
>$$11−2i11 - 2i11−2i$$
