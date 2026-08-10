+++
id = "lie-groups/maximal-levi-subalgebra"
title = "Maximal Levi subalgebra"
kind = "definition"
summary = "A proper Levi subalgebra maximal among proper Levi subalgebras, obtained by deleting one simple root."
aliases = ["maximal Levi subalgebra", "maximal proper Levi subalgebra"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

A **maximal Levi subalgebra** of a complex semisimple Lie algebra \(\mathfrak g\) is a proper [[lie-groups/levi-subalgebra|Levi subalgebra]] that is maximal, under inclusion, among proper Levi subalgebras of \(\mathfrak g\).

After choosing simple roots \(\Delta\), every standard maximal Levi subalgebra has the form
\[
\mathfrak l_{\Delta\setminus\{\alpha_0\}}
=\mathfrak h\oplus
\bigoplus_{\beta\in\Phi\cap
\operatorname{span}_{\mathbb Z}(\Delta\setminus\{\alpha_0\})}
\mathfrak g_\beta
\]
for one \(\alpha_0\in\Delta\). Thus it is obtained by [[lie-groups/removing-a-simple-root|removing one simple root]] from the semisimple root data while retaining the full Cartan subalgebra \(\mathfrak h\).

## Structure

If \(\mathfrak g\) is semisimple, the derived algebra of this maximal Levi has the Dynkin diagram obtained by deleting the vertex \(\alpha_0\) and all incident edges. Its center is one-dimensional:
\[
\dim Z\!\left(\mathfrak l_{\Delta\setminus\{\alpha_0\}}\right)=1.
\]
The Levi subalgebra itself has [[lie-groups/maximal-rank-lie-subalgebra|maximal rank]] in \(\mathfrak g\).

## Important distinction

“Maximal Levi” does not ordinarily mean [[lie-groups/maximal-lie-subalgebra|maximal among all Lie subalgebras]]. A proper Levi subalgebra lies inside the corresponding proper parabolic subalgebra, so there is usually a larger proper subalgebra between it and \(\mathfrak g\).

For example, deleting a suitable node from the \(A_4\) diagram gives a semisimple part of type \(A_2\sqcup A_1\); retaining the Cartan contributes a one-dimensional center, producing a reductive algebra isomorphic to
\[
\mathfrak{sl}_3\oplus\mathfrak{sl}_2\oplus\mathbb C.
\]

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter II. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §2. [arXiv record](https://arxiv.org/abs/2608.06271).
