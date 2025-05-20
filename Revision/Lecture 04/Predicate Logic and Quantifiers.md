## Predicates & Propositional Functions

- **Predicate**: P(x) is a statement whose truth depends on the variable x (e.g., “x > 3”).
    
    - Example: P(4) = T, P(2) = F
        
- **n‑place predicate**: P(x₁,…,xₙ) is a proposition over an n‑tuple.
    
- **Use in programs**: Evaluating conditions, preconditions, postconditions (e.g., swap algorithm).
    

## Quantifiers

- **Universal (∀)**: ∀x P(x) holds if P(x) is true for every x in domain D.
    
    - Finite D={x₁,…,xₙ}: ∀x P(x) ≡ P(x₁) ∧ … ∧ P(xₙ)
        
- **Existential (∃)**: ∃x P(x) holds if there is at least one x in D making P(x) true.
    
    - Finite D: ∃x P(x) ≡ P(x₁) ∨ … ∨ P(xₙ)
        
- **Uniqueness (∃!)**: Exactly one x in D satisfies P(x).
    

## Restricted Domains

- **Syntax**: Add domain restriction inside quantifier or as conjunction/implication.
    
    - ∀x<0 … ≡ ∀x (x<0 → …)
        
    - ∃x>0 … ≡ ∃x (x>0 ∧ …)
        

## Precedence & Binding

- Quantifiers bind tighter than ∧, ∨, →, ¬.
    
    - ∀x P(x) ∨ Q(x) ≡ (∀x P(x)) ∨ Q(x)
        
- **Bound variable**: Variable under quantifier.
    
- **Free variable**: Not bound by any quantifier.
    

## Logical Equivalences

- ∀x (P(x) ∧ Q(x)) ≡ (∀x P(x)) ∧ (∀x Q(x))
    
- ∃x (P(x) ∨ Q(x)) ≡ (∃x P(x)) ∨ (∃x Q(x))
    
- De Morgan’s for quantifiers:
    
    - ¬∀x P(x) ≡ ∃x ¬P(x)
        
    - ¬∃x P(x) ≡ ∀x ¬P(x)
        

## Translating English ↔ Logic

- Identify predicates and domain.
    
- Map “All F imply A” → ∀x (F(x) → A(x)).
    
- Map “There exists x such that…” → ∃x (…).
    

## Nested Quantifiers & Order

- Order matters when mixing ∀ and ∃: ∀x∃y P(x,y) ≠ ∃y∀x P(x,y).
    
- Computational pattern:
    
    - For ∀: assume true then search for counterexample.
        
    - For ∃: assume false then search for witness.
        

## Two‑Variable Quantifications

|Structure|True when…|False when…|
|---|---|---|
|∀x∀y P(x,y)|every pair satisfies P|some pair fails P|
|∀x∃y P(x,y)|∀x has at least one y making P true|∃x with no y making P true|
|∃x∀y P(x,y)|some x works for all y|every x fails for some y|
|∃x∃y P(x,y)|at least one pair makes P true|no pair makes P true|

## Matrix Visualization (Discrete x,y)

- Represent x values as rows and y values as columns; each cell is truth of P(x,y).
    
- **∀x∀y**: all cells T
    
- **∀x∃y**: each row has a T
    
- **∃x∀y**: some row all T
    
- **∃x∃y**: at least one T anywhere