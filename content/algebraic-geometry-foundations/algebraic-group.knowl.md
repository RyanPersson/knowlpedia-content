+++
id = "algebraic-geometry-foundations/algebraic-group"
title = "Algebraic group"
kind = "definition"
summary = "A group scheme of finite type over a field."
aliases = ["algebraic group"]
domains = ["algebraic-geometry-foundations", "lie-groups"]
section_mode = "progressive"
+++

An **algebraic group** over a field \(k\) is a
[[algebraic-geometry-foundations/group-scheme|group scheme]] \(G\) of finite
type over \(k\). Thus \(G\) has multiplication, identity, and inversion
morphisms
\[
m:G\times_kG\to G,\qquad e:\operatorname{Spec}k\to G,\qquad i:G\to G
\]
satisfying the group axioms as identities of morphisms.

An algebraic group is **linear** if its underlying scheme is affine.
Equivalently, it admits a closed immersion into \(GL_n\) for some \(n\).
Projective algebraic groups, such as abelian varieties, need not be linear.

## Points

For every \(k\)-algebra \(R\), the set \(G(R)\) is a group, functorially in
\(R\). The abstract group \(G(k)\) does not by itself determine the
scheme-theoretic structure of \(G\).

## References

1. T. A. Springer, *Linear Algebraic Groups*, 2nd ed., Birkhäuser, 1998.
   [DOI](https://doi.org/10.1007/978-0-8176-4840-4).
