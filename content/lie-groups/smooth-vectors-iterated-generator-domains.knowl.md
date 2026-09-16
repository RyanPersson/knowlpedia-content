+++
id = "lie-groups/smooth-vectors-iterated-generator-domains"
title = "Smooth vectors as iterated generator domains"
kind = "theorem"
summary = "Smooth orbit maps are characterized by existence of every finite ordered infinitesimal action."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/smooth-vector-unitary-representation", "lie-groups/ck-vector-unitary-representation", "lie-groups/infinitesimal-generator-unitary-representation", "functional-analysis/densely-defined-operator"]
+++

Let \(\pi\) be a strongly continuous unitary representation of a finite-dimensional Lie group \(G\) on \(H\). For \(X\in\mathfrak g\), let \(K_X=iA_X\) be the maximal skew-adjoint [[lie-groups/infinitesimal-generator-unitary-representation|generator]] of \(t\mapsto\pi(\exp(tX))\). Then its [[lie-groups/smooth-vector-unitary-representation|smooth-vector space]] is exactly
\[
H^\infty=
\bigcap_{r\geq1}\ \bigcap_{X_1,\ldots,X_r\in\mathfrak g}
\operatorname{Dom}(K_{X_1}\cdots K_{X_r}).
\]
Products use the usual domains of [[functional-analysis/densely-defined-operator|unbounded operators]], with the rightmost factor applied first.

## What a product domain requires

For example,
\[
\operatorname{Dom}(K_XK_Y)
=\{v\in\operatorname{Dom}(K_Y):K_Yv\in\operatorname{Dom}(K_X)\}.
\]
It is not enough that \(v\) separately belong to both generator domains. Requiring the analogous condition for all finite words supplies one common domain closed under every derived action.

## Finite differentiability

The [[lie-groups/ck-vector-unitary-representation|\(C^k\)-vector space]] is the intersection of these domains for \(1\leq r\leq k\). In particular, first derivatives in all directions give \(H^1\), not automatically \(H^\infty\). The restriction to a finite-dimensional Lie group is part of the statement; arbitrary infinite-dimensional groups require additional hypotheses.

## Relation to a single regularity operator

The same smooth space is the intersection of the domains of all powers of the closed [[lie-groups/nelson-laplacian|Nelson Laplacian]]. The word-domain formulation records each infinitesimal direction, while the Laplacian packages the regularity into one operator.

## References

1. Karl-Hermann Neeb, [*On Differentiable Vectors for Representations of Infinite Dimensional Lie Groups*](https://arxiv.org/abs/1002.1602). Definition 3.1(c)–(d), Theorem 9.4, specialized to finite-dimensional groups.
