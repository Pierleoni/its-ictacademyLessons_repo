# Introduzione 
**HTML** è l'acronimo di **Hyper Text Markup Language,**
non è un linguaggio di programmazione perché non possiede i costrutti logici della programmazione, è solo un linguaggio di Markup per Ipertesti ed è lo standard utilizzato per la creazione di pagine Web.
La finalità è quello di utilizzare un programma che venga renderizzato dalla macchina per poter visualizzare dall'utente, in questo caso è il lato front-end.
## Struttura di un tag HTML


L'idea del file html è di scrivere il file e lo si passa ad un parsing html che lo traduce e ti monta la pagina in base alle indicazione.
In HTML esistono i cosiddetti "tags": permettono di formattare il testo 
```html
<nometag>....contenuto...</nometag>
```
Come possiamo all'interno del tag c'è un contenuto che può essere testo o un altro tag annidato:
ad esempio il tag `<body>` che il tag del corpo della pagina può annidare dentro un infinita di tag. 
Le proprietà di un tag si scrivono in `<nometag>`. 
Il file html ha un estensione `index.html`, e lo si può aprire con il nostro parser (browser).

### Esempio di una struttura principale di una pagina
```HTML
<!DOCTYPE html>
<html>
	<head>
		<title> Mia Prima Pagina</title>
	</head>
	<body>
		<h1>Titolo della mia pagina</h1>
		<p>Questo è il testo descrittivo</p>
	</body>
</html>
```

Per conoscere meglio tutti i tag dell'HTML [guarda il sito di w3schools](https://www.w3schools.com/ "https://www.w3schools.com/")

`<br>`: serve per andare accapo 

### Tag fondamentali 
 Tag ci permettono di assegnare un ruolo e una disposizione ai contenuti delle nostre pagine. 
 Il doctype: Il doctype è (o dovrebbe essere) la prima riga di
codice di un documento HTML e serve per indicare
al browser il tipo di documento di cui si tratta.
Il termine doctype, infatti, è la contrazione
di Document Type Declaration (DTD) e consiste in
una dichiarazione, dello sviluppatore della pagina
web, circa il linguaggio utilizzato, la versione di tale
linguaggio e la lingua.

`<h1>`: Il tag `<h1>` serve ad inserire dei titoli. Se proviamo
ad esempio ad inserire subito dopo il tag body il
seguente tag :
```
<h1> titolo dell’articolo </h1>
```
Possiamo notare che subito dopo la scritta “titolo
dell’articolo”, tutto il contenuto che segue va a
capo. I valori possibili sono h1, h2, h3, h4, h5, h6. Il
suo utilizzo è consigliato perchè molto gradito dai
motori di ricerca in fase di indicizzazione della
pagina.

Esistono 2 tipi di tag
1. Tag Block: i tipo block vanno accapo, o meglio hanno un tag di apertura e uno di chiusura, ad esempio `<p>...</p>`
2. Tag Inline: mentre inline rimango solo su una linea ed hanno solo il tag di apertura e non hanno il tag di chiusura, ad esempio `<br>`
Il tag `<div>`: 
sta per divisore, non ha un vlaore semantico ma più concettuale, è un tag block. Se si usassero paragrafi non contenuti in un div dal punto di vista grafico non cambia nulla ma in realtà il div è utile per fa adattare il contenuto della pagina alla grnadezza della pagina stessa.

