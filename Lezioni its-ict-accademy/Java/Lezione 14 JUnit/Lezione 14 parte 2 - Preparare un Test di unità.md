## Preparare un test di unità

Abbiamo visto [[Lezione 14 - Il Framework JUnit|cosa è JUnit e come funziona a livello teorico]], adesso andiamo ad implementarlo a livello di codice
###  Cos’è un test di unità

Un **[[Lezione 14 - Il Framework JUnit#Test di unità (Unit Test)|test di unità]]** ha lo scopo di: 
- ==verificare il comportamento di **una singola classe**, isolandola dalle sue eventuali dipendenze.==

L’obiettivo è controllare che la classe:

- ==rispetti le proprie responsabilità;==
    
- ==soddisfi i vincoli definiti;==
    
- ==produca risultati corretti nei diversi scenari.==
####  Fase preliminare: analisi della classe

Prima di scrivere la classe di test, è necessario:

##### 1. Comprendere le responsabilità

- **Qual è il compito della classe?**
    
- **Quali invarianti deve rispettare?**
    
- **Quali condizioni devono essere sempre vere?**
    

Senza questa analisi, il test rischia di essere incompleto o superficiale.

#####  2. Individuare i metodi pubblici da testare

Nei test di unità si testano **solo i metodi pubblici**.

- ==I metodi privati non si testano direttamente.==
    
- ==Se un metodo privato contiene logica complessa, è spesso un segnale che quella logica dovrebbe essere estratta in una nuova classe testabile.==
    

Il test deve verificare il comportamento osservabile dall’esterno.

#####  3. Analizzare i casi d’uso

Per ogni metodo pubblico, occorre individuare:

- **Casi normali (successo)**  
    → ==utilizzo standard con input validi.==
    
- **Casi limite (ancora di successo)**  
    → ==valori ai bordi del dominio (es. 0, stringhe vuote, collezioni con un solo elemento).==
    
- **Casi di errore**  
    → ==input non validi, eccezioni attese, violazioni di vincoli.==
    

Un buon test copre tutte queste categorie.


###  Approccio teorico/pratico alla scrittura

#### 1. Seguire lo schema AAA

Ogni test dovrebbe seguire lo schema:

- **Arrange** → prepara lo stato iniziale
    
- **Act** → esegui l’azione da testare
    
- **Assert** → verifica il risultato
    

Questo schema aiuta a mantenere il test leggibile e strutturato.
####  2. Definire chiaramente lo stato iniziale

Prima di invocare il metodo, bisogna:

- ==creare gli oggetti necessari;==
    
- ==impostare i valori iniziali;==
    
- ==configurare eventuali dipendenze.==
    

Uno stato iniziale ambiguo porta a test fragili o poco chiari.

####  3. Testare una sola cosa alla volta

Un buon test:

- ==verifica **una sola proprietà o comportamento**;==
    
- ==ha **un solo motivo per fallire**.==
    

> [!failure] Non è buona pratica:
> 
> 
> - verificare due condizioni indipendenti nello stesso test;
>     
> - testare contemporaneamente due scenari di errore.

    

Se un test fallisce, deve essere immediatamente chiaro il motivo

#### 4. Usare nomi descrittivi
Il nome del metodo di test dovrebbe descrivere:
```scss
method_condition_expectedResult()
```

Esempio concettuale:
```scss
addContact_withValidData_shouldIncreaseSize()
```

Un buon nome rende il test autoesplicativo.


#### 5. Eseguire e analizzare il risultato

Dopo l’esecuzione:

- Cosa non funziona?
    
- Perché fallisce?
    
- In quale scenario specifico?
    

Un test che fallisce non è un problema:  
- ==è uno strumento diagnostico che segnala un comportamento non conforme alle aspettative.==


> [!NOTE]  Principio fondamentale
>
>Un test di unità ben scritto è:
>
>- indipendente;
   > 
>- deterministico;
   > 
>- leggibile;
   > 
>- focalizzato su un singolo comportamento.

### Esempio: test di `Calcolatrice`

Quando prepariamo un test di unità per la classe `Calcolatrice`, gli **obiettivi principali** sono chiari:

1. **Testare tutti i metodi pubblici** della classe, assicurandoci che ciascuno si comporti come previsto.
    
    - ==I metodi privati non vengono testati direttamente; eventuali comportamenti complessi al loro interno devono emergere dai metodi pubblici.==
        
2. **Verificare sia i risultati corretti sia le eccezioni attese**.
    
    - ==Per esempio, la somma deve produrre il risultato corretto, mentre la divisione per zero deve generare l’eccezione corrispondente.==
        
3. **Focalizzarsi su un solo comportamento per test**.
    
    - ==Ogni metodo di test deve concentrarsi su un singolo caso o condizione, così che il fallimento indichi esattamente quale comportamento non funziona.==
        
4. **Utilizzare nomi descrittivi per i test**.
    
    - ==Il nome del metodo deve spiegare chiaramente cosa viene testato e quale risultato ci si aspetta.==
    - Esempio:
```java
void sum_withPositiveNumbers_shouldReturnCorrectResult() { … }
void divide_byZero_shouldThrowException() { … }
```

Seguendo questi principi, ogni test diventa **auto-contenuto, leggibile e diagnostico**, facilitando sia la manutenzione della classe di test sia l’individuazione immediata dei problemi.

####  Esempio completo: test di `Calcolatrice` in JUnit 5

La classe di test `CalcolatriceTest` mostra come applicare i principi visti finora: test di unità, nomi descrittivi, separazione dei casi e uso delle asserzioni

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalcolatriceTest {

    private Calcolatrice calcolatrice;

    // ==== Setup del test ====
    // Viene eseguito prima di ogni metodo @Test
    @BeforeEach
    void setUp() {
        calcolatrice = new Calcolatrice();
    }

    // ==== Test dei metodi somma ====
    @Test
    void somma_dueNumeriPositivi_restituisceSommaCorretta() {
        int risultato = calcolatrice.somma(3, 5);
        assertEquals(8, risultato);
    }

    @Test
    void somma_conZero_restituisceAltroNumero() {
        int risultato = calcolatrice.somma(0, 7);
        assertEquals(7, risultato);
    }

    @Test
    void somma_numeriNegativi_restituisceSommaCorretta() {
        int risultato = calcolatrice.somma(-4, -6);
        assertEquals(-10, risultato);
    }

    // ==== Test del metodo potenzaPositiva ====
    @Test
    void potenzaPositiva_baseEdEsponentePositivi_restituiscePotenza() throws Exception {
        int risultato = calcolatrice.potenzaPositiva(2, 3);
        assertEquals(8, risultato);
    }

    @Test
    void potenzaPositiva_baseUno_esponenteQualsiasi_restituisceUno() throws Exception {
        int risultato = calcolatrice.potenzaPositiva(1, 5);
        assertEquals(1, risultato)

```


## Spiegazione

1. **`@BeforeEach`**:
    
    - ==Garantisce che ogni test parta da una nuova istanza di `Calcolatrice`.==
        
    - ==Evita effetti collaterali tra i test.==
        
2. **Nomi descrittivi**:
    
    - ==Seguono lo schema `method_condition_expectedResult()` per rendere chiaro cosa viene testato.==
        
3. **Singolo comportamento per test**:
    
    - Ogni metodo di test verifica una sola cosa: somma, potenza o divisione.
        
    - Eventuali eccezioni sono testate separatamente con [[Lezione 14 - Il Framework JUnit#4️⃣ Test di eccezioni con `assertThrows`|`assertThrows`]].
        
4. **Asserzioni**:
    
    - `assertEquals` ==verifica il risultato atteso.==
        
    - `assertThrows` ==verifica che venga sollevata l’eccezione corretta con il messaggio giusto.==
        
5. **Isolamento dei test**:
    
    - Ogni test è indipendente dagli altri grazie alla nuova istanza creata da `@BeforeEach`.
        

