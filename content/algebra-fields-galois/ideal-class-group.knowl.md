+++
id = "algebra-fields-galois/ideal-class-group"
title = "Ideal class group of a number field"
kind = "definition"
summary = "Nonzero fractional ideals modulo multiplication by a nonzero field element."
aliases = ["ideal class", "ideal classes"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "algebra-commutative/fractional-ideal", "algebra-commutative/dedekind-domain", "algebra-groups/quotient-group"]
+++

For a number field \(K\), let \(I_K\) be the abelian group of nonzero [[algebra-commutative/fractional-ideal|fractional ideals]] of its [[algebra-fields-galois/ring-of-integers|ring of integers]], under ideal multiplication. Its **ideal class group** is the [[algebra-groups/quotient-group|quotient]]
\[
\operatorname{Cl}(K)=I_K/\{a\mathcal O_K:a\in K^\times\}.
\]
Thus \([I]=[J]\) precisely when \(I=aJ\) for some \(a\in K^\times\), and \([I][J]=[IJ]\). The group law exists because \(\mathcal O_K\) is a [[algebra-commutative/dedekind-domain|Dedekind domain]].

## Interpretation

The identity class consists of principal fractional ideals. Every class has an integral-ideal representative, obtained by clearing denominators. Triviality means every ideal is principal; it does not say all ideals are equal.

## Example

For \(K=\mathbb Q\), every fractional ideal is \(a\mathbb Z\), so the class group is trivial.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §3, Theorem 3.20 and definition following Remark 3.21.
