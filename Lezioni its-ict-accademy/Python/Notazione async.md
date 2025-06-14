La O notation 
- O(1): significa che si ha una costante in input e quindi si fanno un numero costante di operazioni. QUinsi è un algorito indipendente: se si ha un algo una lista di n costante di elementi si fanno un numero costante di operazioni quanto è lunga la sudetta lista. 

- O(log n): per la ricerca binaria
- O(n): se si deve trovare un elemento in una lista disordinata, perché si deve scorrere tutta la lista. 
  Quindi se si ha una lista disordianta non ha senso prima ordinarla a meno che se non si sa a priori se questa lista di elementi ha un milione o più di elementi allora ha senso rioridnarla per avere un indexing ordinato. Caso tipico un database con un milione di righe conviene sempre ordninare l'indice e usare la ricerca binaria per trovare gli/l'elementi/o che servono.
		$f(n) = 3n^2+2n+1 = 3n^2 = O(n^2)$
      
      
altro esempio: 
      $f(n) = 2^n + 3n^3+2n^2+5 = 2^n = O(n)$ 
      Quindi in questi casi n è esatamente l'input della funzione e per capire $O(log_2  n)$ la notazione O serve  per capire quale il detr dominate in una funzione 

- O(n log  n):  Questa è la maniera più efficiente di ordinare le liste,anche se il calcolo computazionale inizia a non essere buono
- O (n^2): poliminomiale, tuttavia non è molto efficiente ma non c'è altro modo 
- O(2^n): Fibonacci
	  TSP: problema del comesso viaggiatore; amazon deve fare una serie di consegne quindi una serie di case in cui andare e devp trovare il modo di consegnare i pacchi scelginedo la strada più efficiente e per farlo bisogna trovare tutte le combinazioni possibili quindi per troavere la soluzione a questo problema si risolve in maniera esponenziale, attraverso algoritmi detti euristiche:
		sono algoritmi che permettono di trovare soluzioni sub-ottime per un problema in cui l'ottimo è difficile da trovare.

- O(n!): n fattoriale, permutazioni di una serie di numeri
	  Immaginao di avere  i numeri 1,2,3 e voglimao vedere tutte le sequenze possibili con questi numeri, quindi si parte con 123 → 231, 123→132, 123→321, 123→213, 123→312. 
	  QUindi quante permutazioni ci sono di 3, 3! e di 100; 100!.
Questo è il numero di permeutazioni al secondo:
$3*10^9 = 3000,000,000$ 
Per calcolare il numero di permutazioni di 100! bisogna fare:
$100/3*10^9 = 33333,333,333.33$ 
