+++
id = "operator-algebras/character-space"
title = "Character space of a commutative C*-algebra"
kind = "definition"
summary = "The locally compact space of nonzero characters of a commutative C-star algebra."
aliases = ["Gelfand spectrum", "maximal ideal space"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/commutative-cstar-algebra|commutative
\(C^*\)-algebra]].
Its **character space**, denoted
\(\Delta(A)\) or \(\widehat A\), is the set of all
[[operator-algebras/character-cstar-algebra|characters]]
\(\chi:A\to\mathbb C\), equipped with the
[[functional-analysis/weak-star-topology|weak-star topology]] inherited from
\(A^*\). Equivalently, it is the weakest topology making every evaluation map
\(\chi\mapsto\chi(a)\) continuous for \(a\in A\). The space \(\Delta(A)\) is
[[topology/locally-compact-space|locally compact]] and
[[topology/hausdorff-space|Hausdorff]]. For nonzero \(A\), it is compact exactly when
\(A\) is unital. No topology is chosen independently of the algebra.
This construction is intrinsic.

## Topological structure

All characters have norm one. For a nonunital algebra, adjoining the zero
functional compactifies \(\Delta(A)\) inside the weak-star compact dual unit
ball; this compactification agrees with the character space of the
[[operator-algebras/unitization|unitization]], with the new character as the
point at infinity. These facts
explain why local compactness, rather than compactness, is the natural general
setting.

## Function-algebra model

If \(A=C_0(X)\) for a locally compact Hausdorff space \(X\), the map
\[
x\longmapsto\chi_x,\qquad \chi_x(f)=f(x),
\]
is a homeomorphism \(X\cong\Delta(A)\). Under this identification, the
topology reconstructed from evaluation of algebra elements is exactly the
original topology of \(X\).

## Related spectra

The character space is not the
[[functional-analysis/banach-algebra-spectrum|spectrum]] \(\sigma_A(a)\) of a
single element.
For commutative \(A\), the map
\(\chi\mapsto\ker\chi\) identifies \(\Delta(A)\) with the
[[operator-algebras/primitive-ideal-space|primitive ideal space]]. For a
noncommutative \(C^*\)-algebra, characters may be absent and do not recover
the algebra, so \(\Delta(A)\) is not a substitute for its primitive ideal
space.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: the chapter on characters, the Gelfand topology, and commutative \(C^*\)-algebras.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the introductory treatment of commutative \(C^*\)-algebras and their spectra.
