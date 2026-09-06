+++
id = "operator-algebras/star-isomorphism"
title = "*-isomorphism"
kind = "definition"
summary = "A star-isomorphism is a bijective star-homomorphism between C*-algebras."
aliases = ["C*-isomorphism"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/star-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
A **\(*\)-isomorphism** from \(A\) to \(B\) is a bijective
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\phi:A\to B\). Its set-theoretic inverse is automatically complex-linear,
multiplicative, and involution-preserving, so it is again a
\(*\)-homomorphism. The algebras are then called **\(*\)-isomorphic** or
**\(C^*\)-isomorphic**. This is the isomorphism notion in the category of
\(C^*\)-algebras: it preserves the full algebraic and involutive structure,
not merely the underlying [[linear-algebra/normed-vector-space|normed vector spaces]].

## Automatic norm preservation

Every \(*\)-isomorphism is isometric:
\[
\lVert\phi(a)\rVert=\lVert a\rVert\qquad(a\in A).
\]
Consequently it is a homeomorphism for the norm topologies and preserves
completeness, spectra, positivity, and
[[operator-algebras/continuous-functional-calculus|continuous functional
calculus]].
No boundedness or isometry hypothesis needs to be added to the definition.

More generally, a
[[operator-algebras/faithful-star-homomorphism|faithful
\(*\)-homomorphism]] \(A\to B\) is a \(*\)-isomorphism onto its closed range;
surjectivity is the extra condition that identifies the range with all of
\(B\).

## Units, ideals, and induced structure

If \(A\) and \(B\) are unital, a surjective \(*\)-homomorphism automatically
sends \(1_A\) to \(1_B\). Thus a \(*\)-isomorphism between unital
\(C^*\)-algebras is automatically unital even when the ambient convention
does not require all morphisms to preserve units.

A \(*\)-isomorphism sends closed [[algebra-rings/two-sided-ideal|two-sided ideals]] of \(A\) bijectively to
closed two-sided ideals of \(B\), preserves inclusion, and induces
\(*\)-isomorphisms on the corresponding quotients. It also transports states
and representations by composition with \(\phi\) or \(\phi^{-1}\).

## Examples and non-examples

Unitary conjugation,
\[
\operatorname{Ad}_U(T)=UTU^*,
\]
is a \(*\)-isomorphism between operator \(C^*\)-algebras carried into one
another by a unitary \(U\). The transpose map on \(M_n(\mathbb C)\) is a
linear isometry preserving the involution, but it reverses multiplication,
so for \(n>1\) it is not a \(*\)-isomorphism. A bijective algebra
homomorphism that does not preserve involution is likewise not a
\(C^*\)-isomorphism under this definition.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on \(*\)-homomorphisms, inverse maps, and automatic isometry.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 on \(C^*\)-algebra morphisms and isomorphisms.
