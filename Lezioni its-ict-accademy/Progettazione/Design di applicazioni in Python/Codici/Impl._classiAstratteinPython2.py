from __future__ import annotations

class Persona:
	def __init__(self, *,
		nome:str, 
		is_studente:bool = False, 
		matricola:int|None = None,
		corso_iscritto:Corso|None
		is_lavoratore:bool = False):

		'''QUando si crea una persona, in questo caso, o gli do solo il nome o anche tutti gli altri attributi, 
		inoltre qui non posso limitarmi a scrivere self.setNome(nome), 
		ma devo assicurami che se una perosna è uno studente o un lavoratore'''
	def diventa_studente(self, matricola:int, corso:Corso)
		if (is_studente != matricola is not  None or  is_studente != corso is not None):
			raise ValueError ("Errore!")

		'''
		Se is_studente è True la matricola non è None e corso non è None, mentre se is_studnete è false corso_iscritto è None
		Questo è vero quando creo la Persona ma se ho detto che tutti gli attributi sono immutabili 
		Come faccio a far diventare una Persona uno studente? Devo mettere questa logica in una funzione diventa_studente.
		Nei metodi set come questo dobbiamo mettere un controllo oppure se  un metodo viola i vincolo detti prima.
		Un altro esempio:
		'''
	def lascia_studi(self):

