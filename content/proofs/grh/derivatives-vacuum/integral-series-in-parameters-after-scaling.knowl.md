+++
id = "proofs/grh/derivatives-vacuum/integral-series-in-parameters-after-scaling"
title = "Integral series in the parameters have integral coefficients after scaling"
kind = "lemma"
summary = "If the linear forms are integral and the scale has valuation at least rho_p, an integral series in the y(mu_j z) has integral coefficients after rescaling the variables."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.rescale_mem_range_seriesToCp_of_mem_multiSeriesRing"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-relation|the least valuation relation]]; \(d\) is a prime \(\equiv7\bmod8\), \(\rho_p\) the [[?lean:New.varpiValuation|valuation of \(\varpi\)]].

**Lemma.** If \(\lvert\mu_{i,x}\rvert_p\le1\) for all \(i,x\) and \(\varpi\in\mathbb{C}_p\) has \(\lvert\varpi\rvert_p\le p^{-\rho_p}\), then for every \(H\in\mathcal{O}[\![y(\mu z)]\!]\) the series \(H(\varpi z)\) has coefficients in \(\mathcal{O}_{\mathbb{C}_p}\).

## Proof

In one variable, \(y(\varpi z)\) has integral coefficients; this is a result of the formal-group chapter (Lean `New.CMLattice.rescale_mem_range_seriesToCp`; asserted here). Hence \(y(\mu_i(\varpi z))\), obtained by substituting the integral linear form \(\mu_i(z)\), is an integral series \(Y_i\) without constant term. If \(H=g(y(\mu_iz))_i\) with \(g\) integral, then \(H(\varpi z)=g(Y_i)_i\) is integral.

## References

1. Lean: `New.CMLattice.rescale_mem_range_seriesToCp_of_mem_multiSeriesRing` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