il tag `<h1>...</h1>`: contiene l'intestazione della pagina, ci sono fino a 6 livelli che vanno dal più grande(`<h1>`) al più piccolo(`<h6>`).
Il tag `<a>`: definisce un'ancora: possiamo dunque
utilizzarlo sia per creare dei link a documenti o
pagine esterne (attraverso l'attributo href) che
per inserire uno o più collegamenti all'interno
della stessa pagina.
Se proviamo ad inserire un tag `<a>` all’interno
del nostro testo possiamo vedere che il testo
non va a capo in quanto il tag `<a>` è un tag di
tipo inline.
Per poter agganciare qualcosa ci vuole un'attributo:
href = ""

il tag `<img>`: <img>
Un altro tag di tipo inline è il tag <img> che
viene utilizzato per includere immagini all'interno di una pagina web
`<img src=‘’prova.jpg’’>` 
Provare ad inserire un’ immagine all’ interno del
nostro testo inserito in precedenza e vediamo
cosa succede.

il tag `<span>`: Il tag span è un tag di tipo inline generico per il contenuto di frasi, che non ha alcun valore
semantico. Può essere utilizzato per raggruppare
gli elementi per scopi di stile.


## Gli attributi dei tag HTML
Gli attributi HTML sono i parametri dei tag html. Sono utilizzati
per indicare dei valori e modificare la formattazione del
markup.
In genere gli attributi sono codici ( nome dell'attributo )
inseriti all'interno del tag html, sono seguiti dal simbolo
uguale (=) e da un valore tra virgolette che definisce il
parametro.
`<tag attributo="valore">`
Il valore dell'attributo è inserito tra doppie virgolette per
facilitare l'operazione di interpretazione da parte del browser.

Gli attributi permettono di ottenere effetti diversi, ad
esempio l'attributo bgcolor consente di cambiare il colore
dello sfondo, l'attributo color assegna il colore del testo,
l'attributo href assegna un indirizzo URL in un
collegamento ipertestuale, ecc.
Ad esempio, nel seguente codice sorgente ho un testo
compreso in un tag.
`<p>testo da allineare a destra</p>`
Sul browser il testo del paragrafo viene visualizzato a
partire da sinistra, in quanto tutti i browser in occidente
hanno la visualizzazione di default a sinistra.
Ora voglio allineare a destra il testo compreso in un tag.
Per farlo devo soltanto inserire nel tag 
`<p> l'attributo``ALIGN con il valore RIGHT.`
`<p align=‘’right’’>testo da allineare adestra</p>`
L'effetto sullo schermo del browser è il seguente:
<p align = "right">testo da allineare a destra</p>
Tramite l'uso dell'attributo ho modificato la formattazione
del paragrafo e ho forzato la visualizzazione del testo a
partire da destra.


## Elenchi puntati e Numerati
Vediamo quali sono le tre tipologie di elenco disponibili in
HTML :
• Elenchi ordinati
• Elenchi non ordinati
• Elenchi di definizioni
Tutti e tre i tipi di elenchi funzionano nel medesimo
modo: si apre il tag, si elencano i vari elementi della lista
(ciascuno con il proprio tag), si chiude il tag dell’elenco.

### `<UL>` gli elenchi non ordinati
L’elenco non ordinato è forse il più usato e si
descrive utilizzando il tag `<ul>`. Al suo interno
possiamo inserire gli elementi della lista utilizzando
il tag `<li>`. Ecco un esempio :
```HTML
<ul>
<li>primo elemento</li>
<li>secondo elemento</li>
<li>terzo elemento</li>
</ul>
```

#### Annidare le liste non numerate 
possiamo inserire diversi livelli all’interno delle liste, creando delle strutture
“ad albero”. E’ sufficiente inserire un nuovo elenco all’interno di un elemento
```HTML
<ul>
	<li>primo della 1a lista</li>
	<li>secondo della 1a lista
	<ul>
		<li>primo della 2a lista</li>
		<li>secondo della 2a lista
			<ul>
				<li>primo della 3a lista</li>
			</ul>
		</li>
		<li>terzo della 2a lista</li>
	</ul>
	</li>
</ul>
```

### `<OL>` gli elenchi ordinati
Gli elenchi ordinati sono contraddistinti dall’
enumerazione degli elementi che compongono la lista. Il
tag da utilizzare per aprire un elenco ordinato è `<ol>` e
anche in questo caso gli elementi sono individuati dal
tag `<li>` :
```html
<ol>
	<li>primo elemento</li>
	<li>secondo elemento</li>
	<li>terzo elemento</li>
</ol>
```


### Tabelle 
Per definire una tabella possiamo riprodurre un esempio simile al seguente :
```html
<table>
	<tr>
		<td>Colonna 1</td><td>Colonna 2</td>
	</tr>
	<tr>
		<td>Dato 1</td><td>Dato 1</td>
	</tr>
	<tr>
	<td>Dato 2</td><td>Dato 2</td>
	</tr>
	<tr>
		<td>Dato 3</td><td>Dato 3</td>
	</tr>
</table>
```
Renderizzato viene visualizzato così:
<table>
	<tr>
		<td>Colonna 1</td><td>Colonna 2</td>
	</tr>
	<tr>
		<td>Dato 1</td><td>Dato 1</td>
	</tr>
	<tr>
	<td>Dato 2</td><td>Dato 2</td>
	</tr>
	<tr>
		<td>Dato 3</td><td>Dato 3</td>
	</tr>
</table>


Nell’esempio riusciamo a definire una griglia
formata da righe e colonne, il risultato è
piuttosto povero ma ci aiuta a presentare i tag di
base:


| Tag       | Descrizione                                                           |
| --------- | --------------------------------------------------------------------- |
| `<table>` | È il contenitore di tutta la tabella e la definisce                   |
| `<tr>`    | "table row" Contiene una riga della tabella                           |
| `<td>`    | "table data", Una cella che contiene i valori all'interno di una riga |
Questo tipo di tabella era un elemento
predominante nel “vecchio Web” (ed è ancora
presente in quello attuale), perché funzionale
anche alla suddivisione degli spazi, oltre che alla
rappresentazione dei dati.
Con il consolidarsi di pratiche più specifiche per
il markup dei layout, questo utilizzo delle tabelle
è caduto in disuso.

Per scrivere una tabella che fornisca una
rappresentazione più chiara dei dati introduciamo un
template leggermente più ricco:
```html
<table>
	<tr><th>Colonna 1</th><th>Colonna 2</th> </tr>
	<tr><td>Totale 1</td><td>Totale 2</td></tr>
	<tr><td>Dato 1,1</td><td>Dato 1,2</td></tr>
	<tr><td>Dato 2,1</td><td>Dato 2,2</td></tr>
	<tr><td>Dato 3,1</td><td>Dato 3,2</td></tr>
</table>
```

<table>
	<tr><th>Colonna 1</th><th>Colonna 2</th> </tr>
	<tr><td>Totale 1</td><td>Totale 2</td></tr>
	<tr><td>Dato 1,1</td><td>Dato 1,2</td></tr>
	<tr><td>Dato 2,1</td><td>Dato 2,2</td></tr>
	<tr><td>Dato 3,1</td><td>Dato 3,2</td></tr>
</table>

`table header` o `th`:
Indica una cella che contiene un intestazione (ad esempio il titolo di una colonna
o di una riga) e serve a dare una definizione dei dati cui si riferisce.

#### Annidare tabelle in HTML

Posso annidare le tabelle tra loro:

```HTML
<table>
	<tr>
		<th>Campo</th><th>Tabella</th>
	</tr>
	<tr>
			<td>Campo1</td>
		<td>
		<table>
			<tr><th>Campo</th><th>Descrizione</th></tr>
			<tr><td>Campo1</td><td>Descrizione1</td></tr>
		</table>
		</td>
	</tr>
</table>
```

<table>
	<tr>
		<th>Campo</th><th>Tabella</th>
	</tr>
	<tr>
			<td>Campo1</td>
		<td>
		<table>
			<tr><th>Campo</th><th>Descrizione</th></tr>
			<tr><td>Campo1</td><td>Descrizione1</td></tr>
		</table>
		</td>
	</tr>
</table>


Tuttavia le tabelle sono statiche, da quando sono nati i primi smartphone le tabelle in HTML  sono andati in progressivamente in disuso, ma ancora si utilizzano, si usano i div con la stessa logica delle tabelle
```
<table> 
	<tr>
		<td></td>
	</tr>
</table>

<div>
	<div>
		<div></div>
	</div>
</div>
```

### Attributi delle tabelle
dentro il tag table devo mettere border per farmi fare il bordo della tabella, 
hieght non si usa mai perchè l'aletzza della tabella si deve adattare al contenuto della tabella. 
Per quanto riguarda il l'attributo width non usare la misura della percentualema usa i pixel. 
Prima si dice che la tabella deve avere una misura in percentuale cosi ha un riferimento e poi sui td impostare diverse width in percentuale


## Form
L'HTML mette a disposizione una serie di tag il cui scopo
è quello di creare moduli con caselle di testo, opzioni,
bottoni di invio ed altro ancora.
Il termine tecnico che riassume tutti questi elementi è form ed il loro scopo è quello di creare interazione e scambio dati tra gli utenti ed il sito. 
Più precisamente, attraverso un form HTML è possibile "raccogliere" gli
input degli utenti per poi inviarli ad un qualche sistema di elaborazione (normalmente uno script lato server che vedremo più avanti).

### Il tag `<form>`
Per la creazione di un form utilizziamo l'omonimo tag form, come nell'esempio che segue:

```html
<form method="" action="" name="">
...
</form>
```

Scopo di questo tag è di fare da contenitore ad una serie di tag che costituiranno gli specifici controlli del modulo.

I principali attributi del tag form, come visto nell'esempio, sono i seguenti:
• `method` - specifica il metodo di invio dei dati ed
accetta i valori `get` o `post`;
• `action` - specifica lo script che riceverà,
controllerà ed elaborerà i dati.
• `name` - specifica il nome attribuito al form, in
quanto è possibile inserire in una pagina più form
e questo tag serve ad identificarlo.