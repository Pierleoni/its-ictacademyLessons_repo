Immaginiamo di testare l’espressione con `score = 70`.

- `(score < 51)` → `70 < 51` → **false**
    
- `¬(score < 51)` → `¬false` → **true**
    
- `(score > 80)` → `70 > 80` → **false**
    
- Quindi: `true OR false` → **true**
    

Secondo questa condizione, **uno studente con 70% riceverebbe un ordinary pass** — il che _potrebbe sembrare_ corretto.

Ma prova con `score = 85`:

- `score < 51` → `false`
    
- `¬(score < 51)` → `true`
    
- `score > 80` → `true`
    
- Risultato: `true OR true` → **true**
    

**Errore logico:** anche 85% viene considerato come “ordinary pass”, ma dovrebbe essere classificato come **“distinguished pass”**.  
La condizione non è abbastanza precisa per escludere chi ha più dell’80%.

### ✔️ Soluzione corretta

Per rappresentare logicamente e correttamente i tre casi (fail, ordinary pass, distinguished pass), è meglio **esplicitare i range**:

```
if score > 80
    grade = 'distinguished pass'
else if score >= 51 AND score <= 80
    grade = 'ordinary pass'
else
    grade = 'fail'

```
In logica simbolica:
```
if (score > 80)
    → distinguished pass
else if ((score ≥ 51) ∧ (score ≤ 80))
    → ordinary pass
else
    → fail

```


### Punti chiave da ricordare

- **La logica simbolica è rigorosa**: ogni operatore ha una _precedenza_ specifica.
    
- **Il linguaggio naturale è ambiguo**, quello computazionale non può permetterselo.
    
- **L’uso scorretto di operatori logici** (`AND`, `OR`, `NOT`) può portare a risultati illogici anche se “sembrano giusti”.
    
- **L’algoritmo deve considerare ogni possibile caso**: se dimentichi un ramo logico, il computer non “indovinerà” cosa fare.
    
- Usare **parentesi** per chiarire l’ordine di valutazione è una buona pratica (esattamente come in matematica).


---
# Traduzione in inglese

Imagine testing the expression with `score = 70`.

- `(score < 51)` → `70 < 51` → **false**
    
- `¬(score < 51)` → `¬false` → **true**
    
- `(score > 80)` → `70 > 80` → **false**
    
- So: `true OR false` → **true**
    

According to this condition, **a student with 70% would receive an ordinary pass** — which _might seem_ correct.

But try with `score = 85`:

- `score < 51` → `false`
    
- `¬(score < 51)` → `true`
    
- `score > 80` → `true`
    
- Result: `true OR true` → **true**
    

**Logical error:** a score of 85% is also considered an “ordinary pass,” but it should be classified as a **“distinguished pass.”**  
The condition is not precise enough to exclude those with more than 80%.

---

### ✔️ Correct Solution

To logically and correctly represent the three cases (fail, ordinary pass, distinguished pass), it's better to **explicitly define the ranges**:

```
if score > 80:
    grade = 'distinguished pass'
elif score >= 51 and score <= 80:
    grade = 'ordinary pass'
else:
    grade = 'fail'

```

In symbolic logic:

```python
if (score > 80)
    → distinguished pass
else if ((score ≥ 51) ∧ (score ≤ 80))
    → ordinary pass
else
    → fail

```

### Key Points to Remember

- **Symbolic logic is strict**: each operator has a specific _precedence_.
    
- **Natural language is ambiguous** — computational logic cannot afford that.
    
- **Incorrect use of logical operators** (`AND`, `OR`, `NOT`) can lead to illogical outcomes even if they “seem right.”
    
- **Your algorithm must cover every possible case**: if you forget a logical branch, the computer won’t “guess” what to do.
    
- Using **parentheses** to clarify the order of evaluation is good practice (just like in math).