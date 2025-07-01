
sul file `app.js`

```jsx
function App(){
	let saluto = "Ciao"
	const saluti = () => {
		console.log(saluto);
		saluto = "Arrivederci";
		console.log(saluto);
	}
	return {
	<>
		<div className = "App">
			{saluto}
			<div> <button onClick = {salutami} className = "btn bnt-primary"> 
			Saluta
			</button>
		</div>
	</>
	
	}
}
```

Cosi sull'UI ogni volta che clicchiamo su Ciao diventa arrivederci senza renderizzarmi sulla pagine, ma cosi perdo la reattività. Per evitare ciò utilizzeremo gli hook e partiamo dal primo lo `useState`

Per usare lo `useState` dobbiamo importarlo:
```jsx
import {useState} from "react"
```

La sintassi è :
```jsx
let saluto = "Ciao"
const [saluta, setSaluta] = useState(saluto)
const salutami = ()=>{
	console.log(saluto);
	saluto = "arrivederci";
	setSaluta(saluto);
}
```

il primo parametro è una varibiale mentre il secondo elemento è una funzione che serve per modificare  il valore di saluta, rendendolo reattivo cosi ogni volta che clicchimao su Ciao viene renderizzato in arrivederci.
Lo use state restiuisce un array con due valori, tramite la destrutturazione restituisce il vlaore della variabile slauta e una funzione che aggiorna il valore di quella variabile ogni volta che l'utnete interagisce con un componente dell'UI.

GLi hook sono funzioni prprietarie della libreria che pemrettono di gestire alcuni apsetti fondamentali tra utente e codice. Ad esempio lo useState pemrette di tenere traccia.


### Use effect 
è un hook che è responsabile di gestire tutte le azuoni che avvengono al di fuori del componente.
Esempio:
```jsx
const EsempioUseEffect = () => {
	const [count, setCount] = useState(0);
	useEffect(() => {
		console.log("Sto usando Effect")
	})
	console.log("Fuori dallo use effect")
	const increments = ()=>{
	setCount((currentValue) => {
		return currentValue +1
	)}
	
	}
	return (
		<div>EsempioUseEffect</div>
	)
} 
export defualt EsempioUseEffect
```








