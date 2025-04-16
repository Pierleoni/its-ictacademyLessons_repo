# Introduzione
Bootstrap è ad oggi il framework html css e js più popolare ed utilizzato al mondo. Bootstrap è un insieme di elementi stilistici grafici e funzionali già pronti per essere utilizzati per ogni applicazione web. Il vantaggio di utilizzare un framework come
Bootstrap è quello di trovare una gran parte del lavoro già fatto e di far risparmiare parecchie ore di lavoro.
Il sito di riferimento legato a Bootstrap è raggiungibile all’indirizzo [getbootstrap](https://getbootstrap.com/)
Troviamo qui la documentazione, i link per il download dell’ultima release ufficiale e il pannello di customizzazione. Sullo stesso dominio è possibile consultare anche il blog ufficiale del framework.
Partendo da questo sito di riferimento possiamo illustrare il primo passo per iniziare a usare Bootstrap: il download del framework. Abbiamo a disposizione due opzioni:
• [[#Versione compilata|La versione compilata]]
• [[#Codice sorgente|Il codice sorgente]]
![[Screenshot 2025-04-16 at 12-10-50 BOOTSTRAP 5 - slide-0.3-Bootstrap-5.pdf.png|478x219]]

### Versione compilata

Il download della versione compilata è da prediligere quando si voglia valutare il framework nel suo complesso, per la realizzazione di prototipi rapidi del sito, ma anche, in fase di sviluppo e produzione, in tutti quei casi in cui si pensa di sfruttare in un progetto l’intera gamma di componenti.
Chiaramente, è la via da scegliere anche quando si intenda lavorare direttamente con i CSS invece che con il linguaggio LESS che è la base del codice sorgente di
Bootstrap.

### Codice sorgente
Scaricando il codice sorgente abbiamo innanzitutto a disposizione i file LESS originali su cui si basa l’intero framework.
Chi lavora con LESS e vuole integrare Bootstrap nel proprio flusso di lavoro sfruttando le potenzialità di questo ambiente e di questo linguaggio sceglierà
naturalmente questa opzione.
Per lo scopo di questo corso, quindi, i file compilati sono assolutamente sufficienti e sono quelli che dobbiamo utilizzare.


1. gestite il contenuto tramite le griglie: nei giorni scorsi abbiamo utilizzato le tabelle per gestire il contenuto, anche se ad oggi le tabelle sono superflue e sono state sostituite dai div 
```html
<table>
	<tr>
		<td>Contentuo</td>
	</tr>
</table>

<div>
	<div>
		<div>Contentuto</div>
	</div>
</div>
```
nel caseo delle tabelle vedo il coentuto sulla stessa riga mentre con i div li vedo in due righe diverse, qui netra in gioco bootstrap perché tramite le classi container, rows and column posso definire quale tag div sosotutuisce il tag table, quale il tag tr e quale il tag td.
```html
<table>
	<tr>
		<td>Contentuo</td>
	</tr>
</table>

<div class = "container">
	<div class = "row">
		<div class = "column">Contentuto</div>
	</div>
</div>
```


```html
<table>
	<tr>
		<td>Contentuo pippo pluto paperino</td>
	</tr>
	<tr>
		<td>contneuto 2</td>
	</tr>
</table>

<div class = "container">
	<div class = "row">
		<div class = "column">Contentuto</div>
	</div>
</div>
```
In questo caso se scrivo altro contenuto nel tag td mi aggiunge spazio nella riga della tabella mentre se scrivessi altro contenuto su bootstrap ciò non accade questo perché implementa le griglie CSS e le rende più semplici.
Quindi il codice è responsive: cioè le regole CSS di bootstrap adatta il contenuto al dispositivo usato e visualizza il contenuto da orrizontale a verticale, ma per attivarlo devo usare le taglie(xl, lg, md, sm)

```html
<table>
	<tr>
		<td>Contentuo pippo pluto paperino</td>
	</tr>
	<tr>
		<td>contneuto 2</td>
	</tr>
</table>

<div class = "container">
	<div class = "row">
		<div class = "col-sm-4">Contentuto</div>
		<div class = "col-sm-8">Contentuto</div>
</div>
<div class = "container">
	<div class = "row">
		<div class = "col-sm-10">Contentuto</div>
		<div class = "col-sm-2">Contentuto</div>
</div>
</div>
```

2. da un codice pronto