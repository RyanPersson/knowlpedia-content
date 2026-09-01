+++
id = "harmonic-analysis/l1-group-algebra"
title = "L1 group algebra"
kind = "definition"
summary = "The Banach star-algebra of integrable functions on a locally compact group under convolution."
aliases = ["group Banach algebra", "L^1(G)", "convolution algebra L1(G)"]
domains = ["harmonic-analysis", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "measure-theory/lp-space", "harmonic-analysis/convolution-on-locally-compact-group", "harmonic-analysis/convolution-involution", "measure-theory/measure-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with a fixed
[[harmonic-analysis/haar-measure|left Haar measure]]. The
**\(L^1\) group algebra** is the
[[measure-theory/lp-space|\(L^1\) space]] \(L^1(G)\), equipped with
[[harmonic-analysis/convolution-on-locally-compact-group|group convolution]]
\[
(f*g)(x)=\int_G f(y)g(y^{-1}x)\,dy
\]
and the [[harmonic-analysis/convolution-involution|convolution involution]]
\[
f^*(x)=\Delta(x^{-1})\overline{f(x^{-1})},
\]
where \(\Delta\) is the modular function. With the \(L^1\)-norm these
operations make \(L^1(G)\) a Banach \(*\)-algebra, and
\(\|f*g\|_1\leq\|f\|_1\|g\|_1\). Its multiplication therefore records the
group law, not merely the underlying [[measure-theory/measure-space|measure space]].

## Haar-measure conventions

Replacing the left Haar measure by a positive scalar multiple gives an
isometrically isomorphic algebra after the corresponding rescaling of
functions. The modular factor in the involution is essential for a
nonunimodular group. With right Haar measure or a different convolution
convention, the displayed formulas change; convolution and involution must
always be matched.

## Representations and C-star completions

Every [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(U\) of \(G\) has an
integrated form
\[
U(f)=\int_G f(x)U_x\,dx,
\]
which is a nondegenerate contractive \(*\)-representation of \(L^1(G)\).
The supremum of the resulting [[linear-algebra/operator-norm|operator norms]] produces the full group
\(C^*\)-norm, while the left [[algebra-representation-theory/regular-representation|regular representation]] produces the reduced
group \(C^*\)-norm. Thus the two group \(C^*\)-algebras are completions of
the same convolution algebra.

## Units and approximate units

If \(G\) is discrete and Haar measure is counting measure, the point mass at
the identity is an identity for \(L^1(G)\). For a nondiscrete group, that
point mass is not an \(L^1\)-function, and \(L^1(G)\) has no identity.
Nevertheless, it has contractive approximate identities concentrated in
shrinking neighborhoods of the group identity.

## Examples

For a discrete group, \(L^1(G)=\ell^1(G)\) and convolution is a sum. For
\(G=\mathbb R^n\), the algebra is the usual convolution algebra of integrable
functions, the modular function is \(1\), and Fourier transformation converts
convolution into pointwise multiplication. The algebra is commutative exactly
when \(G\) is abelian.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/b19172). Relevant: Chapters 2–3 on Haar convolution and integrated representations.
2. Jacques Dixmier, *C*-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: the chapters on involutive Banach algebras and unitary representations of locally compact groups.
