+++
id = "operator-algebras/quotient-cstar-algebra"
title = "Quotient C*-algebra"
kind = "definition"
summary = "The C*-algebra obtained by dividing a C*-algebra by a closed two-sided ideal."
aliases = ["C*-algebra quotient", "A/I"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/closed-two-sided-ideal"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(I\) be a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
of \(A\). The **quotient \(C^*\)-algebra** \(A/I\) is the algebraic quotient
with
\[
(a+I)^*=a^*+I
\qquad\text{and}\qquad
\lVert a+I\rVert=\inf_{x\in I}\lVert a+x\rVert.
\]
These operations are well defined, the quotient is complete, and the
\(C^*\)-identity holds. The canonical map \(q:A\to A/I\), \(q(a)=a+I\), is a
surjective \(*\)-homomorphism with kernel \(I\). Closedness of \(I\) is
essential: a quotient by a nonclosed ideal does not carry this Hausdorff
\(C^*\)-norm.

## Universal property and exactness

If \(\varphi:A\to B\) is a
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]] satisfying
\(I\subseteq\ker\varphi\), there is a unique \(*\)-homomorphism
\(\overline{\varphi}:A/I\to B\) such that
\(\varphi=\overline{\varphi}\circ q\). Thus quotient maps are precisely the
surjective morphisms in the usual category of \(C^*\)-algebras, up to
isomorphism of the codomain. The sequence
\[
0\longrightarrow I\longrightarrow A\overset{q}{\longrightarrow}A/I
\longrightarrow 0
\]
is the basic [[algebra-modules/short-exact-sequence|short exact sequence]] associated with \(I\).

## Units and representative examples

When \(A\) is unital and \(I\) is proper, \(A/I\) is unital with identity
\(1_A+I\). A quotient of a nonunital algebra can nevertheless be unital. For
\(A=C(X)\) and a closed subset \(F\subseteq X\), the ideal of functions
vanishing on \(F\) has quotient canonically isomorphic to \(C(F)\). For bounded
operators on a [[linear-algebra/hilbert-space|Hilbert space]], the quotient by the [[linear-algebra/compact-operator|compact operators]] is the
Calkin algebra.

## Conventions and boundary cases

Some authors allow the zero \(C^*\)-algebra to be unital and others require
\(0\ne1\). This affects only the description of \(A/A\), not its quotient
operations. The closedness hypothesis belongs to the definition in the
\(C^*\)-setting even when “ideal” elsewhere means an algebraic [[algebra-rings/two-sided-ideal|two-sided ideal]].
The quotient norm is determined by the ideal; it is not an independently
chosen completion norm.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.1 on ideals, quotient norms, and quotient \(C^*\)-algebras.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 1 on ideals and quotients.
