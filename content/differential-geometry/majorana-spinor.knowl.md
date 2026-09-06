+++
id = "differential-geometry/majorana-spinor"
title = "Majorana spinor"
kind = "definition"
summary = "A complex spinor fixed by a compatible Spin-equivariant real structure."
aliases = ["Majorana condition"]
domains = ["differential-geometry", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/spinor-module", "mathematical-physics/gamma-matrices"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\Delta\) be a complex
[[differential-geometry/spinor-module|spinor module]] for
\(\operatorname{Spin}(p,q)\). A **real structure** on \(\Delta\) is an
antilinear \(\operatorname{Spin}(p,q)\)-equivariant map
\[
J:\Delta\longrightarrow\Delta
\qquad\text{with}\qquad
J^2=\operatorname{id}_\Delta.
\]
Relative to such a structure, a **Majorana spinor** is a spinor
\(\psi\in\Delta\) satisfying
\[
J\psi=\psi.
\]
Equivalently, it is an element of the real form
\(\Delta^J\subset\Delta\).

The existence and type of an equivariant antilinear structure depend on the
dimension, signature, and Clifford sign convention. An antilinear
equivariant map with \(J^2=-1\) is a quaternionic structure, not a Majorana
real structure in the sense above.

The Majorana condition is invariantly a reality condition on the
representation. It is not the basis-dependent assertion that the coordinates
of a spinor, or all of its [[mathematical-physics/gamma-matrices|gamma matrices]], are real.

## References

1. Pierre Deligne, “Notes on spinors,” in *Quantum Fields and Strings: A
   Course for Mathematicians*, Volume 1, American Mathematical Society, 1999,
   pp. 99–135.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
