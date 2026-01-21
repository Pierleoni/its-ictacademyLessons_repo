## Introduzione: mutua autenticazione, firma digitale e hashing

Nel contesto della sicurezza delle comunicazioni, l’obiettivo principale è consentire a due entità che comunicano di **fidarsi reciprocamente**.  
La **mutua autenticazione** nasce proprio da questa esigenza: **
- Alice e Bob devono potersi verificare a vicenda**, assicurandosi entrambi dell’identità dell’altro prima di scambiare informazioni sensibili.

Per raggiungere questo obiettivo si utilizzano tre concetti fondamentali della crittografia moderna:

- **cifratura asimmetrica**
    
- **firma digitale**
    
- **hashing**
    

Questi meccanismi non sono intercambiabili: 
- ==**ognuno ha uno scopo preciso** e viene applicato in momenti diversi del protocollo.==

Le chiavi usate **non sono intercambiabili**: 
- ogni operazione ha uno scopo preciso.  
Riformulo in modo formale e corretto, mantenendo la tua idea.

## Mutua autenticazione: principio generale
==La **mutua autenticazione** è un meccanismo crittografico attraverso il quale **due entità (Alice e Bob)** si autenticano reciprocamente, dimostrando ciascuna la propria identità all’altra in modo verificabile.==

Questo risultato si ottiene combinando **due strumenti distinti**, ciascuno con un ruolo ben preciso:

- la **cifratura asimmetrica:**
	- ==che garantisce la **confidenzialità** del messaggio;==
    
- la **firma digitale:** 
	- ==che garantisce **autenticazione e integrità**.==
    

È fondamentale comprendere che **cifratura e firma hanno scopi diversi** e vengono applicate **in momenti diversi**, anche se sullo stesso messaggio.

###  Ruolo della firma digitale

==La **firma digitale** è il meccanismo che consente di stabilire con certezza **chi ha inviato un messaggio** e se il contenuto è stato alterato.==

In termini operativi:

- ==il mittente calcola una firma utilizzando **la propria chiave privata**;==
    
- ==il destinatario verifica la firma utilizzando **la chiave pubblica del mittente**.==
    

La firma digitale garantisce tre proprietà fondamentali:

1. **Autenticazione**  
    - ==Chiunque riesca a verificare correttamente la firma sa che il messaggio proviene dal possessore della chiave privata corrispondente.==
    
2. **Integrità**  
    - ==Qualsiasi modifica del messaggio rende la firma non valida.==
    
3. **Non ripudio**  
    - ==Il mittente non può negare di aver firmato il messaggio.==
    

Nel contesto della mutua autenticazione, la firma digitale è lo strumento che permette a ciascuna parte di **dimostrare di possedere la propria chiave privata**.

### Principio fondamentale 

Nella crittografia a chiave pubblica, **cifratura e firma digitale svolgono funzioni diverse e complementari**:

- **Cifratura con la chiave pubblica del destinatario**  
    ==garantisce la **confidenzialità** del messaggio: solo il destinatario, in possesso della corrispondente chiave privata, può leggerlo.==
    
- **Firma con la chiave privata del mittente**  
    ==garantisce **autenticazione e integrità**: chiunque può verificare l’identità del mittente utilizzando la sua chiave pubblica.==
    

Nella **mutua autenticazione** entrambe le operazioni vengono utilizzate, **in due fasi distinte e simmetriche**, una per ciascun partecipante.



### Autenticazione di Alice verso Bob (Alice autentica se stessa verso Bob)
In questa fase Alice dimostra la propria identità a Bob e assicura che il messaggio sia leggibile esclusivamente da lui.
#### Operazioni corrette

1. Alice **prepara** il messaggio `M`
    
2. Alice **firma** il messaggio utilizzando **la propria chiave privata:**
    
    `Firma_Alice = Sign(M, K_priv_Alice)`
    
3. Alice cifra **messaggio e la firma** con **la chiave pubblica di Bob:**
    
    `C = Encrypt(M || Firma_Alice, K_pub_Bob)`
    
4. Alice **invia** il messaggio cifrato a Bob. 
	   Alice → Bob: `C`
    



#### Operazioni eseguite da Bob

1. Bob **decifra** il messaggio utilizzando **la propria chiave privata:**
    
    `M || Firma_Alice = Decrypt(C, K_priv_Bob)`
    
2. Bob **verifica** la firma usando **la chiave pubblica di Alice:**
    
    `Verify(M, Firma_Alice, K_pub_Alice)`
    

A seguito di queste operazioni, Bob ha la certezza che:

- ==il messaggio era destinato esclusivamente a lui;==
    
- ==il contenuto del messaggio è integro;==
    
- ==**il mittente è effettivamente Alice**.==



### Autenticazione di Bob verso Alice (Bob autentica se stesso verso Alice)
Per completare la mutua autenticazione, Bob esegue una procedura analoga nei confronti di Alice.
#### Operazioni corrette

1. Bob **prepara** il messaggio `N`
    
