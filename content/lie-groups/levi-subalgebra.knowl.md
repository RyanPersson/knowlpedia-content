+++
id = "lie-groups/levi-subalgebra"
title = "Levi subalgebra"
kind = "definition"
summary = "A reductive subalgebra obtained from a subset of simple roots by retaining the full Cartan and the corresponding root spaces."
aliases = ["Levi subalgebra", "standard Levi subalgebra"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]], choose a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] \(\mathfrak h\), a [[lie-groups/root-system|root system]] \(\Phi\), and a base \(\Delta\) of [[lie-groups/simple-root|simple roots]]. For \(I\subseteq\Delta\), put
\[
\Phi_I=\Phi\cap\operatorname{span}_{\mathbb Z}(I).
\]
The associated **standard Levi subalgebra** is
\[
\mathfrak l_I
=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi_I}\mathfrak g_\alpha.
\]
A **Levi subalgebra** of \(\mathfrak g\) is a subalgebra conjugate under an [[algebra-groups/inner-automorphism|inner automorphism]] to some \(\mathfrak l_I\).

## Structure

The [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak l_I\) is [[lie-groups/reductive-lie-algebra|reductive]]. Its derived algebra and center are
\[
[\mathfrak l_I,\mathfrak l_I]
=\mathfrak h_I\oplus\bigoplus_{\alpha\in\Phi_I}\mathfrak g_\alpha,
\qquad
Z(\mathfrak l_I)
=\{H\in\mathfrak h:\alpha(H)=0\text{ for every }\alpha\in I\},
\]
where \(\mathfrak h_I\) is the span of the coroots belonging to \(I\). Thus
\[
\mathfrak l_I=Z(\mathfrak l_I)\oplus[\mathfrak l_I,\mathfrak l_I],
\]
and the semisimple summand has root system \(\Phi_I\).

## Relation to the Dynkin diagram

The [[lie-groups/dynkin-diagram|Dynkin diagram]] of \([\mathfrak l_I,\mathfrak l_I]\) is the subdiagram induced by the vertices in \(I\). The entire \(\mathfrak l_I\), however, retains the full Cartan subalgebra \(\mathfrak h\), so every Levi subalgebra has the same rank as \(\mathfrak g\).

Levi subalgebras are precisely the reductive factors of parabolic subalgebras. This use of “Levi” is related to, but more specific than, a Levi factor in the [[lie-groups/levi-decomposition-theorem|Levi decomposition]] of an arbitrary finite-dimensional Lie algebra.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter II. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 7–9*, Springer, 2005, Chapter VIII, §3. [Publisher record](https://link.springer.com/book/9783540688518).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §2. [arXiv record](https://arxiv.org/abs/2608.06271).
