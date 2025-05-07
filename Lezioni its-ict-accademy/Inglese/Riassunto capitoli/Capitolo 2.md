# 🧠 Logica – Mappa concettuale

## 🟩 1. Cos'è la logica?
- Disciplina che studia il **ragionamento valido**.
- Obiettivo: determinare la **verità** o la **falsità** di un'affermazione tramite **regole formali**.
- Fondamento del **pensiero computazionale** e della **programmazione**.



## 🟨 2. Tipi di logica

### 🔹 Logica deduttiva
>Dal generale al particolare.

- Parte da **premesse generali**  che si assumono vere 
- Permette di dedurre una conclusione che è necessariamente vera, se le premesse sono vere.
È il tipo di logica usata **nella matematica, nella programmazione, nella filosofia** formale.
**Esempio Classico:**  
  - **Premessa 1:** Tutti gli uomini sono mortali.  
  - **Premessa 2:** Socrate è un uomo.  
  - **Conclusione:** Socrate è mortale.
La conclusione **non può essere falsa** se le premesse sono vere.  
È una forma di **ragionamento certo**: garantisce la verità della conclusione.

### 🔹 Logica induttiva
>Dal particolare al generale. 
- Parte da **osservazioni, esempi o casi concreti** → per poi portare a formulare una **regola generale**.
È il tipo di logica più usata **nella scienza**: si basa sull’**esperienza**.
- Le conclusioni sono **probabili**, ma **non garantite** al 100%.
**Esempio Classico:**  
	-  **Osservazione 1:** Il sole è sorto ieri.
	-  **Osservazione 2:** Il sole è sorto oggi.
	-  **Conclusione:** Il sole sorgerà anche domani.
 
- ⚠️ Non garantisce verità assoluta, ma **probabilità: **
  Anche se il sole **è sempre sorto**, **non è garantito** che lo farà domani (es: evento cosmico imprevisto).  
Quindi, **L’induzione non garantisce verità assoluta**, ma **fornisce ipotesi affidabili** finché non vengono smentite.

---

## 🟧 3. Proposizioni logiche
> Una **proposizione** (o enunciato) è una **frase dichiarativa** che può essere valutata come **vera (V)** o **falsa (F)**.

Deve soddisfare due condizioni:

1. Essere una **dichiarazione completa** (cioè affermare qualcosa).
    
2. Avere un **valore di verità**: o **vera** o **falsa**, mai entrambe e mai incerta.
    

💡 **Esempi di proposizioni:**

- “2 è un numero pari” → ✅ **Vera** (V)
    
- “Il cielo è verde” → ❌ **Falsa** (F)
    
- “Napoleone è morto nel 1821” → ✅ Vera (V)
    
- “5 è maggiore di 10” → ❌ Falsa (F)
    

> ✅ Queste frasi sono **proposizioni logiche** perché fanno un'affermazione chiara che possiamo giudicare vera o falsa.



### ❌ **Cosa NON è una proposizione**

> Alcune frasi **non possono essere classificate come vere o false**, quindi **non sono proposizioni**.

🚫 **Esempi di _non proposizioni_:**

- Domande: “Chi sei?” → non è vera né falsa, è una richiesta di informazione.
    
- Comandi: “Chiudi la porta!” → è un ordine, non afferma nulla da verificare.
    
- Esclamazioni: “Che bello!” → esprime un’emozione, non è valutabile come V o F.
    
- Frasi ambigue o incomplete: “Domani” → non è una proposizione, manca un contenuto dichiarativo.
    

> 🔎 In logica formale, **solo le proposizioni sono utilizzabili** per costruire ragionamenti, formule e deduzioni.

> [!example] In sintesi
> ### ✅ Proposizione
> - Frase dichiarativa che può essere **vera (V)** o **falsa (F)**.
> - Esempio:  
>   - “2 è un numero pari” → V  
>   - “Il cielo è verde” → F
> 
> ### ❌ Non proposizioni
> - Domande, comandi, esclamazioni.
> - Esempio: “Chi sei?”, “Apri la finestra!”

---

## 🟦 4. Operatori logici

| Simbolo | Nome         | Significato                         | Esempio               |
|---------|--------------|-------------------------------------|------------------------|
| ¬       | NOT          | Negazione                           | ¬P: se P è V, allora F |
| ∧       | AND          | Coniugazione (entrambe vere)        | P ∧ Q: V solo se entrambi V |
| ∨       | OR           | Disgiunzione (almeno una vera)      | P ∨ Q: F solo se entrambi F |
| →       | Implicazione | “Se P allora Q”                     | P → Q                  |
| ↔       | IFF          | Doppia implicazione (P ↔ Q)         | V se entrambi uguali   |

