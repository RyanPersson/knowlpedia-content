+++
id = "fiber-bundles/coulomb-gauge"
title = "Coulomb gauge"
kind = "definition"
summary = "Coulomb gauge imposes a covariant divergence-free condition on the difference between a connection and a reference connection."
aliases = ["Coulomb gauge condition", "divergence-free gauge"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-connection", "fiber-bundles/principal-g-bundle", "differential-geometry/riemannian-manifold", "fiber-bundles/formal-adjoint-of-covariant-exterior-derivative", "fiber-bundles/gauge-fixing-condition"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A_0\) be a [[fiber-bundles/principal-connection|connection]] on a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over a [[differential-geometry/riemannian-manifold|Riemannian manifold]], and write another connection as \(A=A_0+a\). The connection \(A\) is in **Coulomb gauge relative to \(A_0\)** when
\[
d_{A_0}^*a=0,
\]
where \(d_{A_0}^*\) is the [[fiber-bundles/formal-adjoint-of-covariant-exterior-derivative|covariant codifferential]] on adjoint-bundle-valued one-forms. This is a [[fiber-bundles/gauge-fixing-condition|gauge-fixing condition]]: it requires the displacement \(a\) to be \(L^2\)-orthogonal to infinitesimal gauge directions \(d_{A_0}\phi\). It does not by itself assert that every gauge orbit has a representative satisfying the equation, or that such a representative is unique.

## Local slice interpretation

The space of connections is affine, so the expression \(A-A_0\) is an adjoint-bundle-valued one-form even though neither connection is itself a globally defined one-form. Infinitesimally, the tangent to the gauge orbit through \(A_0\) is \(\operatorname{im}d_{A_0}\). The Coulomb condition selects its formal \(L^2\)-orthogonal complement \(\ker d_{A_0}^*\).

After suitable Sobolev completions and under standard regularity hypotheses, this complement yields a local slice modulo the stabilizer of \(A_0\). It is therefore local analytical structure, not a canonical global section of the gauge-orbit map.

## Local trivializations and Uhlenbeck gauge

On a trivial bundle over a coordinate ball, with the product connection as reference, the condition becomes \(d^*a=0\). Uhlenbeck's gauge theorem says, roughly, that a connection with sufficiently small scale-invariant curvature norm can be gauge transformed into such a Coulomb gauge with quantitative Sobolev control.

Boundary versions normally add a condition on the normal component of \(a\). Without that extra condition, [[real-analysis/integration-by-parts|integration by parts]] does not identify \(\ker d^*\) as the full [[linear-algebra/orthogonal-complement|orthogonal complement]] of exact gauge directions.

## Residual symmetry

If \(A_0\) has a nontrivial stabilizer, its stabilizing [[fiber-bundles/gauge-transformation|gauge transformations]] preserve the slice condition. Even for an [[fiber-bundles/irreducible-connection|irreducible connection]], a Coulomb representative is generally unique only in a sufficiently small neighborhood and after controlling constant or based gauge transformations.

**Warning.** The relative condition \(d_{A_0}^*(A-A_0)=0\), the nonlinear condition \(d_A^*(A-A_0)=0\), and the local-coordinate expression \(d^*a=0\) are different equations. A source's convention should be checked before transferring estimates between them.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 3, Sobolev gauge groups and Coulomb slices.
2. Karen K. Uhlenbeck, “Connections with \(L^p\) Bounds on Curvature,” *Communications in Mathematical Physics* 83 (1982), 31–42. [DOI record](https://doi.org/10.1007/BF01947069). Relevant: theorem 1.3, local Coulomb gauges with norm estimates.
