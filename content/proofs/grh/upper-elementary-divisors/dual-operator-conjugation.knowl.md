+++
id = "proofs/grh/upper-elementary-divisors/dual-operator-conjugation"
title = "Conjugation and trace of the dual operator"
kind = "lemma"
summary = "Conjugating a polynomial by a point of the Levi subgroup conjugates its dual operator by the tensor power, and the trace of the dual operator of a monomial is a scaled value at the identity."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.dualOperator_conjSubst", "New.Average.leviGeneric_map_linSubst_transpose", "New.Average.trace_dualOperator_monomial", "New.Average.trace_leviTensor", "New.Average.sum_trace_dualOperator"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

**Lemma.** Use the notation of the [[proofs/grh/upper-elementary-divisors/schur-algebra-of-levi|Schur algebra of \(L_\tau\)]] and of [[proofs/grh/upper-elementary-divisors/conjugation-invariant-average|conjugation]] \(c_a\); let \(\iota\colon W\to O\) be a homomorphism of commutative rings and \(\eta\) a function on exponents.

1. If \(\eta\) is a system of [[proofs/grh/upper-elementary-divisors/adjoint-weights|adjoint weights]], then for \(a\in L_\tau(W)\) and \(\psi\in O[X]\): \((c_a\psi)^{\sharp}=\iota(a)^{\otimes d}\,\psi^{\sharp}\,\iota(a^{-1})^{\otimes d}\).
2. For every monomial, \(\operatorname{tr}\bigl((X^{\alpha})^{\sharp}\bigr)=\binom{d}{\alpha}\eta(\alpha)\cdot X^{\alpha}(1)\) if \(\lvert\alpha\rvert=d\), and \(0\) otherwise, where \(X^{\alpha}(1)\) is the value at the identity matrix.
3. If \(c\in O\) satisfies \(c=\binom{\lvert\alpha\rvert}{\alpha}\eta(\alpha)\) for all \(\alpha\) with \(\lvert\alpha\rvert\le D\), and \(\deg\psi\le D\), then \(\sum_{d=0}^{D}\operatorname{tr}(\psi^{\sharp,d})=c\,\psi(1)\), where \(\psi^{\sharp,d}\) is the dual operator in degree \(d\).

## Proof

(1) Both sides are linear in \(\psi\); take \(\psi=X^{\alpha}\). Conjugation \(c_a\) is the linear substitution \(L_A\) on the \(k^{2}\) variables with \(A=\,{}^{t}\iota(a^{-1})\otimes\iota(a)\). By adjointness, \(\eta(\gamma)[X^{\gamma}]L_A(X^{\alpha})=\eta(\alpha)[X^{\alpha}]L_{{}^tA}(X^{\gamma})\), so \((c_aX^{\alpha})^{\sharp}\) is obtained by applying the linear form \(\eta(\alpha)\,[X^{\alpha}]\circ L_{{}^tA}\) to the entries of \(G_\tau^{\otimes d}\). A direct computation, using that \(a\) and \(a^{-1}\) vanish off the blocks of \(\tau\) (so that in \(\sum_{s,t}\iota((a^{-1})_{sj})\iota(a_{it})X_{st}\) the block condition \(\tau(i)=\tau(j)\) is equivalent to \(\tau(t)=\tau(s)\) on nonzero terms), gives \(L_{{}^tA}(G_\tau)=\iota(a)\,G_\tau\,\iota(a^{-1})\) entrywise, hence \(L_{{}^tA}(G_\tau^{\otimes d})=\iota(a)^{\otimes d}G_\tau^{\otimes d}\iota(a^{-1})^{\otimes d}\). Applying the \(O\)-linear form \(\eta(\alpha)[X^{\alpha}]\) entrywise commutes with multiplication by constant matrices, which yields the claim.

(2) \(\operatorname{tr}((X^{\alpha})^{\sharp})=\eta(\alpha)\,[X^{\alpha}]\operatorname{tr}(G_\tau^{\otimes d})\) and \(\operatorname{tr}(G_\tau^{\otimes d})=(\operatorname{tr}G_\tau)^{d}=(\sum_iX_{ii})^{d}\). By the [[?c:Multinomial theorem|multinomial theorem]], the coefficient of \(X^{\alpha}\) is \(\binom{d}{\alpha}\) if \(\lvert\alpha\rvert=d\) and \(\alpha\) is supported on the diagonal, and \(0\) otherwise; and \(X^{\alpha}(1)\) is \(1\) or \(0\) according as \(\alpha\) is supported on the diagonal or not.

(3) Expand \(\psi\) in monomials and sum (2) over \(d\le D\): each monomial of degree \(\le D\) contributes for exactly one \(d\). \(\square\)

## References

1. Lean: `New.Average.dualOperator_conjSubst`, `New.Average.leviGeneric_map_linSubst_transpose`, `New.Average.trace_dualOperator_monomial`, `New.Average.trace_leviTensor`, `New.Average.sum_trace_dualOperator` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
