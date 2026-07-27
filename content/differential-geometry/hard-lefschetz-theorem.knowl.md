+++
id = "differential-geometry/hard-lefschetz-theorem"
title = "Hard Lefschetz theorem"
kind = "theorem"
summary = "Powers of a Kähler class give isomorphisms between complementary cohomological degrees on a compact Kähler manifold."
aliases = ["Lefschetz isomorphism theorem"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(X\) be a compact [[differential-geometry/kahler-manifold|Kähler manifold]] of complex dimension \(n\), and let \(L\) denote [[topology/cup-product-and-cohomology-ring|cup product]] with its [[differential-geometry/kahler-class|Kähler class]] \([\omega]\). The **Hard Lefschetz theorem** states that for every \(0\leq k\leq n\),
\[
L^{\,n-k}:H^k(X;\mathbb R)\longrightarrow H^{2n-k}(X;\mathbb R),
\qquad [\alpha]\longmapsto[\omega]^{\,n-k}\smile[\alpha],
\]
is an isomorphism. The same holds with complex coefficients. Equivalently, \(L^r:H^{n-r}(X)\to H^{n+r}(X)\) is an isomorphism for \(0\leq r\leq n\). Compactness and the Kähler condition are essential hypotheses of this statement [Voisin, Theorem 6.25](https://doi.org/10.1017/CBO9780511615344).

## Proof mechanism

The [[differential-geometry/kahler-identities|Kähler identities]] show that the [[differential-geometry/lefschetz-operator|Lefschetz operator]] \(L\), its adjoint \(\Lambda\), and the degree operator act as an \(\mathfrak{sl}_2\)-triple on [[differential-geometry/harmonic-differential-form|harmonic forms]]. Finite-dimensional \(\mathfrak{sl}_2\)-representation theory then makes the displayed powers of \(L\) bijective. Harmonic representatives transfer these linear-algebraic isomorphisms to de Rham cohomology.

## Primitive decomposition

For \(k\leq n\), the [[differential-geometry/primitive-cohomology|primitive cohomology]] is
\[
P^k(X)=\ker\!\left(L^{\,n-k+1}:H^k(X)\to H^{2n-k+2}(X)\right).
\]
Hard Lefschetz yields the direct-sum decomposition
\[
H^k(X)=\bigoplus_{j\geq0}L^jP^{k-2j}(X),
\]
with only terms of nonnegative degree included. This decomposition organizes the cohomology into irreducible strings for the Lefschetz \(\mathfrak{sl}_2\)-action.

## Scope and consequences

The theorem implies, among other things, that multiplication by \([\omega]\) is injective below the middle degree and surjective at or above it. It is a statement over \(\mathbb R\) or \(\mathbb C\); an integral isomorphism is not asserted, and an arbitrary Kähler class need not be integral. Closed [[differential-geometry/symplectic-manifold|symplectic manifolds]] need not satisfy Hard Lefschetz, so symplecticity alone is a decisive near-miss.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §6.2 and Theorem 6.25, Lefschetz decomposition and the Hard Lefschetz theorem.
