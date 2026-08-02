+++
id = "fiber-bundles/l2-inner-product-on-bundle-valued-forms"
title = "L2 inner product on bundle-valued forms"
kind = "definition"
summary = "The integral inner product on bundle-valued differential forms induced by metrics on the base and coefficient bundle."
aliases = ["L2 pairing on bundle-valued forms", "gauge-theoretic L2 metric"]
domains = ["fiber-bundles", "differential-geometry", "functional-analysis"]
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] and let \(E\to M\) be a real Euclidean or complex Hermitian [[fiber-bundles/vector-bundle|vector bundle]] with [[fiber-bundles/bundle-metric|bundle metric]] \(h\). The metrics induce a pointwise [[linear-algebra/inner-product|inner product]] on [[fiber-bundles/vector-bundle-valued-differential-form|\(E\)-valued \(k\)-forms]]. For compactly supported forms \(\alpha,\beta\), their **\(L^2\) inner product** is
\[
\langle\alpha,\beta\rangle_{L^2}
=\int_M\langle\alpha(x),\beta(x)\rangle_{g,h}\,d\operatorname{vol}_g(x).
\]
In the complex case it is Hermitian, with the linear argument determined by convention. The associated norm is \(\|\alpha\|_{L^2}^2=\langle\alpha,\alpha\rangle_{L^2}\).

## Hodge-star expression

The same pairing can be expressed using the [[differential-geometry/hodge-star-operator|Hodge star]] together with contraction of the \(E\)-coefficients by \(h\). For real bundles,
\[
\langle\alpha,\beta\rangle_{L^2}
=\int_M h(\alpha\wedge *\beta),
\]
where \(h(\alpha\wedge *\beta)\) means pair the coefficient factors and wedge the form factors. For Hermitian bundles, one coefficient factor is conjugated according to the chosen linearity convention.

This formulation explains why orientation enters the displayed integral. An equivalent definition using the Riemannian density does not require an orientation.

## Completion and formal adjoints

Completing compactly supported smooth \(E\)-valued forms in this norm gives the [[linear-algebra/hilbert-space|Hilbert space]] \(L^2\Omega^k(M;E)\). On a compact manifold every smooth form has finite \(L^2\)-norm; on a noncompact manifold finite norm is an additional condition.

The pairing defines formal adjoints of covariant differential operators by [[real-analysis/integration-by-parts|integration by parts]]. In [[fiber-bundles/gauge-theory|gauge theory]], applying it to \(\operatorname{ad}P\)-valued curvature gives the Yang–Mills energy, and applying it to infinitesimal changes of a connection gives the standard weak Riemannian metric on the space of connections.

## Examples and scope

For the trivial [[fiber-bundles/line-bundle|line bundle]] over \(\mathbb R^n\) and \(k=0\), this is the usual \(L^2\) inner product of compactly supported functions. A smooth form on a noncompact manifold need not belong to \(L^2\); the constant function \(1\) on \(\mathbb R^n\) is the basic near-miss because its squared norm has infinite integral.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [Publisher record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 2, norms of bundle-valued forms and the Yang–Mills functional.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [Publisher record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §4.2, \(L^2\) geometry of connections and gauge transformations.
