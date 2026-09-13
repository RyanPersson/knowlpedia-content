+++
id = "asymptotics/quadratic-self-interaction"
title = "Quadratic self-interaction"
kind = "definition"
summary = "The quadratic term involving a perturbation with itself in an exact expansion."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["algebra-modules/bilinear-map", "linear-algebra/quadratic-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[algebra-modules/bilinear-map|bilinear map]] \(B\), set \(Q(v)=B(v,v)\). The **quadratic self-interaction** of an increment \(w\) is \(B(w,w)\), as seen in
\[
Q(u+w)=Q(u)+B(u,w)+B(w,u)+B(w,w).
\]
The two middle terms are interactions with the background. Symmetry of \(B\) is not assumed; symmetrizing it leaves \(Q\) unchanged.

## Fluid example

For \(B(v,w)=(v\cdot\nabla)w\), self-interaction is \((w\cdot\nabla)w\). If \(w\) is divergence free, this equals \(\nabla\cdot(w\otimes w)\). An oscillatory or geometric construction may cancel selected components or averages; that does not establish cancellation of the full expression without a calculation.
