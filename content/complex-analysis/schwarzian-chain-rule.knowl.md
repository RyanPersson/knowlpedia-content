+++
id = "complex-analysis/schwarzian-chain-rule"
title = "Schwarzian chain rule"
kind = "theorem"
summary = "The Schwarzian derivative obeys a quadratic-differential cocycle rule under composition."
aliases = ["chain rule for the Schwarzian derivative"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["complex-analysis/schwarzian-derivative"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(f\) and \(g\) be locally univalent holomorphic maps for which the composite \(f\circ g\) is defined. Their [[complex-analysis/schwarzian-derivative|Schwarzian derivatives]] satisfy
\[
S(f\circ g)
=\bigl(S(f)\circ g\bigr)(g')^2+S(g).
\]

## Postcomposition by a Möbius transformation

If \(T\) is a [[complex-analysis/mobius-transformation|Möbius transformation]], then \(S(T)=0\), so
\[
S(T\circ f)=S(f).
\]
Thus the Schwarzian is unchanged by changing the projective coordinate on the target.

## Coordinate changes

The factor \((g')^2\) is the transformation factor of a quadratic differential, while the added term \(S(g)\) is the cocycle correction. This is the transformation mechanism in the definition of a [[complex-analysis/projective-connection|holomorphic projective connection]].

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
2. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective connections and the Schwarzian.
