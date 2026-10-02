+++
id = "knowlification/orders-and-fractional-ideals-index"
title = "Orders, fractional ideals, and quaternion arithmetic"
kind = "index"
summary = "Created definitions and reused prerequisites from the algebra-class transcript, separate from the object catalogue."
aliases = ["orders and fractional ideals index"]
domains = ["algebra-commutative", "algebra-rings", "algebra-modules"]
section_mode = "continuous"
prerequisites = []
+++

This collection supplies the definitions needed to pass from polynomial modules to fractional ideals, orders, and quaternion arithmetic. The entries below were created for this addition; existing definitions are listed afterward so that familiar terms keep their canonical homes.

## A route through the definitions

Start with an integral domain and its fraction field. A full lattice adds finite integral coordinates; an order adds multiplication. Fractional ideals of number-field orders are full lattices in the field, and their invertibility controls the Picard group. Quaternion ideals require a choice of side, and their class set generally has no group law.

## Modules and integral structures

- [[algebra-modules/polynomial-module-from-operator|Polynomial module associated with a linear operator]].
- [[algebra-modules/full-lattice|Full lattice over an integral domain]].
- [[algebra-modules/lie-order|Lie order]].
- [[algebra-rings/order-in-algebra|Order in an algebra]].
- [[algebra-rings/maximal-order|Maximal order]].

## Fractional ideals and order arithmetic

- [[algebra-commutative/principal-fractional-ideal|Principal fractional ideal]].
- [[algebra-commutative/product-fractional-ideals|Product of fractional ideals]].
- [[algebra-commutative/fractional-ideal-quotient|Quotient of fractional ideals]].
- [[algebra-commutative/invertible-fractional-ideal|Invertible fractional ideal]].
- [[algebra-commutative/multiplier-ring|Multiplier ring of a fractional ideal]].
- [[algebra-commutative/proper-ideal-of-order|Proper fractional ideal of an order]].
- [[algebra-commutative/conductor-of-order|Conductor of an order]].
- [[algebra-modules/invertible-module|Invertible module over a commutative ring]].
- [[algebra-commutative/picard-group|Picard group of a ring]].

## Quaternion algebras and local invariants

- [[algebra-rings/central-simple-algebra|Central simple algebra]].
- [[algebra-rings/maximal-subfield|Maximal subfield of an algebra]].
- [[algebra-rings/brauer-group|Brauer group of a field]].
- [[algebra-rings/quaternion-reduced-trace|Reduced trace in a quaternion algebra]].
- [[algebra-rings/pure-quaternion|Pure quaternion]].
- [[algebra-rings/quaternion-ramification|Ramification of a quaternion algebra at a place]].
- [[algebra-rings/definite-quaternion-algebra|Definite quaternion algebra]].
- [[algebra-rings/hilbert-symbol|Local Hilbert symbol]].
- [[algebra-rings/quaternion-local-invariant|Local Brauer invariant of a quaternion algebra]].
- [[algebra-rings/quaternion-discriminant|Discriminant of a quaternion algebra]].
- [[algebra-rings/quaternion-order-discriminant|Reduced discriminant of a quaternion Z-order]].
- [[algebra-rings/quaternion-fractional-ideal|Fractional ideal of a quaternion order]].
- [[algebra-rings/locally-principal-quaternion-ideal|Locally principal ideal of a quaternion order]].
- [[algebra-rings/quaternion-ideal-class-set|Ideal class set of a quaternion order]].
- [[algebra-rings/quaternion-type-number|Type number of a quaternion algebra]].

## Quadratic forms, groups, and arithmetic connections

- [[linear-algebra/integral-binary-quadratic-form|Integral binary quadratic form]].
- [[linear-algebra/proper-equivalence-binary-quadratic-forms|Proper equivalence of binary quadratic forms]].
- [[lie-groups/d4-root-lattice|D₄ root lattice]].
- [[linear-algebra/theta-series-of-lattice|Theta series of a positive definite lattice]].
- [[algebra-groups/binary-tetrahedral-group|Binary tetrahedral group]].
- [[algebraic-geometry-foundations/elliptic-curve|Elliptic curve]].
- [[algebraic-geometry-foundations/supersingular-elliptic-curve|Supersingular elliptic curve]].
- [[discrete-structures/cayley-graph|Cayley graph]].
- [[discrete-structures/ramanujan-graph|Ramanujan graph]].
- [[complex-analysis/modular-form|Holomorphic modular form]].
- [[complex-analysis/cusp-form|Cusp form]].
- [[algebra-representation-theory/brandt-matrix|Brandt matrix]].
- [[lie-groups/fuchsian-group|Fuchsian group]].
- [[lie-groups/arithmetic-fuchsian-group|Arithmetic Fuchsian group]].

