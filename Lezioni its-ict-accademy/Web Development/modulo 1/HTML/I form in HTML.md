# Introduzione 
L'HTML mette a disposizione una serie di tag il cui scopo
è quello di creare moduli con caselle di testo, opzioni, bottoni di invio ed altro ancora.
Il termine tecnico che riassume tutti questi elementi è **form:** ==il loro scopo è quello di creare interazione e scambio dati tra gli utenti ed il sito.== 
Più precisamente, attraverso un form HTML è possibile "raccogliere" gli
input degli utenti per poi inviarli ad un qualche sistema di elaborazione (normalmente uno script lato server che vedremo più avanti).
Quindi il **form** manda i dati al server remote o li manda alla pagina stessa dove c'è un codice JS che li lavora.

## Il tag `<form>`
Quindi il **form** sta a metà tra i due mondi del front-end e il back-end. 
Per creare un **form** si usa l'omonimo tag `<form>`:
```html
<form method="" action="" name="">
	
</form>
```
Scopo di questo tag è: 
==di fare da contenitore ad una serie di tag che costituiranno gli specifici controlli del modulo.==

### Attributi del tag `<form>`
I principali attributi del tag `<form>`, sono:
- `method`: 
  Specifica il metodo di invio dei dati ed accetta i valori **get** e **post.**
	- get: modalità di default.
	  se si guarda sulla barra degli indirizzi si vede quello che ho scritto
	- post: se si mandando i dati in post, viaggiano nel corpo della richiesta quindi non si vedono sulla barra degli indirizzi
- `action`: 
  specifica lo script che riceverà, controlla ed elabora i dati.
Questi due si usavano per mandare i dati al server remoto, infatti action individua la risorsa, cioè il programma usato dal server remoto(Java, PHP, etc.).
- `name`: 
  specifica il nome attributo al form, in quanto è possibile inserire in una pagina più form e questo tag serve ad identificarlo.
  Il nome si può aggiungere a qualsiasi tag per dargli un identificativo, ha un valore semantico

## Tag utilizzati per creare moduli HTML

Una volta definito un form mediante l'omonimo tag
sarà necessario "popolarlo" con una serie di tag
annidati al suo interno. Attraverso i singoli tag, infatti, sarà possibile creare i vari elementi per l'interazione con l'utente come, ad esempio, caselle di testo o menu di selezione. Passiamo adesso in rassegna i singoli tag che generano gli elementi dei form HTML.
### Il tag `input`
`input`: genrea la maggior parte degli elementi dei form HTML, a seconda del type specificato. Gli input più utilizzati sono:
- text: è utilizzato è utilizzato per creare caselle di testo in cui l'utente può scrivere del contenuto su "singola linea";
- file - è utilizzato per creare caselle di selezione di file in locale al fine di poterli trasmettere al server remoto. 
-  radio: 
  permette di creare un gruppo di opzioni al cui interno deve essere fatta una scelta (non ammette scelte multiple). se io tocco non seleziona niente o se tocco si attiva un valore
- type numbered: accetta cifre da 0 a 9
- checkbox - permette di creare un gruppo di opzioni al cui
interno devono essere fatta delle scelte (ammette scelte
multiple), variazione sul tema del radio accetta
- button - permette di creare bottoni "neutri" ai quali, cioè, può essere associata un'azione mediante Javascript; 
-  submit - permette di creare bottoni di invio attraverso i quali viene, appunto inviato e processato il form; gemello di submit: genera due pulsanti questo permette di submittare i dati fino al server o all'apllicazione JS della pagina web
-  reset - permette di creare bottoni per il reset del form (in sostanza vengono cancellate le scelte effettuate dall'utente ed il modulo torna al suo stato iniziale). 

### Il tag `<select>`
Crea una casella di riepilogo a scorrimento chiamata in gergo selectbox, anche chiamato menù a tendina, simile al radio posso scegliere da 0 a 1 elementi 

### Il tag `<textarea>`:
Genera un'area di testo in cui è possbile andare a capo e viene utilizzata per permettere di inserire utilizzata per permettere di inserire descrizione, commenti o comunque testi piuttosto lunghi.

Guardiamo l'esempio:
```html
<form method="post" action="esegui.php">
Nome <input type="text" name="nome"><br>
Cognome <input type="text" name="cognome"><br>

Paese<br>
<select name="paese">
<option value="I">Italia</option>
<option value="E">Estero</option>
</select><br>
Sesso<br>
<input type="radio" name="sesso" value="M"> M<br>
<input type="radio" name="sesso" value="F"> F<br>
Hobby<br>
<input type="checkbox" name="hobby" value="S"> Sport<br>
<input type="checkbox" name="hobby" value="L"> Lettura<br>
<input type="checkbox" name="hobby" value="C"> Cinema<br>
<input type="checkbox" name="hobby" value="I"> Internet<br>
Commento <textarea name="commento" rows="5" cols="30"></textarea>
<br><br>
<!-- SUBMIT -->
<input type="submit" name="invia" value="Invia i dati">
</form>
```

l'attributo name ha il valore della nome della variabile che dovrò scrivere su JS. 
L'attributo value fa visualizzare un valore di default nell'Input, mentre nella select il value serve perché l'utente non deve scrivere ma visualizzare un valore di defualt. 
Nel submit il value è il vlaore che comparirà sul pulsante di submit.

### Il tag `<label>`
Si possono usare delle etichette da abbinare alla casella di testo, graficamente è utile per l'internazziolizzazione ovvero se voglio usare una parole in inglese di Uomo posso metterci un'etichetta per prendere questa parola automaticamente da il vocabolario internazionale.