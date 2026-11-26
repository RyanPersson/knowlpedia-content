+++
id = "proofs/grh/upper-elementary-divisors/existence-of-average"
title = "Existence of an average for a Levi subgroup"
kind = "theorem"
summary = "Over a valuation domain of characteristic 0 in which p is not a unit, there is a conjugation-invariant linear form that kills monomials of large row weight and equals p^(k^2 f) times evaluation at 1 on polynomials of degree below p^f without such monomials."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.exists_isAverage", "New.Average.averagePart", "New.Average.largeWeightTrace", "New.Average.averagePart_conjSubst", "New.Average.averagePart_monomial_eq_zero_of_lt", "New.Average.largeWeightTrace_mem", "New.Average.dualOperator_mulVec_mem_smul", "New.Average.dualOperator_mulVec_single_mem_smul", "New.Average.range_dualOperator_monomial_le", "New.Average.trace_mem_of_forall_mem_smul_top"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be a [[?c:Valuation ring|valuation ring]] that is a domain of characteristic \(0\), \(p\) a prime that is not a unit of \(O\), \(W\) a [[algebra-commutative/local-ring|local ring]], and \(\iota\colon W\to O\) a ring homomorphism. Let \(k,f,D\ge0\) with \(D<p^{f}\), and suppose the residue field of \(W\) is finite with at least \(D+k\) elements. Then for every labelling \(\tau\) of \(\{0,\dots,k-1\}\), every \(\rho\in\mathbb{Z}^{k}\) and every \(t\in\mathbb{Z}\) there is an [[proofs/grh/upper-elementary-divisors/conjugation-invariant-average|average]] \(I\) for \((\tau,\iota,\rho,t,\,c,\,D)\) with \(c=p^{k^{2}f}\).

## Proof

Choose [[proofs/grh/upper-elementary-divisors/adjoint-weights|adjoint weights]] \(\eta\) on the \(k^{2}\) variables with \(p^{k^{2}f}=\binom{\lvert\alpha\rvert}{\alpha}\eta(\alpha)\) for \(\lvert\alpha\rvert<p^{f}\), in particular for \(\lvert\alpha\rvert\le D\). For \(0\le d\le D\) let \(\psi^{\sharp,d}\) be the [[proofs/grh/upper-elementary-divisors/schur-algebra-of-levi|dual operator]] on \(U_d\) and \(U_{+,d}\) the [[proofs/grh/upper-elementary-divisors/large-weight-submodule|large weight submodule]] for \((\tau,\rho,t,d)\); it is stable under the Schur algebra (as \(d+k\le D+k\) is at most the size of the residue field) and free of finite rank. Define
\[
I(\psi)=\sum_{d=0}^{D}\Bigl(\operatorname{tr}\bigl(\psi^{\sharp,d}\mid U_d\bigr)-\operatorname{tr}\bigl(\psi^{\sharp,d}\mid U_{+,d}\bigr)\Bigr).
\]

*Invariance.* By [[proofs/grh/upper-elementary-divisors/dual-operator-conjugation|the conjugation rule]], \((c_a\psi)^{\sharp,d}=g\,\psi^{\sharp,d}g^{-1}\) with \(g=\iota(a)^{\otimes d}\), and \(g,g^{-1}\) are in the Schur algebra, so they preserve \(U_{+,d}\) and are inverse automorphisms of it. Both traces are invariant under conjugation.

*Bad monomials.* Let \(X^{\alpha}\) have row weight \(>t\). Then \((X^{\alpha})^{\sharp,d}\) maps \(U_d\) into \(U_{+,d}\): it kills \(e_j\) unless the weight of \(e_j\) equals the row weight of \(\alpha\), which is \(>t\), and then the image is in \(U_{+,d}\) by definition. For an endomorphism \(\phi\) of a finite free module \(U\) with image in a free submodule \(U_+\), \(\operatorname{tr}(\phi\mid U)=\operatorname{tr}(\phi\mid U_+)\) (write \(\phi=j\circ\phi_0\) with \(j\colon U_+\hookrightarrow U\) and use \(\operatorname{tr}(j\phi_0)=\operatorname{tr}(\phi_0j)\)). Hence each summand of \(I(X^{\alpha})\) vanishes.

*Comparison with evaluation.* Let \(\deg\psi\le D\). By part 3 of the conjugation lemma, \(\sum_d\operatorname{tr}(\psi^{\sharp,d}\mid U_d)=p^{k^{2}f}\psi(1)\), so \(I(\psi)-p^{k^{2}f}\psi(1)=-\sum_d\operatorname{tr}(\psi^{\sharp,d}\mid U_{+,d})\). Assume that for all \(a\in L_\tau(W)\) the bad coefficients of \(c_a\psi\) lie in \(J\). We claim \(\psi^{\sharp,d}U_{+,d}\subseteq JU_{+,d}\); then the trace on the free module \(U_{+,d}\) lies in \(J\) (compute it in a basis: each diagonal entry is in \(J\)), which finishes the proof.

First, for any \(\varphi\) whose bad coefficients lie in \(J\) and any \(e_j\) of weight \(>t\): \(\varphi^{\sharp,d}e_j=\sum_\alpha[X^{\alpha}]\varphi\cdot(X^{\alpha})^{\sharp,d}e_j\); terms with \(\alpha\) bad lie in \(J\,U_{+,d}\), and terms with \(\alpha\) not bad vanish, because the row weight of \(\alpha\) is \(\le t<\) weight of \(e_j\). By the generation property of \(U_{+,d}\) it suffices to show \(\psi^{\sharp,d}\,g\,e_j\in JU_{+,d}\) for \(g=\iota(a)^{\otimes d}\), \(a\in L_\tau(W)\), \(e_j\) of weight \(>t\). By the conjugation rule, \(\psi^{\sharp,d}g=g\,(c_{a^{-1}}\psi)^{\sharp,d}\); the first step applied to \(\varphi=c_{a^{-1}}\psi\) gives \((c_{a^{-1}}\psi)^{\sharp,d}e_j\in JU_{+,d}\), and \(g\) preserves \(JU_{+,d}\). \(\square\)

## References

1. Lean: `New.Average.exists_isAverage`, `New.Average.averagePart`, `New.Average.largeWeightTrace`, `New.Average.averagePart_conjSubst`, `New.Average.averagePart_monomial_eq_zero_of_lt`, `New.Average.largeWeightTrace_mem`, `New.Average.dualOperator_mulVec_mem_smul`, `New.Average.dualOperator_mulVec_single_mem_smul`, `New.Average.range_dualOperator_monomial_le`, `New.Average.trace_mem_of_forall_mem_smul_top` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
