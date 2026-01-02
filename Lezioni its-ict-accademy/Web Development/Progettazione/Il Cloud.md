Il cloude è un astrazone di risorse di elaborazione, archiviazione e networking
## Il cloud computing
È un modello di erogazione di risorse informatiche (come server,spazio di archiviazione, database, rete, software,ecc.).
Tramite internet, cioè "dal cloud", invece che in locale su un computer o un server fisico di tua proprietà. 
Immagginiamo: 
vogliamo creare una nostra applicazione e di voler usare un server locale anziche remoto, se faccio delle stime e penso che devo getire, ad esempio, 10000 client ma invece nella mia app se ne scrivono almeno il doppio come faccio a gestire tutto questo traffico di dati? 
In questo caso torna utile usare un servizio cloud

### Le categorie 
1. PAAS: Platform as a Service; Google Run
2. IAAS (Infrascture as a service): AWS, Google Cloud e Azure
3. SAAS(): 
Scalabile: dal momento che vuoi aumentare la potenza "pompi" la cpu, la ram e l'hard disk e si aumenta la potenza della macchina.

Su AWS si puo comprare una macchina lightsaile ci si mette ad esempio il window server e la soceita mette sql server e IIS. 
La IIS restituisce gli endpoint JSON, dobbiamo prendere questi Endpoint e peremttere all'utente di fare loggin, cercare i documenti di fatture e stamparli in pdf.
Quindi faremo un form di ricerca React 

### La virtualizzazione 
La virtualizzazione è letteralmente il motore dhe ha reso possbile l'esistenza del cloud moderno. 
Senza virtualizzazione, non avremo AWS, Google Cloud o Azure come li conosciamo oggi. 
#### Cosa significa virtualizzazione 
La virtualizzazione è la teconologia che peremrette di dividere un singolo computer fisico in molteplici virtuali indipendenti. 
È come avere un palazzo con tanti appartamenti: un solo edifico fiisco, ma ogni inqulino ha la sua casa completamente separata e funzionale 
##### Prima della virtualizzazione: 
1. 1 server fisico = 1 SO = 1 applicazione 
2. Spreco di risorse (server utilizzati al 10-15%)
3. Costi altissimi per hardware dedicato 
##### Con la virtualizzazione 
1. 1 server fisico = 10-15+ macchine virtuali 
2. Utlizzo ottimale delle risorse (80-90%)
3. Condivisione intelligente di CPU, RAM e storage
4. VM possono spostarsi tra host automaticemtne 
5. Non ci interessa su quale host fisico gira la VM 