## Existing definitions reused

| Existing knowl | Why it is reused |
| --- | --- |
| [[algebra-rings/integral-domain|Integral domain]] | “Domain” in this algebra discussion means a nonzero commutative ring without zero divisors. |
| [[algebra-rings/fraction-field|Fraction field]] | The exact construction was already present; no second field-of-fractions definition is needed. |
| [[algebra-rings/total-ring-of-fractions|Total ring of fractions]] | The related construction for rings that may have zero divisors already has its own home. |
| [[algebra-commutative/dedekind-domain|Dedekind domain]] | The existing owner now makes its exclusion of fields and its local-characterization hypotheses explicit. |
| [[algebra-commutative/integrally-closed-domain|Integrally closed domain]] | Distinguishes maximal number-field orders from their nonmaximal suborders. |
| [[algebra-commutative/fractional-ideal|Fractional ideal]] | Expanded with denominator examples and links to the new atomic operations. |
| [[algebra-rings/ideal|Ideal]] | An integral ideal is an ordinary ideal contained in the ring. |
| [[algebra-modules/module|Module]] | Supplies the action axioms used by the polynomial construction. |
| [[algebra-modules/rcf-from-structure-theorem|Rational canonical form from the structure theorem]] | Reuses the existing theorem and links the new polynomial-module construction. |
| [[algebra-fields-galois/ring-of-integers|Ring of integers]] | The canonical maximal order of a number field. |
| [[algebra-fields-galois/ideal-class-group|Ideal class group of a number field]] | The number-field specialization of the new Picard-group definition. |
| [[algebra-rings/quaternion-algebra|Quaternion algebra]], [[algebra-rings/quaternion-conjugation|standard conjugation]], and [[algebra-rings/quaternion-reduced-norm|reduced norm]] | These already own the ambient algebra and its basic operations. |
| [[algebra-rings/quaternion-order|Quaternion order]] | Retained as the quaternion specialization of the general order definition. |
| [[algebra-rings/quaternion-real-place-ramification|Real-place ramification]] | Retained as the real specialization of ramification at any place. |
| [[lie-groups/chevalley-basis|Chevalley basis]] and [[algebraic-geometry-foundations/chevalley-lattice-integral-model|Chevalley lattice and integral model]] | Existing specialized integral Lie constructions. |
| [[algebra-representation-theory/group-algebra|Group algebra and group ring]] | Expanded to cover arbitrary groups and commutative coefficient rings, including integer group rings. |

## Specific examples shared with the catalogue

The [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton algebra]], [[catalog/arithmetic/lipschitz-order|Lipschitz order]], and [[catalog/arithmetic/hurwitz-order|Hurwitz order]] have individual catalogue entries. The general definitions above link to those objects without creating competing copies. The broader [[catalog|object catalogue]] compares algebraic objects and their available categorical structures.

## Conventions worth keeping separate

- A fractional ideal here is nonzero; an arbitrary submodule of a fraction field need not have a common denominator.
- A full lattice need not be free over a general Dedekind domain.
- An associative order is closed under multiplication; a Lie order is closed under the bracket.
- A proper ideal of an order means equality of the multiplier ring, which differs from strict containment in the ring.
- A quaternion algebra's discriminant, an order's reduced discriminant, ideal class number, and type number are different invariants.
- Definite versus indefinite refers to archimedean splitting. Arithmetic groups and [[langlands/automorphic-form|automorphic forms]] require additional choices of field, level, weight, and places.

## Scope

This addition supplies definitions and the examples needed to use them. The transcript's passing references to named arithmetic theorems, mass formulas, and conjectures are not replacements for separate theorem knowls. Sources and checked hypotheses appear in each substantive entry.
