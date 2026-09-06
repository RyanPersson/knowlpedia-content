+++
id = "langlands/moduli-stack-of-g-local-systems"
title = "Moduli stack of G-local systems"
kind = "definition"
summary = "The derived moduli stack LocSys_G(X) of principal G-bundles with flat connection."
aliases = ["LocSys_G", "stack of G-local systems"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/g-local-system", "differential-geometry/riemann-surface"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]] over a characteristic-zero field and
let \(G\) be a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive algebraic group]]. The de Rham **moduli stack of
\(G\)-local systems** is the derived mapping stack
\[
\operatorname{LocSys}^{\mathrm{dR}}_G(X)
=\operatorname{Map}(X_{\mathrm{dR}},BG).
\]
It parametrizes [[langlands/g-local-system|principal \(G\)-bundles with flat
connection]] in families.

When \(X\) is a compact [[differential-geometry/riemann-surface|Riemann surface]], the Betti moduli stack is the
derived character stack
\[
\operatorname{LocSys}^{\mathrm{B}}_G(X)
=\operatorname{Map}(X_{\mathrm{Betti}},BG),
\]
whose classical points are representations of \(\pi_1(X)\) in \(G\) modulo
conjugation. Riemann–Hilbert comparison relates the analytifications of the
de Rham and Betti stacks; it does not identify their algebraic structures.

## Why the derived stack matters

Automorphisms and deformation-obstruction groups are part of the moduli
problem. The derived enhancement records them. For a smooth projective curve,
\(\operatorname{LocSys}^{\mathrm{dR}}_G(X)\) is quasi-smooth, so coherent
sheaves on it have a
[[langlands/singular-support-of-coherent-sheaf|singular support]].

## Spectral role

Geometric Langlands uses
\(\operatorname{LocSys}_{\widehat G}(X)\), where \(\widehat G\) is the
[[langlands-letter/knowls/langlands-dual-group|dual group]]. Its relevant
sheaf category is generally
[[langlands/ind-coherent-sheaves-with-nilpotent-singular-support|\(\operatorname{IndCoh}_{\mathcal N}\)]],
not merely quasi-coherent sheaves.

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