2. Bob **firma** il messaggio **con la propria chiave privata:**
    
    `Firma_Bob = Sign(N, K_priv_Bob)`
    
1. Bob cifra **messaggio e la firma** con **la chiave pubblica di Alice:**
    
    `C = Encrypt(N || Firma_Bob, K_pub_Alice)`
    
2. Bob **invia** il messaggio cifrato ad Alice.
	   Bob → Alice: `C`
    

#### Operazioni eseguite da Alice

1. Alice **decifra** il messaggio utilizzando **la propria chiave privata:**
    
    `N || Firma_Bob = Decrypt(C, K_priv_Alice)`
    
1. Alice **verifica la firma** con **la chiave pubblica di Bob:**
    
    `Verify(N, Firma_Bob, K_pub_Bob)`
    

Al termine, Alice ha la certezza che:

- il messaggio era destinato a lei;
    
- il contenuto è integro;
    
- **il mittente è Bob**.

### Perché si tratta di mutua autenticazione

La procedura descritta realizza una **autenticazione reciproca completa**, in quanto:

- ==Alice dimostra di possedere la propria chiave privata;==
    
- ==Bob dimostra di possedere la propria chiave privata;==
    
- ==entrambe le parti verificano l’identità dell’altra tramite le rispettive chiavi pubbliche (tipicamente certificate);==
    
- ==l’autenticazione avviene **in entrambe le direzioni**.==


> [!failure] **Errore concettuale da evitare (importante per l’esame)**
>  
> 
> ❌ _“Uso la chiave pubblica di Alice per capire chi ha mandato il messaggio”_  
> ✔️ La chiave pubblica **non identifica da sola il mittente**:  
>==serve esclusivamente a **verificare una firma digitale** generata con la corrispondente chiave privata.==
>
>==L’autenticazione deriva **dalla verifica della firma**, non dalla semplice disponibilità della chiave pubblica.==

> [!ticket] **Frase corretta da ricordare**
> ==La cifratura garantisce la confidenzialità del messaggio, la firma digitale garantisce autenticazione e integrità.==  
>==Nella mutua autenticazione vengono utilizzate entrambe in modo complementare.==



---

## Cos’è l’hashing

L’hashing è una funzione crittografica che: 
- ==trasforma un dato di **lunghezza arbitraria** (una stringa di testo, un file, una password, un messaggio) in una **sequenza di bit di lunghezza fissa**, detta **hash** o _digest_.==

Il risultato dell’hashing non rappresenta il dato originale in forma cifrata, ma una sua **impronta digitale**: 
- ==una rappresentazione compatta che identifica in modo affidabile il contenuto di partenza==.

Una proprietà fondamentale dell’hashing è che il processo è **a senso unico**: 
- ==partendo dall’input è semplice calcolare l’hash, ma partendo dall’hash è **praticamente impossibile** ricostruire l’input originale.==


### Effetto delle modifiche sull’hash

Una caratteristica essenziale delle funzioni di hash crittografiche è: 
- ==la **sensibilità alle variazioni dell’input**.== 
Anche una modifica minima produce un risultato completamente diverso.

### Esempio

Input: `"ciao mondo"`  
Hash (SHA-256):
```
7509e5bda0c762d2bac7f90d758b5b2263fa01e9f8c9e3b0b1c4f5e4d5f9a4b3
```


Se si modifica anche una sola lettera:

```vbnet
Input: "Ciao mondo"
Hash: 2e7d2c03a9507ae265ecf5b5356885a53393a2027e76ed92c6f1c6b62a8b4b98
```

Questo comportamento garantisce che **ogni cambiamento nel messaggio venga immediatamente rilevato**, rendendo l’hash uno strumento efficace per il controllo dell’integrità.



### Caratteristiche fondamentali dell’hashing
Una funzione di hash crittografica deve soddisfare alcune proprietà essenziali:
1. **Deterministico**
    - ==A parità di input, l’hash prodotto è sempre lo stesso.==
	    - Stesso input → stesso hash
        
2. **Irreversibile**
    
    - ==Non puoi ricostruire il messaggio originale dall’hash==
        
3. **Resistente alle collisioni**
    
    - ==È estremamente difficile trovare due input diversi che producano lo stesso hash.==
        
4. **Effetto valanga (diffusione)**
    
    - ==Una minima variazione dell’input genera un hash completamente differente.==
        
Queste proprietà rendono l’hashing affidabile come meccanismo di verifica e identificazione dei dati.


## Ambiti di utilizzo dell’hashing
L’hashing è alla base di numerosi meccanismi di sicurezza informatica:
- **Gestione delle password**: 
	- ==Le password non vengono memorizzate in chiaro, ma come hash.==
    
- **Verifica dell’integrità dei dati:** 
	- ==Un hash permette di controllare se un file o un messaggio è stato alterato.==
    
- **Firma digitale**: 
	- ==Non si firma il messaggio intero, ma il suo hash, rendendo l’operazione più efficiente.==
    
