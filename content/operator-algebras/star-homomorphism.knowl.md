+++
id = "operator-algebras/star-homomorphism"
title = "*-homomorphism"
kind = "definition"
summary = "A complex-algebra homomorphism that preserves the involution."
aliases = ["C*-homomorphism"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]]. A
**\(*\)-homomorphism** is a complex-linear map \(\phi:A\to B\) satisfying
\[
\phi(ab)=\phi(a)\phi(b),\qquad
\phi(a^*)=\phi(a)^*
\]
for all \(a,b\in A\). If both algebras are unital, \(\phi\) is called
**unital** when \(\phi(1_A)=1_B\); this is an additional condition, not part of
the definition. Thus zero maps and inclusions of ideals are legitimate
\(*\)-homomorphisms. A \(*\)-isomorphism is a bijective
\(*\)-homomorphism, and its inverse automatically preserves all the same
structure.

## Automatic analytic properties

Every \(*\)-homomorphism between \(C^*\)-algebras is positive and contractive,
so no continuity hypothesis is needed. It is isometric exactly when it is
injective. These conclusions are special to the \(C^*\)-setting and follow
from spectral theory and the \(C^*\)-identity
[Murphy, §2.1](https://doi.org/10.1016/C2009-0-22289-6). A merely
multiplicative complex-linear map need not preserve the involution or enjoy
these properties.

## Kernels, ranges, and quotients

The kernel of \(\phi\) is a closed two-sided self-adjoint ideal. The induced
map \(A/\ker\phi\to B\) is an isometric \(*\)-isomorphism onto
\(\phi(A)\); consequently the range of a \(*\)-homomorphism is a closed
\(C^*\)-subalgebra. This is the \(C^*\)-algebraic first isomorphism theorem.
Composition of \(*\)-homomorphisms is again a \(*\)-homomorphism.

## Representations and conventions

A representation of \(A\) on a [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is a
\(*\)-homomorphism \(A\to B(H)\). For nonunital \(A\), nondegeneracy means
that the closed span of \(\phi(A)H\) is \(H\). For unital \(A\), a
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] is automatically unital, but an arbitrary
representation need not be. Authors who define morphisms in the unital
category to preserve identity are imposing a category convention and should
state it explicitly.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on \(*\)-homomorphisms, contractivity, kernels, and ranges.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 on morphisms and quotient structure.
