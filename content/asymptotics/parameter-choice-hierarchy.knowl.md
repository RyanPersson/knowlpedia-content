+++
id = "asymptotics/parameter-choice-hierarchy"
title = "Hierarchy of parameter choices"
kind = "definition"
summary = "An ordered choice of small or large parameters that makes the permitted dependencies explicit."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/first-order-logic", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **hierarchy of parameter choices** specifies which constants are fixed before later ones are selected. A statement such as \(0<\alpha\ll\beta\ll1\) is shorthand, not a numerical relation: first choose \(\beta\) sufficiently small for the fixed data, then choose \(\alpha\) sufficiently small depending on those data and on \(\beta\).

## Quantifier order

One precise form is
\[
\exists\beta_*>0\;\forall\beta\in(0,\beta_*)\;
\exists\alpha_*(\beta)>0\;\forall\alpha\in(0,\alpha_*(\beta)):\ P(\alpha,\beta).
\]
The [[shared-foundations/first-order-logic|quantifiers]] forbid choosing \(\beta\) in response to \(\alpha\). Large parameters can be handled by making their reciprocals small. A proof must exhibit or justify compatible thresholds; the symbol \(\ll\) alone supplies none.
