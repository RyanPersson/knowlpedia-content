+++
id = "complex-analysis/schwarzian-and-second-order-linear-odes"
title = "Schwarzian derivative and second-order linear ODEs"
kind = "theorem"
summary = "Ratios of independent solutions of a second-order linear equation have prescribed Schwarzian."
aliases = ["Schwarzian ODE correspondence"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["topology/simply-connected-space", "complex-analysis/schwarzian-derivative", "complex-analysis/schwarzian-chain-rule", "complex-analysis/meromorphic-function", "complex-analysis/mobius-transformation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be [[topology/simply-connected-space|simply connected]], let \(q\) be holomorphic on \(D\), and let \(y_1,y_2\) be linearly independent solutions of
\[
y''+\frac12q\,y=0.
\]
Then the meromorphic map
\[
f=\frac{y_1}{y_2}:D\longrightarrow\widehat{\mathbb C}
\]
is locally univalent and has [[complex-analysis/schwarzian-derivative|Schwarzian derivative]]
\[
S(f)=q.
\]

## Basis independence

Replacing \((y_1,y_2)\) by another basis of the two-dimensional solution space postcomposes \(f\) by a [[complex-analysis/mobius-transformation|Möbius transformation]]. The [[complex-analysis/schwarzian-chain-rule|Schwarzian chain rule]] therefore makes \(S(f)\) independent of the chosen solution basis.

## Converse

Locally, every locally univalent [[complex-analysis/meromorphic-function|meromorphic function]] \(f\) arises as such a ratio with \(q=S(f)\). One may take
\[
y_2=(f')^{-1/2},
\qquad
y_1=f(f')^{-1/2}
\]
after choosing a local square root. This correspondence explains why solutions of the Schwarzian equation \(S(f)=q\) are unique up to Möbius postcomposition.

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
2. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective connections and second-order differential equations.
