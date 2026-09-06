+++
id = "differential-geometry/calabi-yau-manifold"
title = "Calabi–Yau manifold"
kind = "definition"
summary = "A compact connected Kähler manifold whose holomorphic canonical bundle is trivial."
aliases = ["CY manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/kahler-manifold", "differential-geometry/canonical-bundle-complex-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In this knowl, a **Calabi–Yau manifold** is a connected compact [[differential-geometry/kahler-manifold|Kähler manifold]] \(X\) whose [[differential-geometry/canonical-bundle-complex-manifold|canonical bundle]] \(K_X\) is holomorphically trivial. Equivalently, if \(n=\dim_{\mathbb C}X\), then \(X\) admits a nowhere-vanishing holomorphic \(n\)-form. The form, a [[differential-geometry/kahler-metric|Kähler metric]], and a [[differential-geometry/kahler-class|Kähler class]] are not included as chosen data. This convention is deliberately broad: it includes complex tori and compact Kähler [[differential-geometry/holomorphic-symplectic-manifold|holomorphic symplectic manifolds]], as well as manifolds whose Ricci-flat metrics have full holonomy \(SU(n)\).

## Ricci-flat metrics and holonomy

Triviality of \(K_X\) implies that the real first Chern class vanishes. Yau's [[differential-geometry/calabi-yau-theorem|solution of the Calabi conjecture]] then gives, in each Kähler class, a unique Ricci-flat Kähler metric. A nowhere-vanishing holomorphic volume form is parallel for the corresponding normalized metric, so the restricted holonomy is contained in \(SU(n)\).

Containment need not be equality. Flat complex tori have smaller holonomy, and holomorphic symplectic examples have holonomy contained in a symplectic subgroup. Extra hypotheses, such as simple connectedness and irreducibility of the Riemannian [[fiber-bundles/holonomy-representation|holonomy representation]], are needed before one concludes full holonomy \(SU(n)\).

## Examples

Every elliptic curve is Calabi–Yau under the convention above: its translation-invariant holomorphic \(1\)-form has no zeros. More generally, every compact [[differential-geometry/complex-torus|complex torus]] has a translation-invariant nowhere-vanishing holomorphic top form.

A smooth quintic hypersurface in [[algebraic-geometry-foundations/projective-space|complex projective \(4\)-space]] is a Calabi–Yau threefold. The adjunction formula makes its canonical bundle trivial, while projectivity supplies a Kähler metric. This example belongs to the full-\(SU(3)\) class rather than the torus class.

## Conventions and scope

**Warning.** “Calabi–Yau manifold” has no single universal definition. Some authors require simple connectedness, full holonomy \(SU(n)\), or the vanishings \(H^{p,0}(X)=0\) for \(0<p<n\); others require only \(c_1(X)=0\) in real cohomology. Those variants are not equivalent without additional hypotheses.

This definition concerns smooth [[differential-geometry/complex-manifold|complex manifolds]]. Singular Calabi–Yau varieties require separate choices concerning normality, singularities, and the meaning of the canonical sheaf.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford Mathematical Monographs, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapter 5, the Calabi conjecture, and Chapter 6, Calabi–Yau manifolds and holonomy.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Appendix 4.B, Hermite–Einstein and Kähler–Einstein metrics.
