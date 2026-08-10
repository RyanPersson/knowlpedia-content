+++
id = "langlands-letter/knowls/maximal-compact-hyperspecial"
title = "Maximal compact and hyperspecial subgroups"
kind = "definition"
summary = "Maximal compact subgroups and the more restrictive hyperspecial compact opens arising from reductive integral models."
aliases = ["maximal-compact-hyperspecial", "Maximal Compact and Hyperspecial Subgroup"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/maximal-compact-hyperspecial.md"
section_mode = "progressive"
+++

A **maximal compact subgroup** of a [[topology/locally-compact-group|locally compact group]] is a compact
subgroup maximal under inclusion. For a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
nonarchimedean local field \(F\), maximal compact subgroups are open.

Let \(\mathcal O_F\) be the valuation ring. A compact open subgroup
\(K\subset G(F)\) is **hyperspecial** if there is a smooth affine reductive
[[algebraic-geometry-foundations/group-scheme|group scheme]] \(\mathcal G/\mathcal O_F\), with generic fiber \(G\), such
that

\[
K=\mathcal G(\mathcal O_F).
\]

Requiring the special fiber of \(\mathcal G\) to remain reductive
distinguishes a hyperspecial subgroup from a general parahoric subgroup.

## Existence

A connected reductive \(F\)-group admits a hyperspecial subgroup exactly
when it is unramified: it is quasi-split over \(F\) and becomes split over
an unramified extension. Every hyperspecial subgroup is maximal compact,
but a maximal compact subgroup need not be hyperspecial.

For \(\operatorname{GL}_n(F)\), the subgroup
\(\operatorname{GL}_n(\mathcal O_F)\) is hyperspecial.

## Archimedean distinction

For a real reductive group, a maximal compact subgroup is an archimedean
[[lie-groups/lie-subgroup|Lie subgroup]], such as \(\operatorname O(n)\subset\operatorname{GL}_n(\mathbb
R)\). There is no hyperspecial notion at an archimedean place. Bundling
these phrases in one historical page should not blur the local-field
distinction.

## Spherical role

If \(K\) is hyperspecial, an [[algebra-representation-theory/irreducible-representation|irreducible representation]] with
\(\pi^K\neq0\) is [[harmonic-analysis/unramified-representation-p-adic-group|
unramified]], and the
[[langlands-letter/knowls/spherical-hecke-algebra-satake|spherical Hecke
algebra]] acts on its one-dimensional fixed line. The groups
denoted \(G_{\mathbb Z_p}\) in the letter have this role at almost all
places.

## References

1. François Bruhat and Jacques Tits, “Groupes réductifs sur un corps local
   II,” *Publications Mathématiques de l'IHÉS* 60 (1984), 5–184.
   [Numdam](https://www.numdam.org/item/PMIHES_1984__60__5_0/).
2. Jacques Tits, “Reductive groups over local fields,” Proc. Sympos. Pure
   Math. 33, part 1, 1979.
