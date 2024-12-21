print("Hello World") 
#la funzuionw .append aggiunge un elemento alla lista
#le variabili quando si dichiarano su Py deve essere messo il tipo di variabile. Es:
#gli indici partono S E M P R E da 0, questa lista è lunga 5 ad esempio ma l'indice dell'elemento 5 sta all 4 indice
list_1:list =[1,2,3,4,5]
#ho ricihmto la lista gli ho detto di aggiungere un elemento alla fine della lista in questo caso è un integer
list_1.append(6)
print(list_1)
#é possibile sia inserire una str all'intenro di questa lista fatta di integer, ma posso anche inserire liste all'intenro di liste.
#Nel mondo reale le liste possono essere utilizzate per le immagini,che sono delle matrici, perché le liste di liste sono matrici.
matrice:list = [[2,1], [5,3]]
#trmaite questo possiamo rappresentare immangini, perché ogni elemento all'intenro è un pixel: se io ho un immagino 3*3:
img:list = [[0,1,1], [1,0,0],[0,0,0]]
#print(img)
#Ovviamente non stampa l'immagine perche i valori devono esseere intrepreptati ma possiamo immaginare dove c'è lo zeor\
    # è in bianco e 1 è nero, ma ad esemèpio in un immaggine di una scala di grigi questi numeri sono tutti float
img_2:list = [[0.0,1.0,1.0], [1.0, 0.5, 0.2], [0.1, 0.12, 0.3 ]]
#in questo caso sto cercando di inserire un immagine colorata le sottoliste fanno riferiemnto\
    # ai valori RGB che vanno da 0 a 255 per ogni canale
#Calcolare quante combinazioni posso fare con RGB
R:list = [[24, 128, 1.0], [10, 23, 225], [1,0.34]]
G:list = [[33, 27, 233], [5, 22, 245], [1,2,56]]
B:list = [[22, 128,233], [10, 23, 255], [1, 0, 34]]

#Nella lista all'elemento 0 voglio mettere la str "Ciao" che si sovvrascrive 
#B[0] = "Ciao"

#se uso append invece aggiungo l'elemento alla lista 
B[0].append ("Ciao")
print(B[0])

print(len(B))
#La funzione len è una funzione che mi restituisce la lunghezza dell'elemento messo come arogmenento 
img:list = (R, G, B)
print(R, G, B)
#la famiglia si chiama collection di cui fanno parte le liste, i set, i dictionary, tuple
#Voglio sapere quanto elementi sono contentuti nella lista B:
print(len(B[0]))
# Sto chiedendo di restiuire il primo elemento quando facco B di 0, in questo caso gli sto chiedendo di restiuire la lunghezza del primo elemento della lista B

#Nel caso dell'extend: io ho 2 liste a:list = [1,2] e b:list = [3,4]. se io faccio a.append(b) diventa a = [1,2,[3,4]]\
    #io pero posso anche scrivere a = a + b

a:list = [1,2,3]
b:list = [4,5,6]
#print(a+b)


#io posso anche fare cosi:
print(f"funzione extend: {a+b}")

#La funzione append non restiuise nulla, se io scrivo print (a.append(b)) nel terminale mi compare il "none"(cioè "null").
a.append(b)
print(f"funzione Append: {a}")


#append e exented sono funzioni, cosa sono in maniera astratta le funzioni?\
    # \Possiamo immaginarle come una scatola che ha un ingresso e può avere un uscita, in maniera formale si scirvono così f(x).
    #nella funzione append entra b (che può essere qualsiasi cosa) ma in output no restituisce nulla, \
        # quello che fa in specifico la funzione append quando la chiamo .append (notazione py e java) gli dico di usare come ingresso anche a:\
        #prende la lista a e la lista b e appendo all'ultima posizione b. \
    #Anche se scrivo in quel modo non restiuisce nulla ma modifica gli input e l'ordine degli argomenti cambia:\
        # perche a seconda di come metto gli arogmenti mi restituisce o meno in uscita un risultato diverso
    #La funzione + so che tra due liste le concatena: prende in input a,b e restituisce in output a+b.\
    #quindi avviene qualcosa all'intenro ma non lo salva e butta solo fuori il risultato.
    #In python posso creare una funzione che, ad esempio, calcoli l'area di un quadrato: prende un numero all'ingresso e lo eleva al quadrato 
    #Le funzioni servono per risparmiare codice (ad esempio la funzione append può nascondere righe e righe di codice.
    #la f sta per formatting e permette di formattare le stringhe non solo nel print! 
