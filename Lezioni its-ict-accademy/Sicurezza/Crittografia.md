Nella crittografia moderna il segreto è scambiaris di info.
Prendiamo la tabella di verità:

| A   | B   | AND | OR  | XOR |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 1   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   | 1   |
| 1   | 0   | 0   | 1   | 1   |
| 1   | 1   | 1   | 1   | 0   |
Il programmatore che lavora in C o assembler: `i+` e `i++` fanno la stessa cosa 
Ad esempio in Java
`i++`: significa che aggiorno il vlaore dopo averlo letto
`++i`: prima sommo il valore poi lo aggiorno

```C++
#include <iostream> 
using namespace std; 
int main(int argc, char * argv[]) { 
	for (int i=0; i<100; ++i) { } 
	int n=10; 
	int m=10; 
	cout << n++ << ", " << n++ << endl; 
	cout << "Ora: " << n << endl; 
	cout << ++m << ", " << ++m << endl; 
	cout << "Ora: " << m << endl; 
	}
```



Il secondo è più veloce del primo, di fatto i programmatori di C usano il secondo metodo nei cicli.

X xor X → 0: un numero xor stesso da 0 .
In Python:
```python
a = 45
b = 45
print(45^45) #Output: 0
```

Mentre Y xor 0 = 0. Questo perché non si sa il valore di Y ma se si fa il contrario restituisce Y:
R = Y xor X
Devo calcolare R xor X = Y xor X xor X = Y xor 0 = Y, quindi R xor X = Y.
questo si chiama cifra mentre.
### Crittografia riservatezza vs integrità
La crittografia simmetrica riguarda un segreto e la sua condivisione.
I peer condividono lo stesso segreto.
Esempio: 
A vuole inviare un messaggio M a B ed essere sicuro che solo B lo possa leggere.
Viene scelta una chiave (stringa) che poi diventa un numero, quindi viene condiviso lo stesso segreto in un ambiente sicuro utilizzando la stessa chiave.
Nella crittografia simmetrica eistono i conetti di dominio e codominio.
La crittografia si lavora a blocchi di 64 bit e così via, ad oggi la più sicura è l'AES-256: cripta il messaggio più grosso a 256 bit quindi 32 caratteri, se si ha messaggi di più caratteri lo si spacchetta in tanti messaggi più piccoli.
Il dominio è l'elenco dei valori sui quali opera la funzione, questa funzione lavora su tutti i possibili blocchi a 256 bit.
Cifrare quindi signfica prendere i 256 bit e spostarlsi e scambiarli, quindi il codominio: l'insieme dei vlaori risultanti della funzione è sempre grande 256 bit.
Dal codominio per tornare al dominio si usa l'algoritmo + la chiave quindi se non si conosce nell'algoritmo ne la chiave non è possibile decifrare il messaggio.
Se qualcuno strada facendo riesce a trovare uno di questi due fattori riesce a decodificare il messaggio ma con valori diversi.
Quindi un algoritmo garantisce la sicurezza ma non l'integrità della sicurezza, posso farlo ma a discapito della quantita del pachhetto. 

In casi di crittografia ad alti livelli un programmatore deve conoscere solo mezza chiave.

Crittografia simmettrica: i pachetti condividono una chiave. 
Ha un dominio di $2^128$ bit e ha un codominio identico (2 alla 128 blocchi da 128 bit), questo perché la crittografia prevede che se si crittografica un massaggio lo posso anche decifrare .
e coppie che posso formare sono 2^128 * 2^128 coppie e in base alla chiave sono diverse con la caratteristica che un elemento del dominio corrisponde a uno e uno solo elemento del dominio.
L'algoritmo è l'implemtazione di un problema matemaitco implementato dagli informatici.
Questo modello quali problemi pone? Ad esempio prendendo il messaggio "Ciao, come va?" nel codominio potrebbe diventare "Buongiorno, tutto bene": questo perchè il primo messaggio è lunog 16 bit esattamente come il secondo messaggio.

