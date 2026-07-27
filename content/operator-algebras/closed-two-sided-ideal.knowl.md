+++
id = "operator-algebras/closed-two-sided-ideal"
title = "Closed two-sided ideal of a C*-algebra"
kind = "definition"
summary = "A norm-closed linear subspace of a C*-algebra stable under multiplication from both sides."
aliases = ["C*-ideal", "closed ideal", "two-sided C*-ideal"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**closed two-sided ideal** of \(A\) is a norm-closed
[[convex-analysis/linear-subspace|linear subspace]] \(I\subseteq A\)
satisfying
\[
a x\in I\quad\text{and}\quad x a\in I
\qquad(a\in A,\ x\in I).
\]
Every norm-closed two-sided ideal in a \(C^*\)-algebra is automatically
self-adjoint: \(x\in I\) implies \(x^*\in I\). Consequently \(I\), with the
operations and norm inherited from \(A\), is itself a \(C^*\)-algebra. The
terms **\(C^*\)-ideal** and **closed ideal** normally refer to this notion.

## Quotients and kernels

The algebraic quotient \(A/I\), with
\[
\lVert a+I\rVert=\inf_{x\in I}\lVert a+x\rVert
\quad\text{and}\quad
(a+I)^*=a^*+I,
\]
is again a [[operator-algebras/quotient-cstar-algebra|quotient
\(C^*\)-algebra]]. Thus closedness is essential: an arbitrary algebraic ideal
need not yield a complete Hausdorff quotient. Conversely, the kernel of every
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]] between
\(C^*\)-algebras is a closed two-sided ideal. These two operations organize
ideals as the subobjects that support \(C^*\)-quotients.

## Positivity and approximate identities

Each closed ideal \(I\) has a positive contractive
[[operator-algebras/approximate-identity|approximate identity]]. Moreover,
ideals are hereditary for
[[operator-algebras/positive-element|positive elements]]: if
\(0\leq b\leq a\) with \(a\in I\), then \(b\in I\). Equivalently,
\(I_+=I\cap A_+\), and \(I\) is linearly spanned by its positive elements.
These analytic properties go beyond the defining absorption conditions and
distinguish \(C^*\)-ideals from general ring ideals.

## Examples and distinctions

For a [[topology/locally-compact-space|locally compact]]
[[topology/hausdorff-space|Hausdorff space]] \(X\) and an open subset \(U\),
extension by zero identifies \(C_0(U)\) with the ideal of functions in
\(C_0(X)\) vanishing on \(X\setminus U\). In
[[operator-algebras/compact-operator-cstar-algebra|\(K(\mathcal H)\)]], the
only closed two-sided ideals are \(0\) and \(K(\mathcal H)\). A
[[operator-algebras/cstar-subalgebra|\(C^*\)-subalgebra]] need not be an
ideal, because it may fail absorption by elements of the ambient algebra.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.1 on ideals, quotients, and approximate identities.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §§1.4 and 1.8 on ideals and their positive structure.
