+++
id = "supergeometry/superalgebra"
title = "Superalgebra"
kind = "definition"
summary = "An associative algebra whose multiplication preserves Z/2-degree."
aliases = ["Z/2-graded algebra", "associative superalgebra"]
domains = ["supergeometry", "algebra-rings"]
prerequisites = ["algebra-category-theory/algebra-object", "supergeometry/super-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic different from \(2\). A
**superalgebra** over \(k\) is an associative unital
[[algebra-category-theory/algebra-object|algebra object]] in
\(\mathbf{SuperVect}_k\). Concretely, it is a
[[supergeometry/super-vector-space|super vector space]]
\[
A=A_{\bar0}\oplus A_{\bar1}
\]
with \(1\in A_{\bar0}\) and
\(A_{\bar i}A_{\bar j}\subseteq A_{\bar i+\bar j}\). Its multiplication and
unit are even maps.

The [[supergeometry/supercommutator|supercommutator]] turns every associative
superalgebra into a [[supergeometry/lie-superalgebra|Lie superalgebra]].

## Examples and non-examples

An ordinary associative algebra placed entirely in even degree is a
superalgebra. The [[differential-geometry/clifford-algebra|Clifford algebra]]
has its natural tensor-parity grading and is therefore a superalgebra.

A superalgebra need not be
[[supergeometry/supercommutative-algebra|supercommutative]]. For instance, the
Clifford relation usually gives a nonzero anticommutator of odd vectors.

## Morphisms

A morphism of superalgebras is an even unital [[algebra-modules/algebra-homomorphism|algebra homomorphism]]. Requiring
evenness is part of the standard category: it preserves the stated grading,
not merely the underlying ungraded multiplication.

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*,
   American Mathematical Society, 2004. [DOI
   record](https://doi.org/10.1090/cour/011). Relevant: Chapter 1.
2. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph
   Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*,
   Volume 1, American Mathematical Society, 1999. Relevant: Section 1.
