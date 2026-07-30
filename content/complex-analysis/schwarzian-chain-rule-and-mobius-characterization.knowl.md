+++
id = "complex-analysis/schwarzian-chain-rule-and-mobius-characterization"
title = "Schwarzian chain rule and Möbius characterization"
kind = "theorem"
summary = "The Schwarzian obeys a cocycle rule and vanishes exactly for Möbius transformations."
aliases = ["Schwarzian chain rule", "Möbius characterization by Schwarzian"]
domains = ["complex-analysis", "projective-geometry"]
section_mode = "progressive"
+++

For locally univalent holomorphic maps \(f\) and \(g\),
\[
S(f\circ g)=\bigl(S(f)\circ g\bigr)(g')^2+S(g).
\]
In particular, \(S(T)=0\) for every [[complex-analysis/mobius-transformation|Möbius transformation]] \(T\), and a locally univalent holomorphic \(f\) satisfies \(S(f)=0\) exactly when it is locally the restriction of a Möbius transformation.

## Postcomposition invariance

The chain rule immediately gives
\[
S(T\circ f)=S(f)
\]
for Möbius \(T\). Thus the Schwarzian is insensitive to changing the projective coordinate on the target.

## Equal Schwarzians

If \(f\) and \(g\) are locally univalent and \(S(f)=S(g)\), then locally
\[
f=T\circ g
\]
for some Möbius transformation \(T\). On a connected domain, one obtains a single global \(T\) whenever both maps are globally defined into the sphere and analytic continuation introduces no monodromy. The local statement is the unconditional one.

## Differential-equation interpretation

If \(y_1,y_2\) are linearly independent solutions of
\[
y''+\frac12q\,y=0,
\]
then \(f=y_1/y_2\) satisfies \(S(f)=q\). Changing the solution basis postcomposes \(f\) by a Möbius transformation, explaining both the chain rule and the equal-Schwarzian statement.

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
