+++
id = "operator-algebras/conditional-expectation"
title = "Conditional expectation of C*-algebras"
kind = "definition"
summary = "A conditional expectation is a completely positive contractive bimodule retraction onto a C*-subalgebra."
aliases = ["C*-conditional expectation", "conditional expectation onto a subalgebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(B\subseteq A\) be a nonzero
[[operator-algebras/cstar-subalgebra|\(C^*\)-subalgebra]]. A **conditional
expectation** from \(A\) onto \(B\) is a
[[operator-algebras/completely-positive-map|completely positive]] contractive
[[linear-algebra/linear-map|linear map]] \(E:A\to B\) such that
\[
E(b)=b,\qquad
E(b_1ab_2)=b_1E(a)b_2
\]
for \(a\in A\) and \(b_1,b_2\in B\). The first condition makes \(E\) a
retraction and hence an idempotent projection: \(E^2=E\). The second says that
\(E\) is a \(B\)-bimodule map. If \(A\) and \(B\) have the same identity,
then \(E\) is automatically unital.

## Norm-one projection characterization

Tomiyama's theorem states that a bounded linear projection \(P:A\to B\) onto
a \(C^*\)-subalgebra, with \(\lVert P\rVert=1\), is positive,
\(B\)-bimodular, and completely positive. Conversely, every conditional
expectation in the core definition is such a norm-one projection. Thus many
sources define a conditional expectation simply as a contractive projection
onto \(B\); the substantial bimodule and positivity properties then follow
[Takesaki, vol. I, §IV.2](https://doi.org/10.1007/978-1-4612-6188-9).

## Basic properties

A conditional expectation fixes \(B\) pointwise and has range exactly \(B\).
It is positive, so \(a\geq0\) implies \(E(a)\geq0\), and it is
\(*\)-preserving. When the algebras share an identity, Kadison's inequality
gives
\[
E(a)^*E(a)\leq E(a^*a).
\]
The expectation is **faithful** when \(E(a^*a)=0\) implies \(a=0\).
Faithfulness is an additional condition and is not implied by contractivity
or complete positivity.

Conditional expectations let
[[operator-algebras/positive-linear-functional|positive functionals]] on
\(B\) produce positive functionals on \(A\) by composition. They also provide
canonical \(B\)-valued [[linear-algebra/inner-product|inner products]] in operator-algebra and
[[operator-algebras/hilbert-cstar-module|Hilbert-module]] constructions.

## Examples and non-examples

For the diagonal subalgebra \(D_n\subseteq M_n(\mathbb C)\),
\[
E([a_{ij}])=\operatorname{diag}(a_{11},\ldots,a_{nn})
\]
is a faithful conditional expectation. If a compact group acts continuously
on a \(C^*\)-algebra \(A\), averaging the action against normalized
[[harmonic-analysis/haar-measure|Haar measure]] gives a conditional
expectation onto the fixed-point algebra.

A [[operator-algebras/positive-linear-map|positive map]] \(A\to B\) whose
image lies in \(B\) is not necessarily an expectation: it must fix \(B\) and
satisfy the projection and bimodule requirements. Similarly, an arbitrary
algebraic projection onto \(B\) can have norm greater than one and need not be
positive.

## Von Neumann algebra convention

For an inclusion \(N\subseteq M\) of
[[operator-algebras/von-neumann-algebra|von Neumann algebras]], the same
definition applies, but authors often require the expectation to be
**normal**, meaning ultraweakly continuous. Normality is extra structure; a
\(C^*\)-algebraic conditional expectation between von Neumann algebras need
not be normal. This distinction is important when expectations are used with
preduals, weights, or increasing operator limits.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, especially §IV.2, on norm-one projections and conditional expectations.
2. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [AMS/DOI record](https://doi.org/10.1090/gsm/088). Relevant: §1.5 on conditional expectations and completely positive maps.
