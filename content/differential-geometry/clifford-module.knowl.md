+++
id = "differential-geometry/clifford-module"
title = "Clifford module"
kind = "definition"
summary = "A module carrying a compatible representation of a Clifford algebra."
aliases = ["Clifford representation", "Clifford multiplication"]
domains = ["differential-geometry", "algebra-modules"]
section_mode = "progressive"
+++

Let \(\operatorname{Cl}(V,q)\) be a [[differential-geometry/clifford-algebra|Clifford algebra]]. A **Clifford module** is a [[algebra-modules/module|module]] \(E\) together with a unital algebra homomorphism
\[
c:\operatorname{Cl}(V,q)\longrightarrow \operatorname{End}(E).
\]
Equivalently, it is a linear map \(c:V\to\operatorname{End}(E)\), called **Clifford multiplication**, satisfying
\[
c(v)^2=-q(v)\operatorname{id}_E
\]
under the Riemannian sign convention. Polarization yields
\[
c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{id}_E
\]
when \(q(v)=g(v,v)\). A different Clifford-algebra sign convention changes both displayed signs. The scalar ring and module category are understood to be the same as those used to construct \(\operatorname{Cl}(V,q)\).

## Graded modules

If \(E=E^0\oplus E^1\) is \(\mathbb Z/2\)-graded, it is a **graded Clifford module** when Clifford multiplication by every \(v\in V\) is odd:
\[
c(v):E^j\longrightarrow E^{j+1\!\!\pmod 2}.
\]
Equivalently, the algebra representation preserves total degree: the even part of the Clifford algebra acts evenly and the odd part acts oddly. Ungraded Clifford modules are also standard, especially in odd dimension.

## Clifford module bundles

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]]. A Clifford module bundle is a vector bundle \(E\to M\) with a smooth bundle-algebra action
\[
c:\operatorname{Cl}(T^*M,g)\longrightarrow \operatorname{End}(E).
\]
Fiberwise, each \(E_x\) is a module over \(\operatorname{Cl}(T_x^*M,g_x)\). If \(E\) is Hermitian, one usually also requires \(c(\xi)^*=-c(\xi)\) for real covectors \(\xi\); this compatibility is an extra metric condition, not part of the purely algebraic definition.

## Role in Dirac operators

A compatible connection \(\nabla^E\) on a Clifford module bundle allows the composition
\[
\Gamma^\infty(E)
\xrightarrow{\ \nabla^E\ }
\Gamma^\infty(T^*M\otimes E)
\xrightarrow{\ c\ }
\Gamma^\infty(E).
\]
This first-order differential operator is of Dirac type. Clifford multiplication supplies its principal symbol, whereas the choice of compatible connection supplies additional geometric data.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [DOI record](https://doi.org/10.1515/9781400883912). Relevant: Chapters I–II, Clifford modules and spinors.
2. Nicole Berline, Ezra Getzler, and Michèle Vergne, *Heat Kernels and Dirac Operators*, Springer, 1992. [DOI record](https://doi.org/10.1007/978-3-642-58088-8). Relevant: Chapter 3, Clifford modules and Dirac-type operators.
