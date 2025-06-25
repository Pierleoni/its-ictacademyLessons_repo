from abc import ABC
class Persona(ABC):
	_nome:str
	@abstractmethod
	def __init__(self,nome)->None:
		if len(nome)<2:
			raise ValueError("Il nome deve avere almeno due caratteri")
		self.nome = nome.capitalize
	
	def saluta(self,nome):
		print(f"Ciao {nome}")

class Studente (Persona):
	_matricola:int 

	def __init(self, nome:str, matricola:int)->None:
		super().__init__(nome)
		self._matricola = matricola 
	# Benchè l'init di Persona sia astratto lo si poù invocare nelle sue sottoclassi quindi se si fa:

mario:Persona = Studente("Mario", 1234) #Viene invocato ("Mario") viene invocato Object

print(type(mario))
print(isinstance(mario,Persona))

print(Studente.mro()) #mro() fa vedere, a partire da una classe fa vedere la catena di ereditarietà della classe 
