+++
id = "proofs/grh/derivatives-vacuum/largest-coefficient-among-integral-series"
title = "A monomial has the largest coefficient among integral series"
kind = "lemma"
summary = "Among all integral power series in given series without constant term, multiplied by a fixed series, a monomial of degree at most the degree of alpha has the coefficient at alpha of largest p-adic absolute value."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_monomial_max_norm_coeff", "New.CMLattice.exists_norm_coeff_le_norm_coeff_prod_pow"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
proof_status = "full"
+++

Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\), and \(I\), \(X\) finite sets.

**Lemma.** Let \(f_i\in\mathbb{C}_p[\![z_x:x\in X]\!]\) (\(i\in I\)) have zero constant terms, let \(s\) be a power series in the \(z_x\) and \(\alpha\) an exponent vector. Then there is \(m\in\mathbb{N}^I\) with \(\lvert m\rvert\le\lvert\alpha\rvert\) such that for every \(G\in\mathcal{O}[\![T_i:i\in I]\!]\)
\[ \bigl\lvert[z^\alpha]\bigl(G(f)\,s\bigr)\bigr\rvert_p\le\bigl\lvert[z^\alpha]\bigl(\textstyle\prod_if_i^{m_i}\cdot s\bigr)\bigr\rvert_p . \]
In particular, for a CM lattice \(C\) and linear forms \(\mu_i\), some monomial \(\prod_iy(\mu_iz)^{e_i}\) has a coefficient at \(\alpha\) whose absolute value bounds that of every element of the [[?lean:New.CMLattice.multiSeriesRing|ring \(\mathcal{O}[\![y(\mu z)]\!]\)]].

## Proof

Since the \(f_i\) have no constant term, \(f^d=\prod f_i^{d_i}\) has order \(\ge\lvert d\rvert\), so only the monomials \(T^d\) with \(\lvert d\rvert\le\lvert\alpha\rvert\) contribute: \([z^\alpha](G(f)s)=\sum_{\lvert d\rvert\le\lvert\alpha\rvert}G_d\,a_d\) with \(a_d=[z^\alpha](f^ds)\). This is a finite sum; choose \(m\) among these \(d\) with \(\lvert a_m\rvert_p\) maximal. As \(\lvert G_d\rvert_p\le1\), the ultrametric inequality gives the claim. The particular case is \(f_i=y(\mu_iz)\) (\(y(0)=0\)) and \(s=1\).

## References

1. Lean: `New.exists_monomial_max_norm_coeff`, `New.CMLattice.exists_norm_coeff_le_norm_coeff_prod_pow` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
