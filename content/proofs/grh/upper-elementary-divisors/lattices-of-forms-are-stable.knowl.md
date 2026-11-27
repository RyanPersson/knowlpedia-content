+++
id = "proofs/grh/upper-elementary-divisors/lattices-of-forms-are-stable"
title = "The lattices of monomials and of divided powers are stable"
kind = "lemma"
summary = "The span of the monomials and, over a domain of characteristic 0, the span of the divided powers are stable under the twisted action of GL_k(W)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.polyAction_mem_monomialLattice", "New.FrobeniusCycle.polyAction_mem_dividedPowerLattice", "New.symPowMatrix_mul_multinomial", "New.FrobeniusCycle.polyAction_map_monomial", "New.dividedPowerLattice_le_monomialLattice", "New.dividedPowerCoeff_eq_prod_multinomial"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), \(K\) a commutative \(O\)-algebra, and let \(g\in\mathrm{GL}_k(W)\) act on \(K[x_{b,s}]\) by the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted action]] of the base-changed cycle. Let \(H\supseteq H^{\circ}\) be the [[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|lattices of monomials and of divided powers]] of degree \(n\) in each letter.

1. \(g\cdot H\subseteq H\).
2. If \(O\) is an integral domain of characteristic \(0\), then \(g\cdot H^{\circ}\subseteq H^{\circ}\).

## Proof

(1) \(g\cdot x^{\beta}=\sum_\alpha\rho_n(g)_{\alpha\beta}x^{\alpha}\) with \(\rho_n(g)_{\alpha\beta}\in O\).

(2) For a square matrix \(A\) over \(O\) and exponents \(\alpha,\beta\) of degree \(n\), \(\operatorname{Sym}^n(A)_{\alpha\beta}\binom n\beta=\binom n\alpha\operatorname{Sym}^n({}^tA)_{\beta\alpha}\): multiply the adjointness \(\alpha!\operatorname{Sym}^n(A)_{\alpha\beta}=\beta!\operatorname{Sym}^n({}^tA)_{\beta\alpha}\) for the Fock pairing (see [[proofs/grh/upper-elementary-divisors/adjoint-weights|adjoint weights]]) by \(\binom n\alpha\binom n\beta\) and use \(\gamma!\binom n\gamma=n!\): this gives \(n!\) times each side of the claim, and \(n!\ne0\) is cancellable in the domain \(O\) of characteristic \(0\). Taking the product over the letters, with \(c_\beta=\prod_s\binom n{\beta_s}\) and \(\rho'=\bigotimes_s\operatorname{Sym}^n({}^tg_s)\) (entries in \(O\)): \(\rho_n(g)_{\alpha\beta}c_\beta=c_\alpha\rho'_{\beta\alpha}\). Hence \(g\cdot(c_\beta x^{\beta})=\sum_\alpha\rho'_{\beta\alpha}\,c_\alpha x^{\alpha}\in H^{\circ}\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.polyAction_mem_monomialLattice`, `New.FrobeniusCycle.polyAction_mem_dividedPowerLattice`, `New.symPowMatrix_mul_multinomial`, `New.FrobeniusCycle.polyAction_map_monomial`, `New.dividedPowerLattice_le_monomialLattice`, `New.dividedPowerCoeff_eq_prod_multinomial` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
