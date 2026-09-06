+++
id = "operator-algebras/fock-module-cstar-correspondence"
title = "Fock module of a C*-correspondence"
kind = "definition"
summary = "The Hilbert-module direct sum of all tensor powers of a C*-correspondence, including the coefficient algebra in degree zero."
aliases = ["Fock correspondence", "full Fock module"]
domains = ["operator-algebras", "algebra-modules"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-correspondence", "operator-algebras/internal-tensor-product-correspondences", "operator-algebras/hilbert-cstar-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[operator-algebras/cstar-correspondence|\(C^*\)-correspondence]]
over \(A\). Put \(X^{\otimes 0}=A\), \(X^{\otimes 1}=X\), and recursively
\(X^{\otimes n}=X\otimes_A X^{\otimes(n-1)}\), using the
[[operator-algebras/internal-tensor-product-correspondences|internal tensor
product]]. The **Fock module** of \(X\) is the
[[operator-algebras/hilbert-cstar-module|Hilbert \(A\)-module]]
\[
\mathcal F(X)=\bigoplus_{n=0}^{\infty}X^{\otimes n}.
\]
Its left action \(\varphi_\infty:A\to\mathcal L_A(\mathcal F(X))\) is diagonal:
on degree zero it is left multiplication, and on degree \(n\geq1\) it is
\(\varphi_X(a)\otimes 1\). The tensor-degree summands are mutually
orthogonal.

## Creation operators

For \(\xi\in X\), the creation operator \(T_\xi\) raises tensor degree by one:
\[
T_\xi(a)=\xi a,\qquad
T_\xi(\eta_1\otimes\cdots\otimes\eta_n)
=\xi\otimes\eta_1\otimes\cdots\otimes\eta_n.
\]
It is [[operator-algebras/adjointable-operator-hilbert-module|adjointable]],
and the operators satisfy
\[
T_\xi^*T_\eta=\varphi_\infty(\langle\xi,\eta\rangle_A).
\]
Consequently \((T,\varphi_\infty)\) is the Fock Toeplitz representation.

## Grading and gauge action

Tensor degree gives \(\mathcal F(X)\) an \(\mathbb N\)-grading. For
\(z\) on the unit circle, the unitary \(U_z\) acts as multiplication by
\(z^n\) on \(X^{\otimes n}\). Conjugation fixes the diagonal copy of \(A\)
and sends \(T_\xi\) to \(zT_\xi\). This circle action is the concrete origin
of the gauge action on the Toeplitz–Pimsner algebra.

## Examples and scope

For \(A=\mathbb C\) and \(X=\mathbb C^d\),
\(\mathcal F(X)=\bigoplus_{n\geq0}(\mathbb C^d)^{\otimes n}\), the usual full
Fock space. If \(X=A\) with its standard correspondence structure, every
tensor power is canonically \(A\), so the Fock module is the standard module
\(\ell^2(\mathbb N)\otimes A\).

**Warning.** The degree-zero summand is part of the definition. Omitting it
produces the positive-degree submodule and removes the vacuum summand used by
the creation-operator model.

## References

1. Michael V. Pimsner, “A Class of C*-Algebras Generalizing Both Cuntz–Krieger Algebras and Crossed Products by Z,” in *Free Probability Theory*, Fields Institute Communications 12, American Mathematical Society, 1997, 189–212. [Bibliographic record](https://cir.nii.ac.jp/crid/1570572699254124800). Relevant: tensor powers, Fock module, and creation operators.
2. Takeshi Katsura, “On C*-algebras associated with C*-correspondences,” *Journal of Functional Analysis* 217 (2004), 366–401. [DOI record](https://doi.org/10.1016/j.jfa.2004.03.010). Relevant: the Fock representation and gauge action.
