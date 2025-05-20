## Predicate Logic & Inference

### Inference in First-Order Logic (FOL)

* Propositional inference rules (e.g., Modus Ponens) extend to FOL.
* FOL‐specific rules:

  * **Unification**: find substitutions making two atoms identical
  * **Resolution**: convert formulas to clause form (CNF) and resolve complementary literals
  * **Refutation by Resolution**: assume ¬goal, derive contradiction

### Matching / Substitution

* Match predicate expressions via variable–variable or variable–constant substitutions.
* Examples:

  * `P(x)` vs. `P(y)` → `{y/x}`
  * `Q(x,x)` vs. `Q(y,z)` → `{y/x, z/x}`
  * `P(f(x), z)` vs. `P(y, Fido)` → `{y/f(x), z/Fido}`

### Unification Algorithm

* **UNIFY(A₁, A₂)** returns the Most General Unifier (MGU) or FAIL.
* MGU examples:

  * `UNIFY(King(x), King(John))` → `{x/John}`
  * `UNIFY(f(x,g(y)), f(g(Z), U))` → `{x/g(Z), U/g(y)}`

### Inference Rules for Quantifiers

* **Universal Generalization (UG)**: from P(e) for arbitrary e ⇒ ∀x P(x).
* **Universal Instantiation (UI)**: from ∀x P(x) ⇒ P(e) for any specific e.
* **Existential Generalization (EG)**: from P(e) for some e ⇒ ∃x P(x).
* **Existential Instantiation (EI)**: from ∃x P(x) ⇒ introduce new symbol e, infer P(e).

### Modus Ponens in FOL

1. ∀X (student(X) → studyAI(X))
2. student(Ahmed)
   ⊢ studyAI(Ahmed)

* Apply UI on (1) to get `student(Ahmed) → studyAI(Ahmed)`, then MP with (2).

### Worked Examples

1. **Every man is nice; Ali is a man ⇒ Ali is nice**

   * ∀x (M(x)→L(x)), M(Ali) ⟹ L(Ali)
2. **∃ someone in class hasn’t read; ∀ in class passed ⇒ ∃ someone who passed and hasn’t read**

   * ∃x(C(x)∧¬B(x)), ∀x(C(x)→P(x))
   * Use EI, UI, MP, EG to derive ∃x(P(x)∧¬B(x))

### Resolution Method in FOL

1. Convert KB + ¬goal into CNF clauses.
2. Find complementary literals, unify, and resolve to generate new clauses.
3. Derive the empty clause (⊥) to prove the goal.

### CNF Conversion Recipe

1. **Eliminate implications**: (P→Q) ≡ (¬P ∨ Q)
2. **Move negations inward** (De Morgan’s, quantifier rules)
3. **Standardize variables**: unique names for each quantifier
4. **Skolemize**: replace ∃ with Skolem constants/functions
5. **Drop ∀ quantifiers** (all vars now implicitly universal)
6. **Distribute ∨ over ∧** to achieve CNF
7. **Split conjunctions** into separate clauses
8. **Standardize apart**: ensure no clause shares variable names

### Conversion Examples

* `∀x (P(x) ∧ Q(x)) → R(x)` ⇒ `¬P(x) ∨ ¬Q(x) ∨ R(x)`
* `∀x (Person(x) → ∃y (…))` ⇒ illustrate Skolem function S(x)
