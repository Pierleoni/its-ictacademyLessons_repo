
1. importare la libreria request da pip
2. Definire il main
```python 
if __name__=="__main__": 
	headers = {
		'Content-type': 'applixation/json'
		'Accept': 'application/json'
	}
```

In caso se dovessimo

3. Esempio di get: 
	- Creare una variaible response 
	- Assegnare q questa variabile `request.get`
		- Dobbiamo avere un url e un headers
```python
response = requests.get (
	url = "https://localhost:5000/libri"
	headers = headers
)
print("Risposta GET:", response.json) #Stampa il json della risposta su terminale
```

4. Esempio di post
	- Siccome post crea una risorsa dentro la richiesta devo creare il payload
```python
payload = {
	"nome": "Mario", 
	"cognome" : "Rossi"
}
response_post = requests.json(
	url = "https://localhost:5000/api/utenti",
	json = payload, 
	headers = headers
)
print("Risposta POST:",response_post.json())
```

Un altro modo con `json.dumps()`
```python

payload = {
	"nome": "Mario", 
	"cognome" : "Rossi"
}
response_post_dumps = requests.json(
	url = "https://localhost:5000/api/utenti", #esempio di endpoint
	data = json.dumps(payload), 
	headers = headers
)
print("Risposta POST:",response_post_dumps.json())
```

Questo metodo da più personalizzazione e da più modalità di controllo sugli headers e altro ancora. E il metodo che si usa per roba avanzata.

Ovviamente prima di avviare questo file devo prima avviare il server: prima si scrive il file con la logica e poi si avvia il server e si runna il file. 


