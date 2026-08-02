+++
id = "algebra-hyperstructures/hyperring"
title = "Hyperring"
kind = "definition"
summary = "A canonical additive hypergroup with a single-valued distributive multiplication."
aliases = ["Krasner hyperring", "commutative hyperring"]
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

A **hyperring** in the Krasner convention is a set \(R\) such that
\((R,\boxplus,0)\) is a
[[algebra-hyperstructures/canonical-hypergroup|canonical hypergroup]],
\((R,\cdot,1)\) is a [[algebra-groups/commutative-monoid|commutative monoid]], \(0r=0\), and multiplication
distributes over hyperaddition as an equality of subsets:
\[
a(b\boxplus c)=ab\boxplus ac.
\]
Here \(aA=\{ax:x\in A\}\). Multiplication is single-valued; only addition is
allowed to be multivalued.

## Rings as hyperrings

Every [[algebra-rings/commutative-ring|commutative ring]] becomes a hyperring by interpreting \(a+b\) as the
singleton \(\{a+b\}\). A hyperring whose every hyper-sum is a singleton is
therefore exactly a commutative ring.

## Equality is part of the convention

Some broader multiring definitions require only
\[
a(b\boxplus c)\subseteq ab\boxplus ac.
\]
That weaker distributivity is not the house convention. Krasner hyperrings
here use equality. This condition concerns the operations inside one
hyperring and should not be confused with the inclusion used to define a
weak homomorphism between hyperrings.

## Incomparability with semirings

Hyperrings generalize rings by making addition multivalued while retaining
additive inverses in the canonical-hypergroup sense. Semirings generalize
rings by dropping additive inverses while keeping addition single-valued.
Consequently neither class contains the other.

## References

1. Alain Connes and Caterina Consani, “The hyperring of adèle classes,” *Journal of Number Theory* 131 (2011), 159–194. [arXiv:1001.4260](https://arxiv.org/abs/1001.4260). Relevant: §2, Krasner hyperrings and quotient hyperrings.
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: §2, hyperrings and morphisms.