📌 **Nota:**  
- `P → Q` è falsa **solo** se P è vera **e** Q è falsa.  
- `P ↔ Q` è vera **solo** se P e Q hanno lo **stesso valore di verità**.

---

## 🟥 5. Tabelle di verità

### Esempio: AND (∧)

| P | Q | P ∧ Q |
|---|---|--------|
| V | V |   V    |
| V | F |   F    |
| F | V |   F    |
| F | F |   F    |

> 💡 Ogni operatore ha una sua tabella di verità per tutte le combinazioni possibili.

---

## 🟪 Le **leggi logiche fondamentali** 
appartengono all’**algebra booleana**, la branca della logica che studia il comportamento delle proposizioni con valore di verità (V o F), usando operatori come **AND (∧)**, **OR (∨)**, **NOT (¬)**, ecc.

Queste leggi servono per:

- semplificare espressioni logiche complesse;
    
- dimostrare equivalenze;
    
- progettare circuiti logici o analizzare proposizioni in filosofia e matematica.
    



### ✅ 1. **Legge dell'identità**

> Un valore logico combinato con il suo **identico** "neutro" non cambia.

- **P ∧ V ≡ P** → AND con vero non cambia P.
    
- **P ∨ F ≡ P** → OR con falso non cambia P.
    

📌 _Identità per AND: il vero è l'elemento neutro._  
📌 _Identità per OR: il falso è l'elemento neutro._

🔸 Esempio:  
Se P = “2 è pari” → V

- `P ∧ V` = V ∧ V = **V**
    
- `P ∨ F` = V ∨ F = **V**
    



### ❌ 2. **Legge del dominio (o dell’annientamento)**

> Alcuni valori “dominano” l’espressione, rendendola sempre vera o sempre falsa.

- **P ∧ F ≡ F** → AND con falso dà sempre falso.
    
- **P ∨ V ≡ V** → OR con vero dà sempre vero.
    

📌 _Falso annienta tutto con AND._  
📌 _Vero domina tutto con OR._

🔸 Esempio:  
P = “3 è dispari” → V

- `P ∧ F` = V ∧ F = **F**
    
- `P ∨ V` = V ∨ V = **V**
    

---

### 🔁 3. **Doppia negazione**

> Negare due volte una proposizione equivale a non negarla affatto.

- **¬(¬P) ≡ P**
    

📌 Vale per ogni valore di verità. È simile a dire: “Non è falso che è vero” = è vero.

🔸 Esempio:  
P = “Roma è in Italia” → V

- `¬P` = F
    
- `¬(¬P)` = V → quindi ritorna a P
    

---

### 🔄 4. **Leggi di De Morgan**

> Usate per **negare proposizioni composte** (con ∧ o ∨).

- **¬(P ∧ Q) ≡ ¬P ∨ ¬Q**
    
- **¬(P ∨ Q) ≡ ¬P ∧ ¬Q**
    

📌 _La negazione di un “e” diventa un “o” tra le negazioni._  
📌 _La negazione di un “o” diventa un “e” tra le negazioni._

🔸 Esempio:  
P = “oggi piove” → V  
Q = “c'è vento” → F

- `¬(P ∧ Q)` = ¬(V ∧ F) = ¬F = **V**
    
- `¬P ∨ ¬Q` = F ∨ V = **V**  
    ✔️ Equivalenti
    

---

### 🔃 5. **Legge commutativa**

> L’**ordine** degli elementi **non cambia** il risultato, per AND e OR.

- **P ∧ Q ≡ Q ∧ P**
    
- **P ∨ Q ≡ Q ∨ P**
    

📌 Come in matematica: A + B = B + A

🔸 Esempio:  
P = V, Q = F

- `P ∧ Q` = V ∧ F = **F**
    
- `Q ∧ P` = F ∧ V = **F**
    

---

### 🔗 6. **Legge associativa**

> Quando ci sono più proposizioni, puoi **grupparle come vuoi** senza cambiare il risultato.

- **(P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R)**
    
- **(P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)**
    

📌 L’**associazione** (cioè le parentesi) non cambia nulla.

