+++
id = "operator-algebras/cstar-tensor-norm"
title = "C*-tensor norm"
kind = "definition"
summary = "A norm on the algebraic tensor product of two C*-algebras whose completion is again a C*-algebra."
aliases = ["C*-cross norm", "C*-tensor product norm"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
A **\(C^*\)-tensor norm** on their algebraic tensor product \(A\odot B\) is a
norm \(\gamma\) for which the natural multiplication and involution extend to
the completion and
\[
\|x^*x\|_\gamma=\|x\|_\gamma^2\qquad(x\in A\odot B).
\]
The completion is denoted \(A\otimes_\gamma B\). Such a norm restricts to the
given norms on the factors and satisfies
\(\|a\otimes b\|_\gamma=\|a\|\,\|b\|\). Distinct \(C^*\)-tensor norms can
therefore agree on elementary tensors while assigning different norms to
finite sums of them.

## Extremal norms

Every \(C^*\)-tensor norm lies between two canonical ones:
\[
\|x\|_{\min}\leq \|x\|_\gamma\leq\|x\|_{\max}.
\]
The [[operator-algebras/minimal-cstar-tensor-product|minimal norm]] is obtained
from faithful spatial representations of the factors. The
[[operator-algebras/maximal-cstar-tensor-product|maximal norm]] is the
supremum over all compatible representations and has a universal property.
Thus a \(C^*\)-tensor norm amounts to a completion intermediate between the
spatial and universal completions.

## Why the algebraic tensor product is insufficient

The [[algebra-modules/tensor-product-algebras|algebraic tensor product]]
remembers bilinear algebra but carries no distinguished complete norm. For
finite-dimensional [[operator-algebras/matrix-cstar-algebra|matrix algebras]]
the \(C^*\)-tensor norm is unique, while for general algebras uniqueness can
fail. Asking for uniqueness against every second \(C^*\)-algebra leads to
nuclearity.

For example, representing \(A\) on \(H\) and \(B\) on \(K\) gives a norm from
the action of \(A\odot B\) on \(H\otimes K\). In contrast, representing both
factors with commuting ranges on one
[[linear-algebra/hilbert-space|Hilbert space]] contributes to the maximal norm.
These constructions agree on \(a\otimes b\), but need not agree on a sum
\(\sum_i a_i\otimes b_i\).

## Conventions and scope

**Warning.** A Banach-space cross norm need not satisfy the \(C^*\)-identity
or make multiplication continuous, so it need not be a \(C^*\)-tensor norm.
Likewise, “injective” and “projective” tensor norms in Banach-space theory are
not automatically the minimal and maximal \(C^*\)-norms. The symbol
\(\odot\) here denotes the uncompleted algebraic product; \(\otimes_\gamma\)
denotes its \(C^*\)-completion.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV on tensor products of C*-algebras.
2. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3 on minimal and maximal tensor products and nuclearity.
