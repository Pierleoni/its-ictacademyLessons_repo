class Person:

#Questo è lo stampino dei biscotti
	def __init__(self, nome, cognome, eta)
	#Questa funzione costruttore ci peremtte di assegnare gli attributi a quella classe ma non solo, quei tre parametri definiscono i parametri per altre classi
	
	#La variabile self permette di specificare l'istanza perchè identifica il primo byte di memoria dove l'istanza si trova. 
	#Self, se lanciamo il debug, nella prima istanza termina con c59d0, nella seconda istanza termina con 7fed0.
		self.nome = nome
		self.cognome = cognome
		self.eta = eta
		
		
#Questi sono i biscotti
persona1:Person = Person("Mario", "Rossi", 30)
persona2:Person = person("Flavio", "Rossi", 31)
persona3:Person = Person("Flavia", "Asti", 29)
persona4:Person = Person("Flavio", "Adducci", 31)

#Per python queste istanze sono uguali perché si trovano su celle di memoria diverse, sono simili perché python ha una zona di memoria riservata quindi stora i dati in zone di memoria contigue, quindi la prima classe si estende per alcuni byte e subiot dopo inizia la classe persona2

#In python possiamo implementare delle funzioni getter e setter. Il getter è colui che ottiene un valore, ad esempio, di una variabile o di un attributo di una classe. 
def get_nome(self):
    return self.none

#Se io una libreria, ciòè l'ho scritta e un altro utente la sta importando devo proteggere gli attributi delle classi che stanno nella libreria. Il get leggi l'attributo

def set_name(self, nome):
    self.nome = nome
    #Set lo modifichi, come rendiamo le classi privati?
''''
2 modi: 
possono essere raggirati, il secondo modo decorator

il primo modo è mettere uno o due undersocre davanti al nome del paraetro della funzione
def  get_nome(self):
    return self.__nome

Mettiamo che per qualche ragione definisco l'attributo 
self.password = "password" 
nella funzione init.
Io posso fare 
def get_password(self):
    raise ValueError("Non puoi modiciare alla password")

def set_password(self, password):
    raise ValueError("Non puoi modificare la password)

Posso dare il Rasie value a determinate classi, mi creo una classe admin

class Admin:
    def __init__(self):
        pass

def get_password(self, tipo:ANY)
    if type(tipo)==Admin:
        return self.password
    raise ValueError("Non puoi accedere alla password")

Mi creo una classe dipendente
class Dipendnete(Persona) #Mi prende in eredità la classe persona
def Dipendente(Persona): 
    def __init__(self, nome, cognome, eta,stipendio):
         super().__init__(nome, cognome,eta)
    self.stipendio=stipendio
    
    def get_stipendio(self):
        return self.stipendio
    
''''
