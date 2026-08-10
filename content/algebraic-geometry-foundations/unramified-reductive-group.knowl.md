+++
id = "algebraic-geometry-foundations/unramified-reductive-group"
title = "Unramified reductive group"
kind = "definition"
summary = "A reductive group over a nonarchimedean local field that is quasi-split and splits over an unramified extension."
aliases = ["unramified group", "unramified connected reductive group"]
domains = ["algebraic-geometry-foundations", "langlands", "algebra-groups"]
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|nonarchimedean local
field]]. A connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]] \(G\) is **unramified** if it is
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]] over
\(F\) and becomes split over a finite
[[langlands-letter/knowls/unramified-extension-local|unramified extension]] of
\(F\).

This is a property of the
[[algebraic-geometry-foundations/algebraic-group|algebraic group]] \(G/F\),
not of a representation of
the [[topology/locally-compact-group|locally compact group]] \(G(F)\).

## Integral model and hyperspecial subgroup

Equivalently, \(G\) extends to a reductive
[[algebraic-geometry-foundations/group-scheme|group scheme]]
\(\mathcal G\) over the
[[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_F\).
Then
\(\mathcal G(\mathcal O_F)\) is a
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial maximal
compact subgroup]] of \(G(F)\).  Conversely, the existence of a hyperspecial
vertex in the Bruhat–Tits building characterizes unramified \(G\).

The choice of integral model or hyperspecial subgroup is generally not unique,
even though unramifiedness is intrinsic.

## Langlands use

For an unramified group and a chosen hyperspecial subgroup, the spherical
Hecke algebra has a normalized
[[langlands-letter/knowls/spherical-hecke-algebra-satake|Satake isomorphism]].
Its [[algebra-representation-theory/character|characters]] correspond to
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
[[algebra-groups/conjugacy-class|conjugacy classes]] in the unramified
part of the [[langlands/l-group|L-group]].

## References

1. François Bruhat and Jacques Tits, “Groupes réductifs sur un corps local.
   II. Schémas en groupes. Existence d'une donnée radicielle valuée,”
   *Publications Mathématiques de l'IHÉS* 60 (1984), 5–184.
   [Numdam](https://www.numdam.org/item/PMIHES_1984__60__5_0/).
2. Jacques Tits, “Reductive groups over local fields,” in *Automorphic Forms,
   Representations and L-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 1, 1979.
