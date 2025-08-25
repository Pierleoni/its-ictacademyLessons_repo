Nella crittografia moderna il segreto è scambiaris di info.
Prendiamo la tabella di verità:

| A   | B   | AND | OR  | XOR |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 1   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   | 1   |
| 1   | 0   | 0   | 1   | 1   |
| 1   | 1   | 1   | 1   | 0   |
Il programmatore che lavora in C o assembler: i+ e i++ fanno la stessa cosa 
Ad esempio in Java
i++: significa che aggiorno il vlaore dopo averlo letto
++i: prima sommo il valore poi lo aggiorno

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
2. 