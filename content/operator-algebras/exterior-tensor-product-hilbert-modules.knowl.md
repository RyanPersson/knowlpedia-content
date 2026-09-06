+++
id = "operator-algebras/exterior-tensor-product-hilbert-modules"
title = "Exterior tensor product of Hilbert C*-modules"
kind = "definition"
summary = "The Hilbert module obtained by tensoring two Hilbert modules over the minimal tensor product of their coefficient algebras."
aliases = ["external tensor product of Hilbert modules"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/hilbert-cstar-module", "operator-algebras/minimal-cstar-tensor-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a right [[operator-algebras/hilbert-cstar-module|Hilbert \(A\)-module]] and \(F\) a right Hilbert \(B\)-module. On the algebraic
complex tensor product \(E\odot F\), define
\[
(x\otimes y)(a\otimes b)=xa\otimes yb
\]
and
\[
\langle x_1\otimes y_1,x_2\otimes y_2\rangle
=\langle x_1,x_2\rangle_A\otimes\langle y_1,y_2\rangle_B,
\]
extending sesquilinearly. After quotienting by zero-length vectors and
completing in the induced norm, one obtains the **exterior tensor product**
\(E\boxtimes F\), a Hilbert module over the
[[operator-algebras/minimal-cstar-tensor-product|minimal tensor product]]
\(A\otimes_{\min}B\).

## Positivity and completion

The essential point is that the displayed algebra-valued form is positive on
finite sums, not only on elementary tensors. Its null space is a submodule,
and the quotient norm is
\[
\|z\|=\|\langle z,z\rangle\|^{1/2}.
\]
Completing produces a Hilbert \(A\otimes_{\min}B\)-module independent of
concrete faithful representations used to realize the minimal tensor norm.

## Standard examples

Taking \(E=A\) and \(F=B\) with their standard module structures gives
\(A\boxtimes B\cong A\otimes_{\min}B\). For column modules,
\[
A^m\boxtimes B^n\cong(A\otimes_{\min}B)^{mn}.
\]
When \(A=B=\mathbb C\), the construction reduces to the Hilbert-space tensor
product. These examples show that both the vectors and their coefficient
algebras are tensorized.

## Exterior versus interior tensoring

The exterior product starts with modules over unrelated algebras and uses the
complex tensor product. By contrast, the
[[operator-algebras/internal-tensor-product-correspondences|internal tensor product of correspondences]] balances over a shared intermediate algebra:
relations of the form \(xa\otimes y=x\otimes ay\) are imposed. The two
constructions can interact, but they solve different composition problems.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, London Mathematical Society Lecture Note Series 210, Cambridge University Press, 1995. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 4 on tensor products of Hilbert modules.
