+++
id = "differential-geometry/dolbeault-complex"
title = "Dolbeault complex"
kind = "definition"
summary = "The cochain complex of smooth forms of fixed holomorphic degree with differential given by the d-bar operator."
aliases = ["d-bar complex", "∂̄-complex"]
domains = ["differential-geometry", "algebra-homological"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] of complex dimension \(n\), and fix \(0\leq p\leq n\). The **Dolbeault complex in holomorphic degree \(p\)** is the [[algebra-homological/cochain-complex|cochain complex]]
\[
0\longrightarrow\Omega^{p,0}(X)\xrightarrow{\bar\partial}
\Omega^{p,1}(X)\xrightarrow{\bar\partial}\cdots
\xrightarrow{\bar\partial}\Omega^{p,n}(X)\longrightarrow0,
\]
where \(\Omega^{p,q}(X)\) is the complex [[linear-algebra/vector-space|vector space]] of smooth \((p,q)\)-forms and \(\bar\partial\) is the \((0,1)\) [[differential-geometry/dolbeault-operators|Dolbeault operator]]. The identity \(\bar\partial^2=0\) makes consecutive arrows compose to zero. Unless \(p\) is specified, “the Dolbeault complex” may also mean the resulting family over all \(p\).
Each vector space and arrow is complex-linear, and the cochain grading is the antiholomorphic form degree \(q\).

## Local exactness and sheaves

The Dolbeault lemma says that every \(\bar\partial\)-closed \((p,q)\)-form with \(q>0\) is locally \(\bar\partial\)-exact. Consequently, the sheaf version
\[
0\longrightarrow\Omega_X^p\longrightarrow\mathcal A_X^{p,0}
\xrightarrow{\bar\partial}\mathcal A_X^{p,1}\longrightarrow\cdots
\]
is a fine resolution of the sheaf \(\Omega_X^p\) of holomorphic \(p\)-forms.

## Structure and examples

For \(p=0\), the kernel of the first arrow consists exactly of holomorphic functions. More generally, the degree-zero cocycles are holomorphic \(p\)-forms. In complex dimension one, each fixed-\(p\) complex has only the two potentially nonzero terms \(\Omega^{p,0}(X)\) and \(\Omega^{p,1}(X)\).

Wedge product makes the direct sum over \(p\) and \(q\) into a bigraded differential algebra: if \(\alpha\) has total degree \(k\), then
\[
\bar\partial(\alpha\wedge\beta)
=\bar\partial\alpha\wedge\beta+(-1)^k\alpha\wedge\bar\partial\beta.
\]

## Conventions and scope

Some authors reserve “Dolbeault complex” for the \(p=0\) row and call the general object the \(p\)th Dolbeault complex. The construction requires an integrable complex structure. On a general almost-complex manifold, the [[fiber-bundles/exterior-derivative|exterior derivative]] can have additional type components, so the displayed sequence need not be a complex.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §2.3.3, the Dolbeault complex of a holomorphic bundle.
2. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter II, §3, especially Theorem 3.17, the Dolbeault theorem.