e: str = "Marco"
    
str_1:str = f"funzioni extend: {e}"
    
print(str_1)

#Indicizzazzione delle liste nelle liste: possiamo diciharare una lista 

g:list = [7,8,9]
f:list = [10,11,12]
g.append(f)
print(g)
print(g[3][0])
print(g[3][1:len(g[3])])
#io qui sot chiedendo il terzo indice della macro lista e nella seconda lista e gli sot dicendo di restiuirmi 
#la seconda parentesi posso richiamare l'lelemento dentro la lista nella lista 


h = a 
h= 6
print(a)
print(h)


# in questo caso h diventa la lista e a diventa 6 
# io in questo caso ho diciharato una lista a e poi ho diciharato una variabile h = 6 ma poi gli ho detto che h = a e a=6 in questo caso:\
    # quando gli dico h=a gli dico che h deve puntare alla zona di memoria dove sta la lista di a mentre qui invece gli ho detto che a deve avere il valore di 6 mentre h diventa la lista.
#  se io facessi a[0] = 10 adesso h diventerebbe 10 perche nella lista il primo indice diventa 10,\
    # nel momento che io gli dico h=a punto h nella cella di memoria della ram dove è posta la lista, mentre se modifico "a" punto ad un altra cella di memoria ma non cambio il valore di "h"\+
    # ricordare che in questo caso "h" e "a" sono la stessa cosa 
# se io scrivessi a =lista vado a mettere in memoria in RAM una lista, mentre se scrivessi h=a punto sempre alla stessa cella di memoria,\
    # e se scrivessi anche h=a[:] creo una copia di quella lista in un latra cella di memoria 
h = a
a= 6 

# print(a)
# print(h)


# ci da errore perche h ha il valore di un integer, perché gli integer non possono essere indicizzati in python perché sono numeri e la indicizzazione degli interi, io in questo caso sto dicendo di prendermi il primo elemento di una lista ma\
    # nella seocnda parentesi gli sot chidendo l'indice del primo elemento all'intenro del primo lelemtno stesso che essendo un intero non ha indici. es: 
    # a =[1,2,3, [4,5,6]]. Questo è un problema enorme in python


# a.append(b)
# print(a[3][3])

# SET


# p: set = {"ciao",1,1,1,1,0,0,0, "ciao"}
# p[0]
# print(p)


# I Dizionari 

# m:dict ={"key1":{"key1":"valore1"}}


# diciharazione di un dizionario
m:dict={"key1": 1}
# aggiungere elemento interno
m["key"] = [1,2,3]
m["key2"]= ["CiaoCiao"]

# Estrare un valore dal dizionario 
valore:int=m["key2"]

# print(valore)


# Piccolo trick
# print(f"{valore=}")







#dichiaro una nuova variabile
c:dict ={"i": 1, "j":2, "k" :3}
#sto diciarando una chiave all'intenro di m che ha come valore il dizionario c
m["inner"]= c
m["inner"] ["k"]
m["lista1"] = [1,2,3,4,5,6]
print(m["inner"] ["k"])
print(m)

# esempione
menu:dict={"menu_estivo": {"Pizza": 5.60, "Pasta": 10, "Insalata":5}}
menu["menu_estivo"]["Pasta"]
print(menu)
print(menu["menu_estivo"]["Pasta"])

menu_invernale: dict = {"Pizza":20, "Pasta":15, "Insalata": 10}
menu["menu invernale"] = menu_invernale
print(menu)
# per inserire elelemti nuovi
menu["menu_estivo"]["Bistecca"]=25
menu["menu invernale"]["Bistecca"]=30
# Per eliminare un elemento dal dizionario
# prezzo = menu["menu_estivo"].pop("Pizza")
print(menu)
# print(f"{prezzo=}")
# Sovvrascrivere un valore 
menu["menu_estivo"]["Pizza"] = 150
menu["menu invernale"]["Pasta"] = 42



# LE TUPLE
my_tuple:tuple = (1,2,3,4,5,6) 



