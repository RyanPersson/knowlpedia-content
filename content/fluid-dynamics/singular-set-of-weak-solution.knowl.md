+++
id = "fluid-dynamics/singular-set-of-weak-solution"
title = "Singular set of a weak velocity"
kind = "definition"
summary = "The space-time points with no neighborhood on which the velocity is essentially bounded."
aliases = ["Navier–Stokes singular set"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/weak-navier-stokes-solution", "measure-theory/essential-supremum", "topology/parabolic-metric"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[fluid-dynamics/weak-navier-stokes-solution|weak velocity]] on an open space-time set \(Q\), call \(z\in Q\) **regular in the local boundedness sense** if \(u\) is [[measure-theory/essential-supremum|essentially bounded]] on some neighborhood of \(z\) contained in \(Q\). The **singular set** \(S(u)\) is the complement of these regular points. Neighborhoods may be taken as balls for the [[topology/parabolic-metric|parabolic metric]].

## Regularity convention

The regular set is open and the singular set is relatively closed. Partial regularity statements must specify their regularity convention. Turning boundedness into further smoothness uses an equation-specific theorem and force and pressure hypotheses; it is not part of this set-theoretic definition.
