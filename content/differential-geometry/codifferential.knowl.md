+++
id = "differential-geometry/codifferential"
title = "Codifferential"
kind = "definition"
summary = "The degree-lowering formal adjoint of the exterior derivative on an oriented Riemannian manifold."
aliases = ["formal adjoint of the exterior derivative", "delta operator on forms"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/formal-adjoint-differential-operator", "fiber-bundles/exterior-derivative", "differential-geometry/hodge-star-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented \(n\)-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary. The **codifferential** is the [[differential-geometry/formal-adjoint-differential-operator|formal adjoint]] of the [[fiber-bundles/exterior-derivative|exterior derivative]],
\[
\delta:\Omega^k(M)\longrightarrow\Omega^{k-1}(M),
\]
characterized by \(\langle d\alpha,\beta\rangle_{L^2}=\langle\alpha,\delta\beta\rangle_{L^2}\) for compactly supported forms. With the real [[differential-geometry/hodge-star-operator|Hodge-star]] convention used here,
\[
\delta\beta=(-1)^{n(k+1)+1}*d*\beta
\]
for every \(k\)-form \(\beta\). This definition is formal: it does not by itself specify a domain for an unbounded Hilbert-space operator.

## Local formula and elementary properties

For a local orthonormal frame \(e_1,\ldots,e_n\) and the Levi–Civita connection \(\nabla\),
\[
\delta\beta=-\sum_{j=1}^n\iota_{e_j}\nabla_{e_j}\beta.
\]
Consequently \(\delta^2=0\). A form is called coclosed when \(\delta\beta=0\). On a function, \(\delta\) vanishes because there are no forms of degree \(-1\).

## Relationship to the Hodge Laplacian

The [[differential-geometry/hodge-laplacian|Hodge Laplacian]] is
\[
\Delta=d\delta+\delta d.
\]
It is formally self-adjoint and degree-preserving. On a compact manifold without boundary, a form is harmonic precisely when it is both closed and coclosed. This equivalence follows from
\[
\langle\Delta\alpha,\alpha\rangle_{L^2}
=\lVert d\alpha\rVert_{L^2}^2+\lVert\delta\alpha\rVert_{L^2}^2.
\]

## Conventions and scope

**Warning.** The displayed sign depends on dimension, form degree, metric signature, and the Hodge-star convention. On manifolds with boundary, [[real-analysis/integration-by-parts|integration by parts]] includes a boundary term; an analytic adjoint then requires boundary conditions. The codifferential also extends to nonorientable Riemannian manifolds by using densities or the orientation double cover, although the global star formula above assumes an orientation.

## References

1. Jürgen Jost, *Riemannian Geometry and Geometric Analysis*, 7th ed., Springer, 2017. [Publisher record](https://doi.org/10.1007/978-3-319-61860-9). Relevant: Chapter 3, “The Laplace Operator and Harmonic Differential Forms.”
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter III, Hermitian exterior algebra and the Hodge-star operator.