Quindi è la chiave che determina l'accopiamento, un buon algoritmo di cifratura se ha due messaggi con una differenza di un bit questi due messaggi saranno diversi sopratutto il messaggio decifrato deve esssere profondamento diverso dal primo messaggio perché cambiando un solo bit cambia un solo carattere.
Questo modalità presenta diversi problemi:
1. riduco la dimensioni di bit da spedire e in altri metto numeri casuali


### Problemi della crittografia simmetrica
Caratteristica: 
- Utilizza la stessa chiave sia per cifrare che decifrare
- È sia positivo che negativo:
	- Negativo: 
		- servono ogni chiave pe ogni coppia
		- In contesti grandi come reti sociali non ha senso perché devo avere più chiavi
	- Positivo: 
		- Le chiavi sono cablate negli apparati già accoppiati in modo che solo i dispositivi cablati possono parlarsi.
		- È veloce ed organizzativa

Per questi motivi nasce la crittografia a-simmetrica

### Crittografia simmetrica
Alice manda un messaggio a Bob, e vuole essere sicura che solo Bob possa decifrare il messaggio:
Bob ha 2 chiavi:
1. pubblica: quindi ora bob da ad alice la sua chiave pubblica.
2. privata: c'è l ha bob in tasca (es: carta ID elettronica). 

> [!ticket] Quando nasce una chiave privata è possibile generare una chiave pubblica
> 

Ora alice cifra scrive e cifra il messaggio con un algoritmo asimmetrico e usa la chiave pubblica di Bob. Bob dal canto suo decifra il messaggio con la sua chiave privata 

Con la crittografia asimmetrica ognuno ha una coppia di chiavi pubbliche e private e ognuno cifra con la chiave pubblica e decifra con la sua chiave privata. 
Che ruolo hanno le chiavi pubbliche e private?
Immaginiamo di avere un orologio che punta a 12:00 :
cifrare significa che da 12 mi sposto a un certo punto e decifrare ritorno alle 12.
Quindi mi sposto sempre in avanti mai indietro perché uso le cosiddette funzioni one-way.

### RSA
RSA: il primo e forse il più importante algoritmo di crittografia asimettrica
Nel RSA abbiamo:
- n che è il modulo, 
- e chiave pubblica(esponente pubblico), 
- d esponente privato.
La coppia n, e è la chiave pubblica, mentre la coppia n, d è la chiave privata. 
Voglio decifrare m:
$M^e mod n = c$

Se voglio decifrare c:
$c^d modn = m$

Quindi se l'host A cifra m con la chiave pubblica di B, quindi m è un numero intero.
Quindi se si ha un messaggio testuale lo devo prima convertire in un intero. 
QUindi l'operazione di cifra è:
$$M^e mod n → C$$
Questo mi da il messaggio cifrato c che è un numero intero, per decifrare: 
$$C^d mod n → M$$
Per fare questa operazione sotto Python esiste l'operazione pow() è si scrive
```python
pow (m, e, n)
```

Noi dobbiamo fare da `str → int` e poi `int → str` .


### Diffie-Hellman
John (J) e Katy(K) volgiono creare una chiave intesa come una sequenza di byte che solo loro 2 conosceranno.
Quando abbiamo parlato di crittografia asimmetrica due host concoradno una chiave segreta tra solo loro 2.
Quindi J e K vogliono fare la stessa cosa ma volgiono creare questa chiave scambiandosi messaggi pbblici (inteso come messaggi senza protezione della chiave. 
Es: internet, whatsapp, ecc.)
L'algoritmo di Diffie-Hellman ovvia a questo problema: 
scambiare messaggi pubblici ma che solo i concordati hanno la chiave per decifrarla.
QUesta si basa sulla sequente considerazione:
un numero : 2
elevato a una poteza elevato a sua volta ad un altra potenza è equivalente il numero elevato per il prodotto delle due potenze:
$$
(2^3)^2 ≡ (2^2)^3 ≡ 2^{2*3} = 2^6
$$

