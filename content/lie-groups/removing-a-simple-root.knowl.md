+++
id = "lie-groups/removing-a-simple-root"
title = "Removing a simple root"
kind = "construction"
summary = "Deleting a Dynkin-diagram vertex to obtain a full root subsystem, a regular semisimple subalgebra, and a Levi subalgebra."
aliases = ["removing a simple root", "deleting a simple root", "deleting a Dynkin node"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] with Cartan subalgebra \(\mathfrak h\), root system \(\Phi\), and simple roots \(\Delta\). To **remove the simple root** \(\alpha_0\in\Delta\), set
\[
I=\Delta\setminus\{\alpha_0\},
\qquad
\Phi_I=\Phi\cap\operatorname{span}_{\mathbb Z}(I).
\]
The set \(\Phi_I\) is the full [[lie-groups/root-subsystem|root subsystem]] whose [[lie-groups/dynkin-diagram|Dynkin diagram]] is obtained by deleting the vertex \(\alpha_0\) and its incident edges.

## Two associated subalgebras

Let \(\mathfrak h_I\) be the span in \(\mathfrak h\) of the coroots \(h_\alpha=[e_\alpha,e_{-\alpha}]\) for \(\alpha\in I\). Deleting \(\alpha_0\) gives the regular semisimple subalgebra
\[
\mathfrak g_I
=\mathfrak h_I\oplus\bigoplus_{\beta\in\Phi_I}\mathfrak g_\beta.
\]
Its rank is one less than that of \(\mathfrak g\).

Retaining the whole Cartan instead gives
\[
\mathfrak l_I
=\mathfrak h\oplus\bigoplus_{\beta\in\Phi_I}\mathfrak g_\beta.
\]
This is a [[lie-groups/maximal-levi-subalgebra|maximal Levi subalgebra]], with
\[
\mathfrak l_I=\mathfrak g_I\oplus Z(\mathfrak l_I)
\]
and one-dimensional center.

## Caution about the Cartan part

The Cartan subalgebra of the semisimple algebra \(\mathfrak g_I\) is the span of the retained coroots. It is generally **not** the kernel of the deleted simple root \(\alpha_0:\mathfrak h\to\mathbb C\). The coroot span is what ensures that brackets \([\mathfrak g_\beta,\mathfrak g_{-\beta}]\) remain inside \(\mathfrak g_I\).

## Iteration

Removing several simple roots amounts to choosing a smaller subset \(I\subseteq\Delta\). Iterating the construction produces chains of [[lie-groups/regular-lie-subalgebra|regular subalgebras]]. For example, suitable successive deletions give the exceptional chain
\[
A_2\sqcup A_1\subset A_4\subset D_5\subset E_6\subset E_7.
\]

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§8, 14. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §2. [arXiv record](https://arxiv.org/abs/2608.06271).
