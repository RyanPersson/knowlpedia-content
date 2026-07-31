+++
id = "fiber-bundles/module-of-smooth-sections"
title = "Module of smooth sections"
kind = "definition"
summary = "The module of all smooth sections of a vector bundle under pointwise operations by smooth functions."
aliases = ["section module", "space of smooth sections", "C-infinity module of sections"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(\mathbb F\in\{\mathbb R,\mathbb C\}\), and let \(E\to M\) be a smooth
\(\mathbb F\)-[[fiber-bundles/vector-bundle|vector bundle]] over a
[[fiber-bundles/smooth-manifold|smooth manifold]]. The **module of smooth sections** is
\[
\Gamma^\infty(M,E)=\{s:M\to E\mid s\text{ is a smooth section of }E\}.
\]
For \(s,t\in\Gamma^\infty(M,E)\) and \(f\in C^\infty(M,\mathbb F)\), its operations are defined fiberwise by
\[
(s+t)(x)=s(x)+t(x),
\qquad
(fs)(x)=f(x)s(x).
\]
These operations make \(\Gamma^\infty(M,E)\) a module over the commutative
[[differential-geometry/algebra-of-smooth-functions|algebra
\(C^\infty(M,\mathbb F)\)]]. This module is also written \(\Gamma(E)\) when
smoothness, the scalar field, and the base are understood.

## Local structure

Over a trivializing open set \(U\), a local frame identifies
\[
\Gamma^\infty(U,E|_U)\cong C^\infty(U,\mathbb F)^r.
\]
More precisely, these modules over varying open sets form the
[[fiber-bundles/sheaf-of-smooth-sections|sheaf of smooth sections]], which is
locally free of rank \(r=\operatorname{rank}E\) over
\(C^\infty_M(-,\mathbb F)\). The
single global module \(\Gamma^\infty(M,E)\) is not itself what “locally free”
refers to. Globally it need not possess a basis: a global module basis would
be a global frame and would trivialize \(E\).

Evaluation at \(x\) gives a surjective [[linear-algebra/linear-map|linear map]] \(\Gamma^\infty(M,E)\to E_x\). Its kernel consists of sections vanishing at \(x\), and the fiber can be recovered algebraically as
\[
E_x\cong \Gamma^\infty(M,E)/\mathfrak m_x\Gamma^\infty(M,E),
\]
where \(\mathfrak m_x\) is the ideal of smooth functions vanishing at \(x\).

## Functoriality

A smooth \(\mathbb F\)-linear
[[fiber-bundles/vector-bundle-morphism|vector bundle morphism]]
\(\Phi:E\to E'\) over the identity of \(M\) induces a
\(C^\infty(M,\mathbb F)\)-linear map
\[
\Gamma(\Phi):\Gamma^\infty(M,E)\to\Gamma^\infty(M,E'),
\qquad s\mapsto\Phi\circ s.
\]
Conversely, \(C^\infty(M,\mathbb F)\)-linear maps between section modules
arise from unique smooth \(\mathbb F\)-linear
[[fiber-bundles/bundle-morphism|bundle morphisms]] under the standard
finite-rank hypotheses. This correspondence is one part of the smooth
Serre–Swan viewpoint.

The requirement that \(\Phi\) cover \(\operatorname{id}_M\) is essential:
it places \(E\) and \(F\) in the same
[[fiber-bundles/category-of-vector-bundles-over-a-manifold|fixed-base
bundle category]] and makes both section spaces modules over the same ring.
A morphism covering \(f:M\to N\) does not give the displayed map by
postcomposition.

## Relation to Serre–Swan

If \(M\) is a connected finite-dimensional Hausdorff second-countable
manifold and \(E\) has finite rank, then
\(\Gamma^\infty(M,E)\) is a finitely generated
[[algebra-modules/projective-module|projective module]] over
\(C^\infty(M,\mathbb F)\), and every such module is the section module of a
smooth \(\mathbb F\)-vector bundle. This smooth Serre–Swan statement requires
no compactness hypothesis; finite dimensionality supplies a finite-rank
complementary bundle. On a disconnected base, one requires the ranks on
components to be globally bounded. See
[Nestruev, Chapter 11]. The original compact
Hausdorff theorem over \(C(X)\) is a distinct continuous formulation
[Swan, Theorem 1].

Taking sections over every open set gives the
[[fiber-bundles/vector-bundles-and-locally-free-sheaves|equivalence between
vector bundles and finite-rank locally free
\(C^\infty_M(-,\mathbb F)\)-module sheaves]].

## References

1. R. G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: Theorem 1 and the compact-Hausdorff equivalence.
2. J. Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, vector bundles and projective modules over smooth-function algebras.
3. L. W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55092-8). Relevant: Chapter 1, smooth vector bundles and section modules.
