+++
id = "lie-groups/multiplicity-of-an-irreducible-representation"
title = "Multiplicity of an irreducible representation"
kind = "definition"
summary = "The number of copies of an irreducible representation in a semisimple decomposition."
aliases = ["irreducible multiplicity", "representation multiplicity", "isotypic multiplicity"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional [[algebra-representation-theory/completely-reducible-representation|completely reducible representation]] over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]], and let \(S\) be an [[lie-groups/irreducible-representation-lie-group|irreducible representation]] of the same group. If
\[
V\cong\bigoplus_{[T]}m_TT,
\]
then the **multiplicity of \(S\) in \(V\)** is the nonnegative integer \(m_S\). Equivalently,
\[
m_S=\dim\operatorname{Hom}_G(S,V).
\]
The same definition applies to completely reducible Lie-algebra representations, with \(\operatorname{Hom}_{\mathfrak g}\) in place of \(\operatorname{Hom}_G\).

## Isotypic component

The sum of all subrepresentations of \(V\) isomorphic to \(S\) is its **\(S\)-isotypic component**. It is canonically the image of the evaluation map
\[
S\otimes\operatorname{Hom}_G(S,V)\longrightarrow V,
\qquad s\otimes f\longmapsto f(s),
\]
and is isomorphic to \(S^{\oplus m_S}\). The choice of individual copies of \(S\) inside that component is generally not canonical.

## Computing multiplicity

For compact groups, [[algebra-representation-theory/irreducible-character|irreducible characters]] are orthonormal, so
\[
m_S=\langle\chi_V,\chi_S\rangle
=\int_G\chi_V(g)\overline{\chi_S(g)}\,dg.
\]
For finite groups the normalized integral becomes \(|G|^{-1}\sum_{g\in G}\). In [[lie-groups/highest-weight-representation|highest-weight representations]], character formulas and weight data provide another route to the same irreducible multiplicities.

The multiplicity of the trivial representation is \(\dim V^G\), the dimension of the [[lie-groups/fixed-vector-subspace|fixed-vector subspace]]. Multiplicities appearing after restriction are the coefficients in a [[lie-groups/branching-rule-for-lie-representations|branching rule]].

## Cautions

An irreducible multiplicity is not the same as a **weight multiplicity** \(\dim V_\lambda\): the former counts irreducible summands, while the latter counts vectors having a specified weight inside a representation.

Without complete reducibility, \(V\) need not be a direct sum of irreducibles. One may still count composition factors using a finite-length filtration, but those numbers describe Jordan–Hölder multiplicities and need not equal \(\dim\operatorname{Hom}(S,V)\). Over a non-algebraically-closed field, \(\operatorname{End}_G(S)\) may be larger than the scalar field, so the displayed dimension formula also requires adjustment.

## References

1. Jean-Pierre Serre, *Linear Representations of Finite Groups*, Springer, 1977, Chapters 2 and 6. [Publisher record](https://doi.org/10.1007/978-1-4684-9458-7).
2. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 4 and 12. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
