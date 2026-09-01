+++
id = "lie-groups/spin6-su4-isomorphism"
title = "The isomorphism Spin(6) ≅ SU(4)"
kind = "theorem"
summary = "The low-rank isomorphism between the simply connected compact groups of types D3 and A3."
aliases = ["Spin(6) isomorphic to SU(4)", "D3 A3 isomorphism", "spin6 su4 accidental isomorphism"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["lie-groups/compact-lie-group", "lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

There is an isomorphism of [[lie-groups/compact-lie-group|compact Lie groups]]
\[
\operatorname{Spin}(6)\cong SU(4).
\]
Infinitesimally it gives an isomorphism of real [[lie-groups/lie-algebra|Lie algebras]]
\[
\mathfrak{spin}(6)\cong\mathfrak{so}(6)
\cong\mathfrak{su}(4),
\]
and after complexification it is the exceptional root-system identification \(D_3=A_3\):
\[
\mathfrak{so}_6(\mathbb C)\cong\mathfrak{sl}_4(\mathbb C).
\]

## Corresponding representations

Under a choice of this isomorphism, the two complex [[lie-groups/half-spin-representation|half-spin representations]] of \(\operatorname{Spin}(6)\) correspond to the defining representation of \(SU(4)\) on \(\mathbb C^4\) and its dual:
\[
\Delta^+\leftrightarrow\mathbb C^4,
\qquad
\Delta^-\leftrightarrow(\mathbb C^4)^*.
\]
Interchanging chirality interchanges the two right-hand representations.

The complexification of the six-dimensional [[lie-groups/defining-representation-of-a-classical-lie-algebra|vector representation]] corresponds to the second [[lie-groups/exterior-power-representation|exterior power]]:
\[
\mathbb C^6\cong\Lambda^2\mathbb C^4.
\]
Because \(SU(4)\) preserves a Hermitian form and a complex volume form on \(\mathbb C^4\), \(\Lambda^2\mathbb C^4\) carries an invariant real structure. Its fixed real subspace has dimension six and gives the homomorphism
\[
SU(4)\longrightarrow SO(6).
\]
Its kernel is \(\{\pm I\}\), so it is the spin double covering.

## Why the group isomorphism follows

The compact groups \(\operatorname{Spin}(6)\) and \(SU(4)\) are both connected and simply connected, and their Lie algebras are isomorphic. A Lie-algebra isomorphism between connected [[lie-groups/simply-connected-lie-group|simply connected Lie groups]] integrates uniquely to a Lie-group isomorphism.

This is stronger than \(SO(6)\cong SU(4)\): that latter statement is false. Instead,
\[
SO(6)\cong SU(4)/\{\pm I\}.
\]
The remaining central elements \(\pm iI\) act nontrivially in the vector-covering construction before quotienting by the appropriate kernel.

## Convention warning

No preferred isomorphism singles out which of \(\Delta^+\) or \(\Delta^-\) is \(\mathbb C^4\). Orientation reversal on the orthogonal side and complex conjugation on the unitary side exchange the two choices.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989, Chapter I, §5. [Publisher record](https://doi.org/10.1515/9781400883912).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§19–20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
