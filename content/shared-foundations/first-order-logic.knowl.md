+++
id = "shared-foundations/first-order-logic"
title = "First-order logic and inference rules"
kind = "definition"
summary = "Primitive logical syntax, quantifiers, equality, and rules for classical mathematical inference."
aliases = ["logical quantifier", "universal quantifier", "existential quantifier", "modus ponens"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = []
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

**First-order logic** specifies how statements are formed and how conclusions follow from assumptions. Variables stand for objects; a chosen language supplies relation symbols and, if needed, constants and function symbols. Atomic statements are equalities or applications of relation symbols. Formulas are built using
\[
\neg P,\quad P\land Q,\quad P\lor Q,\quad P\Rightarrow Q,
\quad \forall x\,P(x),\quad \exists x\,P(x).
\]
The quantifiers mean “for every object” and “there exists an object” in the domain of discourse. An occurrence of a variable is **bound** within its quantifier's scope and **free** otherwise. A formula with no free variables is a sentence. Substitution must avoid turning a free variable into a bound one.

## Inference rules

A classical natural-deduction presentation permits the following rules. Assumptions may be used while they remain open, and a discharged assumption is removed from the hypotheses of the resulting conclusion.

- From \(P,Q\), infer \(P\land Q\); from a conjunction, infer either component.
- From \(P\), infer \(P\lor Q\), and similarly from \(Q\). From \(P\lor Q\) and deductions of \(R\) from each alternative, infer \(R\).
- A deduction of \(Q\) under an additional assumption \(P\) gives \(P\Rightarrow Q\) after discharging \(P\). From \(P\) and \(P\Rightarrow Q\), infer \(Q\) (modus ponens).
- A deduction of contradiction under \(P\) gives \(\neg P\). From \(P,\neg P\), infer contradiction; from contradiction infer any formula. Classical logic also permits eliminating double negation.
- From \(\forall x\,P(x)\), infer \(P(t)\) for an admissible term \(t\). To infer \(\forall x\,P(x)\), prove the instance for an arbitrary object not occurring freely in undischarged assumptions.
- From \(P(t)\), infer \(\exists x\,P(x)\). To use an existential statement, introduce a fresh witness, deduce a conclusion independent of that witness, and discharge the witness assumption.
- Equality is reflexive, and equal terms may be substituted for one another in formulas.

These are foundational rules, not theorems requiring a prior mathematical structure. Particular theories add nonlogical axioms, such as those governing [[shared-foundations/set|sets]].

## Quantifier order

The statement \(\forall x\,\exists y\,P(x,y)\) allows the chosen \(y\) to depend on \(x\). The statement \(\exists y\,\forall x\,P(x,y)\) requires one choice valid for every \(x\). They need not be equivalent.

## References

- [Jonathan Pila, Set Theory, Sections 2–9 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
- [John Stalker, Natural deduction for first-order logic](https://www.maths.tcd.ie/~stalker/2023-2024/11602/notes/5.9-natural-deduction-for-first-order-logic.html).
