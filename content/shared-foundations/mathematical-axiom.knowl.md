+++
id = "shared-foundations/mathematical-axiom"
title = "Mathematical axiom"
kind = "definition"
summary = "A nonlogical statement adopted as part of a mathematical theory."
aliases = ["axiom", "axiom schema"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/mathematical-proposition", "shared-foundations/first-order-logic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **axiom** of a mathematical theory is a [[shared-foundations/mathematical-proposition|statement]] adopted as an assumption of that theory. The theory's deductions use these assumptions together with its [[shared-foundations/first-order-logic|logical rules]]. An axiom need not be a theorem of a weaker theory; it may be provable in a different, stronger framework.

## Axiom schemas

An axiom schema is a specified pattern producing one axiom for each permitted formula. For example, separation in [[shared-foundations/zfc-axioms|ZFC]] is a schema indexed by first-order formulas with the required variable restrictions. The restrictions are part of the axiom data.

## Definitions

A definition introduces notation or specifies a property. It does not by itself guarantee that an object with that property exists. For instance, defining an empty set as one with no elements and asserting that an empty set exists have different logical roles.

## References

- [Jonathan Pila, Set Theory, Sections 2–9 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
