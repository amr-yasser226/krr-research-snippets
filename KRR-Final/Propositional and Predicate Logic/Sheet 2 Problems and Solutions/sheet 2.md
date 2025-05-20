# Sheet 2: Problems & Solutions

## Q1. Rewrite each of the following statements in the form “∀… x, …” or “∃… x such that …”

**a)** *Problem:* All dinosaurs are extinct.
*Solution:*

```text
∀x (Dinosaur(x) → Extinct(x))
```

**b)** *Problem:* Every real number is positive, negative, or zero.
*Solution:*

```text
∀x (Real(x) → [Positive(x) ∨ Negative(x) ∨ Zero(x)])
```

**c)** *Problem:* No logicians are lazy.
*Solution:*

```text
∀x (Logician(x) → ¬Lazy(x))
```

(Alternatively: ¬∃x (Logician(x) ∧ Lazy(x))).

**d)** *Problem:* Some exercises have answers.
*Solution:*

```text
∃x (Exercise(x) ∧ HasAnswer(x))
```

**e)** *Problem:* There is a student in DSAI 104.
*Solution:*

```text
∃x (Student(x) ∧ EnrolledIn(x, DSAI104))
```

---

## Q2. Let P(x) be the statement “x spends more than five hours every weekday in class,” where the domain for x consists of all students. Express each of these quantifications in English.

**a)** *Problem:* ∃x P(x)
*Solution:* “There exists a student who spends more than five hours every weekday in class.”

**b)** *Problem:* ∀x P(x)
*Solution:* “Every student spends more than five hours every weekday in class.”

**c)** *Problem:* ∃x ¬P(x)
*Solution:* “There exists a student who does not spend more than five hours every weekday in class.”

**d)** *Problem:* ∀x ¬P(x)
*Solution:* “No student spends more than five hours every weekday in class.”

---

## Q3. Translate these statements into English, where C(x) is “x is a comedian” and F(x) is “x is funny” and the domain consists of all people.

**a)** *Problem:* ∀x (C(x) → F(x))
*Solution:* “For every person, if they are a comedian then they are funny.”

**b)** *Problem:* ∀x (C(x) ∧ F(x))
*Solution:* “Every person is both a comedian and funny.”

**c)** *Problem:* ∃x (C(x) → F(x))
*Solution:* “There exists a person such that if they are a comedian then they are funny.”
*(Vacuously true if that person isn’t a comedian.)*

**d)** *Problem:* ∃x (C(x) ∧ F(x))
*Solution:* “There is at least one person who is both a comedian and funny.”

---

## Q4. Suppose that the domain of the propositional function P(x) consists of the integers 1, 2, 3, 4, and 5. Express these statements without using quantifiers, instead using only negations, disjunctions, and conjunctions.

**a)** *Problem:* ∃x P(x)
*Solution:*

```text
P(1) ∨ P(2) ∨ P(3) ∨ P(4) ∨ P(5)
```

**b)** *Problem:* ∀x P(x)
*Solution:*

```text
P(1) ∧ P(2) ∧ P(3) ∧ P(4) ∧ P(5)
```

**c)** *Problem:* ¬∃x P(x)
*Solution:*

```text
¬[P(1) ∨ P(2) ∨ P(3) ∨ P(4) ∨ P(5)]
```

(Equivalent to ¬P(1) ∧ ¬P(2) ∧ ¬P(3) ∧ ¬P(4) ∧ ¬P(5)).

---

## Q5. Let Q(x, y) be the statement “x has sent an e‑mail message to y,” where the domain for both x and y consists of all students in your class. Express each of these quantifications in English.

**a)** *Problem:* ∃x ∃y Q(x,y)
*Solution:* “There exist two (possibly the same) students such that one has sent an e‑mail to the other.”

**b)** *Problem:* ∃x ∀y Q(x,y)
*Solution:* “There is a student who has sent an e‑mail to every student in the class.”

**c)** *Problem:* ∀x ∃y Q(x,y)
*Solution:* “Every student has sent an e‑mail to at least one student.”

**d)** *Problem:* ∃y ∀x Q(x,y)
*Solution:* “There is a student who has received e‑mails from every student.”

**e)** *Problem:* ∀y ∃x Q(x,y)
*Solution:* “For every student, there is someone who has sent them an e‑mail.”

**f)** *Problem:* ∀x ∀y Q(x,y)
*Solution:* “Every student has sent an e‑mail to every other student.”

---

## Q6. Use quantifiers and predicates with more than one variable to express these statements.

**a)** *Problem:* Every computer science student needs a course in Knowledge Representation and Reasoning.
*Solution:*

```text
∀s [CSStudent(s) → NeedsCourse(s, KR&R)]
```

**b)** *Problem:* There is a student in this class who owns a personal computer.
*Solution:*

```text
∃s [InClass(s) ∧ Owns(s, PC)]
```

**c)** *Problem:* Every student in this class has taken at least one computer science course.
*Solution:*

```text
∀s [InClass(s) → ∃c (CSCourse(c) ∧ Taken(s, c))]
```

**d)** *Problem:* There is a student in this class who has taken at least one course in computer science.
*Solution:*

```text
∃s [InClass(s) ∧ ∃c (CSCourse(c) ∧ Taken(s, c))]
```

---

## Q7. What rule of inference is used in each of these arguments?

**1.** *Problem:* Alice is a mathematics major. Therefore, Alice is either a mathematics major or a computer science major.
*Solution:* Addition (Disjunction Introduction).

**2.** *Problem:* Jerry is a mathematics major and a computer science major. Therefore, Jerry is a mathematics major.
*Solution:* Simplification (Conjunction Elimination).

**3.** *Problem:* If it is rainy, then the pool will be closed. It is rainy. Therefore, the pool is closed.
*Solution:* Modus Ponens.

**4.** *Problem:* “Doug, a student in this class, knows how to write programs in JAVA. Everyone who knows how to write programs in JAVA can get a high-paying job. Therefore, someone in this class can get a high-paying job.”
*Solution:* Universal Instantiation + Modus Ponens + Existential Generalization.

**5.** *Problem:* “Somebody in this class enjoys whale watching. Every person who enjoys whale watching cares about ocean pollution. Therefore, there is a person in this class who cares about ocean pollution.”
*Solution:* Existential Instantiation + Universal Instantiation + Modus Ponens + Existential Generalization.

**6.** *Problem:* “Each of the 93 students in this class owns a personal computer. Everyone who owns a personal computer can use a word processing program. Therefore, Zeke, a student in this class, can use a word processing program.”
*Solution:* Universal Instantiation + Modus Ponens.
