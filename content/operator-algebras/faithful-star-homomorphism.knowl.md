+++
id = "operator-algebras/faithful-star-homomorphism"
title = "Faithful *-homomorphism"
kind = "definition"
summary = "A faithful star-homomorphism is an injective star-homomorphism between C*-algebras."
aliases = ["injective *-homomorphism", "faithful C*-homomorphism"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
A [[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\phi:A\to B\) is **faithful** if it is injective:
\[
\ker\phi=\{0\}.
\]
Equivalently, \(\phi(a)=0\) implies \(a=0\). Faithfulness says that no
nonzero algebra element, and hence no nonzero closed [[algebra-rings/two-sided-ideal|two-sided ideal]], is lost
under \(\phi\). It does not require \(\phi\) to be surjective, unital, or
nondegenerate. When \(B=\mathcal B(H)\), this is the usual faithfulness
condition for a [[operator-algebras/cstar-representation|representation]] of
\(A\) on \(H\).

## Isometry and concrete realization

A \(*\)-homomorphism of \(C^*\)-algebras is faithful exactly when it is
isometric:
\[
\lVert\phi(a)\rVert=\lVert a\rVert\qquad(a\in A).
\]
Thus its range is closed, and \(\phi\) is a
[[operator-algebras/star-isomorphism|\(*\)-isomorphism]] from \(A\) onto the
[[operator-algebras/cstar-subalgebra|\(C^*\)-subalgebra]] \(\phi(A)\).
This automatic isometry is a specifically \(C^*\)-algebraic consequence of
the \(C^*\)-identity and spectral theory
[Murphy, §2.1](https://doi.org/10.1016/C2009-0-22289-6).

The [[operator-algebras/gelfand-naimark-theorem|Gelfand–Naimark theorem]]
therefore says that every abstract \(C^*\)-algebra admits a faithful
\(*\)-homomorphism into some bounded-operator algebra \(\mathcal B(H)\).

## Kernels and quotients

For an arbitrary \(*\)-homomorphism \(\phi:A\to B\), the
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
\(\ker\phi\) measures precisely the failure of faithfulness. The induced map
\[
A/\ker\phi\longrightarrow\phi(A),\qquad
a+\ker\phi\longmapsto\phi(a),
\]
is always a faithful \(*\)-homomorphism and hence an isometric
\(*\)-isomorphism. In particular, faithfulness is a property of the map, not
of either algebra in isolation.

## Examples and distinctions

The inclusion of a \(C^*\)-subalgebra \(A\subseteq B\) is faithful. A quotient
map \(A\to A/I\) is faithful exactly when \(I=\{0\}\). The zero map from a
nonzero algebra is never faithful.

**Warning.** A faithful map need not be nondegenerate. If \(A\) acts
faithfully on \(H\), then the representation \(a\mapsto\pi(a)\oplus0\) on
\(H\oplus K\), with \(K\neq0\), remains faithful but is degenerate. Likewise,
a faithful \(*\)-homomorphism between unital algebras need not preserve the
identity unless unitality or surjectivity is imposed.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§2.1 and 3.4 on injective \(*\)-homomorphisms, isometry, and faithful representations.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 on morphisms, kernels, and represented images.
