+++
id = "algebra-fields-galois/codifferent"
title = "Codifferent of a number field"
kind = "definition"
summary = "The lattice dual to the ring of integers under the field-trace pairing."
aliases = ["inverse different", "trace-dual ring-of-integers lattice"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "algebra-fields-galois/trace-field", "algebra-fields-galois/integral-basis"]
+++

The **codifferent** of a [[algebra-fields-galois/number-field|number field]] \(K\) is
\[
\mathcal O_K^\vee=\{a\in K:\operatorname{Tr}_{K/\mathbb Q}(ab)\in\mathbb Z\text{ for all }b\in\mathcal O_K\}.
\]
It is the trace-dual lattice of \(\mathcal O_K\), also denoted \(\mathfrak D_K^{-1}\).

## Trace-dual basis

For an integral basis \(b_1,\ldots,b_m\), the nondegenerate trace pairing gives a unique rational basis \(b_1^\vee,\ldots,b_m^\vee\) with \(\operatorname{Tr}(b_i^\vee b_j)=\delta_{ij}\). The codifferent is their integer span. This is the basis realization of [[linear-algebra/dual-basis|duality]] through the trace pairing.

## Clearing denominators

Integrality of traces gives \(\mathcal O_K\subseteq\mathcal O_K^\vee\). Since its basis lies in \(K\), some integer \(N\geq1\) satisfies \(N\mathcal O_K^\vee\subseteq\mathcal O_K\). These inclusions allow equivalent ergodicity tests with integral coefficients, though the complete character lattice is still the codifferent.

## Gaussian integers

For \(K=\mathbb Q(i)\), testing against \(1,i\) gives \(\mathcal O_K^\vee=\tfrac12\mathbb Z[i]\). The codifferent need not equal the ring of integers.

## References

1. Keith Conrad, [*The Different Ideal*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf). Definition 3.2, Theorem 3.4, and §4.
