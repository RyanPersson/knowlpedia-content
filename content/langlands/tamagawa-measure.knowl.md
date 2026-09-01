+++
id = "langlands/tamagawa-measure"
title = "Tamagawa measure"
kind = "definition"
summary = "A canonical adelic Haar measure assembled from an invariant differential form and global convergence factors."
aliases = ["Tamagawa measure on an algebraic group", "Tamagawa number", "adelic Tamagawa measure"]
domains = ["langlands", "number-theory", "harmonic-analysis"]
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "langlands-letter/knowls/global-local-fields-completions", "harmonic-analysis/haar-measure", "langlands-letter/knowls/adeles-restricted-product", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/maximal-torus-weight-lattice"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/algebraic-group|linear algebraic group]] over
a [[langlands-letter/knowls/global-local-fields-completions|global field]]
\(F\).
Choose a nonzero invariant top-degree differential form \(\omega\) on \(G\).
At each place \(v\), its absolute value gives a local
[[harmonic-analysis/haar-measure|Haar measure]]
\(|\omega|_v\) on \(G(F_v)\).  After inserting the standard local convergence
factors at almost every place, the
[[langlands-letter/knowls/adeles-restricted-product|restricted product]] of
these measures is the **Tamagawa measure** on \(G(\mathbb A_F)\).

Multiplying \(\omega\) by an element of \(F^\times\) does not change the
global measure, by the product formula.  The convergence factors are essential
for [[algebraic-geometry-foundations/reductive-algebraic-group|reductive
groups]] with nontrivial
[[langlands-letter/knowls/maximal-torus-weight-lattice|characters]]; a bare
product of local
differential-form measures need not converge.

## Tamagawa number

The **Tamagawa number** is the volume

\[
\tau(G)=
\operatorname{vol}\!\left(
G(F)\backslash G(\mathbb A_F)^1
\right),
\]

where \(G(\mathbb A_F)^1\) is the intersection of the kernels of the absolute
values of all \(F\)-rational characters.  For semisimple groups this
superscript is unnecessary.  The quotient and connected-component conventions
must be stated when the [[algebra-groups/center-of-group|center]] is not
anisotropic.

## Automorphic use

Tamagawa measure gives a coherent global normalization for automorphic
quotients, [[langlands/automorphic-constant-term|constant terms]], and
[[langlands/arthur-selberg-trace-formula|trace formulas]]. Local Haar measures
still have to be disintegrated compatibly when forming
[[langlands/orbital-integral|orbital integrals]] or quotient measures.

## References

1. André Weil, *Adeles and Algebraic Groups*, Progress in Mathematics 23,
   Birkhäuser, 1982.
2. Robert E. Kottwitz, “Tamagawa numbers,” *Annals of Mathematics* 127 (1988),
   629–646. [JSTOR](https://doi.org/10.2307/2007007).
