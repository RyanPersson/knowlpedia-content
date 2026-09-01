+++
id = "differential-geometry/einstein-manifold"
title = "Einstein manifold"
kind = "definition"
summary = "A Riemannian manifold whose Ricci tensor is a constant multiple of the metric."
aliases = ["Einstein metric", "Riemannian Einstein manifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "topology/connected-component", "differential-geometry/ricci-curvature"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

An **Einstein manifold** is a [[differential-geometry/riemannian-manifold|Riemannian manifold]] \((M^n,g)\) for which there is a real constant \(\lambda\), on each [[topology/connected-component|connected component]], such that
\[
\operatorname{Ric}_g=\lambda g,
\]
where \(\operatorname{Ric}_g\) is the [[differential-geometry/ricci-curvature|Ricci curvature]]. The metric \(g\) is then called an **Einstein metric**, and \(\lambda\) its Einstein constant. Equivalently, all tangent directions have the same Ricci curvature after normalization by squared length. The case \(\lambda=0\) is called Ricci-flat. This is a Riemannian definition; pseudo-Riemannian Einstein metrics use the same tensor equation but allow indefinite \(g\).

## Equivalent characterizations and scaling

Taking the metric trace gives constant scalar curvature
\[
\operatorname{Scal}_g=n\lambda.
\]
Conversely, constant scalar curvature alone does not imply the Einstein equation when \(n\geq3\), because it controls only the trace of the Ricci tensor. If \(g\) is Einstein and \(c>0\) is constant, then \(cg\) is Einstein with constant \(\lambda/c\). The Levi–Civita connection and Ricci tensor as a covariant \(2\)-tensor remain unchanged under this rescaling.

## Examples and non-examples

An \(n\)-manifold of constant sectional curvature \(k\) is Einstein with \(\lambda=(n-1)k\). Hence the round sphere is Einstein, while [[linear-algebra/euclidean-space|Euclidean space]] and flat tori are Ricci-flat. In dimension two, \(\operatorname{Ric}=Kg\), so an Einstein surface is exactly a surface of constant Gaussian curvature.

A product of two Einstein manifolds with the product metric is Einstein when their Einstein constants agree. If the constants differ, the product has different Ricci eigenvalues along the two factors and is a decisive non-example.

## Structure and scope

The contracted [[fiber-bundles/bianchi-identity|Bianchi identity]] implies that a relation \(\operatorname{Ric}=f g\) already forces \(f\) to be constant on connected manifolds of dimension at least three. In dimension two this conclusion fails without imposing constancy, which is why the constant is included in the definition. Einstein metrics are not generally metrics of constant sectional curvature: the Ricci tensor is only a trace of the full curvature tensor.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Publisher record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 1, “Basic Material,” pp. 20–65, for curvature conventions and the Einstein condition.
2. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7, “Curvature,” for Ricci and scalar curvature and the contracted Bianchi identity.
