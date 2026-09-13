+++
id = "differential-equations/scalar-damping-factorization"
title = "Factoring scalar damping from a matrix evolution"
kind = "lemma"
summary = "A scalar damping term can be removed exactly by an integrating factor even when matrix coefficients do not commute."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/fundamental-matrix", "differential-equations/integrating-factor", "linear-algebra/matrix"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(U(t,s)\) be the [[differential-equations/fundamental-matrix|propagator]] of \(z'=A(t)z\), and let \(d(t)\) be a continuous scalar. The propagator for \(z'=(A(t)-d(t)I)z\) is
\[
V(t,s)=\exp\left(-\int_s^t d(r)\,dr\right)U(t,s).
\]
Differentiating this product proves the identity and the initial condition \(V(s,s)=I\). No commutation between \(A(t)\) at different times is needed, because the damping factor is scalar.

## Harmonics

If \(V_m\) corresponds to \(A-m^2dI\), then
\[
V_m(t,s)=\exp\left(-(m^2-1)\int_s^t d(r)\,dr\right)V_1(t,s).
\]
For \(d\ge0\), \(t\ge s\), and \(|m|\ge1\), higher harmonics have no larger propagator norm than the first harmonic under this comparison.