🔸 Esempio:  
P = V, Q = V, R = F

- `(P ∧ Q) ∧ R` = (V ∧ V) ∧ F = V ∧ F = **F**
    
- `P ∧ (Q ∧ R)` = V ∧ (V ∧ F) = V ∧ F = **F**
    

---

### 🔀 7. **Legge distributiva**

> Puoi **distribuire** un operatore sull’altro come in matematica.

- **P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)**
    
- **P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)**
    

📌 Permette di riscrivere le espressioni logiche in modo equivalente.

🔸 Esempio:  
P = V, Q = F, R = V

- `P ∧ (Q ∨ R)` = V ∧ (F ∨ V) = V ∧ V = **V**
    
- `(P ∧ Q) ∨ (P ∧ R)` = (V ∧ F) ∨ (V ∧ V) = F ∨ V = **V**

---

## 🟫 7. Ragionamento logico (inferenze)
Un’inferenza è un **processo logico** in cui si parte da una o più **premesse** per arrivare a una **conclusione**. Le inferenze valide rispettano schemi precisi che garantiscono la correttezza del ragionamento.
### **Modus Ponens:**  
  > Se **P implica Q** (P → Q), e **P è vera**, allora **Q deve essere vera**.

📌 Forma:

- P → Q
    
- P  
    ⟹ Q



🧠 _È una delle inferenze più comuni e sicure._

🔸 Esempio:

- Se piove, allora porto l’ombrello.
    
- Piove.  
    ⟹ Porto l’ombrello.
### **Modus Tollens:**  
  > e **P implica Q**(P → Q), e **Q è falsa**, allora **P deve essere falsa**.

📌 Forma:

- P → Q
    
- ¬Q  
    ⟹ ¬P
    

🧠 _Serve per escludere una causa se l'effetto non si verifica._(È il ragionamento contrario al _Modus Ponens_, ma altrettanto valido)

🔸 Esempio:

- Se c’è fuoco, c’è fumo.
    
- Non c’è fumo.  
    ⟹ Non c’è fuoco.
Oppure: 
- Se studio, allora supero l'esame.
    
- Non ho superato l'esame.  
    ⟹ Non ho studiato.
### **Sillogismo disgiuntivo:**  
> Se **almeno una tra P o Q è vera**(P v Q), e **una viene esclusa**, allora **l’altra dev’essere vera**.

📌 Forma:

- P ∨ Q
    
- ¬P  
    ⟹ Q
    

🧠 _È basato sulla logica della disgiunzione (OR): se uno dei due è falso, l’altro dev’essere vero (se l’intera disgiunzione è vera)._

🔸 Esempio:

- O studio oppure vado al cinema.
    
- Non studio.  
    ⟹ Vado al cinema.

📎 Questi schemi sono **validi** indipendentemente dal contenuto.

---

## 🟨 8. Logica nei computer e nella programmazione

- Ogni condizione nei linguaggi (es. `if`, `while`) si basa su **espressioni booleane**.
- I circuiti digitali (es. porte logiche) usano **valori binari** (0 = F, 1 = V).
- Esempi in Python:
```python
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```


---

# Traduzione in inglese

## 1. # Logic – Concept Map

## 🟩 1. What is logic?

- A discipline that studies **valid reasoning**.
    
- Goal: to determine the **truth** or **falsehood** of a statement using **formal rules**.
    
- Foundation of **computational thinking** and **programming**.
    

---

## 🟨 2. Types of logic

### 🔹 Deductive logic

> From general to particular.

- Starts from **general premises** assumed to be true.
    
- Allows deriving a conclusion that is **necessarily true** if the premises are true.  
    Used in **mathematics, programming, and formal philosophy**.  
    **Classic Example:**
    
    - **Premise 1:** All men are mortal.
        
    - **Premise 2:** Socrates is a man.
        
    - **Conclusion:** Socrates is mortal.  
        The conclusion **cannot be false** if the premises are true.  
        It is a form of **certain reasoning**: it guarantees the truth of the conclusion.
        

### 🔹 Inductive logic

> From particular to general.

- Starts from **observations, examples, or specific cases** → to formulate a **general rule**.  
    Used especially in **science**: it relies on **experience**.
    
- Conclusions are **probable**, but **not 100% guaranteed**.  
    **Classic Example:**
    
    - **Observation 1:** The sun rose yesterday.
        
    - **Observation 2:** The sun rose today.
        
    - **Conclusion:** The sun will rise again tomorrow.
        
