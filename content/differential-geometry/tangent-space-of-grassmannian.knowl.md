+++
id = "differential-geometry/tangent-space-of-grassmannian"
title = "Tangent space of a Grassmannian"
kind = "theorem"
summary = "The tangent space at a subspace in a Grassmannian is canonically the space of linear maps from that subspace to its quotient."
aliases = ["tangent space to Gr(k,V)"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "differential-geometry/grassmannian", "differential-geometry/tangent-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional real or complex [[linear-algebra/vector-space|vector space]], and let \(W\) be a point of the [[differential-geometry/grassmannian|Grassmannian]] \(\operatorname{Gr}_k(V)\). Its [[differential-geometry/tangent-space|tangent space]] has a canonical linear identification
\[
T_W\operatorname{Gr}_k(V)\cong\operatorname{Hom}(W,V/W).
\]
In the complex case this is an isomorphism of complex vector spaces. Explicitly, represent a tangent vector by a smooth curve \(W(t)\) of \(k\)-planes with \(W(0)=W\). For \(w\in W\), choose a smooth curve \(w(t)\in W(t)\) with \(w(0)=w\); the tangent vector sends \(w\) to the class of \(w'(0)\) in \(V/W\). This class is independent of all choices.

## Derivation from graph charts

Choose a complementary subspace \(U\) with \(V=W\oplus U\). Every plane sufficiently near \(W\) is the graph of a unique [[linear-algebra/linear-map|linear map]] \(A:W\to U\). This chart identifies the tangent space at \(W\) with \(\operatorname{Hom}(W,U)\). The quotient projection restricts to an isomorphism \(U\to V/W\), producing the displayed identification. Although the chart used \(U\), the quotient-space description does not, which proves canonicity.

## Naturality

If \(F:V\to V'\) is a linear isomorphism, its action on Grassmannians sends \(W\) to \(F(W)\). Under the canonical tangent-space identifications, its differential sends \(\phi:W\to V/W\) to
\[
F_{\mathrm{quot}}\circ\phi\circ(F|_W)^{-1},
\]
where \(F_{\mathrm{quot}}:V/W\to V'/F(W)\) is the induced quotient map. Thus the identification respects changes of coordinates and [[algebra-groups/group-action|group actions]].

## Consequences and examples

The dimension follows immediately:
\[
\dim_{\mathbb F}T_W\operatorname{Gr}_k(V)=k(\dim_{\mathbb F}V-k).
\]
Using the [[convex-analysis/dual-space-and-duality-pairing|dual space]], the same result can be written \(T_W\operatorname{Gr}_k(V)\cong W^*\otimes(V/W)\). For \(k=1\), it gives \(T_L\mathbb P(V)\cong\operatorname{Hom}(L,V/L)\). If an [[linear-algebra/inner-product|inner product]] identifies \(V/W\) with the [[linear-algebra/orthogonal-complement|orthogonal complement]] \(W^\perp\), one obtains the convenient but noncanonical model \(\operatorname{Hom}(W,W^\perp)\). The quotient model remains valid without an inner product.

## References

1. Joe Harris, *Algebraic Geometry: A First Course*, Springer, 1992. [Springer DOI record](https://doi.org/10.1007/978-1-4757-2189-8). Relevant: Lecture 6, Grassmannians and their tangent spaces.
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher DOI record](https://doi.org/10.1515/9781400881826). Relevant: §§5–6, Grassmann manifolds and their local structure.
