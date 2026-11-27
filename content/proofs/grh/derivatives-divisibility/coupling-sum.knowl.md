+++
id = "proofs/grh/derivatives-divisibility/coupling-sum"
title = "Sum of powers of couplings"
kind = "definition"
summary = "The integral series Xi, the sum over e in S and j of lambda_{e,j} times the p^j-th power of the coupling Gamma_e."
aliases = ["coupling sum", "series Xi of couplings"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.couplingSum", "New.hasSum_couplingSum", "New.constantCoeff_couplingSum", "New.hasSum_subst_couplingSum", "New.rescale_couplingSum"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
+++

**Definition (coupling sum).** Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\), \(\Phi\) and \(c\) finite sets, \(\operatorname{pr}\) a partner rule on \(\Phi\) with [[proofs/grh/derivatives-divisibility/coupling|couplings]] \(\Gamma_e\in\mathcal{O}[\![z_x : x\in\Phi\times c]\!]\), \(S\subseteq\mathbb{N}\) a set of exponents and \(\lambda=(\lambda_{e,j})_{e,j\ge 0}\) a family of elements of \(\mathcal{O}\). The **coupling sum** is the integral power series
\[
\Xi_{S,\operatorname{pr},\lambda}=\sum_{e\in S}\ \sum_{j\ge 0}\lambda_{e,j}\,\Gamma_e^{\,p^j}.
\]
The sum is locally finite: the term \((e,j)\) has order at least \(p^j(p^e+1)\), so only finitely many terms have order at most \(n\).

## Properties

1. \(\Xi_{S,\operatorname{pr},\lambda}\) has no constant term.
2. *Substitution term by term.* For series \(Z_x\) without constant term, \(\Xi(Z)=\sum_{e\in S}\sum_{j}\lambda_{e,j}\,\Gamma_e(Z)^{p^j}\); the sum is again locally finite, since substitution of series without constant term does not lower orders.
3. *Scaling.* For \(\alpha\in\mathcal{O}\),
\[
\Xi_{S,\operatorname{pr},\lambda}(\alpha z)=\Xi_{S,\operatorname{pr},\lambda'}(z),\qquad \lambda'_{e,j}=\alpha^{(p^e+1)p^j}\lambda_{e,j},
\]
because \(\Gamma_e\) is homogeneous of degree \(p^e+1\).

## Proof

For local finiteness: \(\Gamma_e\) has order at least \(p^e+1\), so \(\Gamma_e^{p^j}\) has order at least \(p^j(p^e+1)>\max(e,j)\) (as \(p\ge 2\)); a term of order at most \(n\) therefore has \(e\le n\) and \(j\le n\). Each term has no constant term, which gives 1. Substitution of series without constant term is a continuous ring homomorphism for coefficientwise convergence, which gives 2. For 3, apply 2 to \(Z_x=\alpha z_x\) and use \(\Gamma_e(\alpha z)^{p^j}=\alpha^{(p^e+1)p^j}\Gamma_e^{p^j}\).

## References

1. Lean: `New.couplingSum`, `New.hasSum_couplingSum`, `New.constantCoeff_couplingSum`, `New.hasSum_subst_couplingSum`, `New.rescale_couplingSum` in `src/New/Derivatives/Divisibility/NormalForm.lean`; the summability criterion is `New.summable_smul_pow_pow` in `src/Lib/General/Algebra/SeriesCongruences.lean`.
