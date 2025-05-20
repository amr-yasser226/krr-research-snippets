---
author: Amr Yasser
title: Predicate Translator – Mini Project 2
---

## Table of Contents

1. [Introduction](#introduction)  
2. [Problem Statement](#problem-statement)  
3. [Methodology](#methodology)  
4. [Results](#results)  
5. [Discussion](#discussion)  
6. [Conclusion](#conclusion)  
7. [Recommendations](#recommendations)  

---

## Introduction

A bidirectional translator for simple English quantifier statements ↔ first-order predicate logic. Handles “All X are Y,” “Some X are not Y,” “No X are Y,” etc., converting back and forth.

## Problem Statement

Manual translation of quantifiers (`∀`, `∃`) is error-prone. Automate:

- **English → Logic:** “all/every/each X are Y,” “some/a/an X are (not) Y,” “no/none X are Y.”  
- **Logic → English:** `∀x (is_X(x) → [¬]is_Y(x))` and `∃x (is_X(x) ∧ [¬]is_Y(x))`.

## Methodology

1. **Parse English:**  
   - Lowercase & tokenize.  
   - Detect quantifier (`all`, `some`, `no`).  
   - Identify negation (`not`).  
   - Map to predicates: `is_subject(x)`, `is_property(x)`.  
2. **Parse Logic:**  
   - Detect `∀x` vs `∃x`.  
   - Split on `→` (universal) or `∧` (existential).  
   - Extract subject/property and `¬` if present.  
   - Reconstruct phrase.  
3. **Testing:**  
   | English Input                | Logic Output                                    |
   |------------------------------|-------------------------------------------------|
   | All dinosaurs are extinct    | `∀x (is_dinosaur(x) → is_extinct(x))`           |
   | Some animals are endangered  | `∃x (is_animal(x) ∧ is_endangered(x))`          |
   | No dinosaurs are alive       | `∀x (is_dinosaur(x) → ¬is_alive(x))`            |

And reverse translations to English.

## Results

All six predefined tests passed:

| Direction        | Input                                 | Expected                                      | Result                                        | Pass |
|------------------|---------------------------------------|-----------------------------------------------|-----------------------------------------------|:----:|
| English → Logic  | All dinosaurs are extinct             | ∀x (is_dinosaur(x) → is_extinct(x))           | ∀x (is_dinosaur(x) → is_extinct(x))           |  ✅  |
| …                | …                                     | …                                             | …                                             |  …   |
| Logic → English  | ∃x (is_animal(x) ∧ is_endangered(x))  | some animals are endangered                   | some animals are endangered                   |  ✅  |

*(Omitted duplicate rows for brevity.)*

## Discussion

- **Robustness:** Good for single-word subjects/properties and simple negation.  
- **Limitations:**  
  - No support for nested/compound quantifiers.  
  - Irregular plurals may be mis-handled.  
- **Error handling:** Clear messages when input is malformed.

## Conclusion

The translator correctly automates the basic English–logic conversions for quantifiers. All tests succeeded.

## Recommendations

- **Multi-word support:** e.g., “large mammals.”  
- **Complex logic:** Add `∨`, `↔`, nested quantifiers.  
- **Internationalization:** Plug in other natural languages.

