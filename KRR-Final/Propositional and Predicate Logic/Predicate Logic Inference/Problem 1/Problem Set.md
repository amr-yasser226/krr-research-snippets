<!-- Problem1.md -->

# Problem 1: Tweety the Penguin

**Informal description**  
Tweety is a penguin.  All penguins are birds.  All birds can fly.  All penguins cannot fly.  Prove that Tweety cannot fly by refutation.

---

## 1. Translate in FOL

1. Penguin(Tweety)  
2. ∀x [Penguin(x) → Bird(x)]  
3. ∀x [Bird(x) → Fly(x)]  
4. ∀x [Penguin(x) → ¬Fly(x)]  
5. Goal: ¬Fly(Tweety)

---

## 2. Negate the Goal and add to KB

6. ¬¬Fly(Tweety)  ⟶  Fly(Tweety)

---

## 3. Convert all to CNF

1. Penguin(Tweety)  
2. ¬Penguin(x) ∨ Bird(x)  
3. ¬Bird(y) ∨ Fly(y)  
4. ¬Penguin(z) ∨ ¬Fly(z)  
5. Fly(Tweety)

---

## 4. Standardize variables (they’re already all distinct)

*(no change)*

---

## 5. Remove ∀, ∃

*(all are universal)*

---

## 6. Final KB for Resolution

1. Penguin(Tweety)  
2. ¬Penguin(x) ∨ Bird(x)  
3. ¬Bird(y) ∨ Fly(y)  
4. ¬Penguin(z) ∨ ¬Fly(z)  
5. Fly(Tweety)  