- ⚠️ It does not guarantee absolute truth, but **probability**:  
    Even if the sun **has always risen**, there's **no guarantee** it will tomorrow (e.g., unforeseen cosmic event).  
    So, **induction does not guarantee absolute truth**, but provides **reliable hypotheses** until proven otherwise.
    

---

## 🟧 3. Logical propositions

> A **proposition** (or statement) is a **declarative sentence** that can be evaluated as **true (T)** or **false (F)**.

It must meet two conditions:

1. Be a **complete statement** (i.e., assert something).
    
2. Have a **truth value**: either **true** or **false**, never both or uncertain.
    

💡 **Examples of propositions:**

- “2 is an even number” → ✅ **True** (T)
    
- “The sky is green” → ❌ **False** (F)
    
- “Napoleon died in 1821” → ✅ True (T)
    
- “5 is greater than 10” → ❌ False (F)
    

> ✅ These sentences are **logical propositions** because they clearly assert something that can be judged as true or false.

### ❌ **What is NOT a proposition**

> Some sentences **cannot be classified as true or false**, and are therefore **not propositions**.

🚫 **Examples of _non-propositions_:**

- Questions: “Who are you?” → neither true nor false, it asks for information.
    
- Commands: “Close the door!” → it gives an order, doesn’t assert anything.
    
- Exclamations: “How beautiful!” → expresses emotion, not verifiable as T or F.
    
- Ambiguous or incomplete sentences: “Tomorrow” → not a proposition, lacks a statement.
    

> 🔎 In formal logic, **only propositions are used** to build reasoning, formulas, and deductions.

> [!example] Summary
> 
> ### ✅ Proposition
> 
> - Declarative sentence that can be **true (T)** or **false (F)**.
>     
> - Example:
>     
>     - “2 is an even number” → T
>         
>     - “The sky is green” → F
>         
> 
> ### ❌ Not propositions
> 
> - Questions, commands, exclamations.
>     
> - Example: “Who are you?”, “Open the window!”
>     

---

## 🟦 4. Logical operators

|Symbol|Name|Meaning|Example|
|---|---|---|---|
|¬|NOT|Negation|¬P: if P is T, then F|
|∧|AND|Conjunction (both must be true)|P ∧ Q: T only if both T|
|∨|OR|Disjunction (at least one true)|P ∨ Q: F only if both F|
|→|Implication|“If P then Q”|P → Q|
|↔|IFF|Biconditional (P if and only if Q)|T if both have same value|
> Every operator has a truth table for all possible combinations.

---

## 🟪 Fundamental **laws of logic**

They belong to **Boolean algebra**, the branch of logic that studies the behavior of truth-valued propositions (T or F) using operators like **AND (∧)**, **OR (∨)**, **NOT (¬)**, etc.

These laws are used to:

- simplify complex logical expressions
    
- prove equivalences
    
- design logic circuits or analyze propositions in philosophy and mathematics
    

---

### ✅ 1. **Identity law**

> A logical value combined with its **neutral** does not change.

- **P ∧ T ≡ P** → AND with true doesn’t change P
    
- **P ∨ F ≡ P** → OR with false doesn’t change P
    

📌 _True is the neutral for AND_  
📌 _False is the neutral for OR_

🔸 Example:  
If P = “2 is even” → T

- `P ∧ T` = T ∧ T = **T**
    
- `P ∨ F` = T ∨ F = **T**
    

---

### ❌ 2. **Domination law (or annihilation law)**

> Some values dominate the expression, making it always true or always false.

- **P ∧ F ≡ F** → AND with false always gives false
    
- **P ∨ T ≡ T** → OR with true always gives true
    

📌 _False annihilates in AND_  
📌 _True dominates in OR_

🔸 Example:  
P = “3 is odd” → T

- `P ∧ F` = T ∧ F = **F**
    
- `P ∨ T` = T ∨ T = **T**
    

---

### 🔁 3. **Double negation**

> Negating a proposition twice is the same as not negating it.

- **¬(¬P) ≡ P**
    

📌 Applies to any truth value. It’s like saying: “It’s not false that it’s true” = it’s true.

🔸 Example:  
P = “Rome is in Italy” → T

- `¬P` = F
    
- `¬(¬P)` = T → goes back to P
    

---

### 🔄 4. **De Morgan's Laws**

