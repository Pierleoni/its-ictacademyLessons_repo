from __future__ import annotations
from typing import Any
class Studente:
    _nome: str
    _esami: dict[Modulo, _esame] # da assoc. 'esame' [0..*] resp. singola, certamente non noti alla nascita

    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._esami = dict()

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def esami(self) -> frozenset[_esame]:
        return frozenset(self._esami.values())

    def esame(self, modulo: Modulo) -> _esame:
        return self._esami[modulo]

    def add_esame(self, modulo: Modulo, voto: int) -> None:
        # # ci assicuriamo che in self._esami non ci sia già un esame del modulo 'modulo'
        #Todo assicurarsi che in self._esami non ci sia già un esame del modulo 'modulo'
    ''' NON HO BISOGNO DI FARE IL CICLO!
        for link in self.esami():
            if link.modulo() == modulo:
                raise ValueError(f"Lo studente {self.nome()} ha già superato il modulo {modulo.codice()}")'''
        if modulo in self._esami:
            raise KeyError(f"Lo studente {self.nome()} ha già superato il modulo {modulo.codice()}")

        l: _esame = _esame(self, modulo, voto)
        self._esami[modulo] = l

    def remove_esame(self, modulo: Modulo) -> None:
        if modulo not in self._esami:
            raise KeyError(f"Lo studente {self.nome()} non ha superato il modulo {modulo.codice()}!")
        del self._esami[modulo] 

    def remove_link_esame(self, esame: _esame) -> None:
        if esame.studente() != self:
            raise ValueError(f"Impossibile rimuovere questo esame perché non è relativo a {self.nome()}, ma a {esame.studente()}")
        del self._esami[esame.modulo()]

    def media_voti(self) -> float:
        try:
            somma: int = 0
            for esame in self.esami():
                somma += esame.voto()
            return somma / len(self.esami())
        except ZeroDivisionError:
            raise RuntimeError(f"{self.nome()} non ha superato alcun esame, quindi non ha una media!")
    
    def __repr__(self) -> str:
        return f"Studente({self.nome()})"
    
    


class Modulo:
    _codice: str

    def __init__(self, codice: str) -> None:
        self._codice = codice

    def codice(self) -> str:
        return self._codice

    def set_codice(self, codice: str) -> None:
        self._codice = codice

    def __repr__(self) -> str:
        return f"Modulo({self.codice()})"

class _esame:
    _studente: Studente
    _modulo: Modulo
    _voto: int

    def __init__(self, studente: Studente, modulo: Modulo, voto: int) -> None:
        self._studente = studente
        self._modulo = modulo
        self._voto = voto

    def voto(self) -> int:
        return self._voto

    def studente(self) -> Studente:
        return self._studente

    def modulo(self) -> Modulo:
        return self._modulo

    def __hash__(self) -> int:
        return hash((self._studente, self._modulo))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False

        return self.studente() is other.studente() \
            and self.modulo() is other.modulo()

    def __repr__(self) -> str:
        return f"{self.studente()} prende {self.voto()} a {self.modulo()}"


# slide 63
if __name__ == "__main__":
    alice: Studente = Studente("Alice")
    biagio: Studente = Studente("Biagio")
    prog1: Modulo = Modulo("Progettazione")
    bd1: Modulo = Modulo("Basi Dati 1")
    python14: Modulo = Modulo("Python 1-4")
    web12: Modulo = Modulo("Web 1-2")


    alice.add_esame(prog1, 21)
    print(alice.esame(prog1))
    alice.add_esame(bd1, 30)
    print(alice.esame(bd1))
    alice.add_esame(python14, 25)
    print(alice.esame(python14))
    alice.add_esame(web12, 25)
    print(alice.esame(web12))

    print("\nProviamo a far superare *di nuovo* Progettazione ad alice")
    try:
        alice.add_esame(prog1, 28)
    except KeyError:
        print("Ci siamo giustamente accorti che alice aveva già superato il modulo Progettazione!\n")




    esami_alice: frozenset[_esame] = alice.esami()
    print(f"Alice ha superato {len(esami_alice)} esami finora:")
    for esame in esami_alice:
        print(f"\tAlice ha superato {esame.modulo()} con il voto {esame.voto()}")


    print(f"\nLa media di {alice.nome()} è {alice.media_voti()}")

    max_voto = max([esame.voto() for esame in alice.esami()])
    min_voto = min([esame.voto() for esame in alice.esami()])
    print(f"\nIl massimo voto di {alice.nome()} è {max_voto}")
    print(f"Il minimo voto di {alice.nome()} è {min_voto}\n")


    # Proviamo a calcolare la media dei voti di biagio, che però non ha superato nessun esame!
    try:
        print(f"La media di {biagio.nome()} è {biagio.media_voti()}") # dà errore perché biagio non ha superato esami
    except RuntimeError:
        print("Ci siamo giustamente accorti che non possiamo chiedere la media aritmetica di biagio, poiché non ha superato nessun esame!\n")

    esame_alice_prog: _esame = alice.esame(prog1)

    print("\nProviamo ad aggiungere altri esami ad alice, in un modo che non è permesso:")
    # Non si può più fare, perché sto utilizzando qualcosa con l'underscore, cioè privato!
    # L'idea è che i link 'esame' andrebbero creati solamente invocando 'add_esame' su un oggetto 'Studente'
    esame_cattivo = _esame(alice, prog1, 54)
    esame_cattivo1 = _esame(alice, prog1, 65)
    esame_cattivo2 = _esame(alice, prog1, 0)

    print(esame_cattivo)