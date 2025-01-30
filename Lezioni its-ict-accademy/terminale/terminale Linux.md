# Comandi Terminale Linux 

`sudo`: permette di loggarci al terminale come amministratori 
per aggiornare gli aggiornamenti:
`alt + t`: apre un altra finestra del terminale 
`nvtop`: se dice `not found`, bisogna scrivere `sudo apt install nvtop`. 
## Apt Install
Il comando `apt install` su Linux è usato per installare pacchetti software sui sistemi basati su Debian, come Ubuntu. Ecco cosa succede quando lo usi:

1. **Ricerca dei pacchetti**:
)
- `apt` verifica nei repository configurati (solitamente indicati in `/etc/apt/sources.list` o in `/etc/apt/sources.list.d/`) se il pacchetto richiesto è disponibile.
2. **Risoluzione delle dipendenze**:

- Controlla se il pacchetto da installare ha dipendenze, ovvero altri pacchetti richiesti per funzionare. Se necessario, li scarica e li installa automaticamente.
3. **Download del pacchetto**:

- Scarica il pacchetto selezionato e le sue dipendenze dai repository configurati.
4. **Installazione**:

- Installa i file del pacchetto sul sistema, configurandoli per essere pronti all'uso. Alcuni pacchetti possono avere script di configurazione che vengono eseguiti automaticamente durante l'installazione.
5. **Aggiornamento dei metadati**:

- Aggiorna il database locale dei pacchetti installati, in modo che il sistema sappia quali pacchetti sono stati aggiunti.

### Esempio

```bash
bashsudo apt install nome_pacchetto
```

Ad esempio:

Installa l'editor di testo `vim`.

### Differenze con altri comandi correlati

- **`apt update`**: Aggiorna l'elenco dei pacchetti disponibili dai repository.
- **`apt upgrade`**: Aggiorna i pacchetti installati alla versione più recente disponibile.
- **`apt remove`**: Rimuove un pacchetto, ma può lasciare file di configurazione.
- **`apt autoremove`**: Rimuove automaticamente pacchetti inutilizzati.


`nvidia-smi`: 

per scaricare Vs Code su terminale ubuntu:
```ubuntu
sudo snap install --classic code
```
