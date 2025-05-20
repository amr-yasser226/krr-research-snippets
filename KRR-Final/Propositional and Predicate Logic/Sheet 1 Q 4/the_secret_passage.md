## 4. The Secret Passage

In a medieval castle, there was said to be a hidden passage leading to a hidden treasure. Sherlock came across the following clues:

> "The hidden passage can only be accessed if the torch is lit and the lever is pulled. The torch is not lit."

Using propositional logic, determine if the hidden passage can be accessed.

---

### Propositional Variables

Let:

* $P$: The hidden passage can be accessed.
* $T$: The torch is lit.
* $L$: The lever is pulled.

### Logical Expression

The clue "The hidden passage can only be accessed if the torch is lit and the lever is pulled" translates to:

$$
P \leftrightarrow (T \land L)
$$

Additionally, we know:

$$
\lnot T
$$

### Truth Table

| $P$ | $T$ | $L$ | $T \land L$ | $P \leftrightarrow (T \land L)$ |
| :-: | :-: | :-: | :---------: | :-----------------------------: |
|  T  |  T  |  T  |      T      |                T                |
|  T  |  T  |  F  |      F      |                F                |
|  T  |  F  |  T  |      F      |                F                |
|  T  |  F  |  F  |      F      |                F                |
|  F  |  T  |  T  |      T      |                F                |
|  F  |  T  |  F  |      F      |                T                |
|  F  |  F  |  T  |      F      |                T                |
|  F  |  F  |  F  |      F      |                T                |

### Analysis

From the truth table, $P \leftrightarrow (T \land L)$ is true exactly when:

* $T \land L$ is true and $P$ is true, or
* $T \land L$ is false and $P$ is false.

However, we are given that $\lnot T$ (the torch is not lit), which makes $T \land L$ false regardless of the value of $L$.

Thus, for the equivalence to hold, $P$ must also be false.

### Conclusion

Since $P$ is false under the given condition (the torch is not lit), **the hidden passage cannot be accessed**.
