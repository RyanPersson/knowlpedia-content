+++
id = "differential-geometry/dolbeault-cohomology"
title = "Dolbeault cohomology"
kind = "definition"
summary = "The cohomology of the d-bar complex of smooth differential forms on a complex manifold."
aliases = ["Dolbeault cohomology group", "d-bar cohomology"]
domains = ["differential-geometry", "algebra-homological"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. Its **Dolbeault cohomology group of bidegree \((p,q)\)** is the [[algebra-homological/cohomology-module|cohomology]]
\[
H_{\bar\partial}^{p,q}(X)
=\frac{\ker\bigl(\bar\partial:\Omega^{p,q}(X)\to\Omega^{p,q+1}(X)\bigr)}
{\operatorname{im}\bigl(\bar\partial:\Omega^{p,q-1}(X)\to\Omega^{p,q}(X)\bigr)}
\]
of the [[differential-geometry/dolbeault-complex|Dolbeault complex]] in degree \(q\). Its elements are classes of smooth \(\bar\partial\)-closed \((p,q)\)-forms, with two representatives equivalent when their difference is \(\bar\partial\)-exact. This is a complex [[linear-algebra/vector-space|vector space]] depending only on the complex structure of \(X\), not on a chosen [[fiber-bundles/hermitian-metric|Hermitian metric]].
Both bidegrees are part of the invariant and must be specified.

## Sheaf-cohomological interpretation

The Dolbeault theorem gives a [[algebra-category-theory/natural-isomorphism|natural isomorphism]]
\[
H_{\bar\partial}^{p,q}(X)\cong H^q(X,\Omega_X^p),
\]
where \(\Omega_X^p\) is the sheaf of holomorphic \(p\)-forms. The proof uses the Dolbeault lemma and the fine resolution by smooth \((p,\bullet)\)-forms [Wells, Chapter II, §3, Theorem 3.17]. This identifies an analytic quotient of differential forms with a sheaf-cohomological invariant.

## Products and functoriality

Wedge product descends to a bigraded product
\[
H_{\bar\partial}^{p,q}(X)\times H_{\bar\partial}^{r,s}(X)
\longrightarrow H_{\bar\partial}^{p+r,q+s}(X).
\]
A [[differential-geometry/holomorphic-map|holomorphic map]] \(f:X\to Y\) preserves form type and commutes with \(\bar\partial\), so pullback induces maps \(f^*:H_{\bar\partial}^{p,q}(Y)\to H_{\bar\partial}^{p,q}(X)\).

In degree \(q=0\), there are no incoming coboundaries, and \(H_{\bar\partial}^{p,0}(X)\) is exactly the space of global holomorphic \(p\)-forms. A \(\bar\partial\)-closed form that is itself \(\bar\partial\)-exact represents zero rather than a new class.

## Relation to de Rham cohomology

Dolbeault cohomology keeps track of bidegree, whereas de Rham cohomology uses the total [[fiber-bundles/exterior-derivative|exterior derivative]]. On a compact [[differential-geometry/kahler-manifold|Kähler manifold]], Hodge theory yields the decomposition
\[
H^k_{\mathrm{dR}}(X;\mathbb C)
\cong\bigoplus_{p+q=k}H_{\bar\partial}^{p,q}(X),
\]
but such a direct-sum identification need not hold for a general complex manifold [Voisin, §6.1].

## References

1. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter II, §3, especially Theorem 3.17, the Dolbeault theorem.
2. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §2.3.3 for the Dolbeault complex and §6.1 for Hodge decomposition.
