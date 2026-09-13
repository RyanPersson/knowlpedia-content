+++
id = "shared-foundations/mathematical-proof"
title = "Mathematical proof"
kind = "definition"
summary = "A deduction from stated assumptions and axioms using specified inference rules."
aliases = ["proof"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/mathematical-proposition", "shared-foundations/mathematical-axiom", "shared-foundations/first-order-logic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **mathematical proof** is a deduction of a [[shared-foundations/mathematical-proposition|statement]] from specified hypotheses and [[shared-foundations/mathematical-axiom|axioms]] using accepted [[shared-foundations/first-order-logic|inference rules]]. In a formal proof, each step has an explicitly checkable justification. An ordinary written proof abbreviates such reasoning and may invoke previously established results.

## Dependency of a conclusion

An assumption remains a hypothesis of the conclusion unless it is discharged by an inference rule. For example, deriving \(Q\) under an additional assumption \(P\) proves \(P\Rightarrow Q\) after discharging \(P\). It does not prove \(Q\) without that condition.

## Parameters

To prove a universal statement, an introduced parameter must be arbitrary under the permitted assumptions. To prove existence, a constructed object must be shown to satisfy every asserted property. Numerical examples and plausibility arguments can guide a proof but do not replace these steps.

## References

- [John Stalker, Natural deduction for first-order logic](https://www.maths.tcd.ie/~stalker/2023-2024/11602/notes/5.9-natural-deduction-for-first-order-logic.html).
