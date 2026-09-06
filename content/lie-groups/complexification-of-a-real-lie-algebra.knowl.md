+++
id = "lie-groups/complexification-of-a-real-lie-algebra"
title = "Complexification of a real Lie algebra"
kind = "construction"
summary = "The complex Lie algebra obtained by extending scalars from the real numbers to the complex numbers."
aliases = ["complexified Lie algebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/lie-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a real [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak h\), its **complexification** is
\[
\mathfrak h_{\mathbb C}:=\mathfrak h\otimes_{\mathbb R}\mathbb C,
\]
with the unique complex-bilinear bracket satisfying
\[
[X\otimes z,Y\otimes w]=[X,Y]\otimes zw.
\]
The map \(X\mapsto X\otimes1\) identifies \(\mathfrak h\) with a real [[lie-groups/lie-subalgebra|Lie subalgebra]], and \(\dim_{\mathbb C}\mathfrak h_{\mathbb C}=\dim_{\mathbb R}\mathfrak h\).

## Universal property and conjugation

Every real-linear [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]] from \(\mathfrak h\) to the underlying real algebra of a complex Lie algebra extends uniquely to a complex-linear homomorphism from \(\mathfrak h_{\mathbb C}\). Complex conjugation on the second tensor factor is an antilinear involution whose fixed Lie algebra is \(\mathfrak h\).

Complexification must not be confused with [[lie-groups/underlying-real-lie-algebra|forgetting complex scalars]]. If \(\mathfrak g\) is complex, then
\[
(\mathfrak g_{\mathbb R})_{\mathbb C}\cong\mathfrak g\oplus\overline{\mathfrak g},
\]
not generally \(\mathfrak g\) alone.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, §I.3. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Jean-Pierre Serre, *Complex Semisimple Lie Algebras*, Springer, 1987, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-3910-7).
