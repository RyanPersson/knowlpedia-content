+++
id = "operator-algebras/internal-tensor-product-correspondences"
title = "Internal tensor product of C*-correspondences"
kind = "definition"
summary = "The composite correspondence obtained by balancing two Hilbert modules, quotienting null vectors, and completing."
aliases = ["interior tensor product", "balanced tensor product of Hilbert modules"]
domains = ["operator-algebras", "algebra-modules"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-correspondence", "algebra-modules/tensor-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a [[operator-algebras/cstar-correspondence|\(C^*\)-correspondence]]
from \(A\) to \(B\), and let \(F\) be one from \(B\) to \(C\), with left
action \(\varphi_F:B\to\mathcal L_C(F)\). Their **internal tensor product**
\(E\otimes_B F\) is the completion of the
[[algebra-modules/tensor-product|balanced algebraic tensor product]]
\(E\odot_B F\), after quotienting vectors of zero length, for the
\(C\)-valued inner product
\[
\langle\xi_1\otimes\eta_1,\xi_2\otimes\eta_2\rangle_C
=\langle\eta_1,\varphi_F(\langle\xi_1,\xi_2\rangle_B)\eta_2\rangle_C.
\]
The right \(C\)-action comes from \(F\), and \(A\) acts by
\(a\cdot(\xi\otimes\eta)=(a\cdot\xi)\otimes\eta\). Thus \(E\otimes_B F\) is
a correspondence from \(A\) to \(C\).

## Construction and positivity

Balancing imposes \((\xi b)\otimes\eta=\xi\otimes\varphi_F(b)\eta\). The
displayed formula is compatible with this relation and defines a positive
semidefinite form; its null space must be removed before completion. This
quotient-and-completion step is essential: the ordinary algebraic tensor
product is generally neither definite nor complete. Adjointable operators on
\(E\) induce adjointable operators \(T\otimes 1\) on the completed product,
which supplies the left \(A\)-action.

## Composition and unit correspondences

Internal tensor product is associative up to the canonical unitary
\[
(E\otimes_B F)\otimes_C G\longrightarrow E\otimes_B(F\otimes_C G),
\qquad
(\xi\otimes\eta)\otimes\zeta\longmapsto\xi\otimes(\eta\otimes\zeta).
\]
The standard correspondence \(A\) from \(A\) to itself is a unit:
\(A\otimes_A E\cong E\) and \(E\otimes_B B\cong E\). These canonical
unitaries, rather than literal equalities of modules, provide the composition
and identity laws for correspondences.

## Examples and scope

When \(B=\mathbb C\), the construction reduces to the Hilbert-space tensor
product, with any remaining coefficient algebra carried by \(F\). If the
left \(B\)-action on \(F\) annihilates a nonzero ideal, tensors involving that
ideal can become null; this is why the quotient cannot be omitted.

**Warning.** “Interior tensor product” sometimes refers more generally to a
right Hilbert \(B\)-module tensored with any correspondence from \(B\) to
\(C\). The definition above specializes that construction to two
correspondences so that the resulting left \(A\)-action is visible.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Chapter DOI record](https://doi.org/10.1017/CBO9780511526206.005). Relevant: Chapter 4, “Tensor products.”
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace C*-Algebras*, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 2 on Hilbert modules and internal tensor products.
