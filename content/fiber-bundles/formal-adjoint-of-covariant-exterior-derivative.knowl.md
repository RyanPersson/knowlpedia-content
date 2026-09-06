+++
id = "fiber-bundles/formal-adjoint-of-covariant-exterior-derivative"
title = "Formal adjoint of the covariant exterior derivative"
kind = "definition"
summary = "The covariant codifferential is the formal adjoint of the covariant exterior derivative with respect to the bundle-valued L2 pairing."
aliases = ["covariant codifferential", "d_A star"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/vector-bundle", "fiber-bundles/bundle-metric", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/exterior-covariant-derivative", "fiber-bundles/l2-inner-product-on-bundle-valued-forms", "differential-geometry/hodge-star-operator", "real-analysis/integration-by-parts"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be an oriented \(n\)-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary, and let \(E\to M\) be a [[fiber-bundles/vector-bundle|vector bundle]] with [[fiber-bundles/bundle-metric|bundle metric]] and compatible [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(A\). The **formal adjoint of the covariant exterior derivative** is the operator
\[
d_A^*:\Omega^{r}(M;E)\longrightarrow\Omega^{r-1}(M;E)
\]
characterized by
\[
\langle d_A\alpha,\beta\rangle_{L^2}
=\langle\alpha,d_A^*\beta\rangle_{L^2}
\]
for all compactly supported smooth forms of the appropriate degrees. Here \(d_A\) is the [[fiber-bundles/exterior-covariant-derivative|exterior covariant derivative]] and the pairing is the [[fiber-bundles/l2-inner-product-on-bundle-valued-forms|\(L^2\) pairing]]. This identity defines a differential expression, not a Hilbert-space adjoint with a specified domain.

## Hodge-star formula

Extend the [[differential-geometry/hodge-star-operator|Hodge star]] to \(E\)-valued forms by acting on the form factor. With the convention used here, its restriction to \(r\)-forms satisfies
\[
d_A^*=(-1)^{n(r+1)+1}*d_A*.
\]
Equivalent sign formulas occur because authors index the input or output degree differently. The compatibility of \(A\) with the fiber metric is what allows [[real-analysis/integration-by-parts|integration by parts]] without an additional derivative of that metric.

For \(E\) the trivial [[fiber-bundles/line-bundle|real line bundle]] with its flat connection, \(d_A^*\) is the ordinary [[differential-geometry/codifferential|codifferential]]. For the gauge-theoretic [[fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms|covariant derivative on an adjoint bundle]] \(\operatorname{ad}P\), invariance of the Lie-algebra [[linear-algebra/inner-product|inner product]] supplies the required bundle metric.

## Analytical role

The operator \(d_A^*\) enters both [[fiber-bundles/gauge-fixing-condition|gauge fixing]] and the Yang–Mills equation. A perturbation \(a\) is in [[fiber-bundles/coulomb-gauge|Coulomb gauge]] relative to \(A\) when \(d_A^*a=0\), while the [[fiber-bundles/yangmills-equation|Yang–Mills equation]] is \(d_A^*F_A=0\). Together with \(d_A\), it forms the gauge-covariant [[differential-geometry/hodge-laplacian|Hodge Laplacian]] used in elliptic estimates.

**Warning.** On a manifold with boundary, integration by parts has a boundary term. An analytic adjoint therefore depends on boundary conditions and on the chosen operator domain even though the displayed formal expression remains local.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 2, bundle-valued forms, formal adjoints, and the Yang–Mills equation.
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: chapters III–IV, Hodge-star identities and formal adjoints.
