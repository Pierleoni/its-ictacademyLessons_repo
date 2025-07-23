Il paradigma REPL  = Read Value Print Loop, è il paradigma su cui si basa Python per questo non è realemente un linguaggio OOP.


Se andiamo sul terminale e chiamiamo Python entriamo in Python e scrivo la prima riga, l'interprete la legge, la esegue e ritorna alla riga nuova per una nuova esecuzione, quindi il paradigma REPL è che l'interprete legge ed esegue il codice dalla prima riga all'ultima n modo sequenziale.
Python essendo un linguaggio interpretato in relata è più lento rispetto ad altri linguaggi come C.
Questo rallentamento è dato dal paradigma REPL perché deve leggere ed eseguire l'operazione, valutarla ed eseguirla.
Python quindi è un linguaggio interpretato.
Python è un linguaggio debolmente tipizato: una variabile (un simbolo a quale posso associare un valore) posso associare valori di tipo  differente
```run-python
x = "Ciao"
print(f"Primo valore di x: {x}")
y = 12
x = y
print(f"Secondo valore di x: {x}")

x = 3.14
print(f"Terzo valore di x: {x}")
```

Difatti in Python è facile sbagliare l'assegnazione dei valori alle variabile, difatti è molto utile per quando si vuole scrivere codice in modo rapido in poche righe.

Python nasce dai programmatori, a differenza del linguaggio Pascal, però non è ortogonale: 

Nascendo dagli sviluppatori si integra bene con librerie esistente: infatti oggi si utilizza per le AI ma la maggior parte di librerie sono scritte in C.
Infatti Python fa il cosidetto scripting.
Le AI sono scritte in Cuda: è una libreria di C particolare (anche gli algorimti nelle GPU).
```run-python
print("Ciao")

a = print

a(10+10)

print = 2*3
print("Ciao")
```
In Python valori e funzioni sono la stessa cosa: posso passare come valori una funzione e viceversa.

Faccimao un approccio olistico, a cosa serve i computer? La prima risposta sarebbe per fare calcoli, ma in realta per sua natura non saprebbe fare neanche le somme.
Se un computer facesse i clacoli sarebbe una calcolatrice.
L'informatica tratta dell'automazione delle gestioni delle informazioni, l'informazione è 0 o 1 (Si o No).
Quindi l'informazione è Vero o Falso, intorno a uqesta struttura Aristotele ci ha costruito tutta la sua logica, in altre parole la logica booleana:
And = è congiuntivo; è vero se i due casi sono veri
Piove e Uscire = Prendo l'ombrello
OR = disgiintivo; basta che uno dei due sia vero allora il risultato è vero
XOR = lavora sulla differenza

| A   | B   | AND | OR  | XOR |
| --- | --- | --- | --- | --- |
| T   | T   | T   | T   | F   |
| T   | F   | F   | T   | T   |
| F   | T   | F   | T   | T   |
| F   | F   | F   | F   | F   |
Gli operatori logici sono la base della gestione dell'informazione.
Problema: se devo fare un computer queste cose li devo rendere un circuito eletrrico (Transistor, Valvole, etc.).
Entriamo dentro la CPU: come rappresenta il True, tramite il potenziale elettrico: nelle vecchie CPU il true era 12V e il False -12V ma da +12 a -12 il salto è alto, adesso il limite si è stretto pero se si stringe troppo il gap la macchina rischia di impazzire.
Analogamente possiamo pensarlo come un compressore Audio: comprimendo il picco massimo e il picco minimo della fluttuazione dell'onda elettrica il salto dell'elettrone è più veloce.
Ad esempio: nei chip delle carte di credito dentro si ha la CPU, la RAM e il Disco fisso, un esempio di attacco e quello di stringere il gap del potenziale elettrico, quindi si imposta una soglia di treshold bassa ma la fluttuazione dell'onda rimane uguale e superando la soglia il chip impazzisce.
L'And lo posso implementare con tre transistor, ma la somma non la si può implementare con i transitor: 
se si facesse la somma in binario di questi valori 

| A1  | A2  | Somma | Riporto(fine dell'unità) |
| --- | --- | ----- | ------------------------ |
| 0   | 0   | 0     | 0                        |
| 0   | 1   | 1     | 0                        |
| 1   | 0   | 1     | 0                        |
| 1   | 1   | 0     | 1                        |

Quindi la somma è il costrutto logico di Or e XOR.
QUindi un computer nativamente non può fare calcoli matematici

Che significa operazione artimentica? Quando si lavora con un editor e si digita la lettera "A" vediamo a video la lettera ma la CPU non conosce questa lettera perchè lavora per composizioni di bit o byte:
nello specifico  la word è 16 bit o 2 Byte, la DWord 32bit o 4Byte mentre la Qword è 64bit/8Byte.
Le prime CPU sono 8 bit: immaginimao di avere uno ospedale con 4 reparti; 
cardio,
Gastro,
Neuro,
Enterologia,
possimao identificare i pazienti internati tramite i bit: il paziente1 0100 è cardio, il paziente2 1100 è neuro, il paziente3 1010 è gastro, il paziente 4 è 1111 è Neuro è cosi via.
Quindi il codice binario è informazione non valori numerici senno faremmo analisi matematica.

In informatica parliamo di linguaggio quando diversi dispositivi devono capirsi e parlarsi quindi un linguaggio comune interpetabile comune: esempio tra una stampante e un computer.
All'inizio i produttori dei computer decidevano i diversi linguaggi per i prorpi sistemi quindi si aveva la necessita di uno standard univoco: è così che nasce l'ascii.
Quindi i caratteri sono una interpretazione di pattern di bit, ma quanti caratteri servono? Nell'america degli anni 70 si è scelto di usare l'afabeto americano che ha 26 caratteri ma solo in minuscoli, quindi servono anche in i caratteri in maiuscolo e quindi altri 26 caratteri maiuscoli, quindi in tutto sono 52 caratteri. Poi servono i numeri, la puntegiattura, i simboli speciali, ecc. quindi alla fine sono già un centinaio quindi cento comandi diversi ma nell'esempio con la stampante il computer da altri comandi come il cambio pagina, vai alla riga nuova, il comando per fermarsi, ecc. 
Il totale di questi comandi sono 127 comandi (il 128 è la tilde).
Mi servono quindi 7bit.



