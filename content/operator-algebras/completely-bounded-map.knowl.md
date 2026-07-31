+++
id = "operator-algebras/completely-bounded-map"
title = "Completely bounded map"
kind = "definition"
summary = "A linear map whose entrywise matrix amplifications have uniformly bounded operator norms."
aliases = ["CB map", "completely bounded linear map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be \(C^*\)-algebras and let \(\phi:A\to B\) be linear. For
each \(n\geq1\), its **matrix amplification** is the entrywise map
\[
\phi^{(n)}:M_n(A)\longrightarrow M_n(B),\qquad
[a_{ij}]\longmapsto[\phi(a_{ij})],
\]
where the domain and codomain carry their canonical
[[operator-algebras/matrix-cstar-algebra|matrix \(C^*\)-algebra]] norms. The
map \(\phi\) is **completely bounded** if
\[
\lVert\phi\rVert_{\mathrm{cb}}
=\sup_{n\geq1}\lVert\phi^{(n)}\rVert<\infty.
\]
The number \(\lVert\phi\rVert_{\mathrm{cb}}\) is its completely bounded norm.
It measures \(\phi\) simultaneously at every matrix level, rather than only
on \(A\). No positivity, multiplicativity, or unitality is part of the
definition.

## Fundamental examples

Every [[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is completely
contractive. Every bounded scalar-valued functional is completely bounded with
the same norm. A [[operator-algebras/completely-positive-map|completely positive map]] is completely bounded; when its domain is unital,
\(\lVert\phi\rVert_{\mathrm{cb}}=\lVert\phi(1)\rVert\). These examples explain
why the matrix norm, rather than only the ordinary [[linear-algebra/operator-norm|operator norm]], is natural
for maps between operator algebras
[Paulsen, Chapters 3 and 8].

## Structure and consequences

Compositions satisfy
\[
\lVert\psi\mathbin{\circ}\phi\rVert_{\mathrm{cb}}
\leq\lVert\psi\rVert_{\mathrm{cb}}\lVert\phi\rVert_{\mathrm{cb}},
\]
so completely bounded maps form the morphisms of the operator-space category.
For maps into \(B(H)\), Wittstock's decomposition theorem expresses every
completely bounded map as a [[convex-analysis/linear-combination|linear combination]] of completely positive maps;
equivalently, it admits a Stinespring-type factorization with bounded
coefficients [Paulsen, Chapter 8].

## Bounded versus completely bounded

Ordinary boundedness controls only the level \(n=1\). The transpose map on
\(M_k(\mathbb C)\) has operator norm \(1\) but completely bounded norm \(k\),
so amplification can reveal behavior invisible at the first level. On a fixed
finite-dimensional operator space every bounded map is completely bounded,
but no dimension-free comparison follows
[Paulsen, Chapter 8].

**Warning.** Complete boundedness and
[[operator-algebras/positive-linear-map|positivity]] are independent without
extra hypotheses; “completely” refers to uniform matrix-level control.

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapters 3 and 8 on completely positive maps, completely bounded maps, amplifications, and the cb norm.