Più generalmente:

$$(n^a)^b =? (n^b)^a≡n^{a*b}$$

Questa cosa si puo risolvere con il logaritmo:
$$log_2 16$$
Significa che:
$$ 2^x=16$$



Nella artimetica modulare non si puo fare il logaritmo, non si puo fare l'inverso della potenza. 
J e K condividono due info pubbliche n,p.
Entrambi queste due info sono pubbliche ovvero i valori di n e p si consocono pero nella aritmentica modulare benchè si sappiano i valori di queste due info non si possono fare l'inverso della potenza di questi valori perché la potenza di calcolo sarebbe troppo elevata.
Dopo J crea un segreto a e K crea un segreto(un numero casuale) b.
A qesto punto J invia a K un modulo:
$P^A mod n = x$ e K invia a J $P^b mod n$
QUindi K prende questo numero e fa 
$P^{a*b}modn$, mentre J prende il numero inviato da K e fa $P^{b*a}modn$ 

In [[Introduzione a Python|Python]] questa cosa si fa: 
```python
#J fa: 
n = 37
p = 11
a = 13
pow(p,a,n)

#K fa: 
pow(36, a,n)
```

Nella vera aritmetica modulare l'algoritmo di diffie-hellman è cosi 
A ha `p,n` e B ha `p,n`.
Entrambi hanno due numeri segreti, rispettivamente a e b.
A manda $P^a modn$ a B che quando lo riceve fa $(P^a modn)^b modn/key$, e B manda $P^bmodn$ ed A quando lo riceve fa $(P^b modn)^a modn/key$. L'obiettivo è quello di costruire una chiave segreta che l'attaccante da fuori vedendo il traffico ma non conoscendo A e B non sa decifrare. 


### Hash 
Una funzione hash è una funzione che converte una stringa in un numero.
Se lo facciamo in temrini di stringhe: 
$$f('Ciao') → ||$$

In python con [[Collections#I dictionaries#Gli hasher nei dizionari|la chiave del dizionario]] calcola una posizione è in quella posizione si trova la coppia chiave-valore 

Abbiamo visto che la crittografia della chiave pubblica e della chiave privata 
A cifra $(M, K^bpos)=C$ mentre B deicfra $(C, K^b pos) =M$.
A sa che solo B puo leggere il messaggio.
Ma come fa B a sapere che il messaggio è stato inviato da A? 
A cifra il messaggio con la sua chiave privata e poi lo cifra con la chiave pubblica di B 
$(M, K^Apos),K^Bpos$ 
Mentre B lo deicifra con la sua chiave privata e intenranamente c'è mepre uil messagio cifrato con la chiave privata di A quindi B lo decifra con la sua chiave pubblica $(C,K^Bpos), K^Apos$. 




#### Hash crittografico 
- Sha (256 bit/32 byte) (certificato di firma digitale)
- Keccam (512/64 byte) (bitcoin, blockchain)

3 prerogative del hash crittografico: 
1. non invertibile: hash non può usare tecniche crittografiche 
2. paradosso del compleanno: evitare il più possibile delle collisioni, se io ho un milione di possibili documenti ne prendo un altro milione un milione per un milione è sicuro che trovo un documento che condivide la stessa chiave per questo devo prendere un numero molo grande 
3. deve sparsificare: ho 2 messaggi che sono identici eccetto un bit l'hash dove essere completamento diverso.
Wuindi al posto di cifrare il messaggio io cifro l'hash del messaggio con la mia chiave privata.
Ma come faccio verificare che il messaggio l'ha scritto chi effetivemrnte la mandato, decifro lìhash del messaggio con la chiave pubblica del mittente poi decifro l'hash


Firma digitale: 
$${M cifra(hash(m) K^a_{pos}):F} $$
A B arriva M e F
1.decifra:  $$(F, K^a_{pos})->HASH(m)=N$$
2. Calcola: 
$$HASH(n|=N2)$$ Se $N| diverso da N$ 



