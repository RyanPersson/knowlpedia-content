+++
id = "differential-geometry/hodge-decomposition-kahler"
title = "Hodge decomposition of a compact Kähler manifold"
kind = "theorem"
summary = "The decomposition of complex de Rham cohomology into Dolbeault cohomology groups of fixed bidegree."
aliases = ["Kähler Hodge decomposition", "Hodge decomposition by bidegree"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a compact [[differential-geometry/kahler-manifold|Kähler manifold]]. For every \(k\), the **Hodge decomposition** is the canonical direct sum
\[
H^k_{\mathrm{dR}}(X;\mathbb C)
\cong \bigoplus_{p+q=k}H_{\bar\partial}^{p,q}(X)
\]
of [[differential-geometry/dolbeault-cohomology|Dolbeault cohomology]] groups. Under the [[differential-geometry/hodge-theorem|Hodge theorem]], a de Rham class has a unique harmonic representative, and the displayed isomorphism sends it to its harmonic components of type \((p,q)\). Complex conjugation exchanges the summands \(H^{p,q}(X)\) and \(H^{q,p}(X)\). Compactness and the Kähler condition are part of the theorem.

## Analytic mechanism

The [[differential-geometry/kahler-identities|Kähler identities]] imply
\[
\Delta_d=2\Delta_{\partial}=2\Delta_{\bar\partial}.
\]
Consequently the [[differential-geometry/hodge-laplacian|de Rham Laplacian]] preserves bidegree, so each \((p,q)\)-component of a [[differential-geometry/harmonic-differential-form|harmonic form]] is harmonic. This is the step that turns the type decomposition of differential forms into a direct-sum decomposition of cohomology [Voisin, §6.1, Theorem 6.3].

## Consequences

Writing \(h^{p,q}(X)=\dim_{\mathbb C}H^{p,q}(X)\), the decomposition gives
\[
b_k(X)=\sum_{p+q=k}h^{p,q}(X)
\]
and conjugation gives \(h^{p,q}=h^{q,p}\). In particular, every odd Betti number of a compact Kähler manifold is even. Wedge product respects bidegree, so the decomposition is compatible with the graded cohomology ring.

## Scope and near-misses

A compact [[differential-geometry/complex-manifold|complex manifold]] need not admit this decomposition. The [[differential-geometry/frolicher-spectral-sequence|Frölicher spectral sequence]] may have nonzero higher differentials, and even its degeneration does not by itself provide the harmonic splitting above. For noncompact Kähler manifolds, ordinary de Rham cohomology need not be represented by harmonic forms without additional analytic conditions.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Publisher record](https://doi.org/10.1017/CBO9780511615344). Relevant: §6.1, especially Theorem 6.3.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, §3.2, Hodge decomposition and its numerical consequences.
