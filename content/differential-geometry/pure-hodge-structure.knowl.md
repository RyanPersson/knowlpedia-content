+++
id = "differential-geometry/pure-hodge-structure"
title = "Pure Hodge structure"
kind = "definition"
summary = "A finite-dimensional real vector space whose complexification decomposes into conjugate bidegree pieces of fixed total weight."
aliases = ["Hodge structure of weight n"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

A **pure real Hodge structure of weight \(n\)** is a finite-dimensional real [[linear-algebra/vector-space|vector space]] \(V_{\mathbb R}\) together with a direct-sum decomposition of its [[linear-algebra/complexification|complexification]]
\[
V_{\mathbb C}=V_{\mathbb R}\otimes_{\mathbb R}\mathbb C
=\bigoplus_{p+q=n}V^{p,q}
\]
such that complex conjugation relative to \(V_{\mathbb R}\) satisfies
\(\overline{V^{p,q}}=V^{q,p}\). The integers \(p\) and \(q\) may be negative unless an effectiveness condition is imposed. A pure rational Hodge structure is defined in the same way from a finite-dimensional \(\mathbb Q\)-vector space, and an integral Hodge structure starts with a finite-rank free [[algebra-groups/abelian-group|abelian group]].

## Filtration formulation

The decomposition determines the decreasing [[differential-geometry/hodge-filtration|Hodge filtration]]
\[
F^pV_{\mathbb C}=\bigoplus_{r\geq p}V^{r,n-r}.
\]
Conversely, a filtration defines a pure real Hodge structure of weight \(n\) exactly when
\[
V_{\mathbb C}=F^pV_{\mathbb C}\oplus\overline{F^{\,n-p+1}V_{\mathbb C}}
\]
for every \(p\). Then \(V^{p,q}=F^p\cap\overline{F^q}\) [Voisin, §7.1.1](https://doi.org/10.1017/CBO9780511615344.008).

## Geometric example

For a compact [[differential-geometry/kahler-manifold|Kähler manifold]] \(X\), the decomposition
\[
H^k(X,\mathbb C)=\bigoplus_{p+q=k}H^{p,q}(X)
\]
makes \(H^k(X,\mathbb R)\) a pure real Hodge structure of weight \(k\). The integral lattice \(H^k(X,\mathbb Z)\) modulo torsion gives an integral Hodge structure. The conjugation condition follows from conjugation of differential forms.

## Conventions and scope

“Pure” means that every bidegree has the same sum \(p+q=n\); it does not mean that only one bidegree occurs. A mixed Hodge structure has an additional increasing weight filtration whose graded pieces are pure. Authors sometimes build a chosen lattice into the phrase “Hodge structure”; the coefficient ring should therefore always be stated.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Chapter record](https://doi.org/10.1017/CBO9780511615344.008). Relevant: §7.1.1, Hodge structures and their filtration description.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: the appendix on Hodge theory and Chapter 3 on compact Kähler cohomology.
