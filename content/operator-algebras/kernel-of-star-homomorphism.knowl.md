+++
id = "operator-algebras/kernel-of-star-homomorphism"
title = "Kernel of a *-homomorphism"
kind = "definition"
summary = "The closed two-sided ideal sent to zero by a *-homomorphism."
aliases = ["C*-homomorphism kernel", "kernel ideal"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

For a [[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\phi:A\to B\) of [[operator-algebras/cstar-algebra|\(C^*\)-algebras]], its
**kernel** is
\[
\ker\phi=\{a\in A:\phi(a)=0\}.
\]
It is a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]:
linearity gives a [[linear-algebra/closed-linear-subspace|closed linear subspace]], multiplicativity gives absorption
from both sides, and preservation of the involution gives self-adjointness.
The homomorphism is injective exactly when \(\ker\phi=\{0\}\). Thus the
kernel records precisely which elements of the domain become
indistinguishable from zero. Because \(*\)-homomorphisms are automatically
continuous, closedness of the kernel requires no separate continuity
hypothesis.

## Factorization through the quotient

Let \(q:A\to A/\ker\phi\) be the quotient map. There is a unique
\(*\)-homomorphism
\[
\widetilde\phi:A/\ker\phi\longrightarrow B,\qquad
\widetilde\phi(a+\ker\phi)=\phi(a),
\]
such that \(\phi=\widetilde\phi\circ q\). It is injective and therefore
isometric. Its range is \(\phi(A)\), so
\[
A/\ker\phi\cong\phi(A)
\]
as \(C^*\)-algebras. In particular, the range of every
\(*\)-homomorphism between \(C^*\)-algebras is norm closed
[Murphy, §3.1](https://doi.org/10.1016/C2009-0-22289-6).

## Universal property

More generally, if \(I\) is a closed [[algebra-rings/two-sided-ideal|two-sided ideal]] of \(A\), then a
\(*\)-homomorphism \(\psi:A\to C\) factors uniquely through the
[[operator-algebras/quotient-cstar-algebra|quotient \(C^*\)-algebra]] \(A/I\)
exactly when \(I\subseteq\ker\psi\). This is the universal property of the
quotient and is often the efficient way to construct homomorphisms out of
\(A/I\).

## Examples

Evaluation at \(x\) on \(C_0(X)\) has kernel
\(\{f\in C_0(X):f(x)=0\}\). A faithful representation
\(\pi:A\to B(H)\) has zero kernel, whereas the quotient map \(A\to A/I\) has
kernel exactly \(I\). These examples connect points, representations, and
ideals through the same construction.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [Publisher DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.1 on ideals, quotient algebras, and the \(C^*\)-algebraic isomorphism theorem.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [Publisher DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §§1.2 and 1.8 on morphisms, kernels, and quotients.
