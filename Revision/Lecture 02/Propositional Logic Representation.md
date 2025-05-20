## Logical Representation
- Logic leverages hardware-native operations for efficient reasoning.
- Knowledge is represented as propositions (true/false statements).

## 1. Propositional Logic

### 1.1 Propositions
- **Proposition**: declarative sentence, either true (T) or false (F).
- Variables: P, Q, R, …
- **Compound propositions** combine atoms via logical connectives.

### 1.2 Basic Connectives
- **Negation**: `¬P` (true iff P is false)
- **Conjunction** (AND): `P ∧ Q` (true iff both P and Q are true)
- **Disjunction** (OR): `P ∨ Q` (inclusive OR; true if ≥ 1 true)
- **Exclusive OR**: `P ⊕ Q` (true iff exactly one is true)

### 1.3 Conditional Statements
- **Implication**: `P → Q` (“if P then Q”; false only when P=T and Q=F)
  - Antecedent = P; Consequent = Q
  - Does **not** imply causation
- **Related forms**:
  - **Converse**: `Q → P` (≠ `P → Q`)
  - **Inverse**: `¬P → ¬Q` (≠ `P → Q`)
  - **Contrapositive**: `¬Q → ¬P` (≡ `P → Q`)

### 1.4 Biconditional
- `P ↔ Q` (true iff P and Q have same truth value)
- Read as “P if and only if Q”

### 1.5 Truth Tables
- Enumerate all combinations of truth values
- Example:  

(P ∨ ¬Q) → (P ∧ Q)

|p|q|¬q|p∨¬q|p∧q|(p∨¬q)→(p∧q)|
|---|---|---|---|---|---|
|T|T|F|T|T|T|
|T|F|T|T|F|F|
|F|T|F|F|F|T|
|F|F|T|T|F|F|

### 1.6 Operator Precedence
1. `¬`  
2. `∧`  
3. `∨`  
4. `→`  
5. `↔`

### 1.7 Logic ↔ Bit Operations
- True/False ↔ 1/0
- Logic gates map to bitwise operators

### Key Exercises
1. Show `(P ∨ ¬Q) ∧ (Q ∨ ¬R) ∧ (R ∨ ¬P)` true only when P=Q=R.
2. “This statement is false” is **not** a proposition (paradox).
3. Barber paradox (`P ↔ Q`) has no consistent assignment.

## 2. Applications of Propositional Logic
1. **Translating English**  
 - E.g., “Access Internet only if CS major or not freshman”  
   `A → (C ∨ ¬F)`
2. **System Specifications**  
 - Translate requirements; check consistency  
 - E.g., `{P∨Q, ¬P, Q→P}` is inconsistent
3. **Boolean Searches**  
 - AND, OR, NOT in information retrieval
4. **Logic Puzzles**  
 - E.g., muddy children puzzle: first “No”, then “Yes”
5. **Logic Circuits**  
 - Design digital circuits with AND, OR, NOT gates

## 3. Propositional Equivalences

### 3.1 Definitions
- **Tautology**: always true (e.g., `P ∨ ¬P`)
- **Contradiction**: always false (e.g., `P ∧ ¬P`)
- **Contingency**: neither tautology nor contradiction

### 3.2 Logical Equivalence
- `P ≡ Q` if `P ↔ Q` is a tautology

#### Important Laws
- **Identity**: `P ∧ T ≡ P`; `P ∨ F ≡ P`
- **Domination**: `P ∨ T ≡ T`; `P ∧ F ≡ F`
- **Idempotent**: `P ∧ P ≡ P`; `P ∨ P ≡ P`
- **Double negation**: `¬(¬P) ≡ P`
- **Commutative**: `P ∧ Q ≡ Q ∧ P`; `P ∨ Q ≡ Q ∨ P`
- **Associative**: `(P∧Q)∧R ≡ P∧(Q∧R)`; `(P∨Q)∨R ≡ P∨(Q∨R)`
- **Distributive**:  
- `P ∧ (Q∨R) ≡ (P∧Q)∨(P∧R)`  
- `P ∨ (Q∧R) ≡ (P∨Q)∧(P∨R)`
- **Absorption**: `P ∨ (P∧Q) ≡ P`; `P ∧ (P∨Q) ≡ P`
- **Negation laws**: `P ∨ ¬P ≡ T`; `P ∧ ¬P ≡ F`

#### With Conditionals & Biconditionals
- `P → Q ≡ ¬P ∨ Q`
- `P ↔ Q ≡ (P→Q) ∧ (Q→P) ≡ (P∧Q) ∨ (¬P∧¬Q)`

### 3.3 Iterative Notation
- `∨ⁿᵢ=1 pi = p1 ∨ p2 ∨ … ∨ pn`
- `∧ᵐⱼ=1 pj = p1 ∧ p2 ∧ … ∧ pm`

### 3.4 Constructing Equivalences
- Combine known laws to prove new ones  
E.g., `(P→Q)∧(P→R) ≡ P→(Q∧R)`

### 3.5 Propositional Satisfiability
- **Satisfiable**: some assignment makes it true
- **Unsatisfiable**: no assignment makes it true
- Check via truth tables or simplification
- E.g., adding conflicting clauses → unsatisfiable