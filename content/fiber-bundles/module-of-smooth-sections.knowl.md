+++
id = "fiber-bundles/module-of-smooth-sections"
title = "Module of smooth sections"
kind = "definition"
summary = "The module of all smooth sections of a vector bundle under pointwise operations by smooth functions."
aliases = ["section module", "space of smooth sections", "C-infinity module of sections"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] over a [[fiber-bundles/smooth-manifold|smooth manifold]]. The **module of smooth sections** is
\[
\Gamma^\infty(M,E)=\{s:M\to E\mid s\text{ is a smooth section of }E\}.
\]
For \(s,t\in\Gamma^\infty(M,E)\) and \(f\in C^\infty(M)\), its operations are defined fiberwise by
\[
(s+t)(x)=s(x)+t(x),
\qquad
(fs)(x)=f(x)s(x).
\]
These operations make \(\Gamma^\infty(M,E)\) a module over the commutative [[differential-geometry/algebra-of-smooth-functions|algebra \(C^\infty(M)\)]]. This module is also written \(\Gamma(E)\) when smoothness and the base are understood.

## Local structure

Over a trivializing open set \(U\), a local frame identifies
\[
\Gamma^\infty(U,E|_U)\cong C^\infty(U)^r.
\]
Thus the section module is locally free of rank \(r=\operatorname{rank}E\). Globally it need not possess a basis: a global module basis would be a global frame and would trivialize \(E\).

Evaluation at \(x\) gives a surjective linear map \(\Gamma^\infty(M,E)\to E_x\). Its kernel consists of sections vanishing at \(x\), and the fiber can be recovered algebraically as
\[
E_x\cong \Gamma^\infty(M,E)/\mathfrak m_x\Gamma^\infty(M,E),
\]
where \(\mathfrak m_x\) is the ideal of smooth functions vanishing at \(x\).

## Functoriality

A smooth [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] \(\Phi:E\to F\) over the identity of \(M\) induces a \(C^\infty(M)\)-linear map
\[
\Gamma(\Phi):\Gamma^\infty(M,E)\to\Gamma^\infty(M,F),
\qquad s\mapsto\Phi\circ s.
\]
Conversely, \(C^\infty(M)\)-linear maps between section modules arise from unique smooth bundle morphisms under the standard finite-rank hypotheses. This correspondence is one part of the smooth Serre–Swan viewpoint.

## Relation to Serre–Swan

When \(M\) is compact, \(\Gamma^\infty(M,E)\) is a finitely generated [[algebra-modules/projective-module|projective module]] over \(C^\infty(M)\), and every such module is isomorphic to the module of sections of a smooth vector bundle. This is the smooth form of Serre–Swan duality; see [Nestruev, Chapter 11](https://doi.org/10.1007/b98871). Compactness is important in this finitely generated formulation; variants for noncompact spaces use different module categories or support/vanishing conditions. [Swan, Theorem 1](https://doi.org/10.1090/S0002-9947-1962-0143225-6) is the foundational compact-space theorem.

## References

1. R. G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: Theorem 1 and the compact-Hausdorff equivalence.
2. J. Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, vector bundles and projective modules over smooth-function algebras.
3. L. W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55092-8). Relevant: Chapter 1, smooth vector bundles and section modules.
