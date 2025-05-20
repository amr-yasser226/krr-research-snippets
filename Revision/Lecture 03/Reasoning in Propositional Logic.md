## Rules of Inference

- Abstraction of valid argument forms so we don’t need full truth tables
    
- Build complex arguments by chaining simpler, proven inference rules
    

## Modus Ponens (Law of Detachment)

- **Form:**
    
    1. _p_
        
    2. _p_ → _q_
        
    3. ∴ _q_
        
- **Intuition:** If “_p_ implies _q_” and _p_ is true, then _q_ must be true
    
- **Derivation Sketch:**
    
    - Start with `(p ∧ (p → q)) → q`
        
    - Rewrite `p → q` as `¬p ∨ q`, distribute, simplify to a tautology
        

## Other Common Inference Rules

1. **Modus Tollens**
    
    - _¬q_, _p_ → _q_ ⟹ _¬p_
        
2. **Hypothetical Syllogism**
    
    - _p_ → _q_, _q_ → _r_ ⟹ _p_ → _r_
        
3. **Disjunctive Syllogism**
    
    - _p_ ∨ _q_, ¬_p_ ⟹ _q_
        
4. **Addition**
    
    - _p_ ⟹ _p_ ∨ _q_
        
5. **Simplification**
    
    - _p_ ∧ _q_ ⟹ _p_
        
6. **Conjunction**
    
    - _p_, _q_ ⟹ _p_ ∧ _q_
        
7. **Resolution**
    
    - _p_ ∨ _q_, ¬_p_ ∨ _r_ ⟹ _q_ ∨ _r_
        

## Quick Applications

- **Modus Tollens Example:**
    
    - If George doesn’t have eight legs → not a spider; George is a spider ⟹ George has eight legs
        
- **Identify by Form:**
    
    1. Kangaroos live in Australia _and_ are marsupials ⟹ Kangaroos are marsupials (Simplification)
        
    2. Either hot > 100° or pollution dangerous; it’s not > 100° ⟹ Pollution is dangerous (Disjunctive Syllogism)
        
    3. Linda swims well; if she swims well → lifeguard ⟹ She can be lifeguard (Modus Ponens)
        
    4. Steve will work at a tech company this summer ⟹ He’ll either work there or be beach bum (Addition)
        
    5. If work all night → answer exercises; answer exercises → understand material ⟹ If work all night → understand (Hypothetical Syllogism)
        

## Building Multi-Premise Arguments

- Chain several inference steps
    
- **Example:**
    
    1. ¬R ∨ ¬G → S ∧ D
        
    2. S → P
        
    3. ¬P
        
    4. ∴ R ∧ G ∧ ... ∴ R (It rained)
        

## Automated Resolution

- **Clauses:**
    
    1. ¬R ∨ U ("It’s not raining or Yvette has umbrella")
        
    2. ¬U ∨ ¬W ("If she has umbrella then she doesn’t get wet")
        
    3. R ∨ ¬W ("If it’s raining then she doesn’t get wet")
        
- **Resolution Steps:**
    
    1. From (1) & (2) derive ¬R ∨ ¬W
        
    2. With (3), derive ¬W (“Yvette does not get wet”)
        