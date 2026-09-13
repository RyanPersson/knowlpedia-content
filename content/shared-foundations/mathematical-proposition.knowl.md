+++
id = "shared-foundations/mathematical-proposition"
title = "Mathematical proposition"
kind = "definition"
summary = "A statement considered under specified hypotheses, with a truth value in an interpretation."
aliases = ["proposition", "mathematical statement"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/first-order-logic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **mathematical proposition** is a statement considered under specified hypotheses. In classical logic it has a truth value once the meanings of its symbols and any free parameters are fixed. A sentence has no free variables; a formula such as \(x=x\) has a free variable until it is assigned a value or quantified.

## Hypotheses and quantifiers

The conditional proposition \(P\Rightarrow Q\) says that \(Q\) follows whenever \(P\) holds. Proving that conditional does not prove its hypothesis \(P\). Similarly, \(\forall x\exists y\,R(x,y)\) permits a different witness for each \(x\), whereas \(\exists y\forall x\,R(x,y)\) requires a common witness.

## Role in exposition

A result called “Proposition” is usually a proved statement; its heading alone is not evidence of a [[shared-foundations/mathematical-proof|proof]]. The logical content comes from its complete hypotheses, quantifiers and conclusion.

## References

- [Jonathan Pila, Set Theory, Sections 2–9 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
