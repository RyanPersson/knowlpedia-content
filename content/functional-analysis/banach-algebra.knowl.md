+++
id = "functional-analysis/banach-algebra"
title = "Banach algebra"
kind = "definition"
summary = "A complete normed algebra whose norm is submultiplicative."
aliases = ["complete normed algebra"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(\mathbb F=\mathbb R\) or \(\mathbb C\). A **Banach algebra over \(\mathbb F\)** is an associative [[algebra-modules/algebra-over-ring|\(\mathbb F\)-algebra]] \(A\) equipped with a [[linear-algebra/norm|norm]] such that \(A\) is a [[linear-algebra/banach-space|Banach space]] and
\[
\lVert ab\rVert\leq \lVert a\rVert\,\lVert b\rVert
\]
for all \(a,b\in A\). The inequality makes multiplication jointly continuous. This definition does not require an identity. A **unital Banach algebra** additionally has a multiplicative identity; here its norm is normalized by \(\lVert 1\rVert=1\).

## Unitization and spectral notions

Every nonunital complex Banach algebra has a unitization \(A^+=A\oplus\mathbb C1\) containing \(A\) as a closed ideal. For \(a\) in a unital complex Banach algebra, the spectrum is the set of \(\lambda\in\mathbb C\) for which \(\lambda1-a\) is not invertible. Completeness is essential to the standard theorem that this spectrum is nonempty and compact [Bonsall–Duncan, “Concepts and Elementary Results”].

## Standard examples

The bounded linear operators on a Banach space form a unital Banach algebra under composition and the [[linear-algebra/operator-norm|operator norm]]. If \(K\) is compact Hausdorff, the continuous complex-valued functions on \(K\), with pointwise multiplication and the [[real-analysis/supremum-norm|supremum norm]], form a commutative unital Banach algebra. Given a [[harmonic-analysis/haar-measure|Haar measure]] on a [[topology/locally-compact-group|locally compact group]], the integrable functions form a generally noncommutative Banach algebra under convolution.

## Conventions and scope

Some authors build unitality into “Banach algebra”; others, as here, do not. Without the normalization \(\lVert1\rVert=1\), submultiplicativity only forces \(\lVert1\rVert\geq1\). A normed algebra need not be a Banach algebra unless it is complete. A \(C^*\)-algebra is a complex Banach algebra with an involution satisfying the additional \(C^*\)-identity, not merely a Banach algebra carrying some involution.

## References

1. F. F. Bonsall and J. Duncan, *Complete Normed Algebras*, Springer, 1973. [Springer DOI record](https://doi.org/10.1007/978-3-642-65669-9). Relevant: “Concepts and Elementary Results.”
