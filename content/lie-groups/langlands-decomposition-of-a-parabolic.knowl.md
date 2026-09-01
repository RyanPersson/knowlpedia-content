+++
id = "lie-groups/langlands-decomposition-of-a-parabolic"
title = "Langlands decomposition of a parabolic subgroup"
kind = "theorem"
summary = "A real parabolic subgroup decomposes into a reductive factor, a split abelian factor, and a nilpotent radical."
aliases = ["Levi decomposition P=MAN", "Langlands decomposition"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/cartan-involution-real-lie-algebra", "lie-groups/parabolic-subgroup-real-reductive-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] with a fixed
[[lie-groups/cartan-involution-real-lie-algebra|Cartan involution]], and let
\(P\subseteq G\) be a
[[lie-groups/parabolic-subgroup-real-reductive-group|parabolic subgroup]]
compatible with the resulting positive restricted roots. The **Langlands
decomposition** is
\[
P=MAN,
\]
where \(A\) is a connected real split abelian subgroup, \(M\) is reductive
with compact center modulo the center inherited from \(G\), and \(N\) is the
connected nilpotent radical. The factors \(M\) and \(A\) commute, \(MA\)
normalizes \(N\), and multiplication \(M\times A\times N\to P\) is a
diffeomorphism under the standard normalization of the factors.

## Construction from restricted roots

Choose the subset of simple restricted roots defining \(P\). The [[lie-groups/lie-algebra|Lie algebra]]
\(\mathfrak a_P\) is the common kernel in \(\mathfrak a\) of those roots,
\(A=\exp(\mathfrak a_P)\), and \(\mathfrak n\) is the sum of the positive
restricted-root spaces not belonging to the Levi subsystem. The remaining
centralizer data determine \(\mathfrak m\). For the fixed Cartan involution
and positive restricted-root data, this construction determines the three
factors with their standard uniqueness properties.

## Role in normalized induction

A representation \(\sigma\) of \(M\) and a character \(e^\nu\) of \(A\)
define a representation of \(P\) by letting \(N\) act trivially. Induction
from \(P\) to \(G\), with the modular correction involving the half-sum
\(\rho_P\) of roots in \(\mathfrak n\), produces normalized parabolic
[[lie-groups/normalized-parabolic-induction|induction]]. The three factors
separate discrete representation data on \(M\), continuous spectral parameters
on \(A\), and the nilpotent directions in \(N\).

## Minimal and extreme cases

For a [[lie-groups/minimal-parabolic-subgroup|minimal parabolic]], this is the
familiar \(P_0=MAN\) associated with an
[[lie-groups/iwasawa-decomposition|Iwasawa decomposition]]. At the other
extreme, \(P=G\) has \(N=\{e\}\); depending on the normalization, its split
central part may appear in \(A\). These cases explain why authors sometimes
state the theorem only for proper parabolics or impose a specified class of
real reductive groups.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/beyond2.html). Relevant: Chapter VII, §7 on parabolic subgroups and their \(MAN\) decomposition.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on principal series and parabolic induction.
