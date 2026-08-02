+++
id = "lie-groups/iwasawa-decomposition"
title = "Iwasawa decomposition"
kind = "theorem"
summary = "The canonical KAN factorization of a real reductive Lie group after choices of Cartan and positive restricted-root data."
aliases = ["KAN decomposition", "Iwasawa theorem"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie
group]] with [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal
compact subgroup]] \(K\). Choose a maximal abelian subspace
\(\mathfrak a\subseteq\mathfrak p\), positive restricted roots
\(\Sigma^+\), and set
\[
\mathfrak n=\bigoplus_{\alpha\in\Sigma^+}\mathfrak g_\alpha,\qquad
A=\exp\mathfrak a,\qquad N=\exp\mathfrak n.
\]
The **Iwasawa decomposition** is the theorem that multiplication
\[
K\times A\times N\longrightarrow G,\qquad(k,a,n)\longmapsto kan,
\]
is a diffeomorphism. In particular, every \(g\in G\) has a unique factorization
\(g=k(g)a(g)n(g)\) relative to these choices.

## Construction from restricted roots

The algebraic statement behind the theorem is
\(\mathfrak g=\mathfrak k\oplus\mathfrak a\oplus\mathfrak n\) as real vector
spaces. Here \(\mathfrak n\) is nilpotent because brackets add positive
restricted roots. Exponentiation is a diffeomorphism from \(\mathfrak n\) to
the simply connected [[algebra-groups/nilpotent-group|nilpotent group]] \(N\).

## Minimal parabolic subgroup

Let \(M=Z_K(A)\). Then \(P=MAN\) is a [[lie-groups/minimal-parabolic-subgroup|minimal parabolic subgroup]], with \(M\)
compact modulo a possible finite central feature in the usual conventions.
Characters and representations of \(MAN\), extended trivially across \(N\)
and induced to \(G\), produce principal-series representations. Thus \(KAN\)
is more than a coordinate system: it supplies the subgroup data used in
parabolic induction.

## Example and comparison

For \(G=\mathrm{SL}_n(\mathbb R)\), take \(K=\mathrm{SO}(n)\), \(A\) the
positive diagonal determinant-one matrices, and \(N\) the upper unitriangular
matrices. The decomposition becomes the QR factorization with a normalized
diagonal. Unlike the
[[lie-groups/global-cartan-decomposition|\(KAK\) decomposition]], \(KAN\)
is uniquely ordered and asymmetric, reflecting the choice of [[lie-groups/positive-root|positive roots]].

## References

1. A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [Publisher record](https://link.springer.com/book/9780817642594). Relevant: Chapter VI, §5.
2. S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapter IX on the Iwasawa decomposition.
