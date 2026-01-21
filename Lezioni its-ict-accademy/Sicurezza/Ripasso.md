### Crittografia RSA

Abbiamo la chiave pubblica, composta dall'esponente pubblico "e" e il modulo "n" 
Esponente pubblico è un numero primo ed è coprimo (massimo comun divisore) con la funzione di eulero applicata al modulo. 

la funzione eulero: 
$p(n) = (p-1) * (q-1)$

p e q sono due numeri segreti e casuali, inoltre sono numeri primi molto grandi.
Il modulo è il prodotto tra questi 2 numeri, difatti
questo è il modulo n dove p e q sono le chiavi 
$n = p*q$
 Il modulo è condiviso nella chiave pubblico sia nella  privata 
Cifratura con la chiave pubblica 
### Cifratura RSA

$c = m^{e} mod n$
La chiave privata (d,n): 
- serve per cifrare 
