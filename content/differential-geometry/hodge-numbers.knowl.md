+++
id = "differential-geometry/hodge-numbers"
title = "Hodge numbers"
kind = "definition"
summary = "The dimensions of the bidegree components in the Hodge decomposition of a compact Kähler manifold."
aliases = []
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/kahler-manifold", "differential-geometry/hodge-decomposition-kahler"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a compact [[differential-geometry/kahler-manifold|Kähler manifold]] of complex dimension \(n\). Its **Hodge number of bidegree \((p,q)\)** is
\[
h^{p,q}(X)=\dim_{\mathbb C}H_{\bar\partial}^{p,q}(X),
\qquad 0\leq p,q\leq n.
\]
Equivalently, \(h^{p,q}(X)\) is the dimension of the \((p,q)\)-summand in the [[differential-geometry/hodge-decomposition-kahler|Hodge decomposition]] of \(H^{p+q}_{\mathrm{dR}}(X;\mathbb C)\). The finite array \(\{h^{p,q}\}\), conventionally displayed with \(p+q\) constant along diagonals, is called the **Hodge diamond**. A Hodge number is a numerical invariant, whereas the corresponding Hodge component retains its vector-space structure.
Only indices in the displayed range occur.

## Symmetries and Betti numbers

Complex conjugation and Hodge duality give
\[
h^{p,q}=h^{q,p},
\qquad
h^{p,q}=h^{n-p,n-q}.
\]
The diagonal sums recover the Betti numbers:
\[
b_k(X)=\sum_{p+q=k}h^{p,q}(X).
\]
These identities are consequences of compact Kähler Hodge theory.

## Examples

For \(\mathbb{CP}^n\), one has \(h^{p,p}=1\) for \(0\leq p\leq n\) and all off-diagonal Hodge numbers vanish. A compact [[differential-geometry/riemann-surface|Riemann surface]] of genus \(g\) has \(h^{0,0}=h^{1,1}=1\) and \(h^{1,0}=h^{0,1}=g\). These examples show respectively that the diamond can be diagonal or can record complex-analytic information not visible in a single cohomological degree.

## Conventions and scope

For an arbitrary compact [[differential-geometry/complex-manifold|complex manifold]], authors still define \(h^{p,q}=\dim H_{\bar\partial}^{p,q}\), but the diagonal-sum formula and the second symmetry need not hold. In algebraic geometry, “Hodge numbers” may also refer to dimensions of graded pieces of a mixed Hodge structure; those require a weight index in addition to \((p,q)\).

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, §3.2, Hodge decomposition and Hodge numbers.
2. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Publisher record](https://doi.org/10.1017/CBO9780511615344). Relevant: Chapter 6 for Kähler Hodge decomposition and Chapter 7 for Hodge structures.
