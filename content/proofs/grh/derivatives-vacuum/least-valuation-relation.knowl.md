+++
id = "proofs/grh/derivatives-vacuum/least-valuation-relation"
title = "The least valuation of coefficients of products of theta products"
kind = "definition"
summary = "The relation val_n(nu) <= r saying that some product over n copies of series H_c Theta, with H_c integral series in the parameters, has a product of coefficients of total degree nu of valuation at most r."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.LeastValLE", "New.CMLattice.LeastValLE.mono", "New.CMLattice.leastValLE_zero", "New.CMLattice.constantCoeff_thetaProd", "New.CMLattice.isLowestTerm_thetaProd"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
+++

Let \(C\) be a [[?lean:New.CMLattice|CM lattice]] for \(d\), \(p\) a prime, \(\iota_p\) a \(p\)-adic place, \(J\), \(X\) finite sets, \(\mu_j\) (\(j\in J\)) linear forms in the variables \(z_x\) (\(x\in X\)) with coefficients in \(\mathbb{C}_p\), and \(m\in\mathbb{N}^J\). Let \(\Theta=\prod_j\theta(\mu_jz)^{m_j}\) be the [[?lean:New.CMLattice.thetaProd|theta product]] and \(\mathcal{O}[\![y(\mu z)]\!]\) the [[?lean:New.CMLattice.multiSeriesRing|ring of integral series in the \(y(\mu_jz)\)]].

For \(n\in\mathbb{N}\), an exponent \(\nu\) on \(X\) and \(r\in\mathbb{R}\), write
\[ \operatorname{val}_n(\nu)\le r \]
if there are \(H_1,\dots,H_n\in\mathcal{O}[\![y(\mu z)]\!]\) and exponents \(\alpha_1,\dots,\alpha_n\) with \(\sum_c\alpha_c=\nu\) and
\[ \prod_{c=1}^n\bigl\lvert[z^{\alpha_c}](H_c\Theta)\bigr\rvert_p\ge p^{-r}. \]
(The left side is the absolute value of one coefficient of the series \(\prod_c(H_c\Theta)(z_c)\) in \(n\) copies of the variables.)

## Properties

The relation is monotone in \(r\). Since \(\theta(0)=1\), \(\Theta\) has constant term \(1\), so \(\operatorname{val}_n(0)\le0\) (all \(H_c=1\)).

## References

1. Lean: `New.CMLattice.LeastValLE`, `New.CMLattice.LeastValLE.mono`, `New.CMLattice.leastValLE_zero`, `New.CMLattice.constantCoeff_thetaProd`, `New.CMLattice.isLowestTerm_thetaProd` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
