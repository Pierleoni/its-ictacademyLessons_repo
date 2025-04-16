# Introduzione
L’acronimo CSS sta per Cascading Style Sheets (fogli di stile a cascata) e designa un linguaggio di stile per i documenti web. il termine sta a significare foglio di stile a cascata 
I CSS istruiscono un browser o un altro programma utente su come il documento debba essere presentato all’utente, per esempio definendone i font, i colori, le immagini di sfondo, il layout, il posizionamento delle colonne o di altri elementi
sulla pagina, etc.

## CSS
L’obiettivo dei CSS si può sintetizzare con una nota espressione: separare il contenuto dalla presentazione.
Tutti i browser oggi usati garantiscono il supporto pieno alla specifica CSS 3
Prima di entrare nei dettagli del linguaggio CSS, è necessario soffermarsi su alcuni concetti chiave legati ad HTML. Si tratta di argomenti propedeutici
per una migliore comprensione del meccanismo di funzionamento dei CSS.
Quando CSS fu inventato HTML ha dovuto integrare due attirbuti che sono style e class.

Il foglio CSS ci sono 3 modi 
- inline: dentro il tag
- blocco: sta nella pagina HTML all'interno dell Head dentro il tag Style
La diffreenza tra questi due a livello di pagina se il CSS si torva nell'head la regola può essere applicata a più tag mentre inline a quel singolo tag. 
Per definire le classi customizzate si usa il punto(`.`) 
```css
.paperino{
color: yellow;
}
```
Per richiamare la classe in HTML uso l'attributo `class="nomeClasse"`

- file esterno: al giorno d'oggi si usa l'opzione di usare il file esterno poiché posso riutilizzare il foglio CSS su quanti documenti HTML voglio.
Per richiamarlo uso il tag link nell'head:
```html
<link href="nome.css" rel="stylesheet"  > 
<--!stylesheet nell'attributo rel è uno standard-->
```
in un attributo class posso mettere quante classi customizzate voglio 

```css
.pippo{color:violet;}
.pluto{back-groundcolor:grey;}
```
```html
<div class = "pippo pluto"></div>
```
A cascata vuol dire che mano a mano che si incontrano le regole queste vengo applicate. 
Quindi per librerie o file esterni anche l'ordine dei tag `<link>` è importante

### Gli spazi
QUando si trovano dei tag come h1, div, etc.
ad esempio tra un div colorato di grigio qual'è il bordo? lo spazio tra il bianco è il grigio, la prima cosa da chiederci e se lo spazio lo volgio intenro o esterno
![[Screenshot 2025-04-09 at 15-36-53 Meet - wri-jxki-bxo.png|562x218]]

si usa il padding: regola lo spazio intenro al bordo:
```
.mydiv{padding: 40px; margin: 100px}
```
il margin: regola lo spazio esterno al bordo
il coamdno border: ha bisogno di 3 proprietà; colore, grnadezza e stile
```
.mydiv{padding: 40px; margin: 100px; border: 20px,solid}
```
border-radius: scontorna gli angoli del bordo 
![[Screenshot 2025-04-09 at 15-41-08 Meet - wri-jxki-bxo.png|569x125]]

