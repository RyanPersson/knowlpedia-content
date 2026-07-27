+++
id = "operator-algebras/bounded-star-representation"
title = "Bounded star-representation"
kind = "definition"
summary = "A representation of an involutive algebra by bounded operators on a Hilbert space."
aliases = ["bounded *-representation", "*-representation by bounded operators"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(A\) be an [[operator-algebras/involutive-algebra|involutive algebra]]
and \(H\) a [[linear-algebra/hilbert-space|Hilbert space]]. A **bounded
\(*\)-representation** of \(A\) on \(H\) is an algebra homomorphism into the
[[operator-algebras/bounded-operator-cstar-algebra|bounded-operator algebra]]
\(\mathcal B(H)\):
\[
\pi:A\longrightarrow\mathcal B(H)
\]
such that \(\pi(a^*)=\pi(a)^*\) for every \(a\in A\). Here “bounded” says
that every represented element is a bounded, everywhere-defined operator; no
norm or topology on \(A\) is assumed. The representation is nondegenerate
when \(\overline{\pi(A)H}=H\), and faithful when \(\pi\) is injective.
Unitality is an additional condition when \(A\) has an identity.

## Relation to C*-representations

When \(A\) is a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]], this is
the usual [[operator-algebras/cstar-representation|\(C^*\)-representation]].
Its map into \(\mathcal B(H)\) is then automatically contractive, so
elementwise boundedness and continuity require no separate hypotheses. For a
general normed \(*\)-algebra, a representation by bounded operators need not
be continuous as a map from \(A\); continuity must be imposed if the phrase
“bounded representation” is intended in the normed-linear-map sense.

## Essential subspace and unitality

The essential subspace \(H_{\mathrm{ess}}=\overline{\pi(A)H}\) is reducing
for \(\pi\). Restriction to it is nondegenerate, while \(\pi\) vanishes on
\(H_{\mathrm{ess}}^\perp\). If \(A\) is unital, a unital representation is
nondegenerate. Conversely, a nondegenerate representation satisfies
\(\pi(1_A)=I_H\), so the two conditions agree in the unital case. A
degenerate representation may send \(1_A\) to a proper orthogonal projection.

## Distinction from unbounded representations

An unbounded \(*\)-representation assigns operators on a common dense domain
and requires explicit domain invariance and adjoint conditions. Those
requirements are absent here because \(\mathcal B(H)\) is already an
involutive algebra of everywhere-defined operators. Thus the adjective
“bounded” distinguishes the codomain, not a bound uniform over all
\(a\in A\).

## References

1. Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory*, De Gruyter, 1990. [DOI record](https://doi.org/10.1515/9783112715734). Relevant: Part II, §8 on \(*\)-representations and the bounded-operator case.
2. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Chapter 3 on representations of \(C^*\)-algebras and automatic contractivity.