> Used to **negate compound propositions** (with ∧ or ∨).

- **¬(P ∧ Q) ≡ ¬P ∨ ¬Q**
    
- **¬(P ∨ Q) ≡ ¬P ∧ ¬Q**
    

📌 _The negation of AND becomes OR between the negations_  
📌 _The negation of OR becomes AND between the negations_

🔸 Example:  
P = “It’s raining today” → T  
Q = “It’s windy” → F

- `¬(P ∧ Q)` = ¬(T ∧ F) = ¬F = **T**
    
- `¬P ∨ ¬Q` = F ∨ T = **T**  
    ✔️ Equivalent
    

---

### 🔃 5. **Commutative law**

> The **order** of elements **does not change** the result (for AND and OR).

- **P ∧ Q ≡ Q ∧ P**
    
- **P ∨ Q ≡ Q ∨ P**
    

📌 Like in math: A + B = B + A

🔸 Example:  
P = T, Q = F

- `P ∧ Q` = T ∧ F = **F**
    
- `Q ∧ P` = F ∧ T = **F**
    

---

### 🔗 6. **Associative law**

> With more propositions, you can **group them any way** without changing the result.

- **(P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R)**
    
- **(P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)**
    

📌 Grouping (i.e., parentheses) doesn’t matter.

🔸 Example:  
P = T, Q = T, R = F

- `(P ∧ Q) ∧ R` = (T ∧ T) ∧ F = T ∧ F = **F**
    
- `P ∧ (Q ∧ R)` = T ∧ (T ∧ F) = T ∧ F = **F**
    

---

### 🔀 7. **Distributive law**

> You can **distribute** one operator over the other, like in math.

- **P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)**
    
- **P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)**
    

📌 Lets you rewrite logical expressions in an equivalent form.

🔸 Example:  
P = T, Q = F, R = T

- `P ∧ (Q ∨ R)` = T ∧ (F ∨ T) = T ∧ T = **T**
    
- `(P ∧ Q) ∨ (P ∧ R)` = (T ∧ F) ∨ (T ∧ T) = F ∨ T = **T**
    

---

## 🟫 7. Logical reasoning (inferences)

An inference is a **logical process** where you start from one or more **premises** to reach a **conclusion**. Valid inferences follow precise structures that guarantee the correctness of the reasoning.

### **Modus Ponens:**

> If **P implies Q** (P → Q), and **P is true**, then **Q must be true**.

📌 Form:

- P → Q
    
- P  
    ⟹ Q
    

🧠 _One of the most common and reliable inferences._

🔸 Example:

- If it rains, then I take an umbrella.
    
- It rains.  
    ⟹ I take an umbrella.

This is the **inverse** of Modus Ponens: it starts from the **negation of the consequence**.

---

### **Hypothetical Syllogism**

> Chain of implications: if **P → Q** and **Q → R**, then **P → R**

📌 Form:

- P → Q
    
- Q → R  
    ⟹ P → R
    

🔸 Example:

- If I study, then I understand.
    
- If I understand, then I pass the exam.  
    ⟹ If I study, then I pass the exam.
    

---

### **Disjunctive Syllogism**

> If **P ∨ Q** (at least one is true), and **P is false**, then **Q must be true**

📌 Form:

- P ∨ Q
    
- ¬P  
    ⟹ Q
    

🔸 Example:

- Either it rains or I go out.
    
- It doesn’t rain.  
    ⟹ I go out.
    

---

### ❌ **Fallacies** to avoid

Logical fallacies are **incorrect reasonings** that may seem valid but aren't.

#### 🔻 **Affirming the consequent**

> Mistakenly thinking:  
> If **P → Q**, and **Q is true**, then **P is true** ❌

📌 Form:

- P → Q
    
- Q  
    ⟹ P ❌ (Invalid)
    

🔸 Example:

- If it rains, the ground is wet.
    
- The ground is wet.  
    ⟹ It **must be raining** ❌  
    (But maybe someone used a sprinkler!)
    

---

#### 🔻 **Denying the antecedent**

> Mistakenly thinking:  
> If **P → Q**, and **P is false**, then **Q is false** ❌

📌 Form:

- P → Q
    
- ¬P  
    ⟹ ¬Q ❌ (Invalid)
    

🔸 Example:

- If I study, I pass.
    
- I did not study.  
    ⟹ I did **not** pass ❌  
    (Maybe you still passed by luck!)


---


