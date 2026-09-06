+++
id = "operator-algebras/unital-star-homomorphism"
title = "Unital *-homomorphism"
kind = "definition"
summary = "A star-homomorphism between unital C-star algebras that preserves the multiplicative identity."
aliases = ["unit-preserving *-homomorphism", "unital C*-homomorphism"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/unital-cstar-algebra", "operator-algebras/star-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) and \(B\) be
[[operator-algebras/unital-cstar-algebra|unital \(C^*\)-algebras]]. A **unital
\(*\)-homomorphism** is a
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\phi:A\to B\) satisfying
\[
\phi(1_A)=1_B.
\]
Thus \(\phi\) is complex-linear, multiplicative, involution-preserving, and
unit-preserving. The last condition is additional: a \(*\)-homomorphism
between unital algebras can instead send \(1_A\) to a proper projection in
\(B\), or be the zero map. Unital \(*\)-homomorphisms are the morphisms in the
category of unital \(C^*\)-algebras when that category is taken to preserve
identities.

## Automatic properties

Every unital \(*\)-homomorphism is positive, completely positive, and
contractive, with norm and completely bounded norm equal to one when the
codomain is nonzero. It preserves spectra in the one-sided sense
\(\sigma_B(\phi(a))\subseteq\sigma_A(a)\); equality holds when \(\phi\) is
injective. It also commutes with continuous and holomorphic functional
calculus. These are consequences of the \(C^*\)-identity, not extra axioms.

## Examples and near-misses

The inclusion of a unital \(C^*\)-subalgebra that shares the same identity is a
unital \(*\)-homomorphism. Evaluation \(C(X)\to\mathbb C\) at a point is
another. If \(p\) is a proper projection in a unital algebra \(B\), the corner
map from \(\mathbb C\) to \(B\), \(\lambda\mapsto\lambda p\), is a
\(*\)-homomorphism but is not unital as a map into \(B\); it is unital only
when regarded as a map into the corner \(pBp\).

## Conventions and universal properties

**Warning.** Some authors build unit preservation into the unqualified word
“\(*\)-homomorphism” whenever both algebras are unital. Others, including the
convention used here, state it separately. Universal properties must therefore
specify whether their test morphisms are unital. A surjective
\(*\)-homomorphism between unital \(C^*\)-algebras is automatically unital, as
is every [[operator-algebras/star-isomorphism|\(*\)-isomorphism]] between them.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on \(*\)-homomorphisms, units, positivity, and contractivity.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 on morphism conventions and quotient maps.
