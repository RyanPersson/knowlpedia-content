+++
id = "noncommutative-geometry/almost-commutative-spectral-triple"
title = "Almost-commutative spectral triple"
kind = "definition"
summary = "A spectral triple obtained by multiplying the canonical spin geometry of a manifold by a finite spectral triple."
aliases = ["almost-commutative geometry", "product geometry with a finite triple"]
domains = ["noncommutative-geometry", "differential-geometry"]
prerequisites = ["noncommutative-geometry/canonical-spin-spectral-triple", "noncommutative-geometry/product-spectral-triple"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a closed even-dimensional Riemannian spin manifold with
[[noncommutative-geometry/canonical-spin-spectral-triple|canonical spin spectral triple]]
\((C^\infty(M),L^2(M,S),\not D_M,\Gamma_M)\), and let
\((\mathcal A_F,H_F,D_F,\Gamma_F)\) be a finite-dimensional even spectral
triple. Their [[noncommutative-geometry/product-spectral-triple|product]]
\[
\left(
C^\infty(M)\odot\mathcal A_F,\,
L^2(M,S)\widehat\otimes H_F,\,
\not D_M\otimes1+\Gamma_M\otimes D_F,\,
\Gamma_M\otimes\Gamma_F
\right)
\]
is an **almost-commutative spectral triple**. The manifold factor supplies the
continuous geometry, while the finite factor supplies finitely many internal
degrees of freedom.

## Algebra-bundle interpretation

For a trivial finite factor, the algebra is the smooth section algebra of the
trivial bundle \(M\times\mathcal A_F\). More general globally
almost-commutative geometries replace it by smooth sections of a locally
trivial bundle of finite-dimensional star-algebras and replace the product
[[noncommutative-geometry/dirac-operator|Dirac operator]] by a compatible twisted
[[noncommutative-geometry/dirac-type-operator|Dirac-type operator]]. This
extension allows nontrivial internal algebra bundles while retaining a
classical manifold as the base.

## Examples and gauge-theoretic role

Taking \(\mathcal A_F=\mathbb C\), \(H_F=\mathbb C\), and \(D_F=0\) recovers
the canonical spin [[noncommutative-geometry/spectral-triple|spectral triple]]. Taking a noncommutative finite algebra,
such as a sum of complex matrix algebras, gives matrix-valued functions over
\(M\). Inner fluctuations of the product Dirac operator then split into
ordinary gauge fields along \(M\) and finite-direction scalar fields; this is
the mechanism used in spectral-triple models of
[[fiber-bundles/gauge-theory|gauge theories]].

## Additional structures and scope

Applications commonly equip both factors with real structures and impose the
order-zero and first-order conditions. Their product involves
KO-dimension-dependent signs, and orientability or regularity must be checked
separately. Those data are not part of the bare complex definition above.

“Almost commutative” does not mean that
\(C^\infty(M)\odot\mathcal A_F\) is nearly commutative in a metric sense. It
means specifically that all noncommutativity is confined to a
finite-dimensional internal factor, or to its finite-algebra-bundle
generalization.

## References

1. Walter D. van Suijlekom, *Noncommutative Geometry and Particle Physics*, Springer, 2015. [Publisher record](https://doi.org/10.1007/978-94-017-9162-5). Relevant: “Almost-Commutative Manifolds and Gauge Theories,” pp. 137–158.
2. Alain Connes and Matilde Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society and Hindustan Book Agency, 2008. [AMS record](https://bookstore.ams.org/coll-55). Relevant: the almost-commutative spectral geometry underlying the noncommutative-geometric Standard Model.
