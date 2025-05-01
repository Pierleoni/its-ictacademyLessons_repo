# Introduzione
Linux è un sistema operativo **==[[I fundamentals di un Sistema Operativo#^multi-user-OS|multiutente]](permette di creare più utenti con i propri comando e dati sulla stessa macchina, inoltre più utenti possono usare e accedere la stessa versione della macchina)==** dove differenti utenti possono avere accesso al sistema avendo i propri dati, i propri programmi e impostazioni completamente separate da quelle di altri utenti oltre ad avere la possibilità di accedere alle risorse del sistema simultaneamente.
- L'operazione di autenticazione dell'utente, tramite nome utente (username) e password, che permette l'accesso alle risorse del sistema è detta login.
- Ad ogni username assegnato dall'amministratore del sistema corrisponde uno user-id (UID) assegnato dal sistema.
  Se si ha un nome utente (es: Antonio) quell'utente viene assegnato a un User-ID, quindi viene gestito in base all'user Id e non al nome utente.
Il login può essere eseguito in ambienti diversi, grafici o testuali da locale o da remoto. L’autenticazione verifica che l'utente abbia i requisiti per accedere al sistema o ad un suo servizio e metterlo in condizione di interagire con la macchina.


## Utente root
**L'utente root (superuser, administrator)** : ==è un utente privilegiato==. 
Ad esso sono riservati i compiti di gestione e configurazione della macchina.
L'utente root ha poteri assoluti sul sistema. 
Esso può:
- ==**aggiungere, eliminare e modificare** account degli utenti==
- ==**installare e configurare** servizi==
- ==**aggiungere e modificare** il file system==
- ==**distruggere** tutto con un solo comando== 

### Commandi di root
Per sfruttare il privilegio root esistono **2 comandi base:**
1. **Il comando `su`:**
==Il comando `su` (substitute user) permette di cambiare in una sessione di terminale.== 
Se viene eseguito senza argomento, cambia all'utente root
```bash
su -
```
Dopo aver eseguito questo comando, ti verrà richiesta la password dell'utente root. Una volta inserita correttamente, la tua shell sarà quella dell'utente root

2. **Usare `sudo` :**
==Permette agli utenti autorizzati di eseguire comandi come root senza dover cambiare utente.==
```bash
sudo comand
```

### Gruppi e password
Su Linux, e non solo, gli utenti possono essere messi all'interno di gruppi per gestirli più facilmente
**Gruppi**
• ==Ogni utente può far parte di uno o più gruppi, definiti dall'amministratore del sistema.==
• ==Ogni gruppo è identificato da un group name associato ad un group-id (GID) numerico.==

**Password**
• ==Ogni utente può avere (e in seguito modificare) una propria password.==
• ==La password non viene visualizzata sullo schermo: è personale e non deve essere rivelata==


> [!attention] ATTENZIONE !
>Il sistema operativo Linux distingue tra lettere maiuscole e minuscole e pertanto:
>•username: admin
>•username: Admin
>•username: ADMIN
>NON sono lo stesso utente.
>Come anche i seguenti file:
>•prova.dat PROVA.dat
>•Prova.dat PROVA.DAT
>NON rappresentano lo stesso file.


### Shell
**La shell (conchiglia):** ==è un programma di sistema che agisce da interfaccia tra utente e il sistema operativo==.
E' un interprete che legge ed esegue le istruzioni di comando per:
• ==la creazione e l'avvio di processi.==
• ==per la gestione di I/O, della memoria di massa e della memoria principale==.
• ==per definire le politiche di protezione dei file e della comunicazione di rete==.
Quindi ogni volta che scriviamo un comando viene creato ed eseguita una shell che permette l'esecuzione di quel comando

> [!info]
> Sebbene i sistemi Linux abbiano un’interfaccia utente grafica, la maggior parte dei programmatori e utenti esperti preferisce un’interfaccia a linea di comando, più veloce e potente, facilmente espandibile che permette all’utente di non dover sempre usare il mouse.

Quando la shell viene avviata:
• vi presenta il **prompt:** 
==spesso un simbolo di percentuale o di dollaro, che permette di inserire comandi.==
• ==**interpreta** il comando inserito==
• ==**crea e avvia** il processo per la sua esecuzione==.
La shell è programmabile, cioè permette di definire gli script:
• ==Uno script è un programma in formato testuale che racchiude comandi   fondamentali per l’uso e l’amministrazione di un S.O==.

![[Shell.png]]

#### Tipi di Shell
Esistono vari tipi di shell:
• Bourne shell (sh)
• Korn shell (ksh)
• C shell (csh ed il suo successore tcsh)
• Bourne again shell (bash)
Ci concentreremo su bash, la shell (quasi) standard in ambiente Linux.

## Comandi di linux
I comandi rappresentano una richiesta di esecuzione.
Vanno scritti rispettando maiuscole, minuscole e spazi, altrimenti non verranno riconosciuti, cioè risulteranno “not found”.
### Forma generale di un comando:
```
comando [opzioni] [argomenti]
```

###### Opzioni:
- ==modificano l'azione del comando.==  ^optionComand
-  iniziano (quasi sempre) con un `-`.


###### Argomenti
• ==indicano l'oggetto su cui eseguire il comando.==
In sostanza sono gli input da dare ai comandi


### Comando: `pwd`
Per verificare quale sia la directory corrente, si utilizza il comando `pwd`(**Print Working Directory**). ==Stampa a video su terminale la directory corrente.==
Es:
```bash
$pwd
```

Output:
```
/home/tua_home_directory
```

### Comando: `passwd`
Permetti di cambiare la password dell'utente.
Es: 
```bash
$ passwd
```



Output:
```bash
Changing password for [current user]
Current password: [insert current password]
New password: [insert the new password]
Retype new password: [retype the new password]
Passwd: all authentication tokens updated successfully.
```


### Comando: `man`
==Permette di aprire il manuale (help on line) riguardante un comando specifico==.

Es: 
```bash
$ man passwd
```

> [!abstract] Navigazione del manuale: 
> - `space` (barra spaziatrice): ==va avanti di una pagina==
> - `return` (invio): ==va avanti di una linea==
> - `q`: ==esce dal file==


> [!NOTE] Nota
> Utilizzare `$ sudo mandb` per aggiornare il database dei manuali.

#### `man -k`
==Per ottenere le pagine di un manuale che contengono una determinata parola chiave== si usa il comando `man -k` (dove `k` sta per keyword) seguito dalla parola chiave ricercata

**Es:** 
```bash
$ man -k password
```

Da notare come `-k`, che è [[#^optionComand|l'opzione]] del comando, cambia l'azione del comando.

**Output:**
```
Elenco di tutte le pagine manuale che contengono la parola chiave specificata.
```

### Comando: `whatis`
==Serve per ottenere una breve descrizione dei comandi di sistema== si usa il comando `whatis`.
Es: 
```bash
$ whatis pwd
```

Output:
```bash
pwd (1)    - print name of current/working directory
```


Oltre a questi comandi base visto sopra esistono moltissimi altri tipi di comandi in Linux, che fanno azioni specifiche in base al contesto. 
### Chi sono e chi è collegato
Questa serie di comandi mostrano gli utenti che sono collegati al sistema operativo e lo stanno utilizzando.
#### Il comando `$ whoami`:
==Il comando per conoscere con quale identità si sta operando.==
```bash
$ whoami
```

#### Il comando `$ id`:
==Il comando per visualizzare lo UserID dell’utente corrente.==
```bash
$ id
```

#### Il comando `$ id nome_utente`
==Il comando per visualizzare lo UserID dell’utente specificato==.
```bash
$ id nome_utente
```
#### Il comando `$ who`
==Il comando per visualizzare tutti gli utenti loggati nel sistema==.
```bash
$ who
```
#### Il comando `$ finger -l`
==Serve per visualizzare le informazioni dell'utente corrente.==
```bash
$ finger -l
```

> [!NOTE]
> se il comando non viene trovato è possibile installarlo mediante il comando: `sudo apt install finger`

#### Il comando `$ finger nome_utente`
==Il comando per visualizzare informazioni dell'utente specificato.==
```bash
$ finger nome_utente
```
#### Il comando `$ last`
==Il comando per visualizzare ed elencare gli ultimi utenti connessi.==

```bash
$ last
```
#### Comando: `$ uname`
==Per conoscere il nome del kernel del Sistema Operativo.==
```bash
$ uname
```
#### Il comando `$ uname -a`:
==Per visualizzare tutte le informazioni relative al Sistema Operativo in uso==.

```bash
uname -a
```


### Creazione di un file 
Questa serie di comandi permette di creare, modificare e salvare i file.

#### Il comando `nano`
Il comando nano è un editor di testo a riga di comando semplice e facile da usare disponibile su molti sistemi Unix e Linux.
È particolarmente utile per modificare file di configurazione o creare e modificare file di testo direttamente dal terminale.

Es:
```bash
nano prova.txt
```


> [!abstract] Sequenze di controlli utili
>-  `CTRL+X`:  ==per uscire dall’editor==. 
>- `CTRL + S`: ==per salvare il file==. 
>-   `CTRL+ INVIO`:  ==per confermare il salvataggio del file==.
>-  `CTRL+O`:  ==per salvare il file==. 
>- `CTRL + INVIO`:  ==per confermare il salvataggio del file==.


Il comando nano consente anche di modificare un file di testo esistente.
Es:
```bash
$ nano prova1.txt
```

> [!abstract] Modificare il file di testo:
> -  Usare le frecce direzionali per spostarsi tra le righe.

### Il comando `$ touch`
Il comando `$ touch filename`:
- ==se il file non esiste, crea un file vuoto==.
- ==se il file esiste, aggiorna la data e l'ora dell'ultimo accesso al file==.


> [!example] 
> `$ touch prova2.txt`      - opera su singolo file
> 
>`$ touch prova3.txt prova4.txt prova5.txt`    - opera su file multipli

### Visualizzare il contenuto di un file

Per visualizzare il contenuto di un file leggibile (non binario) si possono utilizzare i seguenti comandi:
- `cat`
  
-  `more`
  
-  `most`
  
-  `tail`
  
-  `head`
  
### Il comando `$ cat`:
==mostra il contenuto del file facendolo scorrere completamente sullo schermo==.

Es: 
```bash
$ cat prova1.txt
$ cat cenerentola.txt
```


> [!info] Completamento automatico:
>È un modo attraverso il quale la shell aiuta l'utente a completare un comando.
>Durante la digitazione di un nome o di un comando, premendo il tasto Tab, si chiede alla shell di provare a completarlo.
>> [!example]
>>```bash
>> $ cat cene[Tab] rentola
>>```
>> 
>> I tasti ↑ ↓ richiamano i comandi usati in precedenza


### Comando: `$ more`
 ==mostra il contenuto del file, una pagina per volta.==

Es: 
```bash
$ more cenerentola.txt
```

> [!abstract] Navigazione:
> - `space (barra spaziatrice)`: va avanti di una pagina
> - `return (invio)`: va avanti di una linea
> - `q`: esce dal file.

### Comandi `$ tail`, `$ head`
- `$ tail`: ==mostra di default **le ultime 10 linee di un file**==.
Es:
```bash
$ tail cenerentola.txt
```

- `$ head`: ==mostra di default **le prime 10 linee di un file**==.
Es: 
```bash
$ head cenerentola.txt
```

> [!hint] Per entrambi i comandi l'opzione `-n` mostra le prime o le ultime n linee di un file.


Esempio:
```bash
$ head -1 cenerentola.txt
```
- mostra la prima linea del file cenerentola

Esempio:
```bash
$ tail -2 cenerentola.txt
```
- mostra le ultime 2 linee del file cenerentola

### Comando `$ clear`
==Il comando `$ clear` consente di «pulire» la console.==
Es: 
```bash
$ clear
```

## Comando `$ ls`

Il comando `ls` (list directory) in Linux: 
==è uno dei comandi più utilizzati per visualizzare il contenuto di directory==. 
==Esso elenca i file e le directory presenti nella directory corrente o in una directory specificata in ordine alfabetico==.

Esempio di sintanssi:
```bash
$ ls [opzioni] [directory] %% mostra file/directory nella directory corrente %%

$ ls home  %% mostra file/directory nella directory %%

$ ls --color=never  %% mostra senza l’uso colori %%
```

#### Comando `ls -l`
==Per ottenere informazioni più dettagliate sui file== bisogna usare l’opzione `-l`
```bash
$ ls -l
```

In Linux esistono anche i file nascosti che iniziano con il carattere `.` :
• file di configurazione che i programmi collocano nelle home-directory degli utenti per memorizzare le impostazioni utente.
Per visualizzare anche i file nascosi bisogna utilizzare l’opzione `-a`


> [!abstract] 
> `$ ls -a` - mostra i file nascosti e non nascosti
> `$ ls -al` - combina le opzioni –a e l’opzione -l

### Lettura dei file nascosti
I comandi sono
```bash
$ cat .profile
```

```bash
$ cat .bash_profile
```

consentono di leggere i file nascosti chiamati `profile` e `bash_history`.

#### Altre opzioni per il comando `ls`
Esistono molte altre opzioni per il comando ls. Per esempio:
`$ ls -lt`: ==mostra un elenco dettagliato dei file secondo la data dell’ultima modifica.==
`$ ls -lS`: ==ordina i file dal più grande al più piccolo==
`$ ls -lr`: ==ordina i file dal più piccolo al più grande==

> [!example] Esempio:
> -  `$ ls -al etc`: ==mostra tutti i file nascosti e non, contenuti nella directory, etc. in modo dettagliato==
> -  `$ ls -alS etc`: ==come sopra ma ordinandoli dal più grande al più piccolo==

### File System information 
Esaminiamo più in dettaglio le informazioni ricevute dal comando `ls –l`:

> [!example] Esempio
> 
> ```bash
> $ ls -l /home/marco-cascio
> ```
> 
> <mark style="background: #FF5582A6;">-</mark>rw- rw-r- - : 1 marco-cascio marco-cascio 11371 giu 25 17:26 prova1
> <mark style="background: #FF5582A6;">d</mark>rwxr-xr-x:  2 marco-cascio marco-cascio 4096 giu 20 13:47 Documents
> <mark style="background: #FF5582A6;">l</mark>rwxrwxrwwx: 1 marco-cascio marco-cascio 19 nov 29 13:22 prova1→/home/renata/prova1

Il primo carattere è:
• `-`: ==se si tratta di un file.==
• `d`: ==se si tratta di un directory.==
• `l`: ==se si tratta di un link simbolico (puntatore)==.

Come possiamo notare dall'immagine sotto i successivi gruppi di tre caratteri rappresentano i permessi attribuiti al file rispettivamente per il proprietario
del file, per il gruppo e per il resto del mondo.

![[File System information.png]]

. Essi possono assumere i valori:
• `r`: ==permesso di lettura==
• `w`: ==permesso di scrittura==
• `x`: ==permesso di esecuzione (per le directory rappresenta il permesso di attraversamento)==
• `-`: ==nessun permesso.==

![[File System information_2.png]]



Per Spiegare meglio questa cosa guardiamo questa immagine:
![[Spiegazione FSI.png]]

- Il <span style="background:#ff4d4f"><mark style="background: #FF5582A6;">primo carattere della prima colonna</mark></span> indica se l’elemento è un file, una directory o un link simbolico.
- I<span style="background:#d4b106"> successivi caratteri della prima colonna</span> indicano i permessi
- la <span style="background:#40a9ff">terza</span> e la <mark style="background: #D2B3FFA6;">quarta</mark> colonna indicano l'<span style="background:#40a9ff">utente</span> e il <mark style="background: #D2B3FFA6;">gruppo proprietario</mark> del file.
- la<font color="#004dff"> 5° colonna </font>rappresenta la dimensione in byte del file
- la 6° e la 7° colonna rappresentano la data e l'ora dell'ultima modifica del file.
- l'ultima colonna è il nome del file

> [!note] in caso di collegamenti simbolici (link simbolico), `→` è la destinazione del collegamento
> 

### Creazione di una directory
Questa serie di comandi servono per creare, cambiare, spostarsi tra le directory.

#### Il comando `mkdir`
==Serve per creare una directory.==

```bash
$ mkdir [nome_nuovo_directory]
```

Il comando crea la directory `nome_nuova_directory` all'interno della directory corrente, ma è possibile specificare il path desiderato.

**Esempio per creare diverse directory:**

```bash
$ mkdir mia  %% crea una directory chiamata mia nella directory corrente %%

$ mkdir new  %% crea una directory chiamata new nella directory corrente %%

$ mkdirtua disney prova  %% crea tre directory chiamate tua, disney e prova nella directory corrente %%
$ mkdirmia/sua  %% crea la directorysua all’interno della directory mia %%
```


### Spostarsi tra le cartelle: Il comando `cd`
==Serve per cambiare directory e muoversi nella gerarchia padre-figlio delle cartelle sul file system.==
```bash
$ cd [nome_directory]
```

La directory specificata diviene la working directory.
Se nessuna directory viene specificata, si ritorna alla home directory.

![[cd comand.png]]

Prendendo ad esempio questa immagine partiamo dalla directory `home`:
1. Se scriviamo
```bash
$ cd mia
```

Verremo mandati dentro la cartella `mia`; nello specifico il path sarà `home/tua_home_directory(o nome_user)/mia`
In aggiunto possiamo usare il comando `$ pwd` per controllare la directory nella quale ci troviamo.
Se volessi discendere ancora la gerarchia genitore-figlio delle directory:
```
$ cd sua
```

Adesso ci troviamo nella directory `sua` contenuta nella directory mia, il path è: 
`home/tua_home_directory/mia/sua`.

Per ritornare direttamente alla `tua_home_directory`:
```
$ cd
```

Questa semplice riga di comando ci riporta alla `tua_home_directory`

### Spostamenti relativi e assoluti 
Prima di continuare a vedere i prossimi comandi bisogna fare una distinzione tra gli spostamenti relativi e assoluti:
- Gli spostamenti o percorsi assoluti: 
  Partono sempre dalla radice (cioè da `/`) e seguono l'intero 'indirizzo' della directory.
  **Es:**
```bash
$ cd /home/tua_home_directory/mia/esercizio2/alfa
```
Il vantaggio di questo percorso è che funziona da qualsiasi posizione nel file system.

- **Spostamenti o percorsi relativi:**
  Partono dalla working directory corrente (dove ti trovi). 
**Es:**
Se ci si trova in `/home/tua_home_directory`
```
$ cd mia/disney
```
Ci si sposta in `/home/tua_home_directory/mia/disney`, allora in questo caso la directory `disney` diventa la working directory. 

Se invece ci si trova in `/usr` e vuoi raggiungere `lib`:
```
$ cd lib 
```

Ci si sposta in `/usr/lib` che diventerà la nostra working directory


> [!done] Quando usare l'uno o l'altro
> |**Tipo**|**Quando usarlo**|**Esempio**|
|---|---|---|
|**Assoluto**|Se devi raggiungere una cartella lontana o vuoi essere sicuro del percorso.|`cd /home/tua_home_directory`|
|**Relativo**|Per spostamenti rapidi tra directory vicine.|`cd mia/disney` (partendo da `tua_home_directory`)|

### Il comando `cd ./nome_directory`
Un altro modo per spostarsi discendo nella gerarchia padre-figlio delle directory è il comando `$ cd ./nome_directory`:

Es:
```
$ cd ./mia/sua
```
 
 Ha lo stesso comportamento del comando
```bash
 $ cd mia/sua
```

L'unica differenza è: lo si usa per una maggiore leggibilità nel codice.
Quando si scrive 
```
$ cd /mia/sua
```
il sistema assume automaticamente che si intenda `./mia/sua`.
Quindi è del tutto consequenziale chiedersi: *Ma allora quando è utile usare questo tipo di comando?*.
1. Script e automazioni:
   Per evitare ambiguità, specialmente in script complessi dove è sempre meglio essere espliciti per migliorare la leggibilità del codice.
```
$ cd ./cartella_importante
```

2. Nomi ambigui: Quando si ha una cartella nominata come un comando di sistema (es: `ls` o `test`)
```
$ cd ./test
```

In questo caso ci si sposta dentro la cartella `test`, anziché eseguire il comando `test`

3. Percorsi con spazi/nomi speciali:
Quando si hanno delle cartelle nominate con caratteri speciali e/o il nome contiene spazi.
```
$ cd "./ mia cartella"
```

Mentre invece è obbligatorio usare il `./` quando si vuole eseguire i file presenti nella directory corrente (senza `./`, il sistema cerca solo nei binari di sistema):
```
./mio_script.sh  # Senza `./` darà errore "comando non trovato"
```
#### Spostamento a ritroso nella directory
Oltre a discendere la gerarchia padre-figlio delle directory, la si può anche risalire andando a ritroso. 
Per fare ciò esiste un comando specifico

##### Il comando `cd ..`
Questo comando permette di spostarsi dalla directory corrente a quella genitore.

Es: 
```
mia-sua $ cd ...
mia $
```

In questo esempio ci trovavamo nella directory `sua`, ma con il comando `cd ..` siamo tornati nella directory genitore `mia`.


> [!info] Directory di Sistema – Percorsi assoluti
>-  `$ cd/`:  directory radice del sistema
> - `$ cd /bin:` contiene i programmi di sopravvivenza per il sistema
>`$ cd /boot`: contiene i dati necessari all’avvio del sistema
>`$ cd /dev`:  contiene i cosiddetti devices
>`$ cd /etc`:  contiene i file di configurazione
>`$ cd /lib`: contiene le librerie, ovvero parti di codice condivise tra i programmi
>`$ cd /mnt`: contiene i mount-point
>`$ cd /proc`: il mount-point del file system proc
>`$ cd /root`: è la home directory dell’amministratore di sistema, utente root
>`$ cd /sbin`: contiene programmi che solitamente richiedono i privilegi di root
>`$ cd /tmp`:  contiene i file temporanei
>`$ cd /var`:  contiene alcuni file in attesa di essere processati, come file di stampa


### Verifica del tipo di file 
Per verificare di che tipo sia un file (eseguibili, dati, directory) si può utilizzare il comando `file`.

Es: 
```bash
$ file prova2.txt #Output: prova2.txt: ASCII text
```


### Permessi sui file espressi in forma di stringa
Ad ogni file o directory in un sistema Linux sono associati permessi in base a tre categorie standard del sistema, che sono:
- possessore del file stesso (u);
- membri del suo gruppo (g) ;
- altri utenti (o);

I permessi vengono suddivisi, all'interno di queste tre categorie, in coppie di tre.
Guardiamo questa immagine per capire meglio:

![[Permessi sui file.png]]

I permessi vengono suddivisi in coppie di tre per ogni categoria, e si suddividono in:
1. **Read(`r`)**: lettura.
   ==Permette di leggere il contenuto dei file e di leggere l'elenco dei file contenuti in una directory.==
2. **Write(`w`):** Scrittura.
   ==Permette di modificare il contenuto di un file, e di aggiungere, rimuovere, rinominare file in una directory.==
3. **Execute(x):** Esecuzione.
   ==Permette di eseguire un file e da la possibilità di attraversare una directory o accedervi tramite nome del percorso.==

Il comando per vedere i permessi associati ad un file è [[#Comando `ls -l`|`ls -l`]] :

```bash
$ ls -l pluto.txt #Output : - rw-rw-r -- 1 marco marco 26 apr 11:30 pluto.txt
```
Questo output -<mark style="background: #E5FF00A6;">rw-</mark> <mark style="background: #00FF02A6;">rw-</mark> <mark style="background: #ABF7F7A6;">r--</mark> sta ad indicare che, questo file ha il permesso di 

- <mark style="background: #E5FF00A6;">**Lettura (r) e scrittura (w)** per l’utente</mark>, il quale non ha il permesso di esecuzione (-)
- <mark style="background: #00FF02A6;">**Lettura (r) e scrittura (w)** per il gruppo di utenti presenti sul sistema</mark>, i quali non hanno il permesso di
esecuzione (-)
-  <mark style="background: #ABF7F7A6;">di sola **lettura (r)** per il resto del mondo</mark>, per cui non è possibile la scrittura (-) e l’esecuzione (-) di tale file.

#### Definire i permessi
Per definire i permessi di un file su Linux bisogna usare il comando `$ chmod`.
La sintassi è:
```
$ chmod [ugoa] [+-=] [rwx] [nome_file]
```

Dove `[ugoa]` sta per: 
- `u`: user(proprietario)
- `g`: gruppo (group)
- `o`: altri utenti(other)
- `a`: tutti (all)
mentre `[+-=]` indica:
- `+`: aggiungi
- `-`: rimuovi
- \=: assegna

Per ultimo `[r w x]` indica:
- `r`: read
- `w`: write
- `e`: execute

### Copiare un file: comando `cp`
Permette di copiare un file. 
La sintassi è:
```bash
$ cp [file da copiare] [file copia] [nome percorso della copia -opzionale]
```
Es: 
```
$ cp prova1.txt pluto3.txt
```
In questo caso crea il file `pluto3.txt` che è una copia del file `prova1.txt`.

###### Con il comando `cp` si può copiare un file in una directory:
```bash
$ cp prova.txt prova3.txt mia 
```

Crea una copia del file `prova.txt`, `prova3.txt` all’interno della directory `mia`. 
```
$ cp *mia/sua
```
In questo caso  copia tutti i file nella directory corrente dentro la directory
`sua`

```
$ cp pl* mia/sua 
```

copia tutti i file il cui nome inizia per pl nella directory `sua`.

###### Inoltre è possibile, con il comando `cp` copiare una directory:
la sintassi è 
```
$ cp -r [dir1] [dir2]
```

Es. se `dir2` non esiste:
```
$ cp -r mia mia2
```
copia solo il contenuto della directory `mia` in una nuova directory `mia2`.

Es. se `dir2` esiste:

```
$ cp -r mia tua
```

copia la directory `mia` e il suo contenuto dentro la directory `tua`. 

![[cp comand.png]]

### Eliminare i file: il comando `rm`
==Questo comando permette di eliminare un file o una directory.==
La sintassi è:
```
$ rm [nome_file] #Per eliminare un file
$ rm -r[nome_directory] #Per eliminare una directory
$ rmdir [nome_directory] #Per eliminare una directory vuota
$ rm -ri [nome_directory] #Per eliminare una directory e i suo contenuto chiedendo le conferme
```

Es: 
```
$ rm prova.txt  #elimina il file prova.txt

$ rm *  #elimina tutti i file nella directory corrente
$ rm pl*  #elimina tutti i file il cui nome inizia per
pl

$ rmdir new  #elimina la directory new (solo se vuota)

$ rm -r mia2 #elimina la directory mia2 con tutto il suo contenuto
```

```
$ rm -ri tua
```

![[rm -ri.png]]


> [!attention] ATTENZIONE!!!!
Da utente privilegiato non eseguire MAI i comandi:
>`$ rm -rf .*` :  cancella tutti i file e le directory nella working directory
>`$ rm -rf /`:  cancellerà tutti i file e le directory nel file system a partire dalla root /
>`$ rm -rf --no-preserve-root /`:  come sopra ma bypassando meccanismi di protezione