- **Blockchain**: 
	- ==Ogni blocco contiene l’hash del blocco precedente, garantendo l’immutabilità della catena.==
    



### Esempio pratico: hashing delle password

Supponiamo una password:
```arduino
"MiaPassword123"
```
    
1. Il sistema calcola l’hash (ad esempio con SHA-256).
    

```
3a6eb0793f7f86e6f3a9a1c5f4e1b2d3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9
```
2. L’hash viene memorizzato, non la password originale.

- Quando l’utente prova a loggarsi:
    
    -  ==la password inserita viene nuovamente sottoposta alla funzione di hash;==
    
	- ==l’hash ottenuto viene confrontato con quello memorizzato.==
        
- Se i due hash coincidono, la password è corretta, **senza che il sistema abbia mai bisogno di conoscere la password in chiaro**.
    



> [!ticket] **Concetto chiave da ricordare**
> L’hash rappresenta una **impronta digitale del messaggio**:  
> è compatto, univoco nella pratica e non reversibile.


### L' hashing applicato alla mutua autenticazione 
#### Idea generale

Nei protocolli di mutua autenticazione non si firma quasi mai il messaggio completo o l’intera sfida, soprattutto quando i dati possono essere lunghi.  
==Si applica invece una funzione di **hash** al messaggio (o alla challenge) e **si firma il risultato dell’hash**.==

Questa scelta ha 3 obiettivi principali:

1. **Efficienza:** ==l’hash ha dimensione fissa e ridotta, quindi la firma è più veloce==
   
    
 2. **Integrità:** 
    ==qualsiasi modifica del messaggio produce un hash diverso==
    
    
 3. Autenticità: 
    ==solo chi possiede la chiave privata può generare una firma valida su quell’hash==
    
In questo modo hashing e firma digitale lavorano insieme per rendere l’autenticazione sicura ed efficiente.

> [!done] In sintesi: vantaggi dell'hashing applicato alla mutua autenticazione
> - Efficienza: ==serve a **ridurre i dati da firmare** → più veloce==
> - Garantisce **integrità** → ==se l’hash cambia, il messaggio è stato manomesso==
> - Garantisce **autenticità** → ==chi firma con la chiave privata ha creato proprio quel messaggio==


### Scenario e chiavi

```scss
ALICE                               BOB
kpriv_A (segreta)                  kpriv_B (segreta)
kpub_A  (pubblica)                 kpub_B  (pubblica)
```

#### Fase 1 – Bob si autentica verso Alice

1.  **Bob invia una sfida (challenge)**
	   - Bob genera un numero casuale, detto **challenge**, che serve a dimostrare la sua identità ed evitare replay attack.
   
```ini
C1 = numero casuale
```

2. **Hash della sfida**
	  -  Bob calcola l’hash della challenge:

```ini
H1 = HASH(C1)
```

==L’hash rappresenta l’impronta digitale della sfida.==

3. **Firma dell’hash:**
	- Bob firma l’hash usando la propria chiave privata:

```ini
Firma_B = SIGN(kpriv_B, H1)
```

Questa firma dimostra che **solo Bob**, in possesso della chiave privata, ha potuto creare quella firma.

4. Bob invia la firma ad Alice
	- Bob invia ad Alice la firma (e la challenge, se non già nota):

```yaml
Bob → Alice: Firma_B
```

5. **Verifica da parte di Alice**
Alice esegue due operazioni:
5.1. Calcola l’hash della challenge ricevuta:

```ini
H1_check = HASH(C1)
```

5.2. Verifica la firma usando la chiave pubblica di Bob:
```scss
VERIFY(kpub_B, Firma_B, H1_check) → OK
```

Se la verifica ha successo, Alice è certa che:

- ==la sfida **non è stata modificata** (integrità)==
    
- ==la firma è stata creata **da Bob** (autenticità)==
    
#### Fase 2 – Alice si autentica verso Bob
La procedura è simmetrica.
 1. **Alice genera sfida C2:**

```ini
C2 = numero casuale
```
 
 2. **Calcola l’hash:**

```ini
H2 = HASH(C2)
```

3. **Firma l’hash con la propria chiave privata:**
   
```ini
Firma_A = SIGN(kpriv_A, H2)
```
4.  Invia la firma (e challenge) a Bob
    
5. Bob verifica con  la chiave pubblica di Alice (`kpub_A`) e l’hash calcolato di C2
Al termine della verifica, Bob sa che **Alice è autentica**.




##### Schema ASCII riassuntivo
```text
Bob:
C1 → HASH → H1
H1 + kpriv_B → Firma_B
Bob → Alice: C1, Firma_B

Alice:
HASH(C1) → H1_check
VERIFY(kpub_B, Firma_B, H1_check) → OK ✅
```

**Lo stesso flusso viene poi eseguito in senso inverso da Alice verso Bob.**


> [!ticket] **Concetto chiave da ricordare**
> ==Nella mutua autenticazione **non si firma il messaggio**, ma **il suo hash**.==  
>==L’hashing garantisce integrità, la firma digitale garantisce autenticazione.==


