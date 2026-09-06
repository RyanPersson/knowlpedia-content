+++
id = "algebraic-geometry-foundations/ordered-blueprint"
title = "Ordered blueprint"
kind = "definition"
summary = "An ordered semiring together with a multiplicative monoid of generators."
aliases = ["ordered blueprint algebra"]
domains = ["algebraic-geometry-foundations", "algebra-hyperstructures"]
prerequisites = ["algebra-rings/ordered-semiring", "algebra-rings/semiring-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **ordered blueprint** is a triple
\[
B=(B^\bullet,B^+,\leq)
\]
in which \((B^+,\leq)\) is an [[algebra-rings/ordered-semiring|ordered semiring]] and \(B^\bullet\subseteq B^+\) is a multiplicatively closed subset containing \(0\) and \(1\) that generates \(B^+\) as a semiring. A morphism is an order-preserving [[algebra-rings/semiring-homomorphism|semiring homomorphism]] \(f^+:B^+\to C^+\) satisfying \(f^+(B^\bullet)\subseteq C^\bullet\).

## Presentation form

Equivalently, begin with a [[algebra-groups/commutative-monoid|commutative monoid]] \(A\) with zero and impose a compatible [[shared-foundations/partial-order|partial order]] on its free semiring \(\mathbb N[A]\), possibly identifying elements first. One writes
\[
A/\!/\langle{\text{generating inequalities}}\rangle.
\]
The monoid \(B^\bullet\) records the designated monomials; the ordered semiring \(B^+\) records their finite sums and additive inequalities.

## Relation to blueprints

An ordinary [[algebraic-geometry-foundations/blueprint|blueprint]] gives an ordered blueprint by reading each additive equality as inequalities in both directions. The converse fails in general because an inequality need not be symmetric. This extra directionality is what allows one framework to contain semiring orders, hyperaddition, and bend relations without identifying them.

## Important subcategories

- Objects [[algebraic-geometry-foundations/ordered-blueprint-with-unique-weak-inverses|with unique weak inverses]] provide the coefficient setting used for much of matroid geometry.
- [[algebraic-geometry-foundations/hyperrings-as-ordered-blueprints|Hyperrings embed fully faithfully]] after hyperaddition is encoded by monomial inequalities.
- Affine spectra glue to [[algebraic-geometry-foundations/ordered-blue-scheme|ordered blue schemes]].

## References

- Oliver Lorscheid, [*A unifying approach to tropicalization*, §§2–3](https://arxiv.org/abs/1508.07949).
- Matthew Baker and Oliver Lorscheid, [*The moduli space of matroids*, §2.6](https://arxiv.org/abs/1809.03542).
