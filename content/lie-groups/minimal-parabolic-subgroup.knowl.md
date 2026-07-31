+++
id = "lie-groups/minimal-parabolic-subgroup"
title = "Minimal parabolic subgroup"
kind = "definition"
summary = "A parabolic subgroup minimal under inclusion, constructed from a choice of positive restricted roots."
aliases = ["minimal P", "MAN subgroup"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a connected
[[lie-groups/real-reductive-lie-group|real reductive Lie group]]. A **minimal
parabolic subgroup** \(P_0\) is a
[[lie-groups/parabolic-subgroup-real-reductive-group|parabolic subgroup]]
containing no proper parabolic subgroup of \(G\). Choose a Cartan decomposition
\(\mathfrak g=\mathfrak k\oplus\mathfrak p\), a maximal abelian
\(\mathfrak a\subseteq\mathfrak p\), and positive restricted roots. If
\(A=\exp(\mathfrak a)\), \(N\) has [[lie-groups/lie-algebra|Lie algebra]] equal to the sum of the positive
restricted-root spaces, and \(M=Z_K(A)\), then
\[
P_0=MAN
\]
is a minimal parabolic. Every minimal parabolic subgroup is conjugate to one
obtained in this way.

## Relation to the Iwasawa decomposition

The [[lie-groups/iwasawa-decomposition|Iwasawa multiplication map]]
\(K\times A\times N\to G\) is a diffeomorphism.
Replacing \(K\) by its centralizer \(M=Z_K(A)\) gives the subgroup \(P_0=MAN\),
and the Iwasawa decomposition implies \(G=KP_0\). The quotient \(G/P_0\) is
therefore compact and identifies with \(K/M\). These structural facts are
developed in
[Knapp, Chapter VI, §§4–5 and Chapter VII, §7].

## Examples

For \(G=\operatorname{SL}(n,\mathbb R)\), the upper triangular matrices form a
minimal parabolic subgroup. Here \(A\) consists of positive diagonal matrices
of determinant \(1\), \(N\) consists of upper unitriangular matrices, and
\(M\) consists of diagonal sign matrices in \(\operatorname{SO}(n)\). For
\(\operatorname{SL}(2,\mathbb R)\), this subgroup stabilizes a point of the
projective line.

## Conventions and uses

Minimal means minimal among parabolic subgroups, not among all nontrivial
closed subgroups. A minimal parabolic need not be solvable because its compact
factor \(M\) can be nonabelian. It supplies both the induction subgroup for
[[lie-groups/principal-series-representation|minimal principal series]] and the quotient model
[[lie-groups/furstenberg-boundary|\(G/P_0\) of the Furstenberg boundary]].

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/beyond2.html). Relevant: Chapter VI, §§4–5 on Iwasawa decomposition and Chapter VII, §7 on parabolics.
2. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, Mathematical Surveys and Monographs 83, American Mathematical Society, 2000. [AMS record](https://bookstore.ams.org/SURV/83). Relevant: Chapter I on \(KAN\), \(MAN\), and compact homogeneous quotients.
