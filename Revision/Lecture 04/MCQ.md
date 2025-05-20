### Question 1:

Which of the following best describes a propositional function?

A. A statement whose truth value is fixed and does not depend on any variable  
B. A statement whose truth value depends on a variable or variables  
C. A logical connective combining two propositions  
D. A function mapping every real number to its square

<details> <summary>Answer</summary> B. A propositional function (or predicate) is a statement whose truth depends on the value(s) of one or more variables. </details>

---

### Question 2:

What is the standard way to express “there exists exactly one x such that P(x) holds”?

A. ∃x P(x)  
B. ∀x P(x)  
C. ∃!x P(x)  
D. ¬∃x P(x)

<details> <summary>Answer</summary> C. The uniqueness quantifier ∃!x P(x) denotes “there exists exactly one x making P(x) true.” </details>

---

### Question 3:

Which logical equivalence is valid for quantifiers?

A. ∀x (P(x) ∨ Q(x)) ≡ (∀x P(x)) ∨ (∀x Q(x))  
B. ∃x (P(x) ∧ Q(x)) ≡ (∃x P(x)) ∧ (∃x Q(x))  
C. ∀x (P(x) ∧ Q(x)) ≡ (∀x P(x)) ∧ (∀x Q(x))  
D. ∃x (P(x) ∨ Q(x)) ≡ (∃x P(x)) ∧ (∃x Q(x))

<details> <summary>Answer</summary> C. Universal quantification distributes over conjunction: ∀x(P∧Q) ≡ (∀xP)∧(∀xQ). </details>

---

### Question 4:

How would you translate the sentence “All students who got full marks got an A” into predicate logic?

A. ∃x (F(x) → A(x))  
B. ∀x (F(x) → A(x))  
C. ∀x (A(x) → F(x))  
D. ∃x (A(x) → F(x))

<details> <summary>Answer</summary> B. “All F imply A” is ∀x (F(x) → A(x)), where F(x) = “x got full marks” and A(x) = “x got an A.” </details>

---

### Question 5:

What is the correct negation of ∀x P(x)?

A. ∃x P(x)  
B. ¬∃x P(x)  
C. ∃x ¬P(x)  
D. ∀x ¬P(x)

<details> <summary>Answer</summary> C. By De Morgan’s for quantifiers: ¬∀x P(x) ≡ ∃x ¬P(x). </details>

---

### Question 6:

Which statement is **not** equivalent to “There exists an x > 0 such that x is odd”?

A. ∃x (x > 0 ∧ x mod 2 = 1)  
B. ∃x>0 (x mod 2 = 1)  
C. ∃x (x > 0 → x mod 2 = 1)  
D. There is some positive odd x

<details> <summary>Answer</summary> C. Using “→” would allow x ≤ 0 to satisfy the implication, so it’s incorrect for restricting the domain. </details>

---

### Question 7:

Which ordering of nested quantifiers makes the statement “for every x there exists y such that x + y = 0”?

A. ∃x ∀y (x + y = 0)  
B. ∀x ∃y (x + y = 0)  
C. ∃y ∀x (x + y = 0)  
D. ∀y ∃x (x + y = 0)

<details> <summary>Answer</summary> B. ∀x ∃y (x + y = 0) states that for each x, you can find a y (namely –x) making their sum zero. </details>

---

### Question 8:

In a discrete domain D={1,2,3}, ∃x P(x) is equivalent to:

A. P(1) ∧ P(2) ∧ P(3)  
B. P(1) ∨ P(2) ∨ P(3)  
C. ¬P(1) ∧ ¬P(2) ∧ ¬P(3)  
D. ¬P(1) ∨ ¬P(2) ∨ ¬P(3)

<details> <summary>Answer</summary> B. Existential quantification over {1,2,3} expands to a disjunction: P(1) ∨ P(2) ∨ P(3). </details>

---

### Question 9:

Which of these correctly shows that quantifiers bind tighter than ∨?

A. ∀x P(x) ∨ Q(x) ≡ ∀x (P(x) ∨ Q(x))  
B. ∀x P(x) ∨ Q(x) ≡ (∀x P(x)) ∨ Q(x)  
C. ∀x (P(x) ∨ Q(x)) ≡ (∀x P(x)) ∨ (∀x Q(x))  
D. ∀x (P(x) ∨ Q(x)) ≡ ∀x P(x) ∨ ∀x Q(x)

<details> <summary>Answer</summary> B. Without parentheses, ∀x P(x) ∨ Q(x) groups as (∀x P(x)) ∨ Q(x) because ∀ binds tighter than ∨. </details>

---

### Question 10:

In the matrix visualization for ∀x∃y P(x,y), what must each row contain?

A. All F’s  
B. At least one T  
C. All T’s  
D. Exactly one F

<details> <summary>Answer</summary> B. ∀x∃y requires that for every row (x), there exists at least one column (y) with truth T. </details>

---