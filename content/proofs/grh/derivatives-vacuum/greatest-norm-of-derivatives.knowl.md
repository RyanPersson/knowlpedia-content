+++
id = "proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives"
title = "The greatest norm of the n-th derivatives of integral series in y"
kind = "definition"
summary = "The supremum, which is a maximum attained by a power of y, of the p-adic absolute values of the n-th derivatives at 0 of the integral power series in the parameter y of a CM lattice."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.maxDerivNorm", "New.CMLattice.exists_isGreatest_norm_deriv", "New.CMLattice.exists_norm_deriv_eq_maxDerivNorm", "New.CMLattice.norm_deriv_le_maxDerivNorm", "New.CMLattice.maxDerivNorm_nonneg", "New.CMLattice.norm_deriv_le_one", "New.CMLattice.maxDerivNorm_le_one", "New.CMLattice.maxDerivNorm_zero"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
+++

Let \(d\) be a prime \(\equiv7\bmod8\), \(C\) a [[?lean:New.CMLattice|CM lattice]] for \(d\), \(p\) a prime, \(\iota_p\) a \(p\)-adic place of \(\mathbb{C}\), \(y\in\mathbb{C}_p[\![z]\!]\) the Taylor series of the [[?lean:New.CMLattice.translatedY|translated coordinate]] read through \(\iota_p\), and \(\mathcal{O}[\![y]\!]\) the [[?lean:New.CMLattice.integralSeriesRing|ring of integral power series in \(y\)]]. For \(n\in\mathbb{N}\),
\[ c_C(n)=\sup\bigl\{\lvert g^{(n)}(0)\rvert_p:\ g\in\mathcal{O}[\![y]\!]\bigr\},\qquad g^{(n)}(0)=n!\,[z^n]g . \]

## Properties

1. The supremum is attained, by a power \(y^i\): by [[proofs/grh/derivatives-vacuum/largest-coefficient-among-integral-series|the lemma on largest coefficients]] (one variable, \(s=1\)) some \(y^i\) has the largest coefficient of \(z^n\).
2. \(0\le c_C(n)\le1\): the ring \(\mathcal{O}[\![y]\!]\) is stable under differentiation and its elements have integral constant terms (Lean `New.CMLattice.derivative_mem_integralSeriesRing`), so by induction on \(n\) all \(g^{(n)}(0)\) are integral.
3. \(c_C(0)=1\) (take \(g=1\)).

In terms of valuations, \(c_C(n)=p^{-v}\) with \(v\) the least valuation of \(g^{(n)}(0)\).

## References

1. Lean: `New.CMLattice.maxDerivNorm`, `New.CMLattice.exists_isGreatest_norm_deriv`, `New.CMLattice.exists_norm_deriv_eq_maxDerivNorm`, `New.CMLattice.norm_deriv_le_maxDerivNorm`, `New.CMLattice.maxDerivNorm_nonneg`, `New.CMLattice.norm_deriv_le_one`, `New.CMLattice.maxDerivNorm_le_one`, `New.CMLattice.maxDerivNorm_zero` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
