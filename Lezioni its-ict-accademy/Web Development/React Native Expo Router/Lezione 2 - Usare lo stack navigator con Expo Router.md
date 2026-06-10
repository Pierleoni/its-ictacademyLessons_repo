
### Usare lo Stack Navigator con Expo Router

Nelle sezioni precedenti abbiamo costruito le fondamenta: 
sappiamo come strutturare le route con file e cartelle, come i layout si annidano e si eseguono dall'esterno verso l'interno, come `<Link>` e `useRouter()` permettono di navigare tra le schermate, e come lo `<Stack />` mantiene la pila delle schermate visitate.

Tuttavia fino ad ora abbiamo usato lo `<Stack />` in modo minimale — lo abbiamo dichiarato nel root layout e lasciato fare il suo lavoro in modo automatico. Nella pratica, lo Stack navigator è molto più potente e configurabile di così.

In questa lezione lo esploriamo in profondità. Partiremo dalla navigazione di base per poi affrontare scenari più complessi:

- **Navigazione in uno stack** — come funziona la pila nel dettaglio e come controllarla
- **Ritorno a una schermata già esistente** — cosa succede quando la schermata di destinazione è già presente nello stack
- **Sostituzione della schermata corrente** — quando e come usare `replace` in modo consapevole
- **Opzioni di navigazione** — come configurare le transizioni e il comportamento dello stack
- **Passaggio di parametri tra le schermate** — come mandare dati da una schermata all'altra durante la navigazione
- **Percorsi dinamici** — come creare route parametriche che si adattano ai dati, come `/products/[id]`
- **Percorsi dinamici annidati** — come gestire route dinamiche a più livelli di profondità
- **Opzioni di schermata** — come personalizzare header, titolo e stile di ogni singola schermata