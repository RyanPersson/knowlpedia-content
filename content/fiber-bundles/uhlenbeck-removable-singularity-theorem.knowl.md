+++
id = "fiber-bundles/uhlenbeck-removable-singularity-theorem"
title = "Uhlenbeck removable singularity theorem"
kind = "theorem"
summary = "A finite-energy Yang–Mills connection on a punctured four-ball extends smoothly across the puncture after a gauge transformation."
aliases = ["removable singularity theorem for Yang–Mills connections", "instanton removable singularity theorem"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(G\) be compact and let \(A\) be a smooth Yang–Mills connection on a principal \(G\)-bundle over the punctured Riemannian four-ball \(B^4\setminus\{0\}\). If its curvature has finite energy,
\[
\int_{B^4}|F_A|^2\,d\operatorname{vol}<\infty,
\]
then there is a gauge in which \(A\) extends across \(0\) to a smooth [[fiber-bundles/yangmills-connection|Yang–Mills connection]] on a principal \(G\)-bundle over all of \(B^4\). In particular, the apparent isolated singularity is a gauge artifact. The same conclusion applies to [[fiber-bundles/self-dual-and-anti-self-dual-connection|self-dual and anti-self-dual connections]], since they satisfy the [[fiber-bundles/yangmills-equation|Yang–Mills equation]].

## Proof mechanism

Finite total energy implies that the curvature energy on sufficiently small annuli tends to zero. Uhlenbeck’s small-curvature theorem supplies compatible [[fiber-bundles/coulomb-gauge|Coulomb gauges]] with critical Sobolev control. In these gauges the Yang–Mills equation becomes an elliptic system, and decay estimates improve the connection’s regularity until standard elliptic bootstrapping gives a smooth extension [Uhlenbeck, main theorem].

The conclusion concerns the connection modulo gauge, not the coefficients in an arbitrary trivialization. A badly chosen gauge may remain singular even when the underlying connection extends smoothly.

## Role in compactness

In [[fiber-bundles/uhlenbeck-compactness-theorem|Uhlenbeck compactness]], the limiting connection is first constructed only away from finitely many concentration points. The removable singularity theorem extends it over each point, possibly on a bundle with a different topological class from the original one. The discrepancy is recorded by the instanton bubbles and their concentrated energy.

Applying the theorem at infinity after conformally identifying \(\mathbb R^4\cup\{\infty\}\) with \(S^4\) shows that a finite-energy Yang–Mills field on \(\mathbb R^4\) extends over infinity modulo gauge.

## Scope and non-example

**Warning.** Finite \(L^2\)-curvature alone is not the theorem: the Yang–Mills equation, or a comparably elliptic gauge-invariant equation such as self-duality, is essential. An arbitrary finite-energy connection can have low-regularity behavior that elliptic bootstrapping does not remove.

## References

1. Karen K. Uhlenbeck, “Removable Singularities in Yang–Mills Fields,” *Communications in Mathematical Physics* 83 (1982), 11–29. [DOI record](https://doi.org/10.1007/BF01947068). Relevant: the main removable-singularity theorem and its application at infinity.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 4, removable singularities and compactification.
