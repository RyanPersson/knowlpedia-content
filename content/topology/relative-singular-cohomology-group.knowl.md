+++
id = "topology/relative-singular-cohomology-group"
title = "Relative singular cohomology group"
kind = "definition"
summary = "The cohomology of the cochain complex dual to the relative singular chain complex of a pair of spaces."
aliases = ["relative cohomology", "relative singular cohomology"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/singular-chain-complex", "algebra-groups/abelian-group", "algebra-homological/cohomology-module", "algebra-homological/cochain-complex", "algebra-groups/quotient-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Fix an integer \(n\ge0\), using zero chain and cochain groups in negative degrees. Let \(A\subseteq X\) be a subspace of a topological space \(X\), and let \(G\) be an abelian group. The inclusion gives a subcomplex \(C_\bullet(A;\mathbb Z)\subseteq C_\bullet(X;\mathbb Z)\). The **relative singular chain group** is

\[
C_n(X,A;\mathbb Z):=C_n(X;\mathbb Z)/C_n(A;\mathbb Z),
\]

and the boundary on \(C_\bullet(X;\mathbb Z)\) induces a boundary on these quotient groups because \(C_\bullet(A;\mathbb Z)\) is a subcomplex. The relative cochains with coefficients in \(G\) are

\[
C^n(X,A;G):=\operatorname{Hom}\!\bigl(C_n(X,A;\mathbb Z),G\bigr).
\]

Their coboundary is \(\delta\varphi=\varphi\circ\partial\). The **\(n\)th relative singular cohomology group** is

\[
H^n(X,A;G):=
\ker(\delta:C^n(X,A;G)\to C^{n+1}(X,A;G))
/\operatorname{im}(\delta:C^{n-1}(X,A;G)\to C^n(X,A;G)).
\]

Thus relative cohomology is the cohomology of the cochain complex dual to the quotient chain complex of the pair. When \(A=\varnothing\), this recovers ordinary singular cohomology \(H^n(X;G)\).

## Maps of pairs

A continuous map of pairs \(f:(X,A)\to(Y,B)\), meaning \(f:X\to Y\) with \(f(A)\subseteq B\), induces a pullback

\[
f^*:H^n(Y,B;G)\longrightarrow H^n(X,A;G).
\]

The short exact sequence of chain complexes \(0\to C_\bullet(A;\mathbb Z)\to C_\bullet(X;\mathbb Z)\to C_\bullet(X,A;\mathbb Z)\to0\) yields the long exact sequence of the pair.


## Cup product with an absolute class

For coefficients in a commutative ring \(R\), the usual cochain cup product restricts to
\[
H^p(X;R)\times H^q(X,A;R)\longrightarrow H^{p+q}(X,A;R).
\]
Indeed, a relative cochain is an absolute cochain vanishing on chains in \(A\); its product with an absolute cochain still vanishes on such chains. This gives relative cohomology a module structure over the absolute cohomology ring.
