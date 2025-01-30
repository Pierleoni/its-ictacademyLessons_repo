# Creare i file e cartelle su VS Code

## Creare i file di .gitignore e README.md


## Creare le cartelle standard
Di cartelle da inserie sul progetto sono tendenzialmente tre:
1. SRC:
   Contiene tutto il codice sorgente che scriviamo nelle nostra applicazione. 
   Dal terminale Ubuntu per listare i file presenti in una cartella usare il comando `ls` e per creare una nuova directory usare il comando `mkdir <nome-cartella>`. 
   Adesso andiamo a creare i 2 file tramite il comando `touch`, i file sono il `.gitignore` e il file `README.md`.
```shell
touch .gitignore
touch README.md
```

All'interno della cartella SRC possono esserci altre sotto-cartelle.
Mi sono sbagliato a scrivere una cartella da terminale per cambiare nome scrivo
```
mv data data1
```
Per eliminare una cartella:
Per copaire un file o una cartella da una parte all'altra 
```
cp README.md
```
Quindi in SRC bisonga mettere tutto il codice sorgente 
2. DATA: bisogna metterci i file che contengono dati come i .csv
3. Configs: Si mettono i file di configurazione, e sono di 2 tipi
   - JSON
   - YAML
Cosa sono le configurazioni, contengono le impostazioni del programma, se scrivo un programma che fa girare un rete neurale e voglio dare la possibilità all'utente di usare o meno la GPU devo scrivere queste informazioni in uno di questi file. 
Manca l'entry point e si chiama main ed è l'entry point del programma, quando verrà lanciato (ci sono diverse scuole di pensiero: generalemente si mette fuori le sottocartelle dentro la cartella SRC). 

> [!faq] Il file gitignore e il file README.md si mettono al di fuori di queste cartelle ma dentro la cartella principale


