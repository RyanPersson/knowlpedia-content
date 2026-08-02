+++
id = "lie-groups/real-rank-of-a-reductive-group"
title = "Real rank of a reductive group"
kind = "definition"
summary = "The dimension of a maximal abelian subspace in the noncompact part of a Cartan decomposition."
aliases = ["split rank"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a connected
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] with Lie
algebra \(\mathfrak g\), and choose a
[[lie-groups/cartan-decomposition-real-reductive-lie-algebra|Cartan decomposition]]
\(\mathfrak g=\mathfrak k\oplus\mathfrak p\). If \(\mathfrak a\subseteq
\mathfrak p\) is maximal abelian, the **real rank** of \(G\) is
\[
\operatorname{rank}_{\mathbb R}G=\dim_{\mathbb R}\mathfrak a.
\]
All maximal abelian subspaces of \(\mathfrak p\) are conjugate under the
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]],
so this number is independent of the choices. It is
the rank of the [[lie-groups/restricted-root-system|restricted roots]] when
\(G\) is semisimple. For reductive \(G\), split central directions contribute
to \(\dim\mathfrak a\) even though every restricted root vanishes on them.

## Equivalent split-torus formulation

For a linear real algebraic group, \(\operatorname{rank}_{\mathbb R}G\) is the
dimension of a maximal \(\mathbb R\)-split torus. On the Lie-group side, the
connected subgroup \(A=\exp(\mathfrak a)\) is the corresponding maximal split
abelian subgroup. Any two maximal abelian subspaces of \(\mathfrak p\) are
conjugate under \(K\), so their common dimension is well-defined.

## Examples

The compact group \(\operatorname{SO}(n)\) has real rank \(0\).
\(\operatorname{SL}(n,\mathbb R)\) has real rank \(n-1\), witnessed by the
trace-zero diagonal matrices in \(\mathfrak p\).
\(\operatorname{SO}_0(p,q)\), with \(p\leq q\), has real rank \(p\).
Thus real rank distinguishes compact groups, rank-one groups, and
higher-rank groups even when their complexified [[lie-groups/lie-algebra|Lie algebras]] have comparable
root data.

## Conventions and consequences

For a semisimple group, real rank is zero exactly when the group is compact up
to finite covering and finite center. For a reductive group, a noncompact split
center contributes to the displayed definition; “real semisimple rank”
sometimes means the real rank after removing that center. Real rank should not
be confused with the rank of a maximal torus or with complex rank.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/beyond2.html). Relevant: Chapter VI, §§2–5 on Cartan and Iwasawa decompositions, and Chapter VI, §11 on restricted roots.
2. Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, corrected reprint, Graduate Studies in Mathematics 34, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapter VI on symmetric spaces of noncompact type and their rank.
