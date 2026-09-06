+++
id = "operator-algebras/positive-linear-map"
title = "Positive linear map"
kind = "definition"
summary = "A linear map between C*-algebras that sends positive elements to positive elements."
aliases = ["positive map", "order-preserving linear map"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-cone"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]]. A complex-linear map \(\Phi:A\to B\) is **positive** if
\[
\Phi(A_+)\subseteq B_+,
\]
where \(A_+\) and \(B_+\) are their [[operator-algebras/positive-cone|positive cones]]. Equivalently, \(a\geq0\) implies \(\Phi(a)\geq0\). Positivity forces \(\Phi(a^*)=\Phi(a)^*\). When \(A\) is unital, every positive map is bounded and
\[
\lVert\Phi\rVert=\lVert\Phi(1_A)\rVert.
\]
If also \(\Phi(1_A)=1_B\), the map is unital positive. Positivity does not require multiplicativity.
The definition compares the canonical orders on the self-adjoint parts of the
two algebras and does not impose any condition at matrix levels larger than
one.

## Matrix levels

For each \(n\), entrywise application gives \(\Phi^{(n)}:M_n(A)\to M_n(B)\). The map is \(n\)-positive when \(\Phi^{(n)}\) is positive, and completely positive when this holds for every \(n\). Thus ordinary positivity is only the first matrix level. Every \(*\)-homomorphism is completely positive, whereas a merely positive map need not be \(2\)-positive.

## Standard example and counterexample

The transpose map \(x\mapsto x^{\mathsf T}\) on \(M_n(\mathbb C)\) is unital and positive: it preserves the eigenvalues of positive matrices. For \(n\geq2\), however, it is not \(2\)-positive and hence is not completely positive. In contrast, maps of the form
\[
\Phi(a)=V^*\pi(a)V
\]
for a \(*\)-representation \(\pi\) are completely positive. This distinction is essential in operator-algebraic quantum theory.

## Order and norm behavior

A positive map is order preserving on self-adjoint elements: \(a\leq b\) implies \(\Phi(a)\leq\Phi(b)\). A unital positive map sends every self-adjoint contraction to a self-adjoint contraction. Stronger Schwarz inequalities require stronger hypotheses: the [[operator-algebras/kadison-schwarz-inequality|Kadison inequality]] for a unital positive map applies to self-adjoint elements, while the full inequality \(\Phi(a)^*\Phi(a)\leq\Phi(a^*a)\) follows from unital \(2\)-positivity.

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapters 2 and 3 on positive, \(n\)-positive, and completely positive maps.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV on positive maps and operator inequalities.
