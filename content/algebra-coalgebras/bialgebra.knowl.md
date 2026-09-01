+++
id = "algebra-coalgebras/bialgebra"
title = "Bialgebra"
kind = "definition"
summary = "An algebra and coalgebra whose multiplication and comultiplication are compatible."
aliases = ["bialgebra over a ring"]
domains = ["algebra-coalgebras", "algebra-rings"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-modules/algebra-over-ring", "algebra-coalgebras/coalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-rings/commutative-ring|commutative ring]]. A
**\(k\)-bialgebra** is a unital associative \(k\)-[[algebra-modules/algebra-over-ring|algebra]]
\((H,m,u)\) and a [[algebra-coalgebras/coalgebra|\(k\)-coalgebra]]
\((H,\Delta,\varepsilon)\) on the same module such that
\(\Delta:H\to H\otimes_k H\) and \(\varepsilon:H\to k\) are unital algebra
homomorphisms. The tensor-product algebra structure used here is
\[
(a\otimes b)(c\otimes d)=ac\otimes bd.
\]
Equivalently, \(m\) and \(u\) are coalgebra homomorphisms.

## Compatibility in formulas

The algebra-homomorphism formulation means
\[
\Delta(ab)=\Delta(a)\Delta(b),\qquad
\Delta(1_H)=1_H\otimes1_H,
\]
and
\[
\varepsilon(ab)=\varepsilon(a)\varepsilon(b),\qquad
\varepsilon(1_H)=1_k.
\]
Together with coassociativity and the counit identities, these conditions say
that \(H\) is simultaneously a monoid and a comonoid, with each structure
compatible with the other, in the [[algebra-category-theory/symmetric-monoidal-category|symmetric monoidal category]] of \(k\)-modules.

## Morphisms

A **bialgebra homomorphism** is a unital [[algebra-modules/algebra-homomorphism|algebra homomorphism]] that is also a
coalgebra homomorphism. Bialgebras may be commutative as algebras,
cocommutative as coalgebras, both, or neither; these are independent
conditions.

## Examples

- For a [[algebra-groups/group|group]] \(G\), the [[algebra-representation-theory/group-algebra|group algebra]] \(k[G]\) has
  \(\Delta(g)=g\otimes g\) and \(\varepsilon(g)=1\), extended linearly and
  multiplicatively. It is cocommutative, but it is commutative exactly when
  \(G\) is abelian.
- The polynomial algebra \(k[x]\) becomes a commutative and cocommutative
  bialgebra with \(\Delta(x)=x\otimes1+1\otimes x\) and
  \(\varepsilon(x)=0\).

## Why an antipode is extra

A bialgebra encodes multiplication and comultiplication but need not have an
operation representing inversion. A bialgebra equipped with such a
convolution inverse is a [[algebra-coalgebras/hopf-algebra|Hopf algebra]].

## References

1. Christian Kassel, *Quantum Groups*, Graduate Texts in Mathematics 155, Springer, 1995. [Publisher record](https://doi.org/10.1007/978-1-4612-0783-2). Relevant: Chapter III, §§1–2.
2. Susan Montgomery, *Hopf Algebras and Their Actions on Rings*, CBMS Regional Conference Series 82, American Mathematical Society, 1993. [Publisher record](https://doi.org/10.1090/cbms/082). Relevant: Chapter 1.
