+++
id = "fiber-bundles/invariant-polynomial-on-a-lie-algebra"
title = "Invariant polynomial on a Lie algebra"
kind = "definition"
summary = "A polynomial on a Lie algebra that is unchanged by the adjoint action of its Lie group."
aliases = ["Ad-invariant polynomial", "invariant symmetric polynomial"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\). A homogeneous **invariant polynomial of degree \(k\)** is an element \(p\in\operatorname{Sym}^k(\mathfrak g^*)\) fixed by the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]]. Equivalently, regarding \(p\) as a symmetric \(k\)-linear form,
\[
p(\operatorname{Ad}_gX_1,\ldots,\operatorname{Ad}_gX_k)=p(X_1,\ldots,X_k)
\]
for all \(g\in G\) and \(X_i\in\mathfrak g\). A nonhomogeneous invariant polynomial is a finite sum of homogeneous ones. The acting group is part of the data when \(G\) is disconnected, because invariance under its identity component can be weaker than invariance under all of \(G\).

## Infinitesimal characterization

If \(G\) is connected, invariance is equivalent to
\[
\sum_{i=1}^{k}p(X_1,\ldots,[Y,X_i],\ldots,X_k)=0
\]
for every \(Y,X_1,\ldots,X_k\in\mathfrak g\). This is obtained by differentiating the group invariance condition. For a disconnected group it tests only invariance under the identity component, so the remaining components must be checked separately.

The invariant polynomials form a graded subalgebra
\[
\operatorname{Sym}(\mathfrak g^*)^G\subseteq\operatorname{Sym}(\mathfrak g^*).
\]

## Examples

For \(\mathfrak g=\mathfrak{gl}_n\), the functions \(X\mapsto\operatorname{tr}(X^r)\) and the coefficients of the characteristic polynomial are invariant under conjugation.

An invariant symmetric bilinear form \(B\) gives the quadratic polynomial \(X\mapsto B(X,X)\). The Killing form supplies a standard example when it is nonzero.

On \(\mathfrak{so}(2m)\), the Pfaffian is invariant under the adjoint action of \(SO(2m)\). It is the polynomial used to construct the Euler form.

## Role in characteristic classes

Applying a degree-\(k\) invariant polynomial to the curvature of a principal connection produces a [[fiber-bundles/chernweil-form|Chern–Weil form]] of degree \(2k\). Adjoint invariance is exactly what permits this curvature expression to descend from the principal bundle to the base; the Bianchi identity then gives closedness [Bott and Tu, chapter 11](https://doi.org/10.1007/978-1-4757-3951-0).

## Conventions and scope

Authors alternate between a polynomial function \(P(X)\) and its polarized symmetric multilinear form \(p(X_1,\ldots,X_k)\). Over \(\mathbb R\) or \(\mathbb C\) these descriptions are equivalent, but normalization factors such as \(k!\) vary.

**Warning.** Infinitesimal invariance for a Lie algebra does not by itself impose invariance under disconnected components of a chosen integrating group.

## References

1. R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: chapter 11, invariant polynomials and the Chern–Weil homomorphism.
2. S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, vol. II, Wiley, 1969. [Publisher record](https://www.wiley.com/en-us/Foundations+of+Differential+Geometry%2C+Volume+2-p-9780471157328). Relevant: chapter XII, invariant polynomials and characteristic forms.
