+++
id = "operator-algebras/kadison-schwarz-inequality"
title = "Kadison–Schwarz inequality"
kind = "theorem"
summary = "A unital two-positive map bounds the product of an image by the image of the corresponding product."
aliases = ["Schwarz inequality for positive maps", "Kadison inequality"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/n-positive-map", "operator-algebras/unital-completely-positive-map", "operator-algebras/positive-element", "linear-algebra/cauchy-schwarz-inequality"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) and \(B\) be unital \(C^*\)-algebras and let \(\Phi:A\to B\) be a unital [[operator-algebras/n-positive-map|\(2\)-positive map]]. The **Kadison–Schwarz inequality** states that every \(a\in A\) satisfies
\[
\Phi(a)^*\Phi(a)\leq\Phi(a^*a)
\quad\text{and}\quad
\Phi(a)\Phi(a)^*\leq\Phi(aa^*).
\]
In particular the inequalities hold for every [[operator-algebras/unital-completely-positive-map|unital completely positive map]]. The order is the one determined by [[operator-algebras/positive-element|positive elements]] of \(B\). These estimates are operator-algebraic analogues of the scalar [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]].

## Matrix proof

The matrix
\[
\begin{pmatrix}a^*a&a^*\\a&1_A\end{pmatrix}
=\begin{pmatrix}a^*\\1_A\end{pmatrix}
\begin{pmatrix}a&1_A\end{pmatrix}
\]
is positive in \(M_2(A)\). Applying \(\Phi^{(2)}\) and taking the Schur
complement of its lower-right unit gives
\(\Phi(a^*a)-\Phi(a)^*\Phi(a)\geq0\). Applying the same argument to \(a^*\)
gives the second inequality.

## Equality and multiplicativity

For a unital completely positive \(\Phi\), the elements \(a\) for which
equality holds in both displayed inequalities form its multiplicative
domain. On this \(C^*\)-subalgebra,
\[
\Phi(ab)=\Phi(a)\Phi(b),\qquad
\Phi(ba)=\Phi(b)\Phi(a)
\]
for all \(b\in A\). Equality therefore identifies the portion of the domain
on which a generally nonmultiplicative map behaves like a
\(*\)-homomorphism.

## Conventions and sharpness

Kadison's original inequality requires only unital positivity when \(a\) is
self-adjoint:
\(\Phi(a)^2\leq\Phi(a^2)\). The two inequalities for arbitrary \(a\) follow
from unital \(2\)-positivity; this stronger form is often called the
Kadison–Schwarz or Choi–Schwarz inequality. Omitting
unitality changes the estimate and generally introduces a factor involving
\(\Phi(1_A)\).

## References

1. Richard V. Kadison, “A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras,” *Annals of Mathematics* 56 (1952), 494–503. [DOI record](https://doi.org/10.2307/1969657). Relevant: the Schwarz inequality for unital positive maps on self-adjoint elements.
2. Man-Duen Choi, “A Schwarz Inequality for Positive Linear Maps on \(C^*\)-Algebras,” *Illinois Journal of Mathematics* 18 (1974), 565–574. [DOI record](https://doi.org/10.1215/ijm/1256051007). Relevant: the arbitrary-element form and its relation to higher positivity.
3. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapter 3 on completely positive maps and the Schwarz inequality.
