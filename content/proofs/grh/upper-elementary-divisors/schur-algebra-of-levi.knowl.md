+++
id = "proofs/grh/upper-elementary-divisors/schur-algebra-of-levi"
title = "Schur algebra of a Levi subgroup and the operator dual to a polynomial"
kind = "construction"
summary = "The map from linear forms on monomials of degree d to operators on the d-th tensor power, built from the generic block matrix, and the operator attached to a polynomial through adjoint weights."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.leviGeneric", "New.Average.leviTensor", "New.Average.schurMap", "New.Average.leviMonomialValues", "New.Average.scaledCoeff", "New.Average.dualOperator", "New.Average.schurMap_apply_monomial", "New.Average.schurMap_leviMonomialValues", "New.Average.leviTensor_apply", "New.Average.dualOperator_monomial", "New.Average.schurMap_leviMonomialValues_mul"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
+++

Let \(O\) be a commutative ring, \(k,d\ge0\), and \(\tau\) a labelling of \(\{0,\dots,k-1\}\). Let \(U_d=(O^{k})^{\otimes d}\), with basis the tensors \(e_j\), \(j\in\{0,\dots,k-1\}^{d}\), and let \(\mathcal{M}_d\) be the set of exponents of degree \(d\) on the variables \(X_{ij}\).

- The **generic block matrix** (transposed) is \(G_\tau\in M_k(O[X])\) with \((G_\tau)_{ij}=X_{ji}\) if \(\tau(i)=\tau(j)\) and \(0\) otherwise. Its \(d\)-th tensor power \(G_\tau^{\otimes d}\in M_{k^{d}}(O[X])\) has the entry \(\prod_{l}X_{j_l i_l}\) at \((i,j)\) if \(\tau(i_l)=\tau(j_l)\) for all \(l\), and \(0\) otherwise.
- The **Schur map** \(S_d\colon O^{\mathcal{M}_d}\to\operatorname{End}_O(U_d)=M_{k^{d}}(O)\) is the \(O\)-linear map sending the basis vector at \(\gamma\) to the matrix of coefficients of \(X^{\gamma}\) in the entries of \(G_\tau^{\otimes d}\). Equivalently, for a linear form \(l\) on \(O[X]\), \(S_d\bigl((l(X^{\gamma}))_\gamma\bigr)\) is \(G_\tau^{\otimes d}\) with \(l\) applied to each entry. Its image is the **Schur algebra** of \(L_\tau\) in degree \(d\) ([[?c:Schur algebra|Schur algebra]]).
- For a ring homomorphism \(\iota\colon W\to O\) and \(a\in L_\tau(W)\), let \(v(a)=\bigl(\iota(\text{value of }X^{\gamma}\text{ at }X_{ji}=a_{ij})\bigr)_\gamma\). Then \(S_d(v(a))=\iota(a)^{\otimes d}\); in particular \(S_d(v(aa'))=S_d(v(a))S_d(v(a'))\) and \(S_d(v(a^{-1}))S_d(v(a))=1\).
- For a function \(\eta\) on exponents and \(\psi\in O[X]\), the **dual operator** is \(\psi^{\sharp}=S_d\bigl((\,[X^{\gamma}]\psi\cdot\eta(\gamma))_{\gamma\in\mathcal{M}_d}\bigr)\in M_{k^{d}}(O)\): its entry at \((i,j)\) is \(\eta(\alpha)\) times the coefficient in \(\psi\) of \(X^{\alpha}=\prod_lX_{j_li_l}\) if \(\tau(i_l)=\tau(j_l)\) for all \(l\), and \(0\) otherwise. Only the part of degree \(d\) of \(\psi\) matters.

## Remarks

All \(k^{2}\) entries are variables; a monomial containing an entry outside the blocks of \(\tau\) has dual operator \(0\). The Schur algebra is built on the transpose of the matrix of variables, so the row indices of a monomial are the column indices of \(\psi^{\sharp}\): \((X^{\alpha})^{\sharp}e_j=0\) unless the weight \(\sum_l\rho_{j_l}\) of \(e_j\) equals the row weight of \(\alpha\).

## References

1. Lean: `New.Average.leviGeneric`, `New.Average.leviTensor`, `New.Average.schurMap`, `New.Average.leviMonomialValues`, `New.Average.scaledCoeff`, `New.Average.dualOperator`, `New.Average.schurMap_apply_monomial`, `New.Average.schurMap_leviMonomialValues`, `New.Average.leviTensor_apply`, `New.Average.dualOperator_monomial`, `New.Average.schurMap_leviMonomialValues_mul` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
2. J. A. Green, *Polynomial Representations of GL_n*, Lecture Notes in Mathematics 830, Springer, 1980; D. Benson and S. Doty, Schur–Weyl duality over finite fields, 2009 (cited in the head of the Lean file for the Schur algebra and its spanning by group elements).
