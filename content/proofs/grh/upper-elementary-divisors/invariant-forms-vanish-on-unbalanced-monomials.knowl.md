+++
id = "proofs/grh/upper-elementary-divisors/invariant-forms-vanish-on-unbalanced-monomials"
title = "Conjugation-invariant forms vanish on unbalanced monomials"
kind = "lemma"
summary = "A linear form invariant under conjugation by a Levi subgroup of GL_k(W) vanishes on monomials whose row and column weights differ."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.apply_monomial_eq_zero_of_weight_ne"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

**Lemma.** Let \(W\) be a [[algebra-commutative/local-ring|local ring]], \(O\) an [[algebra-rings/integral-domain|integral domain]] of characteristic \(0\), \(\iota\colon W\to O\) a ring homomorphism, and \(p>0\) an integer that is not a unit of \(O\). Let \(\tau\) be a labelling of \(\{0,\dots,k-1\}\), \(\rho\in\mathbb{Z}^{k}\), and let \(I\colon O[X]\to O\) be an \(O\)-linear form with \(I(c_a\psi)=I(\psi)\) for all \(a\in L_\tau(W)\) and all \(\psi\) (notation of [[proofs/grh/upper-elementary-divisors/conjugation-invariant-average|averages]]). If the row weight and the column weight of \(X^{\alpha}\) for \(\rho\) differ, then \(I(X^{\alpha})=0\).

## Proof

The element \(1+p\in W\) is a unit: in a local ring either \(-p\) or \(1+p\) is a unit, and if \(-p\) were a unit of \(W\) then \(p\) would be a unit of \(O\). Let \(u=1+p\in W^{\times}\) and \(a=\operatorname{diag}(u^{\rho_i})\); it is diagonal, hence in \(L_\tau(W)\). By the scaling rule, \(c_a(X^{\alpha})=\iota(u)^{e}X^{\alpha}\) with \(e\ne0\) the column weight minus the row weight. Invariance gives \(\iota(u)^{e}I(X^{\alpha})=I(X^{\alpha})\). Now \(\iota(u)=1+p\in O\) is not a root of unity, since \(O\) has characteristic \(0\) and \((1+p)^{m}>1\) as integers for \(m\ge1\); so \(\iota(u)^{e}\neq1\), and \(I(X^{\alpha})=0\) because \(O\) is a domain. \(\square\)

## References

1. Lean: `New.Average.apply_monomial_eq_zero_of_weight_ne` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
