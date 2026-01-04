# Introduzione: dal “come funziona” al “dove lo metto”

Nei capitoli precedenti abbiamo visto **cosa rende possibile il cloud** ([[Lezione 1 - Introduzione al Cloud Computing#La Virtualizzazione il DNA del Cloud Computing|virtualizzazione]] e [[Lezione 1 - Introduzione al Cloud Computing#1. Astrazione dell’Hardware|astrazione]]), **quali benefici offre** (scalabilità, flessibilità, gestione semplificata) e **perché cambia il modo di progettare le applicazioni web**.

A questo punto la domanda naturale non è più _se_ usare il cloud, ==ma **come e dove utilizzarlo**.==

Un’azienda, infatti, non deve solo scegliere _quante_ risorse usare o _come_ scalarle, ma anche:

- ==**dove risiedono fisicamente i dati**;==
    
- ==**chi gestisce l’infrastruttura**;==
    
- ==**quanto controllo e quanta responsabilità mantenere**.==
    

Queste scelte definiscono il **modello di deployment del cloud**, ovvero il modo in cui le risorse cloud vengono distribuite e gestite.

## Un’analogia intuitiva: organizzare una festa 

Per comprendere i modelli di deployment, utilizziamo un’analogia concreta.

Immagina di dover organizzare una festa:

1. **A casa tua**  
    Devi comprare tutto, cucinare, pulire prima e dopo.  
    → **Cloud Privato**
    
2. **Affittare una sala**  
    Paghi solo per la serata e qualcun altro gestisce pulizie e logistica.  
    → **Cloud Pubblico**
    
3. **Usare entrambe le soluzioni**  
    Antipasti a casa, cena nella sala.  
    → **Cloud Ibrido**
    
4. **Affittare più sale contemporaneamente**  
    Una per il pranzo, una per la cena, magari da gestori diversi.  
    → **Multi-Cloud**
    

Allo stesso modo, nel cloud un’azienda può decidere **come combinare risorse proprie e risorse esterne**, in base a costi, sicurezza, flessibilità e vincoli normativi.


### Cloud Pubblico

Nel **cloud pubblico:**
- ==l’azienda **affitta risorse informatiche** (server, storage, database, rete),==
da grandi provider come:

- Amazon Web Services (AWS)
    
- Microsoft Azure
    
- Google Cloud Platform (GCP)
    

==Queste risorse non si trovano fisicamente presso l’azienda, ma all’interno di enormi **data center** gestiti dal provider.==

> **Data center**: 
> - ==grandi strutture industriali con migliaia di server che funzionano 24/7, dotate di alimentazione ridondante, raffreddamento e sistemi di sicurezza avanzati.==


#### Come funziona operativamente

Il flusso tipico è il seguente:

1. accedi alla console web del provider (o usi le [[Lezione 6 - API#API (Application Programming Interface)|API]]);
    
2. scegli il tipo di risorsa (es. una [[Docker#Le macchine virtuali (VM)|macchina virtuale]]);
    
3. configuri potenza, sistema operativo e rete;
    
4. clicchi su “crea”;
    
5. in pochi minuti hai un server virtuale attivo.
    

Il modello di costo è **pay-as-you-go**:

- ==paghi solo per il tempo di utilizzo;==
    
- ==quando la risorsa non serve più, la spegni e smetti di pagare.==
    

È concettualmente simile alla bolletta elettrica: **usi → paghi**.

##### Vantaggi del cloud pubblico

> [!done] **Nessun investimento iniziale**
> - non è necessario acquistare hardware;
 >   
>- non servono decine di migliaia di euro in anticipo;
  >  
>- puoi partire con costi minimi (anche pochi euro al mese).
   > 
>
>Questo abbassa drasticamente la **barriera di ingresso**, soprattutto per startup e piccoli progetti.


> [!done] **Velocità e time-to-market**
> 
>
>- **prima**: ordinare un server fisico richiedeva mesi;
  >  
>- **ora**: un server è disponibile in pochi minuti.
  >  
>
>Questo consente di:
>
>- testare idee rapidamente;
  >  
>- ridurre il time-to-market;
  >  
>- reagire velocemente al mercato.


> [!done] **Scalabilità automatica**
>  
>
>Il cloud pubblico cresce e si riduce insieme al carico:
>
>- pochi utenti → poche risorse;
   > 
>- picchi improvvisi → molte risorse create automaticamente;
   > 
>- fine del picco → risorse eliminate.
  >  
>
>Il tutto avviene senza interventi manuali e senza sprechi strutturali.



> [!done] **Manutenzione delegata**
> Il provider si occupa di:
>
>- sostituzione dell’hardware guasto;
  >  
>- aggiornamenti dell’infrastruttura;
   > 
>- alimentazione e continuità elettrica;
   > 
>- raffreddamento e sicurezza fisica.
   > 
>
>Dal punto di vista dell’azienda, l’infrastruttura **semplicemente funziona**.

##### Svantaggi del cloud pubblico

> [!failure] **Minore controllo sull'hardware**
> - non puoi accedere fisicamente ai server;
  >  
>- non sai su quale macchina fisica gira il tuo carico di lavoro;
   > 
>- devi fidarti del provider.
  >  
>
>Per molte aziende questo non è un problema, ma in alcuni contesti può esserlo.


> [!failure] **Vincoli normativi e legali**
>
>Alcuni settori hanno obblighi specifici:
>
>- dati bancari;
  >  
>- dati sanitari;
  >  
>- dati governativi.
  >  
>
>In certi casi, la legge impone che i dati rimangano:
>
>- in un determinato paese;
  >  
>- o addirittura all’interno di una specifica struttura.


> [!failure] **Costi variabili e imprevedibili**
> 
>
>Il modello pay-as-you-go richiede attenzione:
>
>- una risorsa dimenticata accesa continua a generare costi;
  >  
>- un successo improvviso può aumentare rapidamente la spesa.
  >  
>
>Il cloud pubblico **non è “economico di default”**, ma **economico se gestito correttamente**.

#### Esempio pratico

> **Negozio online di Mario**

- **Giorno 1**:  
    10 visitatori → server minimo → 5 € / mese
    
- **Black Friday**:  
    10.000 visitatori → 50 server per 2 giorni → 300 €
    
- **Gennaio**:  
    traffico normale → si torna a 5 € / mese
    

Se Mario avesse acquistato server fisici per il Black Friday:

- avrebbe speso decine di migliaia di euro;
    
- per la maggior parte dell’anno quei server sarebbero rimasti inutilizzati.
    

Il cloud pubblico trasforma un **rischio economico** in un **costo proporzionale al successo**.